#!/usr/bin/env python3
"""R125 independent verifier.

Independence contract (same discipline as R122/R123/R124):
  * does NOT import R125-ACQUIRE
  * does NOT read any R125-produced JSON as a substantive data source
  * recomputes every claim from raw bytes on disk with its own parsing logic
  * expected values are literals written from direct measurement, not read
    back from the acquisition map or the source manifest

Group A is explicitly a SAME-MACHINE byte-identity consistency check, not an
independent cross-source verification (declared in the output scope_note).
"""
from __future__ import annotations

import difflib
import hashlib
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"
R124 = HERE.parent / "r3r5-R124" / "raw"

checks: list[dict] = []


def _jsonable(v):
    """V2 fix: raw bytes are not JSON-serializable; encode them explicitly."""
    if isinstance(v, bytes):
        return {"__bytes__": v.decode("utf-8", "replace")}
    if isinstance(v, (list, tuple)):
        return [_jsonable(x) for x in v]
    if isinstance(v, dict):
        return {k: _jsonable(x) for k, x in v.items()}
    return v


def ck(group: str, cid: str, desc: str, expected, observed, ok: bool | None = None):
    if ok is None:
        ok = expected == observed
    checks.append({
        "id": f"{group}-{cid}", "group": group, "desc": desc,
        "expected": _jsonable(expected), "observed": _jsonable(observed), "match": bool(ok),
    })


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def raw(name: str) -> bytes:
    return (RAW / name).read_bytes()


# --- Group A: frozen raw-byte identity (same-machine consistency) -----------
EXPECTED_RAW = {
    "api-details-v1.json": (64741, "09abab723319950682fa6ec7ae31de0be1faa42c2b711dd26311c28509e7ceec"),
    "api-jats.json":       (196,   "80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880"),
    "biorxiv-v1-full.xml": (17,    "e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602"),
    "biorxiv-v1-source.xml":  (17, "e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602"),
    "biorxiv-v1-source2.xml": (17, "e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602"),
    "connect-jats.xml":    (58714, "8501cd131ae26cb74f732066cb40f70dc0e8d5432275197e64442923f885db62"),
    "epmc-core.json":      (6367,  "0875d916d4800f2bf9e972d2efe47f4b582fd15aaefeb5c834200988cd4dc9ac"),
    "epmc-fulltext-v2.xml": (150,  "7638ab17cbd5b178781ea8184278412849c3120eb0b953b6a29cfa53fca7a6e7"),
    "epmc-fulltext.xml":   (150,   "c240883c1ab45c19541f1ca4c89abe87ab99e8ff494aedaf99b2f91c0bb5f19c"),
    "jats-v12.xml":        (17,    "e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602"),
    "jats-v3.xml":         (17,    "e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602"),
    "wayback-cdx.json":    (3,     "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570"),
    "wayback-v1.html":     (4657,  "91cc23843494a080580be5f537716ecfb1007091754e50848487d6a0080d48c7"),
}
# Every SHA literal above was measured by a separate `shasum -a 256`
# invocation on the frozen raw files, so all 13 are asserted (not merely
# informational). No hash value in this file is invented.
for name, (size, digest) in sorted(EXPECTED_RAW.items()):
    b = raw(name)
    ck("A", f"size:{name}", "byte count recomputed from raw", size, len(b))
    ck("A", f"sha:{name}", "sha256 recomputed from raw (external shasum literal)",
       digest, sha(b))

ck("A", "count", "number of frozen raw files", 13,
   len([p for p in RAW.iterdir() if p.is_file()]))

# --- Group B: 429 negative evidence, verbatim ------------------------------
BIO429 = ["biorxiv-v1-source.xml", "biorxiv-v1-source2.xml",
          "biorxiv-v1-full.xml", "jats-v3.xml", "jats-v12.xml"]
for name in BIO429:
    b = raw(name)
    ck("B", f"payload:{name}", "exact Cloudflare 1015 body", b"error code: 1015\n", b)
ck("B", "uniform", "all five 429 bodies share one digest", 1,
   len({sha(raw(n)) for n in BIO429}))

# --- Group C: EPMC full-text 500 is structural -----------------------------
lite = json.loads((R124 / "europepmc-search.json").read_bytes())["resultList"]["result"][0]
for key in ["hasPDF", "inEPMC", "inPMC", "isOpenAccess"]:
    ck("C", f"lite:{key}", f"R124 frozen lite metadata {key}", "N", lite.get(key))
ck("C", "lite:firstPublicationDate", "first publication date", "2026-06-12",
   lite.get("firstPublicationDate"))
ck("C", "lite:firstIndexDate", "first index date", "2026-06-15",
   lite.get("firstIndexDate"))
for name in ["epmc-fulltext.xml", "epmc-fulltext-v2.xml"]:
    body = raw(name).decode("utf-8", "replace")
    ck("C", f"500:{name}", "HTTP 500 marker in preserved body", True, '"status":500' in body)
    ck("C", f"path:{name}", "fullTextXML path in preserved body", True,
       "/europepmc/webservices/rest/PPR1251441/fullTextXML" in body)

# --- Group D: EPMC core = third first-hand endpoint -------------------------
core = json.loads(raw("epmc-core.json"))["resultList"]["result"][0]
ck("D", "id", "EPMC record id", "PPR1251441", core.get("id"))
ck("D", "source", "source is preprint", "PPR", core.get("source"))
ck("D", "doi", "DOI matches", "10.64898/2026.06.10.731214", core.get("doi"))
ck("D", "license", "record-level licence", "cc by", core.get("license"))
ck("D", "dateOfCreation", "creation date", "2026-06-15", core.get("dateOfCreation"))
ck("D", "firstPublicationDate", "first publication date", "2026-06-12",
   core.get("firstPublicationDate"))
ck("D", "firstIndexDate", "first index date", "2026-06-15", core.get("firstIndexDate"))
ck("D", "hasPDF", "no PDF", "N", core.get("hasPDF"))
ck("D", "inEPMC", "not in EPMC full text", "N", core.get("inEPMC"))
ftu = core.get("fullTextUrlList", {}).get("fullTextUrl", [])
ck("D", "fullTextUrlCount", "exactly one full-text URL", 1, len(ftu))
ck("D", "fullTextUrlIsDOI", "the only full-text URL is a DOI resolver", True,
   bool(ftu) and "doi.org/10.64898/2026.06.10.731214" in ftu[0].get("url", ""))

ab = core.get("abstractText", "")
api_col = json.loads((R124 / "biorxiv-api-details.json").read_bytes())["collection"]
api_ab = api_col[0]["abstract"]
ck("D", "abstractChars", "EPMC abstract character count", 4847, len(ab))
ck("D", "apiAbstractChars", "bioRxiv API abstract character count", 4816, len(api_ab))
ratio = difflib.SequenceMatcher(None, api_ab, ab).ratio()
ck("D", "abstractSimilarity", "two endpoints carry the same current abstract (ratio > .98)",
   True, ratio > 0.98)
ck("D", "abstractSimilarityValue", "measured ratio rounded to 4dp (informational)",
   "<informational>", round(ratio, 4), ok=True)
for needle in ["largely null result", "disappears entirely", "statistically indistinguishable",
               "size-matched", "not the confirmation we set out to find"]:
    ck("D", f"neg:{needle[:22]}", f"negative wording present: {needle!r}", True,
       needle in ab)
for needle in ["0.686", "0.846", "0.930", "0.603"]:
    ck("D", f"pos:{needle}", f"v1-positive number absent from first-hand bytes: {needle}",
       0, ab.count(needle))

# --- Group E: bioRxiv details API structural facts --------------------------
ck("E", "records", "version record count", 12, len(api_col))
# V3 fix: the API returns `version` as a decimal STRING, not an int.
# V2's expected int list was an expectation assumption error, not a data
# inconsistency. Compare as strings and assert the field type separately.
ck("E", "versions", "version field is the string sequence '1'..'12'",
   [str(i) for i in range(1, 13)], [str(r["version"]) for r in api_col])
ck("E", "versionType", "version field is a JSON string in every record", True,
   all(isinstance(r["version"], str) for r in api_col))
ck("E", "abstracts", "distinct abstracts across records", 1,
   len({r["abstract"] for r in api_col}))
ck("E", "titles", "distinct titles across records", 2,
   len({r["title"] for r in api_col}))
ck("E", "jats", "distinct JATS URLs across 12 records", 10,
   len({r["jatsxml"] for r in api_col}))
ck("E", "licenses", "distinct licence values", 1,
   len({r["license"] for r in api_col}))
ck("E", "licenseValue", "record-level licence value", "cc_by", api_col[0]["license"])
ck("E", "v1date", "v1 date", "2026-06-12", api_col[0]["date"])
ck("E", "v12date", "12th record date", "2026-10-16", api_col[-1]["date"])
ck("E", "v3v4collision", "v3 and v4 publish the same JATS URL", True,
   api_col[2]["jatsxml"] == api_col[3]["jatsxml"])
ck("E", "v8v9collision", "v8 and v9 publish the same JATS URL", True,
   api_col[7]["jatsxml"] == api_col[8]["jatsxml"])
ck("E", "v1title", "v1 title differs from v2+ title", True,
   api_col[0]["title"] != api_col[1]["title"])
ck("E", "abstractSha", "single shared abstract sha256 prefix",
   "555e28f9fef30a3a", sha(api_ab.encode())[:16])

# --- Group F: Wayback / non-existent endpoint negatives --------------------
ck("F", "cdx", "CDX returns empty JSON array", b"[]\n", raw("wayback-cdx.json"))
wb = raw("wayback-v1.html").decode("utf-8", "replace")
ck("F", "waybackMarker", "Wayback 404 page marker", True, "Wayback Machine" in wb)
ck("F", "waybackTitle", "Wayback 404 page title marker", True,
   "<title>Wayback Machine</title>" in wb)
j404 = raw("api-jats.json").decode("utf-8", "replace")
ck("F", "apiJats404", "api.biorxiv.org/jats returns 404 body", True,
   "404 Not Found" in j404)

# --- Group G: byte-identity with R124 frozen bytes -------------------------
ck("G", "connect", "connect page byte-identical to R124 frozen copy", True,
   raw("connect-jats.xml") == (R124 / "connect-biorxiv-relate181.html").read_bytes())
ck("G", "details", "details /1 response byte-identical to R124 details", True,
   raw("api-details-v1.json") == (R124 / "biorxiv-api-details.json").read_bytes())

# --- Group H: scope / safety on the 13 raw files ---------------------------
LOCAL_MARKERS = [b"/Users/", b"/home/", b"C:\\"]
CRED_MARKERS = [b"api_key", b"apikey", b"Bearer ", b"Authorization:", b"secret=",
                b"password", b"credentials.json", b"ghp_", b"sk-"]
all_raw = [raw(p.name) for p in sorted(RAW.iterdir()) if p.is_file()]
hits_local = sum(1 for b in all_raw for m in LOCAL_MARKERS if m in b)
hits_cred = sum(1 for b in all_raw for m in CRED_MARKERS if m in b)
ck("H", "noLocalPath", "zero local absolute path markers in raw bytes", 0, hits_local)
ck("H", "noCredential", "zero credential markers in raw bytes", 0, hits_cred)
ck("H", "maxSize", "largest raw file <= 200 KiB", True,
   max(len(b) for b in all_raw) <= 200 * 1024)
ck("H", "sizeValue", "largest raw file byte count (informational)",
   "<informational>", max(len(b) for b in all_raw), ok=True)
ck("H", "noScoreLine", "zero numeric **Overall:** lines in raw bytes", 0,
   sum(1 for b in all_raw if b"**Overall:**" in b))
ck("H", "noEmail", "zero explicit email literals in raw bytes", 0,
   sum(1 for b in all_raw if b"@" in b and b".com" in b))

# --- Summary ----------------------------------------------------------------
groups: dict[str, dict[str, int]] = {}
for c in checks:
    g = groups.setdefault(c["group"], {"total": 0, "match": 0})
    g["total"] += 1
    g["match"] += int(c["match"])

result = {
    "scope_note": (
        "Group A is a same-machine byte-identity consistency check, not an "
        "independent cross-source verification; the SHA literals asserted "
        "there were measured by a separate `shasum` invocation. Groups B-H "
        "are substantive first-hand observations recomputed from raw bytes. "
        "The verifier does not import R125-ACQUIRE and does not read any "
        "R125-produced JSON as a substantive data source; R124 frozen bytes "
        "are used only as the pre-existing authority for API/EPMC metadata "
        "comparisons (groups C, D, E, G)."
    ),
    "timepoint_note": (
        "HTTP 429 / 500 / 404 / empty-CDX results are scoped to the R125 "
        "acquisition instant and the exact URLs recorded in R125-ACQUIRE.py. "
        "They are not claims of permanent unavailability."
    ),
    "total": len(checks),
    "match": sum(c["match"] for c in checks),
    "mismatch": sum(not c["match"] for c in checks),
    "groups": groups,
    "checks": checks,
}
out = HERE / "R125-VERIFICATION.json"
out.write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"{result['match']}/{result['total']} MATCH, {result['mismatch']} MISMATCH")
print("groups:", json.dumps(groups, ensure_ascii=False))
for c in checks:
    if not c["match"]:
        print("  MISMATCH", c["id"], "expected=", str(c["expected"])[:120],
              "observed=", str(c["observed"])[:120])

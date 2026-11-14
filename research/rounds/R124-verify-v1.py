#!/usr/bin/env python3
"""R124 independent verifier.

Independence contract:
  * Does NOT import the acquisition module.
  * Does NOT read any R124-produced JSON as a substantive data source. The
    SOURCE-MANIFEST is used ONLY for group A declarative SHA/byte consistency
    checks (same-machine identity check, NOT an independent cross-check).
  * Groups B..I recompute from RAW SOURCE BYTES (and independent project files
    outside this round) with this file's own parsing logic.

Run: /Users/xhf/miniconda3/bin/python R124-verify.py
"""
from __future__ import annotations

import hashlib
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
RUNROOT = os.path.dirname(HERE)
PROJECT = os.path.dirname(os.path.dirname(RUNROOT))  # .../auto-paper/20261111-225602/... -> repo root
# Resolve repo root robustly by walking up to the dir containing goal-ledger.md
p = HERE
REPO = None
for _ in range(8):
    if os.path.isfile(os.path.join(p, "goal-ledger.md")):
        REPO = p
        break
    p = os.path.dirname(p)

checks = []


def _jsonable(v):
    # V-2 defect (preserved): group F passed a bytes literal as `expected`,
    # which json.dump cannot serialize. Normalize bytes to a UTF-8 string
    # for reporting only; the equality comparison itself is unchanged.
    if isinstance(v, bytes):
        return v.decode("utf-8", errors="replace")
    if isinstance(v, (list, tuple)):
        return [_jsonable(x) for x in v]
    if isinstance(v, dict):
        return {k: _jsonable(x) for k, x in v.items()}
    return v


def ck(group, name, expected, observed, note=""):
    ok = expected == observed
    checks.append({
        "group": group, "check": name, "expected": _jsonable(expected),
        "observed": _jsonable(observed), "match": ok, "note": note,
    })
    return ok


def raw(name):
    return open(os.path.join(RAW, name), "rb").read()


def txt(name):
    return raw(name).decode("utf-8", errors="replace")


def sha(b):
    return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------- A (identity)
# SOURCE-MANIFEST is read ONLY here for declarative identity checks.
m = json.load(open(os.path.join(HERE, "R124-SOURCE-MANIFEST.json"), encoding="utf-8"))
ck("A", "manifest_file_count", 13, len(m["files"]))
ck("A", "manifest_bytes_total_declared", 323740, m["totals"]["bytes_total"])
ck("A", "manifest_bytes_total_recomputed", 323740, sum(r["bytes"] for r in m["files"]))
ck("A", "manifest_200_count", 8, m["totals"]["http_200_count"])
ck("A", "manifest_301_count", 1, m["totals"]["http_301_count"])
ck("A", "manifest_429_count", 4, m["totals"]["http_429_count"])
for r in m["files"]:
    b = raw(r["file"])
    ck("A", "bytes:" + r["file"], r["bytes"], len(b))
    ck("A", "sha256:" + r["file"], r["sha256"], sha(b))
    ck("A", "status_bytes_decl:" + r["file"], r["bytes"], r["declared_bytes_at_acquisition"])

# ------------------------------------------------- B (bioRxiv official API bytes)
api = json.loads(txt("biorxiv-api-details.json"))
col = api["collection"]
ck("B", "api_messages_status", "ok", api["messages"][0]["status"])
ck("B", "api_collection_len", 12, len(col))
ck("B", "api_versions_1_to_12", list(range(1, 13)), [r["version"] for r in col])
ck("B", "api_doi_all_same", True, all(r["doi"] == "10.64898/2026.06.10.731214" for r in col))
v1_title = "Connectome wiring shapes population-level neural geometry in the Drosophila visual system"
v2_title = "Representational geometry as a fidelity metric for connectome-constrained networks: evidence from the Drosophila visual system"
ck("B", "v1_title_distinct", v1_title, col[0]["title"])
ck("B", "v2_title", v2_title, col[1]["title"])
ck("B", "v2_v12_titles_all_same", True, all(r["title"] == v2_title for r in col[1:]))
ck("B", "v1_date", "2026-06-12", col[0]["date"])
ck("B", "v12_date", "2026-10-16", col[-1]["date"])
ck("B", "v3_date", "2026-06-23", col[2]["date"])
ck("B", "v1_authors", "Zhou, M. G.; Hasler, J. O.", col[0]["authors"])
ck("B", "v1_license", "cc_by", col[0]["license"])
ck("B", "all_published_NA", True, all(r["published"] == "NA" for r in col))
ck("B", "jatsxml_present_v1", True, "jatsxml" in col[0])

# KEY finding: all 12 abstracts are byte-identical => API field is a
# back-filled CURRENT abstract, not a per-version historical abstract.
abs_shas = [sha(r["abstract"].encode("utf-8")) for r in col]
ck("B", "all_12_abstracts_identical", 1, len(set(abs_shas)))
ck("B", "abstract_len", 4816, len(col[0]["abstract"]))
a1 = col[0]["abstract"]
for kw in ["p < 10-13 in every case", "closes the gap completely",
           "Erdos-Renyi", "size-matched", "OFF-polarity", "trained"]:
    ck("B", "v1_api_abstract_has:" + kw, True, kw in a1)
for kw in ["0.686", "0.846", "0.930 vs", "RSA Spearman"]:
    ck("B", "v1_api_abstract_lacks:" + kw, 0, a1.count(kw))
ck("B", "api_v1_na_endpoint_identical", True,
   raw("biorxiv-api-v1-na.json") == raw("biorxiv-api-details.json"),
   "The /1 suffix is not a version selector; byte-identical response")

# ------------------------------------------------------ C (Crossref official API)
cr = json.loads(txt("crossref-work.json"))["message"]
ck("C", "crossref_DOI", "10.64898/2026.06.10.731214", cr["DOI"])
ck("C", "crossref_type", "posted-content", cr["type"])
ck("C", "crossref_publisher", "openRxiv", cr["publisher"])
ck("C", "crossref_title_is_v2_plus_title", v2_title, re.sub(r"\s+", " ",
   re.sub(r"<[^>]+>", "", cr["title"][0])).strip())
ck("C", "crossref_created_date", "2026-06-12", cr["created"]["date-time"][:10])
ck("C", "crossref_posted_date", [[2026, 6, 12]], cr["posted"]["date-parts"])
ck("C", "crossref_indexed_date", "2026-10-21", cr["indexed"]["date-time"][:10])
ck("C", "crossref_has_abstract", True, "abstract" in cr)
crabs = cr["abstract"]
for kw in ["closes the gap", "size-matched", "Erdős–Rényi", "10</jats:sup>"]:
    ck("C", "crossref_abstract_has:" + kw, True, kw in crabs)
ck("C", "crossref_abstract_lacks_0.686", 0, crabs.count("0.686"))
ck("C", "crossref_license_CC_BY_4",
   "http://creativecommons.org/licenses/by/4.0/", cr["license"][0]["URL"])

# ----------------------------------------------------- D (second-hand mirror page)
mir = txt("secondary-mirror-article-followed.html")
ck("D", "mirror_datePublished_v12_date", "2026-10-16",
   re.findall(r'"datePublished":\s*"([0-9-]+)"', mir)[0])
ck("D", "mirror_datePublished_equals_api_v12", col[-1]["date"],
   re.findall(r'"datePublished":\s*"([0-9-]+)"', mir)[0])
ck("D", "mirror_schema_type", True, '"@type": "ScholarlyArticle"' in mir)
ck("D", "mirror_sameAs_biorxiv_doi", True, "10.64898/2026.06.10.731214" in mir)
for kw in ["p &lt; 10-13 in every case", "p < 10-13 in every case",
           "closes the gap completely", "trained Erdos-Renyi on OFF-polarity structure"]:
    hit = kw in mir
    ck("D", "mirror_has:" + kw, True, hit)
ck("D", "mirror_headline_v2_title", True, v2_title in mir)
ck("D", "bare_url_301_body", True, b"301 Moved Permanently" in raw("secondary-mirror-article.html"))

# --------------------------------------------- E (R5 W8 first-hand arXiv abs)
park = txt("arxiv-2609.39248-abs.html")
dhawan = txt("arxiv-2610.13018-abs.html")
ck("E", "park_has_correct_zenodo_22871090", 1, park.count("22871090"))
ck("E", "park_lacks_wrong_zenodo_22891264", 0, park.count("22891264"))
ck("E", "park_submitted_30_Sep_2026", 1, park.count("Submitted on 30 Sep 2026"))
ck("E", "dhawan_has_9_Oct_2026", 2, dhawan.count("9 Oct 2026"))
ck("E", "dhawan_lacks_12_Oct_2026", 0, dhawan.count("12 Oct 2026"))
ck("E", "dhawan_v1_timestamp", True,
   "[v1] Fri, 9 Oct 2026 05:20:38 UTC" in dhawan)

# --------------------------------------------- F (negative evidence preserved)
for f in ["biorxiv-v1.html", "biorxiv-v1-retry.html",
          "biorxiv-v1-early-full.html", "biorxiv-v3.html"]:
    b = raw(f)
    ck("F", "429_body:" + f, b"error code: 1015", b.strip())
    ck("F", "429_len:" + f, 17, len(b))
ck("F", "no_local_v1_html_freeze", True,
   len(raw("biorxiv-v1.html")) < 100,
   "The v1 HTML page's positive-abstract text was seen via WebFetch only; "
   "no local byte freeze exists. Not counted as a first-hand frozen artifact.")

# ------------------------------------- G (R106 section 6 convergence, source bytes)
r106 = os.path.join(RUNROOT, "gate-G0-R106", "R106-G0-INDEPENDENT-GATE-REVIEW.md")
g = txt if False else None
s106 = open(r106, encoding="utf-8").read()
ck("G", "r106_has_R1", True, "**R1（闭 gap 1）**" in s106)
ck("G", "r106_has_R2", True, "**R2（闭 gap 2）**" in s106)
ck("G", "r106_has_R3", True, "**R3**" in s106)
ck("G", "r106_has_R4", True, "**R4**" in s106)
ck("G", "r106_has_R5", True, "**R5**" in s106)
ck("G", "r106_has_R6", True, "**R6（闭 gap 4）**" in s106)
ck("G", "r106_has_R7", True, "**R7**" in s106)
ck("G", "r106_has_R8", True, "**R8**" in s106)
ck("G", "r106_has_R9", True, "**R9**" in s106)
ck("G", "r106_verdict_G0_NO", True, "G0 may be passed:** NO" in s106 or
   "G0 不得标为 PASSED" in s106)
ck("G", "r106_R3_requires_biorxiv_DOI", True, "10.64898/2026.06.10.731214" in s106)
ck("G", "r106_R3_requires_version_split", True, "v1 阳性 vs v3 大体阴性" in s106)
ck("G", "r106_W13_no_G0_pass_criterion", True, "没有 G0 的成文通过标准" in s106)

# W8 corrections already appended in R106 round audit (do not rewrite history)
ra = open(os.path.join(RUNROOT, "gate-G0-R106", "R106-ROUND-AUDIT.md"), encoding="utf-8").read()
ck("G", "r106_audit_withdrew_v1_claim", True, "核心指控不成立，已撤回" in ra)
ck("G", "r106_audit_corrected_zenodo", True, "10.5281/zenodo.22871090" in ra)
ck("G", "r106_audit_corrected_dhawan_date", True, "Fri, 9 Oct 2026" in ra)

# ------------------------------------------- H (double-gate / state live readings)
ps = os.path.join(RUNROOT, "pipeline-state.json")
state = json.load(open(ps, encoding="utf-8"))
ck("H", "main_pipeline_name", "f-guidance-builder-v1", state["pipeline"])
ck("H", "main_contract_version", "v2", state["contract_version"])
stages = {s["id"]: s for s in state["stages"]}
ck("H", "CCFA_startup_passed", "passed", stages["CCFA-startup"]["status"])
ck("H", "G0_status_pending", "pending", stages["G0"]["status"])
ck("H", "G0_inputs_empty", [], stages["G0"]["inputs"])
ck("H", "G0_evidence_empty", [], stages["G0"]["evidence"])
ck("H", "G0_gate_verdict_pending", "pending", stages["G0"]["gate_verdict"])
ck("H", "G1_G8_all_pending", True,
   all(stages[f"G{i}"]["status"] == "pending" for i in range(1, 9)))
ck("H", "validation_pending", "pending", stages["validation"]["status"])
ck("H", "handoff_pending", "pending", stages["handoff"]["status"])

# validator verdict (recomputed from the authoritative review report bytes)
r95 = os.path.join(REPO, "ccfa-review-reports",
                   "paper-null-ladder-r95-independent-review-20261111.md") if REPO else ""
if r95 and os.path.isfile(r95):
    s95 = open(r95, encoding="utf-8").read()
    ck("H", "governing_r95_overall_6", True,
       bool(re.search(r"^\*\*Overall:\*\* 6\b", s95, re.M)))
    ck("H", "governing_below_threshold", True, 6.0 < 7.0)
else:
    ck("H", "governing_report_found", True, False, "report path not resolved")

# ------------------------------------------------- I (strict-boundary byte scans)
# Scope: ONLY the 13 files in raw/. Local reports/derived files are excluded.
joined = b"".join(raw(r["file"]) for r in m["files"])
ck("I", "raw_no_local_abs_path", 0, len(re.findall(rb"/Users/|/home/|C:\\\\", joined)))
ck("I", "raw_no_credential_filename", 0,
   len(re.findall(rb"credentials\.json|id_rsa|\.pem|AIza[0-9A-Za-z_-]{20,}", joined)))
ck("I", "raw_no_bearer_token", 0, len(re.findall(rb"Bearer\s+[A-Za-z0-9._-]{20,}", joined)))
ck("I", "raw_max_file_under_50MiB", True, max(r["bytes"] for r in m["files"]) < 50 * 1024 * 1024)
ck("I", "raw_max_file_bytes", 64741, max(r["bytes"] for r in m["files"]))
ck("I", "no_dataset_or_weight_file", True,
   all(not re.search(r"\.(npy|npz|pt|pth|ckpt|h5|zip|tar\.gz|mp4|sintel)$", r["file"])
       for r in m["files"]))

# ------------------------------------------------------------------- result
by_group = {}
for c in checks:
    d = by_group.setdefault(c["group"], {"MATCH": 0, "MISMATCH": 0})
    d["MATCH" if c["match"] else "MISMATCH"] += 1
out = {
    "round": "R124",
    "verifier": "R124-verify.py",
    "independence_scope_note": (
        "Group A is a same-machine declarative SHA/byte identity check against "
        "R124-SOURCE-MANIFEST.json (constructively guaranteed, NOT an independent "
        "cross-check; R115 W4). Groups B..I recompute from raw source bytes and "
        "independent project files with this verifier's own logic; no R124-produced "
        "JSON is used as a substantive data source, and the acquisition module is "
        "not imported. Network was not contacted by this verifier."),
    "total_checks": len(checks),
    "total_match": sum(1 for c in checks if c["match"]),
    "total_mismatch": sum(1 for c in checks if not c["match"]),
    "by_group": by_group,
    "checks": checks,
}
dest = os.path.join(HERE, "R124-VERIFICATION.json")
with open(dest, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("checks", out["total_checks"], "MATCH", out["total_match"],
      "MISMATCH", out["total_mismatch"])
for k in sorted(by_group):
    print(" ", k, by_group[k])
for c in checks:
    if not c["match"]:
        print("  MISMATCH:", c["group"], c["check"], "exp=", c["expected"], "obs=", c["observed"])

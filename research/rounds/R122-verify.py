#!/usr/bin/env python
"""R122 INDEPENDENT VERIFIER.

Reads ONLY the five raw byte files under raw/. It does NOT import the
acquisition module, does NOT read any R122 JSON as a data source, and does
NOT read the round audit. Every observed value is recomputed from source
bytes with this file's own parsing logic.

Scope note: checks A1-A4 are same-machine byte-identity checks (necessarily
consistent by construction), not independent cross-verification. Checks B-E
are the substantive first-hand observations.
"""
import os, re, html, json, hashlib, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")


def rd(name):
    with open(os.path.join(RAW, name), "rb") as f:
        return f.read()


def plain(b):
    s = b.decode("utf-8", "replace")
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def meta(s, name):
    m = re.search(r'<meta\s+name="' + re.escape(name) + r'"\s+content="([^"]*)"', s)
    return html.unescape(m.group(1)).strip() if m else None


def abs_block(s):
    m = re.search(r'<blockquote[^>]*class="abstract[^"]*"[^>]*>(.*?)</blockquote>', s, re.S | re.I)
    if not m:
        return None
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).strip()
    return re.sub(r"^Abstract:\s*", "", t)


def body_abstract(p):
    i = p.find("September 2026 Abstract.")
    if i < 0:
        return None
    seg = p[i + len("September 2026 Abstract."):]
    ends = [e for e in (seg.find("1 Introduction"), seg.find("Keywords")) if e > 0]
    end = min(ends) if ends else 1800
    return seg[:end].strip()


CHECKS = []


def chk(cid, desc, expected, observed, match=None):
    if match is None:
        match = expected == observed
    CHECKS.append({"id": cid, "desc": desc, "expected": expected,
                   "observed": observed, "match": bool(match)})


FILES = {
    "v1-abs":  "arxiv-2609.24565v1-abs.html",
    "v2-abs":  "arxiv-2609.24565v2-abs.html",
    "v1-html": "arxiv-2609.24565v1-html.html",
    "v2-html": "arxiv-2609.24565v2-html.html",
    "api":     "arxiv-2609.24565-api.xml",
}
B = {k: rd(v) for k, v in FILES.items()}
S = {k: v.decode("utf-8", "replace") for k, v in B.items()}
P = {k: plain(v) for k, v in B.items()}

# --- A: byte identity (same-machine, structural) ---
for k in FILES:
    b = B[k]
    chk("A1-" + k, "sha256 recomputed from raw bytes", sha256(b), sha256(rd(FILES[k])))
    chk("A2-" + k, "size recomputed from raw bytes", len(b), os.path.getsize(os.path.join(RAW, FILES[k])))
chk("A3", "all five raw files are non-empty", True, all(len(x) > 1000 for x in B.values()))
chk("A4", "html files are HTML, api is XML", True,
    all(S[k].lstrip().lower().startswith("<!doctype html") for k in ("v1-abs", "v2-abs", "v1-html", "v2-html"))
    and S["api"].lstrip().startswith("<?xml"))

# --- B: titles and versions ---
t1, t2 = meta(S["v1-abs"], "citation_title"), meta(S["v2-abs"], "citation_title")
chk("B1", "v1 abs title starts 'Active Visual Sampling'", True,
    bool(t1 and t1.startswith("Active Visual Sampling")))
chk("B2", "v2 abs title starts 'What Survives on Real Drawings'", True,
    bool(t2 and t2.startswith("What Survives on Real Drawings")))
chk("B3", "v1 and v2 titles differ", True, t1 != t2)
d1, d2 = meta(S["v1-abs"], "citation_date"), meta(S["v2-abs"], "citation_date")
chk("B4", "both abs pages report the same citation_date (2026/09/21)", "2026/09/21", d1, d1 == d2 == "2026/09/21")

# --- C: atom feed version identity ---
feed_head = S["api"][:S["api"].find("<entry>")]
entry = S["api"][S["api"].find("<entry>"):]


def tag(s, name):
    m = re.search(r"<" + re.escape(name) + r"[^>]*>(.*?)</" + re.escape(name) + r">", s, re.S)
    return re.sub(r"\s+", " ", html.unescape(m.group(1))).strip() if m else None


e_id, e_title = tag(entry, "id"), tag(entry, "title")
e_pub, e_upd = tag(entry, "published"), tag(entry, "updated")
e_sum = tag(entry, "summary")
f_upd = tag(feed_head, "updated")
chk("C1", "atom entry id points to v2", "http://arxiv.org/abs/2609.24565v2", e_id)
chk("C2", "atom entry title equals v2 abs citation_title", True, e_title == t2)
chk("C3", "entry published date", "2026-09-21T13:30:30Z", e_pub)
chk("C4", "entry updated date", "2026-09-22T12:24:47Z", e_upd)
chk("C5", "feed-level updated is a QUERY timestamp, distinct from entry updated", True,
    bool(f_upd and f_upd.startswith("2026-11-14") and f_upd != e_upd))
chk("C6", "entry published < entry updated", True, e_pub < e_upd)

# --- D: the two v2 abstracts (core R4 finding) ---
a1, a2 = abs_block(S["v1-abs"]), abs_block(S["v2-abs"])
ba = body_abstract(P["v2-html"])
chk("D1", "v2 abs abstract equals atom summary (verbatim)", True, a2 == e_sum)
chk("D2", "v1 and v2 abs abstracts differ", True, a1 != a2)
chk("D3", "v2 HTML body abstract differs from v2 abs abstract", True, ba is not None and ba != a2)
ratio = round(difflib.SequenceMatcher(None, a2 or "", ba or "").ratio(), 4)
chk("D4", "similarity between the two v2 abstracts is below 0.6", True, ratio < 0.6)
chk("D5", "v2 abs abstract length", 1534, len(a2 or ""))
chk("D6", "v2 HTML body abstract length", 1943, len(ba or ""))
chk("D7", "v1 abs abstract length", 1433, len(a1 or ""))

# --- E: G4 positioning needles in v2 body (from raw bytes) ---
needles = {
    "E1": ("7.3 The stimulus never completes a cycle", 2),
    "E2": ("What the sampling sweep answered", 2),
    "E3": ("What remains open", 2),
    "E4": ("Two gaps remain.", 1),
    "E5": ("+0.033", 2),
    "E6": ("[0.015,0.050]", 2),
    "E7": ("T4/T5", 4),
    "E8": ("0.271", 3),
    "E9": ("0.356", 3),
    "E10": ("721", 5),
    "E11": ("1,876", 5),
    "E12": ("0.505", 2),
    "E13": ("0.415", 3),
    "E14": ("9 Limitations", 2),
}
for cid, (n, minc) in needles.items():
    c = P["v2-html"].count(n)
    chk(cid, "v2 body contains %r at least %d times" % (n, minc), True, c >= minc)
chk("E15", "v2 body has more section headings than v1 body", True,
    len(re.findall(r"<h[1-4][^>]*>", S["v2-html"], re.I)) > len(re.findall(r"<h[1-4][^>]*>", S["v1-html"], re.I)))
chk("E16", "v2 html byte size exceeds v1 html byte size", True, len(B["v2-html"]) > len(B["v1-html"]))

# --- F: sanitization gate (what must NOT leave this machine) ---
allbytes = b"".join(B.values())
chk("F1", "no local absolute path in any raw byte file", True, b"/Users/xhf/" not in allbytes)
chk("F2", "no credential-like token in raw byte files", True,
    not re.search(rb"(?i)(bearer\s+[a-z0-9]{20,}|ghp_[a-z0-9]{20,}|api[_-]?key\s*[:=])", allbytes))

result = {
    "scope_note": "A1-A4 are same-machine byte-identity checks, not independent cross-verification. B-F are substantive first-hand observations recomputed from raw bytes.",
    "total": len(CHECKS),
    "match": sum(1 for c in CHECKS if c["match"]),
    "mismatch": sum(1 for c in CHECKS if not c["match"]),
    "abstract_similarity": ratio,
    "observations": {
        "v1_abs_title": t1, "v2_abs_title": t2,
        "v1_abs_abstract_chars": len(a1 or ""), "v2_abs_abstract_chars": len(a2 or ""),
        "v2_body_abstract_chars": len(ba or ""),
        "atom_entry_id": e_id, "atom_published": e_pub, "atom_updated": e_upd,
        "atom_feed_updated_query_time": f_upd,
    },
    "checks": CHECKS,
}
with open(os.path.join(HERE, "R122-VERIFICATION.json"), "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(json.dumps({k: result[k] for k in ("total", "match", "mismatch", "abstract_similarity")}, indent=2))
for c in CHECKS:
    if not c["match"]:
        print("MISMATCH", c["id"], c["desc"], "expected=", str(c["expected"])[:120], "observed=", str(c["observed"])[:120])

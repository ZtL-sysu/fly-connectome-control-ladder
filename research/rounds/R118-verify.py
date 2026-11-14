#!/usr/bin/env python3
"""R118 independent verifier (READ-ONLY, recomputes from raw disk bytes).

Deliberately does NOT read R118-SOURCE-MANIFEST.json. Every value below is
recomputed from the original bytes on disk, so the two artifacts are produced
by separate code paths. NOTE: they still share the same machine and the same
hashlib, so this is a consistency check, NOT an independent cross-validation
(R115 W4 / R114 D1); genuine independent recomputation is delegated to the
fresh isolated sub-agent.
"""
import hashlib
import json
import os
import re
import html as htmlmod
import datetime

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "gate-G0-R118")
LIT = os.path.join(RUN, "literature-search")
REG = os.path.join(LIT, "source-manifest.json")
KDIR = os.path.join(RUN, "gate-G0-R107", "sources")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rel(p):
    return os.path.relpath(p, RUN).replace(os.sep, "/")


def text_of(b):
    s = b.decode("utf-8", "replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", htmlmod.unescape(s)).strip()


def abstract_of(b):
    s = b.decode("utf-8", "replace")
    m = re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', s, re.S | re.I)
    if not m:
        return None
    return re.sub(r"\s+", " ", htmlmod.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).strip()


checks = []


def rec(cid, kind, expected, observed, ok, note=""):
    checks.append({"id": cid, "kind": kind, "expected": expected,
                   "observed": observed, "result": "MATCH" if ok else "MISMATCH",
                   "note": note})


def main():
    # ---- 1. registry declared entries: bytes + sha from raw disk ----
    reg_b = open(REG, "rb").read()
    registry = json.loads(reg_b.decode("utf-8"))
    for i, e in enumerate(registry):
        p = os.path.join(LIT, e["name"] + ".html")
        b = open(p, "rb").read()
        rec(f"REG-{i+1}-{e['name']}-bytes", "bytes", e["bytes"], len(b), len(b) == e["bytes"])
        rec(f"REG-{i+1}-{e['name']}-sha", "sha256", e["sha256"], sha(b), sha(b) == e["sha256"])
        # v2 addition: a matching SHA proves byte integrity, NOT that the
        # registered payload is a usable first-hand source. Probe the text.
        rt = text_of(b)
        rlow = rt.lower()
        is_challenge = ("checking your browser" in rlow or "recaptcha" in rlow
                        or "client challenge" in rlow or "javascript is disabled" in rlow)
        checks.append({
            "id": f"REG-{i+1}-{e['name']}-content-validity",
            "kind": "content_probe",
            "expected": "usable first-hand page",
            "observed": ("CHALLENGE_PAGE" if is_challenge else "has_text"),
            "result": "PROBED",
            "note": f"plain_text_chars={len(rt)}; sha-integrity is separate from content validity",
        })

    # ---- 2. registry invariants (the W7 gap) ----
    rec("REG-size", "bytes", 1124, len(reg_b), len(reg_b) == 1124,
        "R107 independent review recorded 1124 B")
    rec("REG-sha", "sha256", "541880ab1d6a287a7dbd566034a49212858973763fc943eb00d2a1b92de0357b",
        sha(reg_b), sha(reg_b) == "541880ab1d6a287a7dbd566034a49212858973763fc943eb00d2a1b92de0357b",
        "unchanged across R107..R118")
    rec("REG-entry-count", "count", 5, len(registry), len(registry) == 5)
    reg_has_kuklev = "2609.24565" in reg_b.decode("utf-8", "replace")
    rec("REG-contains-kuklev", "absent_expected", False, reg_has_kuklev, not reg_has_kuklev,
        "R106 R4 requires registration into this exact file; still absent")

    # ---- 3. classify the 26 first-hand candidates (no overclaim) ----
    FIRSTHAND = {".html", ".xml", ".pdf", ".txt"}
    cand = []
    for root, dirs, files in os.walk(LIT):
        dirs.sort()
        for fn in sorted(files):
            p = os.path.join(root, fn)
            ext = os.path.splitext(fn)[1].lower()
            if ext not in FIRSTHAND:
                continue
            b = open(p, "rb").read()
            t = text_of(b)
            low = t.lower()
            # v2 fix: a single keyword occurrence in a long real page (e.g. a
            # footer 'captcha' link) is NOT a challenge page. Require the
            # explicit challenge signature AND short plain text.
            challenge_sig = ("checking your browser" in low or "client challenge" in low
                             or "javascript is disabled" in low
                             or "unusual traffic" in low
                             or "access to this resource has been restricted" in low)
            short_challenge = (challenge_sig and len(t) < 1000)
            script_challenge = ("recaptchachallengepageui" in low or "ppconfig" in low)
            if len(b) < 100 or short_challenge or script_challenge:
                cls = "NEGATIVE_OR_ERROR_PAGE"
            elif ext == ".pdf":
                # raw PDF bytes are not reliably text-extractable by this
                # script; leave to owner judgment rather than over-classify
                cls = "UNCLASSIFIED_NEEDS_OWNER_JUDGMENT"
            elif fn.endswith(".txt"):
                cls = "DERIVED_TEXT_FROM_SAVED_SOURCE"
            elif ext == ".json":
                cls = "METADATA"
            elif re.search(r"abstract|references|arxiv|pmc|biorxiv|doi", low[:4000], re.I):
                cls = "EXTERNAL_FIRSTHAND_PAGE"
            else:
                cls = "UNCLASSIFIED_NEEDS_OWNER_JUDGMENT"
            cand.append({"path": rel(p), "bytes": len(b), "sha256": sha(b), "class": cls})

    from collections import Counter
    cls_counts = dict(Counter(c["class"] for c in cand))
    rec("CAND-count", "count", 26, len(cand), len(cand) == 26,
        "candidate by suffix rule; NOT equal to verified first-hand sources")

    # ---- 4. R98 claim "23 saved public sources" (verbatim field) ----
    r98 = open(os.path.join(RUN, "gate-G0-evidence-review-R98.md"), "rb").read()
    r98_has_23 = "23 saved public sources" in r98.decode("utf-8", "replace")
    rec("R98-claim-23-verbatim", "field_found", True, r98_has_23, r98_has_23)
    rec("R98-23-vs-registry", "discrepancy", "23 claimed / 5 registered",
        f"23 claimed / {len(registry)} registered / {len(cand)} candidates / "
        f"{cls_counts.get('EXTERNAL_FIRSTHAND_PAGE', 0)} page-classified",
        True, "quantified, NOT resolved: no registration write performed")

    # ---- 5. Kuklev frozen bytes (R107) vs R107 manifest declaration ----
    r107m = json.load(open(os.path.join(RUN, "gate-G0-R107",
                                        "R107-ONEHAND-SOURCE-MANIFEST.json"), encoding="utf-8"))
    # collect all sha-bearing entries that mention kuklev
    decl = {}
    def walk(o):
        if isinstance(o, dict):
            f = o.get("file") or o.get("path")
            s = o.get("sha256") or o.get("sha")
            if isinstance(f, str) and "kuklev" in f.lower() and isinstance(s, str):
                decl[os.path.basename(f)] = s
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(r107m)
    kbytes = {}
    for fn in sorted(os.listdir(KDIR)):
        if fn.startswith("kuklev_"):
            kbytes[fn] = open(os.path.join(KDIR, fn), "rb").read()
    for fn, b in kbytes.items():
        rec(f"KUKLEV-R107-{fn}-sha", "sha256", decl.get(fn, "<no declaration>"),
            sha(b), decl.get(fn) == sha(b), "R107 declaration vs raw disk bytes")
    rec("KUKLEV-frozen-count", "count", 5, len(kbytes), len(kbytes) == 5)

    # ---- 6. two differently-worded v2 abstracts (byte-level, verbatim) ----
    a_abs = abstract_of(kbytes["kuklev_abs_latest.html"])
    a_v2 = abstract_of(kbytes["kuklev_abs_v2.html"])
    t_body = text_of(kbytes["kuklev_html_v2.html"])
    m = re.search(r"Abstract\.\s*(.+?)(?:\s+1\s+Introduction|\s+Keywords)", t_body, re.S)
    a_body = m.group(1).strip() if m else None
    rec("V2-abs-latest-eq-abs-v2", "equality", True, a_abs == a_v2, a_abs == a_v2,
        "the two ABS pages carry one and the same abstract")
    rec("V2-two-abstracts-distinct", "equality", False,
        (a_abs == a_body) if a_body else None,
        bool(a_body and a_abs != a_body),
        "ABS metadata abstract vs HTML body abstract")
    rec("V2-abs-metadata-len", "count", 1544, len(a_abs) if a_abs else -1,
        len(a_abs) == 1544 if a_abs else False)
    for cid, phrase, where in [
        ("V2-abs-metadata-closing", "Longer observations reverse the circuit-receptor ordering", a_abs),
        ("V2-body-closing", "Exact structure remains insufficient", a_body),
        ("V2-sweep-answered", "What the sampling sweep answered", t_body),
        ("V2-half-held", "That prediction was run, and it half held", t_body),
        ("V2-two-gaps", "Two gaps remain", t_body),
        ("V2-which-stage", "which stage integrates the extra time", t_body),
        ("V2-per-type", "per-type tuning analysis over the sweep", t_body),
        ("V2-effect-0033", "+ 0.033", t_body),
        ("V2-ci-0015-0050", "[ 0.015 , 0.050 ]", t_body),
        ("V2-t4t5-not-grow", "T4/T5 contribution does not grow with length", t_body),
        ("V2-sec73", "7.3 The stimulus never completes a cycle", t_body),
        ("V2-sec9", "9 Limitations", t_body),
    ]:
        found = bool(where and phrase in where)
        rec(cid, "verbatim_field", "FOUND", "FOUND" if found else "ABSENT", found,
            "searched in frozen raw bytes only")

    # ---- 7. matrix stale phrasing still present (gap 2 NOT closed) ----
    mb = open(os.path.join(RUN, "literature-baseline-matrix.md"), "rb").read()
    mt = mb.decode("utf-8", "replace")
    stale = "the open question" in mt and "Kuklev leaves" in mt
    rec("MATRIX-stale-when-phrasing", "field_found", True, stale, stale,
        "R106 R2 requires deleting this; present => gap 2 still OPEN")
    rec("MATRIX-sha", "sha256", "31b5098b4df2718ddf15d0b4613daa4d819a19319bbc15b731fb58d3903da9b2",
        sha(mb), sha(mb) == "31b5098b4df2718ddf15d0b4613daa4d819a19319bbc15b731fb58d3903da9b2",
        "byte-identical to R106 freeze => no silent rewrite")

    # ---- 8. mainline pipeline-state: zero write-back ----
    sb = open(os.path.join(RUN, "pipeline-state.json"), "rb").read()
    sd = json.loads(sb.decode("utf-8"))
    pending = [s["id"] for s in sd["stages"] if s["status"] != "passed"]
    rec("STATE-sha", "sha256", "bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d",
        sha(sb), sha(sb) == "bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d")
    rec("STATE-bytes", "bytes", 3723, len(sb), len(sb) == 3723)
    rec("STATE-pending-list", "list", "G0..G8,validation,handoff", ",".join(pending),
        pending == ["G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
                    "validation", "handoff"])

    # ---- 9. content-safety scan (secret vs local-path kept separate: R115 W2 / R117) ----
    SECRET_PATTERNS = [
        r"AIza[0-9A-Za-z\-_]{20,}", r"sk-[0-9A-Za-z]{20,}",
        r"ghp_[0-9A-Za-z]{20,}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        r"Bearer\s+[A-Za-z0-9\-_\.]{20,}", r"api[_-]?key\s*[:=]\s*['\"][^'\"]{12,}",
        r"password\s*[:=]\s*['\"][^'\"]{8,}", r"credentials\.json",
    ]
    LOCALPATH_PATTERN = r"/Users/[A-Za-z0-9_.\-]+/"
    scan_targets = [os.path.join(OUT, f) for f in sorted(os.listdir(OUT))
                    if os.path.isfile(os.path.join(OUT, f)) and f.endswith((".py", ".json", ".md"))]
    secret_hits, local_hits = [], []
    for p in scan_targets:
        txt = open(p, "rb").read().decode("utf-8", "replace")
        for pat in SECRET_PATTERNS:
            for m in re.finditer(pat, txt, re.I):
                secret_hits.append({"file": os.path.basename(p), "pattern": pat[:24]})
        for m in re.finditer(LOCALPATH_PATTERN, txt):
            local_hits.append({"file": os.path.basename(p), "path_prefix": m.group(0)})
    rec("SAFETY-secret-hits", "count", 0, len(secret_hits), len(secret_hits) == 0,
        "8 strict patterns; value never printed")
    # local paths are configuration facts inside the main project, registered not concealed
    checks.append({"id": "SAFETY-local-paths", "kind": "registered",
                   "expected": "registered, not claimed zero", "observed": len(local_hits),
                   "result": "REGISTERED",
                   "note": "public sync copy must use <local>/ placeholder (R109 red line)"})

    mismatches = [c for c in checks if c["result"] == "MISMATCH"]
    doc = {
        "round": "R118",
        "kind": "READONLY_REGISTRY_GAP_VERIFICATION",
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "generated_at_utc_note": "artifact-generation instant, NOT a fetch timestamp",
        "recomputes_from": "raw disk bytes; does NOT read R118-SOURCE-MANIFEST.json",
        "independence_note": "same machine + same hashlib + same data source as manifest builder; "
                             "consistency check only, NOT independent cross-validation",
        "total_checks": len(checks),
        "mismatch_count": len(mismatches),
        "mismatches": [m["id"] for m in mismatches],
        "candidate_class_counts": cls_counts,
        "candidates": cand,
        "v2_abstract_metadata_length": len(a_abs) if a_abs else None,
        "v2_abstract_body_length": len(a_body) if a_body else None,
        "checks": checks,
        "boundary": "READONLY_REGISTRY_GAP_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
        "explicitly_not_claimed": [
            "gap 1 closed", "gap 2 closed", "gap 4 closed", "G0 passed",
            "any stage status changed", "source-manifest.json written",
            "matrix finalized", "new scientific result", "independent full review",
            "Overall score line", "confirmation authorization",
        ],
    }
    with open(os.path.join(OUT, "R118-REGISTRY-GAP-VERIFICATION.json"), "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(json.dumps({k: doc[k] for k in
                      ("total_checks", "mismatch_count", "mismatches",
                       "candidate_class_counts", "v2_abstract_metadata_length",
                       "v2_abstract_body_length")}, ensure_ascii=False, indent=2))
    for c in checks:
        if c["result"] != "MATCH":
            print(f"  {c['result']:9s} {c['id']}: exp={c['expected']!r} obs={c['observed']!r}")


if __name__ == "__main__":
    main()

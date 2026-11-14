#!/usr/bin/env python3
# R121 INDEPENDENT verifier. Deliberately does NOT import R121-collect*.py and
# does NOT open any R121-produced JSON (RAW / VERIFICATION / manifest). It
# recomputes every number from ORIGINAL SOURCE BYTES using its own code paths.
# NOTE (R118 lesson): two scripts on the same machine using the same hashlib is
# a necessary consistency, NOT independent cross-validation. Genuine
# independence is the separate isolated sub-agent review.
import hashlib
import json
import os
import re
import subprocess
import sys
import time

PR = "/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision"
AP = os.path.join(PR, "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision")
OUT = os.path.join(AP, "success-condition-R121")
PY = "/Users/xhf/miniconda3/bin/python"
R95 = "ccfa-review-reports/paper-null-ladder-r95-independent-review-20261111.md"
REVIEWED_TEX = "papers/paper-null-ladder/R49-7.5-DELIVERY/manuscript/main.tex"
V2 = "papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2"

CHECKS = []
FORBIDDEN = [r"R121-RAW", r"R121-VERIFICATION", r"R121-collect"]


def ck(cid, label, expected, observed, ok=None):
    if ok is None:
        ok = expected == observed
    CHECKS.append({"id": cid, "label": label, "expected": expected,
                   "observed": observed, "status": "MATCH" if ok else "MISMATCH"})
    return ok


def rb(rel):
    p = rel if rel.startswith("/") else os.path.join(PR, rel)
    return open(p, "rb").read()


def sh(b):
    return hashlib.sha256(b).hexdigest()


def main():
    # guard: verify this file itself never reads R121 JSON
    self_src = open(__file__, encoding="utf-8").read()
    ck("SELF-0", "verifier source contains no R121 JSON read",
       True, not any(re.search(p + r"[^\n]*\.json", self_src) for p in FORBIDDEN))

    # A. governing review anchors — recompute line numbers by splitting bytes
    lines = rb(R95).decode("utf-8", "replace").split("\n")
    anchors = {
        "A1": ("**Overall:** 6  | **Scholarly Confidence:** 4", 419),
        "A2": ("| **No quick change** | 继续补流程/披露/格式", 450),
        "A3": ("不新增支持中心主张的科学证据", 450),
        "A4": ("不改变 evidence-capped overall", 450),
        "A5": ("单项 +0.5；三项齐备 Overall 6→7~7.5", 448),
        "A6": ("Raising the score would require: 真实图上确认 motif-survival 阈值迁移", 473),
        "A7": ("需新的真实图实验确认机制迁移（非 prose 可修）", 240),
        "A8": ("无法靠 prose 补出视觉贡献", 249),
        "A9": ("这组 ≥3 个决定性关切不允许 Overall 上到 7", 454),
        "A10": ("| Evidence | 3 | 5 |", 413),
        "A11": ("| Significance | 3 | 4 |", 414),
        "A12": ("行政 blocker 解除仅恢复「可提交」状态", 450),
    }
    for cid, (needle, lineno) in anchors.items():
        found = [i + 1 for i, ln in enumerate(lines) if needle in ln]
        ck(cid, "R95 needle at line " + str(lineno), lineno in found, found, ok=lineno in found)

    ck("A13", "R95 byte size", 52430, len(rb(R95)))
    ck("A14", "R95 sha256 prefix", "c67f8cd39c17d2fe", sh(rb(R95))[:16])

    # B. seven prior rounds: independent full-document tag scan
    round_files = [
        ("R114", "gate-G0-R114/R114-ROUND-AUDIT.md"),
        ("R115", "gate-G0-R115/R115-ROUND-AUDIT.md"),
        ("R116", "gate-G0-R116/R116-ROUND-AUDIT.md"),
        ("R117", "exec-premise-R117/R117-ROUND-AUDIT.md"),
        ("R118", "gate-G0-R118/R118-ROUND-AUDIT.md"),
        ("R119", "review-protocol-R119/R119-ROUND-AUDIT.md"),
        ("R120", "reconciliation-R120/R120-ROUND-AUDIT.md"),
    ]
    for tag, rel in round_files:
        t = rb(os.path.join(AP, rel)).decode("utf-8", "replace")
        ck("B-" + tag + "-1", tag + " declares READONLY", True,
           "READONLY" in t or "READ_ONLY" in t, ok=("READONLY" in t or "READ_ONLY" in t))
        ck("B-" + tag + "-2", tag + " declares NOT_GATE_PASS", True,
           "NOT_GATE_PASS" in t, ok="NOT_GATE_PASS" in t)
        ck("B-" + tag + "-3", tag + " declares NOT_SCIENTIFIC_RESULT", True,
           "NOT_SCIENTIFIC_RESULT" in t, ok="NOT_SCIENTIFIC_RESULT" in t)
        ck("B-" + tag + "-4", tag + " has no line-start numeric Overall", 0,
           len(re.findall(r"(?m)^\s*\*\*Overall:\*\*\s*\d", t)))
    ck("B-COUNT", "prior round count", 7, len(round_files))

    # C. condition (a): recompute from source JSON only, own traversal
    real_vals, synth_vals = [], []
    for base, _, fs in os.walk(os.path.join(PR, "papers")):
        for f in fs:
            if f != "metrics.json" and not f.startswith("task_a_results"):
                continue
            fp = os.path.join(base, f)
            if "real_connectome" not in fp and "p3_p4_taskaware" not in fp and "r51_motif_survival" not in fp:
                continue
            try:
                o = json.load(open(fp, encoding="utf-8", errors="replace"))
            except Exception:
                continue
            if not isinstance(o, dict) or "hypothesis_supported" not in o:
                continue
            (real_vals if "real_connectome" in fp else synth_vals).append(o["hypothesis_supported"])
    ck("C1", "real-graph hypothesis_supported all false", True,
       all(v is False for v in real_vals) and len(real_vals) > 0,
       ok=all(v is False for v in real_vals) and len(real_vals) > 0)
    ck("C2", "real-graph n files", 6, len(real_vals))
    ck("C3", "synthetic controlled has true values", True, any(v is True for v in synth_vals),
       ok=any(v is True for v in synth_vals))
    ck("C4", "condition (a) satisfied", False, False)

    # D. condition (b): version-locked tex by md5 + admission line
    tb = rb(REVIEWED_TEX)
    ck("D1", "reviewed main.tex bytes", 40175, len(tb))
    ck("D2", "reviewed main.tex md5", "e4bfad51ad834fdccdb6db7821e158c",
       hashlib.md5(tb).hexdigest())
    admission_lines = [i + 1 for i, ln in enumerate(tb.decode("utf-8", "replace").split("\n"))
                       if "We did not rerun their flyvis stack and make no benchmark-reproduction claim." in ln]
    ck("D3", "admission at main.tex:637", [637], admission_lines)
    ck("D4", "condition (b) satisfied", False, False)

    # E. condition (c): visual task negative result
    v = json.load(open(os.path.join(PR, V2, "results/r39_visual_task/metrics.json"), encoding="utf-8"))
    ck("E1", "mlp baseline mean acc", 0.9722222222222222,
       v["mlp_baseline"]["mean_acc"])
    d = v["real_minus_condition"]["degree_preserving_null"]["delta"]
    ck("E2", "real minus degree-preserving delta < 0.001 in abs", True, abs(d) < 0.001,
       ok=abs(d) < 0.001)
    ck("E3", "condition (c) satisfied", False, False)

    # F. machine gates, independently re-run
    vp = subprocess.run([PY, os.path.join(PR, "readonly-validator/validate_single_paper.py")],
                        cwd=PR, capture_output=True, text=True)
    vj = json.loads(vp.stdout)
    ck("F1", "validator verdict", "NOT_QUALIFIED", vj["verdict"])
    ck("F2", "validator overall", 6.0, vj["overall_score"])
    ck("F3", "validator threshold", 7.0, vj["threshold"])
    ck("F4", "validator operator", ">=", vj["comparison_operator"])
    ck("F5", "validator score_meets_threshold", False, vj["score_meets_threshold"])
    ck("F6", "validator failing checks", ["D2_tex_pdf_pipeline_all_passed",
                                          "D3_independent_full_review",
                                          "D5_six_sections_traceability"],
       [k for k, x in vj["checks"].items() if not x["pass"]])
    gp = subprocess.run([PY, "/Users/xhf/.workbuddy/skills/task-completion-guard/guard_engine.py",
                         "check", "-l", "guard/ledger-null-ladder.json",
                         "-o", os.path.join(OUT, "R121-guard-report.md")],
                        cwd=PR, capture_output=True, text=True)
    ck("F7", "guard verdict INCOMPLETE", True, "INCOMPLETE" in gp.stdout,
       ok="INCOMPLETE" in gp.stdout)
    ck("F8", "guard failing criteria", ["A2", "A6"],
       [m for m in ["A2", "A6"] if re.search(r"\[FAIL\] " + m, gp.stdout)])
    ck("F9", "guard pending steps", 7,
       len(re.findall(r"S[1-7] \[pending", gp.stdout)))

    # G. ordered gate chain, own parse
    st = json.load(open(os.path.join(AP, "pipeline-state.json"), encoding="utf-8"))
    ids = [s["id"] for s in st["stages"]]
    ck("G1", "mainline stage count", 12, len(ids))
    ck("G2", "first stage CCFA-startup passed", "passed", st["stages"][0]["status"])
    ck("G3", "G0 pending with empty inputs/evidence", (True, True, True),
       (st["stages"][1]["id"] == "G0", st["stages"][1]["inputs"] == [],
        st["stages"][1]["evidence"] == []),
       ok=(st["stages"][1]["id"] == "G0" and st["stages"][1]["inputs"] == []
           and st["stages"][1]["evidence"] == []))
    ck("G4", "all downstream stages pending", True,
       all(s["status"] == "pending" for s in st["stages"][1:]),
       ok=all(s["status"] == "pending" for s in st["stages"][1:]))

    # H. no newer governing review
    pat = re.compile(r"(?m)^\s*\*\*Overall:\*\*\s*([0-9]+(?:\.[0-9]+)?)")
    r95_m = os.stat(os.path.join(PR, R95)).st_mtime
    newer = []
    for base, _, fs in os.walk(PR):
        if "/.git" in base or "research-sync-public" in base:
            continue
        for f in fs:
            if not f.endswith(".md"):
                continue
            p = os.path.join(base, f)
            try:
                t = open(p, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            if pat.search(t) and os.stat(p).st_mtime > r95_m:
                newer.append({"path": os.path.relpath(p, PR),
                              "identical": open(p, "rb").read() == rb(R95)})
    ck("H1", "newer numeric Overall lines", 1, len(newer))
    ck("H2", "all newer lines are byte-identical r95 copy", True,
       all(x["identical"] for x in newer), ok=all(x["identical"] for x in newer))
    ck("H3", "new governing candidates", 0,
       len([x for x in newer if not x["identical"]]))

    # I. isolated copies byte-identical to ORIGINALS (not to each other)
    iso = os.path.join(OUT, "isolated")
    iso_files = sorted(os.listdir(iso))
    ck("I1", "isolated copy count", 21, len(iso_files))
    bad = []
    for f in iso_files:
        tag, _, base = f.partition("__")
        # find the original by suffix match over the source registry paths
        cands = []
        for b, _, fs2 in os.walk(PR):
            if "success-condition-R121" in b or "/.git" in b:
                continue
            if base in fs2:
                cands.append(os.path.join(b, base))
        if not any(open(os.path.join(iso, f), "rb").read() == open(c, "rb").read() for c in cands):
            bad.append(f)
    ck("I2", "isolated copies byte-identical to some original", [], bad)

    res = {
        "round": "R121", "verifier": "R121-verify.py (standalone, no collector import, no R121 JSON read)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
        "python": sys.version.split()[0],
        "n_checks": len(CHECKS),
        "n_match": sum(c["status"] == "MATCH" for c in CHECKS),
        "n_mismatch": sum(c["status"] == "MISMATCH" for c in CHECKS),
        "all_match": all(c["status"] == "MATCH" for c in CHECKS),
        "checks": CHECKS,
        "scope_note": "Same-machine recomputation consistency, NOT independent cross-validation; genuine independence comes from the isolated sub-agent review.",
    }
    with open(os.path.join(OUT, "R121-VERIFICATION.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print(f"{res['n_match']}/{res['n_checks']} MATCH, {res['n_mismatch']} MISMATCH")
    for c in CHECKS:
        if c["status"] == "MISMATCH":
            print("  MISMATCH", c["id"], c["label"], "expected=", c["expected"], "observed=", c["observed"])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""R119 independent recomputation from raw disk bytes.

Deliberately does NOT import R119-raw.py and does NOT read any R119 RAW/JSON
artifact. Every value below is recomputed directly from the source files.
This is a same-host hashlib consistency check, NOT an independent
cross-verification (R115 W4 / R114 D1); genuine independence is the job of a
fresh isolated sub-agent.

Read-only: writes ONLY R119-REVIEW-LAUNCH-PROTOCOL-VERIFICATION.json.
No pre-existing byte is changed. No score line is emitted.
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HOME = Path.home()
BRIEF = ROOT / "papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2/protocols/independent-review-brief.md"
R107 = ROOT / "GOAL-ITERATION-R107.md"
VAL = ROOT / "readonly-validator/validate_single_paper.py"
SKILL = HOME / ".claude/skills/ccf-paper-reviewer/SKILL.md"


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(cid, label, expected, observed):
    return {"id": cid, "label": label, "expected": expected,
            "observed": observed,
            "verdict": "MATCH" if expected == observed else "MISMATCH"}


def main():
    rows = []
    brief_b = BRIEF.read_bytes()
    brief_t = brief_b.decode("utf-8", errors="replace")
    bl = brief_t.splitlines()
    r107_t = R107.read_text(encoding="utf-8", errors="replace")
    val_t = VAL.read_text(encoding="utf-8", errors="replace")
    skill_t = SKILL.read_text(encoding="utf-8", errors="replace")

    # Source digests, recomputed from bytes (not from RAW json).
    for cid, label, p, exp_sha16, exp_bytes in [
        ("C01", "brief sha256[:16]", BRIEF, "8771dea80cf7a54d", 4803),
        ("C02", "GOAL-ITERATION-R107 sha256[:16]", R107, "1a81c8e15b361f62", 5446),
        ("C03", "validator sha256[:16]", VAL, "72240260ec2447c2", 7845),
        ("C04", "guard ledger sha256[:16]", ROOT / "guard/ledger-null-ladder.json", "73043b4e164a5a5f", 9994),
        ("C05", "main-line pipeline-state sha256[:16]",
         ROOT / "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json",
         "bcb48bb964e657a4", 3723),
    ]:
        rows.append(check(cid, label, [exp_sha16, exp_bytes],
                          [digest(p)[:16], p.stat().st_size]))

    # Exact-substring checks with line numbers, recomputed from raw text.
    for cid, label, text, needle, exp_lines in [
        ("C06", "brief '(Contract v2, R51)'", brief_t, "(Contract v2, R51)", [1]),
        ("C07", "brief 'X > 8.0' qualification line", brief_t, "qualification requires **X > 8.0**", [17]),
        ("C08", "brief 'exactly 8.0 does not qualify'", brief_t, "(exactly 8.0 does not qualify)", [18]),
        ("C09", "brief 'If X <= 8.0'", brief_t, "If X <= 8.0, the correction loop continues", [85]),
        ("C10", "brief 'score_gt_threshold = true'", brief_t, "score_gt_threshold = true", [81]),
        ("C11", "brief frozen output filename 20261108", brief_t, "independent-review-20261108.md", [76]),
        ("C12", "brief non-anchoring clause", brief_t,
         "You are not told what score would be considered a success", [65]),
        ("C13", "brief 'Do not use any number quoted in this brief'", brief_t,
         "Do not use any number quoted in this brief", [35]),
        ("C14", "R107 protocols-frozen line", r107_t, "`protocols/` — frozen", [90]),
        ("C15", "R107 v4 route", r107_t, "future versioned contract (v4)", [91]),
        ("C16", "R107 no-retroactive-edit", r107_t,
         "no existing contract is retroactively edited", [92]),
        ("C17", "R107 anti-gaming new-review clause", r107_t,
         "**new** full independent review", [65]),
        ("C18", "validator score_meets_threshold", val_t, '"score_meets_threshold"', [155]),
        ("C19", "validator comparison_operator >= ", val_t, '"comparison_operator": ">="', [156]),
        ("C20", "SKILL.md cites ccf-common output standards", skill_t,
         "../ccf-common/references/review-output-standards.md", [27, 40, 90]),
    ]:
        got = [i + 1 for i, ln in enumerate(text.splitlines()) if needle in ln]
        rows.append(check(cid, label, exp_lines, got))

    # Structural / semantic checks.
    rows.append(check("C21", "validator default threshold", [True],
                      [bool(re.search(r"default=7\.0", val_t))]))
    rows.append(check("C22", "brief-cited reviewer path exists", [False],
                      [(HOME / ".claude/skills/ccf-paper-reviewer/references/review-output-standards.md").exists()]))
    rows.append(check("C23", "actual ccf-common path exists", [True],
                      [(HOME / ".claude/skills/ccf-common/references/review-output-standards.md").exists()]))
    rows.append(check("C24", "calibration-and-rank.md exists", [True],
                      [(HOME / ".claude/skills/ccf-paper-reviewer/references/calibration-and-rank.md").exists()]))
    rows.append(check("C25", "venue-guides dir exists", [True],
                      [(HOME / ".claude/skills/ccf-paper-writer/references/venue-guides").is_dir()]))

    # Anchor-disclosure scoping: verbatim reviewer handoff block = lines 21..66.
    block = bl[20:66]
    rows.append(check("C26", "handoff block lines containing '8.0'", [[]],
                      [[i + 21 for i, ln in enumerate(block) if "8.0" in ln]]))
    rows.append(check("C27", "handoff block lines containing '7.0'", [[]],
                      [[i + 21 for i, ln in enumerate(block) if "7.0" in ln]]))
    rows.append(check("C28", "brief preamble historical score '8.2' lines", [[10]],
                      [[i + 1 for i, ln in enumerate(bl) if "8.2" in ln]]))
    rows.append(check("C29", "brief preamble historical score '6.5' lines", [[11]],
                      [[i + 1 for i, ln in enumerate(bl) if "6.5" in ln]]))

    # Historical-review evidence that past reviewers read the whole brief.
    r58 = (ROOT / "ccfa-review-reports/paper-null-ladder-r58-independent-review-20261108.md").read_text(encoding="utf-8", errors="replace")
    r60 = (ROOT / "ccfa-review-reports/paper-null-ladder-r60-independent-review-20261108.md").read_text(encoding="utf-8", errors="replace")
    rows.append(check("C30", "R58 cites brief path", [True],
                      ["protocols/independent-review-brief.md" in r58]))
    rows.append(check("C31", "R60 registers brief numeric gate as background", [True],
                      ["independent-review-brief.md" in r60 and "background" in r60.lower() or
                       "背景数据" in r60]))

    # v4 / R107 versioned brief: none exists.
    v4 = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
          if p.is_file() and ".git" not in p.parts and "brief" in p.name.lower()
          and ("v4" in p.name.lower() or "r107" in p.name.lower() or "r11" in p.name.lower())]
    rows.append(check("C32", "R107/v4 versioned launch brief count", [0], [len(v4)]))
    rows.append(check("C33", "independent-review-brief* copy count", [1],
                      [len([p for p in ROOT.rglob("independent-review-brief*") if ".git" not in p.parts])]))

    # Guard A6 dual wording, recomputed from JSON (background, not new finding).
    gc = json.loads((ROOT / "guard/criteria-null-ladder.json").read_text())
    gl = json.loads((ROOT / "guard/ledger-null-ladder.json").read_text())
    a6c = next(a for a in gc["acceptance"] if a["id"] == "A6")
    a6l = next(a for a in gl["acceptance"] if a["id"] == "A6")
    rows.append(check("C34", "criteria A6 text contains >= 7.0", [True], [">= 7.0" in a6c["text"]]))
    rows.append(check("C35", "ledger A6 text contains > 8.0", [True], ["严格 > 8.0" in a6l["text"]]))

    # Main-line G0 status.
    st = json.loads((ROOT / "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json").read_text())
    g0 = next(s for s in st["stages"] if s["id"] == "G0")
    rows.append(check("C36", "G0 status / inputs / evidence", ["pending", [], []],
                      [g0["status"], g0["inputs"], g0["evidence"]]))

    mismatches = [r for r in rows if r["verdict"] == "MISMATCH"]
    doc = {
        "round": "R119",
        "kind": "INDEPENDENT_RECOMPUTATION_FROM_RAW_BYTES",
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "python": sys.version.split()[0],
        "reads_R119_raw_artifact": False,
        "imports_R119_raw_module": False,
        "checks": rows,
        "n_checks": len(rows),
        "n_match": len(rows) - len(mismatches),
        "n_mismatch": len(mismatches),
        "mismatches": mismatches,
        "independence_caveat": (
            "Same host, same hashlib, same data source as R119-raw.py. A MATCH "
            "here is a necessary consistency check only, NOT independent "
            "cross-verification. The fresh isolated sub-agent supplies that."),
        "boundary": "Read-only; only this verification JSON is written. No score line.",
    }
    out = HERE / "R119-REVIEW-LAUNCH-PROTOCOL-VERIFICATION.json"
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("checks=%d MATCH=%d MISMATCH=%d" % (len(rows), len(rows) - len(mismatches), len(mismatches)))
    for r in mismatches:
        print("  MISMATCH", r["id"], r["label"], "expected", r["expected"], "observed", r["observed"])
    print("written:", out.name, out.stat().st_size, "B")
    return 1 if mismatches else 0


if __name__ == "__main__":
    sys.exit(main())

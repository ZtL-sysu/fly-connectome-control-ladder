#!/usr/bin/env python3
"""R119 read-only raw measurement: the LAUNCH-PROTOCOL CHAIN of the sole
success-criterion action ("fresh isolated ccf-paper-reviewer full").

Scope (R119 RGE4 pivot): previous rounds R110 measured acceptance-machinery
reachability, R114-R118 measured first-hand licence/archive/registry facts.
No round has audited the LAUNCH BRIEF itself against the R107 goal iteration
and the current heartbeat step-3 instruction. This script only READS bytes.

Red-line contract:
  * ZERO writes to any pre-existing project file. Only files in this R119
    directory are created.
  * ZERO forward pass / inference / training / label / dataset / metric.
  * ZERO gate promotion, ZERO self-certification, ZERO state change.
  * No `**Overall:** <number>` line is ever emitted into any artifact.
  * Local absolute paths are represented as <local>/ in emitted artifacts.
  * Search scope is declared per assertion: RAW_BYTES_EXACT_SUBSTRING or
    FILE_EXISTENCE or REGEX. R118 W2 lesson: "found in rebuilt text" !=
    "found in raw bytes".
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]          # .../fly-gnn-snn-vision
HOME = Path.home()
RUN_V2 = "papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2"
BRIEF_REL = RUN_V2 + "/protocols/independent-review-brief.md"
PY = "/Users/xhf/miniconda3/bin/python"


def stat(rel, base=ROOT):
    p = base / rel
    if not p.exists():
        return {"path": rel, "exists": False}
    st = p.stat()
    if p.is_dir():
        # v2 fix (R119 script defect, NOT a data inconsistency): venue-guides
        # is a directory; read_bytes() raised IsADirectoryError in v1.
        return {"path": rel, "exists": True, "is_dir": True,
                "child_entries": len(list(p.iterdir()))}
    b = p.read_bytes()
    return {
        "path": rel,
        "exists": True,
        "bytes": len(b),
        "sha256": hashlib.sha256(b).hexdigest(),
        "mtime_utc": datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat(timespec="seconds"),
        "lines": len(b.splitlines()),
    }


def raw_lines(rel, base=ROOT):
    p = base / rel
    if not p.is_file():
        return None
    return p.read_text(encoding="utf-8", errors="replace").splitlines()


def exact_substring(rel, needle, base=ROOT):
    """RAW_BYTES_EXACT_SUBSTRING over the file's literal text."""
    p = base / rel
    if not p.is_file():
        return {"scope": "RAW_BYTES_EXACT_SUBSTRING", "found": False,
                "reason": "file missing"}
    txt = p.read_text(encoding="utf-8", errors="replace")
    hits = [i + 1 for i, ln in enumerate(txt.splitlines()) if needle in ln]
    return {"scope": "RAW_BYTES_EXACT_SUBSTRING", "needle": needle,
            "found": bool(hits), "line_numbers": hits}


def main():
    src = {}
    for key, rel in {
        "brief": BRIEF_REL,
        "goal_iteration_r107": "GOAL-ITERATION-R107.md",
        "validator": "readonly-validator/validate_single_paper.py",
        "guard_criteria": "guard/criteria-null-ladder.json",
        "guard_ledger": "guard/ledger-null-ladder.json",
        "ledger": "goal-ledger.md",
        "review_r95": "ccfa-review-reports/paper-null-ladder-r95-independent-review-20261111.md",
        "review_r58": "ccfa-review-reports/paper-null-ladder-r58-independent-review-20261108.md",
        "review_r60": "ccfa-review-reports/paper-null-ladder-r60-independent-review-20261108.md",
        "brief_r95_frozen": "papers/paper-null-ladder/R49-7.5-DELIVERY/provenance/R95-independent-review-brief-FROZEN.md",
        "main_pipeline_state": "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json",
        "r111_decision_package": "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/state-handoff-R111/R111-DECISION-READY-PACKAGE.md",
    }.items():
        src[key] = stat(rel)

    # skills live under HOME, outside the project tree
    skills = {}
    for key, rel in {
        "reviewer_SKILL": ".claude/skills/ccf-paper-reviewer/SKILL.md",
        "reviewer_calibration": ".claude/skills/ccf-paper-reviewer/references/calibration-and-rank.md",
        "reviewer_output_standards_BRIEF_PATH": ".claude/skills/ccf-paper-reviewer/references/review-output-standards.md",
        "common_output_standards_ACTUAL_PATH": ".claude/skills/ccf-common/references/review-output-standards.md",
        "writer_venue_guides": ".claude/skills/ccf-paper-writer/references/venue-guides",
    }.items():
        skills[key] = stat(rel, base=HOME)

    # Assertions, each with an explicitly declared scope.
    assertions = []

    def A(aid, desc, scope, result, note=""):
        assertions.append({"id": aid, "description": desc, "scope": scope,
                           "result": result, "note": note})

    # --- A1: brief is unique on disk ---
    copies = []
    for p in ROOT.rglob("independent-review-brief*"):
        if ".git" in p.parts:
            continue
        copies.append(str(p.relative_to(ROOT)))
    A("A1", "count of independent-review-brief* files in project tree",
      "FILE_GLOB", {"count": len(copies), "paths": sorted(copies)})

    # --- A2..: R51-era threshold wording still inside the frozen brief ---
    for aid, needle in [
        ("A2", "qualification requires **X > 8.0**"),
        ("A3", "(exactly 8.0 does not qualify)"),
        ("A4", "If X <= 8.0, the correction loop continues"),
        ("A5", "score_gt_threshold = true"),
        ("A6", "(Contract v2, R51)"),
        ("A7", "independent-review-20261108.md"),
        ("A8", "8 pages of main content"),
    ]:
        A(aid, "literal string present in brief raw text",
          "RAW_BYTES_EXACT_SUBSTRING", exact_substring(BRIEF_REL, needle))

    # --- A9: the brief's verbatim reviewer handoff block DOES contain an
    #         explicit non-anchoring instruction (do not overstate leakage) ---
    for aid, needle in [
        ("A9", "You are not told what score would be considered a success"),
        ("A10", "Do not use any number quoted in this brief"),
        ("A11", "exactly one** line of the form"),
    ]:
        A(aid, "non-anchoring / output-format clause in brief",
          "RAW_BYTES_EXACT_SUBSTRING", exact_substring(BRIEF_REL, needle))

    # --- A12: R107 explicitly FROZE protocols/ (so this is NOT a bug to fix).
    #  v2 fix (R118 W2 lesson): v1 needle "frozen contracts" missed because the
    #  source wraps it across lines 90-91. Use the exact single-line substring
    #  from line 90 instead; declare the search scope explicitly. ---
    A("A12", "R107 file lists protocols/ among frozen contracts (exact line-90 substring)",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("GOAL-ITERATION-R107.md", "`protocols/` — frozen"))
    A("A12b", "R107 file says 'no existing contract is retroactively edited'",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("GOAL-ITERATION-R107.md", "no existing contract is retroactively edited"))
    A("A13", "R107 file names the versioned-contract route (v4)",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("GOAL-ITERATION-R107.md", "future versioned contract (v4)"))
    A("A14", "R107 success criterion comparison operator is >= 7.0",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("GOAL-ITERATION-R107.md", ">= 7.0"))
    A("A15", "R107 success criterion says a NEW full review of a REVISED manuscript",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("GOAL-ITERATION-R107.md", "**new** full independent review"))

    # --- A16: validator live threshold / operator ---
    v = raw_lines("readonly-validator/validate_single_paper.py") or []
    A("A16", "validator default --threshold is 7.0",
      "REGEX_OVER_SOURCE_LINES",
      {"found": any(re.search(r"default=7\.0", ln) for ln in v),
       "matching_lines": [i + 1 for i, ln in enumerate(v) if re.search(r"default=7\.0", ln)]})
    A("A17", "validator emits comparison_operator '>=' ",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("readonly-validator/validate_single_paper.py", '"comparison_operator": ">="'))
    A("A18", "validator emits new score_meets_threshold field",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("readonly-validator/validate_single_paper.py", '"score_meets_threshold"'))

    # --- A19/A20: guard A6 dual wording (already known from R110/R111;
    #              registered as background, NOT claimed as new finding) ---
    A("A19", "guard criteria A6 text uses >= 7.0",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("guard/criteria-null-ladder.json", "Overall >= 7.0"))
    A("A20", "guard ledger A6 text still uses strictly > 8.0",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("guard/ledger-null-ladder.json", "严格 > 8.0"))

    # --- A21: skill path cited by brief does not exist; real path does ---
    A("A21", "brief-cited skill path vs actual installed path",
      "FILE_EXISTENCE",
      {"brief_cited_exists": skills["reviewer_output_standards_BRIEF_PATH"]["exists"],
       "actual_common_exists": skills["common_output_standards_ACTUAL_PATH"]["exists"],
       "reviewer_SKILL_exists": skills["reviewer_SKILL"]["exists"],
       "calibration_exists": skills["reviewer_calibration"]["exists"],
       "venue_guides_exists": skills["writer_venue_guides"]["exists"]})
    A("A22", "reviewer SKILL.md itself cites ../ccf-common/references/review-output-standards.md",
      "RAW_BYTES_EXACT_SUBSTRING_HOME",
      {"found": "../ccf-common/references/review-output-standards.md" in
                (HOME / ".claude/skills/ccf-paper-reviewer/SKILL.md").read_text(encoding="utf-8", errors="replace"),
       "line_numbers": [i + 1 for i, ln in enumerate(
           (HOME / ".claude/skills/ccf-paper-reviewer/SKILL.md").read_text(encoding="utf-8", errors="replace").splitlines())
           if "../ccf-common/references/review-output-standards.md" in ln]})

    # --- A23: empirical evidence that past reviewers READ the whole brief ---
    A("A23", "R58 independent review states it read protocols/independent-review-brief.md",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("ccfa-review-reports/paper-null-ladder-r58-independent-review-20261108.md",
                      "protocols/independent-review-brief.md"))
    A("A24", "R60 independent review registers the brief's numeric gate as background only",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("ccfa-review-reports/paper-null-ladder-r60-independent-review-20261108.md",
                      "independent-review-brief.md"))

    # --- A25: R95 used a DIFFERENT frozen brief (do not conflate) ---
    A("A25", "R95 FROZEN brief contains no literal 8.0 threshold number",
      "RAW_BYTES_EXACT_SUBSTRING",
      exact_substring("papers/paper-null-ladder/R49-7.5-DELIVERY/provenance/R95-independent-review-brief-FROZEN.md",
                      "8.0"))

    # --- A26b..A26f: the conflict is about ANCHOR DISCLOSURE, not just wording.
    #  R107 heartbeat step 3 requires launching a fresh isolated full review
    #  "without revealing expected score / score anchors". The frozen brief,
    #  however, embeds numeric thresholds and two historical score values in
    #  its preamble (outside the verbatim reviewer handoff block). ---
    bl = raw_lines(BRIEF_REL) or []
    def brief_line_contains(needle):
        return [i + 1 for i, ln in enumerate(bl) if needle in ln]

    A("A26b", "brief contains historical numeric scores in preamble (line 10: 8.2, line 11: 6.5)",
      "RAW_BYTES_EXACT_SUBSTRING",
      {"line_8_2": brief_line_contains("8.2"),
       "line_6_5": brief_line_contains("6.5"),
       "note": "preamble lines 9-11 are OUTSIDE the verbatim reviewer handoff block (lines 21-66)"})
    A("A26c", "brief verbatim handoff block (lines 21-66) numeric threshold tokens",
      "RAW_BYTES_EXACT_SUBSTRING_SCOPED_LINES",
      {"scope_lines": [21, 66],
       "lines_with_8_0": [i + 1 for i in range(20, min(66, len(bl))) if "8.0" in bl[i]],
       "lines_with_7_0": [i + 1 for i in range(20, min(66, len(bl))) if "7.0" in bl[i]],
       "note": "tests whether the quoted reviewer-facing text itself carries a threshold"})

    # Is the R51 brief the file the heartbeat step 3 points at? Check that no
    # versioned v4 brief exists anywhere in the project tree.
    v4 = []
    for p in ROOT.rglob("*"):
        if ".git" in p.parts or not p.is_file():
            continue
        n = p.name.lower()
        if ("brief" in n and ("v4" in n or "r107" in n or "r11" in n)):
            v4.append(str(p.relative_to(ROOT)))
    A("A26d", "existence of any R107/v4 versioned launch brief",
      "FILE_GLOB", {"count": len(v4), "paths": sorted(v4)})
    A("A26e", "count of files named *independent-review-brief* (all copies)",
      "FILE_GLOB", {"count": len(copies), "paths": sorted(copies)})

    # --- A26: main-line state unchanged baseline ---
    A("A26", "main-line pipeline-state.json G0 status",
      "JSON_PARSE",
      {"g0": next((s for s in json.loads((ROOT / "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json").read_text())["stages"] if s["id"] == "G0"), None)})

    doc = {
        "round": "R119",
        "kind": "READONLY_REVIEW_LAUNCH_PROTOCOL_CHAIN_AUDIT",
        "status": "PROTOCOL_CONSISTENCY_MEASUREMENT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "python": PY,
        "runtime_version": sys.version.split()[0],
        "note_on_timestamps": "created_utc is artifact-generation time; must NOT be used to infer capture order (R115 W3 / R114 D5)",
        "network_requests_this_round": 0,
        "sources": src,
        "skills": skills,
        "assertions": assertions,
        "independence_caveat": (
            "Two scripts in this round run on the same host with the same hashlib "
            "and the same data sources; their agreement is a necessary consistency "
            "check, NOT an independent cross-verification (R115 W4 / R114 D1). "
            "Genuine independent recomputation is delegated to a fresh isolated "
            "sub-agent with no access to the authoring conversation."),
        "boundary": (
            "READ ONLY. No pre-existing byte changed. No gate promotion, no "
            "self-certification, no stage status change, no review launched, "
            "no score line produced, no threshold/contract/ledger/brief edit."),
    }
    out = HERE / "R119-REVIEW-LAUNCH-PROTOCOL-RAW.json"
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("=== R119 RAW MEASUREMENT ===")
    for key, s in src.items():
        print("  %-28s exists=%-5s bytes=%-8s sha16=%s" % (
            key, s["exists"], s.get("bytes", "-"), s.get("sha256", "-")[:16]))
    print()
    for key, s in skills.items():
        print("  SKILL %-42s exists=%s bytes=%s" % (key, s["exists"], s.get("bytes", "-")))
    print()
    for a in assertions:
        r = a["result"]
        if a["scope"] == "FILE_GLOB":
            v = r["count"]
        elif a["scope"] == "FILE_EXISTENCE":
            v = r
        elif a["scope"] == "JSON_PARSE":
            v = "G0=" + str(r["g0"]["status"])
        else:
            v = "found=%s lines=%s" % (r.get("found", r.get("count")), r.get("line_numbers", "-"))
        print("  %-5s %-70s %s" % (a["id"], a["description"][:70], v))
    print()
    print("written:", out.name, out.stat().st_size, "B")
    return 0


if __name__ == "__main__":
    sys.exit(main())

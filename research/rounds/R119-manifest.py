#!/usr/bin/env python3
"""R119 source manifest + isolated byte-identical copies.

Read-only with respect to all pre-existing project files. Writes only:
  R119-SOURCE-MANIFEST.json, isolated/<basename> (6 copies).
Local absolute paths are represented as <local>/ in the emitted JSON.
"""
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HOME = Path.home()

SOURCES = [
    ("brief", ROOT / "papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2/protocols/independent-review-brief.md"),
    ("goal_iteration_r107", ROOT / "GOAL-ITERATION-R107.md"),
    ("validator", ROOT / "readonly-validator/validate_single_paper.py"),
    ("guard_criteria", ROOT / "guard/criteria-null-ladder.json"),
    ("guard_ledger", ROOT / "guard/ledger-null-ladder.json"),
    ("review_r58", ROOT / "ccfa-review-reports/paper-null-ladder-r58-independent-review-20261108.md"),
    ("review_r60", ROOT / "ccfa-review-reports/paper-null-ladder-r60-independent-review-20261108.md"),
    ("review_r95", ROOT / "ccfa-review-reports/paper-null-ladder-r95-independent-review-20261111.md"),
    ("brief_r95_frozen", ROOT / "papers/paper-null-ladder/R49-7.5-DELIVERY/provenance/R95-independent-review-brief-FROZEN.md"),
    ("main_pipeline_state", ROOT / "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json"),
    ("r111_decision_package", ROOT / "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/state-handoff-R111/R111-DECISION-READY-PACKAGE.md"),
    ("reviewer_SKILL", HOME / ".claude/skills/ccf-paper-reviewer/SKILL.md"),
    ("common_output_standards", HOME / ".claude/skills/ccf-common/references/review-output-standards.md"),
]

# The six sources that are copied byte-identically for cmp verification.
COPY_KEYS = ["brief", "goal_iteration_r107", "validator", "guard_criteria",
             "guard_ledger", "main_pipeline_state"]


def rel(p):
    """Path shown in the manifest, with local absolute roots masked."""
    s = str(p)
    s = s.replace(str(ROOT), "<local>/fly-gnn-snn-vision")
    s = s.replace(str(HOME), "<local>/home")
    return s


def main():
    entries = []
    for key, p in SOURCES:
        b = p.read_bytes()
        entries.append({
            "key": key,
            "path": rel(p),
            "exists": True,
            "bytes": len(b),
            "sha256": hashlib.sha256(b).hexdigest(),
        })
    # Explicit negative evidence for the path cited by the brief.
    missing = HOME / ".claude/skills/ccf-paper-reviewer/references/review-output-standards.md"
    entries.append({
        "key": "brief_cited_output_standards",
        "path": rel(missing),
        "exists": False,
        "note": "path cited by brief line 30; file absent at this location",
    })

    iso = HERE / "isolated"
    iso.mkdir(exist_ok=True)
    copies = []
    for key, p in SOURCES:
        if key not in COPY_KEYS:
            continue
        dst = iso / (key + p.suffix)
        shutil.copy2(p, dst)
        copies.append({
            "key": key,
            "src": rel(p),
            "dst": "isolated/" + dst.name,
            "src_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "dst_sha256": hashlib.sha256(dst.read_bytes()).hexdigest(),
            "identical": p.read_bytes() == dst.read_bytes(),
        })

    doc = {
        "round": "R119",
        "kind": "SOURCE_MANIFEST_READONLY",
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "timestamp_note": "artifact-generation time only; NOT usable to infer capture order (R115 W3 / R114 D5)",
        "sources": entries,
        "isolated_copies": copies,
        "all_copies_identical": all(c["identical"] for c in copies),
        "network_requests_this_round": 0,
        "python": sys.version.split()[0],
    }
    out = HERE / "R119-SOURCE-MANIFEST.json"
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("sources=%d isolated_copies=%d all_identical=%s" %
          (len(entries), len(copies), doc["all_copies_identical"]))
    print("written:", out.name, out.stat().st_size, "B")
    return 0 if doc["all_copies_identical"] else 1


if __name__ == "__main__":
    sys.exit(main())

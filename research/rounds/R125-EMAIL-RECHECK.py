#!/usr/bin/env python3
"""R125 post-review supplementary recheck (append-only, does not rewrite v1/v2/v3).

Motivation: isolated reviewer L1 found the frozen verifier's H-group `noEmail`
check only counts a file when it contains BOTH `@` AND `.com`. The two email-shaped
strings in wayback-v1.html use `.org`, so that check silently returned 0 and cannot
establish "zero email literals in raw bytes".

This module uses a domain-agnostic regex over the 13 raw files and records the
exact count. Frozen verifier versions are NOT modified.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"
EMAIL = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")

per_file: dict[str, dict[str, object]] = {}
for p in sorted(RAW.iterdir()):
    if p.is_file():
        found = EMAIL.findall(p.read_bytes().decode("utf-8", "replace"))
        if found:
            per_file[p.name] = {
                "occurrences": len(found),
                "distinct": sorted(set(found)),
            }

blobs = [p.read_bytes() for p in sorted(RAW.iterdir()) if p.is_file()]
weak_count = sum(1 for b in blobs if b"@" in b and b".com" in b)

result = {
    "scope": "13 R125 raw byte files only; these files are NOT uploaded to the public repo",
    "regex": EMAIL.pattern,
    "total_occurrences": sum(int(v["occurrences"]) for v in per_file.values()),
    "total_distinct_strings": len({s for v in per_file.values() for s in v["distinct"]}),
    "counting_scope_note": (
        "occurrences = every regex match (2); distinct = unique strings (1). "
        "R124 L1 lesson: any count must declare which scope it uses."
    ),
    "per_file": per_file,
    "frozen_verifier_weak_check_count": weak_count,
    "frozen_verifier_weak_check_rule": "file counted only if it contains BOTH '@' and '.com'",
    "conclusion": (
        "Two email-shaped literals exist, both the public Internet Archive contact "
        "address in the Wayback 404 page. The frozen verifier's weak check is a "
        "false-negative design flaw. No published document claims zero email "
        "literals in the raw set; the public upload set contains none of these files."
    ),
    "note": "No scientific result, no gate change, no score change.",
}
(HERE / "R125-EMAIL-RECHECK.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
)
print(json.dumps(result, ensure_ascii=False, indent=1))

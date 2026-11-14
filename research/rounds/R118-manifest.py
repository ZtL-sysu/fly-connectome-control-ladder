#!/usr/bin/env python3
"""R118 manifest builder (READ-ONLY).

Purpose: quantify, from raw disk bytes, the registry gap named by the R107
independent gate review (W7 / R4 PARTIAL) and the R98 "23 saved public
sources" vs 5-entry source-manifest.json discrepancy.

This script performs NO network requests, writes ONLY into gate-G0-R118/,
and never modifies any pre-existing file.
"""
import hashlib
import json
import os
import re
import datetime

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "gate-G0-R118")
LIT = os.path.join(RUN, "literature-search")
REG = os.path.join(LIT, "source-manifest.json")

# Classification rule (declared up front so an independent recompute can
# reproduce it exactly). Only these suffixes count as "externally fetched
# first-hand source bytes"; everything else is project-owned artifact.
FIRSTHAND_SUFFIXES = {".html", ".xml", ".pdf", ".txt"}
EXCLUDED_SUFFIXES = {".py", ".png", ".npz", ".npy", ".ipynb", ".zip", ".md", ".json"}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rel(p):
    return os.path.relpath(p, RUN).replace(os.sep, "/")


def main():
    all_files = []
    for root, dirs, files in os.walk(LIT):
        dirs.sort()
        for fn in sorted(files):
            p = os.path.join(root, fn)
            if not os.path.isfile(p):
                continue
            b = open(p, "rb").read()
            ext = os.path.splitext(fn)[1].lower()
            all_files.append({
                "path": rel(p),
                "bytes": len(b),
                "sha256": sha(b),
                "suffix": ext,
                "class": ("FIRSTHAND_CANDIDATE" if ext in FIRSTHAND_SUFFIXES
                          else "PROJECT_ARTIFACT"),
                "mtime_utc": datetime.datetime.fromtimestamp(
                    os.stat(p).st_mtime, datetime.timezone.utc
                ).isoformat(timespec="seconds"),
            })

    # Registry file itself, from raw bytes.
    reg_bytes = open(REG, "rb").read()
    registry = json.loads(reg_bytes.decode("utf-8"))
    reg_entry = {
        "path": rel(REG),
        "bytes": len(reg_bytes),
        "sha256": sha(reg_bytes),
        "entry_count": len(registry),
        "names": [e.get("name") for e in registry],
        "contains_2609_24565": "2609.24565" in reg_bytes.decode("utf-8", "replace"),
    }

    # Verify each declared registry entry against raw disk bytes.
    declared_check = []
    for e in registry:
        name = e.get("name")
        # manifest convention: <name>.html for arxiv pages, pmc page is .html too
        cand = [f for f in all_files
                if f["path"].endswith("/" + name + ".html")
                or f["path"].endswith("/" + name + ".xml")]
        hit = cand[0] if cand else None
        declared_check.append({
            "name": name,
            "declared_url": e.get("url"),
            "declared_bytes": e.get("bytes"),
            "declared_sha256": e.get("sha256"),
            "matched_disk_path": hit["path"] if hit else None,
            "disk_bytes": hit["bytes"] if hit else None,
            "disk_sha256": hit["sha256"] if hit else None,
            "bytes_match": bool(hit and hit["bytes"] == e.get("bytes")),
            "sha_match": bool(hit and hit["sha256"] == e.get("sha256")),
        })

    fh = [f for f in all_files if f["class"] == "FIRSTHAND_CANDIDATE"]
    # Sub-classify: which of the first-hand candidates are actually registered?
    registered_paths = {c["matched_disk_path"] for c in declared_check
                        if c["matched_disk_path"]}
    for f in fh:
        f["registered_in_source_manifest"] = f["path"] in registered_paths

    # Kuklev frozen bytes live in gate-G0-R107/sources, not literature-search/
    kuklev_dir = os.path.join(RUN, "gate-G0-R107", "sources")
    kuklev = []
    for fn in sorted(os.listdir(kuklev_dir)):
        if not fn.startswith("kuklev_"):
            continue
        p = os.path.join(kuklev_dir, fn)
        b = open(p, "rb").read()
        kuklev.append({"path": rel(p), "bytes": len(b), "sha256": sha(b)})

    # Cross-round claims to be checked by R118-verify.py (never self-certified here).
    matrix_path = os.path.join(RUN, "literature-baseline-matrix.md")
    mb = open(matrix_path, "rb").read()
    r98_path = os.path.join(RUN, "gate-G0-evidence-review-R98.md")
    r98b = open(r98_path, "rb").read()
    state_path = os.path.join(RUN, "pipeline-state.json")
    sb = open(state_path, "rb").read()

    doc = {
        "round": "R118",
        "kind": "READONLY_SOURCE_REGISTRY_GAP_AUDIT",
        "scope": "literature-search/ + gate-G0-R107/sources/kuklev_* + registry/matrix/R98/pipeline-state claims",
        "generated_at_utc_note": "artifact-generation instant; NOT a fetch timestamp; do not use to reconstruct acquisition order (R115 W3 / R114 D5)",
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "network_requests_this_round": 0,
        "classification_rule": {
            "FIRSTHAND_CANDIDATE_suffixes": sorted(FIRSTHAND_SUFFIXES),
            "PROJECT_ARTIFACT_suffixes": sorted(EXCLUDED_SUFFIXES),
            "note": "candidate != verified first-hand source; see R118-verify.py for the field-level check",
        },
        "counts": {
            "all_files_under_literature_search": len(all_files),
            "firsthand_candidates": len(fh),
            "firsthand_candidates_registered": sum(
                1 for f in fh if f["registered_in_source_manifest"]),
            "firsthand_candidates_unregistered": sum(
                1 for f in fh if not f["registered_in_source_manifest"]),
            "project_artifacts": len(all_files) - len(fh),
            "kuklev_frozen_bytes": len(kuklev),
        },
        "registry": reg_entry,
        "declared_entries_check": declared_check,
        "kuklev_frozen_bytes": kuklev,
        "reference_claims": {
            "literature-baseline-matrix.md": {
                "bytes": len(mb), "sha256": sha(mb),
            },
            "gate-G0-evidence-review-R98.md": {
                "bytes": len(r98b), "sha256": sha(r98b),
            },
            "pipeline-state.json": {
                "bytes": len(sb), "sha256": sha(sb),
            },
        },
        "files": all_files,
    }
    with open(os.path.join(OUT, "R118-SOURCE-MANIFEST.json"), "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2, sort_keys=False)
    print(json.dumps({k: v for k, v in doc.items() if k in
                      ("round", "counts", "registry", "declared_entries_check")},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

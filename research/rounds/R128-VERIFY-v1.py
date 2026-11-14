#!/usr/bin/env python3
"""R128 independent verifier — post-merge PUBLIC default-branch attestation.

Independence contract (R117/R119/R121/R122/R124/R125 precedent):
  * Does NOT import R128-ACQUIRE.py.
  * Does NOT read any R128 JSON as a substantive data source. All values are
    re-derived from the committed `main` tree blobs and from live gate runs.
  * Uses a DIFFERENT, broader real-credential pattern set than the collector
    (Bearer+long, JWT eyJ, hex32+, unquoted assignments, assignment keywords,
    PEM blocks), plus a length/entropy heuristic on opaque tokens.
  * Same-machine byte-identity checks are explicitly declared as such (group A),
    not as independent cross-validation.

Writes only R128-VERIFICATION.json into its own round directory.
"""
import hashlib
import json
import math
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision")
REPO = Path("/Users/xhf/Downloads/phd/4090/research-sync-public")
OUT = ROOT / "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/post-merge-R128"


def git(*a):
    return subprocess.run(["git", "-C", str(REPO), *a],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def entropy(s):
    if not s:
        return 0.0
    from collections import Counter
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in Counter(s).values())


def main():
    rows = []

    def ck(group, name, expected, computed):
        rows.append({"group": group, "check": name, "expected": expected,
                     "computed": computed, "match": expected == computed})

    # ---- rebuild the committed tree independently ------------------------
    txt = git("ls-tree", "-r", "-l", "main").stdout.decode("utf-8", "surrogateescape")
    tree = {}
    for line in txt.splitlines():
        meta, _, path = line.partition("\t")
        f = meta.split()
        tree[path] = {"blob": f[2], "size": int(f[3])}
    ck("A", "tree_file_count", 336, len(tree))
    ck("A", "tree_total_bytes", 9798478, sum(v["size"] for v in tree.values()))
    ck("A", "max_file_bytes_below_50MiB", True,
       max(v["size"] for v in tree.values()) <= 50 * 1024 * 1024)
    ck("A", "local_main_equals_remote_main", True,
       git("rev-parse", "main").stdout.strip() in
       git("ls-remote", "origin", "refs/heads/main").stdout)
    ck("A", "worktree_clean", True, git("status", "--porcelain").stdout.strip() == b"")

    # ---- read blobs via a different mechanism (one cat-file per blob) ----
    blobs = {}
    for path, v in tree.items():
        blobs[path] = git("cat-file", "blob", v["blob"]).stdout
    ck("A", "all_blob_sizes_agree", True,
       all(len(blobs[p]) == v["size"] for p, v in tree.items()))

    # ---- group B: manifest integrity ------------------------------------
    man = json.loads(blobs["research/UPLOAD-MANIFEST.json"])
    cop = man["copied"]
    n_bad = 0
    for c in cop:
        b = blobs.get(c["dst"])
        if b is None or len(b) != c["bytes"] or sha(b) != c["sha256"]:
            n_bad += 1
    ck("B", "manifest_entries", 233, len(cop))
    ck("B", "manifest_byte_sha_mismatches", 0, n_bad)
    ck("B", "manifest_skipped", 0, len(man.get("skipped", [])))
    ck("B", "all_233_present_and_identical", True, n_bad == 0 and len(cop) == 233)
    # distinct dst paths
    ck("B", "manifest_distinct_dst", 233, len({c["dst"] for c in cop}))

    # ---- group C: REAL credential values, broader independent patterns ---
    # A real value = a recognised prefix followed by a long opaque body, OR a
    # secret-key assignment whose RHS is a long opaque literal, OR a PEM block.
    pats = [
        ("github_pat", rb"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
        ("github_tok", rb"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
        ("google_key", rb"\bAIza[0-9A-Za-z_\-]{30,}\b"),
        ("aws_key", rb"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
        ("openai_key", rb"\bsk-(?:proj-)?[A-Za-z0-9_\-]{24,}\b"),
        ("slack_tok", rb"\bxox[baprs]-[A-Za-z0-9\-]{16,}\b"),
        ("jwt", rb"\beyJ[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{10,}\b"),
        ("bearer_long", rb"(?i)bearer\s+[A-Za-z0-9_\-\.]{32,}"),
        ("pem", rb"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
        ("assign_quoted", rb"(?i)\b(?:password|passwd|api[_-]?key|secret[_-]?key|client[_-]?secret|access[_-]?token|auth[_-]?token)\b\s*[:=]\s*[\"'][A-Za-z0-9_\-/.+]{16,}[\"']"),
        ("assign_bare", rb"(?i)\b(?:api[_-]?key|token|secret)\s*=\s*[A-Za-z0-9_\-]{32,}\b"),
        ("hex_secret", rb"(?i)\b(?:secret|token|key)[_-]?(?:hex|sha)?\s*[:=]\s*[\"']?[0-9a-f]{40,}\b"),
    ]
    cred_hits = []
    for path, b in blobs.items():
        for label, p in pats:
            for m in re.finditer(p, b):
                cred_hits.append({"path": path, "label": label, "offset": m.start(),
                                  "redacted": "<redacted>"})
    ck("C", "real_credential_value_hits", 0, len(cred_hits))
    # entropy-based sweep: any long opaque alnum run immediately after a
    # secret-ish keyword, with Shannon entropy >= 3.5 bits/char
    ent_hits = []
    kw = re.compile(rb"(?i)(gh[pousr]_|AIza|sk-|github_pat_|AKIA|ASIA|bearer\s+|api[_-]?key\s*[:=]\s*|token\s*[:=]\s*|secret\s*[:=]\s*)([A-Za-z0-9_\-]{28,})")
    for path, b in blobs.items():
        for m in kw.finditer(b):
            body = m.group(2).decode("ascii", "ignore")
            if len(body) >= 28 and entropy(body) >= 3.5:
                ent_hits.append({"path": path, "redacted": "<redacted>"})
    ck("C", "entropy_secret_candidates", 0, len(ent_hits))

    # ---- group D: size / weights / datasets -----------------------------
    big = [p for p, v in tree.items() if v["size"] > 50 * 1024 * 1024]
    bad_ext = (".pt", ".pth", ".ckpt", ".safetensors", ".onnx", ".h5", ".hdf5",
               ".npy", ".npz", ".pkl", ".pickle", ".parquet", ".dylib", ".so",
               ".bin", ".zip", ".tar", ".gz", ".7z", ".db", ".sqlite")
    wd = [p for p in tree if p.lower().endswith(bad_ext)]
    ck("D", "over_50MiB_files", 0, len(big))
    ck("D", "weights_dataset_suffix_files", 0, len(wd))
    ck("D", "max_file_bytes", 2149921, max(v["size"] for v in tree.values()))

    # ---- group E: published score lines / governing integrity -----------
    sr = re.compile(rb"^\*\*Overall:\*\*\s*([0-9]+(?:\.[0-9]+)?)", re.M)
    pub = []
    for p, b in blobs.items():
        if p.lower().endswith((".md", ".txt")):
            for m in sr.finditer(b):
                pub.append((p, m.group(1).decode()))
    ck("E", "published_numeric_overall_lines", 12, len(pub))
    ck("E", "published_score_lines_all_in_research_reviews", True,
       all(p.startswith("research/reviews/") for p, _ in pub))
    ck("E", "published_values_sorted_equals_expected", True,
       sorted(v for _, v in pub) == sorted(["7.5", "7.5", "8.2", "8.2", "7.0",
                                            "7.5", "7.5", "6.9", "6.3", "5.4",
                                            "5.2", "6"]))
    ck("E", "r95_governing_value", True,
       any(p.endswith("r95-independent-review-20261111.md") and v == "6"
           for p, v in pub))
    ck("E", "no_score_line_after_r95_date", True,
       all(("20261111" in p) or ("20261110" in p) or ("20261108" in p) for p, _ in pub))

    # ---- group F: live gates --------------------------------------------
    v = subprocess.run(["/Users/xhf/miniconda3/bin/python",
                        str(ROOT / "readonly-validator/validate_single_paper.py")],
                       capture_output=True, cwd=str(ROOT))
    vj = json.loads(v.stdout)
    ck("F", "validator_verdict", "NOT_QUALIFIED", vj["verdict"])
    ck("F", "validator_threshold", 7.0, vj["threshold"])
    ck("F", "validator_overall_score", 6.0, vj["overall_score"])
    ck("F", "validator_score_meets_threshold", False, vj["score_meets_threshold"])
    ck("F", "validator_checks", [True, False, False, True, False],
       [vj["checks"][k]["pass"] for k in
        ["D1_guidance_validated", "D2_tex_pdf_pipeline_all_passed",
         "D3_independent_full_review", "D4_novix_experiment_evidence",
         "D5_six_sections_traceability"]])
    gl = (ROOT / "guard/ledger-null-ladder.json").read_bytes()
    gc = (ROOT / "guard/criteria-null-ladder.json").read_bytes()
    ledger = json.loads(gl)
    ck("F", "guard_ledger_sha16", "73043b4e164a5a5f", sha(gl)[:16])
    ck("F", "guard_criteria_sha16", "94846083217df86f", sha(gc)[:16])
    ck("F", "guard_actions_len", 0, len(ledger["actions"]))
    ck("F", "guard_acceptance_ids", ["A1", "A2", "A3", "A4", "A5", "A6"],
       [a["id"] for a in ledger["acceptance"]])

    # ---- group G: mainline stage state (zero gate progression) ----------
    ps = json.loads((ROOT / "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json").read_text())
    stages = {s["id"]: s for s in ps["stages"]}
    ck("G", "stage_count", 12, len(stages))
    ck("G", "CCFA_startup_passed", "passed", stages["CCFA-startup"]["status"])
    pending = ["G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
               "validation", "handoff"]
    ck("G", "all_remaining_stages_pending", True,
       all(stages[k]["status"] == "pending" for k in pending))
    ck("G", "G0_inputs_empty", 0, len(stages["G0"]["inputs"]))
    ck("G", "G0_evidence_empty", 0, len(stages["G0"]["evidence"]))

    # ---- structural authority anchors (re-derived here) -----------------
    auth_rel = ["goal-ledger.md",
                "readonly-validator/validate_single_paper.py",
                "guard/criteria-null-ladder.json",
                "guard/ledger-null-ladder.json",
                "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json",
                "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/literature-baseline-matrix.md",
                "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/literature-search/source-manifest.json"]
    anchors = {r: sha((ROOT / r).read_bytes()) for r in auth_rel}

    matches = sum(1 for r in rows if r["match"])
    out = {
        "scope": "READONLY_POST_MERGE_PUBLIC_MAIN_TREE_ATTESTATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
        "independence": "recomputed from committed main-tree blobs + live gate runs; "
                        "does not import R128-ACQUIRE.py; no R128 JSON used as a data source; "
                        "group A is a declared same-machine byte-identity consistency check",
        "checks_total": len(rows), "matches": matches,
        "mismatches": [r for r in rows if not r["match"]],
        "group_counts": {g: sum(1 for r in rows if r["group"] == g) for g in "ABCDEFG"},
        "real_credential_value_hits": len(cred_hits),
        "entropy_secret_candidates": len(ent_hits),
        "structural_authority_anchors": anchors,
        "rows": rows,
    }
    (OUT / "R128-VERIFICATION.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"checks_total": len(rows), "matches": matches,
                      "mismatches": len(out["mismatches"]),
                      "group_counts": out["group_counts"],
                      "real_credential_value_hits": len(cred_hits),
                      "entropy_secret_candidates": len(ent_hits)}, indent=2))
    if out["mismatches"]:
        print("MISMATCH_DETAIL:", json.dumps(out["mismatches"], indent=2))


if __name__ == "__main__":
    main()

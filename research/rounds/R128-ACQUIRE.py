#!/usr/bin/env python3
"""R128 read-only acquisition: post-merge PUBLIC default-branch attestation.

Scope (strictly read-only on the primary project and on the sync repo objects):
  - Read the committed tree of ref `main` (= the PUBLIC default branch after
    R127 merge) through git object storage. Files are read from blobs, not from
    the working tree, so the attestation is about the published bytes.
  - Recompute SHA-256 of all 233 entries declared in research/UPLOAD-MANIFEST.json
    against those published blobs (full-open archive integrity after merge).
  - Scan every published file for REAL credential VALUES (the owner's sole hard
    exclusion). Scan-pattern literals such as b"ghp_" are explicitly classified
    as non-secrets and reported separately, per the R126 note.
  - Check >50 MiB, model weights / dataset / third-party-source suffixes.
  - Census strict numeric `**Overall:**` lines in the published tree.
  - Capture double-gate readouts and structural-authority byte anchors.

This script WRITES ONLY into its own round directory (post-merge-R128/).
It does not modify the primary project state, any gate, score, manuscript,
review, ledger, registry, matrix, or the sync repository.
"""
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision")
REPO = Path("/Users/xhf/Downloads/phd/4090/research-sync-public")
OUT = ROOT / "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/post-merge-R128"
REVIEW_DIR = ROOT / "ccfa-review-reports"
MANIFEST_REL = "research/UPLOAD-MANIFEST.json"


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def main():
    ts = datetime.now(timezone.utc).isoformat()
    facts = {"scope": "READONLY_POST_MERGE_PUBLIC_MAIN_TREE_ATTESTATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
             "collected_at_utc": ts, "python": sys.executable}

    # ---- A. ref identity -------------------------------------------------
    refs = {}
    for name, argv in [
        ("local_main", ["rev-parse", "main"]),
        ("local_head", ["rev-parse", "HEAD"]),
        ("remote_main", ["ls-remote", "origin", "refs/heads/main"]),
        ("agent_branch", ["rev-parse", "agent/r109-harbor-sync/wb-main"]),
        ("remote_agent", ["ls-remote", "origin", "refs/heads/agent/r109-harbor-sync/wb-main"]),
        ("tree", ["rev-parse", "main^{tree}"]),
        ("status_porcelain", ["status", "--porcelain"]),
    ]:
        r = git(*argv)
        refs[name] = r.stdout.decode("utf-8", "replace").strip()
    facts["refs"] = refs

    # ---- B. enumerate the committed `main` tree ------------------------
    r = git("ls-tree", "-r", "-l", "-z", "main")
    entries = []
    for chunk in r.stdout.split(b"\0"):
        if not chunk:
            continue
        meta, _, path = chunk.partition(b"\t")
        parts = meta.split()
        # 100644 blob <sha> <size>
        entries.append({"mode": parts[0].decode(), "type": parts[1].decode(),
                        "blob": parts[2].decode(), "size": int(parts[3]),
                        "path": path.decode("utf-8", "surrogateescape")})
    facts["tree_file_count"] = len(entries)
    facts["tree_total_bytes"] = sum(e["size"] for e in entries)

    # ---- C. read all blobs through `git cat-file --batch` ----------------
    payload = b"".join((e["blob"] + "\n").encode() for e in entries)
    cp = subprocess.run(["git", "-C", str(REPO), "cat-file", "--batch"],
                        input=payload, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    buf = cp.stdout
    pos = 0
    blobs = {}
    for _ in entries:
        nl = buf.index(b"\n", pos)
        header = buf[pos:nl].decode()
        pos = nl + 1
        hparts = header.split()
        # <requested> blob <size>
        oid, typ, size = hparts[0], hparts[1], int(hparts[2])
        data = buf[pos:pos + size]
        pos += size + 1  # trailing LF
        blobs[oid] = data
    facts["blobs_read"] = len(blobs)
    facts["blobs_read_all_match_sizes"] = all(len(blobs[e["blob"]]) == e["size"] for e in entries)

    # ---- D. real-credential-VALUE scan + pattern-literal classification -
    # A REAL value needs a known token prefix followed by a long opaque body.
    # Scan-pattern literals (b"ghp_", regex char classes, narrative) carry only
    # the prefix and are classified separately, never treated as a secret.
    real_patterns = {
        "github_token": re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
        "github_pat": re.compile(rb"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
        "google_api_key": re.compile(rb"\bAIza[0-9A-Za-z_\-]{30,}\b"),
        "aws_access_key": re.compile(rb"\bAKIA[0-9A-Z]{16}\b"),
        "openai_style_key": re.compile(rb"\bsk-[A-Za-z0-9_\-]{24,}\b"),
        "slack_token": re.compile(rb"\bxox[baprs]-[A-Za-z0-9\-]{16,}\b"),
        "private_key_block": re.compile(rb"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
        "assigned_secret": re.compile(
            rb"(?i)\b(?:password|passwd|api[_-]?key|access[_-]?token|secret[_-]?key|client[_-]?secret)\b"
            rb"\s*[:=]\s*[\"']([A-Za-z0-9_\-/.+]{16,})[\"']"),
    }
    literal_markers = {
        "gh_scan_literal": re.compile(rb"gh[pousr]_"),
        "AIza_scan_literal": re.compile(rb"AIza"),
        "b_quote_ghp": re.compile(rb"b[\"']gh[pousr]_"),
    }
    real_hits = []
    literal_files = {}
    per_file_sha = {}
    for e in entries:
        data = blobs[e["blob"]]
        per_file_sha[e["path"]] = {"sha256": sha256(data), "bytes": len(data), "git_blob": e["blob"]}
        for label, rx in real_patterns.items():
            for m in rx.finditer(data):
                real_hits.append({"path": e["path"], "label": label,
                                  "offset": m.start(),
                                  "redacted": "<redacted>"})
        lf = []
        for label, rx in literal_markers.items():
            n = len(rx.findall(data))
            if n:
                lf.append({"label": label, "occurrences": n})
        if lf:
            literal_files[e["path"]] = lf
    facts["real_credential_value_hits"] = len(real_hits)
    facts["real_credential_value_hits_detail"] = real_hits
    facts["scan_pattern_literal_files"] = literal_files
    facts["scan_pattern_literal_file_count"] = len(literal_files)

    # ---- E. size / weight / dataset / binary checks ---------------------
    BIG = 50 * 1024 * 1024
    bad_suffix = (".pt", ".pth", ".ckpt", ".safetensors", ".onnx", ".h5", ".hdf5",
                   ".npy", ".npz", ".pkl", ".pickle", ".parquet", ".dylib", ".so",
                   ".bin", ".zip", ".tar", ".tar.gz", ".7z", ".db", ".sqlite")
    facts["over_50MiB"] = [{"path": e["path"], "bytes": e["size"]} for e in entries if e["size"] > BIG]
    facts["max_file_bytes"] = max(e["size"] for e in entries)
    facts["weights_datasets_suffix_hits"] = [
        {"path": e["path"], "bytes": e["size"]} for e in entries
        if e["path"].lower().endswith(bad_suffix)]
    # PDF is a legitimate manuscript artifact, not a binary model/dataset blob.
    facts["pdf_files"] = [{"path": e["path"], "bytes": e["size"]}
                         for e in entries if e["path"].lower().endswith(".pdf")]

    # ---- F. UPLOAD-MANIFEST integrity against published blobs ----------
    man_blob = blobs.get(per_file_sha.get(MANIFEST_REL, {}).get("git_blob", ""), b"")
    manifest = json.loads(man_blob.decode("utf-8"))
    copied = manifest["copied"]
    mismatches = []
    for c in copied:
        got = per_file_sha.get(c["dst"])
        if got is None:
            mismatches.append({"dst": c["dst"], "reason": "missing_from_main_tree"})
        elif got["bytes"] != c["bytes"] or got["sha256"] != c["sha256"]:
            mismatches.append({"dst": c["dst"], "reason": "bytes_or_sha_mismatch",
                               "declared": {"bytes": c["bytes"], "sha256": c["sha256"]},
                               "published": {"bytes": got["bytes"], "sha256": got["sha256"]}})
    facts["upload_manifest"] = {
        "path": MANIFEST_REL,
        "sha256": sha256(man_blob),
        "bytes": len(man_blob),
        "entries": len(copied),
        "skipped": len(manifest.get("skipped", [])),
        "verified_matches": len(copied) - len(mismatches),
        "mismatches": mismatches,
        "all_233_byte_identical": len(mismatches) == 0 and len(copied) == 233,
    }

    # ---- G. strict numeric Overall census in the published tree ---------
    score_rx = re.compile(rb"^\*\*Overall:\*\*\s*([0-9]+(?:\.[0-9]+)?)", re.M)
    pub_scores = []
    for e in entries:
        if not e["path"].lower().endswith((".md", ".txt")):
            continue
        for m in score_rx.finditer(blobs[e["blob"]]):
            pub_scores.append({"path": e["path"], "value": m.group(1).decode()})
    facts["published_numeric_overall_lines"] = pub_scores
    # primary project: authoritative review dir + whole-project census
    prim = []
    for p in sorted(REVIEW_DIR.glob("*.md")):
        for m in score_rx.finditer(p.read_bytes()):
            prim.append({"path": str(p.relative_to(ROOT)), "value": m.group(1).decode(),
                          "mtime": datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).isoformat()})
    facts["primary_review_dir_scores"] = prim
    facts["primary_review_dir_newest"] = max(
        (p.stat().st_mtime for p in REVIEW_DIR.glob("*.md")), default=0)
    allproj = []
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        for m in score_rx.finditer(p.read_bytes()):
            allproj.append({"path": str(p.relative_to(ROOT)), "value": m.group(1).decode()})
    facts["primary_project_numeric_overall_lines"] = allproj
    facts["primary_project_numeric_overall_count"] = len(allproj)
    facts["primary_project_numeric_overall_files"] = len({x["path"] for x in allproj})

    # ---- H. double gates (read-only) ------------------------------------
    v = subprocess.run(["/Users/xhf/miniconda3/bin/python",
                        str(ROOT / "readonly-validator/validate_single_paper.py")],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=str(ROOT))
    vj = json.loads(v.stdout.decode())
    facts["validator"] = {
        "exit": v.returncode, "verdict": vj["verdict"], "threshold": vj["threshold"],
        "overall_score": vj["overall_score"],
        "score_meets_threshold": vj["score_meets_threshold"],
        "all_pass": vj["all_pass"],
        "checks": {k: x["pass"] for k, x in vj["checks"].items()},
        "governing_detail": vj["checks"]["D3_independent_full_review"]["detail"],
    }
    gl = (ROOT / "guard/ledger-null-ladder.json").read_bytes()
    gc = (ROOT / "guard/criteria-null-ladder.json").read_bytes()
    ledger = json.loads(gl)
    facts["guard"] = {
        "ledger_sha16": sha256(gl)[:16], "criteria_sha16": sha256(gc)[:16],
        "ledger_bytes": len(gl), "criteria_bytes": len(gc),
        "acceptance_ids": [a.get("id") for a in ledger["acceptance"]],
        "acceptance_status": {a.get("id"): a.get("status") for a in ledger["acceptance"]},
        "actions_len": len(ledger["actions"]),
        "steps": {s.get("id"): s.get("status") for s in ledger.get("steps", [])},
    }

    # ---- I. structural authority byte anchors (zero-writeback baseline) --
    auth_rel = [
        "goal-ledger.md",
        "readonly-validator/validate_single_paper.py",
        "guard/criteria-null-ladder.json",
        "guard/ledger-null-ladder.json",
        "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json",
        "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/literature-baseline-matrix.md",
        "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/literature-search/source-manifest.json",
    ]
    anchors = {}
    for rel in auth_rel:
        p = ROOT / rel
        anchors[rel] = {"bytes": p.stat().st_size, "sha256": sha256(p.read_bytes())} if p.is_file() else None
    facts["structural_authority_anchors"] = anchors

    # pipeline-state stage census
    ps = json.loads((ROOT / auth_rel[4]).read_text())
    facts["mainline_stages"] = {s["id"]: {"status": s["status"],
                                          "inputs": len(s.get("inputs", [])),
                                          "evidence": len(s.get("evidence", []))}
                                for s in ps["stages"]}

    (OUT / "R128-ACQUIRE.json").write_text(json.dumps(facts, indent=2, ensure_ascii=False) + "\n")
    # frozen raw needles for the independent verifier (derived here, but the
    # verifier must recompute from source blobs, not consume this file).
    (OUT / "raw" / "tree_paths.txt").write_text(
        "\n".join(e["path"] + "\t" + e["blob"] + "\t" + str(e["size"]) for e in entries) + "\n")
    print(json.dumps({
        "collected_at_utc": ts,
        "tree_file_count": facts["tree_file_count"],
        "tree_total_bytes": facts["tree_total_bytes"],
        "real_credential_value_hits": facts["real_credential_value_hits"],
        "scan_pattern_literal_file_count": facts["scan_pattern_literal_file_count"],
        "upload_manifest_entries": facts["upload_manifest"]["entries"],
        "upload_manifest_verified_matches": facts["upload_manifest"]["verified_matches"],
        "upload_manifest_all_233_byte_identical": facts["upload_manifest"]["all_233_byte_identical"],
        "max_file_bytes": facts["max_file_bytes"],
        "over_50MiB": len(facts["over_50MiB"]),
        "weights_datasets_suffix_hits": len(facts["weights_datasets_suffix_hits"]),
        "published_numeric_overall_lines": len(pub_scores),
        "primary_project_numeric_overall_count": facts["primary_project_numeric_overall_count"],
        "validator": facts["validator"]["verdict"],
        "validator_score": facts["validator"]["overall_score"],
        "guard_actions": facts["guard"]["actions_len"],
    }, indent=2))


if __name__ == "__main__":
    main()

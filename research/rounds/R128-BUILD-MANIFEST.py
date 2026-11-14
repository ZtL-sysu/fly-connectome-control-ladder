#!/usr/bin/env python3
"""R128 checkpoint manifest builder: create / verify.

NOTE: collaboration/PROTOCOL.md §"Checkpoint cadence" item 3 names
`checkpoint_manifest.py`. No such file exists anywhere in either workspace
(verified by find over /Users/xhf/Downloads/phd/4090 and ~/.workbuddy/skills).
Prior rounds therefore appear to have generated manifests with ad-hoc code.
This frozen round-local script implements the SAME observed schema (from the
R126 checkpoint manifest.json) with explicit create/verify modes, so the
checkpoint is reproducible. It writes only its own checkpoint manifest.json.

Schema: schema_version, task_id, agent_id, created_at_utc, status,
input_git_head, protocol{path,sha256,bytes}, artifacts[{path,sha256,bytes}].
Paths are repo-relative; the manifest never contains its own hash.
"""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/Users/xhf/Downloads/phd/4090/research-sync-public")
CK_REL = "collaboration/tasks/r109-harbor-sync/agents/wb-main/checkpoints/20261114T113553Z-r128-post-merge-attestation"
PROTOCOL_REL = "collaboration/PROTOCOL.md"

# Explicit whitelist — protocol §"GitHub 同步" item 1: never `git add .`.
ARTIFACTS = [
    "AGENTS.md",
    # NOTE (v3 fix): root README.md exists ONLY on `main` (added by R127's
    # post-merge docs commit). This checkpoint is published on the agent branch,
    # which is still pre-merge, so root README.md is NOT present here and must
    # not be listed. We do not copy integrator-owned main-only files across.
    PROTOCOL_REL,
    "collaboration/PROJECT.md",
    "collaboration/tasks/r109-harbor-sync/TASK.md",
    "collaboration/tasks/r109-harbor-sync/agents/wb-main/HANDOFF.md",
    "collaboration/tasks/r109-harbor-sync/agents/wb-main/LOG.md",
    "research/README.md",
    "research/UPLOAD-MANIFEST.json",
    CK_REL + "/CHECKPOINT.md",
    CK_REL + "/metrics.csv",
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(*a):
    return subprocess.run(["git", "-C", str(REPO), *a],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode().strip()


def build():
    proto = (REPO / PROTOCOL_REL).read_bytes()
    arts = []
    for rel in ARTIFACTS:
        p = REPO / rel
        b = p.read_bytes()
        arts.append({"path": rel, "sha256": sha(b), "bytes": len(b)})
    return {
        "schema_version": 1,
        "task_id": "r109-harbor-sync",
        "agent_id": "wb-main",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "in_progress",
        "input_git_head": git("rev-parse", "HEAD"),
        "protocol": {"path": PROTOCOL_REL, "sha256": sha(proto), "bytes": len(proto)},
        "artifacts": arts,
    }


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "verify"
    mf = REPO / CK_REL / "manifest.json"
    if mode == "create":
        data = build()
        mf.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        print("create: OK, artifacts =", len(data["artifacts"]),
              "input_git_head =", data["input_git_head"])
        return
    data = json.loads(mf.read_text())
    ok = True
    for a in data["artifacts"]:
        p = REPO / a["path"]
        if not p.is_file():
            print("MISSING", a["path"]); ok = False; continue
        b = p.read_bytes()
        if len(b) != a["bytes"] or sha(b) != a["sha256"]:
            print("CHANGED", a["path"]); ok = False
    proto = (REPO / data["protocol"]["path"]).read_bytes()
    if sha(proto) != data["protocol"]["sha256"]:
        print("CHANGED protocol"); ok = False
    print("verify:", "OK" if ok else "FAILED",
          "artifacts =", len(data["artifacts"]),
          "| bytes verified; no scientific or remote-sync claim")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

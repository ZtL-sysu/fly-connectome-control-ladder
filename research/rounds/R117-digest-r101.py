#!/usr/bin/env python
"""R117 post-review correction: persist the R101-rule state-dict digest.

Motivation: the R117 independent review (section 6, item 1) correctly found
that "state-dict digest recomputed under R101's original rule = 67ce06c5..."
was only a text assertion in EVIDENCE.md / ROUND-AUDIT.md: the on-disk probe
script uses a different framing (one extra trailing \\0), and no verify check
covered the R101 rule. This script closes that *reproducibility gap* with a
first-hand recomputation written to disk. It does NOT modify any existing
byte, does NOT pass any gate, and does NOT produce a scientific result.

Both framings are recomputed from the same on-disk checkpoint bytes so the
difference is demonstrably framing-only, not a data inconsistency.

Run with: /Users/xhf/miniconda3/envs/ceg_snn_mi/bin/python R117-digest-r101.py
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
CHKPT = RUN / "sources/flyvis-pretrained-access/unpacked/results/flow/0000/000/chkpts/chkpt_00000"
R101_REGISTERED = "67ce06c5cec0a4cda9937b17f061db0c99ad9f76c0224874c9b3a673c2e13a82"
R117_PROBE_VARIANT = "bd3f2cc8a037e1f58517989fced0f233a97e647f3ab9545d865e8bb416e25f74"

import torch


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def walk(o, prefix=""):
    if isinstance(o, torch.Tensor):
        yield prefix, o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, f"{prefix}/{k}" if prefix else str(k))
    elif isinstance(o, (list, tuple)):
        for i, v in enumerate(o):
            yield from walk(v, f"{prefix}/{i}")


obj = torch.load(str(CHKPT), map_location="cpu", weights_only=True)
tensors = sorted(walk(obj), key=lambda kv: kv[0])
raw_bytes = [t.detach().contiguous().cpu().numpy().tobytes() for _, t in tensors]
total_raw = sum(len(b) for b in raw_bytes)


def digest(trailing_nul: bool) -> str:
    h = hashlib.sha256()
    for (key, t), raw in zip(tensors, raw_bytes):
        h.update(key.encode("utf-8")); h.update(b"\0")
        h.update(str(t.dtype).encode()); h.update(b"\0")
        h.update(str(tuple(t.shape)).encode()); h.update(b"\0")
        h.update(raw + (b"\0" if trailing_nul else b""))
    return h.hexdigest()


d_r101 = digest(False)
d_probe = digest(True)

out = {
    "round": "R117",
    "classification": "POST_REVIEW_FIRST_HAND_RECOMPUTATION_NOT_SCIENTIFIC_RESULT_NOT_GATE_PASS",
    "purpose": "Close the R117 independent review section 6 item 1 reproducibility gap: persist the R101-original-rule digest instead of asserting it only in prose.",
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "generated_utc_note": "Product-generation wall clock; NOT an acquisition timestamp (R115 W3).",
    "python": "/Users/xhf/miniconda3/envs/ceg_snn_mi/bin/python",
    "checkpoint_path": "sources/flyvis-pretrained-access/unpacked/results/flow/0000/000/chkpts/chkpt_00000",
    "checkpoint_bytes": CHKPT.stat().st_size,
    "checkpoint_sha256": sha256_file(CHKPT),
    "tensor_count": len(tensors),
    "total_raw_tensor_bytes": total_raw,
    "same_source_bytes_for_both_framings": True,
    "framings": {
        "R101_original_rule": {
            "description": "sorted key\\0dtype\\0shape\\0raw_bytes, NO trailing NUL (R101 weights_only_restore_probe.py lines 147-158)",
            "digest_sha256": d_r101,
            "registered_r101_value": R101_REGISTERED,
            "match": d_r101 == R101_REGISTERED,
        },
        "R117_probe_variant": {
            "description": "same fields PLUS one extra trailing NUL after raw_bytes (R117-probe.py RESTORE_SRC)",
            "digest_sha256": d_probe,
            "raw_json_value": R117_PROBE_VARIANT,
            "match": d_probe == R117_PROBE_VARIANT,
        },
    },
    "both_match": d_r101 == R101_REGISTERED and d_probe == R117_PROBE_VARIANT,
    "conclusion": "Both framings operate on the same 14 tensors and identical raw bytes; the two digest values differ ONLY by framing. Not a data inconsistency (R101 independent review 67ce06c5 vs 297e43d7 precedent).",
    "strict_boundary": {
        "forward_pass": False, "inference": False, "training": False,
        "label_read": False, "scientific_metric": False, "gate_promotion": False,
        "network_constructed": False, "existing_bytes_modified": False,
    },
}
dest = HERE / "R117-DIGEST-RECOMPUTE.json"
dest.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({
    "output": str(dest.relative_to(RUN)), "bytes": dest.stat().st_size,
    "sha256": hashlib.sha256(dest.read_bytes()).hexdigest(),
    "R101_rule_digest": d_r101, "R101_match": d_r101 == R101_REGISTERED,
    "probe_variant_digest": d_probe, "probe_match": d_probe == R117_PROBE_VARIANT,
    "both_match": out["both_match"], "tensor_count": len(tensors),
    "total_raw_tensor_bytes": total_raw,
}, indent=2, ensure_ascii=False))

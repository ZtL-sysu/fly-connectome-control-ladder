#!/usr/bin/env python3
"""R108 frozen CUDA/GPU environment probe. ENGINEERING ONLY.

Deterministic, tiny, hash-verifiable. No training, no labels, no dataset,
no real model forward. Writes a result.json that the verifier independently
re-computes from raw values.
"""
import hashlib
import json
import math
import os
from pathlib import Path
from datetime import datetime, timezone

OUT = Path("results/r108_probe")
SELF = Path("tests/probe.py")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    self_sha = hashlib.sha256(SELF.read_bytes()).hexdigest()
    report = {
        "status": "running",
        "scope": "ENGINEERING_ENVIRONMENT_PROBE_ONLY",
        "scientific_result": False,
        "training": False,
        "labels_used": False,
        "dataset_download": False,
        "probe_script_sha256": self_sha,
        "utc_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    try:
        import torch
        report["python_import_ok"] = True
        report["torch_version"] = str(torch.__version__)
        report["cuda_available"] = bool(torch.cuda.is_available())
        report["device_count"] = int(torch.cuda.device_count()) if torch.cuda.is_available() else 0
        if torch.cuda.is_available():
            report["device_name"] = torch.cuda.get_device_name(0)
            report["driver_or_cuda"] = str(torch.version.cuda)
        else:
            report["device_name"] = "NO_GPU"
            report["driver_or_cuda"] = None
        # Deterministic probe: same arithmetic on CPU and CUDA.
        base = [float(i + 1) for i in range(16)]
        xt = torch.tensor(base, dtype=torch.float64).reshape(4, 4)
        w = torch.tensor([[1.0, 0.0, 0.0, 0.0],
                          [0.0, 2.0, 0.0, 0.0],
                          [0.0, 0.0, 3.0, 0.0],
                          [0.0, 0.0, 0.0, 4.0]], dtype=torch.float64)
        expected = (xt @ w).sum().item()
        if torch.cuda.is_available():
            got = (xt.cuda() @ w.cuda()).sum().item()
        else:
            got = (xt @ w).sum().item()
        vals = (xt @ w).reshape(-1).tolist()
        report["probe_device"] = "cuda" if torch.cuda.is_available() else "cpu"
        report["probe_expected"] = float(expected)
        report["probe_observed"] = float(got)
        report["probe_matrix_flat"] = [float(v) for v in vals]
        report["all_finite"] = bool(all(math.isfinite(v) for v in vals))
        report["probe_ok"] = bool(math.isfinite(got) and abs(got - expected) < 1e-9)
        report["status"] = "success" if report["probe_ok"] else "failure"
    except Exception as exc:  # preserve verbatim, never fabricate
        report["status"] = "failure"
        report["error"] = f"{type(exc).__name__}: {exc}"
    (OUT / "result.json").write_text(json.dumps(report, indent=2) + "\n")
    files = {}
    for p in sorted(OUT.glob("*")):
        if p.is_file() and p.name != "manifest.json":
            files[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    (OUT / "manifest.json").write_text(json.dumps(
        {"status": report["status"], "files": files, "note": "manifest indexes other files; self-excluded"},
        indent=2) + "\n")
    print(json.dumps({"status": report["status"], "probe_device": report.get("probe_device")}))


if __name__ == "__main__":
    main()

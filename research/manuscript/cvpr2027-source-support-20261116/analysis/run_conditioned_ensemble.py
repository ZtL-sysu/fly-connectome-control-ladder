"""Ten-seed digit-parity MLP on the 0.1x degree-preserving draws.

Budget rule, fixed from the structural sweep before any of these accuracies
were computed: among multipliers {0.05, 0.1, 0.25, 0.5, 1, 2, 10}, take the
smallest at which at least 8 of 12 draws keep both source columns and fewer
than half keep the measured transfer. That multiplier is 0.1.

Every draw at that budget is scored, including the draw that lost a column.
Identical transfers are trained once. Two anchor transfers from the hand
edits are scored with the same trainer.
"""
from __future__ import annotations

import importlib.util
import json
import time
from pathlib import Path

import numpy as np

ROOT = Path("/Users/xhf/Downloads/phd/4090")
SWEEP = ROOT / "cvpr2027-rebuild/analysis/source_support/support_sweep.json"
OUT = ROOT / "cvpr2027-rebuild/analysis/source_support/conditioned_ensemble.json"
SEEDS = [11, 17, 23, 31, 41, 53, 67, 79, 97, 103]
ANCHORS = {
    "separate_routes": [[0.0625, 0.0], [0.0625, 0.0625]],
    "deleted_source": [[0.0625, 0.0], [0.0625, 0.0]],
}


def main():
    spec = importlib.util.spec_from_file_location(
        "rm", ROOT / "cvpr2027-rebuild/analysis/source_support/run_multiroute.py"
    )
    rm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rm)
    codes = rm.visual_codes()
    sweep = json.loads(SWEEP.read_text())
    rows = [r for r in sweep["rows"] if r["multiplier"] == 0.1]
    jobs = []
    for r in rows:
        jobs.append({
            "kind": "draw",
            "draw": r["draw"],
            "T": r["T"],
            "rank": r["rank"],
            "n_sources": r["n_sources"],
            "both": r["both"],
            "same_T": r["same_T"],
            "overlap": r["overlap"],
        })
    for name, T in ANCHORS.items():
        arr = np.array(T, dtype=np.float64)
        on = np.abs(arr).sum(0) > 1e-8
        jobs.append({
            "kind": "anchor",
            "name": name,
            "T": T,
            "rank": int(np.linalg.matrix_rank(arr, tol=1e-8)),
            "n_sources": int(on.sum()),
            "both": bool(on.all()),
            "same_T": False,
        })
    cache = {}
    t0 = time.time()
    scored = []
    for job in jobs:
        key = json.dumps(job["T"])
        if key not in cache:
            accs = [rm.run_model(np.array(job["T"], dtype=np.float64), seed, "parity", codes) for seed in SEEDS]
            cache[key] = {"values": accs, "mean": float(np.mean(accs))}
            print(f"trained {key} {cache[key]['mean']:.4f}", flush=True)
        job["accuracy"] = cache[key]
        scored.append(job)
        payload = {
            "budget_multiplier": 0.1,
            "seeds": SEEDS,
            "device": str(rm.DEVICE),
            "selection_rule": (
                "smallest sweep multiplier with at least 8/12 both-column draws "
                "and fewer than half identical to the measured transfer"
            ),
            "jobs": scored,
            "wall_s": round(time.time() - t0, 1),
        }
        OUT.write_text(json.dumps(payload, indent=2))
    print("DONE", payload["wall_s"], OUT)


if __name__ == "__main__":
    main()

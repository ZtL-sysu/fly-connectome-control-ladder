"""Structural sweep: how many degree-preserving swaps leave both source columns.

No accuracy is computed. Selection of later training graphs must use the
rule in the header of run_conditioned_ensemble.py, not these scores.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path("/Users/xhf/Downloads/phd/4090")
sys.path.insert(0, str(ROOT / "cvpr2027-rebuild/evidence/original_code/motif"))
from common import DiGraph, degree_preserving_rewire  # noqa: E402

OUT = ROOT / "cvpr2027-rebuild/analysis/source_support/support_sweep.json"
BASE = ROOT / "cvpr2027-rebuild/analysis/recovered_graphs/narrowk4_base.npz"
SOURCES = (6, 109)
SINKS = (4, 5)
MULTIPLIERS = [0.05, 0.1, 0.25, 0.5, 1, 2, 10]
N_DRAWS = 12


def transfer(g: DiGraph) -> np.ndarray:
    W = g.normalized_W().numpy()
    return (W @ W)[list(SINKS)][:, list(SOURCES)]


def main():
    t0 = time.time()
    z = np.load(BASE)
    g = DiGraph(len(z["body_ids"]), z["src"], z["dst"])
    base_in = g.in_degree().copy()
    base_out = g.out_degree().copy()
    base_edges = set(zip(g.src.tolist(), g.dst.tolist()))
    T0 = transfer(g)
    rows = []
    for mult in MULTIPLIERS:
        n_swaps = int(round(mult * g.n_edges))
        for s in range(N_DRAWS):
            rng = np.random.default_rng(120_000 + int(mult * 1000) * 100 + s)
            gr = degree_preserving_rewire(g, n_swaps, rng)
            T = transfer(gr)
            on = np.abs(T).sum(0) > 1e-8
            edges = set(zip(gr.src.tolist(), gr.dst.tolist()))
            rec = {
                "multiplier": mult,
                "swaps": n_swaps,
                "draw": s,
                "degree_node_match": bool(
                    np.array_equal(gr.in_degree(), base_in)
                    and np.array_equal(gr.out_degree(), base_out)
                ),
                "overlap": int(len(edges & base_edges)),
                "T": np.round(T, 6).tolist(),
                "rank": int(np.linalg.matrix_rank(T, tol=1e-8)),
                "n_sources": int(on.sum()),
                "both": bool(on.all()),
                "same_T": bool(np.allclose(T, T0, atol=1e-8)),
            }
            rows.append(rec)
            print(
                f"m={mult} d={s} both={rec['both']} n={rec['n_sources']} "
                f"rank={rec['rank']} same={rec['same_T']} ov={rec['overlap']}",
                flush=True,
            )
    payload = {
        "measured_T": np.round(T0, 6).tolist(),
        "n_edges": int(g.n_edges),
        "rows": rows,
        "wall_s": round(time.time() - t0, 1),
    }
    OUT.write_text(json.dumps(payload, indent=2))
    print("WROTE", OUT, payload["wall_s"])


if __name__ == "__main__":
    main()

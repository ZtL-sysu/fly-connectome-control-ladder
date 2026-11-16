"""Archive the 24-draw degree-preserving null used in the manuscript.

Seeds are 50_000 + s for s in 0..23, and the budget is 10 swaps per edge.
This file records support only. It does not train a readout.
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

BASE = ROOT / "cvpr2027-rebuild/analysis/recovered_graphs/narrowk4_base.npz"
OUT = ROOT / "cvpr2027-rebuild/analysis/source_support/degree24.json"
SOURCES = (6, 109)
SINKS = (4, 5)


def main():
    t0 = time.time()
    z = np.load(BASE)
    g = DiGraph(len(z["body_ids"]), z["src"], z["dst"])
    module = z["module_ids"]
    base_in = g.in_degree().copy()
    base_out = g.out_degree().copy()
    base_mod = g.module_pair_counts(module)
    base_edges = set(zip(g.src.tolist(), g.dst.tolist()))
    rows = []
    for s in range(24):
        rng = np.random.default_rng(50_000 + s)
        gr = degree_preserving_rewire(g, 10 * g.n_edges, rng)
        W = gr.normalized_W().numpy()
        T = (W @ W)[list(SINKS)][:, list(SOURCES)]
        on = np.abs(T).sum(0) > 1e-8
        edges = set(zip(gr.src.tolist(), gr.dst.tolist()))
        rows.append({
            "rewire_seed": int(50_000 + s),
            "swaps": int(10 * g.n_edges),
            "degree_node_match": bool(
                np.array_equal(gr.in_degree(), base_in)
                and np.array_equal(gr.out_degree(), base_out)
            ),
            "module_pair_match": gr.module_pair_counts(module) == base_mod,
            "overlap": int(len(edges & base_edges)),
            "T": np.round(T, 6).tolist(),
            "rank": int(np.linalg.matrix_rank(T, tol=1e-8)),
            "n_sources": int(on.sum()),
            "both": bool(on.all()),
        })
        print(s, rows[-1]["n_sources"], rows[-1]["rank"], flush=True)
    payload = {"rows": rows, "wall_s": round(time.time() - t0, 1)}
    OUT.write_text(json.dumps(payload, indent=2))
    print("WROTE", OUT)


if __name__ == "__main__":
    main()

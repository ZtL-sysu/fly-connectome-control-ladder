"""Pre-declared routes and degree-matched rewires that keep both sources.

Routes are the first three relays returned by the original motif rule on the
k=4 male visual subgraph. Nothing is selected from accuracy.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

ROOT = Path("/Users/xhf/Downloads/phd/4090")
sys.path.insert(0, str(ROOT / "cvpr2027-rebuild/evidence/original_code/motif"))
from common import DiGraph, degree_preserving_rewire  # noqa: E402

OUT = ROOT / "cvpr2027-rebuild/analysis/source_support/multiroute.json"
DENSE_PATH = ROOT / "cvpr2027-rebuild/analysis/recovered_graphs/rebuild_narrowk4/data/visual_graph.npz"
BASE_PATH = ROOT / "cvpr2027-rebuild/analysis/recovered_graphs/narrowk4_base.npz"
SEEDS = [11, 17, 23, 31, 41, 53]
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
N_PROTECTED = 4
N_OPEN = 2


def build_k4(z):
    src, dst, w = z["src"], z["dst"], z["weight"]
    n = len(z["body_ids"])
    sort_idx = np.lexsort((src, -w, dst))
    s_s, s_d = src[sort_idx], dst[sort_idx]
    _, starts = np.unique(s_d, return_index=True)
    ranks = np.arange(len(s_s)) - np.repeat(starts, np.diff(np.append(starts, len(s_s))))
    keep = ranks < k if (k := 4) else ranks < 4
    return DiGraph(n, s_s[keep], s_d[keep])


def find_routes(g: DiGraph, dense: DiGraph, limit=3):
    found = []
    for r in range(g.n):
        inn = np.sort(g.in_neighbors(r))
        outn = np.sort(g.out_neighbors(r))
        if len(inn) < 2 or len(outn) < 2:
            continue
        a, b = int(inn[0]), int(inn[1])
        s1, s2 = int(outn[0]), int(outn[1])
        if len({a, b, r, s1, s2}) < 5:
            continue
        if any(dense.has(u, s) for u in (a, b) for s in (s1, s2)):
            continue
        found.append({"relay": r, "a": a, "b": b, "s1": s1, "s2": s2})
        if len(found) >= limit:
            break
    return found


def transfer(g: DiGraph, route):
    W = g.normalized_W().numpy()
    sinks = [route["s1"], route["s2"]]
    sources = [route["a"], route["b"]]
    return (W @ W)[sinks][:, sources]


def support_edges(g: DiGraph, route):
    protected = set()
    sources = (route["a"], route["b"])
    sinks = (route["s1"], route["s2"])
    for u in sources:
        for r in g.out_neighbors(u):
            r = int(r)
            if any(g.has(r, s) for s in sinks):
                protected.add((u, r))
                for s in sinks:
                    if g.has(r, s):
                        protected.add((r, s))
    return protected


def visual_codes():
    from sklearn.datasets import load_digits
    digits = load_digits()
    images = digits.images.astype(np.float64) / 16.0
    upper = images[:, :4].reshape(len(images), -1)
    lower = images[:, 4:].reshape(len(images), -1)
    rng = np.random.default_rng(20261116)
    q, _ = np.linalg.qr(rng.standard_normal((32, 16)))
    proj = q[:, :16]
    return {
        "upper": (upper @ proj).astype(np.float32),
        "lower": (lower @ proj).astype(np.float32),
        "parity": digits.target % 2,
        "label": digits.target.astype(np.int64),
    }


def parity_batch(rng, n, codes):
    cls = rng.integers(0, 2, size=(n, 2))
    feats = np.zeros((n, 2, 16), dtype=np.float32)
    for source, field in ((0, "upper"), (1, "lower")):
        for bit in (0, 1):
            pool = np.flatnonzero(codes["parity"] == bit)
            take = np.flatnonzero(cls[:, source] == bit)
            choice = rng.choice(pool, size=len(take), replace=True)
            feats[take, source] = codes[field][choice]
    y = (cls[:, 0] ^ cls[:, 1]).astype(np.float32)
    return feats, y


def digit_batch(rng, n, codes):
    choice = rng.integers(0, len(codes["label"]), size=n)
    feats = np.stack([codes["upper"][choice], codes["lower"][choice]], axis=1)
    return feats, codes["label"][choice]


def run_model(T, seed, task, codes):
    torch.manual_seed(seed)
    n_out = 1 if task == "parity" else 10
    model = torch.nn.Sequential(
        torch.nn.Linear(32, 64), torch.nn.ReLU(), torch.nn.Linear(64, n_out)
    ).to(DEVICE)
    opt = torch.optim.Adam(model.parameters(), lr=0.006)
    loss_fn = torch.nn.BCEWithLogitsLoss() if task == "parity" else torch.nn.CrossEntropyLoss()
    data_rng = np.random.default_rng(1_000_003 + seed + (0 if task == "parity" else 17))
    Tt = torch.tensor(T, dtype=torch.float32, device=DEVICE)
    for _ in range(120 * 32):
        if task == "parity":
            feats, y = parity_batch(data_rng, 128, codes)
            yt = torch.tensor(y, device=DEVICE)
        else:
            feats, y = digit_batch(data_rng, 128, codes)
            yt = torch.tensor(y, device=DEVICE)
        ft = torch.tensor(feats, device=DEVICE)
        mixed = torch.einsum("ij,bjf->bif", Tt, ft).reshape(128, -1)
        pred = model(mixed)
        loss = loss_fn(pred.squeeze(-1), yt) if task == "parity" else loss_fn(pred, yt)
        opt.zero_grad()
        loss.backward()
        opt.step()
    eval_rng = np.random.default_rng(2_000_003 + seed + (0 if task == "parity" else 17))
    if task == "parity":
        feats, y = parity_batch(eval_rng, 2048, codes)
    else:
        feats, y = digit_batch(eval_rng, 2048, codes)
    with torch.no_grad():
        ft = torch.tensor(feats, device=DEVICE)
        mixed = torch.einsum("ij,bjf->bif", Tt, ft).reshape(len(y), -1)
        pred = model(mixed)
        if task == "parity":
            hat = (pred.squeeze(-1) > 0).cpu().numpy()
        else:
            hat = pred.argmax(-1).cpu().numpy()
    return float(np.mean(hat == y))


def column_info(T):
    on = (np.abs(T).sum(0) > 1e-8)
    return {
        "T": np.round(T, 6).tolist(),
        "rank": int(np.linalg.matrix_rank(T, tol=1e-8)),
        "n_sources": int(on.sum()),
        "both": bool(on.all()),
    }


def main():
    t0 = time.time()
    z = np.load(DENSE_PATH, allow_pickle=True)
    base_z = np.load(BASE_PATH)
    g = build_k4(z)
    dense = DiGraph(len(z["body_ids"]), z["src"], z["dst"])
    assert np.array_equal(z["body_ids"], base_z["body_ids"])
    base_in = np.sort(g.in_degree())
    base_out = np.sort(g.out_degree())
    routes = find_routes(g, dense, 3)
    codes = visual_codes()
    payload = {"device": str(DEVICE), "seeds": SEEDS, "routes": []}
    for i, route in enumerate(routes):
        protected = support_edges(g, route)
        graphs = [("measured", g, None)]
        for s in range(N_PROTECTED):
            rng = np.random.default_rng(80_000 + 100 * i + s)
            gr = degree_preserving_rewire(g, 10 * g.n_edges, rng, protected=protected)
            graphs.append((f"protected_{s}", gr, protected))
        for s in range(N_OPEN):
            rng = np.random.default_rng(90_000 + 100 * i + s)
            gr = degree_preserving_rewire(g, 10 * g.n_edges, rng)
            graphs.append((f"open_{s}", gr, None))
        route_rec = {
            "index": i,
            "route": route,
            "body_ids": {k: int(base_z["body_ids"][route[k]]) for k in ("a", "b", "relay", "s1", "s2")},
            "n_protected_edges": len(protected),
            "graphs": [],
        }
        for name, gr, prot in graphs:
            T = transfer(gr, route)
            info = column_info(T)
            info.update({
                "name": name,
                "degree_in_match": bool(np.array_equal(np.sort(gr.in_degree()), base_in)),
                "degree_out_match": bool(np.array_equal(np.sort(gr.out_degree()), base_out)),
                "edges": int(gr.n_edges),
            })
            tasks = ["parity"]
            if name in ("measured", "protected_0", "open_0"):
                tasks.append("digit")
            info["accuracy"] = {}
            for task in tasks:
                accs = [run_model(T, seed, task, codes) for seed in SEEDS]
                info["accuracy"][task] = {
                    "values": accs,
                    "mean": float(np.mean(accs)),
                }
                print(
                    f"route {i} {name} both={info['both']} rank={info['rank']} {task} {info['accuracy'][task]['mean']:.3f}",
                    flush=True,
                )
            route_rec["graphs"].append(info)
            payload["routes"] = payload.get("routes", [])
        # rewrite accumulating file
        payload["routes"].append(route_rec)
        payload["wall_s"] = round(time.time() - t0, 1)
        OUT.write_text(json.dumps(payload, indent=2))
        print("saved", OUT, flush=True)
    print("DONE", payload["wall_s"])


if __name__ == "__main__":
    main()

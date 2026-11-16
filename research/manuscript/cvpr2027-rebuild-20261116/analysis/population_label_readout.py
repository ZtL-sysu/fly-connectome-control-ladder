"""Held-out multi-source digit readout on reconstructed MaleCNS graphs.

Eight, six, or four sources are driven by independent handwritten digits.
Features propagate by the full incoming-normalized two-step operator. The
MLP reads only the two audited sinks. One label is the parity of source 109,
whose column at those sinks is private on the named-edge graph and absent on
the path-zero graph. The control label is the parity of source 107, which
remains visible on every graph.
"""
import json
from pathlib import Path

import numpy as np
import torch
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
GRAPHS = ROOT / "analysis" / "recovered_graphs"
OUT = ROOT / "analysis" / "population-label-readout.json"
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
SINKS = (4, 5)
CRITICAL = 109
CONTROL = 107
COMMON = [107, 152, 6, 194, 136, 35, 18, 760, 544, 542, 305, 280, 116, 58, 20]
SEEDS = [11, 17, 23, 31, 41, 53, 67, 79, 97, 103]
KS = (4, 8)


def operators():
    ops = {}
    for name, fname in {
        "base": "narrowk4_base.npz",
        "named": "narrowk4_namededge_s0.npz",
        "path": "narrowk4_pathblock_p0.npz",
    }.items():
        z = np.load(GRAPHS / fname)
        n = len(z["body_ids"])
        A = np.zeros((n, n), dtype=np.float64)
        A[z["src"], z["dst"]] = 1.0
        scale = np.maximum(A.sum(0), 1.0)
        W = A.T / scale[:, None]
        ops[name] = W @ W
    return ops


def pools():
    digits = load_digits()
    images = digits.images.reshape(len(digits.target), -1).astype(np.float64) / 16.0
    idx = np.arange(len(images))
    tr, te = train_test_split(idx, test_size=0.25, random_state=0, stratify=digits.target)
    rng = np.random.default_rng(20261116)
    proj, _ = np.linalg.qr(rng.standard_normal((64, 16)))
    codes = (images @ proj[:, :16]).astype(np.float32)
    parity = (digits.target % 2).astype(np.int64)
    return {
        "train_codes": codes[tr],
        "train_parity": parity[tr],
        "test_codes": codes[te],
        "test_parity": parity[te],
        "n_train": int(len(tr)),
        "n_test": int(len(te)),
    }


def sample(rng, batch, sources, label_source, codes, parity):
    picks = rng.integers(0, len(codes), size=(batch, len(sources)))
    feats = codes[picks]
    y = parity[picks[:, sources.index(label_source)]].astype(np.float32)
    return feats, y


def column_report(T, sources, label_source):
    j = sources.index(label_source)
    col = T[:, j]
    others = np.delete(T, j, axis=1)
    coef, _, _, _ = np.linalg.lstsq(others, col, rcond=None)
    resid = col - others @ coef
    return {
        "column": [float(v) for v in col],
        "energy": float(np.sum(col ** 2)),
        "private_energy": float(np.sum(resid ** 2)),
    }


def run_readout(T, seed, train_fn, test_fn, linear, epochs=120, steps=32, batch=128, eval_n=2048):
    torch.manual_seed(seed)
    model = (
        torch.nn.Linear(32, 1).to(DEVICE)
        if linear
        else torch.nn.Sequential(
            torch.nn.Linear(32, 64), torch.nn.ReLU(), torch.nn.Linear(64, 1)
        ).to(DEVICE)
    )
    opt = torch.optim.Adam(model.parameters(), lr=0.006)
    loss_fn = torch.nn.BCEWithLogitsLoss()
    data_rng = np.random.default_rng(1_000_003 + seed + int(linear))
    Tt = torch.tensor(T, dtype=torch.float32, device=DEVICE)
    for _ in range(epochs * steps):
        feats, y = train_fn(data_rng, batch)
        ft = torch.tensor(feats, dtype=torch.float32, device=DEVICE)
        yt = torch.tensor(y, dtype=torch.float32, device=DEVICE)
        mixed = torch.einsum("ij,bjf->bif", Tt, ft).reshape(batch, -1)
        loss = loss_fn(model(mixed).squeeze(-1), yt)
        opt.zero_grad()
        loss.backward()
        opt.step()
    eval_rng = np.random.default_rng(2_000_003 + seed + 17 * int(linear))
    feats, y = test_fn(eval_rng, eval_n)
    with torch.no_grad():
        ft = torch.tensor(feats, dtype=torch.float32, device=DEVICE)
        mixed = torch.einsum("ij,bjf->bif", Tt, ft).reshape(eval_n, -1)
        pred = (model(mixed).squeeze(-1) > 0).cpu().numpy()
    return float(np.mean(pred == y))


def summarize(values):
    arr = np.asarray(values, dtype=np.float64)
    return {"mean": float(arr.mean()), "std": float(arr.std(ddof=1)), "values": [float(v) for v in arr]}


def main():
    ops = operators()
    data = pools()
    results = {}
    geometry = {}
    for K in KS:
        sources = [CRITICAL] + COMMON[: K - 1]
        results[str(K)] = {}
        geometry[str(K)] = {"sources": sources}
        for label_source, label_name in ((CRITICAL, "deleted_source"), (CONTROL, "preserved_source")):
            results[str(K)][label_name] = {}
            geometry[str(K)][label_name] = {}
            for graph, W2 in ops.items():
                T = W2[np.ix_(SINKS, sources)]
                geometry[str(K)][label_name][graph] = column_report(T, sources, label_source)
                kind_vals = {"mlp": [], "linear": []}
                for seed in SEEDS:
                    for kind, linear in (("mlp", False), ("linear", True)):
                        def train_fn(rng, n, src=sources, lab=label_source):
                            return sample(rng, n, src, lab, data["train_codes"], data["train_parity"])

                        def test_fn(rng, n, src=sources, lab=label_source):
                            return sample(rng, n, src, lab, data["test_codes"], data["test_parity"])

                        acc = run_readout(T, seed, train_fn, test_fn, linear)
                        kind_vals[kind].append(acc)
                results[str(K)][label_name][graph] = {k: summarize(v) for k, v in kind_vals.items()}
                print(
                    K,
                    label_name,
                    graph,
                    {k: round(v["mean"], 3) for k, v in results[str(K)][label_name][graph].items()},
                    "private",
                    round(geometry[str(K)][label_name][graph]["private_energy"], 6),
                    flush=True,
                )
    payload = {
        "device": str(DEVICE),
        "seeds": SEEDS,
        "sinks": list(SINKS),
        "split": {
            "dataset": "sklearn load_digits",
            "n_train": data["n_train"],
            "n_test": data["n_test"],
            "projection": "fixed QR map from 64 pixels to 16 dimensions, seed 20261116",
            "rule": "each active source receives an independent digit; evaluation uses held-out digits",
        },
        "readout": "MLP 32-64-1 ReLU or linear 32-1; Adam lr 0.006; 120 epochs x 32 batches of 128; BCE-with-logits; eval 2048 held-out samples",
        "propagation": "incoming-normalized two-step operator of the reconstructed 768-node graph; only the listed sources are driven; the MLP sees the two audited sinks",
        "geometry": geometry,
        "results": results,
    }
    OUT.write_text(json.dumps(payload, indent=2))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()

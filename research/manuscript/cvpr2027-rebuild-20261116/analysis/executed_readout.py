"""Executed MLP versus linear readout on the matched MaleCNS graphs.

The readout, loss, optimizer, and step budget match the archived motif-survival
model: sink features go through Linear-ReLU-Linear or a linear map, trained
with Adam and BCE-with-logits. Only the two audited sources are nonzero, so
the sink state is exactly T times those source features.

Two tasks share that readout:
- subspace XOR, the archived task, replayed from the recorded seeds;
- visual parity XOR, where each source carries a fixed 16-d projection of a
  real digit half and the label is the XOR of the two digit parities.
"""
import json
from pathlib import Path

import numpy as np
import torch
from sklearn.datasets import load_digits

ROOT = Path(__file__).resolve().parents[1]
GRAPHS = ROOT / "analysis" / "recovered_graphs"
OUT = ROOT / "analysis" / "executed-readout.json"
SEEDS = [11, 17, 23, 31, 41, 53, 67, 79, 97, 103]
SOURCES = (6, 109)
SINKS = (4, 5)
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")


def transfer(name):
    z = np.load(GRAPHS / name)
    n = len(z["body_ids"])
    A = np.zeros((n, n), dtype=np.float64)
    A[z["src"], z["dst"]] = 1.0
    scale = np.maximum(A.sum(0), 1.0)
    W = A.T / scale[:, None]
    return (W @ W)[list(SINKS)][:, list(SOURCES)]


def make_subspaces(seed, feat_dim=16, sub_dim=8):
    rng = np.random.default_rng(10_000_019 + seed)
    bases = []
    for _ in range(2):
        q, _ = np.linalg.qr(rng.standard_normal((feat_dim, sub_dim)))
        bases.append(q)
    return np.stack(bases)


def subspace_batch(rng, batch, bases):
    cls = rng.integers(0, 2, size=(batch, 2))
    z = rng.standard_normal((batch, 2, bases.shape[2])).astype(np.float32)
    feats = np.einsum("bsc,bsfc->bsf", z, bases[cls]).astype(np.float32)
    y = (cls[:, 0] ^ cls[:, 1]).astype(np.float32)
    return feats, y


def visual_pools():
    digits = load_digits()
    images = digits.images.astype(np.float64) / 16.0
    upper = images[:, :4, :].reshape(len(images), -1)
    lower = images[:, 4:, :].reshape(len(images), -1)
    rng = np.random.default_rng(20261116)
    q, _ = np.linalg.qr(rng.standard_normal((32, 16)))
    proj = q[:, :16]
    codes = {
        "upper": (upper @ proj).astype(np.float32),
        "lower": (lower @ proj).astype(np.float32),
    }
    parity = digits.target % 2
    return codes, parity


def visual_batch(rng, batch, codes, parity):
    cls = rng.integers(0, 2, size=(batch, 2))
    feats = np.zeros((batch, 2, 16), dtype=np.float32)
    for source, field in ((0, "upper"), (1, "lower")):
        for bit in (0, 1):
            pool = np.flatnonzero(parity == bit)
            take = np.flatnonzero(cls[:, source] == bit)
            choice = rng.choice(pool, size=len(take), replace=True)
            feats[take, source, :] = codes[field][choice]
    y = (cls[:, 0] ^ cls[:, 1]).astype(np.float32)
    return feats, y


def run_readout(T, seed, linear, sample_fn, epochs=120, steps_per_epoch=32, batch=128, eval_n=2048):
    torch.manual_seed(seed)
    model = torch.nn.Linear(32, 1).to(DEVICE) if linear else torch.nn.Sequential(
        torch.nn.Linear(32, 64), torch.nn.ReLU(), torch.nn.Linear(64, 1)
    ).to(DEVICE)
    opt = torch.optim.Adam(model.parameters(), lr=0.006)
    loss_fn = torch.nn.BCEWithLogitsLoss()
    data_rng = np.random.default_rng(1_000_003 + seed)
    Tt = torch.tensor(T, dtype=torch.float32, device=DEVICE)
    for _ in range(epochs * steps_per_epoch):
        feats, y = sample_fn(data_rng, batch)
        ft = torch.tensor(feats, dtype=torch.float32, device=DEVICE)
        yt = torch.tensor(y, dtype=torch.float32, device=DEVICE)
        mixed = torch.einsum("ij,bjf->bif", Tt, ft).reshape(batch, -1)
        loss = loss_fn(model(mixed).squeeze(-1), yt)
        opt.zero_grad()
        loss.backward()
        opt.step()
    eval_rng = np.random.default_rng(2_000_003 + seed)
    feats, y = sample_fn(eval_rng, eval_n)
    with torch.no_grad():
        ft = torch.tensor(feats, dtype=torch.float32, device=DEVICE)
        mixed = torch.einsum("ij,bjf->bif", Tt, ft).reshape(eval_n, -1)
        pred = (model(mixed).squeeze(-1) > 0).cpu().numpy()
    return float(np.mean(pred == y))


def summarize(values):
    arr = np.asarray(values, dtype=np.float64)
    return {
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=1)),
        "values": [float(v) for v in arr],
    }


def main():
    graphs = {
        "base": transfer("narrowk4_base.npz"),
        "namededge_zero": transfer("narrowk4_namededge_s0.npz"),
        "path_zero": transfer("narrowk4_pathblock_p0.npz"),
    }
    codes, parity = visual_pools()
    results = {task: {name: {"mlp": [], "linear": []} for name in graphs} for task in ("subspace_xor", "visual_parity_xor")}
    for seed in SEEDS:
        bases = make_subspaces(seed)
        tasks = {
            "subspace_xor": lambda rng, n, bases=bases: subspace_batch(rng, n, bases),
            "visual_parity_xor": lambda rng, n: visual_batch(rng, n, codes, parity),
        }
        for task, sampler in tasks.items():
            for name, T in graphs.items():
                for kind, linear in (("mlp", False), ("linear", True)):
                    acc = run_readout(T, seed, linear, sampler)
                    results[task][name][kind].append(acc)
        print(seed, {task: {name: {k: round(v[-1], 3) for k, v in kinds.items()} for name, kinds in graphs_.items()} for task, graphs_ in results.items()}, flush=True)
    payload = {
        "device": str(DEVICE),
        "seeds": SEEDS,
        "readout": "archived MLP 32-64-1 ReLU, or linear 32-1; Adam lr 0.006; 120 epochs x 32 batches of 128; BCE-with-logits; eval 2048",
        "visual_code": "fixed QR projection of 32-pixel digit halves to 16-d; class is digit parity; label is source XOR",
        "graphs": {name: T.tolist() for name, T in graphs.items()},
        "results": {
            task: {name: {kind: summarize(vals) for kind, vals in kinds.items()} for name, kinds in graphs_.items()}
            for task, graphs_ in results.items()
        },
    }
    OUT.write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload["results"], indent=2))


if __name__ == "__main__":
    main()

"""CIFAR-10 identity through reconstructed MaleCNS transfers.

A two-convolution embedding is trained on the available CIFAR-10 training
batches and then frozen. Its 16-d code is the source feature. Four sources
are driven by independent images. The label is the class at one source.
"""
import json
import pickle
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

ROOT = Path(__file__).resolve().parents[1]
GRAPHS = ROOT / "analysis" / "recovered_graphs"
CIFAR = Path("/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision/papers/R63-results/r82_local/cifar/cifar-10-batches-py")
OUT = ROOT / "analysis" / "cifar-identity-readout.json"
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
SINKS = (4, 5)
SOURCES = [109, 107, 152, 6]
SEEDS = [11, 17, 23, 31, 41, 53, 67, 79, 97, 103]


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


def load_images():
    xs, ys = [], []
    for i in (2, 3, 4):
        with (CIFAR / f"data_batch_{i}").open("rb") as f:
            d = pickle.load(f, encoding="latin1")
        xs.append(np.asarray(d["data"], np.float32).reshape(-1, 3, 32, 32) / 255.0)
        ys.append(np.asarray(d["labels"], np.int64))
    with (CIFAR / "test_batch").open("rb") as f:
        t = pickle.load(f, encoding="latin1")
    return (
        np.concatenate(xs),
        np.concatenate(ys),
        np.asarray(t["data"], np.float32).reshape(-1, 3, 32, 32) / 255.0,
        np.asarray(t["labels"], np.int64),
    )


class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        )
        self.embed = nn.Linear(32 * 8 * 8, 16)
        self.head = nn.Linear(16, 10)

    def forward(self, x):
        z = self.embed(self.conv(x).flatten(1))
        return z, self.head(z)


def embed_all(model, images, batch=256):
    outs = []
    with torch.no_grad():
        for i in range(0, len(images), batch):
            z, _ = model(torch.tensor(images[i:i + batch], device=DEVICE))
            outs.append(z.cpu().numpy())
    return np.concatenate(outs).astype(np.float32)


def sample(rng, batch, label_index, codes, labels):
    picks = rng.integers(0, len(codes), size=(batch, 4))
    return codes[picks], labels[picks[:, label_index]].astype(np.int64)


def run(T, seed, train_fn, test_fn, linear):
    torch.manual_seed(seed)
    model = (
        nn.Linear(32, 10).to(DEVICE)
        if linear
        else nn.Sequential(nn.Linear(32, 64), nn.ReLU(), nn.Linear(64, 10)).to(DEVICE)
    )
    opt = torch.optim.Adam(model.parameters(), lr=0.006)
    loss_fn = nn.CrossEntropyLoss()
    rng = np.random.default_rng(9_000_003 + seed + 17 * int(linear))
    Tt = torch.tensor(T, dtype=torch.float32, device=DEVICE)
    for _ in range(80 * 24):
        feats, y = train_fn(rng, 128)
        ft = torch.tensor(feats, device=DEVICE)
        yt = torch.tensor(y, dtype=torch.long, device=DEVICE)
        loss = loss_fn(model(torch.einsum("ij,bjf->bif", Tt, ft).reshape(128, -1)), yt)
        opt.zero_grad(); loss.backward(); opt.step()
    er = np.random.default_rng(9_100_003 + seed + 17 * int(linear))
    feats, y = test_fn(er, 2048)
    with torch.no_grad():
        ft = torch.tensor(feats, device=DEVICE)
        pred = model(torch.einsum("ij,bjf->bif", Tt, ft).reshape(2048, -1)).argmax(1).cpu().numpy()
    return float(np.mean(pred == y))


def summarize(vals):
    arr = np.asarray(vals, np.float64)
    return {"mean": float(arr.mean()), "std": float(arr.std(ddof=1)), "values": [float(v) for v in arr]}


def main():
    x, y, xt, yt = load_images()
    torch.manual_seed(20261116)
    enc = Encoder().to(DEVICE)
    opt = torch.optim.Adam(enc.parameters(), lr=0.001)
    loss_fn = nn.CrossEntropyLoss()
    images = torch.tensor(x)
    labels = torch.tensor(y)
    gen = torch.Generator().manual_seed(1)
    for _ in range(5):
        perm = torch.randperm(len(x), generator=gen)
        for i in range(0, len(x), 128):
            idx = perm[i:i + 128]
            _, logits = enc(images[idx].to(DEVICE))
            loss = loss_fn(logits, labels[idx].to(DEVICE))
            opt.zero_grad(); loss.backward(); opt.step()
    enc.eval()
    tr, te = embed_all(enc, x), embed_all(enc, xt)
    with torch.no_grad():
        ceiling = float((enc.head(torch.tensor(te, device=DEVICE)).argmax(1).cpu().numpy() == yt).mean())
    print("ceiling", round(ceiling, 3), flush=True)
    ops = operators()
    results = {}
    for lab, label_name in ((109, "deleted_source"), (107, "preserved_source")):
        results[label_name] = {}
        j = SOURCES.index(lab)
        for graph, W2 in ops.items():
            T = W2[np.ix_(SINKS, SOURCES)]
            kind_vals = {"mlp": [], "linear": []}
            for seed in SEEDS:
                for kind, linear in (("mlp", False), ("linear", True)):
                    kind_vals[kind].append(run(
                        T, seed,
                        lambda rng, n, j=j: sample(rng, n, j, tr, y),
                        lambda rng, n, j=j: sample(rng, n, j, te, yt),
                        linear,
                    ))
            results[label_name][graph] = {k: summarize(v) for k, v in kind_vals.items()}
            print(label_name, graph, {k: round(v["mean"], 3) for k, v in results[label_name][graph].items()}, flush=True)
    payload = {
        "device": str(DEVICE),
        "seeds": SEEDS,
        "data": "CIFAR-10 batches 2-4 for training (30000 images); batch 1 absent and batch 5 unreadable in the local archive; official test batch of 10000",
        "encoder": "Conv-16, pool, Conv-32, pool, linear to 16, linear to 10; Adam lr 0.001; 5 epochs; frozen before the connectome readout",
        "ceiling_test_accuracy": ceiling,
        "readout": "MLP 32-64-10 or linear 32-10; Adam lr 0.006; 80 epochs x 24 batches of 128; cross-entropy; eval 2048 resampled official test images",
        "sources": SOURCES,
        "results": results,
    }
    OUT.write_text(json.dumps(payload, indent=2))
    print("wrote", OUT, flush=True)


if __name__ == "__main__":
    main()

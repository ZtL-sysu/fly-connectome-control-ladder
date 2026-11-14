#!/usr/bin/env python
"""r129 density x survival grid — pre-registered companion experiment.

Imports the FROZEN p3_p4_ladder.py (unmodified) for graph generation,
dataset construction and training. New code in this file is limited to the
grid construction described in config.json.
"""
import hashlib, importlib.util, json, time
import numpy as np

SPEC_PATH = "../../papers/paper-null-ladder/f-research-v1-run-20261107-203506-null-ladder/scripts/p3_p4_ladder.py"
spec = importlib.util.spec_from_file_location("p34", SPEC_PATH)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

CODE_SHA = hashlib.sha256(open(SPEC_PATH, "rb").read()).hexdigest()
SIZES = [25, 17, 12, 11, 11, 7, 7, 6]
SEEDS = [11, 17, 23, 31, 41, 53]
D, HIDDEN, EPOCHS, LR, BATCH = 16, 64, 120, 0.006, 128
P_IN, P_OUT = 0.06, 0.004
GRAPH_SEED, SINKS = 123, 4

t_start = time.time()
print("PRE-REGISTERED before any grid training; frozen code SHA:", CODE_SHA, flush=True)
print("config correction v2: graph_seed=123, sinks_per_relay=4 (18 motif edges, 123 total)", flush=True)

# --- fixed motif from the frozen main-campaign graph (seed 123) ---
A0, modules, motifs = m.generate(96, SIZES, P_IN, P_OUT, GRAPH_SEED, 4, SINKS)
motif_edges = [(mt["sources"][0], mt["relay"]) for mt in motifs] + \
              [(mt["sources"][1], mt["relay"]) for mt in motifs] + \
              [(mt["relay"], s) for mt in motifs for s in mt["sinks"]]
assert len(motif_edges) == 18, len(motif_edges)
shortcuts = [(mt["sources"][0], s) for mt in motifs for s in mt["sinks"]] + \
            [(mt["sources"][1], s) for mt in motifs for s in mt["sinks"]]
src_a, src_b = motifs[0]["sources"]
sinks = np.array(sorted({s for mt in motifs for s in mt["sinks"]}))

# --- frozen survival deletion plan (rng 77, independent of s) ---
del_rng = np.random.default_rng(77)
order = del_rng.permutation(18)
delete_for = {9: set(order[:9].tolist()), 0: set(range(18)), 18: set()}

# --- background graphs per density scale ---
def background(s):
    rng = np.random.default_rng(1000 + s)
    mod = np.concatenate([[i] * z for i, z in enumerate(SIZES)])
    same = mod[:, None] == mod[None, :]
    P = np.where(same, P_IN * s, P_OUT * s)
    np.fill_diagonal(P, 0.0)
    B = (rng.random((96, 96)) < P).astype(np.float32)
    np.fill_diagonal(B, 0)
    return B

def grid_graph(s, k):
    B = background(s)
    keep = [e for i, e in enumerate(motif_edges) if i not in delete_for[k]]
    keep_set = set(keep)
    for e in motif_edges:
        B[e[0], e[1]] = 1.0 if e in keep_set else 0.0   # enforce survival exactly
    for (u, v) in shortcuts:          # remove shortcut edges (label leakage)
        B[u, v] = 0.0
    return B.astype(np.float32)

# --- data (fixed seeds, identical protocol) ---
Xtr, ytr = m.make_dataset(512, 96, D, src_a, src_b, np.random.RandomState(1), 0.06)
Xte, yte = m.make_dataset(512, 96, D, src_a, src_b, np.random.RandomState(999), 0.06)

# --- leakage probe once (frozen protocol) ---
lk = m.leakage_probe(Xtr, ytr, Xte, yte)
print("leakage probe acc:", lk, flush=True)

def run(W, seed):
    return m.train_eval(m.col_norm_adj(W), Xtr, ytr, Xte, yte, D, HIDDEN,
                        EPOCHS, LR, BATCH, sinks, 2, "cpu", seed)

rows = []
a0 = {}
for sd in SEEDS:
    a0[sd] = run(np.zeros((96, 96), np.float32), sd)   # A=0: zero adjacency
    print(f"A=0 seed {sd}: {a0[sd]:.4f}", flush=True)
for s in (1, 8, 32, 64):
    for k in (18, 9, 0):
        for sd in SEEDS:
            acc = run(grid_graph(s, k), sd)
            rows.append({"s": s, "k": k, "seed": sd, "acc_real": acc,
                         "acc_a0": a0[sd], "effect": acc - a0[sd]})
            print(f"s={s} k={k} seed={sd}: acc={acc:.4f} effect={acc - a0[sd]:+.4f}", flush=True)

def boot_ci(deltas, resamples=5000, seed=7):
    deltas = np.asarray(deltas)
    rng = np.random.default_rng(seed)
    means = deltas[rng.integers(0, len(deltas), (resamples, len(deltas)))].mean(1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))

cells = {}
for s in (1, 8, 32, 64):
    for k in (18, 9, 0):
        eff = [r["effect"] for r in rows if r["s"] == s and r["k"] == k]
        accs = [r["acc_real"] for r in rows if r["s"] == s and r["k"] == k]
        lo, hi = boot_ci(eff)
        cells[f"s{s}_k{k}"] = {"mean_acc_real": float(np.mean(accs)),
                               "mean_effect": float(np.mean(eff)),
                               "ci95": [lo, hi], "n_seeds": len(eff)}

out = {"experiment_id": "r129_density_survival_grid",
       "frozen_code": SPEC_PATH, "frozen_code_sha256": CODE_SHA,
       "config_sha256": hashlib.sha256(open("config.json", "rb").read()).hexdigest(),
       "leakage_probe": lk, "a0_by_seed": a0, "cells": cells,
       "rows": rows, "wall_seconds": round(time.time() - t_start, 1),
       "device": "Apple M1 CPU"}
json.dump(out, open("metrics.json", "w"), indent=1)
with open("summary.txt", "w") as f:
    f.write("r129 density x survival grid\n")
    f.write(f"frozen code SHA: {CODE_SHA}\n")
    f.write(f"leakage probe: {lk}\n")
    for key, c in cells.items():
        f.write(f"{key}: acc={c['mean_acc_real']:.4f} "
                f"effect={c['mean_effect']:+.4f} CI95=[{c['ci95'][0]:+.4f},{c['ci95'][1]:+.4f}]\n")
    c = cells
    P1 = c["s1_k18"]["ci95"][0] > 0
    P2 = (c["s1_k18"]["mean_effect"] > c["s8_k18"]["mean_effect"] > c["s32_k18"]["mean_effect"]) and c["s64_k18"]["mean_effect"] < 0.05
    P3 = (c["s1_k9"]["mean_effect"] < c["s1_k18"]["mean_effect"]) and (c["s64_k9"]["mean_effect"] < 0.05) and (c["s64_k18"]["mean_effect"] < 0.05)
    f.write(f"P1 (s=1,k=18 effect>0): {P1}\nP2 (monotone density gate): {P2}\nP3 (interaction): {P3}\n")
print("END_OF_RUN_OK", flush=True)

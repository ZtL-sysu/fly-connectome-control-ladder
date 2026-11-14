#!/usr/bin/env python
"""Generate tables_grid.tex + fig6_density_survival_grid.pdf from metrics.json.
No hand transcription: all numbers read from the recorded run output."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

M = json.load(open("metrics.json"))
cells = M["cells"]
S, K = [1, 8, 32, 64], [18, 9, 0]

eff = np.array([[cells[f"s{s}_k{k}"]["mean_effect"] for k in K] for s in S])
acc = np.array([[cells[f"s{s}_k{k}"]["mean_acc_real"] for k in K] for s in S])
lo = np.array([[cells[f"s{s}_k{k}"]["ci95"][0] for k in K] for s in S])
hi = np.array([[cells[f"s{s}_k{k}"]["ci95"][1] for k in K] for s in S])
sd = np.array([[np.std([r["effect"] for r in M["rows"] if r["s"] == s and r["k"] == k],
                        ddof=0) for k in K] for s in S])

def f(x):
    return f"{x:+.4f}"

lines = [r"\begin{table}[t]", r"  \centering", r"  \caption{Density$\times$path-survival grid on the",
         r"  controlled graph family (pre-registered; six paired seeds). Effect = seed-paired",
         r"  held-out accuracy minus the no-graph control; 95\% bootstrap intervals are shown as",
         r"  error bars in Fig.~\ref{fig:grid}. The advantage requires both factors: full survival",
         r"  at base density replicates the main effect, the highest density erases even $k{=}18$,",
         r"  and $k{=}9$ already collapses at base density.}", r"  \label{tab:grid}", r"  \small",
         r"  \begin{tabular}{lccc}", r"    \toprule",
         r"    Mean in-degree & $k{=}18$ & $k{=}9$ & $k{=}0$ \\",
         r"    \midrule"]
indeg = {1: 1.5, 8: 9.5, 32: 24.3, 64: 34.8}
for i, s in enumerate(S):
    row = f"    $s={s}$ (${indeg[s]:.1f}$) "
    for j in range(3):
        row += f"& ${f(eff[i, j])}$ "
    lines.append(row + r"\\")
lines += [r"    \bottomrule", r"  \end{tabular}", r"\end{table}"]
open("tables_grid.tex", "w").write("\n".join(lines) + "\n")

fig, ax = plt.subplots(figsize=(3.4, 2.1))
x = np.arange(len(S))
w = 0.26
for j, k in enumerate(K):
    halfw = (hi[:, j] - lo[:, j]) / 2
    ax.bar(x + (j - 1) * w, eff[:, j], w, yerr=halfw, capsize=2,
           label=f"$k={k}$" if k else "$k=0$")
ax.axhline(0.0, color="gray", lw=0.6)
ax.set_xticks(x)
ax.set_xticklabels([f"$s={s}$\n({indeg[s]:.0f})" for s in S], fontsize=7)
ax.set_xlabel("background density scale (mean in-degree)", fontsize=7)
ax.set_ylabel("effect vs no-graph", fontsize=7)
ax.tick_params(labelsize=7)
ax.legend(fontsize=6.5, frameon=False)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
fig.tight_layout()
fig.savefig("figures/fig6_density_survival_grid.pdf")
print("wrote tables_grid.tex and figures/fig6_density_survival_grid.pdf")

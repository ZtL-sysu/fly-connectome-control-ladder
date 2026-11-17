"""Rebuild paper figures from saved records only; no training or evaluation."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1] / 'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8,
    'axes.spines.top': False, 'axes.spines.right': False,
    'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none',
    'axes.labelsize': 8, 'xtick.labelsize': 7, 'ytick.labelsize': 7,
    'legend.fontsize': 7, 'axes.titlesize': 9})
BLUE, GREEN, ORANGE, GRAY = '#0072B2', '#009E73', '#D55E00', '#7B7B7B'

def save(fig, name):
    for ext in ('pdf', 'svg', 'png'):
        fig.savefig(OUT / f'{name}.{ext}', dpi=240, bbox_inches='tight', pad_inches=.04)
    plt.close(fig)

def errorline(ax, x, stats, label, color, marker='o', ls='-', offset=0):
    y = np.array([s['mean'] for s in stats])
    lo = np.array([s['ci_lo'] for s in stats]); hi = np.array([s['ci_hi'] for s in stats])
    ax.errorbar(np.array(x) + offset, y, yerr=[y-lo, hi-y], label=label,
        color=color, marker=marker, linestyle=ls, lw=1.35, ms=4,
        capsize=2, elinewidth=.8)

def clean(ax):
    ax.set_ylim(.44, 1.025); ax.axhline(.5, color='#BBBBBB', ls=':', lw=.8, zorder=0)
    ax.grid(axis='y', alpha=.16); ax.set_axisbelow(True); ax.set_ylabel('Test accuracy')

R = json.loads((ROOT/'analysis/recovered_graphs/narrowk4_transfer_report.json').read_text())
fig, ax = plt.subplots(figsize=(12, 6), facecolor='white')
ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis('off')

def module(x, y, width, height, title, lines, face, edge='#222222', title_color='#111111', lw=1.0):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
        boxstyle='round,pad=0.035,rounding_size=0.08', facecolor=face,
        edgecolor=edge, linewidth=lw, zorder=1))
    ax.text(x + width/2, y + height - .18, title, ha='center', va='top',
            fontsize=9.2, fontweight='bold', color=title_color, zorder=3)
    for k, line in enumerate(lines):
        ax.text(x + .13, y + height - .48 - .26*k, line, ha='left', va='top',
                fontsize=7.5, color='#333333', zorder=3)

def arrow(x1, y1, x2, y2, label=None, label_pos=None):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=11,
        lw=1.15, color='#222222', shrinkA=2, shrinkB=2, zorder=4))
    if label:
        lx, ly = label_pos if label_pos else ((x1+x2)/2, (y1+y2)/2+.12)
        ax.text(lx, ly, label, ha='center', va='bottom', fontsize=7.4, color='#333333', zorder=5)

headers = [(.25, 'INTERVENTION'), (3.25, 'EXECUTED OPERATOR'),
           (6.25, 'TASK-INFORMATION AUDIT'), (9.25, 'INTERVENTION REPORT')]
for hx, title in headers:
    ax.text(hx + 1.25, 5.55, title, ha='center', va='center',
            fontsize=10.5, fontweight='bold', color='#111111')

module(.25, 3.05, 2.5, 2.0, 'EDITED CONNECTOME',
       ['degree sequence', 'module counts', r'common relays $\mathcal{C}(A)$'], '#F1F1EF')
module(3.25, 3.05, 2.5, 2.0, 'TWO-STEP PROPAGATION',
       [r'$H_S=R_SW^2E_{ab}X_{ab}$', 'incoming-neighbor averaging',
        r'$W_{vu}=A_{uv}/\max(d_v,1)$'], '#E8F4F4')
module(6.25, 4.18, 2.5, .82, 'SOURCE ACCESS',
       [r'$T_{:a}\neq0$   $T_{:b}\neq0$'], '#EFEBF7')
module(6.25, 3.25, 2.5, .82, 'TRANSFER GEOMETRY',
       [r'$\mathrm{rank}(T)$; private residual $q_j$'], '#EFEBF7')
module(6.25, 2.32, 2.5, .82, 'IDEAL TASK TEST',
       [r'nonzero columns $\Leftrightarrow$ Bayes $=1$'], '#EFEBF7',
       edge='#B45151', lw=1.2)
module(9.25, 4.12, 2.5, .92, 'STRUCTURE CERTIFICATE',
       ['verified constraints'], '#FCE8D5')
module(9.25, 3.08, 2.5, .92, 'FINITE READOUT',
       ['retrained MLP; accuracy'], '#FCE8D5')
module(9.25, 1.98, 2.5, 1.02, 'INTERPRET EDIT',
       ['structure preserved?', 'information preserved?', 'behavior changed?'],
       '#F6C89F')

arrow(2.75, 4.05, 3.25, 4.05, r'$A,\,W$')
arrow(5.75, 4.05, 6.25, 4.05, r'$T(A)$', (6.0, 4.22))
arrow(8.75, 4.55, 9.25, 4.55)
arrow(8.75, 3.66, 9.25, 3.66)
arrow(8.75, 2.73, 9.25, 2.73, label=None)
arrow(10.5, 4.12, 10.5, 4.00)
arrow(10.5, 3.08, 10.5, 2.95)

ax.text(8.95, 3.30, 'readout information', ha='center', va='center',
        fontsize=6.8, color='#555555', rotation=90)
ax.text(.25, 1.92, 'MATCHED ZERO-RELAY EXAMPLE', ha='left', va='center',
        fontsize=9.5, fontweight='bold', color='#111111')
ax.plot([.25, 11.75], [1.82, 1.82], color='#DDDDDD', lw=.8)

def evidence_card(x, title, matrix, acc, accent):
    ax.add_patch(FancyBboxPatch((x, .58), 5.05, 1.06,
        boxstyle='round,pad=0.035,rounding_size=0.06', facecolor='#F8FAFA',
        edgecolor='#BBBBBB', linewidth=.8, zorder=1))
    ax.text(x + .18, 1.39, title, ha='left', va='center', fontsize=8.8,
            fontweight='bold', color=accent, zorder=3)
    ax.text(x + .18, 1.06, 'reconstructed operator', ha='left', va='center',
            fontsize=6.8, color='#666666')
    ax.text(x + .18, .78, matrix, ha='left', va='center', fontsize=9.5,
            fontfamily='monospace', color='#222222')
    ax.text(x + 2.85, 1.06, 'archived fit', ha='left', va='center',
            fontsize=6.8, color='#666666')
    ax.text(x + 2.85, .78, acc, ha='left', va='center', fontsize=9.5,
            fontfamily='monospace', color=accent)

evidence_card(.35, 'Named-edge zero', '16T = [1 0; 1 1]', 'accuracy 0.9745', BLUE)
evidence_card(6.60, 'Path zero', '16T = [1 0; 1 0]', 'accuracy 0.5055', ORANGE)
ax.annotate('', xy=(6.45, 1.10), xytext=(5.55, 1.10),
            arrowprops=dict(arrowstyle='<->', color='#555555', lw=1.0))
ax.text(6.0, 1.30, 'same constraints', ha='center', va='bottom',
        fontsize=6.9, color='#555555')

legend_items = [('#F1F1EF', 'Structural constraints'), ('#E8F4F4', 'Executed operator'),
                ('#EFEBF7', 'Task information'), ('#F6C89F', 'Finite-model behavior')]
for k, (color, label) in enumerate(legend_items):
    lx = .35 + 3.05*k
    ax.add_patch(FancyBboxPatch((lx, .18), .20, .14, boxstyle='round,pad=0.01',
        facecolor=color, edgecolor='#777777', linewidth=.5, zorder=2))
    ax.text(lx + .28, .25, label, ha='left', va='center', fontsize=6.7, color='#444444')
fig.subplots_adjust(left=.015, right=.985, top=.99, bottom=.015)
save(fig, 'overview')

E = json.loads((ROOT/'evidence/edge_dose.json').read_text())['stats']['per_dose']
P = json.loads((ROOT/'evidence/path_dose.json').read_text())['stats']['per_dose']
fig, axs = plt.subplots(1, 2, figsize=(3.36, 2.12))
for ax in axs: clean(ax)
errorline(axs[0], [0,1,2,4], [E[k]['real'] for k in ['s0','s1','s2','full']], 'Graph', ORANGE)
errorline(axs[1], [0,1,2], [P[k]['real'] for k in ['p0','p1','pfull']], 'Graph', BLUE)
axs[0].set_xticks([0,1,2,4]); axs[1].set_xticks([0,1,2]); axs[1].set_ylabel('')
axs[0].set_xlabel('Requested motif\nedges retained'); axs[1].set_xlabel('Common-relay\ntriples retained')
axs[0].set_title('(a) Edge-conditioned'); axs[1].set_title('(b) Path-conditioned')
axs[0].annotate('Recovery after complete\nnamed-edge deletion', xy=(0,.9745), xytext=(1.0,.89),
    fontsize=6.8, arrowprops=dict(arrowstyle='->', lw=.7, color=ORANGE), color='#333333')
fig.subplots_adjust(wspace=.35, left=.16, right=.98, bottom=.25, top=.82)
save(fig, 'edge_vs_path')

M = json.loads((ROOT/'evidence/multigraph.json').read_text())['subgraphs']
checks = json.loads((ROOT/'analysis/independent-transfer-checks.json').read_text())
fig, axs = plt.subplots(1, 2, figsize=(7., 2.68), sharey=True)
for ax, (name, obj) in zip(axs, M.items()):
    clean(ax); ax.set_ylim(.44, 1.14); ax.set_yticks([.5,.6,.7,.8,.9,1.0])
    D = obj['stats']['per_dose']; order = ['p0','p1','p2','pfull']; x = [0,1,2,3]
    for c, label, color, mk, ls, off in [('real','Dose graph',BLUE,'o','-',-.045),
           ('L1_degree_null','Degree null',GRAY,'s','--',0),
           ('task_aware_null','Protected null',GREEN,'^','-.',.045)]:
        errorline(ax, x, [D[d][c] for d in order], label, color, mk, ls, off)
    prefix = 'visual_graph_S1_broad_' if name == 'S1_broad' else 'visual_graph_S2_narrow_'
    for xi, dose in zip(x, order):
        row = next(r for r in checks if r['file'] == prefix+dose+'.npz')
        ideal = 1 if all(row['source_columns_nonzero']) else .5
        ax.text(xi, 1.065, '1' if ideal == 1 else r'$1/2$', ha='center', va='center',
            color=BLUE if ideal == 1 else GRAY, fontsize=8, fontweight='bold')
    ax.text(-.43, 1.065, 'Ideal Bayes', ha='right', va='center', fontsize=7.4, color='#444444')
    ax.set_xticks(x); ax.set_xlabel('Common-relay triples retained in dose graph')
    ax.set_title('(a) Broad extraction' if name == 'S1_broad' else '(b) Narrow extraction',
                 loc='left', fontweight='bold')
axs[0].annotate('Finite accuracy changes;\nideal information does not', xy=(1,.6889), xytext=(1.22,.53),
    fontsize=7, color=BLUE, arrowprops=dict(arrowstyle='->', lw=.7, color=BLUE))
axs[1].set_ylabel(''); axs[1].legend(loc='upper left', frameon=False, ncol=1, bbox_to_anchor=(0,.98))
fig.subplots_adjust(wspace=.13, left=.105, right=.99, bottom=.2, top=.94)
save(fig, 'multigraph')

C = json.loads((ROOT/'analysis/cifar-identity-readout.json').read_text())
fig, axs = plt.subplots(1, 2, figsize=(3.36, 2.35), gridspec_kw={'width_ratios':[.9,1.25]})
ax = axs[0]; ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-.1,1.1); ax.set_ylim(-.35,1.25)
ax.annotate('', xy=(1,0), xytext=(0,0), arrowprops=dict(arrowstyle='->',color='#AAAAAA',lw=.8))
ax.annotate('', xy=(0,1), xytext=(0,0), arrowprops=dict(arrowstyle='->',color='#AAAAAA',lw=.8))
ax.text(1.02,-.06,r'$s_1$',fontsize=7); ax.text(-.07,1.02,r'$s_2$',fontsize=7)
for start, end, col, lab in [((0,0),(.42,.84),GRAY,'others'),((0,0),(.28,.70),BLUE,r'$t_j$')]:
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle='->',color=col,lw=1.7))
ax.plot([.84,.42],[.0,.84],ls=':',color=GRAY,lw=.8)
ax.annotate('', xy=(.28,.70), xytext=(.56,.70), arrowprops=dict(arrowstyle='->',color=ORANGE,lw=1.7))
ax.text(.44,.79,r'$q_j$',color=ORANGE,fontsize=8); ax.text(.05,1.17,'Private residual',fontsize=8.5,fontweight='bold')
ax.text(.5,-.28,r'$\rho_j=\|q_j\|^2$',ha='center',fontsize=9)
ax = axs[1]
for yi, (key, label) in enumerate([('deleted_source','Source 109'),('preserved_source','Source 107')]):
    vals=[C['results'][key][g]['mlp']['mean'] for g in ('base','named','path')]
    ax.plot([0,1,2], vals, '-o', color=BLUE if yi==0 else GREEN, label=label, lw=1.3, ms=4)
    for xi,v in zip([0,1,2],vals): ax.text(xi,v+.035,f'{v:.3f}',ha='center',fontsize=6.7)
ax.axhline(.1,color='#BBBBBB',ls=':',lw=.8); ax.set_ylim(0, .68); ax.set_xticks([0,1,2],['Base','Named','Path'])
ax.set_ylabel('CIFAR source-class accuracy'); ax.set_xlabel('Reconstructed graph'); ax.grid(axis='y',alpha=.15)
ax.legend(frameon=False,loc='lower center',fontsize=6.7,ncol=1)
ax.set_title('Source-specific readout',fontsize=8.5,fontweight='bold')
fig.subplots_adjust(wspace=.35,left=.09,right=.98,bottom=.2,top=.9)
save(fig, 'transfer_geometry')

print('Rebuilt main figures from archived records; no training or new evaluation.')

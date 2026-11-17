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
fig = plt.figure(figsize=(7.0, 2.9), facecolor='white')
gs = fig.add_gridspec(3, 2, height_ratios=[.18, 1, .42], left=.02, right=.98, top=.98, bottom=.06, wspace=.18, hspace=.12)
banner = fig.add_subplot(gs[0, :]); banner.axis('off')
banner.add_patch(FancyBboxPatch((0, .08), 1, .84, boxstyle='round,pad=0.02,rounding_size=0.02',
    facecolor='#F3F3F1', edgecolor='#DDDDD9', lw=.7, transform=banner.transAxes))
banner.text(.5, .52, 'Same structure: matched degrees  |  matched modules  |  0 common relays',
    ha='center', va='center', fontsize=9, fontweight='bold', color='#333333')
pos = {'a': (0, .9), 'b': (0, 0), 'ra': (1, 1.0), 'rb': (1, -.2),
       's1': (2, .9), 's2': (2, 0)}
node_text = {'a': 'a', 'b': 'b', 'ra': r'$r_a$', 'rb': r'$r_b$',
             's1': r'$s_1$', 's2': r'$s_2$'}
routes = [[('a','ra'), ('ra','s1'), ('ra','s2'), ('b','rb'), ('rb','s2')],
          [('a','ra'), ('ra','s1'), ('ra','s2')]]
transfers = [R['namededge_s0']['transfer']['W2_sink_rows_source_cols'],
             R['pathblock_p0']['transfer']['W2_sink_rows_source_cols']]
for i in range(2):
    ax = fig.add_subplot(gs[1, i]); ax.axis('off'); ax.set_xlim(-.3, 2.3); ax.set_ylim(-.45, 1.55)
    active = set(v for edge in routes[i] for v in edge)
    for n, (x, y) in pos.items():
        present = n in active
        color = BLUE if n in ('a','s1','s2') else ORANGE if n in ('b','rb') else '#BBBBBB'
        if not present: color = '#B9B9B9'
        ax.add_patch(Circle((x,y), .125, facecolor='white', edgecolor=color, lw=1.5, zorder=3))
        ax.text(x, y, node_text[n], ha='center', va='center', fontsize=9,
                color='#222222' if present else '#999999', zorder=4)
    for u, v in routes[i]:
        color = ORANGE if u in ('b','rb') else BLUE
        rad = .1 if (u,v) == ('ra','s2') else 0
        ax.add_patch(FancyArrowPatch(pos[u], pos[v], arrowstyle='-|>', mutation_scale=11,
            shrinkA=9, shrinkB=9, lw=1.7, color=color, connectionstyle=f'arc3,rad={rad}'))
    ax.text(1, 1.43, ['Named-edge zero dose', 'Path-conditioned zero dose'][i],
            ha='center', fontweight='bold', fontsize=10)
    mat = np.rint(np.array(transfers[i])*16).astype(int)
    res = fig.add_subplot(gs[2, i]); res.axis('off'); res.set_xlim(0,1); res.set_ylim(0,1)
    res.add_patch(FancyBboxPatch((.02,.08), .96, .84, boxstyle='round,pad=0.02,rounding_size=0.02',
        facecolor='#FAFAF8', edgecolor='#E0E0DC', lw=.7))
    res.text(.5,.77,'Reconstructed transfer',ha='center',fontsize=7.5,color='#555555')
    res.text(.5,.51,f'16T = [ {mat[0,0]}  {mat[0,1]} ;  {mat[1,0]}  {mat[1,1]} ]',
        ha='center',fontsize=11,fontfamily='monospace',color='#222222')
    res.text(.5,.25,['Both sources visible  |  Archived accuracy: 0.9745',
                     'Source b deleted  |  Archived accuracy: 0.5055'][i],
        ha='center',fontsize=7.0,fontweight='bold',color=BLUE if i==0 else ORANGE)
fig.text(.5, .01, 'Same structural certificate, different task information at the readout',
    ha='center', fontsize=9.5, fontweight='bold', color='#222222')
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

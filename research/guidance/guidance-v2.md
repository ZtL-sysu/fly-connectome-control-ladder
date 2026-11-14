# Research Guidance File (Contract v2, R51) — A Structure-Sensitive Null Ladder with Real-Connectome Path Preservation

Contract version: v2-R51. Supersedes `guidance.md` (v1), retained as historical
evidence. This is a versioned contract change under `f-research-v1`
`references/research-recovery.md`, triggered by the independent full review
`ccfa-review-reports/paper-null-ladder-r49-independent-review-20261108.md`
(Overall 7.5). Planned claims below are NOT observed findings; all results are
filled at P5/P5A from pulled artifacts.

## Title / Topic

Working title: *A Structure-Sensitive Null Ladder Exposes a Blind Spot in
Connectome-Control Protocols*. Target field: computer vision / AI for Science,
evaluation methodology and connectome-constrained visual models. Target venue
tier: CCF-A conference, CVPR-style formatting (8 pages main content plus
references and the mandatory LLM Usage Statement), double blind.

## Core Idea

Existing work disagrees on whether biological wiring topology confers an
advantage on visual computation. Published answers differ because each uses a
different null graph, training horizon, initialisation and task. The comparison
protocol itself is the confound. We construct a nested ladder of null graphs
matching progressively higher-order global statistics (L0 edge count, L1
in/out degree, L2 module-pair counts, L3 directed triad census; L4 matched
independent-graph control), and — critically — an explicit record of how many
task-relevant 2-hop convergence path edges survive in each control. On a
path-identifiable, low-in-degree real MaleCNS v1.0 visual subgraph we then
isolate, one variable at a time, (a) in-degree/density and (b) the surviving
path-edge count, and ask which one controls the real-versus-null advantage.

### Mechanism-Level Rationale

A global invariant constraint (degree sequence, module counts, triad census)
does not constrain whether a specific local source→relay→sink path is intact.
Under uniform mixing, an unprotected edge is destroyed with probability tending
to one; adding higher-order global constraints restricts the admissible swap
pool but does not remove protected edges from it. Therefore only a control that
explicitly preserves the computational path can be expected to retain the
advantage. This yields two falsifiable predictions: (i) at fixed density,
accuracy should collapse monotonically as surviving path edges are removed;
(ii) a training-free count of surviving 2-hop paths should predict the
real-versus-null delta on held-out, non-manipulated real-wiring graphs.

## Paper Story

The paper opens with the conflicting claims of arXiv:2610.10023 (structure
alone supports efficient visual computation) and arXiv:2604.04033 (a
degree-preserving null removes the reported topological advantage). It argues
that neither is wrong: they differ in control construction, initialisation,
horizon and task. The gap is that no study makes the null generator the
experimental variable with asserted invariants, corrected multi-seed statistics
and an explicit path-survival audit. The insight is that a control is sufficient
only if it preserves every structure the hypothesis does not ablate. Evidence
that convinces the reader: a fixed-density dose-response on real biological
wiring, a faithful rerun of the strongest published control ladder extended with
a task-aware control, an independent non-manipulated graph family with LOGO-CV
prediction, and one hash-verifiable end-to-end main-matrix regeneration. Negative
and null runs are reported, not hidden.

## Paper Outline

1. Introduction: conflicting claims, comparison-protocol gap, preregistered
   adjudication; explicit scope statement (evaluation methodology, no claim of
   improved visual accuracy).
2. Related Work: connectome-constrained vision, null models and motifs,
   structure-sensitivity evaluation, the strongest published control ladder.
3. Method: visual subgraph extraction from public MaleCNS v1.0 with streamed
   column projection; nested null ladder with asserted invariants; fixed-density
   motif-survival dose; structure-sensitive XOR diagnostic task; shared-init
   training protocol; training-free path statistics; strong-baseline ladder.
4. Experiments and Results: baseline reruns, per-rung delta CIs, fixed-density
   path-survival dose on real wiring, control-ladder rerun, real image task,
   independent graph family LOGO-CV, robustness and negative runs; all tables
   generated from persisted metrics.
5. Discussion: which structural layer matters, reconciliation with the
   conflicting literature, sufficiency standard for control construction,
   limitations (synthetic diagnostic XOR label, no official flyvis stack unless
   actually installed, cross-run visual-ID matching differences, retained
   historical execution defects). Scope conditions stated as positive evidence
   boundaries.
6. Conclusion: the adjudication outcome and the reusable generator standard.

## Experiment Plan

### Datasets

- Direct access URL (public, no approval): MaleCNS v1.0 flat connectome (CC-BY 4.0, Berg et al., Cell 2026): public
  1.05 GB `connectome-weights-male-cns-v1.0-minconf-0.5.feather` plus 14.5 MB
  `body-annotations-male-cns-v1.0-minconf-0.5.feather`. Stream with
  `pyarrow.ipc.open_file().get_batch(i)`, project only endpoint columns, filter
  visually annotated body IDs, take top-degree 768-node induced subgraph; never
  densify the full table. Public and directly accessible; no approval, payment
  or credentials.
- `sklearn.datasets.load_digits` (real 8x8 handwritten digit images, 10 classes,
  fixed 60/20/20 split) and, when available, MNIST via torchvision. Real image
  inputs are projected into 64 visual input neurons; no label information is fed
  to the readout.
- Controlled 96-node low-in-degree graph (diagnostic instrument, explicitly
  labelled `SYNTHETIC_APPROXIMATION`) for the end-to-end main-matrix rerun.

### Baselines

- Simple: A=0 no-graph reservoir with identical projection and readout.
- Strong published: faithful rerun of arXiv:2604.04033's three-segment control
  ladder (checkpoint weak control, shared-init strict control) on the real
  subgraph, plus our task-aware extension.
- Strong domain: fixed-wiring + learned scalar gains connectome-constrained
  visual model (flyvis-style equivalent; if the official stack is unavailable,
  label as an equivalent reproduction and never claim official code).
- Matched internal: degree-preserving null, task-aware null, motif-removed,
  L0-L3 rungs, same-generator independent graph.
- Oracle upper bound: clean 2-channel probe on concatenated source features;
  leakage probes on raw and pooled features must stay at chance.

### Proposed Method Variants

- Variant A: nested global-statistic ladder L0-L3 with invariant assertions.
- Variant B: fixed-density path-survival dose (the decisive v2 addition).
- Variant C: task-aware control preserving the computational path.
- Variant D: three-segment published control ladder with task-aware extension.

### Metrics

- Primary metric: held-out test accuracy and paired real-minus-null delta with 95%
  paired seed-level bootstrap CI (R=5000), BH correction across the condition
  family; sign agreement vs majority-class baseline and magnitude MAE vs
  constant baseline for LOGO-CV.
- Secondary metrics: oracle accuracy, leakage probe accuracy, invariant violation
  counts, seed variance, early-training loss/activity for the control ladder,
  peak GPU memory, wall-clock, parameter count.
- Metric direction: higher accuracy is better. Chance level 0.5 for the XOR
  diagnostic; 0.1 for the 10-class image task.

### Required Ablations

- A=0 no-graph control (must be at chance for the XOR diagnostic).
- Fixed-density motif-survival dose with degree/module invariants held.
- L0-L3 rung family with per-instance invariant assertions.
- Motif removal and shuffled node-to-input mapping.
- Independent 24-graph family with no manipulation, LOGO-CV feature selection
  inside training folds only.
- Two task-difficulty levels, two noise levels, two propagation depths where
  applicable.

### Runtime / Hardware Budget

- Novix `exp-4090` single card per task (RTX 4090, 48 GB RAM, 4 CPU cores),
  explicitly authorized by the user for this project. At most 2 h per task,
  memory ≤ 48 GB. Seeds: 10 for C1/C5, 6 for C2/C3/C4. Hyperparameter search
  trials: 0 (all settings frozen). All experiments are delegated to
  `novix-platform`; results pulled back with `novix debug pull task:<id> <dest>
  --sub project/results/<dir>/artifacts`, never whole-workspace pulls (the
  1 GB Feather breaks chunked transfer).
- Frozen seeds `[11,17,23,31,41,53,67,79,97,103]`; held-out test touched once
  at P5. No tuning on the test set.

## Expected Results

- Minimum acceptable: complete fixed-density dose, control ladder, independent
  family and main matrix with all CIs, invariant counts and negative runs logged,
  regardless of sign.
- Strong result (`expected_strong`): `hypothesis_supported=true` on real wiring —
  monotone dose-response with full-dose real ≥ 0.75, zero-dose real ≤ 0.60,
  A0/degree-null/motif-removed ≤ 0.60, task-aware(full) ≥ 0.75, paired delta CI
  lower bound > 0; weak-control apparent advantage reproduced and removed by
  strict control, then restored by the task-aware segment with CI lower bound > 0;
  independent-family LOGO sign agreement ≥ majority baseline + 0.15 and ≥ 3
  features with BH q < 0.05; clean hash-verifiable main matrix with all structure
  gates PASSED.
- Failure signal: structure-sensitivity precheck fails, invariants cannot be
  held, or minimum detectable effect exceeds any observable delta. On failure,
  retain all runs and enter another correction cycle; never lower
  `expected_strong`, invent a result, or tune until significant.

## Figure/Table Decision Rules

Select figures and tables only after evidence stabilises; each visual must answer
a scientific question and be interpreted near its first discussion. All tables
are generated by scripts directly from pulled metric files (no hand-typed
numbers). Preserve one overall framework figure; use vector PDFs for plots.
Figures/tables are not assigned per subsection by quota.

## Traceability Checklist

- Must appear in paper? Only evidence-backed results, tables and figures; workflow logs, delivery notes and review dialogue stay in external audit files.
- Every claim maps to a persisted artifact under the run root.
- `experiment-traceability.md` updated before and after each batch.
- All executed scripts self-report SHA-256 and are pulled back for verification.
- Raw and completed metrics, per-seed logs, invariant counts and local repair
  scripts retained; failed runs retained as data.
- Planned claims distinguished from observed findings at P1B/P3A/P5A/P9 by
  `ccf-integrity-auditor`; `ccf-paper-reviewer` reviews the pre-draft dossier
  scientifically at P5A and the manuscript in full mode at P9, with the P9 full
  review performed by an isolated sub-agent, never the authoring session.

## Citation Scope

Keywords: connectome, null model, graph neural network, visual computation,
evaluation protocol, motif, degree-preserving randomisation, FDR. Must-cite papers
are arXiv:2604.04033, arXiv:2610.10023, Lappalainen et al. Nature 2024, Berg et al.
Cell 2026, Dorkenwald et al. Nature 2024, Maslov & Sneppen 2002, Milo et al.
2002, Wasserman & Faust 1994, Benjamini & Hochberg 1995, Kipf & Welling 2017,
Xu et al. 2019, Hagberg et al. 2008. Verify every entry for authenticity and
claim support at P12/P14; no citation padding, no duplicate preprint versions.

## Constraints and Preferences

- All experiments on Novix `exp-4090` with
  `--provider novixlet --resource-pool exp-4090 --gpu --gpu-count 1`; omit
  `--agent`; use `--model kimi__kimi-k3`; `--json` before the command group.
  Credentials via `ensure_login.py --check/--run`, never written into artifacts.
- Guidance explicitly authorises remote execution (G5 opt-in satisfied).
- `hardware-profile.md` and `feasibility-contract.json` reflect 4090 / 48 GB.
- No submission, commit or push. No fabrication of literature, datasets,
  results or review scores. Unverified items are labelled as such.
- Six numbered main sections exactly as listed; no appendices or checklists
  appended to the manuscript. LLM Usage Statement is placed after the main text
  and before references; external links are excluded from the reference list.
- Final acceptance: an independent full-mode `ccf-paper-reviewer` report whose
  `**Overall:** X` satisfies `X > 8.0`. Self-review is not admissible.

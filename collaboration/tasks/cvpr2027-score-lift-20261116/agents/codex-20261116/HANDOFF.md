# HANDOFF — codex-20261116 @ cvpr2027-score-lift-20261116

Protocol: `collaboration/PROTOCOL.md`. This handoff records a work-state sync. It does not validate or qualify the manuscript.

## Current state (2026-11-16, source-support draft)

The active manuscript is *A Degree Match Does Not Keep Both Inputs*, archived at `research/manuscript/cvpr2027-source-support-20261116/`. It is a six-page CVPR 2027 review draft. The latest isolated full review of that PDF is Overall 4, confidence 4 (`reviews/independent-full-review-ensemble.md`). That review does not replace R95 and does not meet a score of 6.

Resume entry:

1. Open `research/manuscript/cvpr2027-source-support-20261116/main.tex` and `research-decision.md`.
2. Check the 307-swap claims against `analysis/conditioned_ensemble.json` and `analysis/support_sweep.json`. Check the 24-draw null against `analysis/degree24.json`.
3. Do not describe the protected three-route runs as independent wirings. Eleven of twelve copy \(T\).
4. A further score move, as stated by the 2026-11-16 ensemble review, needs the same certificate to change a flyvis, Kenyon, or optic-flow comparison. A signed two-hop T4a–d kernel probe did not separate four direction axes and is not in the paper.
5. Leave the CIFAR revision below untouched. It is a different manuscript.

## Latest additive state (2026-11-16, CVPR-focused refinement)

The refined CIFAR/operator-audit manuscript is at
`research/manuscript/cvpr2027-rebuild-20261116/revision-cvpr26-lift/main.pdf`.
It retains eight scientific pages, with the LLM statement and references on
page 9; the supplement is seven pages. Its final isolated review is Overall
5.5, confidence 5 (`reviews-cvpr26-lift/independent-final-review.md`). This
is equal to the locked baseline's 5.5, not a demonstrated improvement.

The revision removes a mathematically unsupported noise-margin theorem and
its table, limits the CIFAR abstract claim to the measured source contrast,
and retains the archived visual and MLP evidence. No new training was run.
The scientific scope remains one animal, reconstructed dose operators, and
readout assays rather than a broad vision model. R95 governance and all other
manuscript histories remain unchanged.

## Latest additive state (2026-11-17, method refinement)

Use `research/manuscript/cvpr2027-rebuild-20261116/revision-method-refinement/`
as the current best manuscript. Its isolated review is Overall 6.0,
confidence 5 (`reviews-method-refinement/independent-review.md`), and it
supersedes the 5.5 `revision-cvpr26-lift` for paper quality. The paper now
states a four-step Task-Information Audit, expands transfer over relay
paths, defines a private residual for multi-source geometry, and organizes
experiments around two explicit questions. Figure generation reads only
archived records. No training or new evaluation was performed. The evidence
remains one animal, fixed linear operator and narrow readout probes; R95,
thresholds and gate states are unchanged.

## Previous state (CIFAR revision)

# HANDOFF — codex-20261116 @ cvpr2027-score-lift-20261116

Protocol: `collaboration/PROTOCOL.md`. This handoff records a work-state sync. It does not validate or qualify the manuscript.

## Current state

The archived manuscript is *Task Information Audits for Connectome Graph Interventions*. Its latest compiled revision is the 2026-11-16 CIFAR version: main PDF, 9 pages total with 8 pages of content, plus the supplement. The latest independent review is Overall 5 and Scholarly Confidence 4. Governing acceptance remains R95 = 6.0, validator `NOT_QUALIFIED`, guard `INCOMPLETE`. This revision does not replace R95 or the R129 story.

## Verified assay facts

The frozen two-convolution CIFAR-10 embedding has official-test accuracy 0.5708, printed as 0.571. It passes through the reconstructed MaleCNS two-step operator. For source 109, the named-edge MLP/linear means are 0.566260/0.558057, and path zero is 0.096387/0.098291. The preserved source 107 stays at path-zero MLP 0.440088. Base, which carries more energy but no private residual, is 0.163818/0.166211. The separate UCI digit-identity comparison is 0.851807/0.098633/0.697656, printed as 0.852/0.099/0.698. A bulk image-driven reservoir comparison was only 0.260 versus 0.253 and was not written as a positive result.

Training used local CIFAR batches 2--4, or 30,000 images. Batch 1 is absent and batch 5 does not unpickle. The official test batch is held out. The review file is `research/manuscript/cvpr2027-rebuild-20261116/reviews/independent-full-review-20261116-cifar.md`, with Soundness 4, Novelty 2, Significance 2, Clarity 3, and Rigor 3.

## Resume entry

1. Open `research/manuscript/cvpr2027-rebuild-20261116/revision/main.tex` and `sections/experiments.tex`.
2. Check Table values against `analysis/cifar-identity-readout.json`; check the one-sentence UCI comparison against `analysis/population-identity-readout.json`.
3. Read `reviews/independent-full-review-20261116-cifar.md` before changing any CIFAR claim.
4. Keep this manuscript separate from R95 and R129. A future score change requires a new isolated full review of a revised manuscript.
5. Do not rerun the encoder or readout merely to reproduce this archive sync.

# Story v3 selection — "When Does the Wiring Help?" (R129, 2026-11-14)

Owner-authorized direction (2026-11-14): fly connectome, mechanism discovery,
combine ALL current experimental results into one story; fast local experiments
allowed; then sync per research-github-sync protocol.

## Candidate stories considered

| # | Story | Evidence base | Verdict |
|---|-------|---------------|---------|
| S1 | Null-ladder methodology paper (r97 as-is) | controlled campaign + real boundary | R95 = 6.0; venue-fit and evidence-scope ceilings reached; kept as substrate |
| S2 | Real-connectome visual advantage (R63 chain) | N1–N25 chains, Fashion-MNIST/CIFAR-100 | All chains negative incl. `r63_spectral_repl`'s flagged True, which the R68 audit showed degenerates to a constant frontend choice and loses to a trivial contrast baseline — not a positive claim |
| S3 | **Two-factor gating mechanism (selected)** | controlled campaign + real density sweep + new grid + cross-system literature | Mechanism-discovery framing; every existing result family becomes a coordinate of one plane; new grid closes the causal loop |

## Why S3

- The field's published answers disagree *across systems* (adult visual gains
  [Correig-Fraga 2026], flyvis null [Dhiman 2026], larval-connectome null
  [cqw-acq 2026, +0.09pp p=0.51 n=15], whole-connectome cognitive gains
  [Cho 2026], sensory-motor boundary null [Park 2026]). A mechanism that
  predicts *where* each outcome lands is more valuable than another verdict.
- The project already holds both factors with single-variable evidence:
  path survival (task-aware null, dose ladder, survival-not-sufficient) and
  density gating (r39_density_sweep: chance at in-degree 58.4 → 0.9863 at 4.0).
- The missing piece was the orthogonal interaction — closed by a new
  pre-registered grid (r129): density × motif-survival on the controlled
  family, run locally on Apple M1 CPU in ~13 min.
- Narrative pattern learned from Kuklev et al. (arXiv:2610.13018): decompose
  the claim into levels, preregister predictions, make every level's evidence
  conditional rather than a single verdict; we adopt the same multi-scale
  adjudication shape (controlled → real wiring → grid) plus a winner's-curse
  cautionary note (their n=5→n=15 evaporation).

## Story arc of the v3 manuscript

1. Cross-system disagreement is the hook (5 cited datapoints).
2. Reframe: the right question is WHICH STRUCTURAL MECHANISM gates the
   advantage, not whether wiring "helps".
3. Controlled scale: effect is real, ladder can't localise it → survival–match
   gap (phenomenon + taxonomy + constructive repair).
4. Real-wiring scale: density alone gates solvability (single-variable sweep +
   oracle control).
5. Interaction: pre-registered grid — dense background erases a protected
   path; sparse background can't rescue a destroyed one.
6. The literature becomes points on the (survival × density) plane; the
   standard (survival-count audit + gate measurement) is the deliverable.
7. Honest bounds: real image task negative; grid is one graph realization,
   six seeds; mechanism scoped to neighbour-averaged propagation with pooled
   readout (per-edge learnable gains are a different regime).

## Collision check (2026-11-14, live web)

- Larval null repo (github.com/cqw-acq/connectome-null-models) — closest
  external datapoint; cited as evidence FOR the mechanism, not against.
- Park arXiv:2609.39248, Cho arXiv:2610.10014 — cited.
- No CVPR 2026/2027 paper occupies the "two-factor gating mechanism" slot.

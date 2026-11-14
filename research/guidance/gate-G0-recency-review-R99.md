# G0 recency review — R99, 2026-11-12 (independent web check)

Purpose: close the G0 gap left by `gate-G0-evidence-review-R98.md`, which found
the saved baseline map evidence-complete but with no independent recency review.
This session ran a live web search plus a full-text fetch of the strongest new hit.

## Decisive new finding: a 2026 prior art paper already reports the positive
## topology effect this recovery is chasing

**Kuklev, D. (2026), "What Survives on Real Drawings: Active Sampling, Connectome
Wiring, and Matched Baselines in Architectural Document Vision",
arXiv:2609.24565v2, September 2026.**
https://arxiv.org/html/2609.24565v2

Verified verbatim numbers from the article:

| Finding | Number |
|:--|:--|
| Intact connectome, hatch matching, development split | `0.857` area-weighted accuracy |
| Degree-preserving rewiring (in/out degree preserved), 3 rewiring seeds | `0.539`, intact advantage `+0.318 [0.296,0.339]` |
| Type-pair + transmitter-sign preserving rewiring | `0.586`, advantage `+0.271 [0.248,0.293]` |
| Erdős–Rényi same-density null | `0.500`, advantage `+0.356 [0.334,0.379]` |
| Segmentation matched null | IoU `0.483 → 0.089`, ROC-AUC `0.964 → 0.514`, paired diff `0.397 [0.365,0.431]` |
| **Positive control** (silencing R7/R8 input types) | costs `0.092 [0.079,0.104]`, proving the protocol detects a known structural effect |
| Graph scale | `45,669` nodes, `1,513,231` edges, invariants verified, wiring hashed |

This is a **positive, strictly-null-controlled, multi-seed topology effect on a
real visual task with an intact positive control** — i.e. exactly the "Raise ①"
evidence that R95/r93 said was missing and that the R99 user directive asks to
supply. It predates this recovery.

### Its own negative qualification (must not be omitted)

The same paper then bounds the claim: on the held-out split `receptors only
0.894` vs `Fly + drift 0.835` (receptors lead by `+0.059 [0.043,0.075]`); a CNN
on raw receptors `0.961` vs fly front-end `0.962` AP (`+0.001`); silencing T4/T5
leaves both tasks intact. Conclusion: *"Exact structure remains insufficient to
beat what the moving retina already provides"* and *"A structure can be
load-bearing for a computation without that computation being the one a task
needs."* The held-out split was **not** used for the rewiring nulls (opened once,
for model comparison only). Wire-length null could not be built (only `1.08%` of
edges have both endpoints' coordinates), so exact wiring is not separated from
retinotopy/locality. Production drawings are proprietary.

### Second corroborating hit

"Representational geometry as a fidelity metric for connectome-constrained
networks: evidence from the Drosophila visual system" (AI Medical Compendium,
2026, https://www.aimedicalcompendium.com/article.cfm?id=253759): on the Flyvis
pretrained ensemble, real vs weight-shuffled / degree-preserving / ER wiring is
distinguishable **before** training (`p<10^-13`), but once both are trained to
task adequacy the distinction narrows substantially and in one case (trained ER,
OFF polarity) closes completely. An honest largely-null result on the training
question. This is close to Candidate E's "competence-conditioned null" framing.

## Consequence for the goal (stated plainly, not softened)

1. **The "add a positive visual effect" gap is partially pre-empted.** A 2026
   arXiv paper already supplies a large, controlled, positive topology effect on
   a real visual task. Simply producing another positive number on a null ladder
   would now be incremental, not the decisive contribution R95 asked for.
2. G4 (novelty / non-duplication) now has a **severe prior-art risk** from
   arXiv:2609.24565 plus the previously noted Park 2026 (boundary-preserving
   nulls) and Dhawan 2026 (FlyHack). Candidate E must be positioned against all
   three: its distinct angle is *response-conditioned / path-preservation under a
   frozen competent visual function with sealed forecasts*, on optic-flow inputs,
   not architectural drawings.
3. More useful than another positive effect may be the **discriminating
   prediction**: Kuklev shows wiring is load-bearing yet not task-useful beyond
   the retina. A result that *predicts when* path-preserving controls matter
   (vs when the input alone suffices) would answer an open question rather than
   repeat a known effect.
4. **This does not lower the goal or change any score.** Governing remains R95
   6.0. It changes the evidence strategy, per RGE4 diagnosis → strategy change.

## Gate decision

- **G0 (literature/baseline map): evidence now current with an independent live
  recency check**, but the newly found prior art must be added to
  `literature-baseline-matrix.md` before G0 can be marked passed by its gate
  owner. No stage status was mutated in this session.
- **G4: newly flagged as high-risk**, not evaluated/passed.
- No experiment, manuscript, score or frozen identity was changed by this review.

# Discriminative prediction proposal v1 — PROPOSED, NOT ACCEPTED

Date: 2026-11-12. Owner: main session R99 (user authorized the route change).
Status: **a versioned contract proposal, not an accepted guidance, not a result,
not a score change.** Under `f-guidance-builder-v1` / `f-research-v1` a new
binding claim requires a versioned contract change that reopens P0 and
reaccepts P1A/P1B in order. Nothing here grants that. All existing v1/v2/v3
contracts and frozen artifacts remain in force and are not edited.

## Why the axis changes

R99 independent recency review (`gate-G0-recency-review-R99.md`) found
arXiv:2609.24565v2 (Kuklev 2026) already reports a large, strictly-null-controlled
**positive** topology effect on a real visual task (intact `0.857` vs
degree-preserving `0.539`, `+0.318 [0.296,0.339]`, 3 seeds, with an R7/R8
positive control). It then bounds the claim: on held-out data a receptors-only
descriptor leads the circuit (`0.894` vs `0.835`), a CNN on raw receptors ties
the fly front-end (`0.961` vs `0.962`), and T4/T5 silencing leaves both tasks
intact. Its own conclusion: exact structure can be load-bearing for a
computation without that computation being the one the task needs.

So "wiring matters" is no longer a decisive contribution. The open question it
leaves — **when does preserving a computational path matter, and when does the
input alone suffice?** — is. This proposal turns that question into a falsifiable
prediction using the already frozen Candidate-E machinery.

## What is reused unchanged

- `response-null-protocol-closure-v4.md`: gray initial state, composed-mask
  aggregate forcing, noise-only calibration (std `.08`, lower clamp, four draws,
  frozen seed key), three mandatory arms, K=45 family-wise α=.05.
- `response-null-prediction-dataflow-v1.md`: `q` = RMS(null vs original decoder
  flow) / original-output RMS, floor `1e-6`; sealed reference-gated recurrent
  forecast; explicit query-label/outcome isolation; sentinel isolation check.
- `paired-edge-set-executable-spec-v3.md`: response / geometry / magnitude /
  shuffled-response / random arms on the **same edited original edges**, common
  binned geometry, four complete candidates per family, `rawSMD<=.1` balance.
- `competence-baseline-spec-v1.md`: zero flow, scene-mean, input-only temporal
  ridge; and the official pretrained FlyVis + DecoderGAVP as the authoritative
  reference.
- `prospective-identities-v1.json`, `pilot-input-manifest-v2.json`: development
  models 000/001, four scenes, crop1, 2 windows, 4 noise draws; withheld
  confirmation identities stay sealed and unauthorized.

No threshold, identity, comparator, K, seed, or stop rule is relaxed.

## The new binding question (call it D1)

**D1.** A *training-free, pre-registered* "input-sufficiency margin" predicts,
on held-out scenes and independent mask families, how much a path-preserving
(response-matched) null differs from balanced controls in functional disruption.

### Definitions (frozen before any outcome is opened)

For a clip `c` under frozen checkpoint `m`:
- `q_control(c, a)` = normalized paired flow-output discrepancy for arm
  `a ∈ {response, geometry, magnitude, shuffled, random}`.
- `Δ(c) = median_a q_control(c, a) − q_response(c)` — the **path-preservation
  advantage**: how much less the response-matched null disrupts the frozen
  function than the balanced controls on the same edited edges.
- `R(c)` = **input-sufficiency margin**, computed only from the *original*
  (unrewired) model and the frozen competence baselines, with no access to any
  null outcome:
  `R(c) = EPE_input-only-ridge(c) − EPE_frozen-circuit(c)`.
  Positive `R` means the circuit beats an input-only descriptor on that clip,
  i.e. the wiring's extra computation is task-useful there. Kuklev's held-out
  finding corresponds to `R < 0` (receptors lead).
- Both `R` and `Δ` are aggregated equally over clips within a scene, then over
  scenes; the same cluster structure is used in all bootstrap replicates.

### Directional prediction (one-sided, preregistered)

On **held-out** scenes and **independent** mask families, `R` positively predicts
`Δ`: clips where the frozen circuit adds value over its own input should be
exactly the clips where preserving the path matters. Formally the primary gate is
a clustered 95% lower bound > 0 for the paired within-scene slope of `Δ` on `R`,
plus a leave-one-scene-out rank/sign prediction beating the majority baseline
and all seven frozen structural/scale comparators from
`response-null-prediction-dataflow-v1.md`.

### Falsifiers (any one fails D1; failures are retained, not reframed)

1. The slope CI includes zero, or LOGO sign/rank prediction does not beat the
   majority baseline and the seven prespecified comparators.
2. `geometry`, `magnitude` or `shuffled-response` arms predict `Δ` equally well —
   i.e. the effect is a geometry/magnitude/dose artefact, not path correspondence.
3. `R` computed from shuffled trajectory/response correspondence predicts `Δ`
   as well as the true `R` — the "prediction" is not about the computational path.
4. The relation holds only on development scenes and reverses or vanishes on
   held-out scenes / independent mask families.
5. `delta_noise` is ineligible or unstable, competence gates fail, or balance
   `rawSMD>.1`; any of these blocks interpretation and returns to design.

### Why this is worth more than another positive effect

It converts a contested binary ("does topology help?") into a **quantitative
condition on when it helps**, and it directly engages Kuklev's own negative
qualification instead of ignoring it. A confirmed D1 would explain conflicting
reports (different protocols land at different `R`), a failed D1 is an honest,
informative negative. Either way it is a discriminating result, not a benchmark
increment.

## What must happen before any D1 outcome may be queried (ordered, non-skippable)

1. **Contract**: this proposal must be independently reviewed by
   `ccf-experiment-designer` + `ccf-idea-reviewer`, then accepted as a versioned
   contract change (v4) that reopens `P0` and reaccepts `P1A/P1B` in order.
   Until then D1 is a hypothesis only.
2. **Guidance gates**: G0–G8, validation, handoff each need their own substantive
   review. G0 now has an independent recency check but the new prior art must be
   formally incorporated by the gate owner; G4 is high-risk and must be resolved
   against Kuklev 2026, Park 2026, Dhawan 2026 and the 2026 geometry study.
3. **Runner**: the scientific null runner and predictor, which
   `startup-stage-plan.md` says are not yet completed/isolated/reviewed, must be
   finished, SHA-frozen, independently audited, and pass its synthetic + sentinel
   isolation checks. `run_local_baseline_v2.py` refuses to run until
   `P0/P1/P1A/P1B/P2` are passed; do not bypass that guard.
4. **Pilot gates, in order**: competence (frozen circuit beats zero / scene-mean /
   input-only ridge), empirical evoked dose & common support, noise calibration
   stability, geometry balance, control separation, transfer, conservative
   precision. Any failure returns to the earliest affected design gate.
5. **Confirmation authorization**: the ≤32h / K=45 formal confirmation panel is
   **not authorized** by the current user directive. Request explicit approval
   once a credible pilot result exists. No development pilot may be presented as
   confirmation.

## Explicit non-claims

- No positive visual effect is reported here. No number is computed here.
- No existing contract, frozen identity, score, threshold or gate status is
  changed by this document.
- No claim that Kuklev 2026 is wrong; it is treated as prior art that sharpens
  the question.
- No commit, push, submission or publication.

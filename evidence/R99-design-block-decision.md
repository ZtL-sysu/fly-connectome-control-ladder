# R99 design-block decision — D1 discriminative prediction

Date: 2026-11-12. Owner: main session (team lead). This is an RGE4
**gap diagnosis + strategy change** record, not a result, not a score change.

## Evidence chain

| Round | Artifact | Independent verdict |
|:--|:--|:--|
| v1 | `discriminative-prediction-proposal-v1.md` | `revise` (close to `reject`); `discriminative-prediction-independent-review-v1.md` |
| v2 | `discriminative-prediction-proposal-v2.md` | `revise`; `discriminative-prediction-independent-review-v2.md` |

Both reviews are retained in full. Neither proposal was accepted. No number was
computed, no gate status, contract, frozen identity, threshold or score changed.

## Diagnosis (RGE4 step 4): why not v3

A v3 patching the algebra is **not** the right next move. Classifying the failure:

- **Not "means missing"**: Novix works on a verified route, official source and
  pretrained models are provisionable with exact commit/hash, and the frozen
  paired-edge/null machinery exists.
- **Not "strategy wrong" in the sense of a bad axis**: both reviews credited the
  discriminative "when does path preservation matter" question as more honest
  than another positive-effect number.
- **CONDITION NOT MET (decisive)**:
  1. **Statistical power is structurally absent in the authorized pilot.**
     `prospective-identities-v1.json` gives 2 models × 4 scenes × 2 windows ×
     crop1 = 16 clip units / **4 scene clusters**. A 4-cluster bootstrap has
     ~35 distinct resamples, so a clustered 95% lower bound has resolution
     ~1/35 and `LB > 0` is nearly unattainable. The nuisance basis N (~10+
     columns) is near-saturated at 16 points. The v2 reviewer further showed
     the added `q̄` is a null outcome and makes `Δ ~ N + R` an endogenous
     "regress the outcome on its own function" — a fatal-class defect.
  2. **Labels**: official Sintel TEST flow GT is withheld, so `R` is undefined on
     genuinely held-out natural scenes. `procedural_confirmation` does supply
     known labels, but it belongs to the confirmation stage.
  3. **Confirmation is not authorized** (`execution-contract-v3.md` §25/§70–76;
     `local-pilot-budget-v2.json` `scientific_confirmation_authorized: false`).
     The v2 reviewer confirmed D1 is **not decidable in the development pilot**.
  4. **Runner**: the scientific null runner and predictor are not yet
     completed/isolated/reviewed (`candidate-E-local-v2/startup-decision.md:7`;
     the earlier citation to `startup-stage-plan.md` was a misattribution and is
     corrected here). `run_local_baseline_v2.py` guards on
     `P0/P1/P1A/P1B/P2` all passed; all G0–G8 remain pending.

Patching §2 of the proposal a third time would improve prose while leaving all
four conditions untouched. That is polishing a blocked design, not progress.

## Decision: `BLOCKED_ON_CONFIRMATION`, return to ordered gates

1. `discriminative-prediction-proposal-v1.md` and `-v2.md` are **retained as
   superseded design evidence**. The D1 question is kept as a **candidate for a
   future confirmation-stage contract**, not as the current pilot's claim.
2. No v3 will be issued until the blocking conditions change. Reopening D1
   requires, in order: a confirmation authorization from the user, a v4
   contract with a revised K / Bonferroni or gatekeeping α allocation, an
   accepted scene/mask split with real cluster count, a labelled held-out arm
   decision (including the procedural labelled arm), and a completed/audited
   scientific null runner.
3. **Strategy changes back to the ordered engineering and pilot gates** that are
   prerequisites for *any* result — positive, negative or discriminative:
   - Resolve the Novix two-route trade-off (CPU route has source/models but no
     torch/GPU; GPU short tasks had torch+CUDA+L4 but long provisioning dies at
     the control plane) so one sandbox has both dependencies and compute.
   - Complete, SHA-freeze, isolate and independently audit the scientific null
     runner and predictor.
   - Run G0–G8 in canonical order with their own substantive reviews (G4 must
     resolve Kuklev 2026 / Park 2026 / Dhawan 2026 / the 2026 geometry study).
   - Then f-research-v1 P0 → P1A/P1B → P2, and P3 baseline-first competence
     (zero / scene-mean / input-only ridge vs official FlyVis + DecoderGAVP).
   - Only then can any of E1/E2/D1 be considered.
4. **User decision required (paper2 prompt §7(b): a change of experimental
   scope)**: authorizing the ≤32h confirmation panel / K=45 formal family. This
   session does **not** assume it. It is presented to the user as an explicit
   choice; until answered, work stays within the authorized development pilot.

## What this does NOT do

- Does not abandon the 8-point goal, lower any threshold, change any score, or
  declare success/failure of the science.
- Does not hide two failed independent reviews; both are on disk.
- Does not claim a positive or negative result from any Novix run.
- Does not modify any frozen artifact, contract version, or gate status.
- No commit, push, submission or publication.

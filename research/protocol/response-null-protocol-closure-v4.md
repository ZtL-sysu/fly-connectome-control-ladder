# Candidate E protocol closure v4 — prospective

Owner: ccf-experiment-designer. Resolves design-only items from independent design-review-v3; static construction/resource acceptance remains pending. No scientific inference or accepted guidance exists. Paired-edge-set-construction-v1 remains a separately proposed refinement until its static support is checked.

## Fixed state, gray baseline, and vector weighting

For each frozen checkpoint and clip, use eval mode and float32. Compute the original network's gray-input initial state with `Network.steady_state(t_pre=.25, dt=.02, batch_size=1, value=.5)` as in the released solver's test defaults (`solver.py:519-552`). Store that complete state; original, null, noisy-original and forecast all start from its identical copy. Do not independently equilibrate the rewired network. This defines an acute intervention from a shared state.

At each clip's integration length, gray means every receptor input equals .5. For a 19-source-frame clip the audited nearest-exact resampling produces 40 integration inputs; derive the length from the actual preprocessing and assert it rather than substituting the unrelated B12/T269 engineering stress shape. Compare gray and visual trajectories at the same time indices after the same initial state. Evoked source mass uses RMS of their ReLU difference, equally weighting each clip and each of its integration times. Report zero evoked-mass fractions by source type and the fraction of whole-graph mass in the editable pool.

For matching, concatenate absolute gray and visual ReLU trajectories: gray has total weight one clip, and each of the fixed development visual clips also has weight one clip, irrespective of clip duration. This distinguishes dose from matching. Matching uses no labels; competence uses separately logged labelled development outcomes.

## Composed-mask forcing

Individual source-vector distances propose swaps only. For **every complete mask** calculate `r_c,t = (A_null-A_original) ReLU(v_original,c,t)`, including all swaps and shared targets. The scalar aggregate objective is the equally clip-weighted mean of time/node mean squares of r, including the gray clip with the weighting above; report its square root in current units and retain per-clip values. Do not replace this with the sum of pairwise distances. Report both to expose cancellation/reinforcement.

Before pilot execution freeze a finite candidate-mask rule. Proposed bound: at most four complete candidates per family on the same edited-edge support; select the response arm by the smallest **aggregate** objective on development only, retaining all candidates/scores/rejections. Structural random selection is response-independent; geometry and magnitude arms select by their corresponding predeclared criteria from equally bounded support. All complete-arm forcing values are logged. Candidate diversity, topology certificates and geometry balance are required independently of objective ranking. If the selected response arm fails to improve aggregate forcing over balanced controls on development, stop; do not add candidate families until success. No query/confirmation responses may change that selection.

The exact block/global candidate rule still needs static support acceptance. This paragraph supplies its complete-mask objective and search boundary, not a claim that the pending constructor realizes sufficient support.

## Noise-only operational reference

Choose **noise-only**, not joint augmentation. Apply dedicated standard-normal draws scaled by .08 to the cropped, normalized **rendered receptor-luminance** source-frame tensor. Lower-clamp at zero; retain values above one. Disable contrast/brightness, rotation, reflection and all unrelated stochastic transforms. Then use the source's nearest-exact 24-to-50Hz input resampling. Pair clean/noisy inputs on crop, receptor rendering, state, model and decoder. This is a source-inspired isolated sensitivity reference; it does not reproduce the full training augmentation distribution.

Predeclare four noise draws per development model/clip. Derive a dedicated per-identity draw seed from SHA256 of a public run-local seed key plus model/scene/crop/draw IDs; store both seeds and realized noise-array hashes. Do not reuse the task seed as evidence of historical noise draws. Fix the seed key before calibration. Four draws is the initial finite calibration budget; pilot-based precision may require a versioned repeat-count correction before confirmation, with all original draws preserved, within the same cumulative compute cap.

Use normalized output discrepancy q as defined in prediction-dataflow-v1. First average equally over clips within development scene and equally over the four draws, then take the median of model-by-scene calibration cells as delta_noise. Report every cell, raw output units and input lower-clipping fraction. This specifies the previously vague robust aggregation. Recompute that same statistic in nested paired bootstrap replicates. A near-zero original output or unstable/near-zero calibration scale blocks the ratio assay. The exact eligible-reference set is determined and frozen on development; report all exclusions, and apply the same numerical rule to confirmation without deleting failures silently.

## Proposed finite inferential family

Three mandatory evaluation arms: naturalistic within-checkpoint matching; naturalistic source-to-withheld-checkpoint mask transfer; procedural speed/contrast-shift within-checkpoint matching. Keep these separate and retain fixed checkpoint-panel interpretation.

For each arm E1 has seven directional gates: response upper bound below delta_noise; random and geometry lower bounds above delta_noise; and paired response-minus-control upper bounds below zero for random, geometry, magnitude-only and shuffled-response controls. E2 has eight directional gates per arm: the half-margin mean absolute forecast-error bound plus improvement over each of seven comparators named in design-repair-v2. This proposes K=45 one-sided claims with family-wise alpha .05 and at least 100,000 bootstrap replicates. Secondary descriptive analyses cannot substitute for a failed gate. If E2 is retained as a binding secondary claim, all its stated gates remain binding; changing that status requires a versioned design review before confirmation.

The same bootstrap replicate maintains all arm/checkpoint/scene/mask pairings and independently recomputes development calibration from scene/noise-draw clusters. Report conditional fixed-panel uncertainty and a separate finite-ensemble sensitivity analysis; shared initializations remain explicit. The scene-family grouping must be finalized from source scene identities, not assumed from filenames alone. Use actual pilot variance/cost for precision simulation after P2 and before confirmation; K and endpoints are frozen before opening confirmation. If conservative precision is infeasible within the cap, return to design rather than treat this proposed family as accepted merely because it is explicit.

## Source/split boundary

The actual archived metadata omits `original_split`, while current Task's constructor defaults false and current task YAML sets true. Thus do not infer archived split identities from the current YAML. All source training/validation material is development-exposed for this recovery. Official Sintel TEST images have independently verified direct access, but their flow ground truth is withheld. They support paired function agreement only. Their sequences come from the same rendered film; avoid claims of independent real-world environments, biological networks or camera data.

Freeze exact model/scene/clip/mask manifests and the geometry bins before any development scientific run. No resource profile, static-support pass, positive null result, final guidance or score follows from this protocol closure.

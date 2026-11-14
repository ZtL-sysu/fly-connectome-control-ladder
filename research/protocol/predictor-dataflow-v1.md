# Prospective predictor data flow v1

Purpose: close the leakage ambiguity in C2 of the proposed mechanism repair. Owner: ccf-experiment-designer. This specification is prospective and has no measured efficacy. No claim that the simple predictor is itself a novel algorithm.

## Prediction target and admissible inputs

Target: immediate change in mean squared task error under a frozen-parameter graph intervention, at a fixed training checkpoint. This target is different from the effect of independently training a null architecture. All network parameters, canonical decoder weights/biases, state initialization, stimulus mapping and intervention construction are frozen. Output dimension q=2.

For stimulus x let f(x) be the original model output, f_m(x) the intervened output, d_m(x)=f_m(x)−f(x), and e(x)=f(x)−y(x). Define Q(S,m)=mean_over_examples_and_output_dimensions[d_m²] and A(S,m)=2·mean[e·d_m] with the same elementwise normalization. The observed loss effect is Q+A exactly. A on confirmation examples uses their targets and is **an outcome decomposition only**; it is forbidden in predictor inputs.

One row is a (training seed, checkpoint, independently generated mask, stimulus-condition group) tuple. The frozen forecast feature vector is:

1. Q_train and A_train, evaluated on the original training stimuli and labels.
2. Q_query, the output-displacement energy on the query stimulus batch (no query labels).
3. mean_query(||f||²)/q and mean_query(||f_m||²)/q (no query labels).
4. Checkpoint index in the fixed grid, encoded as log(1+updates).

Features never include query direction identity, generating angle/speed metadata that determines labels, targets, validation/test residuals, query losses, or any statistic computed after outcome labels are opened. Generated task metadata is treated as a label source and withheld accordingly. Unlabeled query inference is allowed and declared as part of method cost; this is not a zero-forward-cost forecast. Model selection cannot use query-effect outcomes.

Fit one regularized linear predictor to calibration effects on validation conditions and calibration masks. All standardization is fitted on calibration rows. Ridge penalty is selected inside calibration by leaving entire mask families and condition groups out, using a fixed grid {0, .001, .01, .1, 1, 10, 100}; zero means pseudoinverse with a fixed rcond. Models/feature sets and forecast objective are frozen before confirmation. No per-test-condition recalibration.

## Comparators and ablations

- Zero-effect predictor and calibration-mean predictor.
- Source-training effect Q_train+A_train transferred unchanged; this prevents rebranding the exact loss identity as forecasting.
- Query output-displacement energy Q_query and query output-norm features, using the identical calibration procedure. Direct output change is a strong observable comparator, not hidden from baselines.
- Pure structural predictors: realized changed endpoint fraction, edge overlap, preserved degree/self-loop checks, displacement and group-composition summaries available for the same intervention.
- Latent-state displacement and activation-scale predictors, identical fit/regularization budget.
- Full predictor without A_train; without task projection (replace output displacement with latent displacement); and without checkpoint feature. Compare on the same confirmation rows and cluster at independent training seed.

All primary baselines and ablations are fixed before confirmation. Report whether C2 adds any predictive information over direct output-displacement and source-loss transfer. If it does not, retain only a descriptive decomposition and drop predictive-method novelty. A tiny advantage with imprecise or task-irrelevant error reduction does not pass the strong-result gate.

## Identity and outcome separation

Engineering/pilot: original public TopoSens identities and up to two new training seeds/masks; train/validation only. These identities remain exposed and excluded from confirmation. Pilot may estimate runtime/variance and reject candidate mechanisms; it may not select by confirmation outcomes.

Before confirmation, write a manifest specifying exact training seeds, calibration-mask RNG seeds, confirmation-mask RNG seeds, stimulus generator/config hashes, stimulus IDs and condition groups. A mask chain from a common initial RNG trajectory is one family; dose checkpoints from it cannot straddle calibration and confirmation. Distinct mask families and query condition groups are held out jointly. Fit coefficients/regularization on calibration data only. Validation conditions used for horizon selection cannot also be labelled untouched confirmation.

Use 12 fresh training seeds provisionally, each with three fresh confirmation-mask families, subject to the measured budget/power gate. Calibration graphs need their own masks; their inference costs must be counted in addition to training. Biological runs are shared within training seed. Report seed-average forecast error/improvement; crossed mask effects are secondary. Conditioning on “successful” training seeds after seeing confirmation is forbidden. Failed seeds, OOMs and nonfinite outcomes remain recorded.

Keep confirmation labels outside the predictor process. The inference entrypoint receives only query tensors, frozen model/decoder, mask and the fitted predictor bundle. Evaluation joins its sealed predictions with labels afterward. A sentinel test must show that replacing query targets while keeping query tensors fixed cannot change forecasts. Arithmetic Q+A reconstruction is tested separately and never called prediction.

## Practical-resolution proposal (requires review)

MovingEdge's native generator has a 30° direction grid. Half of that native resolution, 15°, is a proposed practical margin for circular-error changes, fixed from task geometry rather than an observed proposed-method gain. The corresponding unit-normalized directional-vector MSE difference for an otherwise exact direction is 1−cos(15°)≈.034074. This is a geometric reference; raw unnormalized decoder MSE does not equal this quantity generally. Report raw MSE, circular error and prediction magnitude separately.

Proposed C1 strong discovery: a replicated assay×topology interaction whose seed-clustered uncertainty resolves a 15° change in circular error, with matched readout/projection controls and confirmation on independent visual input. This is a demanding candidate criterion, not a promised effect. Competence of a decoder can be operationally defined as circular error below half the native grid interval plus positive mean-predictor skill on validation; feasibility is unverified. Full grid vs angle-parity split and naturalistic optic-flow adaptation require separate metric contracts, so this geometric reference cannot silently supply their margins.

C2 requires a preregistered useful forecast-error reduction in those physical units as well as an interval excluding zero improvement over all stated comparators. Its numerical amount, adequate sample size and cross-task metric conversion remain unresolved and block acceptance. A new confirmation contract cannot be issued merely because this data flow excludes label leakage.

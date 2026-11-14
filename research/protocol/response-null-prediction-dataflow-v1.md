# Candidate E2 frozen prediction and data-flow specification

Status: prospective repair for independent review; no result or guidance acceptance. This replaces E2's unfinished forecast placeholder in response-null-evidence-contract-v1.md for review purposes; no accepted contract is being weakened or overwritten.

## Outcome and permitted observations

For each fixed checkpoint, complete mask and query clip, predict q: RMS difference between null and original trained-decoder flow outputs divided by original-output RMS. Aggregate frames/pixels/channels within clip, then equally across clips within each scene. The normalization floor is fixed at 1e-6 in the source flow units; clips below it are marked reference-ineligible and reported, never silently removed. Both original and null always use the same checkpoint's recurrent parameters, decoder in eval mode, stimulus map and explicit initial state.

At forecast time the process may read: the frozen mask; paired checkpoint/config; **unlabelled query images**; and the original model's trajectory/flow outputs on them. It may not execute the nonlinear rewired network or read any rewired query trajectory/output, query flow labels, query loss, outcome table or confirmation-based selection record. This is a reference-trajectory-assisted forecast, not a training-data-only or zero-inference method. Its cost includes the original forward pass, decoder calls and any response simulation.

Held-out model reference trajectories are permitted for forecasting only after the graph generator/mask is frozen. They may never select or repair a transferred mask. Per-model matching and cross-model transferred masks keep their separate selection boundaries.

## Primary fixed predictor: reference-gated recurrent response

Let v[t] be the original trajectory, D=diag(dt/max(tau,dt)), A' the rewired effective-weight operator and G[t]=diag(1[v[t]>0]). Start z[0]=0 and compute

z[t+1]=(I−D)z[t] + D A' G[t] z[t] + D(A'−A)ReLU(v[t]).

This linearizes the activation about the original state while retaining A' in the feedback. It is exact if the rewired state remains in the same ReLU regions. It is not an unconditional nonlinear/OOD bound and no claim of a new linear-response algorithm is made. Query labels and true rewired states are absent. Feed v[t]+z[t] into the same fixed trained nonlinear decoder in eval mode; its difference from decoding v[t] gives the forecast q_hat. Do not replace G[t] using actual null states. Recurrent state can be forecast sequentially; decoder batching and precision are fixed before confirmation.

Primary forecast error is scene-mean |q_hat−q|/delta_noise, using the independent development-frozen operational noise scale from E1. Primary evidence target: model/scene/mask-clustered 95% upper bound on this error <=.5 (half one operational preservation-resolution unit), and a paired improvement interval excluding zero against every prespecified purely structural, geometry, magnitude and development-output-transfer comparator. This half-unit criterion is a prospective resolution requirement, not an arbitrary desired accuracy gain. If delta_noise is ineligible or too unstable, the claim is blocked. Also report threshold classification at q=delta_noise with all ambiguous cases retained, prediction-interval coverage if such intervals are fitted, and the full error distribution.

The linear-response formula is the primary mechanistic predictor, not a novelty claim by itself. Its scientific value would be predictive fidelity for materially non-isomorphic, active graph edits and a verified forcing-matching ablation at matched geometry/dose. If prediction fails, do not retrospectively replace it with an outcome-trained black box or call an exact outcome reconstruction a forecast.

## Strong comparators, calibration and ablations

1. Zero divergence and development calibration-median divergence.
2. Development-input output discrepancy of that complete mask transferred unchanged to query conditions.
3. Aggregate query forcing norms (time-integrated L2, peak infinity norm), each with a single nonnegative scale coefficient fitted on development/calibration masks only.
4. Structural/geometry features: realized edge turnover, active-weight mass, recomputed endpoint length changes and parameter-group composition. Activity-only: baseline activity scale and source activation magnitude. Fit regularized linear regressors with the same fixed calibration split/grid; no generator-ID shortcut.
5. Ablations of the primary predictor: omit recurrent feedback; replace A' feedback with A feedback; replace forcing with a magnitude-only surrogate; and shuffle response-to-neuron correspondence consistently with the generator ablation. These test mechanism, not optimizer victory.

For fitted comparators use ridge penalties {0,.001,.01,.1,1,10,100}, normalization learned only on calibration rows, mask-family/scene-group nested validation, and no confirmation label/outcome access. The fixed primary predictor has no fitted regression coefficients. Learned comparator hyperparameters and any predictive intervals must be sealed before confirmation. A first-order prediction using actual rewired trajectory differences is forbidden.

## Split manifest and sealed execution

Freeze development/calibration model IDs, untouched confirmation model IDs, source archive/checkpoint/config hashes, scene/clip identities, preprocessing/resampling settings, mask RNG families, dose and control balancing before opening confirmation outcomes. All doses from a common RNG swap chain are one family and cannot straddle calibration/confirmation. Original public source validation remains exposed; use it as development. Public Sintel TEST images supply new functional-preservation inputs without claiming flow accuracy; separate procedural confirmation supplies known task labels where appropriate.

Execution order: (a) freeze generator/calibration and save hashes; (b) run original query trajectory, derive forecasts and seal prediction files; (c) in a separate outcome process run the actual rewired recurrence and join outputs by identity; (d) evaluate with the prespecified aggregation and uncertainty rule. A sentinel isolation check must show that replacing confirmation labels/outcome files cannot change forecasts. Mask generation receives no query trajectory or query predictions. Test refactoring or failed confirmation creates an exposed test and requires a new justified confirmation set, never relabelling.

Twenty withheld trained-solution identities and three independent mask families per arm are provisional within the32GPUh cap; they are not independent initialization seeds. Use a finite-ensemble model analysis and mask/scene uncertainty conditional on this source ensemble, with shared original runs counted once. If conservative development-based precision planning cannot resolve the half-unit target and E1 equivalence at this cap, return to design before confirmation. Keep all failed models/masks, and do not condition final estimates on favorable confirmation performance.

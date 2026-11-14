# Mechanism-level recovery candidates

Owner: ccf-idea-optimizer, standard. These are planned ideas, not observed findings.

## Candidate A: retinotopic alignment as an unheld null invariant
Problem: degree-preserving rewiring of a visually grounded network may conflate computational topology with alignment to input/output coordinates.
Mechanism: graph adjacency alone does not define visual computation; sensory map, output map, signed dynamics and spatial displacement jointly define the operator. Compare degree-only controls with degree + displacement/type-preserving controls at matched initialization.
Assumptions: official flyvis source exposes stable spatial/node-type maps; constraints admit enough rewiring; strict random initialization and matched parameters are possible.
Falsifier: after alignment and dynamic-scale are matched, control-choice effects vanish within baseline uncertainty or constrained swaps cannot mix; then do not claim an unrecognized topology mechanism.
Contribution: discriminating control protocol plus mechanistic evidence, conditional on held-out motion scenes/stimuli.
Risks: structure-alone already studies wiring cost; alignment or retinotopy matching may already be standard. Need stronger novelty than adding one more null.

## Candidate B: task-aligned local transfer rather than raw survival count
Problem: R97 count-only model fails (linear R2=.1004); same edges can carry unaligned features.
Mechanism: linearized or finite-difference input-to-output transfer of an untrained/frozen model depends on signed weights, nonlinear operating point, input/output map and time. Measure response kernels on unlabeled train stimuli, test whether matched transfer predicts which nulls change inference on disjoint motion conditions.
Assumptions: derivative calculation feasible at published graph scale; transfer statistic fixed without held-out labels; metric improves on degree/geometry-only baselines across independently constructed controls.
Falsifier: held-out prediction does not beat constant/degree/geometry baselines; equivalence of transfer does not stabilize behavioral conclusions; comparison driven only by activity scale.
Contribution: a task-aligned control sufficiency criterion.
Risks: task-transfer matching could preserve the outcome tautologically; only local initial kernels, no test labels or optimized behavioral outputs, and explicit nontrivial control ensemble are admissible. V6 disproves raw-path-ratio prediction, not this as-yet untested distinct mechanism.

## Candidate C: density versus specific motif damage
Problem: real-wiring density sweep reaches ceiling even when protected edges are absent.
Mechanism: degree/signal-normalization and alternative paths may dominate specific two-hop motif survival. Compare degree/weight/endpoint-matched motif versus nonmotif disruption at fixed density.
Falsifier: motif-specific damage does not differ from matched random damage.
Contribution: diagnostic boundary/mechanism correction.
Risk: remains synthetic XOR, weak CVPR scope even if positive; do not prioritize over published motion pipeline without a novelty route.

Selection remains unresolved pending public source inspection; no candidate marked proceed. No answer injection or new biological topology fabricated.

## Candidate D: competence-conditioned topology inference
Problem: a negligible connectome-versus-null gap during an uninformative learning regime cannot establish equivalence for competent visual computation.
Public-source observation: Topological Sensitivity uses 5/10 Adam steps on balanced unit-vector motion-direction targets. Its packaged strict-control MSEs at 10 updates are .504455/.502693, and zero-vector prediction has MSE exactly .5 on those targets. This is a reported-number comparison, not a new rerun and not proof of no information.
Mechanism: measured loss = target variance + prediction variance - 2 prediction-target covariance; near-constant predictors erase task-specific differences while architecture/activity statistics can differ. Both task competence and control intervention identity must be measured before interpreting a null delta.
Method: reproduce official shared-initialization degree-preserving comparison; log mean predictor, input-based linear/causal temporal baseline, train/validation competence, feature rank and direction sensitivity across fixed update horizons. Only validation selects a horizon; evaluate a frozen selection on disjoint speeds/offsets/contrasts. Estimate paired null effect and a predeclared horizon-by-control interaction. Preserve zero/negative/null outcomes.
Falsifier: strict-control models demonstrably learn by the published horizon with comparable out-of-domain error, or competent horizon does not change inference beyond baseline variation; then the strong topology-inference claim is not supported.
Novelty risk: general undertraining critiques are standard; Topological Sensitivity explicitly limits itself to early dynamics, so this is an extension, not a refutation of its stated endpoint. Need causal evidence that the competency/visibility regime changes a scientifically relevant visual conclusion beyond the known initialization/boundary confounds.
Contribution: an inferential validity condition and a calibrated visual mechanism experiment, if confirmed; learning longer alone is insufficient for CVPR.
Budget: published code reports ~270s/10 updates in packaged CPU results; real CUDA performance and full graph memory must be probed before allocating a longer campaign. Source-only Novix task will establish hardware and exact dependencies first.

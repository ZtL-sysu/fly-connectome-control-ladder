# Candidate E mechanism note — prospective, unreviewed

Scope: task-aligned null-control sufficiency in the official connectome-constrained visual model. No experiment run, positive result or novelty clearance is asserted. This note complements the separately owned optimizer/literature artifacts; it does not pass CCFA-startup.

## Null intervention and mechanism

Fix a trained model, all neuron/synapse parameters, its decoder, state initialization and input mapping. Default flyvis dynamics use

v[t+1] = v[t] + dt / max(tau,dt) * (−v[t] + bias + A ReLU(v[t]) + x[t]),

where A[target,source] sums effective weights sign×syn_count×syn_strength. The source-only independent sparse-operator audit verifies this form for the default PPNeuronIGRSynapses only.

Consider directed edges i→j and k→l of exactly equal effective weight w and compatible source/target cell types. Swapping their targets changes the original trajectory's current into j by w·(a_k−a_i), and into l by its negative, where a=ReLU(v). Directed in/out degrees are preserved. Equal weights also preserve weighted in/out strengths for these targets; source strengths are unchanged. Reject new self-loops and forbidden duplicate edges; keep original loops fixed. Require compatible edge sign and all fixed weight-group semantics rather than only matching raw learned strength. Verify exact realized weight equality after constructing each null.

For arbitrary paired swaps, define forcing r[t]=(A_null−A_original)ReLU(v_original[t]). If r[t]=0 at every step for a stimulus and initial state is identical, the original trajectory is exactly a trajectory of the rewired discrete dynamics, by induction. This is a simple exact statement, not a novel theorem. Approximate forcing can accumulate through recurrent dynamics; small forcing alone supplies no universal long-horizon or OOD guarantee.

Construct nulls using source-activity similarity on **unlabelled development stimuli only**, respecting the structural constraints above. Pairwise current errors can cancel or reinforce when swaps share targets, so the sum of pairwise distances is only a proposal score. Evaluate the aggregate forcing on original development trajectories and record its residual after all swaps. A rigorous error bound would require a valid stability/Lipschitz condition; empirical finite-horizon linear-response prediction must be labelled empirical if no such condition is established.

The matching conditioning is the scientific intervention: these nulls ask whether a specified functional equivalence class contains substantially different graphs. They are not samples from an unconditional degree-null distribution; no unconditional graph p-value or biological dispensability inference is permitted. Modelling source activity is side information and its acquisition/runtime count toward cost. Claims concern model function, not the causal role of an actual animal neuron.

## Strong controls and falsifiers

Compare response matching to: degree/type/sign/equal-weight constrained swaps without matching; spatial-distance matched swaps; activity magnitude-only swaps; and shuffled correspondence between source response traces and neuron identities. Match realized changed endpoint fraction, active-edge weight mass, accepted swap count, spatial-displacement distribution and weight-group composition wherever claiming a difference due to response matching. Full joint matching may be infeasible; record residual imbalances and block single-cause claims rather than hide them. Preserve edge-carried vs endpoint-derived displacement semantics explicitly.

Function matching that rewires only silent, redundant duplicate or negligible-weight edges is an uninteresting failure. Report changed active synaptic mass and forcing by cell type, not merely total edge count. A method that only recovers short-range swaps is a geometry control unless it improves over a geometry-matched baseline. Reusing development response traces on confirmation stimuli or matching the output/labels on confirmation invalidates generalization.

Potential strong discovery, conditional on literature and feasibility review: at a common nontrivial active-edge intervention dose, response-conditioned nulls preserve independent visual predictions/trajectories within a prospectively calibrated functional-resolution margin while structural/scale controls do not; forcing mismatch predicts divergence across held-out mask families, scenes and model identities, and its matching ablation removes preservation. Equal preservation by all controls, no useful dose, only development-stimulus equivalence or no independent-model transfer falsifies this route.

## Public assets and split boundary

Official 50 pretrained checkpoints/configs actually acquired and checksum verified under sources/flyvis-pretrained-access. The metadata states MultiTaskSintel training with fold1 and 19-frame dt=.02 sequences. Source validation data may have influenced checkpoint choice; do not relabel them pristine confirmation.

Labelled Sintel development imagery/flow is directly accessible and a paired sample was checked. Original Sintel TEST images are public while their flow labels are withheld. A functional-preservation experiment can evaluate original-vs-null output divergence there without ground truth. This measures preservation of the reference model's function, not optic-flow accuracy. Separately establish reference competence against zero/constant and task-matched baselines on clearly labelled development/validation data. Use scene-disjoint development and confirmation inputs and held-out model identities; no conditioning on test outputs.

Prospective split proposal, subject to review: allocate model IDs before response matching into development/calibration and untouched confirmation groups; use a per-model-matched-null arm and a cross-model transferred-mask arm, reported separately. A graph matched to one model then tested on others assesses transfer; a graph independently matched to every model assesses within-model generalization. Those estimands cannot be pooled as if identical. Predeclare all model/mask/stimulus identities before any selection.

## Calibration and budget questions still open

Use functional variation between independent competent source models and/or the source's documented sensory-noise perturbation as candidate resolution references, calculated on development inputs only; an interval selected to make nulls pass is forbidden. Such a reference is an operational model-comparison scale, not universal biological equivalence. Quantitative equivalence bounds and useful intervention dose must be fixed before confirmation. Need actual CUDA recovery/forward cost, exact decoder restoration, matching search budget and mask-level uncertainty plan.

Inference-only 19-frame workloads may be much cheaper than the 269-frame joint-training D plan; this is an estimate from shape, not a measured speedup. Keep the existing <=4GPUh prospective pilot ceiling. No extra campaign or optimizer search is implied by this note. A finite experiment queue and accepted strong-result contract remain required before research execution.

# Candidate D supplement — calibrating a null comparison with positive controls

Planned question: can a reported null comparison distinguish a known functional intervention from an exactly function-preserving transformation in the same visual network/task regime?

This avoids making the biologically real graph beat the degree-null a required discovery. A null result can remain a valid observed null after sensitivity calibration. Near-.5 MSE alone is not enough to reject a comparison. The decisive test is independent intervention visibility plus task competence on validation, followed by frozen evaluation.

Known positive control: remove only the information-bearing input (blank or independently permute stimulus across target identities, after training, preserving marginal stimulus distribution), using paired datasets. Required learned model must be sensitive to real input and exceed mean-predictor performance on held-out samples; shuffled-input predictions test sensory dependence rather than topology superiority. Selection/tuning uses validation only. Use unlabeled stimulus-identity permutations, never choose permutation by test outcomes.

Known negative control: co-permute graph states/parameters/input/output maps by an isomorphism, preserving the complete computational operator. Its outputs should match to numeric tolerance; this is an implementation sanity control, not scientific evidence of new invariance.

Experimental comparison: published 5/10-step regime versus a fixed larger maximum horizon, with checkpoints selected only by the same validation rule for every graph; same parameters/seeds/data. Check whether null-assay conclusions are stable in an informative regime. Inspect learning curves and representation probes, not loss proximity alone.

Strong scientific outcome sought: show a reproducible regime where the published-style comparison cannot detect the known positive control while a competent regime can, validate the resulting calibrated inference on independent motion conditions, then evaluate the actual degree/geometry null without requiring either a pro- or anti-connectome conclusion. A non-significant difference is not equivalence; equivalence needs a predeclared uncertainty-calibrated bound.

Novelty burden: sensitivity/positive controls are standard methodology. Strong paper value requires a counterintuitive empirical consequence on real published vision pipelines, not a checklist or simply longer training. At least two distinct visual settings and task-matched strong nonbiological baseline would be needed for a broad claim. Pilot success alone would not constitute manuscript acceptance or a ready CVPR contribution.

Potential failure: model never becomes competent within budget; input permutation is not a detectable intervention even for a strong task baseline; all regimes already show input sensitivity; held-out effect does not replicate; main result is solely a tautological gauge check. Each is an explicit stop/return condition.

# Independent CVPR 2027 Review

## Summary

This paper argues that structural statistics alone cannot establish what task information survives a graph intervention. For a fixed two-step incoming-averaging operator, it reduces the two-source input reaching two sinks to a 2x2 transfer matrix T. A nonzero source column is shown to be necessary and sufficient for perfect population accuracy on a noiseless two-subspace XOR task. The paper then examines controlled and MaleCNS interventions, including degree/module-matched graphs with zero common-relay triples but different source visibility. Additional experiments separate ideal information from finite MLP behavior, and a coefficient-noise margin is intended to bound the visibility decision.

The operator-first framing is useful and the paper is unusually careful about distinguishing structural preservation, population solvability, and finite trained behavior. The revised abstract, introduction, and discussion make those boundaries substantially clearer. However, the new coefficient-noise bound is not correct as stated. The empirical package also remains narrow, post-hoc in its central graph comparison, and only weakly connected to a significant CVPR visual-computation result. These issues keep the paper below the acceptance threshold despite its clear presentation.

## Strengths

1. **The paper asks a well-defined and useful methodological question.** Equation (2) makes the executed operator explicit, and Table 1 distinguishes genuinely different intervention counterfactuals. This is preferable to treating a motif count or protected edge set as a functional certificate.
2. **Proposition 1 is appropriately task-specific and has a clear proof.** The sink-sum argument establishes why two nonzero columns suffice for the specified noiseless XOR task, while a deleted column gives chance Bayes accuracy. The main text and Supplement Section 1 consistently disclaim generality to nonlinear propagation, arbitrary GNNs, and finite optimizers.
3. **The matched zero-common-relay example exposes a real reporting ambiguity.** Figure 1 and Table 4 show how separate-relay routes can preserve both sources while another degree/module-matched edit loses one. The paper appropriately calls the matrices post-hoc reconstructions and does not claim that common-relay count alone explains the archived accuracy gap.
4. **The controls address several alternative explanations.** The controlled calibration includes no-propagation, moved-readout, linear-readout, shuffled-label, and oracle controls. The k=8 experiments also show why finite accuracy should not be equated with ideal label information: every nonzero dose is ideally solvable even though MLP accuracy changes considerably.
5. **The revision improves the presentation.** The contributions, limitations, and provenance qualifications are visible in the main paper; the figures and tables are readable; and the eight-page body is used efficiently. Supplement Sections 2, 5, 6, and 10 document important distinctions among null generation, statistical units, normalization, and reconstructed assets.

## Major Concerns

### 1. The new coefficient-noise bound is mathematically invalid as stated

Section 3.2 and Supplement Section 11 claim that if both coefficient perturbations have norm at most sigma and

`sigma < g / sigma_min([P0 P1])`,

then a nearest-union-subspace decision retains the correct class pair. This condition does not control the correct-class distance under the perturbation.

Let `Q = [P0 P1]`. For a different-class point, `z = alpha P_ca z_a + beta P_cb z_b` satisfies

`dist(z, U0 union U1) >= ||(I - Q Q^+) z|| >= sigma_min(Q) ||[alpha z_a; beta z_b]|| >= sigma_min(Q) g`.

But after perturbation, the correct-class distance is only bounded by

`dist(z + delta, U_ca union U_cb) <= ||delta_a|| + ||delta_b|| <= 2 sigma`.

The claimed threshold does not ensure that this upper bound remains below the incorrect-union distance. More importantly, the displayed union distance is itself unbounded as `alpha z_a` or `beta z_b` grows, even for fixed g. The statement also asserts preservation for the correct class pair, including points already in U0 or U1.

A counterexample follows for any full-column-rank Q. Choose the source coefficients so that the unperturbed transferred state is `z = t Q v_min`, where `v_min` is a right singular vector associated with `sigma_min(Q)` and t is arbitrarily large. This state belongs to both class-pair subspaces, so its correct-class distance is zero. Perturbing it within the same class pair gives a correct-class distance at most `2 sigma`. Meanwhile, the component orthogonal to span(Q) has norm `t sigma_min(Q)`, and the perturbation changes that component by at most `2 sigma`. For sufficiently large t, every incorrect-union distance therefore exceeds `2 sigma` while the correct-union distance is at most `2 sigma`. The stated threshold is independent of t, so it cannot guarantee the claimed decision. This construction respects positive source gains and the unrestricted continuous source vectors used in the paper.

The supplied `visibility-margin.json` only evaluates the scalar ratio `sigma sigma_min/g` and marks it valid when below one. It does not test nearest-union decisions and therefore cannot validate the mathematical claim. The integrity audit's statement that the margin is supported confirms internal numerical consistency, not correctness of the guarantee.

This is a major soundness problem because the margin is listed as a contribution in the abstract and introduction. A valid revision needs a corrected theorem and proof, with the necessary signal/coefficient assumptions, a changed metric or restricted domain, or removal of the guarantee. Simply adding more deterministic ratio computations will not resolve it.

### 2. The central real-graph comparison is post-hoc and does not identify the causal source of the archived gap

The matched narrow comparison is compelling as a diagnostic illustration, but its strongest evidentiary chain remains indirect. Table 4 places reconstructed transfer matrices next to archived accuracies; original dose-instance hashes are unavailable. Sections 4.4 and 5 acknowledge that the two editing designs also differ in deletion order and partner choices, so the comparison cannot attribute the historical high-versus-chance gap specifically to the no-new-triple rejection rule.

The executed MLP replay in Section 4.8 helps establish that the reconstructed transfers support different learned behavior. It does not prove that the archived executions used exactly those graph instances. Consequently, the abstract's juxtaposition of 0.9745 and 0.5055 with the reconstructed source-access difference remains a consistency result, not a fully closed causal account.

A stronger study would prospectively generate and save matched interventions, compute T before training, train all readouts under controlled initializations, and test whether the transfer-based audit predicts outcomes across many graph pairs. At minimum, the paper should avoid presenting this single pair as more than a proof of the reporting ambiguity.

### 3. The empirical scope is too narrow for the breadth implied by the reporting lesson

All real connectome experiments derive from one MaleCNS animal, two related node selections sharing 195 neurons, one synthetic task family, and one fixed two-step linear propagator. The k=8 extractions are not independent biological replicates. The main proposition is exact only for the specially constructed continuous subspace XOR task.

This narrow setting can support a useful counterexample, but the current evidence does not establish when an operator audit changes scientific conclusions in practice. There is no prospective evaluation across independent connectomes, source/sink selections, propagation depths, normalization schemes, or nonlinear operators, and no measure of how often standard structural reports disagree with the audit. The work therefore demonstrates existence rather than prevalence or practical reliability.

The strongest next evidence would be a broader, pre-registered audit over independently generated interventions, reporting disagreement rates and failure cases alongside finite-model behavior. Without this, claims should remain explicitly limited to the present protocol.

### 4. The visual experiments do not yet establish a significant CVPR contribution

The CIFAR-10 experiment in Section 4.9 is a four-image identity-readout assay on frozen codes through a tiny fixed transfer operator, not a visual recognition benchmark or a connectome-constrained visual model. It shows that a source with a private transfer direction can be decoded while a collinearly mixed source cannot. That is consistent with linear algebra, but it offers limited new insight into visual representation learning or biological visual computation.

The separate reverse-support CIFAR-10 control is negative and, by the supplement's own description, uses a different recurrent model, reverse-directed edges, a small training subset, and learned nonzero weights. It does not validate the main forward operator or demonstrate a benefit on natural-image recognition. The UCI digit and visual parity results similarly function as readout diagnostics rather than independent demonstrations of a broadly useful vision method.

For CVPR significance, the paper needs either a convincing natural-image or neural-visual prediction setting where the audit changes a substantive conclusion, or a clearer positioning as a narrowly scoped methodological counterexample with appropriately modest claims. Adding CIFAR labels to the current transfer test does not by itself supply that significance.

### 5. Novelty is primarily conceptual packaging of straightforward linear algebra

Computing `R_S W^2 E_ab` is a natural way to inspect a fixed linear propagator, and the nonzero-column criterion follows directly once the XOR population task is defined. The matched graph example is useful, but the paper does not introduce a new graph-learning method, visual architecture, dataset, or general theoretical framework.

The related-work section cites intervention and null-model precedents, but the distinctive contribution over directly propagating source basis vectors or inspecting source-to-readout paths remains modest. The paper's best contribution is its disciplined reporting protocol and counterexample, not the algebraic criterion itself. This limits its top-conference novelty even if the margin theorem is corrected.

## Additional Concerns

- **Initialization and null controls:** Supplement Section 6 states that actual trained pairs were not initialized with bit-identical parameters. The paper is transparent about this, but a prospective controlled replay should fix initialization to separate graph effects from optimization variance.
- **Finite-behavior interpretation:** The large finite-accuracy differences among information-preserving k=8 doses are described mainly through transfer geometry. A quantitative predictor of those differences, beyond source gain and rank, would make the finite-readout discussion more explanatory.
- **Noise terminology:** The margin concerns coefficient perturbations in the noiseless transferred-state calculation, not noise in image features, neural activity, graph weights, or the learned readout. Even after correcting the theorem, its practical relevance needs to be established.
- **Supplement organization:** Supplement page 8 contains only a small margin table, while dense provenance and readout details appear earlier. This is not a formatting defect, but the supplement would be easier to audit if the proof, assumptions, worked example, and numerical certificate were kept together.

## Claim-Evidence Assessment

The claim that common-relay count is not necessary for source visibility is strongly supported by the matrices in Figure 1 and the exact counterexample in Supplement Section 1. The claim that nonzero columns determine ideal XOR solvability is strongly supported by Proposition 1 under its stated assumptions. The claim that nonzero k=8 doses retain ideal information while finite accuracy varies is adequately supported by the reconstructed matrices and archived results. The claim that the executed MLP separates the three narrow matrices is adequately supported by Section 4.8 and the per-seed values in Supplement Section 8. The claim that CIFAR identity follows a private direction is supported only for this particular four-image readout assay and should not be generalized. The coefficient-noise guarantee is unsupported because its stated sufficient condition is false.

## Effect of the Revision

- **Clarity:** Improved substantially. The three-level distinction among structure, population information, and finite behavior is easy to follow, and the revised scope statements are precise.
- **Soundness:** Mixed. The operator audit and Proposition 1 are clearer and more carefully bounded, but the new margin claim introduces a material mathematical error. The revision therefore does not improve overall soundness.
- **Evidence:** Improved modestly in organization and interpretability, especially through the transfer summary and explicit scope controls. The deterministic margin table is not new empirical validation, and no new learned-model training broadens the evidence base.
- **Novelty:** Essentially unchanged. The new framing clarifies the conceptual contribution, but the underlying operator calculation and task-specific criterion remain straightforward and narrow.
- **CVPR significance:** Improved slightly in communication, but not in substance. The paper now states its lesson more convincingly, yet still lacks a consequential visual-computation demonstration or broad intervention study.

## Questions for the Authors

1. Can you provide a complete proof of the margin that accounts for both the perturbed correct-class distance and the unbounded signal-dependent incorrect-class distance?
2. Can the matched intervention comparison be rerun prospectively with saved graph hashes, controlled readout initialization, and several independently generated graph pairs?
3. Across a larger intervention collection, how often do degree/module/motif reports disagree with source visibility, and when does that disagreement change downstream conclusions?
4. What substantive natural-image or neural-visual prediction problem is improved or reinterpreted by this audit beyond the present synthetic readout assays?

## Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 3 | 4 | Eq. (2), Proposition 1, Sections 2 and 5 | Useful protocol and counterexample, but limited algorithmic or theoretical novelty; a broader general framework or stronger differentiation would be needed for a higher score. |
| Soundness | 2 | 5 | Section 3.2; Supplement Sections 1 and 11 | Proposition 1 is sound, but the margin theorem has a counterexample under its stated assumptions; correcting or removing that claim is necessary. |
| Evidence | 2 | 5 | Tables 4-7; Supplement Sections 3, 5, 8-10 | Narrow, partly post-hoc evidence and limited visual validation; prospective matched reruns and broader intervention coverage are needed. |
| Significance | 2 | 4 | Sections 4.7-4.9 and 5 | Reporting lesson is useful but current CVPR relevance rests on synthetic readout diagnostics; demonstrate a consequential vision or neural-vision use case. |
| Clarity | 4 | 5 | Abstract, Figure 1, Table 1, Discussion | Clear operator-first story and candid limitations, despite a dense experimental protocol. |
| Reproducibility | 3 | 5 | Sections 4.1, 4.4; Supplement Sections 6 and 10 | Detailed recipes and archived seed data are supplied, but missing dose-instance hashes and uncontrolled historical initialization prevent full reconstruction. |
| Ethics / Limitations | 4 | 4 | Section 5; Supplement Sections 7 and 10 | Strong scope and provenance disclosure; no major human-subject or sensitive-data issue is apparent. |

**Overall:** 4 | **Scholarly Confidence:** 5

**Recommendation:** Weak reject.

The clear framing and matched counterexample are worthwhile, but the invalid noise-margin guarantee and limited, partly reconstructed evidence are decisive at a top-conference standard. Correcting the theorem would remove one major concern; establishing broader prospective evidence and a substantive CVPR-relevant application would be necessary for a materially stronger recommendation.

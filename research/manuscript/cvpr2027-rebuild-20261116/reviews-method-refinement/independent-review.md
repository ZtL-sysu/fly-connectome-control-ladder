# Independent review: revision-method-refinement

**Overall:** 6.0 | **Scholarly Confidence:** 5

## Summary judgment

This revision makes a substantive methodological improvement over the 5.5 locked draft. Task-Information Audit is now presented as an explicit three-level procedure with defined inputs, a fixed sequence of measurements, and different claims attached to each level. The new path expansion and private-residual definitions are algebraically correct within their stated linear setting, and the revised figures make the paper's central argument easier to verify. The manuscript is also more internally consistent: the introduction poses two questions, the experiments answer them in order, and the discussion returns to the same distinctions.

The improvement is in method articulation and presentation. The empirical basis is still one animal, related reconstructions, a fixed two-step linear operator, and narrow readout probes. The paper does not validate the audit across independent connectomes, propagation rules, or realistic visual tasks. I would therefore **replace the 5.5 locked draft with this version**, but only as a clearer and slightly stronger methodological paper, not as a paper whose evidence base has materially broadened.

## 1. Is the three-level framework a clear, executable methodological contribution?

Yes, with an important scope qualification.

Section 3 now gives the audit four concrete inputs: an edited graph, the executed propagation operator, task sources, and readout sites. Section 3.4 then specifies four operations: verify declared structural invariants; construct T from the actual direction, normalization, depth, and sinks; report visibility, task-specific ideal information, rank, and private components; then compare finite readouts with those information-level outputs. This is a usable protocol for the family of fixed linear propagators studied here. The three outputs are also reflected in the introduction, experiment subsection headings, and discussion, so the framework is a genuine organizing contribution rather than terminology added to a previous results section.

The qualification is generality. The audit is executable because the operator is fixed and linear. Section 3 explicitly says nonlinear message passing, gating, and spiking require input-dependent analysis. That limitation is honest, but it means the paper offers a disciplined reporting protocol for a restricted operator family, not a general task-information audit for arbitrary graph neural networks. The claimed methodological contribution should be read at that scope.

A minor consistency issue remains: the Introduction refers to “Eq. (3)” for `T = R_S W^2 E_ab`, while the compiled Method numbers the transfer as Eq. (2), the path expansion as Eq. (3), and the private residual as Eq. (5). This is easy to fix and does not affect the logic, but it is exactly the kind of cross-reference error that should not remain in a methods-centered revision.

## 2. Correctness and scope of Eq. (3) and Eq. (6)

The requested equation references appear to use the reviewer's numbering convention; in the compiled manuscript they are Eq. (3) for the path expansion and Eq. (5) for the private residual.

**Path expansion.** Eq. (3),

`T_sj = sum_r W_sr W_rj = sum_r A_rj A_sr / [max(d_r,1) max(d_s,1)]`,

is correct for a source j and sink s under incoming-neighbor normalization. The intermediate relay r is the only possible two-step bridge. The denominator associated with the first hop is the in-degree of r because `W_rj = A_rj / max(d_r,1)`; the denominator of the second hop is the in-degree of s. The equation correctly counts source-relay-sink walks outside the selected motif family. It does not, by itself, show that equal degree, module, and common-relay counts must produce unequal T; it shows why those statistics fail to determine T. The paper usually states the weaker, correct claim.

The common-relay predicate in Eq. (6) is also correct for the evaluated special case: `(r,s)` with `A_ar A_br A_rs = 1` records a relay reached from both sources and connected to sink s. Its scope remains narrow, and the manuscript explicitly notes that it omits separate-relay routes.

**Private residual.** Eq. (5),

`q_j = (I - P_span(T_-j)) t_j`, `rho_j = ||q_j||_2^2`,

is a valid squared Euclidean residual after projecting target column t_j onto the span of all other source-transfer columns. The supplement correctly gives the equivalent Moore-Penrose form and states that rho is zero both for a deleted source and for a source collinear with other columns. The reported recomputation is internally consistent: for source 109, rho is 0 on base, 0.001953125 on named-edge zero, and 0 on path zero; the named-edge source-109 residual is `(-0.03125, 0.03125)`, whose squared norm is `2(0.03125)^2 = 0.001953125`. Source 107 has zero residual on all three graphs.

The textual description “squared transfer coefficient along a readout direction orthogonal to all other transferred sources” is accurate. The paper also correctly avoids promoting rho to a decoding guarantee: a nonzero residual can support source separation, while finite nonlinear accuracy is not determined by it. The Introduction's phrase “quantify independent source access” is acceptable shorthand for this operator-level residual, especially because the same paragraph calls the assay a probe rather than a recognition benchmark.

One limitation deserves sharper emphasis. With four concurrent sources, a private transfer direction is sufficient for linear separability of that source's contribution under known mixing, but a zero residual does not make the source unrecoverable when the other source codes are independent and class information can be separated statistically. Thus the source-109 result is evidence about this readout and these mixtures, not a general necessity result. The supplement states this; the main text largely does as well, but the phrase “explains source-specific readout behavior” in the abstract is somewhat stronger than the single configuration demonstrated.

## 3. Faithfulness and narrative value of Figures 1, 3, and 4

**Figure 1** is faithful and is the strongest presentation improvement. The plotted routes and matrices match `narrowk4_transfer_report.json`: named-edge zero has `16T = [[1,0],[1,1]]`, and path zero has `16T = [[1,0],[1,0]]`. The archived accuracies 0.9745 and 0.5055 are clearly marked as archived fits, while the matrices are marked as post-hoc reconstructions. The shared banner makes the structural certificate visually explicit. This figure now directly performs the first argumentative step instead of following it as decoration.

**Figure 3** is faithful to `multigraph.json` and `independent-transfer-checks.json`. The dose and null accuracies, bootstrap intervals, and the ideal-Bayes row (`1/2` only for zero-dose graphs with a missing source) match the archived records. The annotation “ideal information does not [change]” is limited by caption text to the dose graphs; null curves remain visible and are not assigned idealized labels. This distinction is important and is handled correctly. The figure makes the information-versus-utilization point clearer than in the locked draft.

**Figure 4** is faithful to `cifar-identity-readout.json`, with source 109 at 0.164/0.566/0.096 and source 107 at 0.281/0.441/0.440. The residual diagram illustrates the projection definition, and the right panel makes the preserved-source counterexample visible. The left diagram is schematic: the projection direction is drawn in a way that could be mistaken for a literal sink-coordinate geometry, whereas rho is computed in the four-dimensional sink-feature space. The caption and equation resolve this for a careful reader, but a label such as “schematic in transfer-feature space” would improve fidelity.

All three figures improve the narrative. They turn the paper from a sequence of accuracy tables into a staged argument: equal structural certificate, separated information and finite use, then multi-source geometry. None of the figure-generation code computes new accuracies; it reads archived records, which is consistent with the stated evidence provenance.

## 4. Narrative consistency across sections

The main line is now consistent:

- Introduction opens with the matched counterexample, defines the evaluation problem, and states two sequential questions.
- Method defines the operator, path accounting, three information-level quantities, structural constraints, and a four-step audit procedure.
- Experiments are renamed around the two questions, followed by null-counterfactual and transfer-geometry sections.
- Discussion restates the protocol contribution and its validity boundary; the conclusion asks authors to attach each claim to the correct level.

This is a real improvement. The two-question structure gives the experiments a purpose that the earlier dose-by-dose presentation lacked. The three-level vocabulary is used consistently, and the discussion no longer reads like a separate list of caveats.

There are localized inconsistencies. The equation-number error in the Introduction is one. The abstract's “explains” is stronger than the qualified main-text claim. The paper also removes the earlier explicit comparison table of counterfactuals from the main method; the nulls are described in prose, which is acceptable but makes the audit procedure less immediately checkable than in the locked draft. Finally, the section titled “Question 2: does information preservation predict finite use?” ends by showing that it does not predict the magnitude of finite accuracy. That is a legitimate negative answer, but the heading could be phrased more neutrally.

## 5. Comparison with the 5.5 locked draft

| Dimension | Locked draft | This revision | Change |
|:---|:---:|:---:|:---|
| Novelty | 3 | 3 | The method is better articulated, but the underlying algebra and counterexample are unchanged. |
| Soundness | 3 | 4 | The path and residual formulas are correct and bounded; the lower score reflected the now-removed noise-bound concern and a less explicit scope. |
| Evidence | 2 | 2 | No new experiment, animal, operator family, or prospective intervention was added; provenance limits remain. |
| Significance | 2 | 2 | The CVPR-facing visual assays remain narrow readout probes rather than a consequential vision result. |
| Clarity | 4 | 5 | Figures and the two-question, three-level narrative substantially improve reviewability. |

**Overall:** 6.0, up from 5.5. The increase comes from soundness and clarity. It is not enough to overcome the weak evidence and significance scores. Confidence remains 5 because the main paper, supplement, figure-generation script, and archived records provide a complete and inspectable evidence package; low confidence should not be used to express narrow evidence breadth.

## Recommendation

**Replace the locked draft with revision-method-refinement.** It is the better submission: easier to understand, more defensible technically, and more faithful in visualizing what the evidence supports. The replacement should be treated as a methodological framing improvement. If the choice is between this paper and another with equally clear presentation but broader evidence, the evidence-limited contribution here should still rank lower.

## Remaining concerns

1. Validate the three-level audit across independently sampled graphs and propagation operators, not only one male connectome and one fixed operator.
2. State the scope of rho and “private direction” more cautiously in the abstract: it is a linear operator residual, not a necessity condition for decoding or biological computation.
3. Correct the Introduction's equation reference and add a cross-reference to the compiled Eq. (5) where the private residual is first described.
4. Report prospective, saved intervention instances with matched initializations if the historical source-access gap is to be causal rather than consistency evidence.
5. Add one consequential visual or neural prediction setting where applying the audit changes a substantive conclusion; the current CIFAR assay demonstrates geometry but limited CVPR significance.

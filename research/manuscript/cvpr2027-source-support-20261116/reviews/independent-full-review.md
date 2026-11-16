# Independent full review

## 1. Report Metadata

```text
Review date: 2026-11-16
Target venue/year/track: CVPR 2027 main conference
Paper title: A Degree Match Does Not Keep Both Inputs
Input materials reviewed: main.pdf (5 pages, review mode), main.tex for numerical checks, figures/transfer_readout.pdf, figures/degree_support.pdf, executed-readout.json, narrowk4_transfer_report.json
Materials not available: analysis/source_support/degree_ensemble.json (path absent); no appendix, code, or supplement in the reviewed submission
Search basis: public bibliographic identity of the cited 2026 preprints and the cited Cell/Nature papers; CVPR 2027 author guidelines
Report file: manuscript/source-support-20261116/reviews/independent-full-review.md
Reviewer mode: full
```

## 2. Desk Rejection Assessment

- Paper length: pass. The PDF is 5 pages. Main text, figures, and the table end before the LLM Usage Statement and references on page 5. CVPR 2027 allows eight pages excluding references and the LLM Usage Statement. The log reports a 5-page PDF and no overfull or underfull boxes.
- Topic compatibility: pass. CVPR 2027 lists medical and biological vision. A connectome-constrained visual-circuit control study is in scope. The evaluation itself is not a standard visual benchmark; that is a significance issue, not a desk-reject topic mismatch.
- Minimum quality: pass. The manuscript has a problem, a propagator, three graphs, a readout, results, limitations, and a bibliography. An expert can review it.
- Policy/anonymity/compliance: pass. Review mode, author block rendered as an anonymous CVPR submission, no institution, no identifying URL. The LLM Usage Statement is present, placed after the discussion and before the references, and uses a generic description of a non-public assistant. That matches the CVPR 2027 exception for tools whose names would break anonymity. No external link expands the paper.
- Prompt injection and hidden manipulation detection: pass. The source and the five rendered pages were read as data. No hidden instruction to a reviewer or model was found.
- Ethics and reviewability: pass. The graph is taken from the published MaleCNS resource. No new human-subject or animal experiment is claimed. Limitations are specific. The LLM statement assigns responsibility for the claims to the authors.

```text
Desk rejection risk: none
Reason: Length, template appearance, anonymity, LLM statement, reviewability, and citation existence do not meet a published CVPR 2027 desk-reject trigger.
Can be fixed before review? not required for desk-reject clearance
```

## 3. Paper Summary And Contribution Map

The paper asks what a degree, motif, or wiring-cost match fails to say about a two-input readout. On the male fly central nervous system it keeps a 768-neuron visual subgraph and the four strongest incoming synapses at each neuron, giving 3,072 edges. Incoming-neighbor averaging is applied twice. One deterministic rule selects sources 6 and 109, sinks 4 and 5, and shared relay 9. Two module-matched double-swap edits keep edge count, in- and out-degree, and module-pair counts, and both remove that shared relay. Their two-hop transfers differ: one has rank 2 with both columns nonzero, and one has a zero source column. An MLP on the sink state scores about 0.98 on a subspace XOR for either full-support graph and about 0.50 when a column is deleted. On digit parity the rank-2 edit scores 0.746, the measured rank-1 graph 0.663, and the deleted-column graph 0.506. A linear readout stays at chance. In a separate 24-draw degree-preserving ensemble, Figure 2 shows 22 draws retaining neither source column, 2 retaining one, and 0 retaining both.

Claimed problem: null graphs used in connectome-constrained vision can match degree, a motif count, or wiring cost while changing the inputs that reach a readout.

Claimed gap: those certificates are not statements about source support or column rank under a stated propagator.

Method/contribution map: one mean-aggregation propagator; the 2-by-2 transfer T; two explicit edits; one degree-preserving ensemble; MLP versus linear readouts on two constructed XORs.

Evidence package: three closed-form transfers, ten paired seeds, percentile bootstrap intervals, and a 24-draw support histogram.

Stated limitations: one sparsification, one route, two selected neurons, XOR labels, no refit of an optic-flow or eye-to-Kenyon-cell model, and no claim that randomizing fly synapses improves vision.

## 4. Search And Related-Work Basis

```text
Queries used:
CVPR 2027 author guidelines page limit and LLM Usage Statement
Berg, Sexual dimorphism, Drosophila male central nervous system connectome, Cell 2026
Lappalainen, Connectome-constrained networks, Nature 2024
Dorkenwald, Neuronal wiring diagram of an adult brain, Nature 2024
arXiv:2604.04033; arXiv:2609.39248; arXiv:2610.10023; arXiv:2611.14508
degree-preserving rewiring and fly visual connectome nulls
Sources searched: CVPR 2027 author guidelines; arXiv abs/html pages; Nature, Cell, and PubMed records
Closest works found: Dhiman arXiv:2604.04033 (5 Apr 2026); Park arXiv:2609.39248 (30 Sep 2026); Correig-Fraga, Guimera, and Sales-Pardo arXiv:2610.10023 (7 Oct 2026); Liu arXiv:2611.14508 (10 Nov 2026); Lappalainen et al., Nature 634:1132-1140 (2024); Dorkenwald et al., Nature 634:124-138 (2024); Berg et al., Cell 189(18):5504-5526.e15 (2026), doi:10.1016/j.cell.2026.08.015
Unverified related-work risks: no uncited paper was found that already runs this two-hop column-rank MLP audit. Classical configuration models are represented by the cited Maslov and Sneppen paper. A broader motif-null literature exists; no closer fly-vision instance than the cited 2026 preprints was identified in this search.
Source-quality screening status: screened. Identity checks used arXiv, Nature, Cell, and the CVPR guidelines. No MDPI source was used.
```

Citation-context check, from public abstracts rather than from private project history:

- Dhiman reports that shared initialization removes an early-loss gap and a degree-preserving null removes an activity gap in a flyvis-style comparison. The manuscript's summary matches that abstract, and Section 5 correctly says the operator there is a masked product, not incoming-neighbor averaging.
- Park reports that column shuffles and degree-preserving swaps create one-step olfactory-to-descending shortcuts the fly graph lacks, and that those shortcuts change an evolutionary comparison. The manuscript's "different sign" discussion matches that abstract. Park's preprint date, 30 Sep 2026, is on or after the CVPR 2027 contemporaneous-work cutoff of 15 Sep 2026. Overlap with Park is not, by itself, a reason to reject. The manuscript cites and discusses it. It does not empirically compare against Park's agents.
- Correig-Fraga and colleagues describe an eye-to-connectome-to-Kenyon-cell model and a wiring-cost comparison. The manuscript's summary matches.
- Liu separates physiology tuned on the real wiring from physiology retuned on each null, with a mushroom-body reversal and a flyvis ranking that depends on the protocol. The manuscript's examples match the paper's abstract.
- Lappalainen et al. and Dorkenwald et al. match the cited titles, author leads, journal, volume, and pages. Berg et al. matches the cited title, year, volume, issue, pages, and DOI.

## 5. Expected Review Outcome

```text
Venue: CVPR 2027 main conference
Venue family: computer vision
Primary scoring dimensions: novelty, technical quality, empirical validation, visual evidence, clarity, fair comparison
Evidence package expected: a visual task or neural-prediction endpoint, recent baselines, ablations, and a control that preserves the quantity being tested
Likely reviewer taste: clean negative controls are valued, but a single synthetic pair will be read as a note
Likely AC concern: the certificate is demonstrated on one route and two constructed XORs, so it does not yet change a vision result
Biggest mismatch risk: "visual readout" names a frozen digit-parity XOR on two neurons
Writing moves that improve fit: lead with the reporting requirement and the scope limits; keep the visual-anatomy claim separate from a vision-benchmark claim

Expected outcome: weak reject
Main accept signal: on this route the executed MLP follows source-column support and, for digit parity, column rank, while degree and module-pair matches do not separate the two edits
Main reject signal: the evidence is one 768-node sparsification, one source-sink pair, three graphs, and two constructed XORs; it does not establish the certificate for connectome-constrained vision
Confidence: 4/5
```

## 6. Strengths And Weaknesses

Strengths:

- The local object is defined tightly. Equations (1) and (2) make T a two-hop mean-aggregation transfer, and the three matrices in Section 3.3 match `narrowk4_transfer_report.json` entrywise.
- The paper reports the comparison that does not move. On the subspace XOR, separate-routes minus measured is +0.003 with interval crossing zero and only six of ten seeds positive. That is the right reading of a ceiling effect.
- Digit parity separates rank from support: separate-routes 0.746 beats measured 0.663 by +0.083 on ten of ten seeds, and both beat the deleted column. The linear control stays at chance on an XOR, as it should.
- Section 4.3 and Section 5 refuse the broad reading. Removing one relay on one edit is not a claim that randomizing fly vision helps, and the result is not claimed to overturn flyvis or Kenyon-cell papers.
- Figure 2 agrees with the text: 22 draws keep neither source, 2 keep one, and 0 keep both.

Weakness:

```text
Weakness: The certificate is shown for one route and three graphs. The degree-preserving ensemble does not test degree-matched graphs that still carry both inputs.
Evidence basis: Sections 3.1, 3.4, 4.2, and 5. Sources, sinks, and the relay are nodes 6, 109, 4, 5, and 9. The support-preserving comparison is one separate-routes edit against one deleted-source edit. Figure 2 is a 24-draw histogram after 10 x 3,072 swaps with no protected edges.
Reviewer deduction: Seed intervals do not capture route selection or graph sampling. A well-mixed degree-preserving swap is expected to cut a specific two-hop route; 0/24 shows that this null is a bad control here, which the paper says, but it does not show that degree is insufficient among graphs that still carry both sources.
Required fix: Pre-declare more routes. Add a degree-matched ensemble constrained to keep both columns, and report MLP accuracy on that ensemble. One published visual endpoint, run under the same propagator, would be the result that could change the venue decision.
```

Weakness:

```text
Weakness: The tasks are constructed probes, not visual computations a CVPR reader can use.
Evidence basis: Section 3.5. The subspace task draws coordinates in frozen 8-d subspaces. Digit parity applies one frozen QR projection to halves of scikit-learn digits and labels the XOR of the two parities. Section 5 says a retinal population code was not tested.
Reviewer deduction: The MLP gap is real for these labels. It is not evidence about optic flow, natural images, or a Kenyon-cell readout.
Required fix: Either retitle the claim as a two-bit probe, or add one task whose inputs and outputs are the ones used in the cited visual models.
```

Weakness:

```text
Weakness: Abstract and Table 1 round the deleted-source digit result to 0.507. Section 4.1 and the readout file give 0.506.
Evidence basis: executed-readout.json path_zero visual_parity_xor MLP mean is 0.506494140625, which rounds to 0.506. Table 1 prints 0.507. The abstract pairs 0.504 and 0.507.
Reviewer deduction: The gap is 0.001 and does not change the ordering. It is still an internal numeric mismatch.
Required fix: Print 0.506 in the abstract and in Table 1.
```

## 7. Potentially Missing Related Work

```text
Work: Dhiman, arXiv:2604.04033 (2026)
Status: searched
Why relevant: degree-preserving nulls can remove an apparent topology effect in a flyvis-style model
Overlap: the null-model moral overlaps; the operator and endpoints do not
Needed comparison: already cited and distinguished in Sections 2 and 5; no further comparison is required for identity
```

```text
Work: Park, arXiv:2609.39248 (2026)
Status: searched
Why relevant: degree-preserving swaps change the paths a task can use, and path statistics belong next to degree statistics
Overlap: same principle, different circuit and sign. Contemporaneous under the 15 Sep 2026 cutoff
Needed comparison: the discussion is sufficient for a contemporaneous preprint. An empirical comparison is not reasonably required unless this paper claims to overturn that evolutionary result. It does not.
```

```text
Work: Liu, arXiv:2611.14508 (2026); Correig-Fraga et al., arXiv:2610.10023 (2026)
Status: searched
Why relevant: physiology-protocol flips and wiring-cost matches are the other controls named in the introduction
Overlap: cited at the correct level of operator difference
Needed comparison: none beyond the existing discussion, because this paper holds the propagator fixed
```

```text
Work: configuration-model and motif-null literature beyond Maslov and Sneppen (2002) and Milo et al. (2002)
Status: searched
Why relevant: degree-preserving swaps are not expected to preserve a named two-hop path
Overlap: the 0/24 result is the expected direction
Needed comparison: not a specific uncited paper. The manuscript should not present 0/24 as surprising path destruction. It already treats it as a failed control. No invented missing citation is asserted.
```

## 8. Claim-Evidence Audit

| Claim | Where stated | Evidence provided | Strength | Reviewer deduction | Required fix |
| --- | --- | --- | --- | --- | --- |
| Two edits match edge count, both degree sequences, and module-pair counts, and their transfers differ | Abstract; Section 3.3; Table 1 | Transfer report: both edits have 3,072 edges, degree and module matches true for the deleted-source edit, both transfers match the printed matrices, common-relay set empty | strong for these two edits | None for this instance | None |
| Separate-routes MLP scores 0.979 and 0.746; deleted-source scores 0.504 and 0.507 | Abstract; Table 1 | Readout means 0.978955, 0.745850, 0.503760, 0.506494 | adequate except the last digit | 0.506494 rounds to 0.506, not 0.507. Section 4.1 already says 0.506 | Use 0.506 |
| Measured graph scores 0.976 on subspace XOR and 0.663 on digit parity, below the relay-removing edit | Abstract; Section 4.1 | Means 0.976367 and 0.662598. Paired digit gap +0.083252, 10/10 seeds, bootstrap about [0.072, 0.094] | strong for this route and this MLP | The relay is not removed in isolation; four swaps also add other edges | Keep the existential wording, and do not generalize past this edit |
| Both columns nonzero are enough for the subspace XOR; rank matters for digit parity | Section 4.1 | Subspace paired gap +0.003, interval crosses 0, 6/10 positive. Digit ordering is separate, measured, deleted | strong inside these two tasks | The subspace features are redrawn per seed; digit halves share one QR map. The split may be a property of that feature geometry | State that dependence in the task section, not only by the scores |
| A zero column forces Bayes accuracy 1/2 on a balanced XOR | Section 3.2 | Deleted-source MLP means 0.504 and 0.506; linear means near 0.50 | strong | None | None |
| Linear intervals on both tasks and all three graphs lie between 0.493 and 0.516 | Section 4.1 | Bootstrap means of the six linear conditions fall in that band at the printed precision. Raw seeds do not; the lowest linear seed is 0.4727 | adequate if read as intervals of the mean | The sentence is easy to misread as a bound on every seed | Say "intervals of the ten-seed means" |
| 24 degree-preserving rewires retain both sources in none of the draws | Abstract; Section 4.2; Figure 2 | Figure 2 prints 22, 2, and 0. No `degree_ensemble.json` was available to recompute swaps or module histograms | adequate as a figure-text match; weak as an independent audit | Module-histogram mismatch and exact degree matches are asserted in prose and are not in the supplied JSON | Release the 24-draw support table and the degree and module checks |
| The degree-preserving null is not capable of carrying both inputs | Section 5 | 0/24 at 10 swaps per edge on this subgraph | adequate for this sample | 0/24 is not an impossibility proof. With no protected edges, cutting one short route is the expected direction | Keep the existing qualifier "at this mixing length," and add a support-preserving ensemble |
| Removing the shared relay can improve a two-input visual readout | Section 1, lines 69-72 of the PDF | One digit-parity comparison, +0.083 | weak as a visual claim; adequate as one edit | "Visual readout" refers to digit parity on two neurons | Replace with the task name |
| A degree match should be reported with source support of the propagator that was run | Section 5 | Supported by the three-graph split and by Figure 2 | adequate as a reporting recommendation for this propagator | Not shown for masked weights, learned gains, or a population readout | Leave it as a requirement for this averaging rule |

## 9. Experiment / Benchmark / Reproducibility Audit

Baselines: the measured graph, one separate-routes edit, one deleted-source edit, a linear readout, and 24 degree-preserving rewires. There is no flyvis, no wiring-cost ensemble, and no learned-gain model. The paper does not claim those baselines.

Ablations: column deletion versus column rank is isolated by the three transfers. The shared relay is not ablated while holding all other two-hop routes fixed. Sum aggregation and symmetric normalization are discussed and not run.

Datasets/benchmarks: MaleCNS visual subgraph, top 768 neurons by total degree, in-degree truncated to 4. Tasks are a subspace XOR and scikit-learn digit parity. Neither is a vision benchmark.

Metrics: accuracy on 2,048 fresh samples; percentile bootstrap over ten seeds; paired-by-seed differences. The intervals I recomputed from the readout file agree with the printed intervals within bootstrap Monte Carlo error. They are not intervals over routes or graphs.

Statistical rigor: ten seeds are enough for the large gaps (about +0.48, +0.24, +0.16, and +0.08). They are not enough to make the +0.003 subspace gap a difference, and the paper does not claim one. Graph-level n is 1.

Robustness/failure cases: the subspace task is the case where rank does not matter, and it is reported. No second route, sparsification, or propagator is reported.

Implementation details: Adam learning rate 0.006, 120 epochs, 32 batches of size 128, BCE-with-logits, seeds listed, PyTorch 2.13 on Apple MPS. The transfer substitution is justified by a stated max deviation of 3e-8; that deviation is not in the supplied JSON files.

Artifacts and reproducibility: given T, the MLP protocol can be rerun. The visual-neuron string rule, node order, synapse ranking, and body IDs are not in the PDF. The transfer report records body IDs 10019, 10854, 10027, 10015, and 10016, and it marks itself as a rebuild rather than the original execution asset. Numerical agreement was checked; the graph was not rebuilt in this review. `degree_ensemble.json` was not present.

Limitations: Section 5 is specific and matched to the experiments. The missing sentence is a data-availability line for the public MaleCNS release. That omission does not change the score.

## 10. Multi-Reviewer Panel

```text
Reviewer: Best-justified reviewer
Expertise: connectome-constrained models
Likely score: 5
Confidence: 4
Main positive signal: The three transfers, the MLP ordering, and the 0/24 histogram tell one consistent story, and the discussion does not overclaim it.
Main negative signal: A CVPR reader still cannot tell whether the certificate matters for any visual function the community measures.
Evidence basis: Table 1, Section 4.1, Figure 2, Section 5.
Fatal concern if any: none
Score-change condition: A both-columns-preserving degree-matched ensemble that preserves the digit-parity ordering would move this reviewer to 6.
```

```text
Reviewer: Critical reviewer
Expertise: empirical computer vision
Likely score: 3
Confidence: 4
Main positive signal: The deleted-column Bayes argument is correct, and the numbers match it.
Main negative signal: One hand-built four-swap edit and a mixing process that is expected to delete a short path do not make a conference result.
Evidence basis: Sections 3.1 and 3.4; 10 x 3,072 unprotected swaps.
Fatal concern if any: none on correctness; fatal only if the paper is read as a general vision claim. The discussion blocks that reading.
Score-change condition: This reviewer stays at 3 unless a recognized visual endpoint moves with the certificate.
```

```text
Reviewer: Method / soundness reviewer
Expertise: graph propagation and readouts
Likely score: 4
Confidence: 4
Main positive signal: W is row-normalized incoming averaging, T is exactly the two-hop map, rank and a zero column are the right distinctions, and a linear map of an XOR should be at chance.
Main negative signal: The separate-routes edit changes four edges, not only the shared relay. The improvement is real for that edit and is not an isolated causal effect of relay deletion.
Evidence basis: Equations (1)-(2); replacement routes in the transfer report; Section 4.3.
Fatal concern if any: none
Score-change condition: An edit that changes rank while preserving both columns and the rest of the two-hop support would remove the residual causal gap.
```

```text
Reviewer: Evidence / experiment reviewer
Expertise: experimental design
Likely score: 3
Confidence: 4
Main positive signal: Seed-paired intervals are computed on the right unit, and the non-effect is reported.
Main negative signal: The decisive missing control is the one Section 4.2 names and does not run: degree-matched graphs that still carry both inputs, in more than one draw.
Evidence basis: Section 4.2, final paragraph; only two module-matched edits.
Fatal concern if any: none for the three printed graphs
Score-change condition: That ensemble, with the same MLP, is worth about one point if the ordering survives.
```

```text
Reviewer: Novelty / positioning reviewer
Expertise: null models for connectomes
Likely score: 4
Confidence: 4
Main positive signal: The operator is not Dhiman's mask, Liu's physiology sweep, or Correig-Fraga's learned gains, and the manuscript says so.
Main negative signal: Park already argues that degree statistics travel with a change in usable routes. This paper is a two-hop, mean-aggregation instance with the opposite sign. The rank split on digit parity is the part that is not in Park's abstract.
Evidence basis: public abstracts of arXiv:2604.04033, arXiv:2609.39248, and arXiv:2611.14508; Sections 2 and 5.
Fatal concern if any: none. Park is contemporaneous and is cited.
Score-change condition: Novelty stays incremental unless the certificate reverses a published visual comparison.
```

```text
Reviewer: Writing / clarity reviewer
Expertise: reviewer readability
Likely score: 5
Confidence: 5
Main positive signal: Section 4 is organized as claim, number, and limit. A reader can recover the contribution in one pass.
Main negative signal: The abstract spends its numbers before the tasks are defined, and "visual readout" in the introduction is broader than digit parity.
Evidence basis: abstract; PDF lines 69-72; Section 3.5.
Fatal concern if any: none
Score-change condition: Rewording does not by itself move the paper across the decision.
```

```text
Reviewer: Ethics / reproducibility reviewer
Expertise: artifacts and responsible research
Likely score: 4
Confidence: 4
Main positive signal: Limitations and the LLM statement are concrete. The cited 2026 preprints and the Cell/Nature papers exist and are used in a context their abstracts support.
Main negative signal: The submission PDF does not contain the graph files, body IDs, or the 24-draw table. Figure 2 cannot be recomputed from the supplied ensemble file because that file is absent.
Evidence basis: Section 3.1; LLM Usage Statement; missing degree_ensemble.json.
Fatal concern if any: none
Score-change condition: An anonymous supplement with the graph, the five body IDs, and the 24 support rows would move reproducibility from 3 to 4. It would not by itself move the overall score by a full point.
```

```text
Reviewer: Domain application reviewer
Expertise: fly visual circuits
Likely score: 3
Confidence: 4
Main positive signal: The subgraph rule is tied to MaleCNS visual annotations, and the paper does not pretend the route is a named motion pathway.
Main negative signal: Two-hop mean aggregation on four synapses per neuron, read by an MLP on an XOR of two neurons, is not how optic-lobe computation is tested.
Evidence basis: Sections 3.1 and 3.5; the explicit non-claim in Section 5.
Fatal concern if any: none
Score-change condition: A readout on a published motion or Kenyon-cell endpoint, under this same propagator, is the domain test that would change the score.
```

```text
Reviewer: Evidence/ablation reviewer
Expertise: ablation design
Likely score: 3
Confidence: 4
Main positive signal: Support versus rank versus linearity are separated by the reported conditions.
Main negative signal: There is no sweep of sparsification, hop count, swap budget, or number of routes.
Evidence basis: one k=4 graph, two hops, one mixing length, one route.
Fatal concern if any: none
Score-change condition: Two more routes with the same pre-declared rule, plus the support-preserving null, would move experimental rigor from 3 to 4.
```

```text
Reviewer: Reproducibility reviewer
Expertise: independent rerun
Likely score: 3
Confidence: 4
Main positive signal: Optimizer, width, seeds, batch size, and epoch count are stated. The printed T matrices match the transfer report.
Main negative signal: Node order and the visual-string filter are not sufficient to rebuild the 768-node graph without the annotation file and ranking code. The ensemble was not rerun.
Evidence basis: Section 3.5; transfer-report provenance flag `not_original_execution_asset`.
Fatal concern if any: none
Score-change condition: Supplement as stated above.
```

```text
Reviewer: Novice advocate reviewer
Expertise: first-pass readability
Likely score: 4
Confidence: 5
Main positive signal: Figure 1 puts the three matrices next to the bars, and the chance line is marked.
Main negative signal: The heatmap axis text collides as "source asource b," and Table 1 uses "Mod." and "Subsp." without the words a new reader needs. The abstract is a list of numbers.
Evidence basis: figures/transfer_readout.pdf; Table 1; abstract.
Fatal concern if any: none
Score-change condition: Figure and abstract edits are local.
```

```text
Reviewer: AC / meta-reviewer
Expertise: CVPR decision
Likely score: 4
Confidence: 4
Main positive signal: The narrow claim matches the narrow evidence, including the places where the measured graph is not best.
Main negative signal: CVPR main should not accept a reporting requirement whose only behavioral support is one constructed pair.
Evidence basis: whole manuscript against the two JSON artifacts and both figures.
Fatal concern if any: none
Score-change condition: Raise to 5 if the support-preserving ensemble confirms the gap on more than one route. Raise to 6 or 7 only if a cited visual model changes its conclusion under the same certificate. Lower to 3 if the route was chosen after seeing the accuracies, or if further routes reverse the ordering.
```

```text
Agreement: The printed three-graph arithmetic is right. The deleted column is at chance. The measured graph is not uniformly best. The standard degree null drops source support in this 24-draw figure.
Disagreement: The best-justified reviewer treats the scoped caveat as a borderline note. The critical and domain reviewers treat one synthetic pair as below the venue, at 3.
Decisive positive axis: Claim-evidence match for this propagator, this route, and these two XORs.
Decisive negative axis: No result shows that source-column support orders a visual computation outside this pair, or that degree fails among graphs that still carry both inputs.
Unresolved evidence: How many relays satisfied the selection rule; the raw 24-draw degree and module checks; behavior under another propagator.
AC stance: weak reject. Do not average the panel up to a borderline accept. The unresolved scope concern is the decision.
```

## 11. Concerns Table

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | major | One route and three graphs carry the certificate | Sections 3.1, 3.3, 4.1, and 5 | Evidence, Significance | experiment | Add pre-declared routes and a both-columns-preserving degree-matched ensemble with the same MLP | ccf-experiment-designer | If the ordering survives, overall 4 to 5 |
| C2 | major | The tasks are not visual benchmarks | Section 3.5; introduction lines 69-72 | Significance, Originality | experiment | Run one published optic-flow or Kenyon-cell endpoint under Equation (1), or narrow every visual claim to the two XOR probes | ccf-experiment-designer | A changed published endpoint could move overall 4 to 6; wording alone does not |
| C3 | moderate | The 0/24 null is expected to cut a short unprotected path and is not the degree-matched control that keeps both inputs | Sections 3.4 and 4.2; Figure 2 | Evidence, Soundness | experiment | Report the support-preserving ensemble and the swap budget sensitivity | ccf-experiment-designer | Included in C1; not an extra point by itself |
| C4 | moderate | Novelty is a two-hop instance of a point already made for sensory-motor paths | Park abstract; Sections 2 and 5 | Originality | related-work | Keep the operator distinction. Do not sell the principle as new relative to Park | ccf-paper-writer | Contemporaneous overlap alone should not lower the score; a reversed published comparison would raise Originality from 3 to 4 |
| C5 | minor | Abstract and Table 1 say 0.507; the readout mean and Section 4.1 say 0.506 | executed-readout.json; Table 1; Section 4.1 | Evidence | writing | Replace 0.507 with 0.506 | ccf-paper-writer | No overall change |
| C6 | minor | Heatmap labels collide, and "motif" sometimes means a module-pair histogram and sometimes the shared relay | Figure 1; Section 4.3 versus Table 1 | Clarity | writing | Separate the axis labels. Use "shared-relay count" and "module-pair histogram" as different names | ccf-paper-writer | Clarity 4 to 5; no overall change |
| C7 | minor | Graph construction and the 24-draw checks are not rerunnable from the PDF | Section 3.1; absent degree_ensemble.json | Reproducibility | reproducibility | Anonymous supplement with filter, body IDs, graph, and 24 support rows | ccf-paper-writer | Reproducibility 3 to 4; overall at most +0.5 |

## 12. AC / Meta-Review

Reviewer consensus: nobody found a broken transfer, a nonexistent cited paper among the ones checked, or a hidden instruction. The large MLP gaps match the readout file.

Reviewer disagreement: scores span 3 to 5. The disagreement is whether a correct, tightly scoped caveat clears CVPR main. It is not a disagreement about the printed arithmetic.

Decisive acceptance axis: for this averaging rule and this route, column support and column rank order the executed MLP, and the degree match does not.

Decisive rejection axis: that demonstration is one pair of neurons and two synthetic labels. The paper says it does not overturn a flyvis or Kenyon-cell result. The venue decision follows that limit.

AC stance: weak reject, overall 4. The paper is reviewable and locally sound. It is not yet a vision result.

Discussion risks: a reviewer may quote the introduction's "visual readout" and ignore Section 5, or may treat Park as prior art rather than contemporaneous work. The AC should keep both distinctions. Another risk is treating 0/24 as evidence that no degree-matched graph can carry both inputs. The manuscript already warns against that reading.

## 13. Quantitative Scores

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
| --- | ---: | ---: | --- | --- |
| Novelty | 3 | 4 | Sections 2 and 5; Park and Dhiman abstracts | Incremental two-hop instance. A reversed published visual comparison would move this to 4. |
| Soundness | 4 | 4 | Equations (1)-(2); Section 3.2; transfer report | Local math holds. The relay effect is one four-swap edit. An isolated rank edit would move this to 5. |
| Evidence | 3 | 4 | Sections 4.1-4.2; executed-readout.json; Figure 2 | Three graphs and one route. The C1 ensemble would move this to 4 and overall by about +1. |
| Significance | 2 | 4 | Section 3.5; Section 5 non-claim | No visual benchmark moves. A published endpoint that moves would raise this to 3 or 4 and overall by +1 to +2. |
| Clarity | 4 | 5 | Abstract; Sections 4 and 5; Figure 1 | Recoverable in one pass. Abstract density and "visual readout" keep it from 5. Wording does not move the decision. |
| Reproducibility | 3 | 4 | Section 3.5; missing ensemble file; rebuild flag in the transfer report | MLP protocol is complete. The graph and 24 draws are not. A supplement moves this to 4, not the decision by a full point. |
| Ethics / Limitations | 4 | 4 | Section 5; LLM Usage Statement; citation identity checks | Limitations match the experiments. A data-availability sentence for MaleCNS is the remaining item. No overall movement. |

```text
Dimension: Novelty
Score: 3
Confidence: 4
Evidence basis: The principle that a degree null can change usable routes is already in Park, which is cited and contemporaneous. Dhiman, also cited, already removes a topology effect with a degree null under a different operator.
Deduction: The new piece is the rank-versus-support split under mean aggregation on one route, not a new null-model principle.
Repair condition: Show the certificate changing a published visual comparison.
Expected score movement: Originality 3 to 4; overall +0.5 to +1 only together with C2.
```

```text
Dimension: Evidence
Score: 3
Confidence: 4
Evidence basis: Ten-seed intervals match the readout file. The route and the support-preserving control do not have a sample size above one edit.
Deduction: Seed bootstrap is not graph bootstrap.
Repair condition: Pre-declared additional routes and a both-columns-preserving degree ensemble.
Expected score movement: Evidence 3 to 4; overall +1 if the ordering survives.
```

```text
Dimension: Significance
Score: 2
Confidence: 4
Evidence basis: Section 5 states that no optic-flow or eye-to-Kenyon-cell model was refit, and that a population code could survive damage to one pair.
Deduction: A reporting checklist for one propagator, without a changed vision result, is below the CVPR main bar.
Repair condition: One cited visual endpoint ordered by the same certificate.
Expected score movement: Significance 2 to 3 or 4; overall +1 to +2. This is the condition that most limits the score.
```

```text
Dimension: Reproducibility
Score: 3
Confidence: 4
Evidence basis: Training hyperparameters are in Section 3.5. Body IDs and the 24-draw rows are not in the PDF. The ensemble JSON was not in the allowed artifact set.
Deduction: The three transfers can be checked; the ensemble and the neuron filter cannot be rerun from the paper.
Repair condition: Anonymous supplement with the graph and draw table.
Expected score movement: Reproducibility 3 to 4; overall unlikely to move by a full point.
```

**Overall:** 4  | **Scholarly Confidence:** 4

**Recommendation:** weak-reject

**Verdict:** Raising the score by one point requires the support-preserving, multi-route ensemble in C1. Raising it by two requires that ensemble to matter on a published visual endpoint. Lowering it by one point would follow from evidence that the route was selected after the accuracies, or that additional routes reverse the ordering.

| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | Both-columns-preserving degree-matched draws, on more than one pre-declared route, preserve the MLP ordering | Evidence, Significance | +1 overall, from 4 to 5 |
| Raise score further | The same certificate changes a flyvis or Kenyon-cell comparison under Equation (1) | Significance, Originality | +1 to +2 overall, from 4 toward 6 |
| Lower score | The audited route was chosen after seeing accuracy, or the transfer report does not come from the stated graph | Soundness, Evidence | -1 overall, or to 3 if the central comparison fails |
| No quick change | Refitting the cited visual models, or proving the 0/24 rate beyond this mixing length | Significance | Unlikely before the decision without new runs |

```text
Quality: 3
Clarity: 4
Significance: 2
Originality: 3
Soundness: 4
Evidence: 3
Reproducibility: 3
Ethics / Limitations: 4
Overall: 4
Confidence: 4
Score-change conditions: C1 can move 4 to 5; a published visual endpoint can move 4 toward 6; route-selection leakage or a reversed route can move 4 to 3.
```

### Writing scorecard

Writing score = 3.72 / 5. Writing risk band = moderate. This measures communication risk, not scientific validity.

| Dimension | Weight | Score (1-5) | Confidence (1-5) | Evidence basis | Concrete repair |
| --- | ---: | ---: | --- | --- | --- |
| Storyline and motivation | 10 | 4 | 5 | Section 1 | Open with the reporting requirement, then the one subgraph. |
| Contribution display | 10 | 4 | 5 | Abstract; Section 5 | Name the two XORs before their scores. |
| Paragraph logic | 10 | 4 | 5 | Sections 3 and 4 | Split the abstract's number list from the task definition. |
| Claim-evidence alignment | 12 | 3 | 5 | PDF lines 69-72 versus Section 3.5 | Replace "two-input visual readout" with "two-input XOR on this route." |
| Method readability | 9 | 4 | 5 | Sections 3.1-3.3 | State how many relays passed the rule before naming nodes 6 and 109. |
| Experiment narration | 9 | 4 | 5 | Section 4.1 | Keep the non-effect on subspace before the digit-parity effect. It already does. |
| Related-work positioning | 8 | 4 | 4 | Section 2 | The operator distinctions are the right axes. |
| Terminology and notation consistency | 8 | 3 | 5 | Section 4.3; Table 1 | Do not call the module-pair histogram a motif count. |
| Prose discipline and voice | 10 | 4 | 5 | Sections 4.3 and 5 | The limits are stated in plain sentences. |
| LaTeX and format discipline | 6 | 4 | 5 | 5-page review PDF; no overfull boxes | Fix the 0.507 cell and the collided axis labels. |
| Reviewer-facing risk | 8 | 3 | 5 | Abstract plus introduction | The abstract can be quoted as a vision result that Section 5 retracts. |

```text
Format verdict: acceptable for review. Not compiled in this review; the existing log was read. It reports 5 pages and no overfull or underfull boxes.
Blocking compliance issues: none found against the CVPR 2027 eight-page rule, anonymity rule, or LLM-statement rule.
LaTeX/source issues: not compiled here. Source uses \usepackage[review]{cvpr}, \def\confYear{2027}, and \author{Anonymous}.
Figure/table/caption issues: Figure 1 axis text collides; Table 1 digit cell disagrees with Section 4.1 by 0.001. Captions otherwise say what the panels are.
Citation/reference issues: checked identities match. ieeenat_fullname is the CVPR bibliography style.
Notation/equation issues: A_uv, W_vu, and T are defined before use and match the JSON matrices.
Suggested checks or build command: not recompiled in this review.
```

## 14. Questions For Authors

1. How many relays satisfied the Section 3.1 rule, and was node 9 the first in the pre-declared order before any accuracy was computed?
2. If degree-preserving swaps are rejected unless both source columns stay nonzero, what is the MLP accuracy distribution on digit parity relative to 0.663 and 0.746?
3. Do sum aggregation and symmetric normalization produce the same support and rank split on this route?
4. Which visual-string filter and which body IDs define the 768 nodes and the five audited neurons?

## 15. Score Revision Criteria

```text
Raising the score would require: a both-columns-preserving degree-matched ensemble on more than one pre-declared route, with the MLP ordering intact. That is the one-point change, from 4 to 5. A further point requires the certificate to change a published visual endpoint under the same propagator.
Lowering the score would be triggered by: evidence that the route was selected after the accuracies, a transfer that does not come from the stated graph, or additional routes that reverse the digit-parity ordering.
Concerns unlikely to change before submission: a full refit of flyvis or the eye-to-Kenyon-cell model. The manuscript already says those runs were not done. Wording fixes will not move 4 to 5.
```

## 16. Action Plan And CCFA Handoffs

```text
Priority: 1
Action: Build the support-preserving degree-matched ensemble and repeat the MLP on every pre-declared route that passes the existing rule.
Owner skill: ccf-experiment-designer
Input needed: the 768-node graph, the selection rule, and the current training script
Expected output: a table of column support, rank, and paired MLP accuracy
Handoff required: yes
```

```text
Priority: 2
Action: Add one published visual endpoint under Equation (1), or remove vision-benchmark wording from the abstract and introduction.
Owner skill: ccf-experiment-designer for the endpoint; ccf-paper-writer for the wording fallback
Input needed: the chosen endpoint's published protocol, or the author decision to stay with the XOR probes
Expected output: either a new result table or a narrowed claim
Handoff required: yes
```

```text
Priority: 3
Action: Correct 0.507 to 0.506, separate the Figure 1 axis labels, and stop using "motif" for the module-pair histogram.
Owner skill: ccf-paper-writer
Input needed: main.tex and figures/transfer_readout.pdf
Expected output: a numeric and terminology patch
Handoff required: yes
```

```text
Priority: 4
Action: Add an anonymous supplement with the neuron filter, five body IDs, graph, and 24-draw support rows.
Owner skill: ccf-paper-writer
Input needed: the graph build outputs
Expected output: a supplement that makes Section 4.2 auditable
Handoff required: yes
```

```text
Checks run: four reading passes; claim-to-readout arithmetic and 5,000-resample percentile bootstrap from executed-readout.json; entrywise comparison of the three T matrices with narrowk4_transfer_report.json; visual check of both figures; PDF page count and compile log; CVPR 2027 policy page; bibliographic identity of Berg, Lappalainen, Dorkenwald, Dhiman, Park, Correig-Fraga et al., and Liu.
Checks skipped: no re-execution of the graph build, the 24 swaps, or the MLP; no byte-level diff against the CVPR 2027 author-kit zip; degree_ensemble.json was not available.
Unresolved risks: route multiplicity is unknown; the module-histogram claim for the 24 draws is prose-only; the transfer report is marked as a rebuild, so agreement is numerical rather than a fresh execution.
```

## 17. Output Self-Check

Section order follows the standard report. Tables have a header and a separator. Overall 4, weak reject, and scholarly confidence 4 match the AC stance and the significance deduction. Scores of 3 or below have a repair condition. No acceptance probability is stated. Park is treated as contemporaneous, not as silent prior art. The 0.507 mismatch is recorded and does not carry the decision.

**Overall:** 4  | **Scholarly Confidence:** 4

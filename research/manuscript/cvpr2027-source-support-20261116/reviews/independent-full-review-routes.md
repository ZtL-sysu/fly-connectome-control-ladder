# Independent full review: A Degree Match Does Not Keep Both Inputs

## 1. Report Metadata

```text
Review date: 2026-11-16
Target venue/year/track: CVPR 2027 main technical program
Paper title: A Degree Match Does Not Keep Both Inputs
Input materials reviewed: manuscript/source-support-20261116/main.tex, main.pdf, references.bib; executed-readout.json; analysis/source_support/multiroute.json; analysis/source_support/one_column_digit.json; narrowk4_base.npz, narrowk4_namededge_s0.npz, narrowk4_pathblock_p0.npz; make_figures.py; run_multiroute.py; run_degree_ensemble.py
Search basis: CVPR 2027 Author Guidelines, Reviewer Guidelines, and Call for Papers; arXiv abstracts 2610.10023, 2604.04033, 2609.39248, 2611.14508, 2611.01213; Cell 189(18) Berg et al. DOI 10.1016/j.cell.2026.08.015
Report file: manuscript/source-support-20261116/reviews/independent-full-review-routes.md
Reviewer mode: full (scientific + writing + format). No manuscript rewrite. No rebuttal text.
```

CVPR 2027's public reviewer page describes review duties, quality, and process. It does not publish a numeric recommendation form. Scores below use the skill scale: criteria 1–5, overall 1–10. They are not an official CVPR form and they are not an acceptance probability.

## 2. Desk Rejection Assessment

```text
Check: Paper length
Status: pass
Evidence: main.pdf has 6 pages, US Letter, 612 x 792 pt. Discussion ends on page 5. References continue onto page 6. Content is under the eight-page limit.
Consequence: Not a length desk reject.
Required action: None for length.
```

```text
Check: Topic compatibility
Status: pass
Evidence: The 2027 Call for Papers lists "Medical and biological vision, cell microscopy" among topics of interest. The manuscript is a connectome-constrained visual-readout audit, not a standard recognition benchmark.
Consequence: Not a wrong-venue desk reject. Venue fit still limits significance; see Section 6.
Required action: None at desk-reject level.
```

```text
Check: Minimum quality
Status: pass
Evidence: The source has an abstract, introduction, related work, method, results, a routes section, discussion, one table, three figures, equations, and a bibliography. The central comparison can be checked against stored runs.
Consequence: Reviewable.
Required action: None at desk-reject level.
```

```text
Check: Policy/anonymity/compliance
Status: pass
Evidence: Review mode, line numbers, header "CVPR 2027 Submission. CONFIDENTIAL REVIEW COPY. DO NOT DISTRIBUTE.", author line "Anonymous CVPR submission". LLM Usage Statement is present on page 5, lines 384–391, before the references, and uses the generic-tool anonymity carve-out. No external links in main.tex. Dual submission cannot be checked from the files.
Consequence: No anonymity or missing-statement desk reject found. Dual-submission status is unknown.
Required action: None from the inspected files.
```

```text
Check: Prompt injection and hidden manipulation detection
Status: pass
Evidence: main.tex was read in full. No hidden instructions, white-on-white text, or instructions addressed to a reviewer model.
Consequence: None.
Required action: None.
```

```text
Check: Ethics and reviewability
Status: pass
Evidence: The graph is a public male fly connectome subset. No human subjects. Limitations are stated in the discussion. Graph files and the 24-draw records are not inside the submission PDF.
Consequence: Not an ethics desk reject. Artifact completeness is a reproducibility score issue, not a desk reject.
Required action: Archive the draw records with the submission if this remains a CVPR paper.
```

```text
Desk rejection risk: low
Reason: Length, anonymity, LLM statement, topic listing, and absence of prompt injection all pass. The decision risk is evidentiary, not administrative.
Can be fixed before review? partly
```

## 3. Paper Summary And Contribution Map

The paper asks what a degree, motif, or wiring-cost match fails to preserve for one propagator. On a 768-neuron, 4-incoming-synapse subgraph of the male fly visual cells, incoming-neighbor averaging for two steps gives a 2×2 source-to-sink transfer \(T\). Two module-matched edits share edge count, degree sequences, and module-pair counts with the measured graph and both remove the shared relay. One leaves both source columns nonzero and rank 2. The other deletes a column. An MLP on the sink state tracks that difference. A linear readout stays at chance. An unrestricted degree-preserving ensemble of 24 draws retains both columns in none. Holding the two-hop edges fixed leaves \(T\), and the parity score, essentially where the measured route put them.

Claimed problem: published connectome-versus-null verdicts follow the control, but degree, motif, and cost certificates do not state whether both inputs of a two-input readout survive a stated propagator.

Claimed gap: prior nulls are not statements about the signal at a chosen pair of sinks. Park is the closest precedent on route destruction by a standard null. This paper's claimed delta is column support and column rank under mean aggregation, not a new visual model.

Method/contribution map:

- Select the first eligible relay and read \(T = R_S W^2 E_{ab}\).
- Separate a rank-2 both-support edit from a rank-1 deleted-column edit, both degree- and module-matched.
- Show that subspace XOR follows support, digit-parity XOR also follows rank, and a linear readout follows neither.
- Show that 24 unrestricted degree-preserving rewires keep both columns in 0 draws, while protecting two-hop edges keeps both columns.

Evidence package: Table 1, Figures 1–3, ten seeds (11 through 103) for the three graphs, six seeds for three routes, and a digit-class side task. Limitations stated by the authors: one searched route, one sparsification, no refit of optic flow or an eye-to-Kenyon model, and no claim that randomizing fly synapses improves vision.

## 4. Search And Related-Work Basis

```text
Queries used:
CVPR 2027 author guidelines, reviewer guidelines, call for papers
arXiv 2609.39248 Park null-model sensory-motor boundary
arXiv 2604.04033 Dhiman topological sensitivity
arXiv 2610.10023 Correig-Fraga structure alone visual computation
arXiv 2611.14508 Liu When Does the Real Wiring Win flyvis
arXiv 2611.01213 connectome degree
Berg 2026 Cell male CNS connectome DOI 10.1016/j.cell.2026.08.015
Sources searched:
https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines
https://cvpr.thecvf.com/Conferences/2027/ReviewerGuidelines
https://cvpr.thecvf.com/Conferences/2027/CallForPapers
https://arxiv.org/abs/2609.39248
https://arxiv.org/abs/2604.04033
https://arxiv.org/abs/2610.10023
https://arxiv.org/abs/2611.14508
https://arxiv.org/abs/2611.01213
https://doi.org/10.1016/j.cell.2026.08.015
Closest works found:
Park, arXiv:2609.39248. Degree-preserving swaps and column shuffles add one-step olfactory-to-descending shortcuts and change an evolutionary comparison. The manuscript's "different sign" sentence matches that abstract: there the null adds a shortcut; here an unrestricted null removes two-hop inputs.
Dhiman, arXiv:2604.04033. A flyvis-style masked recurrence loses an early-loss gap under shared initialization and an activity gap under a degree-preserving null. The manuscript is right that this operator is W_G = M_G odot W-tilde, not incoming-neighbor averaging.
Correig-Fraga, Guimerà, and Sales-Pardo, arXiv:2610.10023. A connectome-only eye-to-Kenyon model learns scalar gains and beats cost-matched randomizations. The manuscript's paraphrase matches the abstract.
Liu, arXiv:2611.14508. Physiology-assignment protocols flip some wiring verdicts. The abstract does contain a flyvis ranking and a mushroom-body comparison, so that phrase in the introduction is supported.
Berg et al., Cell 189(18):5504–5526.e15, 2026, DOI 10.1016/j.cell.2026.08.015. Bibliographic identity matches.
Nearby and not the same claim: Bertamini et al., arXiv:2611.01213, separates weight placement from wiring in human connectome reservoirs under degree-preserving rewiring. Different organism, task, and claim.
Unverified related-work risks:
Lappalainen et al. Nature 2024, Dorkenwald et al. Nature 2024, Maslov and Sneppen Science 2002, Milo et al. Science 2002, and the GIN, PNA, GCN, and GraphSAGE entries were not re-fetched in this session. They are standard citations and the bibliography fields are complete enough to identify them. No MDPI entries are present.
Source-quality screening status:
Four positioning papers are 2026 arXiv preprints and were checked at abstract level. No predatory-publisher entries were found in references.bib. Full texts of the Nature, Science, and GNN entries were not re-read.
```

The novelty delta against Park is real and narrow: rank versus support under mean aggregation on one visual subgraph, not a second demonstration that nulls rewrite a sensory-motor boundary. That is not a novelty collapse.

## 5. Expected Review Outcome

```text
Expected outcome: weak reject
Main accept signal: Table 1 is a real, checked contrast. Degree and module matches do not separate a both-support edit from a deleted-column edit, and the MLP does.
Main reject signal: The evidence never leaves one 768-neuron sparsification, one averaging rule, and one searched pair. Section 5 does not supply an ensemble of distinct both-support rewires, and the unrestricted 24-draw null cannot, because it keeps both columns in none of the draws.
Confidence: 4/5
```

## 6. Strengths And Weaknesses

Strengths:

- The question is stated before the method. Intro-P2 says a degree, motif, or cost match is not a statement about the signal at two sinks. That is the right object.
- Table 1 separates the certificates. Degree and module columns match on both edits; shared relays are 0 and 0; rank(\(T\)) is 2 versus 1; subspace MLP is 0.979 versus 0.504 and digit-parity MLP is 0.746 versus 0.506. Those three-graph means match `executed-readout.json` after ordinary three-decimal rounding.
- The discussion already refuses the over-reading. Disc-P2 says the result does not overturn a flyvis or Kenyon-cell comparison, because those operators are not Equation (1). Disc-P3 says the tasks use two selected neurons and an XOR.
- The three recovered graphs have the printed transfers, ranks 1/2/1, shared relays 1/0/0, 3072 edges, and exact in-degree, out-degree, and module-pair matches. The measured-graph identity residual is \(5.55\times 10^{-17}\) in float64 and \(2.98\times 10^{-8}\) in float32, consistent with the printed \(3\times 10^{-8}\).
- Related-work positioning against Dhiman, Park, Liu, and Correig-Fraga follows the abstracts rather than a citation list.

```text
Weakness: The decision-relevant evidence is one constructed route, and Section 5 does not multiply it.
Evidence basis: Abstract-P1 and Section 5. Routes are the first three relays from the rule in Section 3.1. Twelve protected draws are stored in multiroute.json. Eleven leave T unchanged and repeat the measured accuracy vector exactly. The twelfth, route 2 protected_2, changes one entry from 0.0625 to 0.125 and moves parity from 0.709880 to 0.700439. Training uses T, so an unchanged T is a repeated training of the same map, not a new wiring test. The reported route scores 0.670, 0.675, and 0.708 are 0.670492, 0.674886, and the four-draw mean 0.707520.
Reviewer deduction: I cannot treat "both columns survive degree-matched rewiring" as an ensemble result. It is three measured transfers, plus one nearby transfer.
Required fix: Narrow Section 5 and the abstract so protected rewires are described as replicates of T, except the one changed draw. A score move needs a source-support-conditioned ensemble in which both columns are actually retained and rank is recorded, with the ten-seed MLP, beyond the two hand edits.
```

```text
Weakness: The unrestricted degree null cannot test the hypothesis it is introduced to test.
Evidence basis: Section 4.2 and Figure 2. Replay of seeds 50_000+s, without retraining, reproduced 22 draws with neither column, 2 with one, and 0 with both. All 24 degree sequences matched. Module-pair counts matched in 0 of 24. The manuscript says this comparison contrasts a graph that carries both inputs with graphs that do not. The abstract still leads with the accuracy drop and the 24-draw sentence before that qualification.
Reviewer deduction: A null that is incapable of carrying both inputs cannot show that degree is insufficient among graphs that do carry both inputs. The only both-support, degree-matched, fully trained contrast is the hand-built separate-routes edit against the measured graph.
Required fix: Add degree-preserving draws conditioned on both columns remaining nonzero, record rank(T), and evaluate the same ten-seed MLP. Until that exists, keep the 24-draw result as a statement about route destruction, which the paper already understands, and do not let it carry the sufficiency claim.
```

```text
Weakness: The open-route number 0.504 is the wrong rounding, and the six open lists are one stored chance result.
Evidence basis: multiroute.json. All six open parity means are 0.5034993489583334, which rounds to 0.503, not the printed 0.504 in Section 5 and the abstract. Five of the six transfers are the zero matrix. Route 2 open_1 is T = [[0, 0], [0, 0.0625]] and still has a bitwise-identical parity vector. Route 0's measured parity vector is bitwise-identical to the first six seeds of the ten-seed measured run. The ten-seed deleted-source mean 0.503760, printed as 0.504 in Table 1, is a different quantity and is rounded correctly.
Reviewer deduction: "0.504 on all six draws" reads as six graph tests. The archive supports one repeated chance vector. The one-column open draw was not shown to have been trained into a distinct accuracy.
Required fix: Print 0.503 and state that the six open lists are one repeated chance result. Archive the 24-draw records. Do not describe these draws as independent wiring tests.
```

Two smaller numerical facts do not drive the score. A 200,000-draw percentile bootstrap of the stored ten seeds, seed 20261116, moves two printed intervals by 0.001: deleted-source subspace [0.494, 0.515] against printed [0.495, 0.514], and digit separate-minus-measured [0.073, 0.094] against printed [0.072, 0.094]. The figure hardcodes the deleted-source subspace endpoints as 0.4947 and 0.5141, which round to the sentence rather than to this resample. Ordering is unchanged. The measured-minus-deleted digit interval rounds to the printed [0.141, 0.170]. The sentence "linear intervals lie between 0.493 and 0.516" is true for bootstrap intervals of the ten-seed means (about 0.4937 to 0.5157) and false for the raw seeds (0.4727 to 0.5386).

## 7. Potentially Missing Related Work

```text
Work: Park, arXiv:2609.39248, Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison
Status: searched
Why relevant: Closest precedent that a standard degree null rewrites the routes a task can use.
Overlap: Both conclude that a performance gap against an unrestricted degree null is not yet a difference beyond degree.
Needed comparison: One sentence, already partly present in Disc-P1, stating the delta: this paper measures support and rank under mean aggregation, and the null removes two-hop inputs rather than adding one-step shortcuts. No further experiment is required to avoid a novelty collapse. A visual-model comparison is required for significance, not to cite Park.
```

```text
Work: Bertamini et al., arXiv:2611.01213, Is Newborn Wiring Special?
Status: searched
Why relevant: Also argues that a degree-preserving rewiring does not isolate wiring.
Overlap: Shared moral, different object. That paper separates weight placement from edge support on human connectome reservoirs.
Needed comparison: Optional citation if space allows. Not a missing baseline for this 2×2 transfer.
```

```text
Work: Dhiman, arXiv:2604.04033; Correig-Fraga et al., arXiv:2610.10023; Liu, arXiv:2611.14508
Status: searched
Why relevant: The introduction's verdict-follows-the-control paragraph.
Overlap: Already cited and, at abstract level, accurately paraphrased. Liu's abstract does contain the flyvis ranking, so that phrase is not unsupported.
Needed comparison: None for citation honesty. The missing piece is empirical: these operators are not rerun with column support and rank stratified. The discussion already says they are different operators.
```

## 8. Claim-Evidence Audit

| Claim | Where stated | Evidence provided | Strength | Reviewer deduction | Required fix |
| --- | --- | --- | --- | --- | --- |
| Degree and module matches do not separate the two edits; \(T\) does | Abstract-P1; Table 1; Section 3.3 | Three npz graphs: exact degree and module-pair matches; printed \(T\); ranks 1, 2, 1; shared relays 1, 0, 0 | Strong for these three graphs | None for this sentence | Keep the claim on these three graphs |
| MLP scores 0.979 and 0.746 with both columns independent, against 0.504 and 0.506 when one column is deleted | Abstract-P1; Table 1; Section 4.1 | Ten-seed means 0.978955 / 0.745850 / 0.503760 / 0.506494. Paired digit gaps are positive on 10/10 seeds. Subspace separate-minus-measured is positive on 6/10 only, and the paper says so | Strong for this MLP, these seeds, these tasks | None on the rounded table means | Leave the paired subspace contrast described as small, which the paper already does |
| Measured wiring scores 0.976 on subspace XOR and 0.663 on digit parity, below the edit that removed the shared relay | Abstract-P1; Section 4.1 | Means 0.976367 and 0.662598. Digit gap +0.083 on 10/10 seeds | Strong for digit parity; weak as a biological-relay conclusion | The relay is confounded with rank 1 versus rank 2 | Keep the certificate as support and rank, which Intro-P4 already says |
| A linear readout stays at chance | Abstract-P1; Section 4.1 | Six linear mean-intervals lie between about 0.4937 and 0.5157. Raw seeds reach 0.4727–0.5386 | Strong if "intervals" means bootstrap intervals of the means | A reader can misread the sentence as the range of seeds | Say these are intervals of the ten-seed means |
| Twenty-four unrestricted rewires retain both sources in none of the draws | Abstract-P1; Section 4.2; Figure 2 | Structural replay, seeds 50_000+s: 22 neither, 2 one, 0 both; 24/24 degree matches; 0/24 module-pair matches. Figure 2 hardcodes [22, 2, 0]. MLPs for these 24 draws were not retrained in this review | Strong as a structural count on this subgraph and mixing length | The null cannot answer the sufficiency question | Report it only as route destruction, and archive the 24 records |
| Protected rewiring leaves both columns and parity at 0.670, 0.675, and 0.708, while each graph shares only 42 to 57 of 3,072 edges | Abstract-P1; Section 5 | Edge overlap replay is 42–57 and protected edges are retained. Parity numbers match the route means, with 0.708 equal to the four-draw mean on route 2. Eleven of twelve protected draws copy \(T\) and the accuracy vector | The edge overlap is real. The accuracy sentence is a replicate summary | This is not twelve wiring tests | Call them replicates of \(T\), and separate the one changed draw |
| The same budget with those edges free falls to 0.504 | Abstract-P1; Section 5 | Stored mean 0.503499 on all six open draws, bitwise-identical vectors, including route 2 open_1 whose \(T\) is not zero | The chance outcome is plausible. The printed thousandth and the independence are not | One chance vector is printed as six results, and 0.504 does not round from 0.503499 | Print 0.503 and say the six lists are one repeated result |
| Digit class stays between 0.939 and 0.985 with both columns and falls to 0.099 with none; one column still scores 0.878 and remains at chance on parity | Abstract-P1; Section 5 | Digit means 0.958903, 0.938558, 0.985270; zero-transfer 0.098877; one_column_digit.json 0.878092, upper 0.939697, lower 0.894613 | Strong for this side task | The drop from about 0.96 to 0.10 is loss of every input. The paper says this in Routes-P3 | Keep that qualification next to the abstract sentence |
| Removing the shared relay can improve a two-input readout | Intro-P4; Section 4.1 | True for digit parity on this one edit, 10/10 seeds, not for a stable subspace gap | Narrowly supported | Easy to read as a biological claim | Keep Misread-P2's scope sentence in the abstract |
| Where source support differs, the accuracy table is not yet a wiring result | Disc-P2 | Supported as a reporting rule by the three-graph table. Not shown inside flyvis, optic-lobe, or Kenyon comparisons | Moderate as advice; weak as a transferred empirical result | The sentence is the paper's real contribution, and it is not yet demonstrated on the models named in the introduction | Either narrow it to this propagator, or run one pre-specified visual comparison |

## 9. Experiment / Benchmark / Reproducibility Audit

Baselines: the linear map is the right negative control for an XOR. There is no flyvis, optic-flow, or Kenyon-cell arm. The discussion says so. For CVPR that absence is the significance limit, not a hidden baseline the authors pretended to run.

Ablations: separate-routes versus deleted-source isolates column support under matched degree, module, edge count, and zero shared relays. Measured versus separate-routes confounds the shared relay with rank(\(T\)). The 24-draw ensemble does not contain a both-support cell, so it is not an ablation of degree given support. Section 5's protected condition mostly copies \(T\).

Datasets and benchmarks: scikit-learn digits, a fixed QR projection, and a synthetic subspace XOR. The route is the first relay passing a search rule, not a named motion pathway. Nodes are 6 and 109 to sinks 4 and 5, relay 9, on the first route only.

Metrics: balanced accuracy against chance 1/2, plus ten-way digit accuracy against chance 0.1. Appropriate for the constructed labels.

Statistical rigor: ten seeds for the main table, paired by seed, percentile bootstrap. The paper says the minibatches are not paired across graphs. Six of ten subspace paired signs are positive, and the interval on that difference includes zero. Digit paired signs are 10/10. The open-route "six draws" are not six tests. The paper states 5,000 bootstrap resamples; the plotted intervals are hardcoded. A larger resample moves two endpoints by 0.001 without changing order.

Robustness and failure cases: digit class is a useful negative example, because one column is enough. There is no failure case on a distributed retinal code, a population readout, another aggregator, or another sparsification. Disc-P3 names that boundary and does not test it.

Implementation details present in the paper: Adam learning rate 0.006, binary cross-entropy with logits, 120 epochs, 32 batches of size 128, evaluation on 2,048 samples, seeds, Apple MPS, PyTorch 2.13, and the statement that training uses \(T\).

Artifacts: the three graph files and the route JSON exist in the working tree and were checked. They are not part of the six-page submission. There is no `degree_ensemble.json`. `make_figures.py` hardcodes the bar means, the interval endpoints, and the counts 22, 2, 0. The 24-draw MLP accuracies were not retrained in this review. The structural replay was.

Limitations: the honest ones are already written. The missing limitation is statistical: protected draws with equal \(T\) are replicates, and the six open accuracy lists are one list.

## 10. Multi-Reviewer Panel

```text
Reviewer: Best-justified reviewer
Expertise: connectome controls and readout geometry
Likely score: 5
Confidence: 4
Main positive signal: Table 1 is a clean negative result. A degree match and a module match do not determine whether both inputs reach the sinks, and the MLP follows support and, on digit parity, rank.
Main negative signal: The result is one subgraph and two hand edits. Section 5 repeats T instead of sampling new both-support graphs.
Evidence basis: Table 1; executed-readout.json; the three npz transfers; Disc-P2 and Disc-P3, which already limit the claim.
Fatal concern if any: none
Score-change condition: A both-columns-retained degree ensemble with the ten-seed MLP, plus the replicate and 0.503 corrections, would move this reviewer toward 6. It would not by itself reach 7.
```

```text
Reviewer: Critical reviewer
Expertise: CVPR empirical standard
Likely score: 3
Confidence: 4
Main positive signal: The three-graph arithmetic checks out, and the paper does not hide the linear control.
Main negative signal: A CVPR submission whose visual evidence is a searched pair of neurons, a 2×2 transfer, and an MLP on a subspace XOR does not establish the control rule advertised in the introduction.
Evidence basis: Abstract-P1; Section 5 replicate structure in multiroute.json; 0/24 both-support draws; no flyvis or Kenyon arm.
Fatal concern if any: For this venue, the missing visual comparison is fatal to acceptance. It is not a claim that Table 1 is numerically false.
Score-change condition: Only a pre-specified visual-model comparison whose conclusion changes after stratification by column support and rank would move this reviewer. Wording fixes will not.
```

```text
Reviewer: Method / soundness reviewer
Expertise: graph propagators
Likely score: 4
Confidence: 4
Main positive signal: Equation (1), the definition of T, the zero-column Bayes argument, and the rank distinction are the right objects. The measured identity residual matches the printed bound.
Main negative signal: Because training uses T, graphs that share T are not distinct mechanistic tests. The unrestricted null is also the wrong instrument for a both-input hypothesis.
Evidence basis: Section 3.2; Section 5; eleven identical protected transfers; 0/24 both-support unrestricted draws.
Fatal concern if any: none. The algebra for the three named graphs is intact.
Score-change condition: Report replicates as replicates and add draws that keep both columns while varying rank. That is a method-of-evidence fix, not a repair of Equation (1).
```

```text
Reviewer: Evidence / experiment reviewer
Expertise: controlled ablation
Likely score: 3
Confidence: 4
Main positive signal: Separate-routes versus deleted-source is a real support ablation. Digit class shows that a one-column graph can still classify the digit.
Main negative signal: The degree ensemble has an empty both-support cell, and Section 5 fills the protected cell with copies.
Evidence basis: Figure 2 replay 22/2/0; multiroute.json; Table 1 sample size of two edits.
Fatal concern if any: none inside the three-graph claim; fatal for the broader control claim.
Score-change condition: Ten-seed MLP on a pre-specified set of degree-matched graphs that retain both columns, with rank recorded, including failures.
```

```text
Reviewer: Novelty / positioning reviewer
Expertise: connectome-null literature
Likely score: 3
Confidence: 4
Main positive signal: The delta from Park is support versus rank under mean aggregation, and the manuscript does not pretend to rerun Park's evolutionary task.
Main negative signal: The new empirical object is a 2×2 matrix on a searched pair. The positioning papers are cited fairly, but the paper's own conclusion says the finding does not transfer to their operators.
Evidence basis: Park abstract; Disc-P1; Disc-P2; arXiv:2611.01213 as a nearby but different claim.
Fatal concern if any: none. This is not "Park already did this."
Score-change condition: Novelty reaches 4 if the delta is demonstrated on one of the visual comparisons named in the introduction. Citation edits alone do not raise the score.
```

```text
Reviewer: Writing / clarity reviewer
Expertise: reviewer readability
Likely score: 4
Confidence: 4
Main positive signal: A reader can recover the certificate, the three graphs, and the refusal to claim that randomizing vision helps.
Main negative signal: The abstract is a stack of numbers, and it reports replicate route scores as if the rewiring had been independently re-fit.
Evidence basis: Abstract-P1; Section 5's 0.670 / 0.675 / 0.708 and 0.504 sentences.
Fatal concern if any: none
Score-change condition: Rewrite the abstract around task, gap, certificate, and the three-graph result, and label Section 5 as replicates. Clarity can reach 5. Overall does not, without new evidence.
```

```text
Reviewer: Ethics / reproducibility reviewer
Expertise: auditability
Likely score: 4
Confidence: 4
Main positive signal: Seeds, optimizer, batch size, device, and the T-substitution are written down. The LLM statement is generic and present. No human-subjects issue.
Main negative signal: The submission does not contain the graphs, the 24-draw archive, or a figure script that reads the JSON. The six open accuracy vectors are copies, including across a non-zero T.
Evidence basis: Page 5 LLM statement; absence of degree_ensemble.json in the submission; hardcoded bars in make_figures.py; multiroute.json identity.
Fatal concern if any: none
Score-change condition: Release graph files, seeds, and draw records, and regenerate the figures from those files. That repairs reproducibility toward 4 or 5 on that axis only.
```

```text
Reviewer: Domain application reviewer
Expertise: biological and medical vision
Likely score: 3
Confidence: 4
Main positive signal: The subgraph is cut from the male visual cells, and the paper says it is not a named motion pathway.
Main negative signal: No optic-lobe population, no eye image through the measured graph, and no flyvis-style task. A distributed code could survive the loss of one pair, and Disc-P3 states that without a test.
Evidence basis: Section 3.1; Disc-P3; digit halves used as a proxy visual input.
Fatal concern if any: For a vision claim about connectome-constrained models, yes. For a narrow propagator certificate, no.
Score-change condition: One pre-specified flyvis-style or optic-lobe/Kenyon comparison, with failure cases.
```

```text
Reviewer: Evidence/ablation reviewer
Expertise: what the controls isolate
Likely score: 3
Confidence: 4
Main positive signal: Deleted-source versus separate-routes holds degree, module, edge count, and shared-relay count fixed.
Main negative signal: Degree is not crossed with support. Rank is not crossed with an otherwise fixed route except at the single measured-versus-separate comparison. Protected rewires do not change the tested matrix.
Evidence basis: Table 1; Section 4.2; Section 5.
Fatal concern if any: none for the printed three-row table
Score-change condition: A support-by-rank table with more than two both-support graphs.
```

```text
Reviewer: Reproducibility reviewer
Expertise: rerun from the paper
Likely score: 3
Confidence: 4
Main positive signal: Enough training constants are printed to rerun the MLP given T.
Main negative signal: A reader of the PDF cannot recover the 24 draws, the protected edge sets, or the plotted intervals. The archived open-draw file repeats one accuracy vector. This review recomputed the structural claims only.
Evidence basis: main.tex Section 3.5; make_figures.py literals; no degree_ensemble.json.
Fatal concern if any: none
Score-change condition: Archive the draw records and generate figures from them. Re-saving the existing files does not create the missing both-support ensemble.
```

```text
Reviewer: Novice advocate reviewer
Expertise: first-pass readability
Likely score: 4
Confidence: 4
Main positive signal: The story order is readable: control, certificate, three graphs, degree null, what would be misread, protected routes, limits.
Main negative signal: The abstract starts with numbers before the task is easy to hold, and Figure 1's bars cannot be checked against a table of intervals.
Evidence basis: Abstract-P1; Figure 1 caption; Table 1 has means but not intervals.
Fatal concern if any: none
Score-change condition: Lead the abstract with the certificate, and put the intervals in Table 1 or say that the figure endpoints are hardcoded.
```

```text
Reviewer: AC / meta-reviewer
Expertise: CVPR area chair
Likely score: 4
Confidence: 4
Main positive signal: A careful negative control result that is numerically mostly faithful and already carefully scoped in the discussion.
Main negative signal: The result does not yet change a visual-model conclusion a CVPR reader came to see. The routes section over-counts replicates.
Evidence basis: Panel above. The best-justified score is 5 and the critical score is 3. Those are not averaged.
Fatal concern if any: Evidence scope for this venue.
Score-change condition: Wording, the 0.503 correction, and an archived 24-draw file can justify 5. Accept-leaning 7 needs a new pre-specified visual comparison, failure cases, and released records.
```

```text
Agreement: Table 1 is real. The 24-draw null destroys both-input support. Section 5 mostly repeats three transfers. The discussion's self-limits are accurate. Park is close and not identical.
Disagreement: The best-justified reviewer would discuss a repaired version at borderline. The critical and domain reviewers treat the missing visual comparison as decisive for CVPR now.
Decisive positive axis: A checked certificate that degree and module matches do not encode column support or rank for this propagator.
Decisive negative axis: Evidence scope. The both-support sample is two hand edits, and the apparent ensemble is replicates plus a null that never keeps both inputs.
Unresolved evidence: Whether any degree-matched graph that still carries both columns, other than the separate-routes edit, changes the MLP. The 24-draw MLP numbers were not retrained here. Nature, Science, and GNN full texts were not re-read.
AC stance: Weak reject, overall 4. Do not average 5 and 3. The binding issue is scope, not a collapsed three-graph table.
```

## 11. Concerns Table

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | major | Protected route results are replicates of \(T\), not an ensemble of rewirings | multiroute.json: 11/12 protected draws copy \(T\) and the accuracy vector; training uses \(T\) | Evidence, soundness | experiment | Call them replicates in the abstract and Section 5. Add a both-columns-retained degree ensemble with rank recorded and the ten-seed MLP | ccf-experiment-designer | Required for +1, together with C3 and the archive. Not sufficient for 7 |
| C2 | major | The unrestricted null never keeps both inputs, so it cannot test sufficiency of degree | Replay seeds 50_000+s: 22/2/0; Section 4.2 already says this | Evidence, significance | experiment | Keep the 24-draw claim as route destruction. Do not let it carry the both-input hypothesis | ccf-experiment-designer | Part of the +1 package only if a both-support ensemble is added |
| C3 | major | Open parity is printed as 0.504 from a mean of 0.503499, and six lists are one vector | multiroute.json open draws, including route 2 open_1 with a nonzero \(T\) | Evidence, reproducibility | writing | Print 0.503 and say the six open lists are one repeated chance result | ccf-paper-writer | Required for +1. Does not raise the score alone |
| C4 | major | No pre-specified flyvis-style or optic-lobe/Kenyon comparison | Disc-P2; Disc-P3; introduction citations | Significance, novelty | experiment | Run one comparison whose conclusion changes when degree-matched nulls are stratified by column support and rank. Include failure cases | ccf-experiment-designer | Required to reach accept-leaning 7. Not a wording fix |
| C5 | moderate | Two printed bootstrap endpoints differ by 0.001 from a 200,000-draw resample, and the figure hardcodes endpoints | executed-readout.json; make_figures.py values 0.4947 and 0.5141 | Reproducibility | reproducibility | Regenerate intervals from the stored seeds and print the resample count and seed | ccf-paper-writer | Does not move the overall score while order is unchanged |
| C6 | moderate | Graphs, 24-draw records, and figure-source values are not in the submission | No degree_ensemble.json; hardcoded figure script; PDF has no artifact link, correctly, because external links are disallowed | Reproducibility | reproducibility | Archive draw records and graph files in the supplement | ccf-submission-checker | Required alongside C1–C3 for +1 |
| C7 | moderate | The abstract is number-led and states route accuracies before the replicate structure | Abstract-P1 | Clarity | prose-quality | Rebuild the abstract around the certificate and the three-graph result | ccf-paper-writer | Clarity only |
| C8 | minor | "Linear intervals lie between 0.493 and 0.516" is true for mean intervals and false for raw seeds | Six linear seed vectors in executed-readout.json | Clarity | claim-qualification | Say the bounds are intervals of the ten-seed means | ccf-paper-writer | No overall movement |

## 12. AC / Meta-Review

Reviewer consensus: the three-graph table is a genuine, checked contrast, and the paper already knows that an unrestricted degree null on this subgraph throws away the inputs. The discussion's refusal to overturn flyvis or Kenyon-cell results is earned, because those operators were not run.

Reviewer disagreement: a sympathetic reading stops at "borderline if the replicates are labeled and one both-support ensemble is added." A CVPR reading stops at "this is not yet evidence about the vision models named in the first page." The disagreement is about what would count as the result, not about the arithmetic of Table 1.

Decisive acceptance axis: column support and rank order the executed MLP when degree, module, and edge count do not.

Decisive rejection axis: that demonstration is two edits and a set of repeated transfers. It does not change a pre-specified visual comparison.

AC stance: overall 4, weak reject. Confidence 4. The best-justified score of 5 and the critical score of 3 are not averaged. The 0.001 interval drift is not the reason for 4.

Discussion risks: a reviewer may collapse the paper into "the three-graph table is wrong" because of the open-route 0.504. That would be a misread. A reviewer may also treat Park as a novelty collapse. That would also be a misread. The fair reject is scope.

## 13. Quantitative Scores

### Criterion deductions for every score of 3 or below

```text
Dimension: Novelty
Score: 3
Confidence: 4
Evidence basis: Disc-P1 against Park, arXiv:2609.39248; the new object is rank versus support on one 2×2 transfer.
Deduction: The delta is real and too small, by itself, for a CVPR contribution. It does not rerun the visual comparisons that motivate the introduction.
Repair condition: Show the certificate changing one pre-specified flyvis-style or optic-lobe/Kenyon conclusion.
Expected score movement: novelty 3 to 4, and overall toward 7 only with the rest of the accept condition.
```

```text
Dimension: Soundness
Score: 3
Confidence: 4
Evidence basis: Section 3.2 says training uses T. Section 5 then treats twelve protected draws as route-level evidence, while eleven share T exactly.
Deduction: The propagator math is fine. The ensemble is not an ensemble of distinct maps, so the routes section does not test degree once the route is held fixed. It retests the same T.
Repair condition: Report equal-T draws as replicates, and evaluate draws whose retained routes are actually different.
Expected score movement: soundness 3 to 4 if the writing is narrowed and one real both-support ensemble is added. That is part of moving overall from 4 to 5.
```

```text
Dimension: Evidence
Score: 3
Confidence: 4
Evidence basis: Table 1; Figure 2 replay 22/2/0; multiroute.json; digit side task.
Deduction: The both-support, degree-matched sample with a distinct T is essentially one edit. The 24-draw null has no both-support cell. Six open accuracies are one vector.
Repair condition: The +1 package in Section 15. The jump to 7 needs the new visual comparison, failure cases, and released records.
Expected score movement: evidence 3 to 4 on the +1 package; 5 only if the visual comparison is real.
```

```text
Dimension: Significance
Score: 3
Confidence: 4
Evidence basis: Intro-P1 names flyvis, Kenyon readout, and evolutionary nulls. Disc-P2 says none of those operators is Equation (1).
Deduction: A reporting rule for this averaging operator on one searched pair does not yet change a vision result a CVPR reader can use.
Repair condition: One pre-specified comparison on a flyvis-style or optic-lobe/Kenyon task, stratified by column support and rank.
Expected score movement: required for overall 7. Not moved by wording.
```

```text
Dimension: Reproducibility
Score: 3
Confidence: 4
Evidence basis: Training constants are printed. degree_ensemble.json is absent. make_figures.py hardcodes the plotted numbers. Open-draw vectors are duplicated in the archive.
Deduction: The structural replay was reproducible from the scripts and seeds. A reviewer who has only the PDF cannot audit the 24 draws or the figure intervals, and the archived open result is one vector stored six times.
Repair condition: Archive the 24-draw records and graph files, and generate the figures from those files. Correct 0.504 to 0.503.
Expected score movement: reproducibility 3 to 4. Overall 4 to 5 only together with C1 and the both-support ensemble.
```

```text
Dimension: Quality
Score: 3
Confidence: 4
Evidence basis: The paper is careful, and the binding hole is the evidence design in Sections 4.2 and 5.
Deduction: Quality follows the strongest unresolved hole. A correct three-row table does not make a sufficient evaluation.
Repair condition: Same as evidence.
Expected score movement: quality 3 to 4 with the +1 package.
```

Clarity is 4. Ethics / limitations is 4. Those are above the mandatory deduction threshold. Clarity loses a point because the abstract is number-led. Ethics is not 5 because the draw records are not released; the limitations that are written are honest.

## Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
| --- | ---: | ---: | --- | --- |
| Novelty | 3 | 4 | Disc-P1; Park arXiv:2609.39248; one 2×2 transfer | Real delta, too narrow. Repair by changing one named visual comparison. |
| Soundness | 3 | 4 | Section 3.2; 11/12 identical protected transfers | Algebra holds. The routes section repeats T. Label replicates and add distinct both-support draws. |
| Evidence | 3 | 4 | Table 1; 22/2/0 replay; multiroute.json | Both-support sample is two hand edits. Repair with a support-conditioned ensemble. |
| Significance | 3 | 4 | Intro-P1; Disc-P2; Disc-P3 | Does not change a flyvis, optic-lobe, or Kenyon conclusion. Repair by running one. |
| Clarity | 4 | 4 | Abstract-P1; Section 4 and Section 5 are otherwise ordered | Abstract stacks numbers. Repair the abstract. Overall stays 4 without new evidence. |
| Reproducibility | 3 | 4 | Printed seeds and optimizer; no 24-draw archive; hardcoded figure | Archive records and regenerate figures. Correct the open-route rounding. |
| Ethics / Limitations | 4 | 4 | Disc-P3; page-5 LLM statement; public connectome | Limitations match the experiments. Release draw records to go higher. |

**Overall:** 4 | **Scholarly Confidence:** 4

**Recommendation:** weak reject

**Verdict:** Correcting the replicate wording, printing 0.503, archiving the 24 draws, and adding a both-columns-retained degree ensemble with the ten-seed MLP would raise the score by one point, to 5. Accept-leaning 7 needs a new pre-specified visual comparison, failure cases, and released graph and seed records.

```text
Quality: 3
Clarity: 4
Significance: 3
Originality: 3
Soundness: 3
Evidence: 3
Reproducibility: 3
Ethics / Limitations: 4
Overall: 4
Confidence: 4
Score-change conditions: +1 to 5 from the replicate correction, the 0.503 correction, the 24-draw archive, and a both-support degree ensemble. Overall 7 only from a new visual comparison plus failure cases and released records. The 0.001 bootstrap drift does not move the score.
```

## 14. Questions For Authors

1. For the twelve protected draws, how many distinct values of \(T\) were trained, and will the paper report eleven of them as repeated seeds on an unchanged transfer?
2. Why is the parity vector for route 2 `open_1`, whose transfer is not zero, bitwise-identical to the five zero-transfer open draws? Was that draw trained separately?
3. Can you archive the 24 unrestricted draws, including \(T\), rank, and degree-match flags, rather than only the hardcoded counts 22, 2, and 0?
4. Is there any degree-matched graph, other than the separate-routes edit, that keeps both columns and changes rank, and was it chosen before seeing accuracy?
5. Which single published visual comparison, if any, changes its conclusion when the nulls are split by column support and rank? If none was run, the discussion should keep saying so, as it does now.

## 15. Score Revision Criteria

```text
Raising the score would require:
To 5: In Section 5 and the abstract, describe the protected rewires as replicates of T, except route 2 protected_2. Change the open-parity 0.504 to 0.503 and state that the six open lists are one repeated chance result. Archive the 24-draw records. Add a source-support-conditioned degree ensemble that keeps both columns, records rank, and reports the ten-seed MLP beyond the two hand edits.
To accept-leaning 7: New evidence. A pre-specified flyvis-style or optic-lobe/Kenyon visual comparison whose conclusion changes when degree-matched nulls are stratified by column support and rank, plus failure cases and released graph and seed records.
Lowering the score would be triggered by:
A failed replay of Table 1, or a demonstration that the separate-routes and deleted-source graphs do not match degree or module counts. This review did not find that. Discovery that the printed transfers are not the matrices that were trained would drop soundness further. The stored JSON matches the printed matrices.
Concerns unlikely to change before submission:
CVPR significance, if no new visual comparison is run. Wording cannot supply that comparison. The gap to Park can be clarified in a sentence; it cannot be turned into a broader vision result by editing.
```

## 16. Action Plan And CCFA Handoffs

```text
Priority: 1
Action: Narrow Section 5 and the abstract so protected equal-T draws are replicates, print open parity as 0.503, and say the six open lists are one repeated chance result.
Owner skill: ccf-paper-writer
Input needed: This review and multiroute.json. Do not rewrite the scientific claim beyond those qualifications.
Expected output: Scoped abstract and Section 5. No new experiments.
Handoff required: yes
```

```text
Priority: 2
Action: Archive the 24 unrestricted draws and regenerate Figure 1 and Figure 2 from stored seeds rather than hardcoded endpoints and counts.
Owner skill: ccf-submission-checker
Input needed: Replay records from seeds 50_000+s and the ten-seed JSON. MLPs for the 24 draws were not retrained here.
Expected output: A draw archive and figures whose endpoints match a stated bootstrap.
Handoff required: yes
```

```text
Priority: 3
Action: Design a degree-preserving ensemble conditioned on both columns remaining nonzero, with rank recorded, using the existing ten-seed MLP and the same tasks.
Owner skill: ccf-experiment-designer
Input needed: The current propagator, seeds, and a pre-declared retention rule. No accuracy-based route picking.
Expected output: A support-by-rank table that can move the score from 4 to 5 if the present three-graph result still holds.
Handoff required: yes
```

```text
Priority: 4
Action: Only if the target remains CVPR acceptance: pre-specify one flyvis-style or optic-lobe/Kenyon comparison and stratify its nulls by column support and rank, with failure cases.
Owner skill: ccf-experiment-designer
Input needed: A declared model and endpoint before fitting. This review does not authorize inventing that result.
Expected output: The only evidence package that would support overall 7.
Handoff required: yes
```

```text
Checks run:
PDF page count, page size, review header, anonymous author line, LLM statement placement, and absence of external links.
Full read of main.tex for prompt injection.
Ten-seed means, paired signs, and a 200,000-draw percentile bootstrap, seed 20261116, from executed-readout.json.
Three npz graphs: transfers, ranks, shared relays, 3072 edges, degree and module-pair identity, and the measured identity residual.
multiroute.json: replicate structure, open-draw identity, route means, and bitwise match of route 0 parity to the first six measured seeds.
one_column_digit.json means.
Structural replay of 24 degree-preserving draws, seeds 50_000+s, and of 12 protected rewires, seeds 80_000+100*i+s. No MLP retraining.
Abstract-level checks of Park, Dhiman, Correig-Fraga, Liu, Berg, and arXiv:2611.01213.
CVPR 2027 author, reviewer, and call pages for length, LLM statement, anonymity, external links, and topic list.
Checks skipped:
Retraining the MLP, including the 24-draw readouts and route 2 open_1.
Re-fetching Lappalainen, Dorkenwald, Maslov, Milo, GIN, PNA, GCN, and GraphSAGE full texts.
A second independent bootstrap seed. The 0.001 endpoint drift is reported only for seed 20261116 and 200,000 draws.
Official CVPR numeric score form, because the public reviewer page does not publish one.
Unresolved risks:
The bitwise copy of route 2 open_1's accuracy was not reproduced by a new training run. It is a property of the archived JSON.
Dual submission and reciprocal-reviewer eligibility cannot be judged from the manuscript.
Whether a both-support degree ensemble would agree with the separate-routes edit is untested.
```

## 17. Paragraph Review

IDs follow blank lines in `main.tex`. Line numbers are source lines.

| ID | Lines | Current role | Reviewer takeaway | Main problem | Concrete edit | Severity |
| --- | --- | --- | --- | --- | --- | --- |
| Abstract-P1 | 17–35 | Hook, claim, and all headline numbers in one paragraph | Degree matches miss column support, and the MLP follows support and rank | Number-led. Route scores 0.670, 0.675, 0.708 and the open 0.504 read as independent rewiring tests. The second 0.504 is rounded the wrong way | Rebuild around the certificate and Table 1. Label Section 5 as replicates. Print 0.503 | high |
| Intro-P1 | 48–56 | Motivation from four connectome comparisons | The verdict follows the control | None of fact at abstract level. The stakes name models this paper does not rerun | Keep, and point forward to the limited transfer in the discussion | medium |
| Intro-P2 | 58–65 | Gap | Degree, motif, and cost are not statements about the two-sink signal | Clean | Keep | low |
| Intro-P3 | 67–78 | Method map | One propagator, one subgraph, two edits, one unrestricted null | Accurate and dense | Keep. The route-search rule is enough | low |
| Intro-P4 | 80–83 | Claim | The MLP tracks column support, not the degree match and not the relay | Supported for this MLP. Easy to over-read | Keep the last sentence. Do not add a vision-wide claim | medium |
| Related-P1 | 90–98 | Positioning | This comparison holds the propagator fixed | Paraphrases match the checked abstracts, including Liu's flyvis phrase | Keep. Add the Park delta already used in the discussion if a sentence fits | low |
| Related-P2 | 100–106 | Operator gap | Mean aggregation's known degree shrinkage is not the question | The tasks are admitted to be constructed | Keep | low |
| Graph-P1 | 115–120 | Graph construction | 768 neurons, 3072 edges, four strongest incoming synapses | Clear | Keep | low |
| Graph-P2 | 122–129 | Route selection | First eligible relay, fixed before accuracy | Honest that it is not a named motion pathway | Keep | low |
| Prop-P1 | 136–151 | Propagator and \(T\) | Two averaging steps equal \(T\) on source-only features | The identity is checked on the measured graph. Training on \(T\) later makes equal-\(T\) graphs identical tests | Keep the math. Forward-reference the replicate consequence | medium |
| Prop-P2 | 153–159 | Support and rank | A zero column forces chance. Parallel columns are one direction | This is the paper's real definition | Keep | low |
| Edit-P1 | 166–171 | Edit mechanism | Module-preserving swaps hold degree and module counts | Clear | Keep | low |
| Edit-P2 | 173–195 | The three transfers | Printed matrices, ranks, and the empty shared-relay sets | Matches the npz files | Keep next to Table 1 | low |
| Ens-P1 | 219–226 | Unrestricted null | Ten swaps per edge, route unprotected, 24 draws | The paragraph already says the null is not asked to preserve either source | Keep that sentence adjacent to Figure 2 | medium |
| Task-P1 | 233–241 | Two XOR tasks | Subspace XOR and digit-parity XOR, plus how digits are projected | Constructed, and said to be constructed | Keep | low |
| Task-P2 | 243–250 | Training constants | MLP, linear control, seeds, bootstrap | Enough to rerun given \(T\). "Not paired at minibatch level" is easy to miss | Keep the constants. Name the bootstrap count next to every printed interval | low |
| Res-P1 | 259–264 | Subspace result | Both nonzero columns are enough. The deleted column falls to chance. The paired separate-versus-measured gap is small | The deleted-source interval's third decimal is unstable under a larger resample | Keep the scientific sentence. Regenerate the interval | medium |
| Res-P2 | 266–271 | Digit-parity result | Removing the shared relay beats the measured graph and the deletion | This is the rank result, on one edit, 10/10 seeds | Keep, with the one-edit scope | medium |
| Res-P3 | 273–276 | Linear control | Linear intervals sit near chance | "Between 0.493 and 0.516" is about intervals of means, not raw seeds | Qualify "intervals of the ten-seed means" | medium |
| Null-P1 | 294–299 | What 24 draws retain | 22 neither, 2 one, 0 both, and no module match | Replay confirms the counts. The inference in the paragraph is already the right one | Keep | low |
| Null-P2 | 301–305 | The module-matched pair as the real control | 0.746 versus 0.506 would have been one degree bin | Correct and decision-relevant | Keep. This should outrank the 24-draw story in the abstract | low |
| Mis-P1 | 312–316 | Three wrong summaries | Subspace means, motif count, and the degree null each mis-rank the graphs | Strong interpretation of existing numbers | Keep | low |
| Mis-P2 | 318–321 | Scope | One edit is not a claim that randomizing fly vision helps | The abstract does not carry this sentence | Move the scope sentence earlier | medium |
| Routes-P1 | 328–336 | Protected-route design | First three relays, edges protected, 42 to 57 edges in common, eleven transfers unchanged | The twelfth-draw disclosure is present and easy to skip. Overlap 42–57 was recomputed | Lead with "eleven draws repeat T" | high |
| Routes-P2 | 351–354 | Protected versus open parity | 0.670, 0.675, 0.708 versus 0.504 | 0.708 averages three copies and one changed draw. 0.504 should be 0.503. The six open vectors match bitwise | Replace with replicate language and 0.503 | high |
| Routes-P3 | 356–361 | Digit-class side task | One half is enough. The drop to 0.099 is loss of every input | Numbers match the JSON. The qualification is correct and should stay | Keep | low |
| Disc-P1 | 368–373 | Control principle | A both-input hypothesis needs a null that can carry both inputs. This unrestricted null cannot | Agrees with the replay. "Leave the parity readout where it was" still sounds like many distinct graphs | Say the protected condition repeated the measured T | high |
| Disc-P2 | 375–381 | Non-transfer | Dhiman, Correig-Fraga, and Liu use different operators. Only the reporting requirement transfers | Matches the checked abstracts. The requirement is not itself tested on those models | Keep | medium |
| Disc-P3 | 383–387 | Boundaries | Two neurons, an XOR, no optic-flow or Kenyon refit | This is the limitation that decides the venue score | Keep. Do not soften it | low |
| Disc-P4 | 389–393 | Closing | Equal degree sequences make the usual mean-shrinkage prediction silent. Support and rank are cheap to report | Fair for this evidence | Keep | low |
| LLM-P1 | 397–402 | Required statement | A generic coding assistant was used. Runs were local. Authors remain responsible | Meets the 2027 carve-out as far as the text shows | Keep | low |

## 18. Writing Scorecard

Writing score (1–5) = 3.51. Risk band: moderate. This is communication risk, not an acceptance probability.

Weights 10, 10, 10, 12, 9, 9, 8, 8, 10, 6, 8 sum to 100. Weighted sum: 4·10 + 3·10 + 4·10 + 3·12 + 4·9 + 3·9 + 4·8 + 4·8 + 3·10 + 4·6 + 3·8 = 351. Score = 351/100 = 3.51.

| Dimension | Weight | Score (1-5) | Confidence (1-5) | Evidence basis | Concrete repair |
| --- | ---: | ---: | ---: | --- | --- |
| Storyline and motivation | 10 | 4 | 4 | Intro-P2 then Intro-P4 then Table 1 | Keep the order. Move Misread-P2's scope sentence before the route numbers |
| Contribution display | 10 | 3 | 4 | Abstract-P1 lists scores before the contribution is one sentence | State one contribution: report support and rank of \(T\), because degree and module matches do not determine them. Location: Abstract-P1. Confusion: the paper sounds like a vision-performance result. Smallest edit: one contribution sentence before any score |
| Paragraph logic | 10 | 4 | 4 | Section 4 before Section 5; Null-P2 is the right control paragraph | Split Routes-P1 so the replicate count is its own sentence |
| Claim-evidence alignment | 12 | 3 | 5 | Routes-P2 versus multiroute.json | At Routes-P2, replace "0.504 on all six draws" with the single stored mean 0.503 and the identity of the six lists. At Abstract-P1, do not present 0.670, 0.675, and 0.708 as four-draw discoveries |
| Method readability | 9 | 4 | 4 | Equations (1) and (2) follow the graph section. Symbols are defined before use | Add one clause that equal \(T\) implies equal training inputs |
| Experiment narration | 9 | 3 | 4 | Res-P1 and Res-P2 interpret Table 1. Routes-P2 reports numbers without the dependence | Start Routes-P2 with what is identical, then the one draw that changed |
| Related-work positioning | 8 | 4 | 4 | Related-P1 and Disc-P1 compare operators and route signs | Keep the Park contrast on the route sign, not on a shared task |
| Terminology and notation consistency | 8 | 4 | 4 | Separate routes, deleted source, protected, and open stay stable. "Intervals" is the soft term | Use "bootstrap interval of the ten-seed mean" at Res-P3 |
| Prose discipline and voice | 10 | 3 | 4 | Abstract-P1 is number-led. The body is otherwise direct and not hype-heavy | Rebuild the abstract in the order task, gap, certificate, three-graph evidence, limit. Leave the body voice |
| LaTeX and format discipline | 6 | 4 | 4 | Review class, booktabs, captions, labels, and bibliography resolve in the PDF | No blocking format defect. Figure endpoints should not be literals disconnected from the JSON |
| Reviewer-facing risk | 8 | 3 | 4 | Abstract-P1 plus Routes-P2 create an independent-ensemble reading the archive does not support | The smallest edit is the replicate sentence. It removes an avoidable rejection that is about over-counting, not about Table 1 |

Scores of 3 in this card: contribution display, claim-evidence alignment, experiment narration, prose, and reviewer-facing risk. Each row above names the location, the confusion, and the smallest edit. None of those edits, alone, moves the scientific overall score to 7.

## 19. Writing Panel

```text
Role: Storyline reviewer
Writing score tendency: 4
Confidence: 4
Main readability gain: Problem, gap, certificate, three graphs, and limits appear in that order.
Main reviewer-confusion risk: The abstract's route numbers arrive before the reader knows they are replicates.
Evidence basis: Abstract-P1 against Routes-P1.
Concrete edit: Move the replicate clause ahead of 0.670, 0.675, and 0.708.
Expected score movement: storyline stays 4. Reviewer-facing risk can rise to 4.
```

```text
Role: Skeptical reviewer-reader
Writing score tendency: 3
Confidence: 4
Main readability gain: Disc-P3 is more careful than the abstract.
Main reviewer-confusion risk: A skeptical reader will think Section 5 tested many wirings and will then find eleven identical transfers.
Evidence basis: Abstract-P1; multiroute.json.
Concrete edit: Use the word replicates in the abstract and in Routes-P2.
Expected score movement: this role moves to 4 only after that wording. Overall scientific score does not.
```

```text
Role: Claim-evidence reviewer
Writing score tendency: 3
Confidence: 5
Main readability gain: Table 1, Res-P1, and Res-P2 agree with the ten-seed file.
Main reviewer-confusion risk: The open-route 0.504 does not agree with 0.503499, and six lists are one list.
Evidence basis: Section 8.
Concrete edit: Correct the thousandth and the independence claim. Do not weaken Table 1.
Expected score movement: claim-evidence alignment 3 to 4. Overall +1 still needs the ensemble.
```

```text
Role: Paragraph-logic reviewer
Writing score tendency: 4
Confidence: 4
Main readability gain: Most paragraphs have one job. Null-P1's inference follows its count.
Main reviewer-confusion risk: Routes-P1 mixes design, overlap, and the twelfth draw. Disc-P1 then restates the protected result as if the draws were distinct.
Evidence basis: Routes-P1; Disc-P1.
Concrete edit: One sentence for design, one for the eleven copies, one for the changed entry.
Expected score movement: paragraph logic can reach 5 locally. No overall change.
```

```text
Role: Venue-style reviewer
Writing score tendency: 3
Confidence: 4
Main readability gain: The contribution is visible once the reader reaches Intro-P4 and Table 1.
Main reviewer-confusion risk: CVPR readers expect the first page to say what visual conclusion changed. This first page says the control changed.
Evidence basis: Intro-P1; Disc-P2.
Concrete edit: On the first page, say the evidence is the certificate on one subgraph, not a new flyvis ranking.
Expected score movement: contribution display 3 to 4. Significance stays 3.
```

```text
Role: LaTeX/format reviewer
Writing score tendency: 4
Confidence: 4
Main readability gain: The PDF is in review mode, within eight pages, with a visible LLM statement and resolved citations.
Main reviewer-confusion risk: Figure error bars cannot be traced to a command that reads the JSON.
Evidence basis: make_figures.py literals; six-page letter PDF.
Concrete edit: Generate the bars from the stored means and a stated bootstrap.
Expected score movement: format stays 4. Reproducibility can rise if the archive exists.
```

Writing-panel synthesis: the body is clearer than the abstract. No role found a format failure or a novelty collapse created by the prose. The shared writing defect is over-counting repeated transfers. Fixing it removes a bad objection and does not create an accept case.

## 20. Format Audit

```text
Format verdict: pass on the 2027 checks that can be made from the PDF and source. Not compiled in this review. The existing PDF was inspected.
Blocking compliance issues: none found.
LaTeX/source issues: \documentclass[10pt,twocolumn,letterpaper]{article} with \usepackage[review]{cvpr}. paperID is *****. confYear is 2027. No unfinished marker or empty citation in the source, and no undefined-reference marker. The PDF shows line numbers and the confidential review header.
Figure/table/caption issues: Table 1, Figure 1, Figure 2, and Figure 3 are referenced. Captions name the claim. Figure 1 and Figure 2 values are hardcoded in make_figures.py. Table 1 has no interval column, so the unstable third decimals live only in the prose.
Citation/reference issues: Citation keys in the tex resolve in the PDF. No external URL. Nature, Science, and GNN entries were not re-fetched. No MDPI entries.
Notation/equation issues: W and T are defined before the edits use them. rank(T) is consistent. The linear-interval sentence should say "of the means."
Suggested checks or build command: not recompiled here. A submission check can rebuild main.tex with the review class and confirm the PDF remains at or under eight content pages.
```

## 21. Revision Actions

These are handoffs, not a rewrite performed in this review.

| Priority | Class | Action | Where | Risk reduced |
| --- | --- | --- | --- | --- |
| 1 | Claim-qualification | Say protected draws with equal \(T\) are replicates, and separate the one changed entry | Abstract-P1, Routes-P1, Routes-P2, Disc-P1 | Over-counted ensemble |
| 2 | Claim-qualification | Replace open-route 0.504 with 0.503 and state that the six lists are one vector | Abstract-P1, Routes-P2 | Wrong thousandth and false independence |
| 3 | Prose-quality | Rewrite the abstract in the order certificate, three-graph result, limit, then only the numbers that survive | Abstract-P1 | Number-led first page |
| 4 | Reproducibility | Archive the 24 draws and rebuild the figure endpoints from the seed file | Figure 1, Figure 2, supplement | Unauditable bars |
| 5 | Requires-new-result | Both-columns-retained degree ensemble, rank recorded, ten-seed MLP | New table | Overall 4 to 5, if the current pattern holds |
| 6 | Requires-new-result | One pre-specified visual comparison, stratified nulls, failure cases, released records | New experiment | Overall 7 only if that result exists |
| 7 | Accepted-limitation | Until item 6 exists, keep Disc-P2 and Disc-P3 as firm limits | Discussion | A reviewer treating advice as a transferred result |

## 22. Output Self-Check

Section order 1–16 is intact, with writing, format, and revision annexes after them. Tables use a consistent column count. Overall 4 is the AC score, not the mean of the best-justified 5 and the critical 3. Every scientific score of 3 has a deduction and a repair. The writing score 3.51 uses the stated weights. No acceptance probability is stated. No rebuttal text is included. No citation was invented: unchecked classics are marked unchecked. The open-route rounding error is separated from the correctly rounded Table 1 value 0.504.

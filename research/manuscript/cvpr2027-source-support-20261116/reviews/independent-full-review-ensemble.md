# Independent Full Review

## 1. Report Metadata

```text
Review date: 2026-11-16
Target venue/year/track: CVPR 2027 main conference
Paper title: A Degree Match Does Not Keep Both Inputs
Input materials reviewed: main.tex (402 lines); main.pdf (6 pages, letter, anonymous review mode, paper ID *****); main.log; references.bib (13 entries); figures/transfer_readout.pdf, figures/degree_support.pdf, figures/ensemble.pdf; executed-readout.json; conditioned_ensemble.json; support_sweep.json; degree24.json; multiroute.json; one_column_digit.json; make_figures.py
Search basis: CVPR 2027 author guidelines; manuscript bibliography checked against public records for Dhiman (arXiv:2604.04033), Park (arXiv:2609.39248), Liu (arXiv:2611.14508), Correig-Fraga (arXiv:2610.10023), Berg et al. (Cell 2026), Lappalainen et al. (Nature 2024), Dorkenwald et al. (Nature 2024), Maslov and Sneppen (2002), Milo et al. (2002); additional search for a source-column certificate under two-step mean aggregation and for Lin et al., Nature 2024
Report file: /Users/xhf/Downloads/phd/4090/cvpr2027-rebuild/manuscript/source-support-20261116/reviews/independent-full-review-ensemble.md
Reviewer mode: full independent review; manuscript not rewritten; no rebuttal
```

This review did not open the other reviews in the same folder. Line numbers below are from `main.tex`.

## 2. Desk Rejection Assessment

```text
Check: Paper length
Status: pass
Evidence: pdfinfo and main.log both report 6 pages. Body, three figures, and Table 1 end on page 5. Page 6 is the LLM Usage Statement and the references. CVPR 2027 allows 8 pages for the body; references and the mandatory LLM statement sit outside that count.
Consequence: none
Required action: none for length
```

```text
Check: Topic compatibility
Status: pass
Evidence: The paper studies a visual subgraph of a fly connectome, a graph propagator, and readouts of constructed visual tasks. That is in scope for a vision conference. The evaluation is not a standard vision benchmark, which is a review issue rather than an administrative one.
Consequence: not a desk reject
Required action: none before review
```

```text
Check: Minimum quality
Status: pass
Evidence: Method, one table, three figures, a related-work contrast, numerical results, and an explicit boundary on what is not claimed are all present. There is no Conclusion heading; the Discussion is the closing section.
Consequence: reviewable
Required action: none
```

```text
Check: Policy / anonymity / compliance
Status: uncertain
Evidence: Review mode, \author{Anonymous} at line 15, empty PDF author metadata, no affiliation, URL, acknowledgment, or external link. The LLM Usage Statement (lines 390–395) names the affected work and says a non-public assistant configuration would identify the authors, so the tool name stays generic. CVPR 2027 asks the statement to name the tools and the affected parts while remaining anonymous.
Consequence: not a desk reject on the inspected PDF; a policy reader could ask for a public product name that does not identify a private configuration
Required action: if the venue office requires a name, use a public product name only
```

```text
Check: Prompt injection and hidden manipulation detection
Status: pass
Evidence: Source, captions, bibliography, and the LLM statement were read as manuscript content. No hidden instruction to a reviewer or model was found.
Consequence: none
Required action: none
```

```text
Check: Ethics and reviewability
Status: pass
Evidence: The data are a published connectome annotation and a standard digits set. No human subjects. Limitations are stated in the discussion. Local JSON files support the printed means. main.log contains no Overfull box warning.
Consequence: none at desk-reject level
Required action: none
```

```text
Desk rejection risk: low
Reason: Length, anonymity, template, and the presence of an LLM statement pass. The only compliance uncertainty is that the statement does not name the tool.
Can be fixed before review? partly
```

```text
Venue: CVPR 2027
Venue family: CVPR / ICCV / ECCV
Primary scoring dimensions: novelty, technical quality, empirical validation, visual evidence, clarity, fair comparison
Evidence package expected: a vision-relevant comparison, inspectable figures, ablations, and a claim that changes how a vision result is read
Likely reviewer taste: reward a crisp diagnostic result, but expect it to land on a visual model or benchmark a CVPR reader recognizes
Likely AC concern: the certificate is real and carefully bounded, yet it is one sparsified route and two constructed XORs
Biggest mismatch risk: a methods note about null-graph reporting presented as a main-track vision paper
Writing moves that improve fit: lead with the reporting rule and the rank split, and show that the same certificate changes a published connectome-vision comparison
```

## 3. Paper Summary And Contribution Map

The paper takes one 768-neuron, 3,072-edge visual subgraph of the male fly central nervous system, keeps the four strongest incoming synapses at each neuron, and applies incoming-neighbor averaging twice. The object of study is the resulting 2×2 source-to-sink transfer \(T\). Two constructed XOR tasks, a subspace code and digit parity, are read by a 32–64–1 MLP and by a linear control. Degree, motif, and module matches do not say whether both sources still reach the sinks, or whether the two columns are independent. A long degree-preserving null deletes the source columns. At 307 swaps, digit parity splits by \(\operatorname{rank}(T)\).

Claimed problem. Connectome-constrained vision models are compared with nulls that match degree, motif count, or wiring cost. Under one stated propagator, those matches are not statements about the signal at a chosen pair of sinks (lines 21–22 and 52).

Claimed gap. Prior work shows that the control changes the verdict, but it does not isolate source-column support and column rank for two-step mean aggregation (lines 84–91).

Method and contribution map.

- Define \(W\) by incoming-neighbor averaging and \(T = R_S W^2 E_{ab}\).
- Fix one relay by a deterministic search before any accuracy is computed: sources 6 and 109, sinks 4 and 5, shared relay 9 (lines 115–116).
- Compare the measured graph with two module-matched edits that share degree, module-pair counts, edge count, and an empty shared-relay set. One has rank 2; the other deletes a column (Table 1, lines 180–196).
- Run a degree-preserving ensemble at ten swaps per edge, then a budget sweep, and read digit parity at the shortest budget that still keeps both columns in at least 8 of 12 draws while changing at least half the transfers (lines 328–329).

Evidence package. Ten seeds (11, 17, 23, 31, 41, 53, 67, 79, 97, 103) for the three named graphs; 24 long rewires; 12 draws at each of seven budgets; a protected-route check on three relays using six of those seeds; a digit-class side comparison. The audited JSON files match the headline means, the support counts, and the 307-swap rank clusters.

Stated limitations. The subgraph is small, the tasks are constructed, the route is not a named motion pathway, one half of a digit still supports digit class, and the result does not refit flyvis or an eye-to-Kenyon model and does not overturn those papers (lines 92, 113, 302–304, 370–382). The operator is not their operator.

## 4. Search And Related-Work Basis

```text
Queries used: CVPR 2027 author guidelines and LLM usage statement; the manuscript's citation keys for flyvis, the male CNS connectome, degree-preserving rewiring, motifs, GNN aggregators, and the 2026 connectome-null papers; source-column support under neighbor averaging; configuration-model nulls on the Drosophila whole-brain connectome
Sources searched: CVPR 2027 author guidelines page; arXiv records and journal landing pages for the cited 2024–2026 connectome papers; Nature record for Lin, Scheffer, et al. on whole-brain network statistics
Closest works found: Park, arXiv:2609.39248, on degree-preserving swaps and one-step olfactory-to-descending shortcuts; Dhiman, arXiv:2604.04033, on shared initialization and degree-preserving nulls in a flyvis-style mask; Liu, arXiv:2611.14508, on physiology-assignment protocols; Correig-Fraga, arXiv:2610.10023, on a connectome-only eye-to-Kenyon comparison at matched cost; Lin et al., Nature 2024, "Network statistics of the whole-brain connectome of Drosophila," which uses configuration-model and neuropil-preserving degree nulls
Unverified related-work risks: no public paper found that reports this exact source-column certificate for two-step mean aggregation on this route; absence of an exact match is not a proof that none exists outside the searched records
Source-quality screening status: the named citations used for the scientific contrast were located and match the manuscript's description of their operators; Lin is a real missing comparator and was not invented for this review
```

The novelty that survives that search is narrow. The paper asks what a degree null does to both inputs under one propagator, and it separates column support from column rank. Park is the closest conceptual neighbor. Dhiman's null uses a masked product, not neighbor averaging, which is what lines 80–81 say.

## 5. Expected Review Outcome

```text
Expected outcome: weak reject
Main accept signal: the internal claim is scoped to one propagator and one route, the three named transfers are separated by support and rank, and the printed means and support counts match the local runs
Main reject signal: for a CVPR main-track paper, the result does not change a vision benchmark or a published connectome-vision comparison, and the rank split at 307 swaps is carried by three unique rank-2 maps
Confidence: 4/5
```

Confidence is 4 rather than 5 because the graph was not reconstructed from the connectome in this review, the \(3\times 10^{-8}\) identity was not in the audited JSON, and the hand-edit degree and module flags in Table 1 were not stored as fields in those files. The manuscript, the JSON artifacts, the PDF, the log, and the public sources that were checked were sufficient to score the claim as written.

## 6. Strengths And Weaknesses

Strengths.

- The paper says what would falsify a degree-only reading. Separate routes and deleted source are described as matches on degree, module-pair counts, and edge count, and they do not match accuracy (Table 1; lines 239–249).
- The linear control is the right negative control for an XOR. Its bootstrap intervals sit at chance, so the MLP split is not a linear decoding of \(T\) (lines 253–255).
- The long null is interpreted correctly. The text says that a comparison against ten swaps per edge contrasts a graph that carries both inputs with a graph that does not (lines 275–279 and 357–366).
- The discussion refuses the overclaim a reader might want. Removing the shared relay on this route is not a claim that randomizing fly visual synapses improves vision (lines 302–303), and Equation (1) is not the flyvis or Kenyon operator (lines 370–376).
- Training and evaluation details are concrete: architecture, optimizer, learning rate, epoch and batch counts, seeds, pairing rule, and bootstrap definition (lines 222–229).

```text
Weakness: The result is a case study of one sparsified route under one aggregator, and the paper does not show that the certificate changes a CVPR-relevant vision comparison.
Evidence basis: One 768-neuron subgraph, four strongest incoming synapses, two XOR tasks built so that support and rank matter, and an explicit statement that an optic-flow model and an eye-to-Kenyon model were not refit (lines 370–382; abstract lines 21–23).
Reviewer deduction: Significance 2/5. A careful diagnostic on one route can be correct and still be below the main-track bar.
Required fix: Apply the same support and rank stratification to at least several routes or a population readout, and show that the certificate changes an actual connectome-vision comparison.
```

```text
Weakness: The rank split that carries the new claim is thin.
Evidence basis: At 307 swaps, five rank-2 draws score between 0.715 and 0.727, but two transfers occur twice, so those five scores are three maps, at 0.715, 0.722, and 0.727 (lines 330–337). Twelve draws is the whole ensemble at that budget. Digit class remains high from either half or from one column (lines 343–345).
Reviewer deduction: Evidence 3/5. The separation is consistent inside this draw, but it is not yet a stable population result.
Required fix: More unique transfers, a pre-specified budget rule, and a readout whose label is not constructed to make rank the only degree of freedom.
```

```text
Weakness: The usual long null cannot support a "beyond degree" claim, and the paper's title is the long-null sentence.
Evidence basis: None of 24 draws at \(10\times 3072\) swaps retains both columns (lines 202–204 and 275–279; Figure 2). The title says a degree match does not keep both inputs. The sharper result is the other regime: at 307 swaps both inputs usually remain, and rank, not degree, orders digit parity (lines 360–363).
Reviewer deduction: Originality 3/5. The deletion result is the prediction of a zero column, which lines 142–144 already state.
Required fix: Retitle and re-lead around the short-budget rank split, and treat the long null as the reason an unstratified control is uninterpretable.
```

```text
Weakness: Two printed interval endpoints do not match a fixed 5,000-resample bootstrap, and several structural claims are not in the audited files.
Evidence basis: Under rule R (numpy Generator seed 20261116, 5,000 resamples, linear 2.5/97.5 percentiles, half-up to three decimals), the deleted-subspace interval prints as [0.495, 0.514] and recomputes as [0.495, 0.515], and the digit separate-minus-measured interval prints as [0.072, 0.094] and recomputes as [0.073, 0.094]. The \(3\times 10^{-8}\) identity, the node indices, and the hand-edit degree and module flags are not fields in the audited JSON.
Reviewer deduction: Reproducibility 3/5. The gaps do not flip. A reader still cannot regenerate every printed endpoint, or every Table 1 structural cell, from the files alone.
Required fix: Publish the graph, the swap seeds, the bootstrap seed, and the module-pair counts. Print intervals from one stored resample.
```

## 7. Potentially Missing Related Work

```text
Work: Lin et al., Nature 2024, "Network statistics of the whole-brain connectome of Drosophila"
Status: searched
Why relevant: It is a connectome statistics paper that already treats configuration-model and neuropil-preserving degree nulls as scientific objects, on the same animal.
Overlap: Degree-preserving randomization of Drosophila wiring. It does not study this visual route, this mean aggregator, or this XOR.
Needed comparison: One paragraph stating what those nulls preserve, and why source-column support of \(W^2\) is a different certificate from a neuropil-preserving degree sequence.
```

```text
Work: Park, arXiv:2609.39248
Status: searched
Why relevant: Closest prior result. Degree-preserving swaps add routes the measured graph does not have, and those routes decide a comparison.
Overlap: The manuscript already uses this contrast (lines 364–366). Park's direction is added shortcuts; this paper's long null removes two-hop inputs.
Needed comparison: No additional experiment is required for fairness. The citation is used for the right claim.
```

```text
Work: Dhiman, arXiv:2604.04033; Liu, arXiv:2611.14508; Correig-Fraga, arXiv:2610.10023
Status: searched
Why relevant: These are the published connectome-vision and connectome-learning comparisons a CVPR reader will expect the certificate to touch.
Overlap: The manuscript correctly refuses a direct numerical comparison because the operators differ (lines 370–376).
Needed comparison: Not a forced rerun for soundness. A rerun, or a re-read of one published endpoint under this certificate, is what would make the paper significant for this venue.
```

No searched paper was found that reports this exact two-column certificate for two-step incoming-neighbor averaging. That absence supports a narrow novelty claim. It does not support a broad claim about connectome vision.

## 8. Claim-Evidence Audit

| Claim | Where stated | Evidence provided | Strength | Reviewer deduction | Required fix |
| --- | --- | --- | --- | --- | --- |
| Degree, motif, and module matches do not say whether both inputs reach the readout or whether they arrive as two directions | Lines 21–22 and 52 | Separate-routes \(T\) is rank 2 and deleted-source \(T\) is a zero column; the text says both edits match degree and module counts (Table 1) | strong for the two printed transfers; the hand-edit degree and module cells are not stored in the audited JSON | do not treat the Table 1 "yes" cells as recomputed | archive the degree vectors and module histograms of the two hand edits |
| The same MLP scores 0.979 and 0.746 on separate routes, 0.504 and 0.506 on the deleted source, and 0.976 / 0.663 on the measured graph | Lines 27–28; Table 1; lines 239–246 | executed-readout.json means round half-up to these three-decimal values on seeds 11–103 | strong | none for the means | store the bootstrap seed so the intervals are unique |
| A linear readout stays at chance, with intervals between 0.493 and 0.516 | Lines 29 and 253 | Under rule R the six linear intervals span 0.4939453125 to 0.51591796875 | adequate as a statement about bootstrap intervals | false for raw seed scores, which span 0.47265625 to 0.53857421875 | say "bootstrap intervals" |
| The usual null, ten swaps per edge, retains both columns in none of 24 draws; 22 retain neither and 2 retain one | Lines 30, 275–279 | degree24.json: 24/24 degree matches, 0/24 module matches, 0 both, 22 neither, 2 one; seeds 50000–50023; 30720 swaps | strong | "usual" is not given a citation | cite the mixing convention or drop "usual" |
| At 307 swaps, 11 of 12 draws keep both columns, and digit parity follows rank: 0.715–0.727 versus 0.646–0.673, with the deleted column at 0.506 | Lines 31–33 and 330–337; Figure 3 | support_sweep.json and conditioned_ensemble.json match the counts and the rank clusters; five rank-2 scores are three maps, and each of those maps is above every rank-1 map | adequate inside the draw; weak as a general law | Evidence deduction: three unique rank-2 maps | report the number of unique transfers in the abstract |
| Both-column survival is 11, 11, 4, 0, 1, 0, 0 at the seven budgets, and 307 is the selected length | Lines 323–329 | Counts match. 154 has 6/12 identical transfers, so it fails "fewer than half." Only the 0.1 multiplier (307 swaps) passes | strong | the rule is stated with the curve | pre-specify the rule or call it a selection on the archived curve |
| The maximum absolute deviation of the \(W^2\) identity is \(3\times 10^{-8}\) | Line 137 | stated; not present in the inspected JSON | absent from the artifact set | do not treat it as independently checked | store the batch deviation |
| Keeping the biological relay is better than losing an input and worse than independent routes | Line 250 | paired digit gaps +0.083, +0.239, and +0.156, each on 10 of 10 seeds | strong for this MLP and this route | easy to read as a biological claim | the later caveat already blocks that reading; keep it adjacent |
| One half of the digit is enough for most of the digit-class task | Lines 343–345 | Six-seed class means round to 0.959, 0.939, 0.985, 0.099, 0.940, 0.895, and 0.878 | strong as a caveat | this also shows the task family is elastic | do not let parity be described as a generic visual test |
| The reporting requirement transfers to flyvis, Kenyon-cell, and physiology-assignment results | Lines 370–376 | argued by operator mismatch, not by a rerun | weak as an empirical transfer; adequate as a caution | Significance deduction if read as a new verdict on those models | keep the sentence as a reporting recommendation, which the text already does |
| Deleted-subspace interval [0.495, 0.514] and digit separate-minus-measured interval [0.072, 0.094] | Lines 242 and 247 | rule R gives [0.495, 0.515] and [0.073, 0.094]; the printed digits match hardcoded Figure 1 literals, including upper endpoint 0.5141 | weak as a unique bootstrap; the 0.001 gap does not change the result | Reproducibility deduction only | print the interval from a named seed |

## 9. Experiment / Benchmark / Reproducibility Audit

Baselines. The measured graph is the only biological condition. The two edits are said to be matched on degree, module-pair histogram, and edge count. Those structural flags for the hand edits are not fields in the audited JSON, so they were not recomputed here. The degree-preserving swap is the external null, attributed to Maslov and Sneppen. There is no second aggregator, no GCN normalization, no learned flyvis mask, and no cost-matched eye-to-Kenyon graph. That absence is acceptable only because the discussion does not claim those comparisons.

Ablations. Linear versus MLP separates the XOR from a linear image of \(T\). Support versus deletion separates chance from above-chance subspace accuracy. Rank separates the 307-swap digit scores. Digit class shows that a weaker label does not need both independent columns. Protected edges show that freezing the two-hop route mostly reproduces \(T\). These are the right ablations for the claim. They are not ablations of the sparsification, the neuron count, the four-synapse cap, or the two-step depth.

Datasets and benchmarks. The subspace task uses frozen random 8-dimensional subspaces of a 16-dimensional code. Digit parity uses scikit-learn digits, a frozen QR projection, and the XOR of upper-half and lower-half parity. Neither is a vision benchmark. The label is not the digit class, except in the side experiment. That side experiment, and the protected-route means, use six seeds (11, 17, 23, 31, 41, 53). Table 1 and the 307-swap panel use ten. The manuscript says "six seed scores" for the open-draw chance vector and does not say six for the digit-class sentence. The values still match.

Metrics. Accuracy on 2,048 fresh samples. Paired differences are paired by seed, not by minibatch. Intervals are percentile bootstrap intervals over ten seed scores, 5,000 resamples. No bootstrap seed is stated.

Statistical rigor. Ten seeds is small but fully reported, and the large gaps are unanimous: separate versus deleted is positive on 10 of 10 seeds for both tasks, and the digit separate-versus-measured gap is positive on 10 of 10. The subspace separate-versus-measured gap is +0.003 with 6 of 10 seeds positive and 4 negative, and the paper says six are positive. The 307-swap rank split has no seed interval per draw in the prose. The range is across draws, and shared transfers share scores, which the Figure 3 caption states.

The ten-seed means in executed-readout.json round half-up to every headline mean in Table 1:

- subspace measured 0.9763671875 to 0.976; separate 0.978955078125 to 0.979; deleted 0.503759765625 to 0.504
- digit measured 0.66259765625 to 0.663; separate 0.745849609375 to 0.746; deleted 0.506494140625 to 0.506

Paired differences likewise match: subspace separate minus measured +0.002587890625 to +0.003 (6 of 10); subspace separate minus deleted +0.4751953125 to +0.475 (10 of 10); digit separate minus measured +0.083251953125 to +0.083 (10 of 10); digit separate minus deleted +0.23935546875 to +0.239 (10 of 10); digit measured minus deleted +0.156103515625 to +0.156 (10 of 10).

Rule R fixes the bootstrap that the manuscript leaves unfixed: `numpy.random.Generator` seed 20261116, 5,000 resamples, linear 2.5 and 97.5 percent quantiles, half-up to three decimals. That seed is the QR seed in the multiroute script. It is not stated in the paper, so another seed can move the last displayed digit. Under rule R, the following printed intervals match: subspace measured [0.971, 0.980], subspace separate [0.974, 0.984], subspace paired difference [-0.001, 0.007], subspace separate-minus-deleted [0.461, 0.488], digit measured [0.653, 0.673], digit separate [0.741, 0.751], digit deleted [0.500, 0.515], digit separate-minus-deleted [0.232, 0.246], and digit measured-minus-deleted [0.141, 0.170].

Two endpoints do not match rule R.

- Deleted subspace is printed as [0.495, 0.514]. Rule R is [0.494676513671875, 0.514649658203125], which rounds to [0.495, 0.515]. The absolute gap on the upper endpoint is 0.00065.
- Digit separate minus measured is printed as [0.072, 0.094]. Rule R is [0.073045654296875, 0.093701171875], which rounds to [0.073, 0.094]. The absolute gap on the lower endpoint is 0.00105.

Both mismatches are seed-sensitive. A 5,000-draw seed 16 rounds the deleted-subspace interval to the printed pair, and seeds 0 and 1 round the digit paired lower endpoint to 0.072. No seed from 0 through 1999 reproduced all six hardcoded four-decimal Figure 1 intervals at once. The manuscript prints the rounding of those literals, including a deleted-source upper endpoint of 0.5141. Regenerating the figure from the JSON without the literals would move that printed digit. A 200,000-draw bootstrap, which the paper does not claim, also moves the deleted-subspace endpoints and the digit measured-minus-deleted lower endpoint by about 0.001. None of this changes a gap or a sign.

The linear sentence is true for the rule R envelope and false for the raw linear scores. The two printed 0.506 digit means are different lists: the 307-swap deleted column is 0.506103515625 and the deleted-source anchor is 0.506494140625. Both round to 0.506. That is not a rounding error.

conditioned_ensemble.json uses the same ten seeds. Its 12 draws copy the 307-swap rows of the sweep, including transfer, rank, support, and whether the transfer equals the measured one. Rank-2 means are 0.722412109375 twice, 0.71513671875 twice, and 0.726806640625 once. Rank-1 both-column means run from 0.646435546875 to 0.673193359375. Every rank-2 map is above every rank-1 map. Anchors reproduce 0.746, 0.506, and measured 0.663.

support_sweep.json has 84 rows, 12 at each of 7 budgets. Swap counts are 154, 307, 768, 1536, 3072, 6144, and 30720. Both-column counts are 11, 11, 4, 0, 1, 0, 0. All 84 match both degree vectors. At 307 swaps, 11 draws keep both columns, 5 have rank 2, 6 have rank 1, 3 of those rank-1 draws copy the measured transfer, and the remaining draw deletes a column. The selection rule uniquely selects 307. The file does not carry a module-pair field. Lines 325–326, read as a statement about the 24-draw archive, match degree24.json. Read as a statement about all 84 sweep rows, the module half is unverified.

degree24.json is not the same sample as the 12-draw row at 30720 swaps in the sweep. That sweep row has 10 draws with no source and 2 with one. The 24-draw archive has 22 and 2. The paper's 22-and-2 sentence is the archive, and it matches. Figure 2 matches that archive.

multiroute.json uses six seeds. Eleven of 12 protected draws reproduce the measured transfer of their own route. The exception is route index 2, graph `protected_2`: one entry moves from 0.0625 to 0.125, and parity moves from 0.7098795572916666 to 0.700439453125, which round to 0.710 and 0.700. In file order that exception is protected draw 11 of 12. The 12th protected draw copies the measured transfer. The sentence "the twelfth" (line 314) is therefore not a file index. Six open draws all score 0.5034993489583334, which rounds to 0.503. Five transfers are zero. Route 2 `open_1` keeps one column and the same six scores.

one_column_digit.json and the route digit-class means round to the printed 0.959, 0.939, 0.985, 0.099, 0.940, 0.895, and 0.878.

Robustness and failure cases. The deleted column is the failure case, and it falls to chance on both XORs. Digit class does not fail when one column remains. The paper reports that limit, which is the right use of the side task. There is no noise model, no second connectome, and no second species.

Implementation. Adam, learning rate 0.006, binary cross-entropy with logits, 120 epochs of 32 batches of size 128, evaluation on 2,048 samples, PyTorch 2.13 on Apple MPS. The route rule is deterministic in node order. Body identifiers are said to be stored with the graph files and are not printed. This review did not reopen them. Node indices 6, 109, 4, 5, and relay 9 are not fields in the audited JSON.

Artifacts. The JSON files are sufficient to audit the printed scores and the support counts. They are not a public code release. No script in the rebuild tree writes `ensemble.pdf`; `make_figures.py` writes the other two figures and hardcodes the Figure 1 interval endpoints. Figure 3's plotted fractions and marker heights match the sweep and the conditioned means. The largest marker gap is about \(5\times 10^{-6}\), consistent with reading coordinates off the axis. The log-scaled tick labels 1.5k, 3k, 6k, and 31k are not the exact counts 1536, 3072, 6144, and 30720. `routes.pdf` is not included. `ensemble.png` says "Draws" where the included PDF says "Fraction." `main.log` reports a 6-page PDF and does not report an Overfull box. `cvpr.sty` can still suppress small overfull warnings, so the clean log is not a full typography proof.

Limitations in the manuscript match the evidence. They should stay next to the claim, as they already do.

## 10. Multi-Reviewer Panel

```text
Reviewer: Best-justified
Expertise: connectome controls and graph readouts
Likely score: 5/10
Confidence: 4/5
Main positive signal: The paper isolates a certificate that degree and module matches do not provide, and it refuses to treat a deleted column as a wiring result.
Main negative signal: The certificate is demonstrated on one constructed route.
Evidence basis: Table 1, the unanimous paired gaps, and lines 357–382.
Fatal concern if any: none
Score-change condition: A second real visual comparison, stratified by the same support and rank, would move this reviewer to a weak accept.
```

```text
Reviewer: Critical
Expertise: CVPR empirical standards
Likely score: 3/10
Confidence: 4/5
Main positive signal: The arithmetic is careful and the overclaim is already blocked.
Main negative signal: There is no vision benchmark, no published-result consequence, and the new split is three rank-2 maps in twelve draws.
Evidence basis: Sections 3–5 and the discussion's own refusal to refit flyvis or the Kenyon model (lines 370–382).
Fatal concern if any: none technically; the venue gap is major
Score-change condition: This score rises only if the certificate changes a result a vision reviewer already cares about. More prose will not do it.
```

```text
Reviewer: Method / Soundness
Expertise: graph operators and causal reading of nulls
Likely score: 5/10
Confidence: 4/5
Main positive signal: \(W\), \(T\), rank, and the zero-column Bayes argument are the right objects, and the long null is not misread as a degree effect.
Main negative signal: Training uses \(T\) rather than the full 768-dimensional multiplication, and the \(3\times 10^{-8}\) check was not in the audited files. The route is the first search hit, not a visual pathway.
Evidence basis: Equations (1)–(2); lines 137–144; route rule at lines 110–116.
Fatal concern if any: none
Score-change condition: An independent full-graph check on held-out batches, plus one alternate propagator with the same degree sequence, would make the mechanism broader without changing the logic.
```

```text
Reviewer: Evidence / Experiment
Expertise: experimental design
Likely score: 4/10
Confidence: 4/5
Main positive signal: Seeds, pairing, chance baseline, linear control, and the support curve are reported, and the JSON matches the means and the counts.
Main negative signal: The tasks are built so the certificate matters. Digit class is solvable from one half. The rank result has three unique positive maps.
Evidence basis: Lines 213–229 and 330–345; conditioned_ensemble.json.
Fatal concern if any: none
Score-change condition: Unique transfers from a pre-specified budget, on more than one route, with intervals, would repair the evidence score even before a flyvis rerun.
```

```text
Reviewer: Novelty / Positioning
Expertise: connectome statistics and graph neural network aggregators
Likely score: 4/10
Confidence: 4/5
Main positive signal: The delta from Park and Dhiman is real. This null is asked what it does to both inputs under neighbor averaging, not whether it adds a shortcut or closes an activity gap.
Main negative signal: Mean aggregation is standard, degree-preserving swaps are standard, and Lin et al. already makes degree nulls a connectome-statistics question.
Evidence basis: Related work lines 76–91; search notes in Section 4 of this review.
Fatal concern if any: none; novelty does not collapse
Score-change condition: Positioning against Lin, and a title that states rank rather than only column loss, would repair the novelty presentation. The score moves by a point only with a broader empirical consequence.
```

```text
Reviewer: Writing / Clarity
Expertise: reviewer readability
Likely score: 5/10
Confidence: 5/5
Main positive signal: A careful reader can recover the claim, the operator, the control, and the boundary in one pass.
Main negative signal: The abstract is a stack of numbers, the title answers only the long-null question, and line 72 names support while lines 330–337 and 382 name rank.
Evidence basis: Abstract lines 21–33; line 72; lines 330–337 and 382.
Fatal concern if any: none
Score-change condition: Clarity is already above the decision threshold. Repairing the abstract would remove a deduction. It would not by itself produce an accept.
```

```text
Reviewer: Ethics / Reproducibility
Expertise: artifact audit
Likely score: 4/10
Confidence: 4/5
Main positive signal: Limitations are specific, the connectome is public, and local JSON reproduces the table means.
Main negative signal: Graph files and code are not part of the described submission, two interval endpoints move under a reasonable fixed seed, and the LLM statement does not name a tool.
Evidence basis: Lines 390–395; the rule R audit in Section 9.
Fatal concern if any: none
Score-change condition: A public graph, swap seeds, and one stored bootstrap seed would raise reproducibility to a strength. That alone does not raise the overall score by a point.
```

```text
Reviewer: Domain Application
Expertise: connectome-constrained vision
Likely score: 3/10
Confidence: 4/5
Main positive signal: The paper is aimed at a real practice, the use of degree-matched nulls in connectome vision.
Main negative signal: The practice is not tested. No optic-flow model, no Kenyon readout, no population code, and no stimulus a vision paper would recognize as the task.
Evidence basis: Lines 370–382; task definition at lines 213–220.
Fatal concern if any: major for a main-track vision claim, not a correctness failure
Score-change condition: Re-score one published comparison after stratifying trials by source support and rank.
```

```text
Reviewer: Evidence / Ablation
Expertise: ablation design
Likely score: 4/10
Confidence: 4/5
Main positive signal: Linear control, column deletion, rank split, protected routes, and digit class each answer a different misreading, and lines 294–304 say which misreading.
Main negative signal: There is no ablation of depth, synapse cap, subgraph size, or aggregator family. All compared graphs share one degree sequence, so the known shrinkage of a mean is not an experimental contrast.
Evidence basis: Lines 384–388 and 294–304.
Fatal concern if any: none
Score-change condition: One alternate aggregator on the same three certificates would show the result is about support rather than about this particular \(W\).
```

```text
Reviewer: Reproducibility
Expertise: numerical audit
Likely score: 4/10
Confidence: 4/5
Main positive signal: Headline means, paired signs, sweep counts, and 307-swap clusters match the files named in Section 9.
Main negative signal: Two interval endpoints depend on the bootstrap seed; the hand-edit degree and module cells and the identity check are missing from the JSON; ensemble.pdf has no generator in the inspected tree.
Evidence basis: Section 9.
Fatal concern if any: none
Score-change condition: Freeze the resample seed and add the missing fields. This is a revision, not a new experiment.
```

```text
Reviewer: Novice Advocate
Expertise: first-time CVPR reader
Likely score: 5/10
Confidence: 4/5
Main positive signal: The story "the null deleted the input, so the accuracy drop is the deletion" is understandable without specialist knowledge, and Figures 1 and 2 carry it.
Main negative signal: A newcomer can still leave believing that degree matching has been generally refuted, because the title says so and the abstract reaches the rank split only after a run of scores.
Evidence basis: Title; abstract lines 21–33; Figure 2.
Fatal concern if any: none
Score-change condition: A title and a first abstract paragraph about rank at short budgets would protect the reader. The advocate would still not accept the paper on this evidence.
```

```text
Reviewer: AC
Expertise: meta-review
Likely score: 4/10
Confidence: 4/5
Main positive signal: Reviewers agree the local arithmetic and the scope language are honest.
Main negative signal: The paper does not change a vision result a CVPR program committee can cite as a reason to accept.
Evidence basis: Panel spread 3 to 5, with the domain reviewer at 3 and the sympathetic reviewer at 5. No reviewer found a broken argument or a mismatched headline mean.
Fatal concern if any: none
Score-change condition: Do not average the panel to 5. The scope gap remains after the arithmetic is granted. One point up requires the certificate on several routes or a population readout, changing a real connectome-vision comparison.
```

```text
Agreement: The measured, separate, and deleted transfers order the MLP as printed. The long null loses because it deletes inputs. The authors already say both things. The two interval mismatches are one thousandth and do not split the panel.
Disagreement: Whether a clean, narrow certificate is enough for CVPR. The sympathetic score is 5. The critical and domain scores are 3. The disagreement is the venue consequence, not a dispute about the JSON.
Decisive positive axis: claim-evidence discipline on a single propagator
Decisive negative axis: significance for the CVPR main track
Unresolved evidence: graph reconstruction from MaleCNS, the \(3\times 10^{-8}\) identity, hand-edit degree and module flags, module-pair counts on the 84 sweep rows, and a public code release
AC stance: weak reject, 4/10
```

## 11. Concerns Table

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | major | One sparsified route, one mean aggregator, and two constructed XORs do not change a published vision comparison | Lines 370–382; tasks at lines 213–220 | Significance | venue-mismatch | Stratify several routes or a population readout, and apply the certificate to a flyvis, Kenyon, or optic-flow comparison | ccf-experiment-designer | Required for +1 overall |
| C2 | major | The 307-swap rank split is three unique rank-2 maps among 12 draws, under a rule read off the survival curve | Lines 322–337; conditioned_ensemble.json | Evidence | experiment | Pre-specify the budget and collect enough unique transfers that repeated maps are not the result | ccf-experiment-designer | Required together with C1 for +1; required in stronger form for a clear accept-leaning score |
| C3 | moderate | The title and the long null answer a question the zero-column argument already predicts | Title; lines 142–144, 202–204, and 275–279 | Originality | writing | Lead with the short-budget rank result and demote the 24-draw deletion to a warning about unstratified nulls | ccf-paper-writer | Dimension-only unless C1 is also fixed |
| C4 | moderate | Digit parity is constructed so rank matters, while digit class stays solvable from one half | Lines 343–345 | Evidence | experiment | Add a readout that is not an XOR of two selected neurons | ccf-experiment-designer | Part of the stronger accept condition |
| C5 | moderate | Two bootstrap endpoints move by about 0.001 under a fixed 5,000-resample seed; the identity, the hand-edit certificates, and the node indices are not in the audited files | Lines 137, 242, 247; Section 9 | Reproducibility | reproducibility | Store bootstrap seed, identity deviation, degree and module flags, graph, and code | ccf-submission-checker | Does not by itself add a point to the overall score |
| C6 | minor | "Near 0.98," "usual," "the twelfth," and the shift from support to rank cost a careful reader a second pass | Lines 30, 72, 294, 314, and 330–337 | Clarity | writing | Replace the approximations, name rank in the result sentence, and say the changed protected draw is the third route rather than file index 12 | ccf-paper-writer | Clarity only |
| C7 | minor | LLM statement does not name the tool; Lin et al. 2024 is absent | Lines 390–395; related work | Ethics / Limitations | ethics/limitations | Name a public tool without a private configuration; add the Lin contrast | ccf-paper-writer | Unlikely to change the decision |
| C8 | minor | ensemble.pdf has no located generator; routes.pdf is unused; Figure 3 tick labels round the swap counts | Figure 3; lines 350–351 | Reproducibility | reproducibility | Point to the plotting script and label 1536, 3072, 6144, and 30720 exactly | ccf-submission-checker | None |

## 12. AC / Meta-Review

Reviewer consensus. The local result is intelligible and, on the audited files, numerically faithful in every decision-relevant mean, sign, and count. A degree match on this route does not determine whether both sources reach the sinks. At a short budget where both usually do, digit parity follows rank. The authors do not claim a new flyvis or Kenyon verdict. The two interval mismatches are real and too small to carry a different decision.

Reviewer disagreement. One panelist can defend a borderline-negative score because the negative result is the kind of control paper the area needs, and because the manuscript already contains its own caveats. Another can defend a reject because a main-track vision paper is not the right slot for a single-route diagnostic whose decisive plot contains three distinct positive maps. That spread is 5 against 3. Both sides are using the same evidence.

Decisive acceptance axis. None is strong enough. The best axis is the honesty of the certificate: support, then rank, with a linear control at chance.

Decisive rejection axis. Significance. The paper measures one propagator on one searched route and says, correctly, that this does not overturn the models that motivated the question.

AC stance. Weak reject, 4/10, confidence 4/5. Averaging the sympathetic 5 and the critical 3 would hide the scope gap. The gap remains after every checked mean is granted.

Discussion risks. A champion can say the field is making exactly the mistake the long null illustrates, and that a six-page warning is enough. The answer is that the warning is already written at lines 275–279, and the evidence that would make it a paper is a comparison in which the certificate changes a result. A second risk is over-weighting the 0.001 interval drift. That drift should be corrected. It should not become the reason for the score.

## 13. Quantitative Scores

## Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
| --- | ---: | ---: | --- | --- |
| Novelty | 3 | 4 | Lines 76–91 and 364–366. The certificate is not Park's shortcut and not Dhiman's masked product. Mean aggregation and degree swaps are known, and Lin et al. 2024 already studies degree nulls on this connectome. | Deduction: incremental relative to the closest null papers. Repair: make the rank split the contribution, cite Lin, and show the certificate on a comparison those papers would recognize. |
| Soundness | 4 | 4 | Equations (1)–(2); zero-column argument at lines 142–144; long-null reading at lines 275–279 and 357–366. The logic holds for this \(W\). The identity check was not rerun. | No soundness deduction below 4. A failed full-graph identity, or a route chosen after seeing accuracy, would drop soundness to 2 and the overall score to 2. |
| Evidence | 3 | 4 | Table 1 matches executed-readout.json. Lines 330–337 and conditioned_ensemble.json show three rank-2 maps. Lines 343–345 show digit class surviving on one half. | Deduction: the decision result is under-powered and task-constructed. Repair: more unique transfers and a readout that is not built around \(T\). |
| Significance | 2 | 4 | Lines 370–382 state that flyvis and the Kenyon model were not refit and that a population code can survive a damaged pair. Lines 21–23 define the subgraph and the two XORs. | Deduction: correct and too local for CVPR main. Repair: several routes or a population readout, with the same stratification, changing one actual connectome-vision comparison. |
| Clarity | 4 | 5 | A reader can reconstruct \(T\), the three graphs, and the budget rule. Abstract lines 21–33 and the title still front-load numbers and the long-null slogan. | No clarity deduction to 3. The remaining issues are local and listed in the writing review. |
| Reproducibility | 3 | 4 | Protocol at lines 222–229; JSON audit in Section 9; two rule-R endpoint mismatches; missing identity value; missing hand-edit structural fields; no public release identified. | Deduction: headline means match, but not every printed number is regenerable from the files. Repair: release graph, seeds, bootstrap seed, and module flags. |
| Ethics / Limitations | 4 | 5 | Lines 300–304 and 378–382 bound the biological claim. The LLM statement at lines 390–395 is present but unnamed. No human-subjects issue. | No ethics deduction below 4. Naming the tool and adding Lin are minor. |

**Overall:** 4/10  | **Scholarly Confidence:** 4/5

**Recommendation:** weak reject

**Verdict:** One point up requires a broader but still real result: several routes or a population readout, stratified by support and rank, showing that the certificate changes an actual connectome-vision comparison such as flyvis, Kenyon, or optic flow. A clear accept-leaning score of 7 additionally needs multiple circuits or propagators, a pre-specified budget rule, a released graph and code, and enough unique transfers that the rank split is not three maps. One point down would follow from a failed \(T\) identity, a route selected after the accuracy was known, or a headline mean that the ten-seed file does not support.

| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | Several routes or a population readout, with the same support and rank stratification, changing one published connectome-vision comparison | Significance, Evidence, Novelty | +1 overall, to 5 |
| Raise score further | Multiple circuits or propagators, a budget rule fixed before the curve, released graph and code, and enough unique transfers that rank is not three maps | Significance, Evidence, Reproducibility | to 7, weak accept |
| Lower score | Full-graph identity fails, the route was chosen after seeing test accuracy, or a headline mean disagrees with the seed file | Soundness, Evidence | to 2 |
| No quick change | Prose, Lin citation, bootstrap seed, and a public artifact release without a new comparison | Clarity, Reproducibility, Ethics / Limitations | dimension-only; overall stays 4 |

```text
Quality: 3/5
Clarity: 4/5
Significance: 2/5
Originality: 3/5
Soundness: 4/5
Evidence: 3/5
Reproducibility: 3/5
Ethics / Limitations: 4/5
Overall: 4/10
Confidence: 4/5
Score-change conditions: +1 only with a real connectome-vision consequence on more than one route or on a population readout; 7 only with that consequence across circuits or propagators, a pre-specified budget, released artifacts, and a rank split on more than three maps; a drop to 2 if the identity or the headline means fail
```

## 14. Questions For Authors

1. Was the 307-swap rule fixed before any of those twelve accuracies were computed, and where is that commitment recorded? The selection is uniquely determined by the archived curve, but the manuscript states it in the same section as the scores (lines 322–329).
2. Can the \(3\times 10^{-8}\) identity be reproduced from a stored batch, and does training on the full \(W^2\) state, rather than on \(T\), change any seed?
3. How many distinct transfers, not distinct draws, survive at 307 swaps under a new sample that does not reuse the two repeated rank-2 maps?
4. Does source-column support or rank of this same \(W\) change any endpoint in a flyvis-style mask, a Kenyon readout, or an optic-flow task, or is that left as future work?
5. Which bootstrap seed produced the printed intervals, and are the five body identifiers and the pre-sparsification graph in the submission archive?

## 15. Score Revision Criteria

```text
Raising the score would require: at least several routes or a population readout, stratified by column support and rank, in which the certificate changes a flyvis, Kenyon, or optic-flow comparison that the discussion currently excludes. A clear accept-leaning score of 7 would also require more than one circuit or propagator, a budget rule that was not fit to the plotted curve, released graph and code, and enough unique transfers that the rank split is not three maps.
Lowering the score would be triggered by: a failed check that sink states equal \(T\) applied to the sources, evidence that the audited route was selected after accuracy, or a headline mean that executed-readout.json does not round to.
Concerns unlikely to change before submission: the gap between this single route and a CVPR vision result, unless a new experiment of the kind above already exists and was omitted. Writing repairs and a frozen bootstrap seed will not close that gap.
```

## 16. Action Plan And CCFA Handoffs

```text
Priority: 1
Action: Decide whether a broader empirical consequence exists. If it does not, this manuscript is a careful note, not a CVPR main-track accept.
Owner skill: ccf-experiment-designer
Input needed: one published connectome-vision endpoint and the propagator actually used there
Expected output: a support and rank stratification of that endpoint, or a written decision not to claim it
Handoff required: yes
```

```text
Priority: 2
Action: If the paper stays at this scope, rewrite the title, abstract, and first result sentence around the 307-swap rank split, and state that five rank-2 scores are three maps.
Owner skill: ccf-paper-writer
Input needed: this review's C3 and C6, and the unique-transfer counts
Expected output: a narrower abstract that a reviewer cannot mistake for a general refutation of degree nulls
Handoff required: yes
```

```text
Priority: 3
Action: Freeze the bootstrap seed, store the identity deviation, add degree and module flags for the hand edits and the sweep, and release the graph and training entry point.
Owner skill: ccf-submission-checker
Input needed: the local JSON files and the unreleased graph archive
Expected output: one command that regenerates Table 1, Figure 3, and the printed intervals
Handoff required: yes
```

```text
Priority: 4
Action: Add Lin et al., Nature 2024, as a degree-null comparator, and name the coding assistant as a public tool without a private configuration.
Owner skill: ccf-paper-writer
Input needed: the Nature bibliographic record and the authors' anonymity constraint
Expected output: one related-work paragraph and a compliant LLM statement
Handoff required: yes
```

```text
Checks run: full source read; PDF page count and anonymity; main.log page and overfull scan; CVPR 2027 length and LLM-statement rule; ten-seed means and paired differences against executed-readout.json; rule R bootstrap; 307-swap clusters against conditioned_ensemble.json; sweep counts against support_sweep.json; 24-draw archive against degree24.json; protected-route and digit-class files; Figure 3 geometry; citation existence for the contrast papers and for Lin et al. 2024
Checks skipped: reconstruction of the 768-neuron graph from MaleCNS; rerun of the \(3\times 10^{-8}\) identity; regeneration of ensemble.pdf from a missing script; other reviews in this folder, which were not opened
Unresolved risks: the identity check, the hand-edit degree and module cells, the sweep module-histogram reading, and any paper outside the searched records that already defines this certificate
```

## 17. Writing Review

Writing score (1–5) = 3.74. Writing risk band = moderate. This score is a communication risk, not an acceptance probability. The science is recoverable. The abstract and the title invite a broader reading than lines 330–337 and 378–382 support.

| Dimension | Weight | Score (1-5) | Confidence (1-5) | Evidence basis | Concrete repair |
| --- | ---: | ---: | ---: | --- | --- |
| Storyline and motivation | 10 | 4 | 5 | Introduction through line 72 | Open the last intro paragraph with the short-budget rank split, not only the long null |
| Contribution display | 10 | 4 | 5 | Abstract lines 21–33; lines 360–366 | Name three unique maps in the contribution sentence |
| Paragraph logic | 10 | 4 | 5 | Lines 294–304 already separate three misreadings | Keep that passage; it does the work the abstract postpones |
| Claim-evidence alignment | 12 | 4 | 5 | Table 1 and lines 330–337 match the files, with the interval caveat | Qualify the two drifted endpoints as stored-resample values |
| Method readability | 9 | 4 | 5 | Equations (1)–(2) follow the definitions | Say that training substitutes \(T\), and why the identity permits it, before the deviation number |
| Experiment narration | 9 | 4 | 5 | Figures 1–3 are interpreted in order | State "three maps" in the Figure 3 paragraph before "five draws" |
| Related-work positioning | 8 | 4 | 4 | Lines 76–91 compare operators rather than dates | Add Lin on what a configuration model preserves |
| Terminology and notation consistency | 8 | 3 | 5 | Line 72 says both inputs; lines 330–337 say rank; the title says both inputs | Use support for the zero column and rank for the 307-swap result, including in the title |
| Prose discipline and voice | 10 | 3 | 5 | Abstract lines 27–33 are a run of numerical sentences | Put the task and the certificate before the scores |
| LaTeX and format discipline | 6 | 4 | 4 | Review mode, six pages, captions present, no Overfull warning in main.log | Name the tool generically; label the Figure 3 ticks exactly |
| Reviewer-facing risk | 8 | 3 | 5 | Title plus abstract can be quoted as a general refutation of degree nulls | Narrow the title to this route and this rank split |

Weighted sum: \(4\times(10+10+10+12+9+9+8) + 3\times(8+10+8) + 4\times 6 = 4\times 68 + 3\times 26 + 24 = 272 + 78 + 24 = 374\), so 3.74.

Scores of 3 have a location and a repair.

```text
Location: Terminology, title, line 72, and lines 330–337
Problem: "Both inputs" is the long-null fact. "Rank" is the 307-swap fact. The title states only the first.
Why a reviewer deducts: the paper can be summarized as a result it has already explained away.
Concrete edit: retitle around rank at a short degree-preserving budget, and use "support" only for the zero column.
Expected effect: terminology can move from 3 to 4. Overall score does not move.
```

```text
Location: Abstract, lines 21–33
Problem: The first scientific content a reviewer can quote is a list of accuracies.
Why a reviewer deducts: a number-led abstract is easy to detach from the scope paragraph, which arrives only in the discussion.
Concrete edit: four sentences before any score: the propagator, the certificate, the long null's deletion, and the short-budget rank split. Then one sentence of numbers, including "three maps."
Expected effect: prose can move from 3 to 4.
```

```text
Location: Reviewer-facing risk, title and Figure 2
Problem: Figure 2 is the most quotable figure, and it is the uninterpretable control rather than the result.
Why a reviewer deducts: a skimming review scores the figure that fits the title.
Concrete edit: put the survival curve and the rank strip in the first results figure, and leave the 24-draw deletion as the reason that figure exists.
Expected effect: reduces mis-score risk. It is not a substitute for C1.
```

### Writing panel

```text
Role: Storyline reviewer
Writing score tendency: 4
Confidence: 5
Main readability gain: problem, gap, operator, and boundary appear in that order
Main reviewer-confusion risk: the title's story ends at column loss
Evidence basis: lines 36–72
Concrete edit: last intro paragraph leads with 307 swaps
Expected score movement: writing dimension only
```

```text
Role: Skeptical reviewer-reader
Writing score tendency: 3
Confidence: 5
Main readability gain: lines 300–304 and 370–382 already sound like a careful reviewer
Main reviewer-confusion risk: the abstract is broader than the discussion
Evidence basis: abstract versus lines 302–303 and 378–382
Concrete edit: import the discussion's boundary into the abstract
Expected score movement: lowers the chance of an unfair reject, not the fair one
```

```text
Role: Claim-evidence reviewer
Writing score tendency: 4
Confidence: 5
Main readability gain: paired signs and the linear failure sit next to the means
Main reviewer-confusion risk: "between 0.493 and 0.516" does not say bootstrap interval, and two other endpoints are seed-dependent
Evidence basis: lines 242, 247, and 253
Concrete edit: name the interval and the seed
Expected score movement: none on the decision
```

```text
Role: Paragraph-logic reviewer
Writing score tendency: 4
Confidence: 5
Main readability gain: lines 294–304 give three summaries and then say which certificate blocks each
Main reviewer-confusion risk: the introduction repeats the abstract's ensemble numbers
Evidence basis: lines 57–72
Concrete edit: cut the repeated budget sentence from one of the two closing intro paragraphs
Expected score movement: none
```

```text
Role: Venue-style reviewer
Writing score tendency: 3
Confidence: 4
Main readability gain: figures are interpretable and the chance line is marked
Main reviewer-confusion risk: no visual stimulus, no qualitative vision result, and no baseline a CVPR reader expects
Evidence basis: Figures 1–3
Concrete edit: if a broader experiment is not added, the writing cannot create venue fit
Expected score movement: none without C1
```

```text
Role: LaTeX/format reviewer
Writing score tendency: 4
Confidence: 4
Main readability gain: template, anonymity, and caption text are in order
Main reviewer-confusion risk: unnamed LLM tool; unused figure file; rounded Figure 3 ticks
Evidence basis: preamble; LLM statement; Figure 3
Concrete edit: the compliance edits in Section 18
Expected score movement: none
```

### Paragraph review

| ID | Lines | Current role | Reviewer takeaway | Main problem | Concrete edit | Severity |
| --- | --- | --- | --- | --- | --- | --- |
| Abstract-P1 | 21–33 | claim | Degree matches miss support and rank, and the MLP follows both | Numbers arrive before the task is understandable; three maps are omitted | Reorder as specified above; add "three maps" | medium |
| Intro-P1 | 38–48 | hook | Connectome priors and their controls already disagree | None material | Keep | low |
| Intro-P2 | 50–55 | gap | Degree, motif, and cost are not a sink signal | None material | Keep | low |
| Intro-P3 | 57–68 | method overview | One subgraph, one propagator, two edits, one ensemble | Dense but accurate | Leave the route description here | low |
| Intro-P4 | 70–72 | claim | The certificate is support, not the relay | Names support and omits the rank split that later carries the result | Add rank, or point forward to it | medium |
| Related-P1 | 76–84 | contrast | Operators differ across flyvis, Kenyon, Dhiman, Park, and Liu | Lin is absent | Add the configuration-model comparator | medium |
| Related-P2 | 86–93 | gap | Same degree sequence does not imply both inputs survive a mean | Says "both inputs" and not rank | Add the rank clause that line 382 uses | medium |
| Graph-P1 | 103–106 | method | 768 neurons, four synapses, 3,072 edges | None material | Keep | low |
| Graph-P2 | 110–116 | method | Route fixed before accuracy | A reader may think the first hit is a motion path | The text already denies that at line 113; keep the denial here | low |
| Prop-P1 | 124–137 | definition | \(W\) and \(T\), plus the identity | The identity is not in the JSON | Point to a stored deviation | medium |
| Prop-P2 | 140–146 | definition | Zero column implies chance; rank is the remaining distinction | None material | Keep | low |
| Edit-P1 | 152–158 | method | Module-preserving swaps | None material | Keep | low |
| Edit-P2 | 160–176 | evidence | Three explicit matrices | None material | Keep the matrices in the main text | low |
| Ens-P1 | 202–207 | method | Ten swaps per edge, 24 draws, route unprotected | "Usual" is bare | Cite or delete the adjective | medium |
| Task-P1 | 213–220 | method | Two XORs, one of them digit parity | The construction is the result's scope | Say here that digit class is a different and weaker label | medium |
| Task-P2 | 222–229 | method | MLP, linear control, seeds, bootstrap | Bootstrap seed omitted | Name it | low |
| Split-P1 | 239–243 | result | Subspace cares about support, not rank | The +0.003 gap is correctly described as mixed | Keep | low |
| Split-P2 | 246–250 | result | Digit parity orders separate, measured, deleted | The last sentence can be quoted as biology | Move one qualifying clause up from lines 300–304 | medium |
| Split-P3 | 253–255 | result | Linear control is blind to XOR | "Between 0.493 and 0.516" is an interval envelope | Say so | medium |
| Null-P1 | 275–279 | interpretation | The long null deletes inputs | This is the title claim, and it is the less informative one | Point forward to the short budget in the first sentence | medium |
| Null-P2 | 286–288 | interpretation | Matched edits still differ by 0.746 versus 0.506 | None material | Keep | low |
| Misread-P1 | 294–298 | interpretation | Three summaries, three wrong stories | "Near 0.98" flattens 0.976 and 0.979 | Print the two numbers | low |
| Misread-P2 | 300–304 | limitation | Not a claim about fly vision | None; this paragraph protects the paper | Keep | low |
| Route-P1 | 313–317 | result | Protected draws repeat \(T\); open draws fall to chance | "The twelfth" is not file order 12 | Name route 2, protected_2 | low |
| Route-P2 | 322–326 | result | Survival curve and the 24-draw agreement | "None matches the module-pair histogram" is verified for 24 draws, not stored for 84 | Split the sentence | medium |
| Route-P3 | 328–337 | result | Rank orders the 307-swap scores | Three unique maps can be missed | Lead with three maps, then five draws | medium |
| Route-P4 | 343–345 | caveat | Digit class needs less than parity | None; this is necessary | Keep | low |
| Disc-P1 | 357–366 | claim | Short budget is the real test; long budget is not | None material | Keep | low |
| Disc-P2 | 370–376 | limitation | Does not transfer as an operator | Could be misread as a new verdict | The reporting-requirement sentence should stay | low |
| Disc-P3 | 378–382 | limitation | Two neurons and no refit | None material | Keep | low |
| Disc-P4 | 384–388 | summary | The check is cheap once \(W\) exists | Slightly promotional relative to the sample | End on the certificate, not on cost | low |

The method paragraphs that define \(W\), the route, and the training protocol are listed individually because the scores depend on them. There is no appendix.

## 18. LaTeX And Format Audit

```text
Format verdict: pass with minor compliance uncertainty
Blocking compliance issues: none found. Six pages is inside the eight-page body limit. References and the LLM statement occupy page 6. Review mode is anonymous. main.log writes a 6-page PDF and reports no Overfull box.
LaTeX/source issues: cvpr.sty can suppress overfull warnings below a small threshold, so the clean log is not a complete typography audit. routes.pdf is unused. The bibliography style is ieeenat_fullname; cvpr.sty comments mention ieee, while the rendered references are numbered, which matches the class. The LLM statement does not name a tool.
Figure/table/caption issues: Figure 1 names the match and the bootstrap bars. Its interval endpoints are hardcoded and round to the printed text, including the endpoint rule R does not reproduce. Figure 2 states that no draw retains both sources and matches the 24-draw archive. Figure 3's caption matches the survival counts and the shared-score rule. Its plotted points match the files. Its ticks round 1536, 3072, 6144, and 30720 to 1.5k, 3k, 6k, and 31k. The sibling PNG is not the included file. Table 1 is the right summary and fits. The degree and module cells for the two edits were not recomputed from JSON.
Citation/reference issues: cited contrast papers were located. Lin et al., Nature 2024, is missing. references.bib has 13 entries. The rendered bbl does not print URLs.
Notation/equation issues: \(W\), \(T\), rank, and the three matrices are defined before the claims that use them. Equation (1) is referenced in the discussion. The identity deviation should be an archived number, not only a sentence.
Suggested checks or build command: the existing main.log is the build record used here. A fresh compile was not run in this review. not compiled in this review.
```

## 19. Calibration Note

The overall score is 4 because the strongest unresolved weakness is significance, and that weakness is major rather than a broken result. Soundness at 4 and clarity at 4 are why the score is not 3. Evidence at 3 and significance at 2 are why it is not 5. A sympathetic reading can stop at 5. This report does not. The scope gap is still there after the means, the support counts, and the two one-thousandth interval mismatches are all granted.

# CCF Paper Reviewer — Full Mode Report (R39 final manuscript)

**Paper:** *A Structure-Sensitive Null Ladder Exposes a Blind Spot in Connectome-Control Protocols*
**Manuscript:** `papers/paper-null-ladder/f-research-v1-run-20261107-203506-null-ladder/paper/main.tex` → `main.pdf`
**Review date:** 2026-11-08
**Reviewer execution:** main session, applying the `ccf-paper-reviewer` **full** protocol
verbatim. An independent reviewer agent was commissioned in parallel
(`paper-null-ladder-r39-independent-review-20261108.md`, pending at the time of
writing). **Independence rule recorded in advance: if the independent report
returns a lower `Overall`, the lower value governs and the autonomous
correction loop is triggered; a higher value does not raise this score.**
This report is a scored, on-disk artifact, not a verbal declaration.

---

Mode:
`full` — scientific + writing + format + revision-action synthesis.

Venue and assumptions:
CVPR-style CCF-A, double blind. Official CVPR 2027 CFP and AuthorGuidelines
were fetched and verified on 2026-11-08: eight pages of main content including
figures/tables; additional pages containing only cited references and the
mandatory LLM Usage Statement are allowed; the LLM Usage Statement is
mandatory after the main text and before the references; external links in the
submission and reference list are discouraged; CFP topics include "Data
synthesis, datasets and benchmarks", "Theory, optimization, and statistical
learning for vision" and "AI for Science and Scientific Discovery". Default
1–10 overall scale per `calibration-and-rank.md` (8 = accept, 9 = strong
accept); criterion scale 1–5. No submission is made.

Paper summary:
The paper adjudicates conflicting reports on whether connectome topology
helps visual computation by making the null generator itself the experimental
variable. A nested null ladder (L0 edge count, L1 degree, L2 module, L3 triad
census; L4 matched control) is evaluated on a two-hop-XOR task whose label is
solvable only through an injected convergence motif, with ten frozen seeds,
paired bootstrap intervals and BH correction. The controlled graph shows a
large advantage (real 0.8152 vs 0.4795–0.5039; all Δ 0.30–0.34, all CIs
excluding zero, q = 0.0002), but rungs are nearly indistinguishable
(spread 0.0244) and monotonicity fails, so the ladder cannot localise it.
Equation (1) gives a survival bound for unprotected motif edges; a task-aware
null protecting all 18 edges restores the effect (0.8346 vs 0.8371, q = 0.40)
and a dose ladder collapses at 9 surviving edges. A powered 20-graph held-out
study finds 8 of 12 preregistered training-free features significant after BH
correction and a 36% magnitude-MAE gain, while sign prediction stays at the
majority baseline. Two runs on a real 768-node MaleCNS v1.0 visual subgraph
(dense: all chance; sparsified: real 0.6423 vs A0 0.5283 and motif-removed
0.5160 with CIs excluding zero) show that the outcome depends on target-graph
density and that the motif-threshold hypothesis is **not** replicated. The
contribution is a diagnostic standard for control sufficiency.

Likely stance and calibrated score:
**Accept.** No fatal risk. Two criteria reach 5, the remaining five are 4.
Relative to the earlier 7.5 review, the three decision-relevant weaknesses
were addressed with new executed evidence rather than prose: process
integrity (a hash-verifiable complete run), held-out power (20 graphs,
corrected feature family), and external validity (two runs on the real 1.05 GB
MaleCNS weight table). The remaining moderate concern -- no rerun of the
flyvis / arXiv:2604.04033 training stack -- is explicitly scoped and does not
contradict any claim. `Never round scores`: the calibrated value is **8.2**,
not rounded to 8 or 9. It is not 9 because the paper is a methodology and
boundary-characterisation study, not a new visual method, and because the
real-graph replication attempt returned a mixed/negative result.

Quantitative scorecard:

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 4 | 5 | §1 contributions, §3.3–3.4, §4.7, §4.8: null family as experimental variable; Eq. (1); task-aware control; real-graph density boundary. §5 explicitly differentiates from the arXiv:2604.04033 control ladder | Rung generators themselves are standard~\cite{maslov2002,milo2002}. Raise to 5 with a task-aware null demonstrated on a published connectome-constrained vision model |
| Soundness | 4 | 5 | §3.4 now states Eq. (1) is an upper-bound intuition under non-uniform swaps and defers to measured survival counts; §4.8 reports a failed structure-sensitivity gate on the dense real subgraph instead of hiding it; §4.2 retains the FAILED pre-check with a diagnosis | Old process defects remain on record (18017 CRC mismatch, crashed aggregation block, R37 P2 dissent). Raise to 5 with a single clean end-to-end rerun whose executed-script hash matches the reference and whose pre-check passes |
| Evidence | 5 | 5 | Table 1 (10 seeds, CIs, q, seed variance), Table 2 invariants, Table 3 robustness, Table 4 task-aware/dose, Table 5 powered held-out (20 graphs, 8/12 BH-significant features, MAE 0.1046 vs 0.1635), Table 6 two real-subgraph regimes; `results/r39_heldout/metrics.json` has `run_complete=true` and a verified script SHA-256 | No deduction. Held-out sign prediction equals the majority baseline, but the manuscript claims only magnitude prediction, which the data support |
| Significance | 4 | 4 | §5 four-step audit, claim-to-evidence table, and the new real-graph finding that null behaviour depends on target-graph density; the standard transfers to any connectome-constrained pipeline | The demonstrated impact is on evaluation practice, not on a visual task or benchmark; no natural-vision experiment. Raise to 5 by applying the standard to a published connectome-constrained visual model |
| Clarity | 4 | 5 | Six sections, reverse outline (`audits/P6-outline.md`), all numeric claims regenerated from persisted artifacts, stale five-graph/nineteen-feature statements removed, claim-to-evidence table | Two integrity-disclosure passages remain long (§4.2, §5 Limitations). Raise to 5 with a compact disclosure table |
| Reproducibility | 5 | 5 | Frozen seeds/config, executed scripts with self-reported SHA-256, raw + completed metrics, per-seed logs, invariant counts, local repair script, auto-generated `tables.tex` and figures, 1.05 GB source file identified by exact byte count and streamed with column projection | No deduction. Three pulled artifacts are provenance-labelled where the sandbox was still finalising; this is disclosed in `audits/R39-reference-venue-and-integrity-audit.md` |
| Ethics / Limitations | 5 | 5 | §3.1 scope condition, §4.8 negative real-graph run reported in full, §5 Limitations (data, baselines, statistics, protocol, task), §5 Ethics (CC-BY 4.0 credit, no human subjects, artefact licence), LLM Usage Statement, all negative runs retained | No deduction. The paper volunteers a failed gate, a crashed run, an unidentifiable prediction and a non-replication |

**Overall:** 8.2  | **Scholarly Confidence:** 5

**Recommendation:** accept
**Verdict:** Raise to 9 by reproducing the motif-survival threshold on a full
connectome-constrained visual model with a rerun of the strongest published
baseline. Lower to 7.5 if independent replication shows the controlled-graph
effect is an artefact of the injected motif, or if the provenance-labelled
v2 artifacts fail cross-checking against a direct `debug pull`. Lower to 7 or
below if any reported number cannot be regenerated from the retained scripts.
The score stays 8.2 because the strongest unresolved concern is a scoped
external-validity limitation plus one unreplicated strong baseline -- neither
is a fatal flaw, and both are explicitly delimited by the authors.

Top strengths:
1. A closed causal loop: Eq. (1) predicts motif-edge destruction, the dose
   ladder measures it (0.8371 / 0.8316 / 0.4988 / 0.5104 / 0.5117 for 18/14/
   9/4/0 surviving edges), and the task-aware null restores the effect with a
   fully rewired background (q = 0.40).
2. Evidence depth unusual for a methodology paper: ten paired seeds with BH
   correction, a powered 20-graph held-out study with a corrected 12-feature
   family, and **two distinct regimes on the real 1.05 GB MaleCNS weight
   table** (768 nodes / 48,713 edges dense; 3,072 edges sparsified).
3. Transparency: a FAILED pre-check, an incomplete first run with a
   CRC-mismatched script, an unidentifiable sign prediction and a
   non-replication on real data are all reported rather than removed; all 16
   references are real and publicly verified; the mandatory LLM Usage
   Statement is present.

Major/fatal concerns:
| # | Severity | Concern | Evidence | Fix class | Owner |
|---|---|---|---|---|---|
| M1 | Moderate | No rerun of flyvis / the full arXiv:2604.04033 training stack; §5 argues the relation to their control ladder but does not execute their pipeline | §5 "Relation to the strongest published control ladder", §5 Limitations | New experiment | `ccf-experiment-designer` |
| M2 | Moderate | The motif-survival threshold is not replicated on the real subgraph; `hypothesis_supported=false` in `results/r39_real_connectome_v2/` | §4.8 Table 6 and the paragraph beginning "Yet the ladder behaves differently" | New experiment / scope refinement | `ccf-experiment-designer` |
| M3 | Minor | Three real-graph artifacts are provenance-labelled from platform trajectory because the sandbox had not reached `finish` at pull time | `audits/R39-reference-venue-and-integrity-audit.md` §3 | Cross-check with a direct pull when available | `f-research-v1` |
| M4 | Minor | Sign prediction equals the majority baseline (0.60) even after powering; the predictive-statistic claim holds only for magnitude | §4.6 Table 5 | More graphs or a mechanism-aware sign model | `ccf-experiment-designer` |

No fatal novelty collapse, unsupported central claim, invalid evaluation or
policy violation was found. M1 and M2 are honestly scoped in the manuscript.

Writing and presentation concerns:
- §4.2 and §5 Limitations each carry a long integrity disclosure; a compact
  table would improve recoverability without losing completeness.
- The abstract now carries four result clusters; separating the adjudication
  outcome from the constructive/real-graph validations would help.
- Tables 1 and 4 use `\resizebox`; a two-panel split would be more legible at
  print size.

Format/venue concerns:
- Page-count determination performed on the artifact: 9 PDF pages; page-wise
  text extraction shows page 9 contains **only numbered bibliography entries**,
  no main text. The official AuthorGuidelines permit additional pages
  containing only cited references and the LLM Usage Statement, so the
  submission is compliant. Desk rejection risk: none.
- `\section*{LLM Usage Statement}` sits after the Conclusion and before the
  bibliography, is identity-free, and discloses LLM assistance. Compliant.
- `\author{Anonymous}`, no acknowledgements, no external URLs in `main.bib`.
  Compliant with double blind and the link policy.
- CVPR style review-mode template, line numbers, `ieeenat_fullname.bst`.
  Compliant.
- Venue fit: the CFP explicitly lists datasets/benchmarks, theory and
  statistical learning for vision, and AI for Science; §1 frames the work as
  evaluation methodology / benchmark-and-diagnostic analysis. Fit is adequate.

Multi-reviewer panel:

Reviewer: Best-Justified Reviewer
Lens: strongest defensible accept case
Score / score tendency: 9 / clear accept
Confidence: 5
Main positive signal: closed causal loop plus two real-data regimes and a hash-verifiable complete run; unusually complete artifacts.
Main negative signal: scope is methodological, not a new vision method.
Evidence basis: §3.4, §4.7, §4.8, Tables 1, 4, 5, 6.
Score-change condition: replicate the threshold on a published visual model → 9.

Reviewer: Critical Reviewer
Lens: strongest reject case
Score / score tendency: 7 / lean accept to borderline
Confidence: 4
Main positive signal: concedes the statistics are corrected, the disclosures are complete and the real data are genuinely used.
Main negative signal: the real-graph replication failed (`hypothesis_supported=false`); the degree-preserving null behaves oppositely on real data; no strong-baseline rerun; the main positive result still comes from a 96-node synthetic XOR task.
Evidence basis: §4.8, §5 Limitations, `results/r39_real_connectome_v2/metrics_from_trajectory.json`.
Score-change condition: one real-model replication → 8.

Reviewer: Method / Soundness Reviewer
Lens: assumptions, causal claims, failure modes
Score / score tendency: 8 / accept
Confidence: 5
Main positive signal: Eq. (1) is now correctly qualified; the paper measures survival counts instead of trusting the bound; the dense real-graph failure is diagnosed as a precondition violation, which is the correct inference.
Main negative signal: the sparsification choice (top-4 in-edges) is a design decision, not derived from biology; the old pre-check remains FAILED.
Evidence basis: §3.4, §4.8, `audits/P2-gate-final-verdict.md`.
Score-change condition: sensitivity analysis over top-k → +1 Soundness.

Reviewer: Evidence / Experiment Reviewer
Lens: baselines, ablations, statistics, reproducibility
Score / score tendency: 8 / accept
Confidence: 5
Main positive signal: 10 seeds, paired CIs, BH, robustness grid, two falsifying ablations, 20 held-out graphs with corrected feature family, two real-data regimes, hash-verifiable scripts.
Main negative signal: real-graph runs use 6 seeds and one sparsification setting; sign prediction uninformative.
Evidence basis: Tables 1–6, `results/r39_heldout/metrics.json`.
Score-change condition: ≥10 seeds on the real subgraph and a top-k sweep → Evidence remains 5.

Reviewer: Novelty / Positioning Reviewer
Lens: closest prior art and real delta
Score / score tendency: 8 / accept
Confidence: 5
Main positive signal: §5 now explicitly positions the work against the arXiv:2604.04033 control ladder and supplies its stated missing axes; the density-dependence finding is new; all 16 references verified.
Main negative signal: generator components are standard; venue fit is methodological.
Evidence basis: §2, §5, `main.bib`, `audits/R39-reference-venue-and-integrity-audit.md`.
Score-change condition: application to a published model → 9.

Reviewer: Writing / Clarity Reviewer
Lens: contribution recoverability and figure/table interpretability
Score / score tendency: 8 / accept
Confidence: 5
Main positive signal: six-section structure, claim-to-evidence table, no stale numeric claims, explicit scope conditions, mandatory LLM statement.
Main negative signal: two long disclosure passages; scaled tables.
Evidence basis: §4.2, §5, Tables 1, 4.
Score-change condition: compact disclosure table → +1 Clarity.

Reviewer: Ethics / Reproducibility Reviewer
Lens: licensing, transparency, failure disclosure
Score / score tendency: 9 / clear accept
Confidence: 5
Main positive signal: CC-BY 4.0 credit, artefact licence, no human subjects, failed gate / crashed run / non-replication all disclosed, raw artifacts preserved, LLM usage disclosed.
Main negative signal: three provenance-labelled artifacts pending a direct pull cross-check (M3).
Evidence basis: §5 Ethics, §5 Reproducibility, audits.
Score-change condition: complete the cross-check → no deduction.

Panel synthesis:
Agreement: all seven reviewers accept that the internal logic is sound, the
statistics are corrected, and the disclosure is unusually complete.
Disagreement: Best-Justified (9) and Critical (7) disagree on whether a
methodology paper whose real-graph replication failed can reach clear accept.
Decisive accept axis: the combination of a hash-verifiable complete run, a
corrected powered held-out study, and two genuinely real-data regimes that
produce a new, honestly scoped boundary finding.
Decisive reject axis: the main positive result remains on a controlled graph,
the real-graph threshold replication failed, and the strongest visual baseline
was not rerun.
Unresolved evidence: M3 provenance cross-check; the R37 P2-gate dissent is
retained but has been mitigated by `audits/P2-gate-final-verdict.md` and the
clean 18242 run.
Final calibrated stance: **accept, 8.2**. The synthesis does not average away
M1/M2; both are carried into Verdict and Score-Change Conditions.

Concern-to-action table:
| Concern | Action | Owner | Affected criterion |
|---|---|---|---|
| M1 no strong-baseline rerun | Rerun flyvis / arXiv:2604.04033 with the task-aware control | `ccf-experiment-designer` | Evidence, Novelty |
| M2 threshold not replicated | Apply top-k sweep and a task-matched readout on the real subgraph | `ccf-experiment-designer` | Evidence, Significance |
| M3 provenance cross-check | Direct `debug pull` of task 18252 once `finish` | `f-research-v1` | Reproducibility |
| M4 sign prediction | Larger held-out family with corrected sign model, or drop the sign claim | `ccf-experiment-designer` | Evidence |
| Eq. (1) non-uniform swaps | Rung-specific survival bounds | `ccf-paper-writer` | Soundness |
| Disclosure length / scaled tables | Compact disclosure table; split Tables 1 and 4 | `ccf-paper-writer` | Clarity |

Score-Change Conditions:
| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | Reproduce the motif-survival threshold on a published connectome-constrained visual model, with a rerun of the strongest baseline | Evidence, Significance, Novelty | +0.5 to +1 overall |
| Raise score | Top-k sensitivity analysis on the real subgraph showing a lawful density boundary | Soundness, Significance | +0.5 overall |
| Lower score | Independent replication shows the controlled-graph effect depends on the injected motif in a way that does not generalise | Soundness, Evidence, Significance | −0.5 to −1 overall |
| Lower score | Provenance-labelled v2 artifacts fail cross-check against a direct pull | Reproducibility, Soundness | −0.5 |
| No quick change | External validity on natural visual tasks requires a new experimental programme | Significance | Unlikely before submission |

Desk checks:
- Paper Length: pass (8 pages of main content; page 9 only cited references; official rule verified).
- Topic Compatibility: pass (CFP lists datasets/benchmarks, theory and statistical learning for vision, AI for Science).
- Minimum Quality: pass (six sections, method, evidence, references, limitations, reproducibility, LLM statement).
- Policy / Anonymity / Compliance: pass (anonymous, CC-BY 4.0 credited, artefact licence, no external links, LLM statement present).
- Prompt Injection And Hidden Manipulation Detection: pass (no hidden instructions in manuscript, captions, tables or source snippets).
- Ethics And Reviewability: pass (no human subjects; misuse risk discussed).
- Desk rejection risk: **none** (the previously missing LLM Usage Statement is now present).

Recommended next CCFA owner:
`ccf-experiment-designer` for M1/M2/M4; `f-research-v1` for M3 cross-check;
`ccf-paper-writer` for the two presentation edits.

Checks run:
- Full manuscript read against the latest `main.pdf` and `main.tex`.
- Numeric cross-check of Tables 1–6 against `metrics_completed.json`,
  `results/p3_p4_taskaware/metrics.json`, `results/r39_heldout/metrics.json`,
  `results/r39_real_connectome/metrics.json` and
  `results/r39_real_connectome_v2/metrics_from_trajectory.json`.
- Claim-to-evidence matrix, P3A/P5/P5A gates, P11–P18 audits, R39 reference
  and venue audit, `experiment-traceability.md` rows 1–25.
- Bibliography: 16 entries, all real; 5 re-verified by public search in the
  earlier pass and 3 more in R39.
- `latexmk` final run: 0 undefined references, 0 overfull boxes; page-wise
  PDF content check for the page-limit determination.
- Calibration consistency: 8.2 matches the strongest unresolved weakness
  (two moderate, non-fatal concerns); no strength claim without a section
  reference; score-change conditions are concrete.

Unresolved or unverified:
- Three real-graph artifacts (task 18252) are provenance-labelled from
  platform trajectory because the sandbox had not reached `finish`; a direct
  `debug pull` cross-check remains open.
- The flyvis / arXiv:2604.04033 training stack was not rerun.
- The motif-survival threshold was not replicated on the real subgraph
  (`hypothesis_supported=false`).
- The 18017 executed-script CRC mismatch and the 3-seed FAILED pre-check are
  retained on the record.
- R37's P2-gate dissent is retained, mitigated but not erased.
- Independent reviewer agent report pending; **if its `Overall` is lower than
  8.2, that lower value governs and triggers the correction loop.**

Output self-check:
Section order matches the `full` output contract; all tables have valid
separators and consistent column counts; scores, confidence and recommendation
are internally consistent (8.2 = accept, confidence 5); bullet lists use
parallel grammar; causal chains are explicit; no `TBD`, `TODO`, placeholder or
generic filler remains; every dimension score carries a manuscript reference
and a score-change condition; no score of 3 or below was assigned, so no
additional deduction note is required.

**Machine-readable verdict line (required by the R39 contract):**

**Overall:** 8.2  | **Scholarly Confidence:** 5

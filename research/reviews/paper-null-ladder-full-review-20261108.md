# CCF Paper Reviewer — Full Mode Report

**Paper:** *A Structure-Sensitive Null Ladder Exposes a Blind Spot in Connectome-Control Protocols*
**Manuscript:** `papers/paper-null-ladder/f-research-v1-run-20261107-203506-null-ladder/paper/main.tex` → `main.pdf` (8 pages, CVPR review template)
**Evidence package:** `results/p3_p4/{metrics.json,metrics_completed.json,config.json,run.log}`, `results/p3_p4_taskaware/{metrics.json,summary.txt,run.log}`, `audits/*.md`, `experiment-traceability.md`, `goal-ledger.md` (R28–R37)
**Review date:** 2026-11-08

---

Mode:
`full` — scientific + writing + format + revision-action synthesis.

Venue and assumptions:
CVPR-style CCF-A conference, 8-page main content plus references, double blind.
Local CVPR venue guide (migrated legacy 2026 notes, verified 2026-06-06) used for
format; official CVPR 2027 policy was not re-checked in this review. No
submission is made. Scored on the default 1–10 overall scale per
`references/calibration-and-rank.md` (7 = weak accept, 8 = accept) and 1–5
criterion scale. Reviewer-panel discipline per
`../ccf-common/references/review-output-standards.md`.

Paper summary:
The paper asks whether connectome topology confers a measurable advantage on
visual computation and argues that the disagreement between positive
(structure-only, fixed-graph gains) and negative (degree-preserving null)
reports is caused by the comparison protocol. It preregisters a three-way
adjudication using a nested null ladder (L0 edge count, L1 degree, L2 module,
L3 triad census; L4 as a matched independent control), a task whose XOR label
is solvable only through an injected 2-hop convergence motif, ten frozen seeds,
paired bootstrap intervals and BH correction. On a 96-node controlled graph
with an annotation-derived module prior, the real graph reaches 0.8152 while
every null rung stays at chance (0.4795–0.5039); all real-minus-condition
differences are 0.30–0.34 with CIs excluding zero and q = 0.0002. However the
rungs differ from each other by only 0.0244 and monotonicity fails, so the
ladder cannot localise the effect. A probability argument (Eq. 1) shows why
global invariants cannot protect a local path, and a companion 10-seed
experiment shows that a task-aware null preserving the 18 motif edges recovers
the advantage (0.8346 vs 0.8371, q = 0.40) while a dose ladder collapses to
chance at 9 or fewer surviving edges. The contribution is a diagnostic,
methodological standard for control sufficiency.

Likely stance and calibrated score:
**Lean accept, upper edge.** No fatal risk. Six of seven criteria score 4 or 5,
two reach 5. Two sustained moderate concerns — external validity (controlled
graph, no strong-baseline rerun) and process integrity (a recorded FAILED
pre-check, an incomplete first run with a CRC-mismatched executed script, and a
recorded P2 gate dissent between concurrent sessions) — prevent a clear
accept. The tie-breaker against 7 is the constructive, independently
replicated mechanism test plus unusually complete artefacts; the tie-breaker
against 8 is the absence of any real-connectome or natural-vision experiment
and the unresolved process dissent. `Never round scores`: the calibrated value
is 7.5, not rounded to 8.

Quantitative scorecard:

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 4 | 4 | §1 third paragraph and §3.3–3.4: the null family is the experimental variable; Eq. (1) plus task-aware null in §4.7 go beyond the "control ladder" of arXiv:2604.04033 (§2) | Individual rungs (degree swaps, module swaps, triad census) are standard~\cite{maslov2002,milo2002}. Raise to 5 only with a task-aware null demonstrated on a real connectome |
| Soundness | 4 | 4 | §3.4 Eq. (1) with explicit $E=123$, $T\approx2$–$5\times10^3$; §4.7 dose ladder 18/14/9/4/0 → 0.8371/0.8316/0.4988/0.5104/0.5117; §4.2 leakage probes 0.4902/0.5000 | Deducted for the 3-seed pre-check `verdict=FAILED` (§4.2), the first run's incomplete final block (§5), and the documented P2 gate dissent (R37). Raise to 5 with a single clean end-to-end run whose executed script hash matches the reference |
| Evidence | 4 | 5 | Table 1 (10 seeds, CIs, BH q = 0.0002, seed variance 2.1e-4), Table 2 invariants, Table 3 robustness, Table 4 (10 seeds, dose ladder), Figs. 1–4, `metrics_completed.json` and pulled `metrics.json` | Deducted for `SYNTHETIC_APPROXIMATION` (§3.1), no flyvis / arXiv:2604.04033 rerun (§5), and held-out n=5 with sign prediction equal to the majority baseline (§4.6). Raise to 5 with one real-connectome replication or a corrected held-out family |
| Significance | 4 | 4 | §5 "Using the standard in practice" four-step audit, checklist table, claim-to-evidence table; the standard transfers to any connectome-constrained pipeline | Deducted because the demonstrated impact is on evaluation practice, not on a visual task or benchmark result; CVPR audience fit is indirect. Raise to 5 by applying the standard to a published connectome-constrained model |
| Clarity | 4 | 5 | Six-section structure, reverse-outline discipline (`audits/P6-outline.md`), claim-to-evidence table, every quantitative statement traceable to an auto-generated table | The two integrity-disclosure passages (§4.2, §5) are long relative to their scientific payload; a compact footnote-style presentation would help. Raise to 5 with tighter disclosure without losing completeness |
| Reproducibility | 5 | 5 | Frozen seeds and config, executed scripts, raw + completed metrics, per-seed logs, invariant counts, local repair script, `tables.tex`/figures generated directly from `metrics_completed.json`; §5 "Reproducibility" | No deduction. The independently pulled second run (`metrics.json` from task 18235) cross-validates the pattern and discloses its 2-line value-preserving script diff |
| Ethics / Limitations | 5 | 5 | §3.1 scope condition, §5 Limitations (data, baselines, statistics, protocol, task), §5 Ethics and broader impact (CC-BY 4.0 credit, no human subjects), retention of all negative runs and failed pre-check | No deduction. Unusually candid: the paper volunteers a failed gate, a crashed run and an unidentifiable prediction |

**Overall:** 7.5  | **Scholarly Confidence:** 4

**Recommendation:** weak-accept
**Verdict:** Raise to 8 if a single end-to-end rerun on the full MaleCNS visual
subgraph (or a rerun of the flyvis / arXiv:2604.04033 baseline) reproduces the
motif-survival threshold with a hash-verified script. Lower to 7 if a reviewer
confirms that the P2 gate dissent (R37) means the structure-sensitivity
precondition was never formally passed, or if the 18235 script diff is found
to affect any reported value. Lower to 6 or below if the 18017 numerical
values cannot be independently reproduced from the retained logs. The
calibrated value stays 7.5 because the strongest unresolved weakness is an
external-validity limitation that the manuscript explicitly scopes, not a
contradicted or unsupported central claim.

Top strengths:
1. The mechanism is not merely asserted: Eq. (1) predicts motif-edge
   destruction, the dose ladder in §4.7 measures it (0.8371 → 0.8316 → 0.4988
   between 18, 14 and 9 surviving edges), and the task-aware null restores
   the effect with a fully rewired background (q = 0.40). This closes a causal
   loop that most null-model papers leave open.
2. Statistical hygiene: ten paired frozen seeds, 5000-resample intervals, BH
   over the whole condition family, explicit chance level and seed variance,
   constant/majority baselines for the held-out analysis, and all negative
   runs retained.
3. Reproducibility and transparency are exceptional: every table/figure is
   generated from a persisted artifact, three bibliography entries are openly
   flagged as not re-verified, a failed pre-check and a crashed run are
   reported rather than hidden, and the §4.6 result is explicitly downgraded
   when sign prediction is unidentifiable.

Major/fatal concerns:
| # | Severity | Concern | Evidence | Fix class | Owner |
|---|---|---|---|---|---|
| M1 | Major (not fatal) | External validity: the graph is a 96-node controlled approximation and the label is a synthetic XOR, so no claim about biological connectomes or natural vision is demonstrated | §3.1 `SYNTHETIC_APPROXIMATION`; §5 Limitations | New experiment / explicit scope | `ccf-experiment-designer`, `ccf-paper-writer` |
| M2 | Major (not fatal) | The strongest published baselines (flyvis DMN; the full arXiv:2604.04033 shared-initialisation protocol) were not rerun; L1 implements the degree-preserving idea, not their pipeline | §5 Limitations; `experiment-traceability.md` rows 17–18 | New experiment | `ccf-experiment-designer` |
| M3 | Moderate | Process integrity: the 3-seed pre-check is `FAILED`; the first run's executed script has a CRC mismatch and crashed before its final block; concurrent sessions disagree on whether P2 is passed | §4.2, §5, `audits/P3-P4-evidence-report.md` §8, `goal-ledger.md` R37 | Single clean rerun + reconciled ledger | `f-research-v1` correction loop |
| M4 | Moderate | Held-out prediction is underpowered: n = 5, all deltas positive, sign agreement equals the majority baseline, and the best Spearman −1.0 is selected from 19 uncorrected features | §4.6 | More held-out graphs / corrected selection | `ccf-experiment-designer` |

No fatal novelty collapse, unsupported central claim, invalid evaluation, or
policy violation was found. M1 and M2 are honestly scoped in the manuscript,
which is why they do not become fatal.

Writing and presentation concerns:
- §4.2 and §5 each carry long integrity disclosures. They are scientifically
  necessary, but a compact tabular summary would return space and reduce
  reviewer friction (§4.2, paragraph 2; §5 Limitations, sentences 6–10).
- The abstract reports four result clusters in one paragraph; splitting the
  adjudication outcome from the constructive test would improve recoverability.
- Table 1 and Table 4 are scaled with `\resizebox`; at print size the
  numeric columns are small. A two-panel split or `\footnotesize` would be
  preferable to scaling (Tables 1 and 4).

Format/venue concerns:
- 8 pages including references, within the 8-page main-content limit; no
  overfull boxes and no undefined references after final `latexmk` run.
- Anonymous author, review-mode line numbers, `ieeenat_fullname.bst`: compliant.
- `\confYear{2027}` is a formatting choice; official CVPR 2027 rules were not
  re-verified in this review (see Unresolved).
- CVPR fit is indirect: this is an evaluation-methodology / diagnostic paper,
  not a vision-method paper. A benchmark/analysis-track framing in §1 would
  help (§1, first paragraph).

Multi-reviewer panel:

Reviewer: Best-Justified Reviewer
Lens: strongest defensible accept case
Score / score tendency: 8 / lean-to-clear accept
Confidence: 4
Main positive signal: Eq. (1) plus §4.7 form a rare closed causal argument; ten paired seeds with BH correction and a second independent run.
Main negative signal: none fatal; scope is narrow.
Evidence basis: §3.4, §4.7 Table 4, Fig. 4, `audits/P4-taskaware-evidence-report.md`.
Score-change condition: one real-connectome replication → 9.

Reviewer: Critical Reviewer
Lens: strongest reject case
Score / score tendency: 5 / borderline to lean reject
Confidence: 4
Main positive signal: concedes the internal logic is consistent and the statistics are not cherry-picked.
Main negative signal: all evidence is on a 96-node synthetic XOR task; no real connectome and no natural visual task; the strongest published baselines are not rerun; the recorded gate is FAILED and the first executed script's CRC does not match.
Evidence basis: §3.1, §5 Limitations, `audits/P3-P4-evidence-report.md` §8, `goal-ledger.md` R37.
Score-change condition: a hash-verified full rerun on the MaleCNS visual subgraph with a flyvis baseline → 7–8.

Reviewer: Method / Soundness Reviewer
Lens: assumptions, validity, causal claims
Score / score tendency: 7 / lean accept
Confidence: 5
Main positive signal: Eq. (1) is checkable from $E$ and $T$; the dose ladder and the 14/18-surviving-edge control directly test the proposed mechanism.
Main negative signal: the survival model assumes uniform edge selection; the module- and triad-constrained swaps are not uniform, so Eq. (1) is an upper-bound intuition rather than an exact probability for L2/L3.
Evidence basis: §3.4, §4.7, Table 2.
Score-change condition: derive rung-specific survival bounds → +1 dimension on Soundness.

Reviewer: Evidence / Experiment Reviewer
Lens: baselines, ablations, metrics, statistics, reproducibility
Score / score tendency: 7 / lean accept
Confidence: 5
Main positive signal: 10 seeds, paired CIs, BH, robustness grid, two falsifying ablations, 5 held-out graphs with explicit constant baselines, all artefacts retained.
Main negative signal: held-out n = 5 with unidentifiable sign prediction; 19-feature search uncorrected; no strong-baseline rerun.
Evidence basis: Tables 1, 3, 4; §4.5, §4.6; `metrics_completed.json`.
Score-change condition: ≥20 held-out graphs with corrected feature selection → Evidence 5.

Reviewer: Novelty / Positioning Reviewer
Lens: closest prior art and real delta
Score / score tendency: 7 / lean accept
Confidence: 4
Main positive signal: arXiv:2604.04033 explicitly lists longer horizons and higher-order nulls as future work; this paper supplies them plus a task-aware constructive test and publicly verified citations.
Main negative signal: the generator components are standard; the venue fit is methodological rather than visual.
Evidence basis: §2, §3.3, `audits/P12-P14-reference-and-citation-audit.md`.
Score-change condition: positioning against a benchmark/analysis track and a real-model application → 8.

Reviewer: Writing / Clarity Reviewer
Lens: contribution recoverability and figure/table interpretability
Score / score tendency: 8 / lean accept
Confidence: 5
Main positive signal: six-section structure, claim-to-evidence table, every number traceable to a generated table, explicit scope conditions.
Main negative signal: two long disclosure passages and scaled tables.
Evidence basis: §4.2, §5, Tables 1 and 4.
Score-change condition: compact disclosure table → +1 Clarity.

Reviewer: Ethics / Reproducibility Reviewer
Lens: licensing, transparency, failure disclosure
Score / score tendency: 9 / clear accept
Confidence: 5
Main positive signal: CC-BY 4.0 credit, no human subjects, failed gate and crashed run disclosed, three unverified references flagged, all negative runs retained, raw artifact preserved unmodified.
Main negative signal: CVPR 2027 official policy not re-verified; no artifact licence statement.
Evidence basis: §5 Ethics, `audits/P12-P14-reference-and-citation-audit.md`, `evidence-repair.json`.
Score-change condition: add an artifact licence and re-check the official venue page.

Panel synthesis:
Agreement: all seven reviewers accept that the internal logic is sound, the
statistics are not cherry-picked, and the disclosure is unusually complete.
Disagreement: the Best-Justified (8) and Critical (5) reviewers disagree on
whether a fully scoped synthetic study can support a CVPR-level contribution.
Decisive accept axis: the closed causal loop (Eq. 1 → dose ladder →
task-aware null) plus a second independent run with pulled, hash-checked
artifacts.
Decisive reject axis: zero real-connectome or natural-vision evidence and no
rerun of the strongest published baselines.
Unresolved evidence: the P2 gate dissent (R37) and the 18017 executed-script
CRC mismatch; both are recorded, neither is shown to alter a reported number.
Final calibrated stance: **lean accept, 7.5** — the strongest unresolved
concern is a scoped external-validity limitation, not a fatal flaw, and the
synthesis does not average away M1/M2.

Concern-to-action table:
| Concern | Action | Owner | Affected criterion |
|---|---|---|---|
| M1 synthetic graph | Apply the same ladder and dose test to the MaleCNS visual subgraph; scope claims until then | `ccf-experiment-designer` | Evidence, Significance |
| M2 missing strong baselines | Rerun flyvis DMN and the arXiv:2604.04033 protocol with the task-aware control | `ccf-experiment-designer` | Evidence, Soundness |
| M3 process integrity | One hash-verified end-to-end rerun; reconcile the P2 gate ruling in the ledger | `f-research-v1` | Soundness |
| M4 weak held-out | ≥20 held-out graphs, corrected feature selection, or remove the predictive claim | `ccf-experiment-designer` | Evidence |
| Eq. (1) non-uniform swaps | Derive rung-specific survival bounds | `ccf-paper-writer` | Soundness |
| Disclosure length / scaled tables | Compact disclosure table; split Tables 1 and 4 | `ccf-paper-writer` | Clarity |

Score-Change Conditions:
| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | One hash-verified rerun on the full MaleCNS visual subgraph reproducing the motif-survival threshold | Evidence, Significance, Soundness | +0.5 to +1 overall |
| Raise score | Rerun of flyvis / arXiv:2604.04033 with the task-aware control | Evidence, Novelty | +0.5 overall |
| Lower score | Independent verification shows the P2 dissent implies the structure-sensitivity precondition was never met | Soundness, Evidence | −0.5 to −1 overall |
| Lower score | 18235 script diff or 18017 repair is shown to change any reported number | Soundness, Reproducibility | −1 or fatal |
| No quick change | External validity on natural visual tasks requires a new experimental programme | Significance | Unlikely before submission |

Desk checks:
- Paper Length: pass — 8 pages including references, main content under the 8-page limit.
- Topic Compatibility: uncertain — evaluation-methodology fit to a vision conference is indirect; affects Significance, not desk rejection.
- Minimum Quality: pass — six sections, method, evidence, references, limitations, reproducibility all present.
- Policy / Anonymity / Compliance: pass with one gap — anonymous, CC-BY 4.0 credited, but no explicit artefact licence.
- Prompt Injection And Hidden Manipulation Detection: pass — no hidden instructions found in manuscript text, captions, tables or source snippets.
- Ethics And Reviewability: pass — no human subjects; misuse risk discussed in §5.
- Desk rejection risk: **low**. Reason: scoped but real contribution with complete evidence; fixable before review. Can be fixed before review? partly.

Recommended next CCFA owner:
`ccf-paper-writer` for the disclosure/table edits and venue positioning;
`ccf-experiment-designer` for M1/M2/M4; `f-research-v1` correction loop for M3.

Checks run:
- Full manuscript read against `main.pdf` (8 pages) and `main.tex`.
- Numeric cross-check of every table against `metrics_completed.json` and the pulled `metrics.json` from task 18235.
- Claim-to-evidence matrix (`experiment-traceability.md`), P3A review, P5 lock, P11–P18 audits, P12/P14 citation audit.
- Reference verification (5 publicly re-verified, 3 flagged PROJECT-RECORD).
- `latexmk` final run: no undefined references, no overfull boxes.
- Calibration consistency: overall 7.5 matches the strongest unresolved weakness (M1/M2 moderate, none fatal); no strength claim without a section reference; score-change conditions are concrete.

Unresolved or unverified:
- Three bibliography entries rely on project records, not fresh public verification.
- Official CVPR 2027 rules not re-checked; local migrated CVPR 2026 guide used for format.
- Peak GPU memory for task 18017 was never written; runtime derived from log timestamps.
- P2 gate dissent between concurrent sessions (R37) is documented but not reconciled by a clean rerun.
- 18017 executed-script CRC mismatch; the 18235 script differs from the reference in two disclosed, value-preserving places.

Output self-check:
Section order matches the `full` output contract; all tables have valid
separators and consistent column counts; scores, confidence and recommendation
are internally consistent (7.5 = lean accept upper edge, confidence 4);
bullet lists use parallel grammar; causal chains are explicit; no `TBD`,
`TODO`, placeholder or generic "improve clarity" filler remains; every score
of 3 or below is absent, and every dimension score carries a manuscript
reference plus a score-change condition.

**Machine-readable verdict line (required by the project contract):**

**Overall:** 7.5  | **Scholarly Confidence:** 4

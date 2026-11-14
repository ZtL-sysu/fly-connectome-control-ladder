# CHECKPOINT — 20261114T042729Z-r122-post-review

- Task / agent / branch: `r109-harbor-sync` / `wb-main` / `agent/r109-harbor-sync/wb-main`
- Status: `completed` (work-state label, NOT scientific validation)
- Round: R122 heartbeat, independent recheck recovered 2026-11-14 12:25 +0800
- Created (UTC): 2026-11-14T04:27:29Z
- Input HEAD at manifest creation: see `manifest.json` (`input_git_head`)
- Immutable: the sixteenth checkpoint's bytes are **not rewritten**.

## Why this checkpoint exists

The **sixteenth** checkpoint (`20261114T040622Z-r122-first-hand-r4`) was
written while the fresh isolated sub-agent was running and truthfully stated
"recheck launched, not recovered, no verdict claimed". Following the
R117/R119/R120/R121 precedent, the recovered verdict and any append-only
corrections are published in this **new immutable checkpoint** instead of
editing the earlier one.

## Recovered independent recheck

Fresh isolated sub-agent `r122-independent-reviewer`, launched with **no
expected verdict, no score anchor, no conclusion anchor**. Single output
`R122-INDEPENDENT-REVIEW.md` (primary project, NOT uploaded):
**24,434 B**, SHA-256
`bcc78c27ab05ccee699199f8c01899f4a6bd912a6e24202a82397df080cace4e`,
one write, mtime 12:25:48, original unchanged. Recomputed only from the five
raw byte files with its own parsing logic; no collector/verifier import, no
R122 JSON as data source, round audit read LAST for defect grading.

- Verdict `REPRODUCIBLE_WITH_DEFECTS`
- `**G0 may be passed:** NO` / `**Scientific result claimed:** NO` /
  `**Forward pass performed:** NO`
- A–F: A 13/0, B 6/0, C 8/0, D 9/2, E 19/1, F 2/0 => **57 MATCH / 3 MISMATCH**
- 12 named overclaim categories: **CONFIRMED 0 / REFUTED 12**
- Defects: **HIGH 0 / MEDIUM 0 / LOW 2**; 0 fact error, 0 data inconsistency,
  0 fabrication; 0 expected-score / score-anchor tokens in the report
- Reviewer modified no existing file, wrote no other directory, ran no git.

## Three MISMATCHes (reviewer parsing-scope differences, not report errors)

- D: v2 body abstract 1,943 (report) vs 1,938 (reviewer, naive 1,941) — inline
  formula `46x` rendered via LaTeX `alttext` vs MathML glyphs + `<annotation>`.
  Reviewer measured the derived file itself as 1,943 => report accurate for its
  own artifact.
- D: similarity 0.4717 vs 0.4724 (naive 0.4719); **38 diff opcodes identical
  under all four scopes**.
- E: plaintext 45,960 vs 45,430 (full collapse) / 46,545 (no collapse) —
  whitespace-normalization degree; derived txt measured 45,960 by reviewer.

Reviewer's own script defect retained verbatim: initial `str.find()` for
`What remains open` sliced into the TOC (`False / 18 chars`), fixed with
`rfind()` to `True / 561 chars`. Confined to the reviewer's analysis script.

## Two LOW defects — all accepted, append-only corrections

Lodged in a **NEW** primary-project file `R122-POST-REVIEW-CORRECTION.md`.
Round audit, independent review, verification JSON, source manifest, all five
raw byte files and the sixteenth checkpoint are **byte-unchanged**.

- **C-1 [LOW | wording]** `R122-ROUND-AUDIT.md:75` calls a section 8
  quotation "verbatim"; it is a MathML-cleaned rendering, not a contiguous
  byte substring of the derived plaintext. Narrowed to "numeric tokens
  verbatim-matchable; full sentence presented after whitespace/MathML
  normalization". All tokens (E5/E6) and the section 8 conclusion unchanged.
- **C-2 [LOW | scope]** `R122-ROUND-AUDIT.md:60` "37 / 16 section headings"
  is correct under "all h1–h6 tags minus modal title and Abstract
  pseudo-heading", but includes the h1 document title, six h4 subheadings and
  the bibliography heading without declaring the counting scope. Reviewer's
  section/subsection count: v1 14 / v2 28; **v2 > v1 under every scope**.

Reviewer explicitly found **no** time-point / scope-mixing defect; the
round audit's separation of feed query time from entry-level version times
(section 4.1, verifier C5/C6) was noted as a strength.

## Additional first-hand facts (no conclusion change)

- v1/v2 `citation_title` differ; `citation_date` = 2026/09/21 for both;
  `citation_online_date` distinguishes 09/21 vs 09/22 — consistent with the
  abs page `Submission history` and atom entry-level timestamps.
- The atom `<id>` opaque token is an arXiv API query id, **not a credential**;
  five raw byte files have 0 local-path / credential-style hits.
- Reviewer's scope limitation accepted: concurrency guard, ledgers,
  `pipeline-state.json` readings and "all HTTP 200" are not verifiable from
  the five raw byte files alone; no truth claim made about them by reviewer.

## Content safety

Sanitized summary only: `evidence/R122-POST-REVIEW-SANITIZED.md`.
**Not uploaded**: independent review original (R117 precedent — only sanitized
summaries published; this report happens to have 0 local-path/email/credential/
scored-line hits), raw third-party HTML (contains an author email), primary
round audit, scripts, JSON, verification artifacts, full ledger, any dataset
/ weight / binary / third-party source / unpublished manuscript. Local paths
in public text use `<local>/`. `metrics.csv` carries real read-only
measurements.

## Strict boundary

- Zero gate promotions (G0 pending), zero self-certification, zero state
  write-back to registry / matrix / `pipeline-state.json`.
- EXEC LOCK: zero forward / inference / training / labels / dataset /
  EPE·l2 / scientific metric / new positive evidence.
- No `ccf-paper-reviewer full`, no numeric scored-verdict line, no
  self-assessed governing, no score / threshold / review / historical-byte
  change, no v4 contract, no P3 forward pass, no gate skipping, no
  `<=32h / K=45` authorization assumption, no 4090/L4/H20 claim.
- Primary project: no submission / commit / push. Private
  `ZtL-sysu/novix-platform` untouched. No merge / force push / branch
  deletion / Release. This checkpoint sits on the agent's own branch only.

## Result (unchanged)

**0 papers qualified, no COMPLETE written.** Governing remains
**R95 = 6.0 / Confidence 4.0**, `NOT_QUALIFIED` / `INCOMPLETE`.
Double gate: validator `NOT_QUALIFIED / 6.0 / >=7.0` (D1 pass D2 fail D3 fail
D4 pass D5 fail), guard `INCOMPLETE` (A2/A6, S1–S7 pending). Heartbeat ACTIVE
schedule unchanged. Step-3 precondition (substantive positive new scientific
evidence) unmet => no manuscript copy, no compile, no fresh isolated full
review.

## Next

1. Use `R120-CONSOLIDATED-DECISION-REGISTER.md` as the single decision entry
   (minimal set G1 + G4 + G10).
2. R4 registry registration and R2 matrix finalization need decisions G7/G6;
   heartbeat must not self-write.
3. Only admissible path remains G0–G8 -> validation -> handoff -> P0 ->
   P1A/P1B -> P2 -> P3 baseline-first real forward pass -> new manuscript
   copy -> compliant compile -> fresh isolated full review; COMPLETE only at
   >= 7.0 with QUALIFIED + COMPLETE.

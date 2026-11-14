# R122 — isolated independent recheck recovered + append-only corrections (sanitized public summary)

Status: `READ_ONLY_FIRST_HAND_SOURCE_FREEZE_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
Date: 2026-11-14 (heartbeat R122, independent recheck recovered)
Primary project artifacts (raw bytes, scripts, JSON, round audit, corrections,
independent review original) are **NOT uploaded**. Local paths are written as
`<local>/`.

## Recheck delivery

The fresh isolated sub-agent `r122-independent-reviewer` was launched with
**no expected verdict, no score anchor, no conclusion anchor**. Its single
output `R122-INDEPENDENT-REVIEW.md` is **24,434 B**, SHA-256
`bcc78c27ab05ccee699199f8c01899f4a6bd912a6e24202a82397df080cace4e`,
one write, mtime 12:25:48, original unchanged. It used only the five raw byte
files with its own parsing logic — no import of the collector/verifier, no
R122-produced JSON as a data source — and read the round audit only LAST for
defect grading.

- Verdict: `REPRODUCIBLE_WITH_DEFECTS`
- `**G0 may be passed:** NO` / `**Scientific result claimed:** NO` /
  `**Forward pass performed:** NO`
- A–F group MATCH/MISMATCH: A 13/0, B 6/0, C 8/0, D 9/2, E 19/1, F 2/0
  => **57 MATCH / 3 MISMATCH**
- 12 named overclaim categories: **CONFIRMED 0 / REFUTED 12**
- Defects: **HIGH 0 / MEDIUM 0 / LOW 2**; fact errors, data inconsistencies
  and fabrication: **0**
- Expected-score / score-anchor tokens inside the report: **0**
- Reviewer modified no existing file, wrote no other directory, ran no git.

## Three MISMATCHes — accepted as reviewer parsing-scope differences

| # | report value | reviewer value | cause |
|:--|:--|:--|:--|
| D | v2 body abstract **1,943** chars | **1,938** (naive 1,941) | inline formula `46x`: reviewer renders LaTeX `alttext`, this round's derived file keeps MathML glyphs + `<annotation>` text. Reviewer measured the derived file itself as 1,943 => the report value is accurate for its own artifact. |
| D | similarity **0.4717** | **0.4724** (naive 0.4719) | same cause, delta <= 0.0007; **38 non-equal opcodes identical under all four scopes**. |
| E | plaintext **45,960** chars | **45,430** (full collapse) / 46,545 (no collapse) | different whitespace-normalization degree; reviewer measured the derived txt itself as 45,960 => accurate for its own artifact. |

None is a report error, a data inconsistency, or fabrication. Core findings
hold under every scope: two differently worded v2 abstracts, similarity ~0.47,
38 diff blocks, v1 differing from both.

**Reviewer script defect retained verbatim, not hidden**: its first version used
`str.find()` for `What remains open`, slicing into the TOC and giving
`section8_two_gaps_remain=False / 18 chars`; switching to `rfind()` fixed it to
`True / 561 chars`. This defect existed only in the reviewer's analysis script
and was fixed before its final numbers.

## Two LOW defects — all accepted, append-only corrections

Both are lodged in a **NEW** primary-project file
`R122-POST-REVIEW-CORRECTION.md`; the round audit, the independent review,
the verification JSON, the source manifest, all five raw byte files and the
sixteenth checkpoint are **byte-unchanged**.

- **C-1 [LOW | imprecise wording]** `R122-ROUND-AUDIT.md:75` labels a section 8
  quotation "verbatim": that quotation is a MathML-cleaned rendering, not a
  contiguous byte substring of the derived plaintext (where `+ 0.033 +0.033
  [ 0.015 , 0.050 ] [0.015,0.050]` appears because visible glyphs and
  `<annotation>` TeX coexist). Narrowed to "numeric tokens verbatim-matchable,
  full sentence presented after whitespace/MathML normalization". Semantics,
  all numeric tokens (verifier E5/E6) and the section 8 conclusion unchanged.
  Related scope note: `7.3 ...` and `9 Limitations` use U+2002/U+2006 Unicode
  spaces in the raw bytes (0 strict-ASCII matches, 2 after normalization);
  `Two gaps remain.` is plain ASCII (1 raw-byte match).
- **C-2 [LOW | undeclared scope]** `R122-ROUND-AUDIT.md:60` "37 / 16 section
  headings" is correct under "all `<h1>`–`<h6>` tags minus modal title and
  Abstract pseudo-heading", but this count includes the h1 document title, six
  h4 paragraph subheadings and the bibliography heading, and the label does not
  declare the counting scope. Reviewer's section/subsection-level count is
  v1 14 / v2 28; **v2 > v1 holds under every scope** (E15/E16 unaffected).

The reviewer explicitly found **no** time-point / scope-mixing defect and noted
that the round audit section 4.1 and verifier C5/C6 separating feed query time
from entry-level version times is a strength of the report.

## Additional first-hand facts registered (no conclusion change)

- v1/v2 `citation_title` differ; `citation_date` is **2026/09/21 for both**;
  the field distinguishing the versions is `citation_online_date` (09/21 vs
  09/22). Consistent with the abs page `Submission history` and atom
  entry-level timestamps reported in the round audit.
- The atom `<id>` opaque query token is an arXiv API query id, **not a
  credential**; the five raw byte files contain no local absolute path and no
  Bearer / ghp_ / api_key style secret.
- Reviewer's scope limitation (accepted): the round audit's concurrency-guard,
  ledger, `pipeline-state.json`, guard-ledger readings and the "all HTTP 200"
  acquisition statement are not verifiable from the five raw byte files alone;
  the reviewer made no truth claim about them. Those readings were collected
  independently by the primary session (round audit section 7 + closing check).

## Unchanged

- governing **R95 = 6.0 / Confidence 4.0**; validator `NOT_QUALIFIED / 6.0 /
  >=7.0`, guard `INCOMPLETE`.
- **0 papers qualified, no COMPLETE written**; G0 `pending`, zero gate
  promotions, zero self-certification, zero state write-back.
- Gate/evidence-layer recheck, **NOT** `ccf-paper-reviewer full`: no scored
  `**Overall:**` line, no numeric paper score, no governing change.
- The **sixteenth checkpoint** truthfully claimed the recheck was launched and
  not recovered; that statement was true at write time and its bytes are **not
  rewritten**. This **seventeenth immutable checkpoint** carries the recovered
  verdict and append-only corrections.
- The independent review original is **NOT uploaded** (R117 precedent: only
  sanitized summaries are published), even though this particular report has
  0 local-path / email / credential / scored-line hits.

## Next

1. Use `R120-CONSOLIDATED-DECISION-REGISTER.md` as the single decision entry
   (minimal set G1 + G4 + G10).
2. R4's registry registration and R2's matrix finalization need decisions
   G7 / G6; the heartbeat must not self-write.
3. Only admissible path remains G0–G8 in order -> validation -> handoff ->
   P0 -> P1A/P1B -> P2 -> P3 baseline-first real forward pass with substantive
   positive new evidence -> new manuscript copy -> compliant compile -> fresh
   isolated full review; COMPLETE only at >= 7.0 with QUALIFIED + COMPLETE.

**New lessons**: (i) quoting MathML-rich text must declare normalization
scope — "verbatim" applies only to tokens or explicitly normalized text;
(ii) count-like numbers must state their counting scope (tag count vs section
count); (iii) char counts / similarity / plaintext length must be bound to a
concrete derived artifact; (iv) an independent reviewer's MISMATCH must first
be checked for parsing-scope differences before being called either a data
error or a report error.

A checkpoint `completed` is a work-state label, not scientific validation.

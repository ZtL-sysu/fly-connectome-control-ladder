# R120 — isolated independent recheck, sanitized summary

**Nature**: gate/evidence-layer recheck by a **fresh isolated sub-agent** with
no access to the authoring conversation and no expected conclusion or score
anchor supplied. **NOT** a `ccf-paper-reviewer full` manuscript review; no
scored-review verdict line, no numeric paper score, no change to governing.
Network requests: 0. Local absolute paths are `<local>/`.

This is a **sanitized summary**. The independent report original (which quotes
two local paths), the primary-project scripts, JSON, byte-identical isolated
copies, full ledger and gate readouts stay in the private workspace and are
**not uploaded**.

---

## Verdict

- Final report: **23,074 B**, SHA-256
  `c7c613c54bd08cad1b945c5affcdf371522430e63fff84d702ac86625cf3d9ea`,
  one write, no intermediate state, mtime `2026-11-14T08:55:00 +0800`;
  original text unchanged.
- First line: `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific
  result claimed: NO`; second line `Forward pass performed: NO`.
- The reviewer used **no** R120-produced JSON as a data source; every reading
  was recomputed from original source bytes. A–H, J and L **MATCH**; **I and K
  MISMATCH**.
- **12 named overclaim / self-certification categories (a)–(l):
  CONFIRMED = 0, REFUTED = 12.** No fabrication, no data inconsistency, no
  score line, no forward pass, no gate promotion, no existing file modified
  by the reviewer.
- **7 defects (1 HIGH / 3 MEDIUM / 3 LOW / 0 fabrication)**, all accepted as
  append-only corrections in the private `R120-POST-REVIEW-CORRECTION.md`.

## Central result (after corrections)

Standing step-1 item ② ("U6/W2 versioned contract handling of the guidance
handoff → create a NEW f-research-v1 P0 state, do not insert P stages into the
guidance state") was **already executed at R108 as a DRAFT scaffold**. The
reviewer confirmed the central characterization `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED`
is **accurate — neither overclaimed nor underclaimed** — and independently
recomputed the three distinct state namespaces, the 26-stage all-pending
scaffold, the zero P-stage insertions in the guidance state, the DRAFT contract
status, the G0-pass-criterion DRAFT, the stale baseline matrix, the live
validator/guard config and both gate readouts.

Two claims were corrected:

- **W1 (HIGH, substantive withdrawal)** — the literal claim "no newer file
  with a numeric scored-verdict line exists anywhere in the project" was
  **refuted**: the reviewer scanned 13,704 files and found 647 literal lines /
  109 inline numeric lines / 14 line-start numeric lines across 12 files,
  including files newer than r95 that quote or copy existing scores. R120's own
  collector had left the corresponding field as an **empty, never-populated
  placeholder** with no verifier check, so the claim had no first-hand
  byte-anchored evidence. The closure was a **new first-hand recomputation
  artifact, not a wording patch**: `R120-I2-EVIDENCE.py/json` scanned 13,706
  files (662 literal / 109 inline / 14 line-start across 12 files) and found
  **39 files / 83 inline lines newer than r95**, all quotations or copies of
  existing scores. The narrowed, evidence-backed claim — **zero new
  independent full reviews after r95 and zero newly produced numeric verdict
  lines this round** — is supported by `qualifying_files = []`,
  `supported = true`. The 13,704 vs 13,706 difference is a scan-time effect
  (new R120 artifacts + append-only bookkeeping), **not** a data inconsistency.
- **W2 (MEDIUM)** — "first-ever / never" historical negatives in the report
  title and decision register were narrowed to a **scope observation**: "no
  precedent found among this round's visible artifacts". R111 line 26 is a
  documented prior observation of prompt/ledger drift.

Other accepted defects: W3 the four R107 restatements are different
wording/numbering versions (a spliced quotation, not a verbatim single line;
line numbers 175/175/116/180 are correct); W4 the **whole** item ② must not
be called "satisfied" — only the "create P0 state / no P stages in guidance
state" sub-clause exists as a draft scaffold, while "versioned contract
handling of the guidance handoff" is unmet (handoff still pending); W5 "12"
was a **file** count, exact is 14 lines / 12 files; W6 there are 3 byte-identical
closure copies on disk, the R120 evidence set collected 2; W7 R115 added no
new gate-owner decision, the "R115/R116" grouping is an evidence-source merge.

## Scope and boundary

All seven defects are wording, scope, transcription, counting-unit or
first-hand-evidence-gap issues; every byte-level value in groups A–H and J
(line numbers, sizes, SHAs, stage statuses, criterion text, D1–D5 booleans,
S1–S7 counts, gate readouts) matched the original source bytes. No historical
byte, published checkpoint, sanitized summary or independent-review original
was rewritten; all corrections are append-only. The twelfth checkpoint was
written while the recheck was in flight and truthfully claimed no verdict;
its bytes are **not rewritten** — this **thirteenth immutable checkpoint**
carries the recovered conclusion and corrections.

Step-3 precondition (substantive positive new scientific evidence) remains
unmet ⇒ no manuscript copy, no 9-page compile, no fresh isolated full review.
**0 papers qualified, no COMPLETE, governing still 6.0 / Confidence 4.0,
`NOT_QUALIFIED` / `INCOMPLETE`, G0 pending.** A checkpoint `completed` is a
collaboration work state, **not** scientific validation.

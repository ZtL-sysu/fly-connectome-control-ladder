# R121 — Sanitized summary: recovered independent recheck and append-only corrections

- Round: R121, recovered 2026-11-14 10:42 +0800.
- This is the **fifteenth** immutable checkpoint. The fourteenth checkpoint was
  written while the fresh isolated sub-agent was still running; it truthfully
  stated "recheck launched, not recovered, no verdict claimed" and explicitly
  reserved the recovered conclusion for a new checkpoint. Its bytes are **not
  rewritten**.
- The independent report original is **NOT uploaded** (it quotes 2 local
  absolute paths). Only this sanitized summary is published.

## Recovered independent recheck

- Final report (private working tree): **28,736 B / 237 lines**, SHA-256
  `9650a024f84c9b1ec308db4a96c18fee26e5cfd67e3b73b0b9a50f1a0891200c`,
  mtime `2026-11-14 10:42:30`, one write, no intermediate state, original
  unchanged.
- Verdict: `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific
  result claimed: NO | Forward pass performed: NO`.
- Groups A–H (governing-review anchors, seven prior rounds, three raise
  conditions, both machine gates, main-line state, numeric scored-verdict
  scan) were recomputed from original source bytes using the reviewer's own
  logic: **all MATCH**. The reviewer used **no** R121-produced JSON as a data
  source and read the round audit only last, for defect grading.
- **12 named overclaim / self-certification categories (a)–(l):
  CONFIRMED = 0, all 12 REFUTED.** No fabrication, no new scored line, no
  forward pass, no gate promotion, no threshold change, no self-authored
  governing review, no assumption of the ≤32h / K=45 panel authorization, no
  4090 / L4 / H20 claim, no data inconsistency.
- The reviewer explicitly found **no overclaim** in R121's negative closure
  finding, which is scoped to "read-only audits of this class" and states the
  only admissible path remains a P3 real forward pass followed by a fresh
  isolated full review. It also confirmed that an RTX 4090 string inside an
  old metrics file is existing device metadata, not a capability claim.

## Six items — all accepted, append-only

Graded **HIGH = 0, MEDIUM = 1, LOW = 3**, plus 1 already-disclosed snapshot
observation and 1 declared review-scope limitation. All are wording, scope,
time-point, or label-precision issues; none changes any first-hand number,
byte integrity, the three `satisfied = False` conditions, either gate reading,
gate state, or the governing score.

| ID | Grade | Accepted correction |
|:--|:--|:--|
| J-1 | MEDIUM | "14 line-start numeric scored-verdict lines" was the **wake-time (10:03)** truth. At audit-write time (10:28), after this round's own `isolated/` byte-identical copy was created, the count is **15 lines / 13 files** (main session re-measured). Precise wording: 14 at wake, 15 afterwards; both later-than-r95 files are byte-identical to r95, `new_governing_candidates = 0`, no new score. The verifier already separated the pre-existing copy from this round's self-produced copy; the imprecision was in the round-audit summary phrasing. |
| J-2 | LOW | Of the 4 `True` synthetic/controlled files, only 2 carry `data.source = SYNTHETIC_APPROXIMATION`; the other 2 are `p3_p4_taskaware/metrics_from_trajectory.json` mirrors without that field. One further `False` file without a source field was not enumerated. Narrowed; all 6 `REAL_MALECNS_VISUAL_SUBGRAPH` files remain `False`. |
| J-3 | LOW | R120's token is `READ_ONLY_RECONCILIATION_…` (with underscore), not literally `READONLY…`. Narrowed to "7/7 declare read-only semantics (`READONLY…` or `READ_ONLY…`) + NOT_GATE_PASS + NOT_SCIENTIFIC_RESULT"; the v2 collector already matches both spellings. |
| J-4 | observation | 20 of 21 `isolated/` copies still match current sources; `goal-ledger.md` differs only by a **pure append** (+9,574 B R121 ledger section) with the first 687,472 B byte-identical. Already disclosed as a capture-time snapshot in the round audit; it corroborates "no historical byte rewritten", and is not an unnoticed defect. |
| J-5 | scope | The reviewer was constrained not to read any R121 JSON, so it did not independently verify the verifier's internal "74/74" count. Accepted: 74/74 is a **same-host necessary-consistency check, never an independent cross-validation** (stated verbatim in the verifier's `scope_note` and the round audit). The genuine independent work is the A–H recomputation. Not an audit defect. |
| J-6 | LOW | Line 4's governing score is a paraphrased status summary, not a verbatim quotation. The exact verbatim form is given in the round audit §4.1. |

Corrections live in the private `R121-POST-REVIEW-CORRECTION.md`.
`R121-ROUND-AUDIT.md`, the independent report original, both v1/v2 RAW and
VERIFICATION files, the `isolated/` copies, and the fourteenth checkpoint are
all **byte-unchanged**.

## Result and boundaries unchanged

This is a **gate / evidence-layer recheck, NOT a `ccf-paper-reviewer full`
manuscript review**: no scored-verdict line, no numeric paper score, no
governing change. EXEC LOCK held; zero gate promotion, zero
self-certification, zero state write-back (G0 pending). No `ccf-paper-reviewer
full` launched; no threshold change; no v4 contract; no assumption of the
confirmation-panel authorization; no 4090/L4/H20 capability claim. The
primary project was not submitted, committed, or pushed.

**0 papers qualified, no COMPLETE, governing R95 = 6.0 / Scholarly
Confidence 4.0, `NOT_QUALIFIED` / `INCOMPLETE`.** Heartbeat ACTIVE, schedule
unchanged. A checkpoint status of `completed` describes work state only,
never scientific validity.

# R107 目标迭代 — 成功标准锁定（用户授权）

Date: 2026-11-13 08:0x +0800. Mode: `relentless-goal-executor` RGE1 **目标迭代**
(user-initiated goal iteration, with explicit user authorization).

## Authorization

User message 2026-11-13 08:03:
「更新一下目标，大方向不变，ccfa独立评审改为全文达到7分及以上即可。你相应的定时任务，心跳啥的改一下吧」

This is a **user-authorized goal iteration**, not an in-loop threshold
relaxation. The distinction matters: the RGE "no threshold lowering" guard
forbids the *executor* from weakening a target after a failed round; it does not
bind the *goal owner*. All prior rounds were executed against the old standard
and remain valid historical evidence. No historical round, review, contract or
validator verdict is rewritten, deleted or retroactively reinterpreted.

## Old vs new

| | Old (R51/R59) | New (R107) |
|:--|:--|:--|
| Independent full review Overall | **strictly > 8.0** (8.0 does not qualify) | **>= 7.0** (7.0 qualifies) |
| Comparison operator | `>` | `>=` |
| Validator default `--threshold` | `8.0` | `7.0` |
| guard A6 | `g > 8.0` | `g >= 7.0` |
| Goal name / direction | one CVPR 2027 CCF-A manuscript | **unchanged** |

**Big direction unchanged**: one complete CVPR 2027 main-conference manuscript,
evidence-first, real visual positive effect as the scientific route, no
submission / commit / push, no fabricated results, no edited on-disk reviews.

## Success-criteria evidence list (RGE1, three questions each)

**S1 — Independent full review score.**
- Observable change: a **new** `ccfa-review-reports/paper-null-ladder-r<NN>-independent-review-<date>.md`
  written by a **fresh isolated sub-agent** `ccf-paper-reviewer full`, containing
  exactly one `**Overall:** X  | **Scholarly Confidence:** Y` line with `X >= 7.0`.
- Judge: `readonly-validator/validate_single_paper.py` (machine, read-only) plus
  the pre-existing "LATEST independent full review governs" rule.
- **Not achieved if**: X < 7.0; the line is absent or duplicated; the report is
  self-authored by the main session; a historical 7.5 report (R47/R49) is
  retroactively promoted to governing; the report is edited after scoring; or a
  score is inferred from a proposal/idea/gate review instead of a full-manuscript
  review.

**S2 — Machine gates.**
- Observable change: validator emits `QUALIFIED` with
  `score_meets_threshold=true`, and `guard check` emits `COMPLETE`.
- Judge: the two validators, run read-only.
- Not achieved if: either still `NOT_QUALIFIED` / `INCOMPLETE`, or A2/A6 fail.

**S3 — Manuscript integrity.**
- Observable change: the scored manuscript exists as compilable TeX + PDF under a
  run root, 9 pages, p8 complete Conclusion, p9 only LLM placeholder +
  References, 0 Overfull / 0 undefined, `main.tex` == `paper.tex` byte-identical.
- Judge: `paper-compile` / local compile check.
- Not achieved if: not compiled, stale duplicate, or workflow text in the body.

## Explicit anti-gaming clause (important)

The current governing score is **R95 = 6.0**. Historical 7.5 reports (R47, R49)
remain on disk and remain **historical**. Under the unchanged
"LATEST independent full review governs" rule, lowering the threshold to 7.0
does **not** make any past 7.5 report governing and does **not** declare the
current paper qualified. Reaching S1 requires a **new** full independent review
of a **revised** manuscript. No review is deleted, hidden, edited or re-dated.

## What is changed (live configuration only)

1. `readonly-validator/validate_single_paper.py`: default threshold 8.0→7.0,
   `>`→`>=` in both `d3_review` and `final_pass`, contract / acceptance_rule /
   governing_review strings updated, backward-compatible
   `score_gt_threshold` retained alongside new `score_meets_threshold`.
2. `guard/criteria-null-ladder.json`: A6 text + hardcoded `g>8.0`→`g>=7.0`,
   meta.task description, plus a new `notes` entry for R107.
3. `guard/ledger-null-ladder.json`: `meta.task` description only.
4. Heartbeat automation `b88e368e…`: prompt success criterion and all
   `>8.0` references → `>=7.0`; name updated.
5. `goal-ledger.md` (append R107) and `.workbuddy/memory/2026-11-13.md` (append).

## What is deliberately NOT changed (historical evidence)

- All `ccfa-review-reports/*.md` — every past independent review, byte for byte.
- All past `goal-ledger.md` rounds (R1–R106) — append-only.
- `guard/criteria.json`, `guard/ledger.json`,
  `readonly-validator/validate_qualified.py`, `scripts/register_r*.py` — these
  belong to the **old >=5-paper portfolio goal** (superseded historical target)
  or are historical round-registration scripts. Their 8.0 strings are historical
  facts, not live acceptance criteria.
- `guidance-v2.md`, `execution-contract-v1/v2/v3.md`, `protocols/` — frozen
  contracts; a future versioned contract (v4) may restate the new criterion, but
  no existing contract is retroactively edited.
- Frozen identities, seeds, K=45, stop rules, Novix routing notes.
- `qualified_paper.json` (6.3 stale snapshot) — not refreshed.

## Status after this iteration

Validator re-run + guard re-run recorded in `goal-ledger.md` R107. The expected
result with governing 6.0 is still `NOT_QUALIFIED` / `INCOMPLETE` — **the goal
is not achieved by changing the criterion**. Zero papers qualified, no COMPLETE
written. Stop gates remain ① achieved ② user stop.

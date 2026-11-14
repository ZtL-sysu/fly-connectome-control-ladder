# R121 — Sanitized summary: governing review's own score-change conditions vs. the last seven rounds

- Round: R121, 2026-11-14 10:02–10:3x +0800 (heartbeat, ACTIVE, unchanged cadence).
- Kind: `READONLY_SUCCESS_CRITERION_CLOSURE_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`.
- Status: **no paper accepted, no COMPLETE written.** Governing independent full review
  is still R95 = 6.0 / Scholarly Confidence 4.0. Validator `NOT_QUALIFIED` (6.0,
  threshold 7.0, `>=`), guard `INCOMPLETE` (A2 and A6 failing, all 7 steps pending).
- All primary artifacts live in the private working tree under
  `<local>/auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/success-condition-R121/`.
  Only this sanitized summary is published here.

## Why the lane changed

R114–R120 each audited a different process/infrastructure layer. Earlier rounds had
already flagged "keep producing evidence documents" as an isomorphic loop three times.
R121 instead reconciles the **governing independent full review's own score-change
taxonomy** against (a) the seven rounds' declared output classes, (b) first-hand
evidence for the three "raise score" conditions, (c) the two machine gates, and
(d) the ordered gate chain. This is the layer closest to the success criterion and
had not been audited in the visible round artifacts.

## The governing review's own rules (byte-anchored, verbatim)

- §13 "No quick change": process / disclosure / format work
  "不新增支持中心主张的科学证据" ⇒ "不改变 evidence-capped overall";
  clearing the administrative blocker only restores a submittable state.
- §13 "Raise score" and §15 "Raising the score would require": the Overall can
  move up from 6 only via three **new scientific evidence** items (a)(b)(c);
  "单项 +0.5；三项齐备 Overall 6→7~7.5".
- §8 M1 "需新的真实图实验确认机制迁移（非 prose 可修）"; M2
  "无法靠 prose 补出视觉贡献"; §11 Evidence = 3, Significance = 3;
  the tie-breaker states that ≥3 decisive concerns block Overall 7.

## First-hand status of the three raise conditions (all unsatisfied)

| Condition | First-hand evidence | Result |
|:--|:--|:--|
| (a) real-graph mechanism transfer | 6 `REAL_MALECNS_VISUAL_SUBGRAPH` metrics files have `hypothesis_supported = False`; 4 `SYNTHETIC_APPROXIMATION` (96-node XOR / task-aware controlled) files are `True` — exactly the surrogate M1 excludes | not satisfied |
| (b) strong baseline rerun | version-locked manuscript (40,175 B, md5 `e4bfad51…158c6`, matching R95 §1) states verbatim at line 637 "We did not rerun their flyvis stack and make no benchmark-reproduction claim."; 0 flyvis/toposens rerun metric files | not satisfied |
| (c) real visual task changes a conclusion | `mlp_baseline.mean_acc = 0.97222…` dominates; real minus degree-preserving-null delta `−0.000463`, CI95 includes 0; R95 §8 M2 records a negative result | not satisfied |

## Seven prior rounds vs. that taxonomy

7 of 7 round audits declare, over their full text,
`READONLY…NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`; 7 of 7 claim no new positive
evidence, no gate passed, and contain no line-start numeric `**Overall:**` line.

## Negative closure finding (the round's only substantive conclusion)

By the governing review's **own** rules — not by the main session's judgement —
R114–R120 and read-only audits of this class fall under §13 "No quick change" and
therefore **cannot**, even in principle, raise the evidence-capped Overall from 6.0
to the required >= 7.0. This is a criterion-level impossibility, not slow progress.

The only admissible path remains the ordered gate chain G0–G8 → validation →
handoff → P0 → P1A/P1B → P2 → a baseline-first P3 real forward pass producing
substantive positive new evidence → a new manuscript copy → compliant compilation
→ a fresh isolated full review. Lowering the threshold does not lower the
evidence bar. The blocking decisions remain the minimum set `G1 + G4 + G10` in the
R120 consolidated decision register, all requiring the designated gate owner / user.

## Reproducibility

- `<local>/…/success-condition-R121/R121-collect.py` + `R121-RAW-v1.json` (retained)
  → `R121-collect-v2.py` → `R121-RAW-v2.json` (18 byte-exact review needles,
  21 sources, 21 byte-identical isolated copies).
- `R121-verify.py` does not import the collector and reads no R121-produced JSON;
  it recomputes from original source bytes: **74 checks / 74 MATCH / 0 MISMATCH**.
- Six v1 script defects (enumeration, transcription, and a self-check regex) are
  documented in `R121-V1-DEFECTS.md`; both v1 and v2 readings are retained. All are
  script-judgement defects, not data inconsistencies.

## Boundaries

EXEC LOCK: zero forward pass / inference / training / labels / EPE-l2 / scientific
metrics; zero network. Zero gate promotion, zero self-certification, zero state
write-back (G0 still `pending` with empty `inputs`/`evidence`). No historical bytes,
reviews, scores, thresholds, manuscript, gates, frozen artifacts, matrix, registry,
or gate config were modified. No `ccf-paper-reviewer full` was launched; no new
numeric `**Overall:**` line produced; no self-authored governing review; no gate
skipping; no v4 contract created; no assumption of the ≤32h / K=45 confirmation
panel authorization; no 4090 / L4 / H20 capability claim. The primary project was
not submitted, committed, or pushed.

A checkpoint status of `completed` describes work state only, never scientific
validity. This repository is a public, sanitized collaboration record; datasets,
weights, third-party source, unpublished double-blind manuscripts, credentials and
local absolute paths are deliberately absent.

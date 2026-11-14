# Execution contract v3 — Novix execution route, 2026-11-12

Versioned run-local contract. Supersedes v2 for the **execution location only**.
v1 and v2 remain historical evidence and are not modified.

## Trigger

User instruction 2026-11-12 (WorkBuddy main session):
"我把你这个研究交给codex做了做…按照gpt给出的最新的guidance，协议，接着往下做。
实验你就在 @skill:novix-platform 上做，做实验和更新协议日志的标准用我的
@skill:f-research-v1 @skill:f-guidance-builder-v1 @skill:relentless-goal-executor
死磕目标为8分 ccfa独立评审".

This is a **route authorization**, not a result, not a score change, and not an
approval of the confirmation panel.

## What changes from v2

| Item | v2 | v3 |
|:--|:--|:--|
| Development execution location | local Conda/MPS only (<=4 cumulative hours) | **Novix platform is the user-designated experiment location**; local evidence remains valid and is reused only after identity/applicability checks |
| Novix use | authorization persists but "no identical retry warranted" | a **non-identical route** was found and verified (see route diagnosis); identical retries remain prohibited |
| Scientific protocol | frozen | **unchanged, frozen** |
| Prospective identities, E1/E2/E3, K=45, comparators, stop rules | frozen | **unchanged** |
| Confirmation (<=32h) | not authorized | **still not authorized** |
| Local <=4h development cap | authorized | retained as a cap on local work; does not authorize confirmation |

## Binding constraints carried forward verbatim

- Method family, public-data constraints, evidence/integrity requirements,
  protected historical artifacts, local artifact root, no-publish/no-commit rules
  from v1/v2 remain binding.
- No silent CPU neural-operator fallback. No neural/decoder optimizer or refitting.
- Freeze generator, identities and parameters before query; seal forecasts before
  the actual-null outcome process. Test isolation is unchanged.
- `expected_strong` (K=45 one-sided directional gates at family-wise alpha .05)
  is unchanged and is NOT relaxed.
- Failed experiments are data: keep all receipts, failures, zero-step tasks and
  negative outcomes. No result is fabricated; no threshold is lowered.
- Independent full-manuscript review receives frozen evidence only, with no
  requested score or score anchors. Acceptance requires Overall > 8.0 under the
  pre-existing "latest independent full review governs" rule.

## Route diagnosis (this session, diagnostic only)

`novix/route-diagnosis-20261112-v1.json` records seven dispatches. Finding:
`--resource-pool` is the single consistent trigger of `AI_SERVICE_CALL_FAILED /
ControlPlaneFailure` at steps 0. Tasks omitting it finish normally. This corrects
the earlier interpretation that the whole platform was unavailable; the three
historical failures (21892/21897/21945) are preserved and are NOT claimed as
recovered. GPU/4090 capability on the working route is not yet established.

## Ordered pipeline discipline (f-guidance-builder-v1)

`CCFA-startup` is passed under v2. `pipeline_state.py --before G0` returns PASS.
G0–G8, validation and handoff each require their own substantive evidence and
ordered review; none is marked passed by this contract. In f-research-v1, P0,
P1A/P1B precede scientific P2; P5/P5A block drafting until the accepted
strong-result contract is met. No stage is skipped, reordered or inferred.

## Authorized actions under v3

- Read-only platform/state checks and minimal routing diagnostics.
- Development-stage, pre-confirmation engineering and analytical pilot work on
  Novix, using frozen scripts with SHA verification, producing artifacts that
  are pulled back into this run root and independently recomputed.
- Protocol-log updates: `guidance-pipeline-state.md`, `pipeline-state.json`,
  `correction-ledger.md`, `goal-ledger.md`, and the session work log.

## Explicitly NOT authorized

- Confirmation panel / <=32h confirmation execution.
- Any real model outcome, competence claim, null-response claim or manuscript
  claim from engineering diagnostics.
- Score changes, threshold changes, deletion of reviews or failed artifacts.
- Commit, push, submission, publication.

## Success criterion (locked, unchanged)

A fresh isolated `ccf-paper-reviewer full` independent report on the final
actual manuscript with `**Overall:** X`, X strictly > 8.0, plus
`readonly-validator/validate_single_paper.py` QUALIFIED and guard COMPLETE.
Current governing remains R95 = 6.0 / NOT_QUALIFIED. Zero papers qualified.

# CHECKPOINT — 20261114T040622Z-r122-first-hand-r4

- Task / agent / branch: `r109-harbor-sync` / `wb-main` / `agent/r109-harbor-sync/wb-main`
- Status: `completed` (work-state label, NOT scientific validation)
- Round: R122 heartbeat, 2026-11-14 11:47–12:0x +0800 (unattended)
- Created (UTC): 2026-11-14T04:06:22Z
- Input HEAD at manifest creation: see `manifest.json` (`input_git_head`)
- Immutable: no earlier checkpoint is rewritten; recovered independent-recheck
  conclusions go into a **new** checkpoint.

## Direction change (RGE4)

R105/R107/R109 halted the "produce another process/evidence dossier" loop
three times; R114–R121 produced eight consecutive read-only audit layers, and
R121 derived from the governing R95 review's own §13 rules a **negative
closure**: this class of read-only audit cannot in principle raise the
evidence-capped Overall from 6.0 to >= 7.0. Producing a ninth process dossier
would be empty repetition.

R122 instead performs the substantive action named in the standing step-1
item ①: close the *evidence-acquisition* half of **R106 §6 R4** with real
first-hand, SHA-anchored bytes — a named gap repeatedly flagged in
R106/R107/R118/R120 and left undone for 11 rounds. This is a recomputable
first-hand artifact, not a wording patch.

## What landed (primary project, not uploaded)

`first-hand-R122/` under the main-line run root: 5 raw byte files (v1/v2 abs
pages, v1/v2 HTML full text, atom API response), source manifest, raw
extraction, v2 plaintext, body-abstract extraction, acquisition script,
independent verifier, verification JSON, round audit.

**Substantive finding (third-party version fact, not a project result)**: the
same v2 carries two materially different official abstracts — abs/API
(1,534 chars) versus HTML body-embedded (1,943 chars), similarity **0.4717**
with 38 non-equal opcodes. The abs/API abstract contains the time-scale sweep
conclusion; the body-embedded one does not. v1 differs from both in abstract
and title. Verified needles: §7.3 `The stimulus never completes a cycle`,
§8 `What the sampling sweep answered` with `+0.033 [0.015,0.050]` and
"T4/T5 contribution does not grow with length", §8 `What remains open` with
"Two gaps remain.", §9 Limitations. Version times from the abs page's
`Submission history` and atom **entry-level** fields agree; atom **feed-level**
`updated` is the query time and is explicitly NOT an article update.

Independent verifier recomputes from the five raw byte files without importing
the acquisition module and without reading any R122 JSON as a data source:
**47 checks / 47 MATCH / 0 MISMATCH**. A1–A4 are declared same-host byte
identity checks (necessary consistency, not independent cross-verification);
B–F are the substantive observations.

## Fresh isolated independent recheck

A fresh isolated sub-agent (`r122-independent-reviewer`) was launched with
**no expected verdict, no score anchor, no conclusion anchor**. It recomputes
A–F from source bytes with its own parsing logic, grades 12 named overclaim
categories and defects, and writes one report.

**At this checkpoint's write time the recheck had NOT been recovered. This
checkpoint therefore claims NO recheck verdict, NO defect list, NO
confirmation.** That statement is true as written and its bytes are not
rewritten later. Recovered conclusions and append-only corrections will be
published in a NEW immutable checkpoint (R117/R119/R120/R121 precedent).

## Content safety

Sanitized summary only: `evidence/R122-FIRST-HAND-R4-SANITIZED.md`.
**Not uploaded**: raw third-party HTML/XML (v2 HTML contains an author email),
primary project round audit, scripts, JSON, verification artifacts, any
independent-review original (may quote local paths), the full ledger, any
dataset / weight / binary / third-party source / unpublished manuscript.
Local paths in public text are written `<local>/`. See `metrics.csv` for the
read-only measurements (real, not fabricated).

## Strict boundary

- No write-back to any pre-existing registry / matrix / state / gate config.
  `literature-search/source-manifest.json`, `literature-baseline-matrix.md`,
  `pipeline-state.json` byte-unchanged. R4's "register into source-manifest"
  and R2's matrix finalization are decision groups G7/G6 requiring a
  designated gate owner.
- Zero gate promotions (G0 pending), zero self-certification, zero state
  changes, zero scientific activity (no forward / inference / training /
  labels / dataset / EPE·l2 / metric), zero new positive evidence.
- No `ccf-paper-reviewer full`, no numeric scored-verdict line, no
  self-assessed governing, no score / threshold / review / historical-byte
  change, no v4 contract, no P3 forward pass, no gate skipping, no
  `<=32h / K=45` authorization assumption, no 4090/L4/H20 claim.
- Primary project: no submission / commit / push. Private
  `ZtL-sysu/novix-platform` untouched. No merge / force push / branch
  deletion / Release.

## Result (unchanged)

**0 papers qualified, no COMPLETE written.** Governing remains
**R95 = 6.0 / Confidence 4.0**, `NOT_QUALIFIED` / `INCOMPLETE`.
Double gate: validator `NOT_QUALIFIED / 6.0 / >=7.0` (D1✓ D2✗ D3✗ D4✓ D5✗),
guard `INCOMPLETE` (A2/A6, S1–S7 pending). Heartbeat ACTIVE schedule
unchanged. Step-3 precondition (substantive positive new scientific evidence)
unmet ⇒ no manuscript copy, no compile, no fresh isolated full review.

## Next

1. Recover the isolated recheck → new immutable checkpoint with append-only
   corrections.
2. Decisions G7 (registry registration) and G6 (matrix finalization) need a
   designated gate owner; heartbeat must not self-write.
3. Only admissible path remains G0–G8 → validation → handoff → P0 → P1A/P1B
   → P2 → P3 baseline-first real forward pass → new manuscript copy →
   compliant compile → fresh isolated full review; COMPLETE only at >= 7.0
   with QUALIFIED + COMPLETE.

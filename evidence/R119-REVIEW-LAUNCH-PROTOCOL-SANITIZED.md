# R119 — review-launch protocol chain, recomputable read-only audit (sanitized)

**Nature**: `READONLY_REVIEW_LAUNCH_PROTOCOL_CHAIN_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
**Network requests**: 0. Every number below was recomputed from frozen local
disk bytes with `<local>/miniconda3/bin/python`. No new fetch, no timestamp
contamination.
**Write-back**: 0 for all pre-existing project bytes. All local paths in this
public copy are `<local>/`; no credentials, account identifiers or tokens.

This is a **sanitized summary**. The primary-project reports, scripts and JSON
stay in the private workspace and are not uploaded. No manuscript, dataset,
checkpoint weight, third-party source tree or unpublished review is uploaded.

---

## Why this round

R110 already measured acceptance-*machinery* reachability (validator/guard
with synthetic fixtures) and showed `QUALIFIED ∧ COMPLETE` unreachable for any
score because D2/D5 and A2/S1–S7 are score-independent blockers. R111 turned
all remaining actions into five decision points needing a designated gate
owner; that package is still unanswered. R114–R118 did first-hand licence /
archive / execution-premise / registry-gap acquisition, and R105/R107/R109
already stopped the "keep producing documents about evidence" loop three times.

So this round performs **no** machine-gate fix, **no** Nth G0 text patch, **no**
P3 forward pass, **no** probe/guard/runner patch cycle. It audits a layer
untouched in all 118 prior rounds: the **launch protocol of the sole
success-criterion action**. Heartbeat step 3 says a future fresh isolated
full-manuscript review is launched "per `protocols/independent-review-brief.md`
… without revealing an expected score or score anchors". R107's own iteration
file places `protocols/` in the deliberately-unchanged frozen contracts and
names a *future* versioned contract (v4) as the route to restate the new
criterion. This round measures, from raw bytes, what that instruction currently
resolves to.

## Measured facts (36 verification checks, 36 MATCH, 0 MISMATCH)

Two scripts: one collects, one recomputes independently (it does **not** import
the collector and does **not** read any collector JSON). Six sources copied
byte-identically to `isolated/` (6/6 identical). Both scripts run on the same
host with the same hash library and same data sources; their agreement is a
necessary consistency check, **not** an independent cross-verification — a
fresh isolated sub-agent supplies that.

| # | Fact | Reading |
|:--|:--|:--|
| F1 | Files named `independent-review-brief*` in the project tree | **1** — 4,803 B, SHA256 `8771dea8…` |
| F2 | Its title line | `(Contract v2, R51)` — R51-era frozen brief |
| F3 | Qualification clause (lines 17–18) | `X > 8.0`, `exactly 8.0 does not qualify` — R51 threshold |
| F4 | Post-review gate (lines 80–85) | `score_gt_threshold = true`; `If X <= 8.0 … threshold is never lowered` — R51 wording |
| F5 | Output path (line 76) | hard-coded `…independent-review-20261108.md` |
| F6 | Page clause (line 46) | `8 pages of main content` — differs from step 3's 9-page compliant compile |
| F7 | R107 iteration file lines 90–92 | `protocols/` listed as frozen contracts; `future versioned contract (v4) may restate the new criterion`; `no existing contract is retroactively edited` ⇒ leaving the brief unchanged was **deliberate** |
| F8 | Any R107/v4 versioned launch brief on disk | **0 files** ⇒ the v4 route R107 named was never built |
| F9 | Live validator | default threshold 7.0, `>=`, `score_meets_threshold` present, `score_gt_threshold` retained as backward-compatible field |
| F10 | guard A6 double wording | criteria `>= 7.0` / ledger `严格 > 8.0` — **R110/R111 known**, background only, not a new finding |
| F11 | Skill path cited by brief line 30 | `…/ccf-paper-reviewer/references/review-output-standards.md` → **absent**; the real file is under `ccf-common/references/` (3,364 B), and the reviewer `SKILL.md` lines 27/40/90 themselves cite the `ccf-common` path |
| F12 | Other cited skill paths | `SKILL.md`, `calibration-and-rank.md`, `venue-guides/` all present |
| F13 | **Anchor scoping** | the verbatim reviewer handoff block (lines 21–66) contains **zero** `8.0` and **zero** `7.0` tokens; it explicitly says `You are not told what score would be considered a success` and `Do not use any number quoted in this brief as a score anchor` |
| F14 | Preamble (lines 9–11, outside the handoff block) | contains two historical score values (`8.2`, `6.5`) |
| F15 | Past reviewers read the whole brief | the R58 non-anchoring declaration and the R60 §28 note both name the brief; R60 explicitly registers its numeric gate as background only, not an anchor |
| F16 | R95's actual launch brief | a **different** file (5,275 B, `0d42d1d9…`) with no literal `8.0` ⇒ R95 was not launched from the R51 protocols brief |
| F17 | Main-line `pipeline-state.json` | G0 `pending`, `inputs=[]`, `evidence=[]`; SHA256 `bcb48bb9…` unchanged |

## The one substantive finding, stated narrowly

A **versioned-contract gap** exists on the launch path of the sole
success-criterion action: step 3 points at `protocols/independent-review-brief.md`;
the only file by that name is the R51 frozen brief carrying R51 threshold,
output-path, page and score-field wording. R107 deliberately froze `protocols/`
and named a v4 contract as the way to restate `>= 7.0`, but no v4 brief exists.
When a fresh isolated full review is eventually launched, there is no
versioned launch artifact consistent with the R107 criterion.

This is explicitly **not** reported as:

- "the brief leaks the expected score to the reviewer" — F13 shows the
  reviewer-facing verbatim block carries no threshold and has explicit
  non-anchoring clauses; the R51 numbers live in the preamble and post-review
  gate (F4/F14), which R58/R60 read as background and excluded as anchors.
- "a machine gate will fail because `score_gt_threshold` is missing" — F9 shows
  the field still exists with `>=` semantics; the mismatch is one of documented
  criterion wording, not an executable check.
- "R95 was anchored by the old brief" — F16 shows R95 used a separate brief.
- a new finding about guard A6 (F10), a G0 pass, a scientific result, a change
  to governing, or the first-ever discovery of brief path imprecision (the R95
  ledger already recorded a different brief's imprecise `paper/sources/` path).

## Strictly not done

Per R107 (frozen contracts), R111 (five decision points await a designated gate
owner) and the heartbeat red lines: no edit/version/replace/re-date/delete of the
brief or any contract, gate, criteria, ledger, validator, review, score, stage
state or manuscript; **no v4 launch contract created** (that is a
versioned-contract decision for the gate owner, not something the heartbeat may
self-certify); no `ccf-paper-reviewer full` launched; no scored-review Overall
line produced; no expected score or anchor revealed to any reviewer; no G0
promotion, no self-attestation, no assumption of the `≤32h / K=45`
confirmation-panel authorization.

**EXEC LOCK** holds: zero forward pass / inference / training / label / dataset
load / EPE·l2 / scientific metric. No 4090/L4/H20 capability claim; unrelated
to the harbor 25092 engineering reward. Main project: no submission / commit /
push.

## Read-only double gate

| Gate | Result |
|:--|:--|
| validator | `EXIT=1 / NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`, `score_meets_threshold=false`; D1✓ D2✗ D3✗ D4✓ D5✗ |
| guard | `EXIT=1 / INCOMPLETE`; 7 deliverables all PASS; failures exactly A2, A6; S1–S7 all `pending` |
| ledger SHA16 + mtime | `f98b69369db6eb80` / `1794605184`, identical before and after |
| main-line `pipeline-state.json` SHA16 | `bcb48bb964e657a4` / 3,723 B, identical before and after |

A6's rendered text is still the ledger's `严格 > 8.0` — the dual-wording issue
registered in R109/R111/R118; read-only registration, not edited.

## Script-defect log (retained, not hidden)

- Collector v1 raised `IsADirectoryError` by calling `read_bytes()` on a
  directory; v2 branches on `is_dir()`. **Script defect, not a data
  inconsistency** (R116 discipline).
- Collector v1 assertion A12 searched an exact substring that the source wraps
  across two lines, returning `found=false`; v2 uses the exact single-line
  substring plus a second assertion. **Search-scope defect, not a missing
  clause** (R118 W2 lesson). Both v1 defects occurred before any artifact was
  written.

## Result and handoff

Step 3's precondition — **substantive positive new scientific evidence** — is
not met ⇒ no new manuscript copy, no 9-page compliant compile, no fresh
isolated full review. **0 papers qualified, COMPLETE not written**; governing
remains **R95 = 6.0 / Confidence 4.0**, `NOT_QUALIFIED` / `INCOMPLETE`. Stop
gates remain ① achieved ② user stop.

The versioned-contract decision belongs to the designated gate owner: which
launch brief governs, whether to create the v4 contract R107 named (restating
`>= 7.0`, the current 9-page compile and current output-path convention),
correcting the skill reference path **only in that new artifact**, keeping the
non-anchoring property of F13 verbatim, and recording it as a protocol decision
rather than evidence. Historical frozen artifacts stay byte-for-byte unchanged.

---

No scientific conclusion is claimed by any line above. A checkpoint marked
`completed` describes work state only, not validation.

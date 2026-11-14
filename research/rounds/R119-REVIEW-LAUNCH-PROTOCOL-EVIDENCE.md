# R119 — Review-launch protocol chain: read-only first-hand evidence

**Kind:** `READONLY_REVIEW_LAUNCH_PROTOCOL_CHAIN_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
**Round:** R119 (2026-11-14, +0800). **Python:** `/Users/xhf/miniconda3/bin/python` (3.14.6).
**Network requests this round:** 0.
**Governing:** unchanged, R95 = 6.0 / Confidence 4.0, `NOT_QUALIFIED` / `INCOMPLETE`.

---

## 1. Why this object, and why this is not the R114–R118 loop again

R110 already measured acceptance-*machinery* reachability (validator/guard with
synthetic fixtures) and proved `QUALIFIED ∧ COMPLETE` unreachable for any score
because D2/D5 and A2/S1–S7 are score-independent blockers. R111 turned the
remaining actions into 5 decision points requiring a designated gate owner.
R114–R118 did first-hand licence / archive / execution-premise / registry gap
acquisition, with R105/R107/R109 three times halting the "keep producing
documents about evidence" loop.

No round has audited the **launch protocol of the sole success-criterion action
itself**. The heartbeat step 3 says the fresh isolated `ccf-paper-reviewer full`
review is launched "按 `protocols/independent-review-brief.md` …（不透露期望分/分数锚点）".
R107's own file places `protocols/` in the **deliberately unchanged frozen
contracts** list and names a *future* versioned contract (v4) as the route to
restate the new criterion. This round measures, from raw bytes, what that
launch instruction currently resolves to. This is a protocol-consistency
measurement, not a gate pass, not a scientific result, not a repair.

## 2. Measured facts (all recomputed from raw bytes; 36/36 MATCH)

`R119-raw.py` collects and `R119-verify.py` independently recomputes (it does
**not** import the raw module or read any R119 JSON artifact). See
`R119-REVIEW-LAUNCH-PROTOCOL-RAW.json` and
`R119-REVIEW-LAUNCH-PROTOCOL-VERIFICATION.json`.

| # | Fact | Reading |
|:--|:--|:--|
| F1 | Files named `independent-review-brief*` in the project tree | **1**, at `papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2/protocols/independent-review-brief.md`, 4,803 B, SHA256 `8771dea8…` |
| F2 | Its title line | `(Contract v2, R51)` — R51-era frozen brief |
| F3 | Its qualification clause (lines 17–18) | `X > 8.0`, `exactly 8.0 does not qualify` — **R51 threshold**, not R107's `>= 7.0` |
| F4 | Its post-review gate (lines 80–85) | `score_gt_threshold = true`; `If X <= 8.0, the correction loop continues; the threshold is never lowered` — R51 wording |
| F5 | Its output path (line 76) | hard-coded `…independent-review-20261108.md` |
| F6 | Its page clause (line 46) | `8 pages of main content` — differs from step 3's 9-page compliant compile (p8 Conclusion, p9 LLM placeholder + References) |
| F7 | R107 file lines 90–92 | `protocols/` listed as frozen contracts; `future versioned contract (v4) may restate the new criterion`; `no existing contract is retroactively edited` ⇒ **leaving this brief unchanged was deliberate** |
| F8 | Any R107/v4 versioned launch brief on disk | **0 files** ⇒ the v4 route named by R107 was never created |
| F9 | Live validator | `--threshold` default 7.0, `comparison_operator` `>=`, `score_meets_threshold` present, `score_gt_threshold` retained as backward-compatible field |
| F10 | guard A6 double wording | criteria `>= 7.0` / ledger `严格 > 8.0` — **R110/R111 known**, registered here only as background, not a new finding |
| F11 | Skill path cited by brief line 30 | `~/.claude/skills/ccf-paper-reviewer/references/review-output-standards.md` → **does not exist**; the real file is `~/.claude/skills/ccf-common/references/review-output-standards.md` (3,364 B), and `ccf-paper-reviewer/SKILL.md` lines 27/40/90 themselves cite the `ccf-common` path |
| F12 | Other skill paths cited by brief | `SKILL.md`, `calibration-and-rank.md`, `venue-guides/` all exist |
| F13 | **Anchor-disclosure scoping** | the verbatim reviewer handoff block (lines 21–66) contains **zero** `8.0` and **zero** `7.0` tokens; it explicitly says `You are not told what score would be considered a success` and `Do not use any number quoted in this brief as a score anchor` |
| F14 | Preamble (lines 9–11, outside the handoff block) | contains two historical score values (`8.2`, `6.5`) |
| F15 | Past reviewers read the whole brief | R58 §non-anchoring declaration and R60 §28 both name `protocols/independent-review-brief.md`; R60 explicitly registers its numeric gate as background only and not an anchor |
| F16 | R95's actual launch brief | a **different** file `R49-7.5-DELIVERY/provenance/R95-independent-review-brief-FROZEN.md` (5,275 B, `0d42d1d9…`), containing **no** literal `8.0` threshold → R95 was not launched from the R51 protocols brief |
| F17 | Main-line `pipeline-state.json` | G0 `pending`, `inputs=[]`, `evidence=[]`; SHA256 `bcb48bb9…` unchanged |

## 3. The one substantive finding, stated narrowly

**There is a versioned-contract gap on the launch path of the sole
success-criterion action.** Step 3 points at `protocols/independent-review-brief.md`;
the only file by that name is the R51 frozen brief carrying R51 threshold,
output-path, page and score-field wording. R107 deliberately froze `protocols/`
and named a v4 contract as the way to restate `>= 7.0`, but **no v4 brief exists**.
So when a fresh isolated full review is eventually launched, the authoring
session has no versioned launch artifact consistent with the R107 criterion.

This is **not** reported as any of the following:

- **Not** "the brief leaks the expected score to the reviewer". F13 shows the
  reviewer-facing verbatim block carries no threshold and carries explicit
  non-anchoring instructions. The R51 numbers live in the preamble and the
  post-review gate section (F4/F14), which R58/R60 read as background and
  explicitly excluded as anchors (F15).
- **Not** "a machine gate will fail because `score_gt_threshold` is missing".
  F9 shows the field still exists with `>=` semantics; the brief's clause would
  still be satisfiable. The mismatch is one of **documented criterion wording**,
  not an executable check.
- **Not** "R95 was anchored by the old brief". F16 shows R95 used a separate
  frozen brief with no literal threshold.
- **Not** a new finding about guard A6 (F10), nor a claim that any of this
  changes the governing 6.0, nor a G0 pass, nor a scientific result.
- **Not** "first discovery" of path imprecision in briefs in general: the R95
  ledger entry already records that a brief's `paper/sources/` path was
  imprecise and assigned responsibility to the brief. F11 is a **different
  object** (a skill reference path in the R51 protocols brief).

## 4. What is deliberately NOT done

Per R107 (frozen contracts), R111 (5 decision points await a designated gate
owner), and the heartbeat red lines, this round **does not**:

- edit, version, replace, re-date or delete the brief, any contract, gate,
  criteria, ledger, validator, review, score, stage state or manuscript;
- create a v4 launch contract (that is a versioned-contract decision for the
  designated gate owner, and writing it now would be self-certification);
- launch any `ccf-paper-reviewer full` review, produce any `**Overall:**` line,
  or reveal an expected score / anchor to any reviewer;
- promote G0 or any gate, self-attest, or assume the `≤32h / K=45`
  confirmation-panel authorization;
- perform any forward pass, inference, training, label, dataset load or
  scientific metric; EXEC LOCK holds.

Zero pre-existing bytes changed. Only this R119 directory was created.

## 5. Handoff to the designated gate owner (decision, not self-action)

When a real revised manuscript and substantive positive evidence exist and a
fresh isolated full review is actually imminent, the gate owner must decide and
record, in a **versioned** artifact, at minimum:

1. Which launch brief governs: keep the R51 frozen brief as historical context
   and create the v4 contract R107 named, or explicitly declare an equivalent
   launch specification. The v4 contract must restate `>= 7.0`, the current
   9-page compile, and the current output-path convention.
2. Correct the skill reference path (F11) in that **new** artifact only; do not
   retroactively edit frozen history.
3. Keep the non-anchoring property of F13 verbatim; do not move threshold or
   historical score values into the reviewer-facing block.
4. Record that this is a protocol/versioning decision, not evidence, and that
   it does not by itself change `NOT_QUALIFIED` / `INCOMPLETE`.

## 6. Reproducibility

- `R119-raw.py` → `R119-REVIEW-LAUNCH-PROTOCOL-RAW.json` (17,177 B).
- `R119-verify.py` → `R119-REVIEW-LAUNCH-PROTOCOL-VERIFICATION.json` (7,879 B),
  36 checks, 36 MATCH, 0 MISMATCH.
- `R119-SOURCE-MANIFEST.json` — source byte sizes, SHA-256, existence.
- `R119-ROUND-AUDIT.md` — round audit, script-defect log, boundary.
- `isolated/` — byte-identical copies for `cmp`.

**Independence caveat (R115 W4 / R114 D1):** both scripts run on the same host
with the same `hashlib` and the same data sources; their agreement is a
necessary consistency check, **not** an independent cross-verification. A
fresh isolated sub-agent with no access to the authoring conversation supplies
that, and its report is recorded separately.

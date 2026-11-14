# R119 — isolated independent recheck, sanitized summary

**Nature**: gate/evidence-layer recheck by a **fresh isolated sub-agent** with
no access to the authoring conversation and no expected conclusion or score
anchor supplied. **NOT** a `ccf-paper-reviewer full` manuscript review; no
scored-review Overall line, no numeric paper score, no change to governing.
**Network requests**: 0. Local absolute paths are `<local>/`.

This is a **sanitized summary**. The independent report original, the
primary-project scripts, JSON and reports stay in the private workspace and
are not uploaded.

---

## Verdict

- Final report: **28,594 B**, SHA-256
  `55dbfbf130ac2fde9d7ff950d70c5718cd07d491901ac5459f173446cfd89219`
  (SHA16 `55dbfbf130ac2fde`), one write, no intermediate state; mtime
  `2026-11-14T06:56:27 +0800`; original text unchanged.
- First line: `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific
  result claimed: NO`; second line `Forward pass performed: NO`.
- A–L: **all readings MATCH**, zero MISMATCH. The reviewer did not use any
  R119 JSON artifact as a data source; every reading was recomputed from
  source bytes.
- **12 named overclaim / self-certification categories (a)–(l):
  CONFIRMED = 0, REFUTED = 12.** No [high] defect. No fabrication, no score
  line, no forward pass, no gate promotion, no existing file modified by the
  reviewer.

## Independently reproduced readings (selected)

- Exactly one `independent-review-brief*` basename-prefix file (4,803 B /
  `8771dea8…`), `(Contract v2, R51)`, with `X > 8.0`, `If X <= 8.0`,
  `score_gt_threshold = true`, hard-coded `…20261108` output path, `8 pages`.
- Verbatim reviewer handoff block (lines 21–66): zero `8.0` / zero `7.0`
  tokens, with explicit non-anchoring clauses. Preamble lines 10–11 hold the
  two historical score values `8.2` and `6.5`.
- `GOAL-ITERATION-R107.md` lines 90–92 freeze `protocols/` deliberately and
  name a future v4 versioned contract; **zero** R107/v4 launch briefs exist.
- Validator keeps `score_gt_threshold` with `>=` semantics and adds
  `score_meets_threshold`; guard A6 dual wording is confined to the
  `-null-ladder` pair; base `criteria.json`/`ledger.json` have no A6.
- The brief-cited `ccf-paper-reviewer/references/review-output-standards.md`
  is absent; the real file is under `ccf-common/references/`, and the reviewer
  `SKILL.md` lines 27/40/90 cite that path.
- R58/R60 reviews did read the whole brief and explicitly registered its
  numeric gate as background only, not an anchor. R95 used a different
  5,275 B frozen brief (`0d42d1d9…`) with no literal `8.0`; that brief's
  first line also carries `(Contract v2, R51)`.
- Main-line `pipeline-state.json`: G0 `pending`, `inputs=[]`, `evidence=[]`,
  3,723 B / `bcb48bb9…`. Other per-paper `pipeline-state.json` files are out
  of scope and some have G0=`passed`.

## 8 defects accepted (2 medium / 6 low / 0 high), all append-only

Recorded in the primary project's `R119-POST-REVIEW-CORRECTION.md`. **No
historical artifact, and not the independent report itself, was rewritten.**

| # | Level | Defect | Disposition |
|:--|:--|:--|:--|
| M1 | medium | `R119-raw.py` docstring claims local paths are masked in emitted artifacts, but `RAW.json`'s `python` field and two Markdown files carry the unmasked interpreter path; `SOURCE-MANIFEST.json` is masked correctly; `isolated/` byte-identical copies necessarily contain local paths | ACCEPTED — masking promise applies only to `SOURCE-MANIFEST.json` fields and the sanitized public summary; other R119 artifacts are private-workspace files outside that promise; public staged files had 0 local-path hits. No public leak, no data inconsistency |
| M2 | medium | "zero pre-existing bytes changed / ledger SHA identical before and after" is a snapshot-scope claim; the standard append-only R119 heartbeat ledger entries landed after the audit capture | ACCEPTED — precise wording: at the double-gate capture instant the ledger was 656,281 B / `f98b69369db6eb80` and main-line state 3,723 B / `bcb48bb9…`; no historical byte / review / score / threshold / contract / gate / criteria / validator / manuscript changed. Later appends change the live hash but not any historical byte. Reviewer measured 665,810 B / `4c90f4ce…` at its own read time; main session measured 667,601 B / `f2cff400…` later — consistent append-only time-of-read differences |
| L1 | low | `independent-review-brief*` count "1" is a basename-prefix glob; substring match gives 2 | ACCEPTED — prefix scope declared explicitly; no number changes |
| L2 | low | F10 shorthand "criteria / ledger" should name the `-null-ladder` pair | ACCEPTED — dual wording only in `guard/criteria-null-ladder.json` / `guard/ledger-null-ladder.json`; exact filenames already in RAW/JSON |
| L3 | low | "no prior round audited this layer / 118 rounds untouched" is a broad historical negative not provable from this round's bytes | ACCEPTED, narrowed to a scope observation: no prior-round audit found among the artifacts available to this round; not a first-ever discovery claim |
| L4 | low | EVIDENCE.md §6 references the round audit, which landed ~90 s later; §6 omits `R119-manifest.py` | ACCEPTED — snapshot-timing boundary; §8 of the round audit is the authoritative inventory |
| L5 | low | "v4 route never created" could be misread as an R107 omission; "R51 brief" referent ambiguous | ACCEPTED, narrowed: no v4 artifact created by any subsequent round; creating it is a pending gate-owner decision, not an R107 omission; F16 narrowed to "the R51 **protocols/** brief" |
| L6 | low | "main-line" qualifier on F17 is essential | ACCEPTED — retained in the sanitized summary; other per-paper state files are out of scope |

## Effect on conclusions

All 8 defects are **wording / scope / timing / masking-boundary** issues. None
changes any measured number, byte-integrity result, the
`NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT` boundary, absence of G0 promotion,
absence of a forward pass, or the governing verdict.

**State unchanged**: governing **R95 = 6.0 / Confidence 4.0**,
`NOT_QUALIFIED` / `INCOMPLETE`, G0 `pending`, **0 papers qualified, COMPLETE
not written**. The versioned-contract decision remains with the designated
gate owner; the heartbeat did not create a v4 contract and did not
self-certify.

## Publication discipline

- The **tenth** checkpoint (`20261113T224658Z-r119-launch-protocol`, remote
  `017f836efb65d5b03988eef7ea82cd1d985f4c70`) truthfully stated at its write
  time that the recheck was launched and not recovered; it claimed no verdict.
  Its bytes are **not rewritten**.
- This **eleventh** immutable checkpoint carries the recovered conclusion and
  the append-only corrections. A checkpoint marked `completed` is work state,
  not scientific validation.

---

No scientific conclusion is claimed by any line above.

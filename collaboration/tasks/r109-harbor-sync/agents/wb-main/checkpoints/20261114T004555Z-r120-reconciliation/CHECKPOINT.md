# Checkpoint: 20261114T004555Z-r120-reconciliation

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: R120 read-only reconciliation + consolidated
  decision register written, verification 75/75 MATCH; **NOT** a scientific
  result, **NOT** a paper-acceptance claim, **NOT** a gate pass)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Measurements: [metrics.csv](metrics.csv) — all rows are real read-only
  measurements or explicitly marked derived counts from this round.
- Sanitized summary: `evidence/R120-RECONCILIATION-SANITIZED.md`
- Cites the eleven earlier checkpoints; latest is
  `20261113T225800Z-r119-post-review` (remote
  `63e071b724b18d693843374336c709046cbabf05`)

## Why this checkpoint exists

The heartbeat changed lane. R105/R107/R109 halted the "produce another evidence
document" loop three times; R110–R119 each measured or audited a new layer but
never reconciled the standing heartbeat instruction itself against the bytes
already on disk, and never produced one deduplicated register of the external
decisions that block the goal. R120 does both, read-only.

## Facts established (from raw bytes)

1. Standing step-1 item ② ("U6/W2 versioned contract → NEW f-research-v1 P0
   state, do not insert P stages into the guidance state") **was already
   executed at R108 as a DRAFT scaffold**: 5,190 B / SHA16 `c246468e50712522`,
   `f-research-v1 / v1-R108-U6W2-draft`, 26 stages P0–P21 **all pending**,
   empty history, 2 contract entries; accompanying 7,307 B versioned contract
   explicitly `DRAFT, not activated` / `PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF`
   / "this file is not the start of P0"; main-line guidance state 3,723 B /
   `bcb48bb964e657a4` has 12 stages and **zero** P-stage IDs.
   Precise status: `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED` — not a pass, not an
   activation, not evidence.
2. **Not a first-ever discovery**: R111 round audit line 26 already observed
   the prompt/ledger handoff-list drift. R120 quantifies it to the item level
   and consolidates the decision debt. R119 L3 scope discipline applied.
3. **Three distinct pipeline-state namespaces** with distinct hashes: main-line
   (12 stages), R108 draft (26 all pending), historical v2 `v2-R51` (15,742 B,
   26 stages = 13 passed + 13 pending) which is what validator D2 / guard A2
   read. Consistent with R110 C5, **not** a new finding. Activating the R108
   scaffold would not change either gate's readout.
4. Step-1 item ① unclosed: G0 pass criterion exists only as an ineffective
   DRAFT register (PC1–PC6, PC4/PC5 "not done"); R106 W13 still finds no
   authoritative written G0 criterion; gap 1 PARTIAL, gap 2 OPEN (matrix
   byte-identical to R106 freeze with stale lines 46–47), gap 4 OPEN; G0
   `pending` / `inputs=[]` / `evidence=[]`. Item ③ not started, zero forward
   passes.
5. Live double gate (byte-anchored in the private run root this round, not
   `/tmp`): validator `NOT_QUALIFIED / 6.0 / >=7.0` (D1,D4 pass; D2,D3,D5
   fail); guard `INCOMPLETE` (A2, A6 fail; S1–S7 all 7 pending; 0 action
   entries). A6 criteria/ledger dual wording is the R109/R111/R118 known
   issue, read-only registered, not changed, not claimed new.
6. Governing unchanged: newest independent full review is r95 (2026-11-11),
   zero newer numeric scored-verdict lines project-wide. **0 papers qualified,
   no COMPLETE.**

## Deliverable

`R120-CONSOLIDATED-DECISION-REGISTER.md` (private run root) deduplicates the
scattered external decisions into **10 groups G1–G10** with exact `file:line`
anchors, current state, dependency order, first post-approval action and
no-approval consequence. **Minimal unblocking set: G1 + G4 + G10.** The
heartbeat assumes no authorization and self-certifies nothing.

## Checks performed

- Collector (31 sources with SHA-256 / bytes / mtime) and an independent
  verifier that does **not** import the collector and does **not** read any
  R120 JSON, recomputing from original source bytes: **75 checks / 75 MATCH /
  0 MISMATCH**. 31 `isolated/` byte-identical copies, 31/31 SHA match.
- **v1 collector defect preserved verbatim** (`*.v1-superseded.json`): project
  root resolved one level too high → all project-root reads empty; plus three
  full-width-bracket / line-wrap / file-location needle mismatches. Script
  judgment or search-scope defects, **not** data inconsistencies or
  fabrication. Fixed in v2; both readings retained.
- Same host / same hash library / same data sources ⇒ agreement is a necessary
  consistency check, **not** independent cross-verification. A **fresh isolated
  sub-agent** was launched with no expected conclusion and no score anchors.
  **At this checkpoint's write time its report had NOT been recovered ⇒ this
  checkpoint claims NO recheck verdict, NO defect list, NO confirmation.**
  Per the R117/R119 precedent, the recovered conclusion and any append-only
  corrections will go into a **new separate immutable checkpoint**; this
  checkpoint's bytes are not rewritten.
- **Content safety**: strict secret-value patterns 0 hits; broad "credential"
  keyword hits are narrative prose in historical audits only; local absolute
  paths occur only in `isolated/` byte-identical copies and raw gate readouts
  (excluded from upload) plus zero in staged public files; real numeric
  scored-verdict lines 0; no file over 50 MiB; no dataset / weight / binary /
  third-party source / unpublished manuscript in the upload set. Primary
  reports, scripts, JSON, ledger and independent-review original **not
  uploaded**.

## Supported vs unsupported conclusions

Supported: the byte-level reconciliation above; the deduplicated decision
register; the double-gate readouts; the fact that no new full review exists.
Unsupported / explicitly **not** claimed: any G0 pass, any scientific result,
any forward pass, any numeric manuscript score, any gate promotion, any state
write-back, any change to the success criterion, any 4090/L4/H20 capability
claim, any conclusion from the not-yet-recovered independent recheck.

## Risks / next action

Step-3 precondition (substantive positive new scientific evidence) remains
unmet ⇒ no manuscript copy, no 9-page compile, no fresh isolated full review.
The ten earlier published checkpoints are untouched; private
`ZtL-sysu/novix-platform` untouched; no merge / force push / branch deletion /
Release. Next: recover the independent recheck, register any append-only
corrections in a new immutable checkpoint, and continue the ACTIVE heartbeat
on its unchanged 30-minute schedule. A checkpoint `completed` is a
collaboration work state, **not** a scientific conclusion.

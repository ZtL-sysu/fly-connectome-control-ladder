# R120 — standing-instruction / on-disk-state reconciliation, sanitized summary

**Nature**: read-only, byte-anchored reconciliation by the local heartbeat
automation. `READ_ONLY_RECONCILIATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`.
**NOT** a gate pass, **NOT** a scientific result, **NOT** a
`ccf-paper-reviewer full` manuscript review, **NOT** a scored review.
No numeric paper score line is produced or quoted here. Network requests: 0.
Forward passes / inference / training / datasets / labels / scientific metrics: 0.
Local absolute paths are `<local>/`.

This is a **sanitized summary**. Primary-project scripts, JSON, isolated
byte-identical copies (which necessarily contain local paths), the full ledger,
the independent-review original and all raw gate readouts stay in the private
workspace and are **not uploaded**.

---

## Why this round changed lane

R105/R107/R109 halted the "produce another evidence document" loop three
times. R110 measured acceptance-machinery reachability, R111 judged
"autonomously reachable actions exhausted" and handed out 5 decision points,
R114–R118 did five consecutive rounds of first-hand license / archive /
execution-premise / registry evidence acquisition, and R119 audited the
launch-protocol chain of the sole success-criterion action. **None of those
rounds reconciled the standing heartbeat instruction itself against the bytes
already on disk, and none produced a single deduplicated register of the
external decisions that block the goal.** R120 does exactly those two things,
read-only.

## Governing state (unchanged)

- validator: `NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`, `D1 pass, D2 fail,
  D3 fail, D4 pass, D5 fail`, `score_meets_threshold=false`.
- guard: `INCOMPLETE`, failures exactly **A2 and A6**, all seven S1–S7 steps
  `pending`, action sequence 0 entries.
- newest independent full review remains the r95 report (2026-11-11); no
  newer report with a numeric scored-verdict line exists anywhere in the
  project. **0 papers qualified, no COMPLETE.**
- Step-3 precondition (substantive positive new scientific evidence) unmet ⇒
  no new manuscript copy, no 9-page compile, no fresh isolated full review.

## Central finding (narrowly stated)

The standing instruction's step-1 item ② — "U6/W2 versioned contract handling
of the guidance handoff → create a NEW f-research-v1 P0 state (do not insert P
stages into the guidance state)" — **was already executed at R108 as a DRAFT
scaffold**:

| object | measured |
|:--|:--|
| `state-handoff-R108/f-research-v1-state/pipeline-state.json` | 5,190 B, SHA16 `c246468e50712522`, `pipeline=f-research-v1`, `contract_version=v1-R108-U6W2-draft`, **26 stages P0–P21 all `pending`**, empty history, 2 contract entries |
| `R108-U6-W2-VERSIONED-CONTRACT.md` | 7,307 B; line 1 `DRAFT, not activated`; line 3 `ENGINEERING_STATE_SCAFFOLD_ONLY_NOT_SCIENTIFIC_RESULT`; line 5 `PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF` and "this file is not the start of P0" |
| main-line `pipeline-state.json` | 3,723 B, SHA16 `bcb48bb964e657a4`, `f-guidance-builder-v1 / v2`, 12 stages, **zero P-stage IDs inserted** |

⇒ precise status: **`SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED`**. The literal
requirement is satisfied as a draft scaffold; this is **NOT** a claim that P0
started, that any gate passed, that the handoff passed, that the contract was
frozen, or that any scientific evidence exists. Every one of the 26 scaffold
stages is still `pending`.

**Not a first-ever discovery.** `R111-ROUND-AUDIT.md` line 26 already observed
that the heartbeat prompt's embedded handoff list was stale relative to the
ledger. R120's increment is quantifying that drift down to the specific item
and consolidating the decision debt. Likewise, the finding that the acceptance
machinery reads a different state namespace than the main line is R110 C5, not
new; R120 quantifies it as **three distinct state namespaces with three
distinct hashes** (main-line 12 stages; R108 draft scaffold 26 all pending;
historical v2 `v2-R51` 26 stages = 13 passed + 13 pending, read by validator
D2 / guard A2). Activating the R108 scaffold would therefore not change either
gate's readout — which is exactly why R111 D-1 (delivery object / gate path)
needs an external decision.

Other items: step-1 item ① (written G0 pass criterion) exists only as a DRAFT
register (`PENDING DESIGNATED GATE OWNER APPROVAL`, PC1–PC6, PC4/PC5 "not
done", explicitly "not in effect"), R106 W13 still finds no authoritative
written G0 criterion, gap 1 PARTIAL, gap 2 OPEN (baseline matrix byte-identical
to the R106 freeze with stale wording on lines 46–47), gap 4 OPEN, G0 remains
`pending` with empty `inputs`/`evidence`. Step-1 item ③ (ordered G1–G8 →
validation → handoff → P0 → P1A/P1B → P2 → P3 real forward) is not started;
zero forward passes.

## Deliverable: one consolidated external-decision register

Decisions requiring the user or a designated gate owner were scattered across
11+ files and restated in every round's handoff. R120 deduplicates them into
**10 decision groups (G1–G10)** with exact `file:line` anchors, current state,
dependency order, the first heartbeat action after approval, and the
consequence of no approval:

- G1 delivery object / gate path (blocks all others)
- G2 sync the legacy guard A6 wording to `>=7.0`
- G3 real evidence for the 13 pending stages + step-ledger certification + D5 matrix
- G4 written frozen G0 pass criterion + designated independent judging party
- G5 three remaining gap-1 first-hand evidence judgments
- G6 baseline-matrix finalization + SHA re-freeze
- G7 R4 registration, CAPTCHA entry disposition, candidate classification
- G8 three P3 execution premises frozen as a versioned execution contract
- G9 which launch brief governs / whether to create the R107-named v4 contract
- G10 the `<=32h / K=45` confirmation-panel authorization (pending since R99)

**Minimal unblocking set: G1 + G4 + G10.** The heartbeat assumes **no**
authorization, self-certifies nothing, and writes back no state, matrix,
registry, gate config or v4 contract.

## Reproducibility and honesty notes

- Collector → `R120-RECONCILIATION-RAW.json` (31 sources with SHA-256 / bytes /
  mtime) + `R120-SOURCE-MANIFEST.json`. Independent verifier (does **not**
  import the collector and does **not** read any R120 JSON; recomputes from
  original source bytes) → `R120-RECONCILIATION-VERIFICATION.json`:
  **75 checks / 75 MATCH / 0 MISMATCH**. `isolated/` holds 31 byte-identical
  copies, 31/31 SHA match.
- **v1 collector defect preserved verbatim** (`*.v1-superseded.json`): the
  project root was resolved one directory too high, so all project-root reads
  were empty; three further needles had full-width-bracket / line-wrap / file
  location mismatches. All are **script judgment or search-scope defects, not
  data inconsistencies or fabrication**. Fixed in v2; both readings retained.
- Both scripts run on the same host with the same hash library and the same
  data sources, so their agreement is a necessary consistency check, **not**
  independent cross-verification. Truly independent recomputation was delegated
  to a fresh isolated sub-agent with no expected conclusion and no score
  anchors; at the time this summary was written its report had **not been
  recovered**, so no review verdict is claimed here.
- Double-gate readouts were written into the run root this round (not `/tmp`),
  so an independent reviewer can recompute them from bytes — closing the
  R118 W7 / R119 M2 snapshot-scope gap.
- Content safety: strict secret-value patterns 0 hits; broad "credential"
  keyword hits are all narrative prose in historical audits; local absolute
  paths appear only in isolated byte-identical copies and raw gate readouts,
  which are excluded from upload; no file over 50 MiB; no dataset, weight,
  binary, third-party source or unpublished manuscript uploaded.

A checkpoint `completed` is a collaboration work state, **not** a scientific
conclusion. The heartbeat remains ACTIVE on its unchanged 30-minute schedule.

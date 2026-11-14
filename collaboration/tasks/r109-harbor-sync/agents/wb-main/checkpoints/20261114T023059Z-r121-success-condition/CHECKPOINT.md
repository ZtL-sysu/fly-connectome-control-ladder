# Checkpoint: 20261114T023059Z-r121-success-condition

- Task / agent / branch: `r109-harbor-sync` / `wb-main` /
  `agent/r109-harbor-sync/wb-main`
- Status: **completed** (work state: fourteenth checkpoint; R121 read-only
  success-criterion closure audit finished; **NOT** a scientific result,
  **NOT** a paper-acceptance claim, **NOT** a gate pass)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Measurements: [metrics.csv](metrics.csv) — real read-only measurements.
- Sanitized summary: `evidence/R121-SUCCESS-CONDITION-SANITIZED.md`
- Cites the thirteen earlier checkpoints; the latest is the thirteenth
  (`20261114T005802Z-r120-post-review`, remote
  `f0ef624192a4e03854a9dc53f8694cdfb58a82a9`).

## Why this checkpoint exists

R114–R120 each audited a different process / infrastructure layer. Earlier
rounds had already flagged "keep producing evidence documents" as an isomorphic
loop three times (R105/R107/R109). R121 changes lane: it reconciles the
**governing independent full review's own score-change taxonomy** (R95 §8/§11/
§13/§15) against the seven prior rounds' declared output classes, first-hand
evidence for the three "raise score" conditions, the two machine gates, and the
ordered gate chain. This is the layer closest to the success criterion and had
no precedent among the visible round artifacts (a scope observation, not a
claim about all history).

## What was measured (read-only)

- 18 byte-exact needles from R95, all matched: the scored-verdict line,
  §13 "No quick change" (process / disclosure / format does "not add scientific
  evidence supporting the central claim" and "does not change the
  evidence-capped overall"), §13 "Raise score" (three conditions,
  "6→7~7.5"), §15 "Raising the score would require", §8 M1 "not fixable by
  prose" / M2 "cannot produce a visual contribution with prose", §11
  Evidence = 3 / Significance = 3, and the tie-breaker that ≥3 decisive
  concerns block Overall 7.
- Three raise conditions, from source bytes: (a) 6 real MaleCNS
  `hypothesis_supported = False`, 4 synthetic controlled graphs `True`
  (the surrogate M1 excludes); (b) the version-locked manuscript
  40,175 B / md5 `e4bfad51…158c6` states verbatim at line 637 that the
  flyvis stack was not rerun, and 0 rerun metric files exist; (c) the real
  visual task has MLP baseline 0.97222 dominating, real-minus-null delta
  −0.000463 with CI95 including 0 — R95 records a negative result.
  **All three `satisfied = False`.**
- 7 / 7 prior round audits declare, over their full text,
  `READONLY…NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`; 0 new positive evidence,
  0 gate passed, 0 line-start numeric scored-verdict line.
- Live double gate: validator `NOT_QUALIFIED / 6.0 / >=7.0`
  (D1✓ D2✗ D3✗ D4✓ D5✗); guard `INCOMPLETE` (A2 + A6 failing, 7 steps
  pending, 0 actions). Main-line state: 12 stages, `CCFA-startup=passed`,
  G0–G8 / validation / handoff all `pending` with empty `inputs`/`evidence`.
- Numeric scored-verdict scan: 14 line-start lines project-wide; exactly 1
  pre-existing file newer than r95 (a byte-identical copy of r95) plus 1
  self-produced isolated copy from this round. **Zero new governing
  candidates.**

## Supported vs. unsupported conclusions

- **Supported (negative closure):** by the governing review's **own** rules,
  read-only process / disclosure / format audits of the R114–R120 class fall
  under §13 "No quick change" and therefore **cannot** raise the
  evidence-capped Overall from 6.0 to the required >= 7.0. This is a
  criterion-level impossibility, not slow progress. The only admissible path
  remains the ordered gate chain through a baseline-first P3 real forward pass
  that produces substantive positive new evidence, a new manuscript copy,
  compliant compilation, then a fresh isolated full review.
- **NOT supported / NOT claimed:** any scientific result, any forward pass,
  any gate promotion, any score change, any threshold change, any new
  independent full review, any self-authored governing review, any activation
  of the R108 draft scaffold, any v4 launch contract, any assumption of the
  ≤32h / K=45 confirmation-panel authorization, any 4090 / L4 / H20
  capability.
- A6's dual wording (criteria `>=7.0` vs ledger `严格 > 8.0`) is a known
  R109/R111 issue, read-only registered, not changed, not new.

## Reproducibility

Primary (private) run root:
`<local>/auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/success-condition-R121/`.

- `R121-collect.py` + `R121-RAW-v1.json` (retained) →
  `R121-collect-v2.py` → `R121-RAW-v2.json` (21 sources + 21 byte-identical
  `isolated/` copies).
- `R121-verify.py` does **not** import the collector and reads **no**
  R121-produced JSON; it recomputes from original source bytes:
  **74 checks / 74 MATCH / 0 MISMATCH**. Verifier v1 and its reading are
  retained too.
- Six v1 script defects (three collector-side, four verifier-side including
  one overlap) are documented in `R121-V1-DEFECTS.md`. All are enumeration,
  transcription, or self-check-regex defects — **not** data inconsistencies
  or fabrication. Both v1 and v2 readings are retained.
- Same host / same `hashlib` / same sources ⇒ a necessary consistency check,
  **not** independent cross-verification (R115 W4). Genuine independence is
  delegated to a fresh isolated sub-agent.

## Fresh isolated independent recheck

A **new** isolated sub-agent was launched with **no expected verdict, no score
anchor, and no conclusion anchor**, instructed to recompute A–J from original
source bytes and to use no R121-produced JSON as a data source.

**At the time this checkpoint was written the recheck had NOT been recovered.
This checkpoint therefore claims NO recheck verdict, NO defect list, and NO
confirmation of the recheck.** Per R117/R119/R120 precedent, the recovered
conclusion and any append-only corrections will go into a **new, separate
immutable checkpoint**; this checkpoint's bytes will not be rewritten.

## Files and content safety

Only these files are staged for this checkpoint: the new sanitized summary,
`HANDOFF.md`, `LOG.md`, and the three files in this checkpoint directory.
Primary-project reports, scripts, JSON, `isolated/` byte-identical copies,
the full ledger, and any independent-review original are **not uploaded**.
All published files use `<local>/` instead of absolute paths. The full repo
was scanned for credentials / tokens / account identifiers / local absolute
paths / scored-verdict lines, for files over 50 MiB, and for datasets,
weights, binaries, third-party source, and unpublished double-blind
manuscripts; results are recorded in the primary round audit.

## Next action

Recover the isolated recheck, append any corrections in a new immutable
checkpoint, and continue to await the designated gate owner / user decisions
(minimum unblocking set `G1 + G4 + G10` in the R120 consolidated decision
register). No gate is promoted here; G0 remains `pending`.

## Stop conditions

Only (1) a new independent full review with Overall >= 7.0 plus QUALIFIED +
COMPLETE, or (2) the user calling a stop. A checkpoint status of `completed`
describes work state only, never scientific validity.

# Checkpoint: 20261114T005802Z-r120-post-review

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: R120 isolated independent recheck
  recovered, all 7 defects accepted as append-only corrections, conclusion
  published; **NOT** a scientific result, **NOT** a paper-acceptance claim,
  **NOT** a gate pass)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Measurements: [metrics.csv](metrics.csv) — real read-only measurements from
  the recovered review and the new first-hand I-2 evidence artifact.
- Sanitized summary: `evidence/R120-INDEPENDENT-REVIEW-SANITIZED.md`
- Cites the twelve earlier checkpoints, in particular the twelfth
  (`20261114T004555Z-r120-reconciliation`, remote
  `9e340862be1a0870b68fd2e4ba25fe596bef9c1e`)

## Why this checkpoint exists

The twelfth checkpoint was written while the fresh isolated sub-agent was
still running. It truthfully stated "recheck launched, not recovered, no
verdict claimed" and explicitly reserved the recovered conclusion for a **new,
separate immutable checkpoint** (R117/R119 precedent). This is that
checkpoint. The twelfth checkpoint's bytes are **not rewritten**.

## Recovered independent recheck

- Final report `R120-INDEPENDENT-REVIEW.md` (primary project, **not uploaded**
  because it quotes two local paths): **23,074 B**, SHA-256
  `c7c613c54bd08cad1b945c5affcdf371522430e63fff84d702ac86625cf3d9ea`,
  mtime `2026-11-14T08:55:00 +0800`, one write, no intermediate state,
  original unchanged.
- Verdict: `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific
  result claimed: NO`; `Forward pass performed: NO`.
- The reviewer used **no** R120-produced JSON as a data source and recomputed
  everything from source bytes. A–H, J, L: **MATCH**; **I and K: MISMATCH**.
- **12 named overclaim / self-certification categories (a)–(l):
  CONFIRMED = 0, REFUTED = 12.** No fabrication, no data inconsistency, no
  score line, no forward pass, no gate promotion, no existing file modified
  by the reviewer.
- This is a **gate/evidence-layer recheck**, **not** a
  `ccf-paper-reviewer full` manuscript review: no scored-review verdict line,
  no numeric paper score, no governing change.

## 7 defects accepted (1 HIGH / 3 MEDIUM / 3 LOW), all append-only

Full disposition in the private `R120-POST-REVIEW-CORRECTION.md` and the
sanitized `evidence/R120-INDEPENDENT-REVIEW-SANITIZED.md`. Summary:

- **W1 (HIGH, substantive withdrawal + evidence gap)** — the literal claim
  "no newer file with a numeric scored-verdict line exists anywhere in the
  project" is refuted (reviewer scan: 13,704 files, 647 literal / 109 inline
  numeric / 14 line-start numeric lines across 12 files, with newer files
  quoting or copying existing scores). R120's own collector left the field as
  an **empty never-populated placeholder** with no verifier check, so the claim
  lacked first-hand byte-anchored evidence. Closed by a **NEW first-hand
  recomputation artifact, not a wording patch**: `R120-I2-EVIDENCE.py/json`
  (13,706 files scanned; 662 literal / 109 inline / 14 line-start across 12
  files; **39 files / 83 inline lines newer than r95**, all quotations/copies).
  Narrowed, evidence-backed claim: **zero new independent full reviews after
  r95, zero newly produced numeric verdict lines this round**, supported by
  `qualifying_files=[] / supported=true`. The 13,704 vs 13,706 difference is
  a scan-time effect, not a data inconsistency.
- **W2 (MEDIUM)** — "first-ever / never" historical negatives in the report
  title and decision register narrowed to a scope observation ("no precedent
  among this round's visible artifacts"); R111 line 26 is a documented prior
  observation. Original titles not rewritten; the correction register is the
  authority on wording.
- **W3 (MEDIUM)** — the four R107 restatements are different wording /
  numbering versions; no single line contains the full spliced quotation;
  line numbers 175/175/116/180 are correct.
- **W4 (MEDIUM)** — the **whole** item ② must not be called satisfied: only
  the "create P0 state / no P stages in guidance state" sub-clause exists as
  a draft scaffold; "versioned contract handling of the guidance handoff" is
  unmet (handoff pending). The reviewer confirmed
  `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED` is accurate — neither overclaim nor
  underclaim.
- **W5 (LOW)** — "12" was a file count; exact is 14 lines / 12 files.
- **W6 (LOW)** — 3 byte-identical closure copies on disk, R120 evidence set
  collected 2.
- **W7 (LOW)** — R115 added no new gate-owner decision; "R115/R116" is an
  evidence-source merge.

None of the seven changes any byte-level value in groups A–H/J, the
non-scientific-result boundary, the absence of G0 promotion, or governing.

## Content safety

- Independent report original **NOT uploaded** (contains 2 local paths); only
  the sanitized summary is published (0 local-path hits, 0 credential hits,
  0 email hits, 0 numeric scored-verdict lines).
- Full-repo scan: 10 strict pattern classes 0 hits; no file over 50 MiB; no
  binary / dataset / weight / third-party source / unpublished manuscript in
  the upload set. Primary scripts, JSON, isolated byte-identical copies,
  full ledger and raw gate readouts stay in the private workspace.
- Strict `git add --` explicit files only; staged re-scan; no merge / force
  push / branch deletion / Release; all twelve earlier published checkpoints
  untouched; private `ZtL-sysu/novix-platform` untouched.

## Supported vs unsupported conclusions

Supported: the recovered recheck verdict, the 7 accepted corrections, the new
I-2 first-hand evidence, and the byte-level reconciliation from checkpoint 12.
Unsupported / explicitly **not** claimed: any G0 pass, any scientific result,
any forward pass, any numeric manuscript score, any gate promotion, any state
write-back, any change to the success criterion, any new full independent
manuscript review, any 4090/L4/H20 capability claim.

## Result

Step-3 precondition (substantive positive new scientific evidence) unmet ⇒
no manuscript copy, no 9-page compile, no fresh isolated full review.
**0 papers qualified, no COMPLETE, governing still 6.0 / Confidence 4.0,
`NOT_QUALIFIED` / `INCOMPLETE`, G0 pending.** The heartbeat remains ACTIVE on
its unchanged 30-minute schedule. A checkpoint `completed` is a collaboration
work state, **not** a scientific conclusion.

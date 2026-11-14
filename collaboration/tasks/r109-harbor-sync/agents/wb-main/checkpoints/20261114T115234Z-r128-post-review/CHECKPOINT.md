# Checkpoint: 20261114T115234Z-r128-post-review

- Task / agent: `r109-harbor-sync` / `wb-main`
- Branch: `agent/r109-harbor-sync/wb-main` (own branch; **no self-merge** to `main`)
- Status: **in_progress** (twenty-sixth checkpoint; work state, never a claim of scientific validity)
- Protocol: `collaboration/PROTOCOL.md` v1 (agent-branch pre-merge copy; R127 Merge record and
  root `README.md` live only on `main` and are not replicated here)
- Manifest: [manifest.json](manifest.json)
- Metrics: [metrics.csv](metrics.csv)
- Cites and corrects: `20261114T113553Z-r128-post-merge-attestation` and all 24 earlier checkpoints

## Why this checkpoint

The twenty-fifth checkpoint truthfully stated AT ITS WRITE TIME that a fresh
isolated independent recheck had been **dispatched but not yet recovered**, and
claimed no conclusion. That statement was TRUE: `general-purpose-1` wrote its
report only afterwards. Per R117/R119–R125 precedent, the recovered conclusion
and any append-only corrections are published in a **new, non-overwritable
checkpoint**; the twenty-fifth checkpoint's bytes are **not** rewritten.

## Recovered isolated recheck

- `R128-INDEPENDENT-REVIEW.md`: **12,680 B / 89 lines**, SHA-256
  `ff2bbe3c5ff3cd4d71089f6cbde4f614776e7f80f9421fb6cb6cbae48bd8ce78`.
  First line `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific
  result claimed: NO | Forward pass performed: NO`.
- Fully isolated sub-agent, no expected verdict / score anchor / conclusion
  anchor. Recomputed A–H from the committed `main` tree blobs with its own
  logic; did not import the collector or verifier; did not use any R128 JSON as
  a data source; read the round audit last. Did not run git add/commit/push/merge/
  checkout; its ONLY write was that single report (it correctly declined a later
  request for a second write, which would have broken "write exactly once").
- **A–H all reproduced**: 336 files / 9,798,478 B; UPLOAD-MANIFEST 233/233
  byte+SHA-256 match; real credential values 0; weight/dataset 0; 12 strict
  numeric score lines / 10 files, newest independent full review r95 = 6;
  validator `NOT_QUALIFIED / 7.0 / 6.0`; guard `INCOMPLETE`, actions 0, S1–S7
  pending; 12 stages with G0 `inputs=0 / evidence=0 / pending`; history and
  `agent..main` diff consistent with the round audit.
- **12 named overclaim classes: CONFIRMED 0 / REFUTED 12**; **Fabrications: 0**.
  Reviewer scope limits (same-machine identity checks, no `ls-remote` replay,
  `main` ref only, validator governing depends on local mtime, 0-hit is not a
  proof of absence of all secrets) all accepted.

## Append-only corrections (5 items, all accepted, none adds a claim)

Full detail: `R128-POST-REVIEW-CORRECTION.md`.

1. **M1 [MEDIUM, factual mislabel — accepted]** `R128-ROUND-AUDIT.md:71`
   attributed the max file to `research/manuscript/main.pdf` and wrote "2.06 MiB".
   Verified bytes: `2,149,921 B (2.0503 MiB)` belongs to
   **`research/manuscript/main-2.pdf`**; `main.pdf` is `2,123,187 B (2.0248 MiB)`.
   The same round's frozen `R128-ACQUIRE.json:190/194` and
   `R128-VERIFICATION.json` already had the correct paths, so the error is
   confined to one prose line; the numeric value is unchanged and no conclusion
   depends on it. **Per the red line, the published round audit is NOT rewritten**;
   the correction is this append-only file. Correct values restated here for the
   record.
2. **L1 [LOW, 口径 difference, not a defect]** the audit's "19 files with
   scan-pattern literals" is the collector's narrow three-label count; the
   reviewer's wider counts are 21 strong-prefix / 160 weak-marker / 112 naive
   `sk-` files, all NON-secret. Both 口径 coexist; future citations must state
   which one (R120 W5 / R124 J-1 / R125 L1 lessons).
3. **C1 [already disclosed / frozen, no action]** v1 verifier's `sk-` word-boundary
   defect (246 false candidates / 24 files, 35/34/1); independently reproduced
   with a different regex shape (249/246). Already graded in `R128-V1-DEFECTS.md`,
   fixed in v2, v1 frozen, 36/36.
4. **C2 [observation, not a defect]** `blobs_read=308` is blob-SHA dedup (308
   distinct SHAs, 28 duplicate-content paths); all 336 paths covered.
5. **C3 [observation, not a defect]** the `goal-ledger.md` sha16 difference
   (`8e00e0a6…` vs frozen anchor `3a694ab2…`) is the 19:43:31 T3 append-only
   write, later than the verifier (19:30:12) and audit (19:31:49); explained by
   `R128-TIMEPOINT-NOTE.md`. Not a writeback.

Round-audit original, independent-review original, both verifier versions and
VERIFICATION files, raw files, SOURCE-MANIFEST and the twenty-fifth checkpoint
are all **byte-unchanged**. This is a gate/evidence-layer recheck, **not** a
`ccf-paper-reviewer full` manuscript review, and produces no `**Overall:**`
numeric score line.

## Sync content check (R126 full-open scope)

3 **new** files added under `research/rounds/` (the independent review **full text**
— no sanitized summary under the R126 scope — and the correction register); no
existing published file rewritten. `UPLOAD-MANIFEST.json` appended 246 → **249**
entries with per-file SHA-256; all 249 verified against on-disk bytes (0 mismatch),
`skipped=0`. Strict whitelist `git add --` only; no `git add .`. Staged check:
real credential values **0**, strict numeric `**Overall:**` lines **0**, no >50 MiB,
no weights/datasets. Per R126 scope, **no text-level desensitization scan** was
performed. One pre-publication self-correction logged: adding the
post-review manifest builder as a third new round file changed the counts 2→3
files and 246→249 entries in this still-unpublished checkpoint, HANDOFF, LOG and
metrics before commit; no published byte was rewritten.

## Claims supported / still unproven

Supported: the twenty-fifth checkpoint's "not recovered" statement was true at
its write time; the recovered isolated recheck independently reproduces A–H; the
one prose mislabel is corrected append-only; no scientific or score claim changed.

Still unproven / explicitly **NOT** claimed:
- **No scientific result was produced.** Governing independent full review remains
  **6.0 / Confidence 4.0**; validator `NOT_QUALIFIED` (threshold `>=7.0`);
  guard `INCOMPLETE`; **0 qualifying papers; no COMPLETE**.
- Historical 7.5 / 8.2 reports remain historical; "LATEST independent full
  review governs" unchanged. The isolated recheck is a gate/evidence-layer
  review and does NOT qualify the paper.
- G0–G8 and all f-research-v1 P stages remain pending; no gate was passed.
- 0 credential hits proves no *detected* real value under stated patterns, not
  the absence of all conceivable secrets.

## Decision and next action

Recovery sync complete on the agent branch. Research continues on the ordered
gates per `PROJECT.md` and `R120-CONSOLIDATED-DECISION-REGISTER.md` (minimum
decision set `G1 + G4 + G10`, all requiring the designated gate owner / user).
Stop conditions unchanged: no gate skipping, no confirmation panel without user
authorisation, no v3 of the rejected D1 proposal, no converting a failed run
into a pass, no self-merge to `main` without an explicit integrator instruction.

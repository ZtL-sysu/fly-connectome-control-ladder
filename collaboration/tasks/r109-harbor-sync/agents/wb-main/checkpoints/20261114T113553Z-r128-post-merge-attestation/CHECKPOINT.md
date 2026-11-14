# Checkpoint: 20261114T113553Z-r128-post-merge-attestation

- Task / agent: `r109-harbor-sync` / `wb-main`
- Branch: `agent/r109-harbor-sync/wb-main` (own branch; **no self-merge** to `main`)
- Status: **in_progress** (twenty-fifth checkpoint; work state, never a claim of scientific validity)
- Protocol: `collaboration/PROTOCOL.md` v1 (agent-branch pre-merge copy). The R127
  **Merge record** and the root `README.md` exist only on `main`, which is the
  integrator's post-merge docs commit; they are deliberately **not** replicated
  onto this agent branch. The v1 rules attested here are identical in both copies.
- Manifest: [manifest.json](manifest.json)
- Metrics: [metrics.csv](metrics.csv)
- Cites and corrects: `20261114T102224Z-r126-full-open` and all 23 earlier checkpoints

## Why this round

R126 (owner instruction) published a 233-file full-open research archive and R127
(owner instruction) merged it into the **PUBLIC default branch `main`** (336 files).
R126's credential check covered the **staged agent-branch diff before push**; R127's
check was a `merge-tree` **no-conflict** check. Neither attested the merged public
`main` tree end-to-end. The owner's **sole hard exclusion** is files containing a
**real credential value** (account risk). R128 performs that attestation on the
committed `main` tree, read-only. This is a safety/integrity check, **not** a
scientific result and **not** a claim of progress toward the acceptance criterion.

## Facts and commands actually run

- `git ls-tree -r -l -z main` + `git cat-file --batch` → all 336 **committed blobs**
  (not the working tree) enumerated and hashed. Script:
  `research/rounds/R128-ACQUIRE.py` → `R128-ACQUIRE.json`, raw list
  `R128-tree-paths.txt`.
- Independent verifier `R128-VERIFY.py` (does not import the collector, uses none
  of the R128 JSONs as a data source, uses a different/broader credential pattern
  set and one-cat-file-per-blob reading) → `R128-VERIFICATION.json`:
  **36 checks / 36 MATCH / 0 MISMATCH**.
- Read-only `validate_single_paper.py` and guard ledger/criteria reads; seven
  structural-authority SHA-256 anchors taken before and after → **7/7 identical**
  (zero writeback).

| Check | Result |
|:--|:--|
| Merged `main` tracked files / bytes | **336 / 9,798,478 B**; `research/` 235 |
| Max single file / >50 MiB | **2,149,921 B** (`research/manuscript/main.pdf`) / **0** |
| Model weights / dataset / binary suffixes | **0** |
| Real credential **values** (strict prefix+body, JWT, Bearer, PEM, quoted/bare assignments, hex, entropy heuristic) | **0** |
| Files with only scan-pattern literals / narrative | **19**, each context-checked; includes the R123 record that a third-party upstream public API-key literal was deleted before disk persist and never uploaded |
| `UPLOAD-MANIFEST.json` 233 declared entries vs merged public blobs | **233 / 233 byte-identical**, 0 mismatch, `skipped=0` |
| Published strict numeric `**Overall:**` lines | **12**, all in `research/reviews/`, dated ≤ 2026-11-11, newest independent full review r95 = **6** |
| Primary project strict numeric `**Overall:**` | **15 lines / 13 files / 10 distinct contents**; r95 = 3 byte-identical copies; no unregistered async full review |
| Local `main` / local HEAD / `origin/main` | all `6cc2e4fbe35121e6777f3c19c4502adc95f7427d` |
| agent branch local / remote | both `d76bb642dd502264230561327566c4c0c48af935` (retained, not deleted) |
| Validator | `NOT_QUALIFIED / 6.0 / >=7.0 / score_meets_threshold=false` (D1✓ D2✗ D3✗ D4✓ D5✗) |
| Guard | `INCOMPLETE`; ledger sha16 `73043b4e…`, criteria `94846083…`, A1–A6, S1–S7 pending, `actions=0` |
| Mainline `pipeline-state.json` | `CCFA-startup=passed`; **G0–G8 / validation / handoff all pending**, `G0.inputs=[]`, `G0.evidence=[]` |

### v1 verifier defect (frozen, not rewritten)

`R128-VERIFY-v1.py` / `R128-VERIFICATION-V1.json` are preserved. A naive `sk-`
entropy pattern matched `Ta`**`sk-`**`Aligned-Controls-for-Connectome-Vision`
across the project path, producing **246 false candidates** (35 checks / 34 MATCH /
1 MISMATCH). All 246 were diagnosed: label `sk-`, body `Aligned-Controls-for-Con…`,
0 pure-hex. v2 adds a lookbehind word guard and a check that pins the root cause;
v2 = 36/36. Full detail: `R128-V1-DEFECTS.md`. No data inconsistency, no
fabrication; both versions kept.

### Finding: the public progress mirror is stale (documented, not silently rewritten)

`research/ledger/goal-ledger.md` on `main` is **775,792 B**, a strict byte-prefix
of the primary project's current **781,988 B** ledger. The **6,196 B** appended
R126/R127 sections (18:32, after the R126 upload snapshot) are absent from the
public archive. R128 does **not** rewrite any published byte; it adds a new
append-only exact-byte delta file `research/ledger/R128-goal-ledger-delta-R126-R127.md`
(6,196 B, SHA-256 `88713b4f…`), verified free of real credential values and
numeric score lines, and records the gap here for the integrator.

### Sync content check (R126 scope)

13 **new** files added (12 under `research/rounds/`, 1 ledger delta); no existing
published file rewritten. `UPLOAD-MANIFEST.json` appended 233 → **246** entries,
per-file SHA-256; all 246 verified against on-disk bytes (0 mismatch), `skipped=0`.
Strict whitelist `git add --` only; no `git add .`. Content check on the new
files: **real credential values 0**, **strict numeric `**Overall:**` lines 0**,
**max 34,436 B** (no >50 MiB), no weights/datasets. Per R126 scope, **no
text-level desensitization scan** was performed; original text is uploaded as-is.
Three pre-publication self-corrections logged: (i) `R128-SOURCE-MANIFEST.json` v1
held a stale hash because `R128-BUILD-MANIFEST.py`'s UTC id was edited after
generation; v2 was regenerated from final bytes and the affected manifest entry
rebuilt; (ii) an append-only `R128-TIMEPOINT-NOTE.md` was then added, so the counts
in this still-unpublished checkpoint were corrected 12→13 files and 233→246
entries before commit; (iii) the manifest builder's artifact list initially
included the root `README.md`, which exists only on `main` (R127 docs commit) and
is absent on this pre-merge agent branch — removed before publication, with the
branch divergence recorded below. All three are unpublished-draft corrections,
not rewrites of any published byte. The timepoint note records that
`worktree_clean=True` in the acquire/verify JSONs is true only at collection time
T1/T2; this round's own sync writes make the worktree non-clean at T3 by design,
and `main` blobs never changed.

**Branch state**: this checkpoint is published on `agent/r109-harbor-sync/wb-main`
at `d76bb642…`, which is the pre-merge agent branch. `main` at `6cc2e4f…` is ahead
by the `--no-ff` merge and the integrator's docs commit. No self-merge, no
force push, no branch deletion, no Release.

## Claims supported / still unproven

Supported: the merged PUBLIC default branch at `6cc2e4f…` contains no real
credential value, no >50 MiB file and no weight/dataset; all 233 R126-declared
research files are byte-identical after the merge; all 23 review reports and their
score lines are historical and unchanged; no gate, score, threshold, state,
manuscript or review byte was written.

Still unproven / explicitly **NOT** claimed:
- **No scientific result was produced.** Governing independent full review remains
  **6.0 / Confidence 4.0**; validator `NOT_QUALIFIED` (threshold `>=7.0`);
  guard `INCOMPLETE`; **0 qualifying papers; no COMPLETE**.
- Historical 7.5 / 8.2 reports remain historical; "LATEST independent full review
  governs" unchanged; upload/merge does not qualify the paper.
- G0–G8 and all f-research-v1 P stages remain pending; no gate was passed.
- A manifest match proves **byte integrity**, not scientific validity; 0 credential
  hits proves no *detected* real value under the stated patterns, not that the repo
  is free of all conceivable secrets.
- Large weights/datasets are absent, so full experimental reproduction from this
  repo alone is still impossible.
- Uploading an unpublished double-blind manuscript to a public repo remains an
  owner-authorised disclosure, not a submission or publication.
- R126/R127 changed the repository scope and branch layout, **not** the success
  criterion, threshold, or the governing score.

## Fresh isolated independent recheck

`general-purpose-1` was dispatched with no expected verdict, score anchor or
conclusion anchor, told to recompute A–H from the committed blobs with its own
logic, judge 12 named overclaim classes, and grade defects. **At the time this
checkpoint was written it had not been recovered and no recheck conclusion is
claimed.** Per R117/R119–R125 precedent, the recovered conclusion and any
append-only corrections belong in a **new, non-overwritable checkpoint**; this
file's bytes are not rewritten. This is a gate/evidence-layer recheck, **not** a
`ccf-paper-reviewer full` manuscript review, and produces no Overall score line.

## Decision and next action

Sync complete on the agent branch. Research itself continues on the ordered gates
per `PROJECT.md` and `R120-CONSOLIDATED-DECISION-REGISTER.md` (minimum decision set
`G1 + G4 + G10`, all requiring the designated gate owner / user). Stop conditions
unchanged: no gate skipping, no confirmation panel without user authorisation, no
v3 of the rejected D1 proposal, no converting a failed run into a pass, no self-merge
to `main` without an explicit integrator instruction.

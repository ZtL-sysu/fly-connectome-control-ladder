# Checkpoint: 20261114T102224Z-r126-full-open

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: the full-open archive upload is done;
  NOT a scientific or paper-acceptance claim)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Metrics: [metrics.csv](metrics.csv)
- Cites and corrects: `20261113T121816Z-r109-init` and all 22 later checkpoints

## Owner instruction that triggered this checkpoint

2026-11-14 18:0x–18:1x: 「给我把研究成果，研究进展，研究思路这些整上去。那种大的
模型权重，数据集就不用传，不用担心。你把我说的东西都传一下，按照
`research-github-sync` 的规则来，里面有模版。按那个来，之前不对的你也整理整理」
then 「不用考虑脱敏的事情，open 就对了」。

This changed the repository's scope from a small sanitized collaboration log
to a **full-open public research archive**. Earlier checkpoints remain
untouched; this checkpoint records the change rather than rewriting them.

## Changes and actual commands

Built `research/` from an **explicit whitelist** (not `git add .`), grouped by
category. Each source file was checked for size, binary/data suffix, and real
credential values before copying. The full per-file index (path, bytes,
SHA-256) is `research/UPLOAD-MANIFEST.json`.

| Category | Files | Content |
|:--|--:|:--|
| `manuscript/` | 5 | TeX + PDF for `revision-r97` (the version reviewed as R95), the v2-R51 run, and `r93-candidate` TeX |
| `results/` | 10 | 10-seed main matrix `metrics.json` / `metrics_completed.json`, independent-family metrics, i1 runs, R63 density/robust, R78 control-ladder replay, `qualified_paper.json` |
| `reviews/` | 23 | **All** independent / full / idea review reports, full text, including 7.5 (R47/R49) and governing 6.0 (R95) |
| `guidance/` | 8 | `guidance-v2.md`, execution contracts v1–v3, `GOAL-ITERATION-R107.md`, G0 reviews, generated-directions index |
| `protocol/` | 30 | Frozen Candidate-E packet: claim-evidence matrix, competence spec, prediction dataflow, paired-edge-set spec, design reviews, prospective identities, prior-art map |
| `ideas/` | 10 | D1 proposals v1/v2, both independent reviews, D1 block decision, G4 positioning, literature matrix, dataset log, hardware profile |
| `ledger/` | 10 | full `goal-ledger.md`, `STATUS.md`, daily work logs 11-10 … 11-14 |
| `rounds/` | 129 | R106–R125 round audits, independent rechecks, post-review corrections, verifiers, source manifests, verification JSON, guard/validator readouts |
| `harbor/` | 8 | package, three-attempt trial log, final verification, route diagnosis |
| **total** | **233** | **~8.6 MiB** |

Rewrote `AGENTS.md` (removed the old "no manuscript PDF/TeX", "no unpublished
manuscript", "sanitized handoff layer", "no local absolute paths" statements),
updated `collaboration/PROJECT.md` status to R126 and its repo-purpose section,
and extended `TASK.md` scope/acceptance/writers. `PROTOCOL.md` is unchanged
(its rules were not the problem). `research/README.md` documents the archive.

## Checks and results

- `research/UPLOAD-MANIFEST.json`: 233 entries with SHA-256, **skipped: none**.
- Excluded by policy: large model weights/datasets, files >50 MiB, and **files
  containing a real credential value**. A regex scan for actual token values
  (`gho_…`, `ghp_…`, `AIza…`) over `research/` returned **0 hits**.
- **False-positive correction**: 11 verifier/audit files initially matched the
  credential *pattern* but contain only scan-pattern literals such as
  `b"ghp_"` and narrative wording. They were re-checked and included. No real
  secret was uploaded; no research file was lost.
- `metrics.csv` uses the fixed skill columns and only real values read from
  `metrics.json` (10-seed `mean_acc`: real 0.815234375, nulls 0.4795–0.5039,
  chance 0.5), the historical 7.5 / 6.0 review scores, and the harbor probe
  result (`sum=360.0`, reward 1.0). Target values are not mixed in; historical
  status is marked `historical`.
- Historical checkpoints, `evidence/`, review reports and the primary project
  were not modified. No gate status, score, threshold, protocol, seed or
  manuscript content changed.

## Corrections to earlier records ("之前不对的")

1. **Scope**: the previous `AGENTS.md`/`PROJECT.md` described this repo as a
   "sanitized collaboration log" with "no manuscript" — that conflicted with
   the owner's instruction and is now corrected here and in those files.
2. **Coverage gap**: earlier the archive held only 7 `*-SANITIZED.md`
   summaries. All 23 review reports, the full ledger, work logs, guidance,
   protocols and round audits are now present in full.
3. **R110–R113 round coverage**: earlier checkpoints jumped from `r109-init`
   to `r114-g0-license`. Verified locally: R110 and R111 have real round
   sections in `goal-ledger.md` and were cited in existing checkpoints;
   **R112 and R113 triggered the concurrency guard and performed read-only
   checks only, with no substantive output and no independent output
   directory** — so no standalone checkpoint was warranted, but the gap was
   never stated. `research/ledger/goal-ledger.md` now carries the full text and
   this checkpoint records the explicit reason. No checkpoint was back-filled
   or rewritten.
4. **Local absolute paths / redaction**: the prior convention replaced them
   with `<local>/`. Per the owner's "open 就对了" instruction, no text is
   rewritten now; original bytes are uploaded as-is.

## Claims supported / still unproven

Supported: the public repository now contains the research outputs, progress
records and ideas the owner asked for, with a verifiable per-file manifest and
a remote-confirmed upload. A new agent can read the science and the decision
history end-to-end.

Still unproven / explicitly NOT claimed:
- **No scientific result was produced by this upload.** Governing independent
  full review remains **6.0**; validator `NOT_QUALIFIED` (threshold 7.0);
  guard `INCOMPLETE`; **0 qualifying papers; no COMPLETE**.
- The 7.5 reports are historical; "latest independent full review governs" is
  unchanged, so uploading them does not qualify the paper.
- G0–G8 and all f-research-v1 P stages remain pending; no gate was passed.
- Harbor's reward 1.0 is an engineering CUDA probe on an NVIDIA H20, not a
  4090 result and not a scientific finding.
- Large weights/datasets are absent, so full experimental reproduction from
  this repo alone is still not possible; the gap is documented.
- Uploading an unpublished double-blind manuscript to a public repo is an
  owner-authorised disclosure. It is not a submission or publication, and the
  integrator should consider double-blind/priority implications before any
  external circulation.

## Decision and next action

Archive upload complete. Heartbeat should keep syncing future rounds using
the same explicit-whitelist + manifest + content-check procedure, and may now
upload full research content rather than sanitized summaries. Research itself
continues on the ordered gates in `PROJECT.md`. Stop conditions unchanged:
no gate skipping, no confirmation panel without user authorisation, no v3 of
the rejected D1 proposal, no converting a failed run into a pass, no merge to
the default branch without the integrator.

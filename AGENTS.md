# AGENTS.md — read this first

This is the **public research archive and collaboration log** for a project on
structure-sensitive null ladders in connectome-constrained vision.

Since R126 (2026-11-14) the owner has instructed that **research results,
progress records and research ideas are uploaded in the open**, with no
text-level redaction. Only large model weights/datasets and files containing a
real credential value are excluded. See `research/README.md`.

## What is here

- `research/` — **the actual science**: manuscripts (TeX/PDF), real experiment
  metrics, all independent/full/idea review reports, guidance and frozen
  protocols, research proposals and their independent reviews, the full
  round-by-round ledger and daily work logs, R106–R125 round audits, and the
  harbor trial. Start with `research/README.md` and
  `research/UPLOAD-MANIFEST.json` (per-file path, size, SHA-256).
- `evidence/` — the earlier, smaller sanitized evidence set. Retained
  unchanged; `research/` supersedes it in coverage.
- `collaboration/PROTOCOL.md` — rules for syncing and checkpoints.
- `collaboration/PROJECT.md` — goal, scientific protocol, true status.
- `collaboration/tasks/<task_id>/TASK.md` — task scope and acceptance.
- `collaboration/tasks/<task_id>/agents/<agent_id>/HANDOFF.md`, `LOG.md`,
  `checkpoints/<UTC-id>/` — snapshot, append-only log, immutable checkpoints.

## What is deliberately NOT here

- Large model weights and datasets (owner instruction; also the default
  50 MiB per-file ceiling).
- **Files containing a real credential value.** This is the one hard exclusion.
  It is not a redaction policy: such values would compromise the account, and
  they are not research output. Verifier scripts that merely contain scan
  pattern literals (e.g. `b"ghp_"`) ARE included.
- Third-party source trees and compiled binaries unrelated to our findings.

Missing large artifacts are recorded by relative path, size and hash in the
primary project; `research/README.md` states the gap. This archive lets a new
agent read and understand the science, but reproducing experiments requires
requesting the data separately.

## Status honesty

Governing independent full review is **R95 = 6.0**; acceptance is `>= 7.0`
(R107 user-authorised goal iteration). Validator `NOT_QUALIFIED`, guard
`INCOMPLETE`, **0 qualifying papers, no COMPLETE**, G0–G8 pending. Uploading
content does not change any of this, does not pass a gate, and does not
constitute submission or publication. Historical 7.5 reviews are retained but
do not govern.

## Rules for a new agent

1. Read `research/README.md`, `collaboration/PROTOCOL.md`, `PROJECT.md`, the
   relevant `TASK.md`, and the latest `HANDOFF.md`.
2. Work on a unique branch `agent/<task_id>/<agent_id>`. Never `git add .`.
   Stage only explicit files; check the staged diff; keep a per-file manifest.
   `main` is the default branch and was merged by the integrator on
   2026-11-14 (24 checkpoints + R126 archive); see `PROTOCOL.md` "Merge
   record". Publish new checkpoints on the agent branch; only the integrator
   merges them into `main`.
3. Do not treat a checkpoint or a manifest as scientific validation.
   `completed` describes work state only.
4. Do not change a scientific threshold, split, seed set, or acceptance rule to
   turn a failed result into a pass. Version such changes and keep old evidence.
5. Report "uploaded" only after confirming the remote branch SHA.
6. Do not rewrite or delete historical checkpoints; corrections are new
   checkpoints that cite the record being corrected.

The primary project working tree remains the authority for live state; this
repository is its public research record and handoff layer.

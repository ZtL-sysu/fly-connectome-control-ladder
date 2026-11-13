# AGENTS.md — read this first

This repository is a **collaboration and evidence-checkpoint log** for a
research project on structure-sensitive null ladders in connectome-constrained
vision. It is deliberately small and public.

## What is here

- `collaboration/PROTOCOL.md` — rules for syncing and checkpoints.
- `collaboration/PROJECT.md` — goal, current scientific protocol, true status,
  and where the primary evidence lives.
- `collaboration/tasks/<task_id>/TASK.md` — task scope and acceptance.
- `collaboration/tasks/<task_id>/agents/<agent_id>/HANDOFF.md` — current snapshot.
- `collaboration/tasks/<task_id>/agents/<agent_id>/LOG.md` — append-only log.
- `collaboration/tasks/<task_id>/agents/<agent_id>/checkpoints/<UTC-id>/` —
  one immutable checkpoint each: `CHECKPOINT.md`, `manifest.json`, and
  `metrics.csv` only when a real measurement exists.
- `evidence/` — small, sanitized, reproducible artifacts (protocols, scripts,
  summaries). **No datasets, no checkpoints, no credentials.**

## What is deliberately NOT here

The primary project is a large local working tree (~3000 files, including a
602 MB Sintel-derived development subset, official model checkpoints, a 190 MB
chain-status JSON, and compiled binaries). None of that is uploaded here. In
particular:

- No credentials, tokens, API keys, or account identifiers.
- No raw/derived Sintel data (non-commercial licence, redistribution excluded).
- No third-party source trees or model weights.
- No file over 50 MiB.
- No local absolute paths; they are replaced with `<local>/`.
- No manuscript PDF/TeX (double-blind, unpublished).

Where a checkpoint refers to such material, the path, size and SHA-256 are
recorded and the storage gap is stated explicitly. This is a collaboration
record, not a full reproduction bundle.

## Rules for a new agent

1. Read `collaboration/PROTOCOL.md`, `PROJECT.md`, the relevant `TASK.md`, and
   the latest `HANDOFF.md` on your own branch.
2. Work on a unique branch `agent/<task_id>/<agent_id>`. Never `git add .`.
3. Do not treat a checkpoint as scientific validation. `completed` describes
   work state only.
4. Do not change a scientific threshold, split, seed set, or acceptance rule to
   turn a failed result into a pass. Version such changes and keep old evidence.
5. Report "uploaded" only after confirming the remote branch SHA.

The authoritative scientific state lives in the primary project; this repo is
its public, sanitized handoff layer.

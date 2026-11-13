# Collaboration protocol v1

## Scope

This repository records research collaboration state for the project described
in `PROJECT.md`. It does **not** replace the primary project's scientific
protocol, experiment scope, or acceptance criteria. Existing evidence keeps its
original location in the primary project; this repo links to it by relative
path, size and SHA-256. Do not move or rewrite evidence just to fit this format.

## Single-writer discipline

| File | Writer |
|:--|:--|
| `PROTOCOL.md`, `PROJECT.md` | integrator (task owner) |
| `tasks/<task>/TASK.md` | task owner only |
| `agents/<id>/HANDOFF.md`, `LOG.md` | that agent only |
| `checkpoints/<UTC-id>/*` | immutable after publication |

Each worker uses its own branch `agent/<task_id>/<agent_id>`. Fetch the latest
main and relevant agent branches before starting. Never checkout/reset/stash in
a shared dirty worktree. A branch is progress, not a lock: read published
handoffs before starting overlapping work.

Merging into the default branch is an acceptance action by the designated
integrator only. This protocol does not authorise merge, force push, remote
branch deletion, releases, or messaging others.

## Checkpoint cadence

Commit at first claim/handoff, when an important result or failure appears,
when a long job starts/ends, and before handoff. During active work, consolidate
roughly every 15–30 minutes of meaningful change — not one commit per tool call.
Long jobs record provider, real job id, last verification time, and the recovery
command.

Each sync:
1. Update `HANDOFF.md`; append only this round's key decisions/failures to `LOG.md`.
2. Write `CHECKPOINT.md` with facts, commands run, checks, supported vs
   unsupported conclusions, artifacts, risks, next action. Status is one of
   `in_progress / completed / blocked / failed` (work state, never a claim of
   scientific validity).
3. Generate `manifest.json` with `checkpoint_manifest.py`; verify it.
   Paths are repo-relative; the manifest never contains its own hash.
4. Inspect `git diff --cached`, remove credentials, private conversation,
   local identity paths, caches and large duplicates. **Public-repo upload
   scope must be content-checked.** Files over 50 MiB stay local; record path,
   hash, size and intended storage. Do not silently route around this with LFS
   or releases.
5. Stage only explicit files (`git add -- <file> ...`), check the staged diff,
   confirm remote identity and own branch, commit, push own branch, then verify
   the remote SHA with `git ls-remote`. "Uploaded" requires remote confirmation;
   a local-only commit is reported as "not synced".

## Handling conflict, offline, and correction

- Push rejected: keep the local commit, fetch, inspect branch/owner. Resolve
  only explicit conflicts on your own clean branch. No force push, no overwrite,
  no infinite retry. One immediate retry for network failure, then record the
  unsynced commit SHA and recovery command.
- Re-check the protocol version before each sync. Material changes to goal,
  split, baseline, selection or scientific threshold must be versioned with
  their impact recorded. Old results stay; never change a hash or lower a
  threshold to convert a failure into a pass.
- A checkpoint is never overwritten. Corrections are a new checkpoint that
  cites the one being corrected and the reason. `HANDOFF` may roll forward,
  `LOG` appends; old commits and negative evidence remain traceable.
- `HANDOFF` must state: protocol path/hash, which files are trustworthy, which
  results are still unaccepted, which jobs are really running, the next
  executable command, and stop conditions. Missing weights or remote data are
  explicit gaps.

## What this protocol does not do

It does not declare experiments or papers accepted. A valid manifest and a
green checkpoint script are evidence of bookkeeping, not of scientific
validity.

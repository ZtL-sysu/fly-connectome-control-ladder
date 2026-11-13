# Checkpoint: 20261113T121816Z-r109-init

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **in_progress** (work state only; no scientific claim)
- Protocol: `collaboration/PROTOCOL.md` v1; scientific protocol in
  `collaboration/PROJECT.md`
- Manifest: [manifest.json](manifest.json)

## Changes and actual commands

Created a new **public** collaboration repository and its first sanitized
checkpoint. Commands actually run (local paths redacted):

```bash
git init -q -b main                     # in a separate sync root, not the primary project
gh repo create <owner>/fly-connectome-control-ladder --public --source <sync-root> --remote origin
gh auth status                          # confirmed a single authenticated account
gh repo view <owner>/novix-platform --json visibility   # PRIVATE, contains credentials: untouched
```

Collaboration files written: `AGENTS.md`, `collaboration/PROTOCOL.md`,
`collaboration/PROJECT.md`, `tasks/r109-harbor-sync/TASK.md`,
`agents/wb-main/HANDOFF.md`, `LOG.md`, this `CHECKPOINT.md`.
Sanitized evidence copied to `evidence/`: goal-iteration record, G0 recency
review, D1 block decision, harbor trial log + package, and a redacted Novix
route-diagnosis JSON (7 dispatch rows preserved; one account identifier
replaced with a placeholder).

`checkpoint_manifest.py create/verify` used for the hash manifest.

## Checks and results

- Content scan of the whole upload set (excluding `.git`): **0 hits** for
  credentials, tokens, account identifiers, or local absolute paths after one
  correction in `TASK.md`.
- No file over 50 MiB (largest is ~7.6 KiB). No binary, dataset, weight,
  archive, compiled library, or PDF. Total upload set: 16 small text files.
- Deliberately excluded and recorded: 602 MB Sintel-derived development subset
  (non-commercial licence, redistribution excluded), 190 MB chain-status JSON,
  124 MB CIFAR archive, 130 MB compiled dylib, official model checkpoints,
  third-party source trees, the unpublished double-blind manuscript, and the
  pre-existing **private** repo containing real credentials.
- `harbor_task_lint --dry-run` results quoted in `evidence/R108-HARBOR-TRIAL.md`:
  attempt 1 = 9 pass / 0 fail; attempts 2 and 3 = 8 pass / 1 warn / 0 fail.
- Local Conda self-test of the harbor package: probe success (CPU), verifier
  rc 0 with engineering-only reward, empty-environment branch rc 1 with
  `apparatus_fault` and no reward file.
- No `metrics.csv` in this checkpoint: **no new measurement was produced**.
  An empty table is not fabricated.

## Claims supported / still unproven

Supported by this checkpoint:
- The collaboration layer exists, is public, is sanitized, and its state
  agrees with the primary project's recorded status.
- The R107 goal iteration and R108 harbor attempts happened as documented,
  with three real task ids (25075, 25076, 25092) and verbatim failure reasons.

Still unproven / explicitly NOT claimed:
- **No GPU execution, no verifier reward, no scientific result from harbor.**
  Task 25092 was `processing / harborPhase=building` at the last check
  (2026-11-13 20:16 +0800).
- The 4090 pool was `offline` at submit time; harbor tests its own GPU path,
  not the broken `--resource-pool` route.
- Governing independent full review remains **6.0**; validator
  `NOT_QUALIFIED`; guard `INCOMPLETE`; 0 qualifying papers; no COMPLETE.
- G0–G8 and all f-research-v1 P stages remain pending. Confirmation panel
  not authorised.

## Decision and next action

Continue. Live jobs: harbor task 25092 (Novix, building) and the local
heartbeat automation (ACTIVE, every 30 min, recovers 25092 first).

Next command for a resuming agent:

```bash
novix --json task result 25092
# finish -> novix debug pull task:25092 <out> --sub project/results/r108_probe
#          then independently recompute probe arithmetic from raw artifacts
# error  -> novix debug build-logs 25092, record verbatim, STOP harbor retries
```

Stop conditions: no gate skipping, no confirmation panel without user
authorisation, no v3 of the twice-rejected D1 proposal, no converting a failed
run into a pass, no publishing sensitive or oversized material, no merging to
the default branch without the integrator.

# HANDOFF — wb-main / r109-harbor-sync

- Task / agent / branch: `r109-harbor-sync` / `wb-main` /
  `agent/r109-harbor-sync/wb-main`
- Status: **in_progress** (3 checkpoints published; harbor trial closed, research itself unfinished)
- Last update: 2026-11-13 22:0x +0800
- Protocol: `collaboration/PROTOCOL.md` v1; `collaboration/PROJECT.md`
- Repo: `ZtL-sysu/fly-connectome-control-ladder` (public)

## Completed

- Public repo created with a sanitized collaboration layer only.
- R107 goal iteration recorded: independent full-review acceptance changed from
  strictly > 8.0 to **>= 7.0** (equal qualifies). Machine validators synced.
  Historical 7.5 reports are NOT promoted to governing.
- R108 harbor-trial evidence sanitized and published: the package, the trial
  log, a redacted route-diagnosis JSON with 7 dispatch rows, and the goal
  iteration record.
- Content scan performed: no credentials / local absolute paths / dataset
  binaries / files >50 MiB in the upload set.

## NOT completed / do not assume

- **Harbor trial finished with a verified engineering reward (1.0).**
  CUDA execution on **NVIDIA H20**, independent recomputation passed, frozen
  probe SHA matched. **Still no scientific result and no 4090 claim.** See
  checkpoints `20261113T130720Z-r108-build` and `20261113T140607Z-r108-final`.
- Two earlier harbor attempts failed (25075 COPY-context error; 25076
  platform 1800 s image-build timeout). Both retained verbatim in the primary
  project; 25092 is the declared last build-stage attempt.
- Governing independent full review remains **6.0**, validator
  `NOT_QUALIFIED`, guard `INCOMPLETE`, 0 qualifying papers, no COMPLETE.
- Confirmation panel (<=32 h / K=45) is **not authorised**; an explicit user
  decision is still pending.
- G0–G8 and all f-research-v1 P stages remain pending.

## Trustworthy files here

`AGENTS.md`, `collaboration/PROTOCOL.md`, `collaboration/PROJECT.md`,
`tasks/r109-harbor-sync/TASK.md`, this HANDOFF, `LOG.md`,
`checkpoints/<UTC-id>/CHECKPOINT.md` and its `manifest.json`,
`evidence/**` (small, sanitized, hash-listed).

## Known gaps

The primary evidence (datasets, checkpoints, full reviews, full ledger,
manuscript) is **not** in this repo. `PROJECT.md` and `AGENTS.md` state why.
A new agent cannot reproduce experiments from this repo alone; it can read the
protocol and know exactly which local artifacts to request.

## Running jobs (verified 2026-11-13 20:16 +0800)

| Job | Provider | State | Recovery |
|:--|:--|:--|:--|
| 25092 | Novix harbor | **FINISH**, `reward=1.0`, `measurementValid=true`, 169 steps, device **H20** (not 4090), no scientific result | trial closed; optional `novix debug pull task:25092 <out> --sub project/results/r108_probe` after track-ops recovers |
| heartbeat | local automation | ACTIVE, every 30 min | reads the primary project's `goal-ledger.md` |

Do not claim either produced a scientific result.

## Next executable command (for a resuming agent)

```bash
# Harbor trial is closed. Resume the ordered research gates instead.
# If workspace files are needed later (track-ops was unreachable):
novix debug pull task:25092 <out> --sub project/results/r108_probe
# then re-verify file hashes against the trajectory raw values.
```

Stop conditions: do not skip gates, do not open the confirmation panel without
user authorisation, do not reissue a v3 of the rejected D1 proposal, do not
turn a failed run into a pass, do not publish sensitive material.

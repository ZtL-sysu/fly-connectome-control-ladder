# HANDOFF — wb-main / r109-harbor-sync

- Task / agent / branch: `r109-harbor-sync` / `wb-main` /
  `agent/r109-harbor-sync/wb-main`
- Status: **in_progress** (4 checkpoints published; harbor trial closed, research itself unfinished)
- Last update: 2026-11-13 22:4x +0800
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
- R114 G0 gap-1 first-hand license verification: sanitized summary published
  (`evidence/R114-G0-R1-LICENSE-EVIDENCE.md`). Two previously OPEN items
  **advanced to recomputable first-hand attachments but remain PARTIAL**:
  Zenodo 21549559 license identifier `cc-by-4.0` (one Zenodo metadata source
  exposed through three same-source views, NOT independent cross-checks), and
  the MPI Sintel official non-commercial license page. **Gap 1 overall is
  still PARTIAL; no gate was passed.** A fresh isolated recheck returned
  `PARTIAL | G0 may be passed: NO` and identified overclaims (withdrawn by
  appending a correction register). Raw bytes and hashes stay in the primary
  project and are not uploaded.
- Content scan performed each sync: no credentials / local absolute paths /
  dataset binaries / files >50 MiB in the upload set.

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

## Running jobs (verified 2026-11-13 22:4x +0800)

| Job | Provider | State | Recovery |
|:--|:--|:--|:--|
| 25092 | Novix harbor | **FINISH**, `reward=1.0`, `measurementValid=true`, 169 steps, device **H20** (not 4090), no scientific result | trial closed; optional `novix debug pull task:25092 <out> --sub project/results/r108_probe` after track-ops recovers |
| heartbeat | local automation | ACTIVE, every 30 min | reads the primary project's `goal-ledger.md` |
| R114 isolated review | local isolated sub-agent | **RECOVERED** `PARTIAL \| G0 may be passed: NO \| Scientific result claimed: NO`; final 26,104 B, SHA-256 `879ecb78…3e`. Found 7 flaws; two substantive overclaims (same-source views called independent sources; license identifier called LICENSE text CLOSED) withdrawn by appended correction register. | primary project `gate-G0-R114/R114-G0-R1-INDEPENDENT-REVIEW.md` + `R114-POST-REVIEW-CORRECTION.md` |

Do not claim any of these produced a scientific result. A gate-evidence
recheck is not a `ccf-paper-reviewer full` manuscript review and must not
produce an Overall score line.

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

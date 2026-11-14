# R108 harbor 25092 — final verification

Date: 2026-11-13 22:0x +0800. Status: **harbor task finished with a verified
engineering reward. NO scientific result.**

## Terminal state (double-confirmed)

`novix --json task result 25092` and `novix --json task get 25092`:

| Field | Value |
|:--|:--|
| `status` | `finish` |
| `harborPhase` | `done` |
| steps | 169 |
| `harborResult.reward` | `1.0` |
| `observedReward` / `visibleReward` | `1.0` / `1.0` |
| `measurementValid` | `true` |
| `tamperSuspected` | `false` |
| `rewardSource` | `reward.json` |
| `testsDigestExpected` | `d772852a5783ab75b296cacade300c02d4c12bc6351ea2fdc3b055e173c861ac` |
| `testsDigestObserved` | identical to expected |
| `harborImageDigest` | `sha256:3f6290d03df10654a0243bb0fc40c8c9bb27383685760e7811a4d8232f583e79` |
| `executionSummary.result_subtype` | `success`, elapsed 1563.84 s |

`rewardRaw`: `{"reward":1.0,"metric":"environment_verification","scope":
"ENGINEERING_ONLY_NO_SCIENTIFIC_RESULT","probe_device":"cuda","status":"verified"}`

## Artifact retrieval limitation (honest)

`novix debug pull task:25092 ... --sub project/results/r108_probe` **failed**
twice with: `track-ops ... does not answer /healthz`. The track-ops endpoint is
unreachable from this session, so no workspace files were pulled to disk.

Independent verification was therefore performed on the **raw values embedded
in the 169-step trajectory returned by `task get`** (saved at
`/tmp/r108_taskget.json`, 229,414 B). This is not the same as holding the
workspace files; the gap is recorded rather than glossed over.

## Independent recomputation (local, from raw values, not self-report)

Values recovered from the trajectory's `result.json` fragment:

| Field | Observed |
|:--|:--|
| `probe_device` | `cuda` |
| `cuda_available` | `true` |
| **`device_name`** | **`NVIDIA H20`** |
| `torch_version` | `2.5.1+cu124` |
| `probe_script_sha256` | `d3659dcb886a89ae65098a6f3f51b0f350c63307d029a66d33f843bed24f883c` |
| `probe_matrix_flat` | 16 finite values |
| `probe_expected` | `360.0` |
| `probe_observed` | `360.0` |
| `all_finite` / `probe_ok` | `true` / `true` |
| `scientific_result` / `training` | `false` / `false` |

Local checks (recomputed here, not copied from the remote verdict):

- `sum(probe_matrix_flat) = 360.0` → matches `probe_expected` ✅
- `probe_observed = 360.0` → matches the recomputed sum ✅
- all 16 values finite ✅
- `sha256(harbor-r108/tests/probe.py) = d3659dcb…883c` → **byte-identical to
  the frozen local probe** ✅ (EXEC LOCK held; the remote agent did not alter
  the probe script)
- engineering-only boundary flags all false for scientific result / training ✅

Note: the first `"status":"running"` string in the trajectory is an early
`result.json` write during execution; the terminal `finish` is confirmed by
`task get`. No contradiction.

## What this establishes — and what it does NOT

**Established**: the harbor题包 entry point works. After two failures
(25075 COPY-context defect, 25076 platform 1800 s build timeout), task 25092
with `--build-timeout 3600` produced a real image, executed the frozen probe
**on a CUDA device**, passed a verifier that independently recomputes the
arithmetic and checks hashes, and returned a measurement-valid reward of 1.0
with no tamper suspicion. This is the first end-to-end verified heavy-work
execution through harbor in this project.

**NOT established**:
- **The GPU is an NVIDIA H20, not a 4090.** `cuda_available=true` and a real
  CUDA compute, but the device is H20. No 4090 claim. The exp-4090 pool was
  `offline` at submit time; harbor used its own GPU path.
- **No scientific result whatsoever.** The probe is a deterministic 4×4
  matrix multiply. `rewardRaw.scope` says
  `ENGINEERING_ONLY_NO_SCIENTIFIC_RESULT`. No training, no labels, no dataset,
  no real model forward.
- **No paper / review / score change.** Governing independent full review
  remains R95 6.0; validator `NOT_QUALIFIED`; guard `INCOMPLETE`;
  0 qualifying papers; no COMPLETE.
- The workspace artifacts themselves were not retrieved (track-ops outage);
  verification used trajectory-embedded raw values plus the local frozen
  script hash.

## Next

If artifacts are needed later, retry `novix debug pull task:25092 <out> --sub
project/results/r108_probe` after track-ops recovers, then re-verify the file
hashes. Harbor can now be treated as a **usable heavy-work entry point** for
engineering-style GPU tasks, subject to: pinned environment deps (torch was
absent in the default image and had to be installed at runtime), adequate
build timeout, and no assumption about which GPU model is allocated.

No commit / push / submission of the primary project.

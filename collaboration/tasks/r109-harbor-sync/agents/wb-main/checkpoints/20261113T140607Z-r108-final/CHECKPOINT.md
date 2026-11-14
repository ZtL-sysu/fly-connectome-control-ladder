# Checkpoint: 20261113T140607Z-r108-final

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: the harbor trial finished; NOT a scientific
  or paper-acceptance claim)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Cites: `20261113T121816Z-r109-init`, `20261113T130720Z-r108-build`

## Changes and actual commands

Tracker `XyCcV5` caught the true terminal state of harbor task 25092 at
22:00:26 +0800. Commands run:

```bash
novix --json task result 25092
novix --json task get 25092          # double confirmation
novix --json debug pull task:25092 <out> --sub project/results/r108_probe   # failed x2
```

`debug pull` failed twice because track-ops `/healthz` was unreachable, so
**workspace files were not retrieved**. Verification used the raw values
embedded in the 169-step trajectory returned by `task get` plus the frozen
local probe script. Full audit:
`evidence/R108-FINAL-VERIFICATION.md`; the trial log was refreshed in
`evidence/R108-HARBOR-TRIAL.md`.

## Checks and results

Terminal state (double-confirmed): `status=finish`, `harborPhase=done`,
169 steps, `harborResult.reward=1.0`, `observedReward=1.0`,
`measurementValid=true`, `tamperSuspected=false`, `rewardSource=reward.json`,
`testsDigestExpected == testsDigestObserved =
d772852a5783ab75b296cacade300c02d4c12bc6351ea2fdc3b055e173c861ac`,
`result_subtype=success`, elapsed 1563.84 s.

Independent local recomputation from trajectory raw values (not self-report):

| Check | Result |
|:--|:--|
| `probe_device` / `cuda_available` | `cuda` / `true` |
| **`device_name`** | **`NVIDIA H20` — NOT a 4090** |
| `torch_version` | `2.5.1+cu124` |
| `probe_matrix_flat` | 16 finite values, `sum = 360.0` |
| `probe_expected` / `probe_observed` | `360.0` / `360.0` — both equal recomputed sum ✅ |
| `probe_script_sha256` | `d3659dcb…883c` = local `sha256(tests/probe.py)` ✅ EXEC LOCK held |
| `scientific_result` / `training` | `false` / `false` |
| reward scope | `ENGINEERING_ONLY_NO_SCIENTIFIC_RESULT` |

Whole-repo content scan repeated: 0 hits for credentials, tokens, account
identifiers, local absolute paths; no file over 50 MiB; no datasets, weights,
binaries or unpublished manuscript.

`metrics.csv` is deliberately absent. The only number here (`360.0`) is a
deterministic 4×4 matrix-multiply probe constant, not a research measurement;
fabricating a metrics row would misrepresent it.

## Claims supported / still unproven

Supported:
- **Harbor is a usable heavy-work entry point** for engineering GPU tasks in
  this project: image build → CUDA execution → verifier independent
  recomputation → measurement-valid reward 1.0, first end-to-end verified run.
- The two earlier failures were correctly diagnosed and fixed one at a time
  (25075 COPY context; 25076 platform 1800 s build timeout, fixed by
  `--build-timeout 3600`).
- The frozen probe was not altered by the remote agent (SHA match).

Still unproven / NOT claimed:
- **No scientific result.** The probe is a deterministic 4×4 multiply; no
  training, labels, dataset, or real model forward.
- **No 4090 capability claim.** The device was H20; the exp-4090 pool was
  offline at submit time and harbor uses its own GPU path.
- Workspace artifacts were not pulled (track-ops outage); verification rests on
  trajectory-embedded raw values plus the local frozen script.
- Governing independent full review remains **6.0**; validator
  `NOT_QUALIFIED`; guard `INCOMPLETE`; 0 qualifying papers; no COMPLETE.

## Decision and next action

Harbor trial **closed**. Three operational caveats for any future heavy run:
(1) the default image has no importable torch — pin it in the environment;
(2) a cold 1.36 GB CUDA base pull needs build timeout >= 3600 s;
(3) the allocated GPU model is not guaranteed (H20 here).

If the workspace files are needed, retry after track-ops recovers:

```bash
novix debug pull task:25092 <out> --sub project/results/r108_probe
```

Research continues on the ordered gates in `collaboration/PROJECT.md`
(G0–G8 all pending). Stop conditions unchanged: no gate skipping, no
confirmation panel without user authorisation, no v3 of the rejected D1
proposal, no converting a failed run into a pass, no publishing sensitive
material, no merge to default branch without the integrator.

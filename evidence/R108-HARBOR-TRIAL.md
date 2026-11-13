# R108 — harbor 题包试验（正经重活入口）

Date: 2026-11-13 19:2x–19:3x +0800. User request: 「试试呗，正经干重活的入口方式，试一试」.
Status: **IN PROGRESS — 任务 25076 镜像构建中**. Engineering-only; no scientific result.

## Why this trial

All prior Novix work used bare `task create` with natural-language queries and
base64-injected scripts. The official CLI docs state plainly: *"想长期跑自有项目
应走 harbor 题包（task.toml + Dockerfile + tests），而非裸 task create"*
(`references/platform.md` 使用含义). This trial tests that entry point for the
first time in this project.

## Package built (`harbor-r108/`)

| File | Role |
|:--|:--|
| `task.toml` | `completion_mode="artifacts"`, `required_artifacts=[result.json, manifest.json]`, `[environment] gpus=1 cpus=4 memory_mb=16384` |
| `instruction.md` | EXEC LOCK: no training / optimizer / labels / dataset / real model forward; agent must run `tests/test.sh` itself |
| `tests/probe.py` | Frozen deterministic CUDA probe: 4×4 matrix @ diagonal W, recomputable from raw values; reports device/torch/CUDA, all-finite, self SHA |
| `tests/test.sh` | Verifier: re-computes the arithmetic from raw matrix, checks probe SHA + manifest hashes + artifact existence, writes `reward.json`; empty-environment run takes the apparatus exit |
| `solution/solve.sh` | Reference solution: run probe, then verifier; never touches `logs/verifier` or score |
| `environment/Dockerfile` | **Removed after attempt 1** — see below |

**No Dockerfile in the submitted v2**: lint confirms the platform default
`ubuntu/cuda` image is used, which is what supplies torch/CUDA. A custom
`FROM python:3.11-slim` would have replaced that base and made the GPU probe
meaningless.

## Verification performed locally (conda python)

- `tests/probe.py` on CPU → `status=success`, `probe_device=cpu`.
- `tests/test.sh` with artifacts → rc 0, writes
  `reward.json{"reward":1.0,"scope":"ENGINEERING_ONLY_NO_SCIENTIFIC_RESULT"}`.
- Empty-environment branch → rc 1 and `verifier_error.json` with string
  `apparatus_fault`, no `reward.json`. Required by `harbor_task_lint`.

## Attempt 1 — task 25075 (FAILED, retained)

- `task harbor harbor-r108 --dry-run` → lint **9 pass / 0 warn / 0 fail**,
  spec `enableGpu:true, gpuCount:1`.
- Real submit created task **25075**, `harborPhase=building` — i.e. it did NOT
  die at `ControlPlaneFailure / steps 0` like every bare `task create` carrying
  `--resource-pool`. It reached the image build stage.
- `errorCode=HARBOR_ENV_BUILD_FAILED`: Yunxiao build could not find
  `/instruction.md`, `/tests`, `/environment/Dockerfile`. **Root cause**: the
  platform uses `environment/` as the Docker build context, so COPYing task
  files from the task root is invalid; the task overlay is mounted at runtime.
- Preserved verbatim; not deleted or hidden.

## Attempt 2 — task 25076 (IN PROGRESS)

- Fix: removed `environment/Dockerfile` entirely (old copy kept at
  `/tmp/r108-Dockerfile.v1`), letting the platform default CUDA image build.
- `--dry-run` → lint **8 pass / 1 warn / 0 fail** (the WARN is expected: no
  Dockerfile → default ubuntu/cuda base).
- Submitted → **task 25076**, session `468b4154ee04f4ed0596335e6456460e`,
  `status=processing`, `harborPhase=building`, `build_id=yx-ce87172b-…`.
- `debug build-logs 25076` shows a real CUDA base layer pulling:
  `1.36 GB`, at 19:35:31 `243.27 MB / 1.36 GB`, ~0.4 MB/s, `status=working`.
  This is genuine build progress, not a stall. Estimated tens of minutes.
- A background tracker (`SyzZZV`) polls to terminal state; heartbeat is
  instructed to recover the result.

## What is NOT claimed

- No GPU execution, no reward, no scientific result has been obtained yet.
- No claim that exp-4090 is reachable: the pool probe at submit time showed
  both exp-4090 nodes `offline`, `usable_nodes=[]`. Harbor's own GPU path is
  what is being tested here, not the `--resource-pool` route.
- No frozen artifact, contract, gate status, score or manuscript changed.
- No commit / push / submission.

## Next steps (heartbeat / next session)

1. Poll `novix --json task result 25076` to terminal state.
2. If `finish`: read `harborResult` (reward / cleanReward / image digest), then
   `novix debug pull task:25076 <out> --sub project/results/r108_probe`, and
   **independently recompute** from raw artifacts.
3. If `error`: read `errorInfo` + `novix debug build-logs 25076`, record
   verbatim, fix at most one concrete defect with a documented reason, and
   resubmit as a new task id (no identical retry, no deleting failures).
4. Only after a verified reward should harbor be considered a viable heavy-work
   entry point. Until then: still experimental.

---

## Attempt 2 result — task 25076 FAILED (retained), 2026-11-13 20:01

Terminal: `status=error`, `errorCode=HARBOR_ENV_BUILD_FAILED`,
`harborPhase=done`, `harborImageDigest=null`,
`harborResult.workspaceFailureReason="session workspace not found"`.

`debug build-logs 25076` tail (verbatim essence):
```
#5 DONE 1793.6s
#6 [2/2] RUN apt-get update && apt-get install -y ... python3 ...
#6 CANCELED
ERROR: failed to solve: Canceled: context canceled
subprocess.TimeoutExpired: Command ['docker','buildx','build','--platform','linux/amd64',
  '--progress=plain','--provenance=false','--pull','--build-context', ...]
Managed build failed: CalledProcessError
```

**Root cause: platform-side image-build timeout, not a package defect.**
Pulling the 1.36 GB default CUDA base layer consumed 1793.6 s — almost
exactly the default 1800 s build ceiling. The very next `RUN apt-get` layer was
cancelled and the build subprocess raised `TimeoutExpired`. The 404
`NoSuchKeyError` and `session workspace not found` are downstream consequences
of the build being cancelled before any artifact/workspace was registered.
The `--dry-run` lint had 0 fail, so the package itself was accepted.

CLI source confirms `--build-timeout` maps to `spec["buildTimeoutSeconds"]`
(`backend.py:514-516`), max 3600 (`task.py:496`). Default is the 1800 s ceiling
we hit.

## Attempt 3 — task 25092 (IN PROGRESS)

Single-defect fix, documented: raise build ceiling only.
`novix --json task harbor harbor-r108 --max-turns 20 --timeout 3600 --build-timeout 3600`
→ task **25092**, session `83ab1ec05301b8682ef498bfc717c264`,
`status=processing`, `harborPhase=building`,
spec `buildTimeoutSeconds: 3600`. Package unchanged otherwise (lint 8 pass /
1 warn / 0 fail).

Rationale for one more attempt: the 1.36 GB base layer was already pulled in
attempt 2, so a cache hit should make attempt 3 much faster; and the timeout is
an explicitly configurable, single, evidenced parameter. **This is the last
build-stage attempt.** If it fails for a different platform reason, record it
verbatim and stop retrying harbor until the platform's build service is healthy;
do not enter an unbounded patch loop (R105 precedent).

## Recovery instruction (heartbeat / next session)

1. `novix --json task result 25092` to terminal state.
2. `finish` → read `harborResult` (reward / cleanReward / image digest), then
   `novix debug pull task:25092 <out> --sub project/results/r108_probe`, and
   **independently recompute** the probe arithmetic from raw artifacts.
3. `error` → read `errorInfo` + `novix debug build-logs 25092`, record verbatim,
   and STOP harbor retries. Report the platform build-service blocker.
4. Only a verified reward makes harbor a viable heavy-work entry point.
   Until then: experimental, no GPU execution claim, no 4090 claim.

---

## Attempt 3 milestone — BUILD SUCCEEDED, run in progress (2026-11-13 21:0x)

Background tracker `dNf5Pa` (55 × 1 min) recorded the phase transition:
`building` through 20:39:57 → **`running` from 20:41:04 through 21:04:16**,
still `processing`. The tracker exhausted its poll count; the task did NOT
terminate.

Direct re-check confirms:
- `harborPhase = "running"`, `status = "processing"`, `errorCode = None`.
- **`harborImageDigest = sha256:3f6290d03df10654a0243bb0fc40c8c9bb27383685760e7811a4d8232f583e79`**
  — the first successfully built image digest in all three attempts.
- `debug build-logs 25092` returns `status = "success"`, ending with
  `run cache step successfully!`.
- `harborResult = None`, `steps = []`, no `reward` yet; the agent is executing
  `instruction.md` inside the container.

**Interpretation**: the single `--build-timeout 3600` fix worked. The 1.36 GB
CUDA base pull finished within the raised ceiling, the `apt-get` layer
completed, and the image was pushed. This is an **engineering milestone, not a
result**: no probe output, no verifier reward, no scientific claim yet.

A fresh tracker `D8mdCU` polls the run phase. Recovery on finish:
`novix --json task result 25092` → read `harborResult` →
`novix debug pull task:25092 <out> --sub project/results/r108_probe` →
independently recompute the probe arithmetic from raw artifacts. On error:
`novix debug build-logs` / `task result` verbatim, record, and stop harbor
retries as previously declared.

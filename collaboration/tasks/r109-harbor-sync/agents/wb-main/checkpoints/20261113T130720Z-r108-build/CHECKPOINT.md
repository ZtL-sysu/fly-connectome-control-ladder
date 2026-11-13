# Checkpoint: 20261113T130720Z-r108-build

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **in_progress** (work state; not a scientific claim)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Supersedes: nothing; cites `20261113T121816Z-r109-init`

## Changes and actual commands

A background tracker for harbor task 25092 completed its poll budget without
the task terminating. Its log shows a real phase transition:

```
building through 20:39:57  ->  running from 20:41:04 through 21:04:16
```

Commands actually run to verify (no secrets in this repo):

```bash
novix --json task result 25092
novix --json task get 25092
novix --json debug build-logs 25092
novix --json debug ls task:25092 -L 3
```

`evidence/R108-HARBOR-TRIAL.md` was refreshed with the milestone section and
rescanned (0 sensitive hits). A new immutable checkpoint directory was created;
the earlier checkpoint is untouched.

## Checks and results

- `harborPhase = running`, `status = processing`, `errorCode = None`.
- **`harborImageDigest = sha256:3f6290d03df10654a0243bb0fc40c8c9bb27383685760e7811a4d8232f583e79`**
  — the first successfully built image digest across attempts 25075 / 25076 /
  25092.
- `debug build-logs 25092` → `status = success`, tail
  `run cache step successfully!`.
- Interpretation: the single documented fix `--build-timeout 3600` worked. The
  1.36 GB CUDA base layer finished inside the raised ceiling, the `apt-get`
  layer completed and the image was pushed. Attempt 2 died at 1793.6 s against
  the 1800 s default; attempt 3 did not.
- Whole-repo content scan repeated: no credentials, tokens, account
  identifiers, or local absolute paths; no file over 50 MiB; no datasets,
  weights, binaries, or unpublished manuscript. Largest file is ~9 KiB.
- No `metrics.csv`: **no measurement has been produced yet**. No empty table
  is fabricated.

## Claims supported / still unproven

Supported:
- A harbor task package passed lint, built a GPU-capable image, and entered the
  execution phase. This is the first time in this project that the official
  heavy-work entry point got past image build.
- The build-timeout diagnosis for attempt 2 was correct and the single-parameter
  fix was effective.

Still unproven / explicitly NOT claimed:
- **No probe output, no verifier reward, no GPU execution result.**
  `harborResult = None`, `steps = []`, `reward` absent. The agent is running
  `instruction.md` inside the container.
- No claim about exp-4090 availability: the pool was `offline` at submit time;
  harbor uses its own GPU path, not the broken `--resource-pool` route.
- Governing independent full review remains **6.0**; validator
  `NOT_QUALIFIED`; guard `INCOMPLETE`; 0 qualifying papers; no COMPLETE.

## Decision and next action

Continue polling. A fresh tracker polls the run phase; heartbeat recovers it.

```bash
novix --json task result 25092
# finish -> read harborResult (reward/cleanReward/image digest)
#           novix debug pull task:25092 <out> --sub project/results/r108_probe
#           independently recompute probe arithmetic from raw artifacts
# error  -> novix debug build-logs 25092, record verbatim, STOP harbor retries
```

Stop conditions unchanged: no gate skipping, no confirmation panel without
user authorisation, no v3 of the rejected D1 proposal, no turning a failed run
into a pass, no publishing sensitive material, no merge to the default branch
without the integrator.

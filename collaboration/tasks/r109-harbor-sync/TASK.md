# Task: r109-harbor-sync (scope extended by R126)

- Owner: project owner (integrator)
- Input revision/branch: initial repository creation; no predecessor commit.
  Scope extended 2026-11-14 18:1x by explicit owner instruction.
- Protocol: `collaboration/PROTOCOL.md` v1; scientific protocol in
  `collaboration/PROJECT.md`.
- Goal: maintain a public research archive so another agent can read-only
  resume the research. **Since R126 this includes the actual research outputs,
  progress records and research ideas in the open**, not only checkpoints.
- Acceptance (measurable):
  1. `AGENTS.md`, `PROTOCOL.md`, `PROJECT.md`, this `TASK.md`, `HANDOFF.md`,
     `LOG.md`, `CHECKPOINT.md` exist and agree on goal/status.
  2. `research/UPLOAD-MANIFEST.json` lists every uploaded research file with
     path, bytes and SHA-256; a `checkpoint_manifest.py` manifest verifies.
  3. Content check: **no file containing a real credential value**, no large
     model weights/datasets, no file over 50 MiB. Text-level redaction is NOT
     required (owner: "不用考虑脱敏，open 就对了"). The result is recorded.
  4. Remote branch SHA equals local HEAD (remote confirmation).
  5. No checkpoint claims a scientific result that has not been measured.
  6. Previously identified gaps are corrected with an explicit record:
     R110–R113 round coverage, and the old "no manuscript / sanitized only"
     repo description in `AGENTS.md` / `PROJECT.md`.
- Out of scope: large model weights, datasets, third-party source trees,
  compiled binaries; any file containing a real credential value; changing any
  frozen scientific protocol/threshold/split/seed; declaring paper acceptance;
  merging to the default branch without the integrator; submitting or
  publishing the manuscript.
- Dependencies: none. Harbor task 25092 is finished (engineering reward 1.0)
  and is not a dependency.
- Writers: `wb-main` → `AGENTS.md`, `collaboration/PROTOCOL.md`,
  `collaboration/PROJECT.md`, this `TASK.md`, `agents/wb-main/*`,
  `evidence/**`, `research/**`. No other agent writes these paths in this task.
- Execution: local macOS, project Conda Python. Git over HTTPS with the
  owner's authenticated `gh` CLI. No CI, no automation writes to this repo
  unless the owner authorises it.
- Change control: goal/threshold/split/baseline changes require a versioned
  record in `PROJECT.md` and a new checkpoint citing the prior value. Failed
  runs are never converted to passes by editing hashes or thresholds.
  Historical checkpoints are never rewritten; corrections are new checkpoints.
- Stop condition: the R126 archive checkpoint is published and
  remote-confirmed, or the content check finds a real credential value that
  cannot be excluded (then publish nothing and report the blocker).

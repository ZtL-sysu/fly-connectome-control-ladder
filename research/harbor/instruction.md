# R108 — Frozen CUDA/GPU environment probe (engineering only)

You run the verifier yourself with `tests/test.sh`.

## Goal

Prove that a **fixed, hash-verifiable GPU probe** executes inside the task
container and produces artifacts that can be independently re-computed from
raw outputs. This is an **engineering environment check**, not a scientific
experiment.

## Hard boundaries (EXEC LOCK)

- No training, no optimizer, no backprop, no labels, no dataset download.
- No model forward of any real network. Only a tiny deterministic CUDA tensor
  op used as a device probe.
- No editing of any frozen project script, checkpoint, or existing artifact.
- No rewriting the probe to make a failure pass. Preserve failures verbatim.
- No scientific inference, no score, no claim about visual results.

## What to do

1. Read `tests/probe.py` and verify its SHA-256 before running. Do not modify it.
2. Run `python3 tests/probe.py`; it writes `results/r108_probe/result.json`
   containing the verbatim device report, torch/CUDA versions, the probe result,
   all-finite checks, the probe script SHA-256, and a UTC timestamp.
3. Write `results/r108_probe/manifest.json` listing every produced file with
   its SHA-256.
4. Run `tests/test.sh` to let the verifier score the artifacts. The verifier
   re-computes the probe's arithmetic from raw values, checks every declared
   artifact exists with matching hashes, and writes `reward.json`.

You must name `tests/test.sh` in your final reply and state whether the
verifier passed. If anything fails, report the failure verbatim and do not
fabricate a result.

# R117 — Mainline P3 forward-pass execution premises (sanitized summary)

Status: `READONLY_EXECUTION_PREMISE_PROBE_NOT_SCIENTIFIC_RESULT_NOT_GATE_PASS_NOT_FORWARD_PASS`
Verdict (round-level, gate/evidence only): `PARTIAL | G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`

**This is a gate/evidence engineering recheck, NOT a `ccf-paper-reviewer full`
manuscript review.** It contains no scored-review Overall line, no numeric
paper score, and does not change the governing independent full review
(still 6.0).

> Sanitization: all machine-local absolute paths are written as `<local>/`.
> No credentials, tokens, account identifiers, private keys, datasets,
> model weights, third-party source trees or unpublished manuscript content
> appear in this file. Original raw bytes stay in the primary local project.

## Why this round changed direction

R114/R115/R116 exhausted the approval-free first-hand license / archive-byte
acquisition channel; R116's isolated recheck assigned the three remaining
gap-1 items to a designated gate owner. Producing a fourth evidence-acquisition
document would repeat the same loop that R105/R107/R109 already stopped three
times. The standing instruction requires returning to the mainline and,
eventually, a **P3 real forward pass to resolve U5**. R106 had asserted
"the bottleneck is gate order and G4 positioning, not missing data or compute"
based on an asset inventory plus an R101 environment check. That claim was an
**inference**: asset bytes and execution environment are different objects and
had never been frozen together by a reproducible measurement. R117 measures
the latter.

## Measurement (local Conda only, zero network requests)

Driver `<local>/miniconda3/bin/python`; child interpreters
`<local>/miniconda3/bin/python` and
`<local>/miniconda3/envs/ceg_snn_mi/bin/python`.

| Config | Interpreter | PYTHONPATH / cwd | `import flyvis` |
|:--|:--|:--|:--|
| A | base 3.14.6 | default | **FAIL** `No module named 'flyvis'` |
| B | ceg_snn_mi 3.11.15 | default | **FAIL** `No module named 'flyvis'` |
| C | ceg_snn_mi | cwd = official source tree | **FAIL** `No module named 'flyvis.version'` |
| D | ceg_snn_mi | PYTHONPATH = official source tree | **FAIL** `No module named 'flyvis.version'` |
| E | base | PYTHONPATH = official source tree | **FAIL** `No module named 'pytz'` |
| F | ceg_snn_mi | R101 sandbox + `FLYVIS_ROOT_DIR` | **OK** v1.2.0 |
| G | ceg_snn_mi | F + local deps directory | **OK** v1.2.0 |

**Finding 1 (negative).** The historical `import flyvis` result is reproducible,
but only inside a **local sandbox containing a reconstructed, non-official
file**: `flyvis/version.py` begins verbatim with
`# RECONSTRUCTED for local provisioning only -- NOT an official FlyVis file.`
The pinned official snapshot omits that file (setuptools_scm build output).
So the premise is "reconstructed local copy + explicit PYTHONPATH + explicit
FLYVIS_ROOT_DIR", not the official source tree and not the default environment.
This does **not** overturn R101/R106 readouts; it separates *asset bytes present*
from *environment ready to execute*, and the former remains confirmed.

**Finding 2 (negative, device).** The upstream FlyVis `__init__.py` contains
verbatim:
```python
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
torch.set_default_device(device)
```
All 7 configs reported `mps_available=True / cuda_available=False`; both
successful configs resolved `flyvis.device = cpu`, and `set_default_device(cpu)`
is a global side effect. Therefore a P3 forward pass running the upstream
default path would execute entirely on CPU; using MPS requires an explicit
`.to("mps")` plus an assessment of its interaction with the global default.
R101 §8.3 already named this gap but never froze a measurement. No device
migration and no forward pass were performed this round. Neither "MPS works"
nor "MPS is unavailable" is claimed; nor is any 4090 / L4 / H20 capability.

**Finding 3 (positive, asset bytes).** Official `chkpt_00000`: 49,396 B,
SHA-256 `d0e42857…ccc3f`, matches R101. `weights_only=True` restore yields
`dict{network, decoder}` with 14 tensors, all finite; no network object was
constructed. Recomputing the state-dict digest under **R101's original rule**
(sorted `key\0dtype\0shape\0raw_bytes`, no trailing `\0`) gives
`67ce06c5cec0a4cda9937b17f061db0c99ad9f76c0224874c9b3a673c2e13a82`, matching
the R101 registered value. All 8 Sintel npz files pass zip central-directory
CRC / `testzip` and their SHA-256 values match the R106 declarations 8/8.
**No array, label or stimulus value was instantiated.** Official `_meta.yaml`
verbatim clauses: `seed: 0`, `gaussian_white_noise: 0.08`, `n_frames: 19`,
`batch_size: 4`, `MultiTaskSintel`, `DecoderGAVP`, `flow: l2norm` — read only,
no calibration run.

**Framing difference, not a data conflict.** A first version of this round's
probe appended one extra `\0` after each tensor's raw bytes and obtained
`bd3f2cc8…5e74`. Recomputing under R101's rule matches exactly. Both values are
retained; the difference is framing only, analogous to the R101 independent
review's `67ce06c5` vs `297e43d7` note. It is **not** judged a data
inconsistency.

**Finding 4 (v1 false negative, preserved).** The first verifier merged nine
credential patterns with the machine-local-path pattern into one boolean and
reported `SECRET-free = MISMATCH / 17 hits`. Item-by-item recheck: all 17 were
`<local>/`-style interpreter/config paths, **zero credentials**. The final
version separates `SECRET-free` (9 patterns, 0 hits, MATCH) from
`LOCALPATH-registered` (19 hits, explicitly registered, not claimed absent).
The v1 product is preserved verbatim as `.v1-superseded.json` (11,505 B /
`5eb48011…`); final verification 9,552 B / `aa1372d2…`, 45/45 MATCH. The raw
measurement bytes were not rewritten. Public sync copies redact all local
paths to `<local>/`.

## Contract readiness (status only, no self-certification)

| Clause | Status | Note |
|:--|:--|:--|
| Frozen seed set | `NOT_ESTABLISHED_BY_THIS_PROBE` | only the official single `seed: 0` line was read |
| Noise calibration (std .08 / lower-clamp / 4 draws) | `OFFICIAL_META_LINE_PRESENT` | zero calibration runs |
| Zero-injection assertion | `NOT_MEASURED` | needs an executable runner; none invoked |
| MPS device adaptation | `MEASURED` | see Finding 2 |

All four carry `is_gate_pass=false`. Collection is not a gate pass.

## Reproducibility and independence caveat

Two scripts (`R117-probe.py`, `R117-verify.py`) produce the raw JSON, a 45-check
verification, a preserved v1, and a source manifest (19 local sources).
They share the same host, the same `hashlib` and the same source bytes, so their
agreement is a **necessary consistency check, not an independent
cross-validation** (R115 W4 / R114 D1). A fresh isolated sub-agent was
**launched** (no expected conclusion supplied) to perform the genuine
independent recomputation. **At the time this summary is written that recheck
has not yet been recovered; no verdict, score or review outcome is claimed
here.** When recovered, its report is left unedited and any corrections are
registered append-only.

## Strict boundary

EXEC LOCK: zero forward pass, inference, training, label read, dataset array
instantiation, EPE/l2 computation, scientific metric or gate promotion. Main
`pipeline-state.json` unchanged (`bcb48bb9…`, 3,723 B, identical to the R107
frozen value); G0–G8 / validation / handoff all `pending`, **G0 stays pending**.
No historical byte, review, score, threshold, manuscript, gate, frozen artifact,
matrix, criterion register or gate configuration was modified. No
`ccf-paper-reviewer full` was launched, no scored-review Overall line produced,
no governing self-assessment, no gate skipping, no repeat review of an unchanged
manuscript. D1/v3 not reopened, no predictor v4, no assumption of the
`<=32h / K=45` confirmation authorisation. No 4090 capability claim. Primary
project: no submission / commit / push. Heartbeat ACTIVE schedule unchanged.

Read-only double gate: validator `NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`
(D1 pass, D2/D3/D5 fail, D4 pass, `score_meets_threshold=false`); guard
`INCOMPLETE / EXIT=1` (A2, A6 FAIL; S1–S7 all pending). Guard ledger SHA-16
`73043b4e164a5a5f` and mtime, and main `pipeline-state.json` SHA-16
`bcb48bb964e657a4`, identical before/after => zero write-back. Both reports
written to temporary paths outside the project tree. The A6 dual-wording
(criteria `>=7.0` / ledger `>8.0`) is a known registered issue, read-only this
round.

## Result and handoff

The step-3 precondition (substantive positive new scientific evidence) is not
met, so no new manuscript copy, no 9-page compilation, no fresh isolated full
review. **0 qualifying papers, no COMPLETE written**, governing still
**R95 = 6.0 / Confidence 4.0**, `NOT_QUALIFIED` / `INCOMPLETE`. Stop gates
remain (1) achieve >= 7.0, (2) user stops.

Handoff: (1) machine-gate fixes still need user / gate-owner approval
(R111 five-point decision package unanswered); (2) the three P3 premises
exposed here — acceptability/traceability of the reconstructed non-official
`version.py`, explicit MPS adaptation vs global `set_default_device(cpu)`, and
an executable frozen-seed/noise/zero-injection runner — must be frozen into a
versioned execution contract by a designated gate owner; the heartbeat does
not self-certify and does not start P3 while G0 is pending; (3) gap-1's three
remaining items keep R116's gate-owner judgement; (4) ordered G0–G8 (G4
addressing Kuklev v2 §7.3/§8/§9) → validation → handoff → P0 → P1A/P1B → P2
→ P3 real forward; (5) only with `failed_runs=0`, all finite, independent
recomputation agreement and substantive positive evidence may a new manuscript
copy → 9-page compile → fresh isolated full review proceed; **X >= 7.0** plus
QUALIFIED + COMPLETE is required before writing COMPLETE.

**Checkpoint status `completed` is a collaboration work state, not a scientific
conclusion.**

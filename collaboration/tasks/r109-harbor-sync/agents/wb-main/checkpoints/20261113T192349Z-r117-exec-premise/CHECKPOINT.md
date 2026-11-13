# Checkpoint: 20261113T192349Z-r117-exec-premise

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: this round's read-only measurement and
  bookkeeping finished; the fresh isolated recheck was launched but is **still
  running** at write time and is NOT claimed complete; **NOT** a scientific
  result, **NOT** a paper-acceptance claim, **NOT** a gate pass)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Cites: `20261113T121816Z-r109-init`, `20261113T130720Z-r108-build`,
  `20261113T140607Z-r108-final`, `20261113T144313Z-r114-g0-license`,
  `20261113T161442Z-r115-g0-remaining`, `20261113T180130Z-r116-archive-content`

## Changes and actual commands

R117 heartbeat, awakened 2026-11-14 03:09 +0800. Concurrency guard checked
first: primary `goal-ledger.md` mtime `2026-11-14 02:07:07` (62.5 min stale,
>10 min); zero project writes in the preceding 15 min; no independent main
session or polling process; no new file in `ccfa-review-reports/` or
`ccfa-idea-review-reports/` (latest full review still r95 = 6.0); no R117
artifacts. Governing therefore stays **6.0**.

**Direction change (RGE4).** R114/R115/R116 exhausted the approval-free
first-hand license / archive-byte channel, and R116's isolated recheck assigned
the three remaining gap-1 items to a designated gate owner. R111's five-point
decision package is still unanswered, and R105/R107/R109 already stopped the
"produce another evidence document" loop three times. The standing instruction
requires returning to the mainline and, eventually, a **P3 real forward pass to
resolve U5**. R106 had inferred "the bottleneck is gate order and G4
positioning, not missing data or compute" from an asset inventory; asset bytes
and the **execution environment** had never been frozen together by a
reproducible measurement. R117 measures the latter, with real local commands
rather than another text patch.

Commands actually run (local Conda only, **zero network requests this round**):

```bash
<local>/miniconda3/bin/python R117-probe.py          # 7 subprocess configs
<local>/miniconda3/bin/python R117-verify.py         # 45 checks, v1 preserved
# child interpreter for torch/checkpoint work:
<local>/miniconda3/envs/ceg_snn_mi/bin/python -c '... torch.load(weights_only=True) ...'
<local>/miniconda3/bin/python readonly-validator/validate_single_paper.py --out /tmp/r117_validator.md
<local>/miniconda3/bin/python .../guard_engine.py check -l guard/ledger-null-ladder.json -o /tmp/r117_guard_report.md --no-report
```

No model forward pass, inference, training, label read, dataset array
instantiation, EPE/l2 computation, scientific metric, or gate promotion. Sintel
npz files were inspected only through the zip central directory (entry names,
CRC, uncompressed sizes, `testzip`); no array or stimulus value was read.

## Checks and results

| Check | Result |
|:--|:--|
| Import matrix (7 independent child interpreters) | **5 FAIL / 2 OK**. Default base (3.14.6), default ceg_snn_mi (3.11.15), official source-tree cwd, PYTHONPATH=official source tree all FAIL (`flyvis` / `flyvis.version` / `pytz` missing). Only the R101 sandbox + explicit `PYTHONPATH` + explicit `FLYVIS_ROOT_DIR` imports OK (v1.2.0). |
| Reconstructed non-official file | `flyvis/version.py` in the sandbox begins verbatim `# RECONSTRUCTED for local provisioning only -- NOT an official FlyVis file.`; the pinned official snapshot omits it. Historical R101/R106 readouts are **reproducible but not portable**; asset bytes present != environment ready. |
| Device premise | All 7 configs `mps_available=True / cuda_available=False`; both OK configs `flyvis.device = cpu`. Upstream verbatim `cuda if available else cpu` + global `torch.set_default_device(device)` => a default-path P3 forward would run entirely on CPU; MPS needs an explicit `.to("mps")`. No device migration or forward was performed; **no 4090 / L4 / H20 capability claim**. |
| Official checkpoint | 49,396 B / `d0e42857…ccc3f` matches R101; `weights_only=True` -> `dict{network, decoder}`, 14 tensors, all finite; no network object constructed. |
| State-dict digest under **R101's original rule** | `67ce06c5cec0a4cda9937b17f061db0c99ad9f76c0224874c9b3a673c2e13a82` **MATCH**. A first probe variant (`bd3f2cc8…5e74`) differed only because it appended one extra `\0` per tensor; recomputed under the original rule it matches exactly. **Framing difference, not a data conflict**; both values retained. |
| 8 Sintel npz | zip CRC / `testzip` 8/8 OK, SHA-256 matches R106 declarations 8/8; zero array instantiation. |
| Official `_meta.yaml` verbatim clauses | `seed: 0`, `gaussian_white_noise: 0.08`, `n_frames: 19`, `batch_size: 4`, `MultiTaskSintel`, `DecoderGAVP`, `flow: l2norm` — read only, zero calibration runs. |
| Frozen-contract readiness | seed set `NOT_ESTABLISHED_BY_THIS_PROBE`; noise calibration `OFFICIAL_META_LINE_PRESENT` (zero runs); zero-injection assertion `NOT_MEASURED`; MPS adaptation `MEASURED`. All four `is_gate_pass=false`. |
| v1 verifier false negative | First verification merged 9 credential patterns with the machine-local-path pattern and reported `SECRET-free=MISMATCH / 17 hits`; item-by-item recheck: all 17 were `/Users/<user>/` interpreter/config paths, **zero credentials**. Final version separates `SECRET-free` (0 hits, MATCH) from `LOCALPATH-registered` (19 hits, explicitly registered, not claimed absent). v1 preserved verbatim (11,505 B / `5eb48011…`); final 9,552 B / `aa1372d2…`, **45/45 MATCH**. Raw bytes not rewritten. |
| Read-only double gate | validator `EXIT=1 / NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`, `score_meets_threshold=false` (D1 pass, D2/D3/D5 fail, D4 pass); guard `EXIT=1 / INCOMPLETE` (A2, A6 FAIL; S1–S7 all pending). Guard ledger SHA-16 `73043b4e164a5a5f` + mtime and main `pipeline-state.json` `bcb48bb9…` / 3,723 B identical before/after => **zero write-back**. A6 dual-wording (criteria `>=7.0` / ledger `>8.0`) is a known registered issue, read-only this round. |
| Content safety (public repo) | 33-file full-repo scan: 10 strict patterns **0 hits** (API keys, tokens, private keys, emails, Bearer headers, machine-local absolute paths, credential-file names); max file 16,744 B; **0 files > 50 MiB**; no dataset/weight/binary/third-party-source/unpublished-manuscript files. Local paths in the primary project's own artifacts are configuration facts and were redacted to `<local>/` in every public copy. |

Primary local artifacts (not in this public repo):
`exec-premise-R117/R117-probe.py`, `R117-EXEC-PREMISE-RAW.json`
(18,455 B / `891a950b…`), `R117-verify.py`,
`R117-EXEC-PREMISE-VERIFICATION.json`, `…v1-superseded.json`,
`R117-SOURCE-MANIFEST.json` (7,765 B / `b113ed99…`, 19 sources, all present,
valid UTC, `network_requests_this_round=0`),
`R117-EXEC-PREMISE-EVIDENCE.md`, `R117-ROUND-AUDIT.md`.

The two scripts share host, hash function and source bytes: their agreement is
a necessary consistency check, **not an independent cross-validation**. A
fresh isolated sub-agent was **launched** to perform the genuine independent
recomputation, with no expected conclusion supplied. **At the time this
checkpoint is written, that recheck has not yet been recovered; no verdict,
score, or review outcome is claimed here.** When it completes, its report is
left unedited and any corrections are registered append-only (a new checkpoint
if needed). This checkpoint therefore records only the measurement itself, the
read-only double gate, and the strict boundary.

## Limitations

- **No scientific result.** EXEC LOCK throughout. No forward pass, no training,
  no labels, no dataset values, no EPE/l2, no competence measurement.
- **No gate passed.** G0 stays `pending`; G0–G8 / validation / handoff all
  `pending`. Zero state write-back, zero self-certification.
- **Not a manuscript full review.** No `ccf-paper-reviewer full` was launched,
  no scored-review Overall line produced, no numeric paper score, no change to
  governing. Step-3 precondition (substantive positive new scientific evidence)
  not met => no new manuscript copy, no 9-page compile, no fresh isolated full
  review.
- **Three P3 premises exposed and NOT resolved here** (need a designated gate
  owner to freeze a versioned execution contract): acceptability/traceability
  of the reconstructed non-official `version.py`; explicit MPS adaptation vs
  the global `set_default_device(cpu)`; an executable frozen-seed / noise /
  zero-injection runner. The heartbeat does not start P3 while G0 is pending.
- Primary repository: no submission / commit / push. Heartbeat ACTIVE schedule
  unchanged. Private `ZtL-sysu/novix-platform` untouched.

## Result

**0 qualifying papers, no COMPLETE written.** Governing stays
**R95 = 6.0 / Confidence 4.0**, `NOT_QUALIFIED` / `INCOMPLETE`. Stop gates
remain (1) achieve >= 7.0, (2) user stops.

## Next

(1) Machine-gate fixes still need user / gate-owner approval (R111 five-point
decision package unanswered). (2) Freeze the three P3 premises above into a
versioned execution contract by a designated gate owner; no self-certification,
no P3 start while G0 pending. (3) gap-1's three remaining items keep R116's
gate-owner judgement. (4) Ordered G0–G8 (G4 addressing Kuklev v2 §7.3/§8/§9)
-> validation -> handoff -> P0 -> P1A/P1B -> P2 -> P3 real forward. (5) Only
with `failed_runs=0`, all finite, independent recomputation agreement and
substantive positive evidence may a new manuscript copy -> 9-page compile ->
fresh isolated full review proceed; **X >= 7.0** plus QUALIFIED + COMPLETE is
required before writing COMPLETE.

**Checkpoint status `completed` is a collaboration work state, not a scientific
conclusion.**

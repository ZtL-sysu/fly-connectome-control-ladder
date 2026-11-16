# Research archive — full-open upload (R126, 2026-11-14)

Per the project owner's instruction, this directory now holds **actual research
outputs, progress records and research ideas**, not just sanitized summaries.
Previous checkpoints (`evidence/`) remain untouched and are still valid.

Upload is by an explicit whitelist recorded in `UPLOAD-MANIFEST.json` (path,
size, SHA-256 for every file). No recursive `git add .`. Excluded by policy:
large model weights and datasets (owner: "不用传"), any file over 50 MiB, and
**files containing a real credential value**. Scan-pattern *literals* inside
verifier scripts (e.g. `b"ghp_"`) are not secrets and are included. No text was
rewritten or redacted: the owner said "不用考虑脱敏，open 就对了".

## What is here

| Directory | Contents | Count |
|:--|:--|--:|
| `manuscript/` | Main manuscript TeX + PDF across versions: `revision-r97` (the version reviewed as R95), the v2-R51 run, and the `r93-candidate` TeX. Unpublished, double-blind. | 5 |
| `results/` | Real experiment metrics: the 10-seed main matrix (`metrics.json`, `metrics_completed.json`), independent-family metrics, i1 null-ladder runs, R63 density/robust replays, R78 control-ladder replay, `qualified_paper.json`. | 10 |
| `reviews/` | **All 23** independent / full / idea review reports, full text, including the historical 7.5 (R47/R49) and the governing 6.0 (R95). | 23 |
| `guidance/` | `guidance-v2.md` (v2-R51 contract), execution contracts v1–v3, `GOAL-ITERATION-R107.md`, G0 evidence/recency reviews, generated-directions index. | 8 |
| `protocol/` | The frozen Candidate-E protocol packet: claim-evidence matrix, competence-baseline spec, prediction dataflow, paired-edge-set spec, design reviews, prospective identities, prior-art map, etc. | 30 |
| `ideas/` | Research thinking: discriminative-prediction proposal v1/v2, both independent reviews, the D1 block decision, G4 positioning, literature-baseline matrix, dataset-access log, hardware profile. | 10 |
| `ledger/` | `goal-ledger.md` (the full round-by-round ledger), `STATUS.md`, and all daily work logs 2026-11-10 … 11-14. | 10 |
| `rounds/` | R106–R125 round audits, independent rechecks, post-review corrections, verifiers, source manifests, verification JSON, guard/validator readouts. | 129 |
| `harbor/` | Harbor task package, the full three-attempt trial log, final independent verification, and the Novix route-diagnosis matrix. | 8 |

`UPLOAD-MANIFEST.json` is the authoritative per-file index (233 files, ~8.6 MiB).

## Honest status (do not infer success from upload)

- Governing independent full review remains **R95 = 6.0 / Confidence 4.0**.
- Validator `NOT_QUALIFIED` (acceptance is `Overall >= 7.0` after the R107
  user-authorised goal iteration); guard `INCOMPLETE`.
- **0 qualifying papers, no COMPLETE.** G0–G8 and all f-research-v1 P stages
  are still pending; no gate was passed by uploading.
- The 7.5 reports in `reviews/` are **historical**; "latest independent full
  review governs" is unchanged, so they do not qualify the paper.
- Uploading a manuscript does not constitute submission or publication.

## Later additive records

These records are additive and do not replace the R126 manifest or the governing R95 status.

- `manuscript/cvpr2027-rebuild-20261116/` records the 2026-11-16 CIFAR revision of *Task Information Audits for Connectome Graph Interventions*, with its analysis files and four independent reviews. Its latest review is Overall 5. It does **not** replace R95 = 6.0, and it does not qualify the manuscript.
- `reviews/cvpr2027-rebuild-independent-20261116-cifar.md` is the same latest CIFAR review, copied at the reviews index for direct lookup.
- `collaboration/tasks/cvpr2027-score-lift-20261116/` contains this sync's task record, handoff, and SHA-256 manifest.

## Deliberately absent

Large model weights, official checkpoints, Sintel-derived development data,
third-party source trees, compiled binaries, and files over 50 MiB. Their
locations, sizes and hashes are recorded in the primary project; this archive
is a research/content record, not a full reproduction bundle. A new agent can
read the science and the decisions here, but must request the data separately
to reproduce experiments.

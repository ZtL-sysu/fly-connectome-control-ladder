# CHECKPOINT — 20261114T060001Z-r123-post-review

- Task / agent / branch: `r109-harbor-sync` / `wb-main` / `agent/r109-harbor-sync/wb-main`
- Status: `completed` (work-state label, NOT scientific validation)
- Round: R123 heartbeat, independent recheck recovered 2026-11-14 13:57 +0800
- Created (UTC): 2026-11-14T06:00:01Z
- Input HEAD at manifest creation: see `manifest.json` (`input_git_head`)
- Immutable: the eighteenth checkpoint's bytes are **not rewritten**.

## Why this checkpoint exists

The **eighteenth** checkpoint (`20261114T054515Z-r123-gap1-licence`) was written while the
fresh isolated sub-agent was running and truthfully stated "recheck launched, not recovered,
no verdict claimed". Following the R117/R119/R120/R121/R122 precedent, the recovered verdict
and any append-only corrections are published in this **new immutable checkpoint** instead of
editing the earlier one.

## Recovered independent recheck

Fresh isolated sub-agent (`general-purpose-1`), **no expected verdict / score anchor /
conclusion anchor supplied**. Final report in the primary project (NOT uploaded, per R117):
**16,565 B / 105 lines / SHA-256
`40edc181845f5d5086e7ee3dc71c6515861d2061c41be8d688301f45cb744408`**, one write, mtime
13:57, original unchanged. Verdict `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO |
Scientific result claimed: NO | Forward pass performed: NO`.

**A–F 6 MATCH / 0 MISMATCH**; **12 named overclaim categories CONFIRMED 0 / REFUTED 12**;
**HIGH 0 / MEDIUM 1 / LOW 1** (2 defects), fabrication 0. Reviewer recomputed from the 13 raw
byte files with its own logic only, used no round-produced JSON as a data source, read the
round audit LAST, ran no verifier script / git / network, and modified no existing file.
Report contains 0 credential values, 0 scored verdict lines, 0 expected-score anchors.

## Two defects, both accepted append-only

- **W-1 [MEDIUM | fact error / data inconsistency, NOT fabrication]**: round audit section 3
  wrote the six Zenodo files as `152,578` bytes; byte-exact recount is **152,628** (50-byte
  difference). Main-session recount: 10,603 + 131,225 + 4,061 + 2,615 + 2,267 + 1,857 =
  152,628; four-group total 262,728, matching the heading, the manifest `total_bytes=262728`,
  and the reviewer's A-group recount. Impact is scoped to **one derived summary number**; it
  does not propagate to raw bytes, SHA-256, either verifier reading, machine gates, gate
  state, governing, A–F, or the 12 overclaim rulings. Per append-only discipline neither the
  round audit nor the eighteenth checkpoint is rewritten.
- **W-2 [LOW | scope not delimited]**: "zero local paths" was not explicitly limited to the
  **13 raw frozen files**. Those 13 files do have 0 hits (A/F unaffected), but two
  same-directory guard-output files and the independent report contain local absolute-path
  literals. Not a factual misstatement; corrected wording limits the claim to the 13 raw
  files and states that guard outputs and the independent report are local-only, not
  uploaded. The 6-file public upload set has 0 local-absolute-path hits.

Pre-existing V-1 (verifier expected 20 MANIFEST rows, true 18; v1 86/87, v2 91/91, both
retained) was independently confirmed as correctly classified and is not a new defect.

## Uploaded in this checkpoint

Only a **sanitized** summary (`evidence/R123-INDEPENDENT-REVIEW-SANITIZED.md`), plus this
CHECKPOINT.md, `manifest.json`, and `metrics.csv`. The independent report's original text
contains local absolute-path literals and is **not uploaded**; the 13 raw third-party files,
primary-project reports, scripts, JSON and guard outputs are likewise not uploaded.

## Unchanged / boundary

13 raw bytes and SHA-256 values, `artifact_count=13 / total_bytes=262728`, v2 91/91 MATCH,
A–F 6/6, 12 overclaim categories 0 CONFIRMED, validator `NOT_QUALIFIED` (6.0 / `>=7.0`),
guard `INCOMPLETE`, G0 and G0–G8 all pending, zero gate promotion / zero self-certification /
zero state write-back, zero forward pass / zero scientific result, governing R95,
**0 qualifying papers, no COMPLETE**, heartbeat schedule unchanged. This is a gate /
evidence-layer recheck, **not** a `ccf-paper-reviewer full` manuscript review; no
`**Overall:**` numeric line was produced. Primary project: no submission / commit / push.
The eighteenth checkpoint's write-time statement ("launched, not recovered, no verdict
claimed") was true and its bytes are not rewritten; all 17 earlier checkpoints are unchanged.

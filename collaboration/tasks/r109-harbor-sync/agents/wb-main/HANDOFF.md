# HANDOFF — wb-main / r109-harbor-sync

- Task / agent / branch: `r109-harbor-sync` / `wb-main` /
  `agent/r109-harbor-sync/wb-main`
- Status: **in_progress** (6 checkpoints published; harbor trial closed, research itself unfinished)
- Last update: 2026-11-14 02:0x +0800 (R116 heartbeat, awakened 2026-11-14 01:27)
- Protocol: `collaboration/PROTOCOL.md` v1; `collaboration/PROJECT.md`
- Repo: `ZtL-sysu/fly-connectome-control-ladder` (public)

## Completed

- Public repo created with a sanitized collaboration layer only.
- R107 goal iteration recorded: independent full-review acceptance changed from
  strictly > 8.0 to **>= 7.0** (equal qualifies). Machine validators synced.
  Historical 7.5 reports are NOT promoted to governing.
- R108 harbor-trial evidence sanitized and published: the package, the trial
  log, a redacted route-diagnosis JSON with 7 dispatch rows, and the goal
  iteration record.
- R114 G0 gap-1 first-hand license verification: sanitized summary published
  (`evidence/R114-G0-R1-LICENSE-EVIDENCE.md`). Two previously OPEN items
  **advanced to recomputable first-hand attachments but remain PARTIAL**:
  Zenodo 21549559 license identifier `cc-by-4.0` (one Zenodo metadata source
  exposed through three same-source views, NOT independent cross-checks), and
  the MPI Sintel official non-commercial license page. **Gap 1 overall is
  still PARTIAL; no gate was passed.** A fresh isolated recheck returned
  `PARTIAL | G0 may be passed: NO` and identified overclaims (withdrawn by
  appending a correction register). Raw bytes and hashes stay in the primary
  project and are not uploaded.
- R115 G0 gap-1 remaining first-hand evidence acquisition: sanitized summary
  published (`evidence/R115-G0-R1-REMAINING-EVIDENCE.md`). Three items from
  R114's handoff were advanced with first-hand bytes, **none promoted to CLOSED**:
  (1) Correig-Fraga archive **content bytes** — all 6 Zenodo routes returned
  HTTP 403 at this timepoint (explicit negative evidence; R107 403 / R114 200 /
  R115 403 are separate timepoint observations, no history rewritten) ⇒ OPEN;
  (2) pretrained-checkpoint **hosting located** — official upstream bytes show
  the weights come from a Google Drive public folder, not the GitHub code repo,
  with two published SHA-256 checksums ⇒ hosting PARTIAL, **distribution terms
  still OPEN** (a script constant is not a LICENSE text; code MIT is not
  extrapolated to weights); (3) "natural clips" **identity confirmed** —
  official source verbatim shows they are MPI Sintel-derived `AugmentedSintel`
  stimuli, not a separate asset ⇒ identity PARTIAL, independent license still
  OPEN. A credential-bearing official script was deleted before persistence;
  its value was never printed, copied, recorded or uploaded. **Gap 1 overall
  remains PARTIAL; G0 stays `pending`; no gate passed.**
- R115 fresh isolated recheck recovered: `PARTIAL | G0 may be passed: NO |
  Scientific result claimed: NO`, final **24,958 B** / SHA-256
  `5758007a…62e0` (an earlier 22,396 B / `ef2b0e21…d55b3` reading was an
  intermediate state; both retained in the primary project, final bytes
  govern). It independently confirmed 10/10 SHA and 10/10 verbatim fields, 0
  credential hits in this round's directory, and an unchanged pipeline state;
  it found **no instance** of the ten named overclaim categories. Six
  boundary/precision issues (W1–W6) were recorded as append-only corrections:
  W1 and W4 withdrawn, W2/W3/W5/W6 narrowed. In particular the weight-hosting
  constants came from a **local frozen copy outside this round's collected
  bytes**, not from official upstream bytes fetched this round; and the UTC
  field is write-time, not a recomputable fetch time (the final review does
  NOT judge the time difference a factual contradiction). Unpublished files
  were corrected before this publication. The recheck is not an authorisation
  and does not replace an R9 independent review.
- R116 G0 gap-1 archive-content bytes **first obtained** (sanitized summary
  `evidence/R116-G0-R1-ARCHIVE-CONTENT.md`). R115's handoff item 2 named this
  approval-free action and its channel recovered: 8 small archive content files
  (incl. `README.md` / `MANIFEST.csv` / `SHA256SUMS`) returned HTTP 200 and
  **byte-match the upstream official md5 8/8**, with zero MISMATCH; size 8/8;
  disk <-> manifest <-> verification SHA/MD5/bytes 8/8. Channel stayed mixed:
  a first batch of 10 custom-UA requests all returned throttling 403 (8 pages
  saved verbatim, 8 distinct md5), while single sequential requests returned
  200. 8/20 files / 16,519 B = **0.0028% of archive bytes** obtained; the
  remaining 12 files (6 compressed tables + 6 CSV, ~591 MB) were deliberately
  not downloaded under the exclusion list and are **not verified**. v1 of the
  verification script falsely counted structurally absent checksum rows as
  failures; v1 is preserved verbatim and v2 uses a three-state rule. A fresh
  isolated recheck: `PARTIAL | G0 may be passed: NO | Scientific result
  claimed: NO`, final **31,188 B** / SHA-256 `2e348521…b75c2`, ten named
  overclaim categories **CONFIRMED = 0**, two NARROW issues (`CLOSED (partial)`
  -> PARTIAL; "7 + 5" -> "6 compressed + 6 CSV") plus six LOW wording issues
  accepted by append-only correction. **gap 1 overall PARTIAL, G0 pending,
  no gate passed, no state write-back.**
- Content scan performed each sync: no credentials / local absolute paths /
  dataset binaries / files >50 MiB in the upload set.

## NOT completed / do not assume

- **Harbor trial finished with a verified engineering reward (1.0).**
  CUDA execution on **NVIDIA H20**, independent recomputation passed, frozen
  probe SHA matched. **Still no scientific result and no 4090 claim.** See
  checkpoints `20261113T130720Z-r108-build` and `20261113T140607Z-r108-final`.
- Two earlier harbor attempts failed (25075 COPY-context error; 25076
  platform 1800 s image-build timeout). Both retained verbatim in the primary
  project; 25092 is the declared last build-stage attempt.
- Governing independent full review remains **6.0**, validator
  `NOT_QUALIFIED`, guard `INCOMPLETE`, 0 qualifying papers, no COMPLETE.
- Confirmation panel (<=32 h / K=45) is **not authorised**; an explicit user
  decision is still pending.
- G0–G8 and all f-research-v1 P stages remain pending.

## Trustworthy files here

`AGENTS.md`, `collaboration/PROTOCOL.md`, `collaboration/PROJECT.md`,
`tasks/r109-harbor-sync/TASK.md`, this HANDOFF, `LOG.md`,
`checkpoints/<UTC-id>/CHECKPOINT.md` and its `manifest.json`,
`evidence/**` (small, sanitized, hash-listed).

## Known gaps

The primary evidence (datasets, checkpoints, full reviews, full ledger,
manuscript) is **not** in this repo. `PROJECT.md` and `AGENTS.md` state why.
A new agent cannot reproduce experiments from this repo alone; it can read the
protocol and know exactly which local artifacts to request.

## Running jobs (verified 2026-11-13 22:4x +0800)

| Job | Provider | State | Recovery |
|:--|:--|:--|:--|
| 25092 | Novix harbor | **FINISH**, `reward=1.0`, `measurementValid=true`, 169 steps, device **H20** (not 4090), no scientific result | trial closed; optional `novix debug pull task:25092 <out> --sub project/results/r108_probe` after track-ops recovers |
| heartbeat | local automation | ACTIVE, every 30 min | reads the primary project's `goal-ledger.md` |
| R114 isolated review | local isolated sub-agent | **RECOVERED** `PARTIAL \| G0 may be passed: NO \| Scientific result claimed: NO`; final 26,104 B, SHA-256 `879ecb78…3e`. Found 7 flaws; two substantive overclaims (same-source views called independent sources; license identifier called LICENSE text CLOSED) withdrawn by appended correction register. | primary project `gate-G0-R114/R114-G0-R1-INDEPENDENT-REVIEW.md` + `R114-POST-REVIEW-CORRECTION.md` |
| R116 isolated review | local isolated sub-agent | **RECOVERED** `PARTIAL \| G0 may be passed: NO \| Scientific result claimed: NO`; final 31,188 B, SHA-256 `2e348521…b75c2`, original text unchanged. Ten named overclaim categories CONFIRMED = 0; two NARROW + six LOW wording issues accepted by append-only correction. Gate/evidence recheck, not a manuscript full review. | `evidence/R116-G0-R1-ARCHIVE-CONTENT.md`, primary project `gate-G0-R116/R116-G0-R1-INDEPENDENT-REVIEW.md` + `R116-POST-REVIEW-CORRECTION.md` |

Do not claim any of these produced a scientific result. A gate-evidence
recheck is not a `ccf-paper-reviewer full` manuscript review and must not
produce an Overall score line.

## Next executable command (for a resuming agent)

```bash
# Harbor trial is closed. Resume the ordered research gates instead.
# If workspace files are needed later (track-ops was unreachable):
novix debug pull task:25092 <out> --sub project/results/r108_probe
# then re-verify file hashes against the trajectory raw values.
```

Stop conditions: do not skip gates, do not open the confirmation panel without
user authorisation, do not reissue a v3 of the rejected D1 proposal, do not
turn a failed run into a pass, do not publish sensitive material.

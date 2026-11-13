# R116 · G0 gap-1: Zenodo 21549559 archive-content bytes obtained and byte-compared

> Sanitized collaboration summary. All paths are `<local>/`-style or omitted.
> This is **first-hand evidence acquisition**, not a gate pass, not a
> scientific result, not a manuscript review. Status `completed` on the
> checkpoint is a work state only.

## Why this round

R115's handoff item 2 named a specific, approval-free action: *if the Zenodo
channel recovers, fetch `README.md` / `MANIFEST.csv` / `SHA256SUMS` content
bytes and byte-compare them with the official md5*. R115 had 6/6 routes return
HTTP 403 (anti-crawler throttling), so archive-content bytes were OPEN.
At the R116 wake-up (2026-11-14 01:27 +0800) the channel was reachable again.

All machine-gate / acceptance-gate fixes remain **unexecuted** because they
require explicit user / designated gate-owner approval (R111 decision package,
still unanswered). No G0 text patch, no probe / guard v2, no state write-back.

## Concurrency guard

Primary ledger mtime `2026-11-14 00:25:08`, 62.6 min before wake-up (>10 min).
Zero project writes in the preceding 15 min; no independent main session or
polling process; no new file in either review-report directory; no R116
artifacts. Governing independent full review therefore unchanged at **6.0**.

## Channel: mixed within one round (timepoint discipline)

| Round | Time | Record-level API | Archive content bytes |
|:--|:--|:--|:--|
| R107 | 11-13 05:4x | 403 | 403 |
| R114 | 11-13 22:3x | **200** | not requested (metadata/license only) |
| R115 | 11-13 23:5x | 403 | **6 routes all 403 (throttling)** |
| **R116** | **11-14 01:3x** | **200** | **8 content files 200 + 8 throttling 403 pages** |

These are observations at their own timepoints; no historical bytes were
rewritten, deleted, redated or promoted. In R116, the first batch of 10
requests with a custom UA all returned 403; subsequent single sequential
requests without a custom UA returned 200 for 8/8 content files. This is an
engineering observation, **not a causal claim about the platform**.

The 8 saved 403 pages each contain verbatim
`Access to this resource has been restricted due to unusual traffic from your network.`
=> anti-crawler / traffic throttling, **not** a content-level authorization
refusal. All 8 pages have distinct byte strings (8 distinct md5). They are
named `*.403.html` so a throttling page can never be mistaken for content.

## Saved raw bytes

18 files: 10 x HTTP 200 (2 API metadata containers + **8 archive content
files**) + 8 x `*.403.html` throttling pages.

8 content files: `README.md`, `MANIFEST.csv`, `SHA256SUMS`,
`DATA_DICTIONARY.md`, `software_versions.csv`,
`source_data_figure_3_task_accuracy.csv`,
`source_data_figure_3d_transfer.csv`, `source_data_figure_3f_weber.csv`.

## Byte-level comparison (recomputed independently from disk)

| Source | Nature | Result |
|:--|:--|:--|
| (a) Zenodo files-list API checksum `md5:...` | **upstream official** | **8/8 MATCH** |
| (b) in-archive `MANIFEST.csv` sha256 column | in-archive self-statement | 6 MATCH + 2 structurally absent |
| (c) in-archive `SHA256SUMS` | in-archive self-statement, **same source as (b)** in another encoding, NOT independent cross-validation (R114 D1) | 7 MATCH + 1 structurally absent |
| size | upstream API `size` | **8/8 MATCH** |

- `mismatches = []`, `all_available_sources_match_and_size_match = True`.
- The `STRUCTURALLY_ABSENT` cells are **checksum tables not self-referencing**:
  `MANIFEST.csv` has no row for itself nor for `SHA256SUMS`; `SHA256SUMS` has
  no row for itself (it does list `MANIFEST.csv`). Verified verbatim from the
  saved bytes. A missing row is not a mismatch.
- Disk bytes <-> `SOURCE-MANIFEST.json` <-> `VERIFICATION.json` SHA-256 / MD5 /
  bytes **8/8 identical** for the 8 content files. The verification script does
  not read the manifest product.
- Archive total: **20 files / 591,418,589 B**. Obtained: **8 files / 16,519 B
  = 0.0028% of bytes**.
- 6 verbatim README strings, program-extracted: **6/6 FOUND**, including
  `The record is released under CC BY 4.0.` (a **record-level self-statement**),
  `The raw FlyWire synapse release is not duplicated.`,
  `proofread_connections_783.feather`, and `sha256sum --check SHA256SUMS`.
- Credential / token / private key / bearer / **local absolute path** / email
  scan over all 18 saved bytes: **0 hits** (6 strict pattern classes; the
  isolated recheck used 10 broader classes, still 0).

## v1 false negative, preserved

The first verification script counted a structurally absent checksum row as a
failure, producing a spurious `all_pass=False`. This was a **script judgment
defect**, not a data inconsistency. The v1 output is preserved verbatim as
`R116-G0-R1-VERIFICATION.v1-superseded.json` (9,413 B, SHA-256
`756fd2b1…`). v2 uses a three-state `MATCH / MISMATCH / STRUCTURALLY_ABSENT`
rule and passes. Both readings are retained; neither historical byte is
rewritten.

## Not downloaded (R109 exclusion list)

12 files deliberately not fetched: **6 compressed tables**
(5 x `connections_*.csv.gz` + 1 x `neuron_annotations_*.tsv.gz`,
587,260,790 B) and **6 plain CSV** (5 x `predictions_numerical_*.csv` +
1 x `right_visual_positions_all_neurons.csv`, 4,141,280 B). Their content
bytes are **not obtained and not verified**; only their metadata sizes/checksums
are retained. Reason: the exclusion list (large Sintel-derived / big dataset
files) plus throttling risk. The earlier "7 + 5" split in the primary report
was corrected by append-only register to "6 + 6" after independent recheck.

## Fresh isolated recheck (recovered before publication)

A fresh isolated sub-agent, with **no expected conclusion supplied**, wrote
`R116-G0-R1-INDEPENDENT-REVIEW.md`: final **31,188 B**, SHA-256
`2e348521889a549968ce0d6b0e1f6a77a947d44b8b6d7d36322962632a5b75c2`,
verbatim first lines
`**Verdict:** PARTIAL | **G0 may be passed:** NO` and
`**Scientific result claimed:** NO`. Original text unchanged.

It independently recomputed the three-way hashes (zero MISMATCH), the
structural absences, the v1 false negative and its preservation, the 8
throttling pages, the 6 verbatim strings, the content-safety scan and file
integrity — all matched. **Ten named overclaim / self-certification categories
(a)–(j): CONFIRMED = 0 (all REFUTED); WITHDRAW = none.** Two NARROW issues:
`CLOSED (partial)` should be **PARTIAL** (8/20 files, 0.0028% of bytes), and
the "7 + 5" not-downloaded split should be "6 compressed + 6 CSV". Six LOW
wording/precision issues were also registered. All corrections are
**append-only** in the primary project; the published independent review is
untouched; previously published checkpoints are untouched.

Independent state re-judgment: archive-content bytes **PARTIAL**, full-archive
verification **OPEN**, checkpoint-weight distribution terms **OPEN**,
natural-clips stand-alone license **OPEN**, gap 1 overall **PARTIAL**,
**G0 PENDING and may not be passed**. This is a gate/evidence recheck, **not** a
`ccf-paper-reviewer full` manuscript review: no `**Overall:**` line, no numeric
paper score, no change to governing.

## Guard against prior recheck lessons

Same-source multi-views are explicitly **not** called independent verification
(D1). Fields are never called LICENSE text; no item is promoted to CLOSED (D2).
Verbatim strings are program-extracted FOUND/ABSENT (D3). The 591.42 MB
Correig-Fraga archive is a **different object** from the 602 MB Sintel-derived
data excluded earlier and is given no one-sided compliance endorsement (D4).
The top-level UTC field is named as product-generation time and explicitly
forbidden for recomputing fetch timing (D5, R115 W3). 403 pages are named as
throttling pages (D6). The two API JSON files are labelled metadata containers,
not archive content files. A local frozen copy from a previous round is not
presented as this round's first-hand upstream bytes (D7).

## Read-only double gate (zero write-back)

| Gate | Result |
|:--|:--|
| validator | `NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`, `score_meets_threshold=false`; D1 pass, D2 fail (P9–P21), D3 fail, D4 pass, D5 fail (`claim_evidence_matrix=False`) |
| guard | `INCOMPLETE`; A2 and A6 fail; S1–S7 pending |
| freeze | guard ledger SHA-16 `73043b4e164a5a5f` + mtime identical before/after; main `pipeline-state.json` SHA-16 `bcb48bb964e657a4` byte-identical |

The A6 dual wording (criteria `>=7.0` vs ledger `>8.0`) is a **known issue,
logged read-only, not modified**, pending gate-owner approval.

## Claims supported vs still unproven

Supported: 8 small archive content files were obtained at this timepoint and
byte-match the upstream official md5 (8/8); the two in-archive checksum tables
are self-consistent with those bytes for all non-absent rows; 8 throttling 403
pages are real at their timepoints; all saved bytes are recomputable; no gate
state changed; no credential or local absolute path entered this repo.

Still unproven / OPEN: the remaining 12 archive files' **content bytes**;
checkpoint **weight distribution terms** (a script constant is not a LICENSE;
code MIT does not license weights; public download is not a redistribution
grant); a stand-alone **natural-clips LICENSE text**; gap 2 and gap 4; a
designated gate-owner scientific/visual judgment; a written effective G0 pass
criterion. **gap 1 overall is PARTIAL, not closed; G0 stays `pending`.**

`metrics.csv` is deliberately absent: no experiment, model forward pass,
training, labels or scientific measurement was run. All numbers here are HTTP
statuses, byte counts and hashes of evidence files.

## Governing state (unchanged)

Independent full review **6.0**, validator `NOT_QUALIFIED`, guard `INCOMPLETE`,
0 qualifying papers, no COMPLETE. The R108 harbor engineering reward 1.0 is
unrelated to science and implies no 4090 capability claim. The confirmation
panel (<=32 h / K=45) remains **unauthorised** pending an explicit user
decision. Main project: no submission, no commit, no push.

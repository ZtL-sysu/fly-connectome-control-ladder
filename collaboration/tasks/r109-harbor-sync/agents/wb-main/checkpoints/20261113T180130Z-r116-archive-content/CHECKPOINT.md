# Checkpoint: 20261113T180130Z-r116-archive-content

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: this round's evidence acquisition,
  isolated recheck and bookkeeping finished; **NOT** a scientific result or a
  paper-acceptance claim)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Cites: `20261113T121816Z-r109-init`, `20261113T130720Z-r108-build`,
  `20261113T140607Z-r108-final`, `20261113T144313Z-r114-g0-license`,
  `20261113T161442Z-r115-g0-remaining`

## Changes and actual commands

R116 heartbeat, awakened 2026-11-14 01:27 +0800. Concurrency guard checked
first: primary `goal-ledger.md` mtime `2026-11-14 00:25:08` (62.6 min stale,
>10 min); zero project writes in the preceding 15 min; no independent main
session or polling process; no new file in `ccfa-review-reports/` or
`ccfa-idea-review-reports/`; no R116 artifacts. Governing independent full
review therefore stays **6.0**.

Instead of any machine-gate fix (R111: all such fixes need explicit user /
designated gate-owner approval; the five-point decision package is still
unanswered), this round executed **R115's handoff item 2 verbatim** — a named,
approval-free first-hand evidence action: the Zenodo 21549559 channel recovered,
so fetch the archive content bytes R115 could not obtain (6/6 HTTP 403) and
byte-compare them with the official md5.

Commands actually run (single sequential requests, no custom UA for content):

```bash
curl -sS --max-time 40 -o <file> -w '%{http_code}' \
  https://zenodo.org/api/records/21549559[/files][/<name>/content]
# two independent scripts, <local>/miniconda3/bin/python:
#   R116-manifest.py  -> R116-G0-R1-SOURCE-MANIFEST.json
#   R116-verify.py    -> R116-G0-R1-VERIFICATION.json (does NOT read the manifest)
readonly-validator/validate_single_paper.py --threshold 7.0 --out /tmp/r116-validator.txt
guard_engine.py check -l guard/ledger-null-ladder.json -o /tmp/r116-guard-check.txt
```

No experiment, model forward pass, training, labels, dataset load or inference
was run. No remote compute was contacted except public Zenodo HTTP GETs.

## Checks and results

| Check | Result |
|:--|:--|
| Raw response bytes saved | **18 files**: 10 x HTTP 200 (2 API metadata containers + **8 archive content files**) + 8 x `*.403.html` throttling pages |
| (a) upstream official md5 (Zenodo files-list API) | **8/8 MATCH** (zero MISMATCH) |
| (b) in-archive `MANIFEST.csv` sha256 | 6 MATCH + 2 `STRUCTURALLY_ABSENT` |
| (c) in-archive `SHA256SUMS` | 7 MATCH + 1 `STRUCTURALLY_ABSENT` — **same source as (b)**, not independent cross-validation |
| size (upstream API) | **8/8 MATCH** |
| three-party disk <-> manifest <-> verification | SHA-256 / MD5 / bytes **8/8 identical** |
| structural absences | `MANIFEST.csv` has no row for itself or for `SHA256SUMS`; `SHA256SUMS` has no row for itself (it does list `MANIFEST.csv`). Verified verbatim from saved bytes; a missing row is NOT a mismatch |
| verbatim README strings | **6/6 FOUND**, incl. `The record is released under CC BY 4.0.` (record-level self-statement), `The raw FlyWire synapse release is not duplicated.`, `proofread_connections_783.feather`, `sha256sum --check SHA256SUMS` |
| archive scale | 20 files / **591,418,589 B**; obtained 8 files / **16,519 B = 0.0028%** |
| not downloaded | **12 files** = 6 compressed tables (587,260,790 B) + 6 plain CSV (4,141,280 B); content bytes NOT obtained, NOT verified (exclusion list + throttling risk) |
| 403 pages | **8/8** verbatim `unusual traffic from your network` (anti-crawler throttling, NOT authorization refusal), **8 distinct md5**, named `*.403.html` |
| credentials / local paths | 6 strict pattern classes over 18 bytes files: **0 hits**; isolated recheck with 10 broader classes: 0 hits |
| v1 false negative | v1 counted structurally absent rows as failures => spurious `all_pass=False`; **script judgment defect, not data inconsistency**. v1 preserved verbatim (9,413 B / `756fd2b1…`), v2 three-state rule passes, both readings retained, no historical byte rewritten |
| Validator (read-only) | `NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`, `score_meets_threshold=false`; D1 pass, D2 fail (P9–P21), D3 fail, D4 pass, D5 fail |
| Guard (read-only) | `INCOMPLETE`; A2 and A6 fail; S1–S7 pending; ledger SHA-16 `73043b4e164a5a5f` + mtime `2026-11-13 08:09:20` identical before/after => zero write-back |
| Main pipeline state | `bcb48bb964e657a4` byte-identical before/after; G0 `pending`; G0–G8 / validation / handoff all pending |
| isolated copies | 6/6 primary artifacts byte-identical in `isolated/` |

## Timepoint discipline (no history rewriting)

| Round | Time | Record-level API | Archive content bytes |
|:--|:--|:--|:--|
| R107 | 11-13 05:4x | 403 | 403 |
| R114 | 11-13 22:3x | **200** | not requested (metadata/license only) |
| R115 | 11-13 23:5x | 403 | **6/6 HTTP 403 throttling** |
| **R116** | **11-14 01:3x** | **200** | **8 files 200 + 8 throttling 403 pages** |

All four are observations at their own timepoints. No historical bytes were
rewritten, deleted, redated or promoted. R116's channel was **mixed within one
round**: a first batch of 10 requests with a custom UA all returned 403,
subsequent single sequential requests without a custom UA returned 200 for
8/8 content files. This is an engineering observation, **not a causal claim**
about the platform's internals. The 403 pages are anti-crawler throttling, not
content-level authorization refusals.

## Fresh isolated recheck (recovered this round, before publication)

A **fresh isolated** sub-agent rechecked the bytes with **no expected
conclusion supplied**. Report `R116-G0-R1-INDEPENDENT-REVIEW.md`:
`PARTIAL | G0 may be passed: NO | Scientific result claimed: NO`, final
**31,188 B**, SHA-256
`2e348521889a549968ce0d6b0e1f6a77a947d44b8b6d7d36322962632a5b75c2`,
mtime `01:57:19`, original text unchanged (26 input files / 105,595 B; the
report was the only new output). Gate/evidence review, **not** a
`ccf-paper-reviewer full` manuscript review: no `**Overall:**` line, no
numeric paper score, no confidence field, no change to governing.

It independently recomputed three-way hashes (zero MISMATCH), structural
absences, v1 false negative and its preservation, 403 pages, verbatim fields,
content safety and file integrity — all matched. **Ten named overclaim /
self-certification categories (a)–(j): CONFIRMED = 0 (all REFUTED);
WITHDRAW = none.**

Two NARROW accepted, both independently re-verified by the main session from
bytes: (1) `CLOSED (partial)` -> **PARTIAL** (8/20 files, 0.0028% of bytes);
(2) not-downloaded split `7 + 5` -> **6 compressed tables + 6 CSV**
(587,260,790 + 4,141,280 B). Six LOW wording/precision issues L3–L8 also
registered (manifest role terminology; D5 field covers only the manifest;
403 pages' embedded server timestamps; `ledger` term ambiguity; 403 tsv trace
alignment; /tmp double-gate claims not independently recomputable). All are
**append-only corrections** in the primary project; the published independent
review is untouched; the five published historical checkpoints are untouched.

Independent state re-judgment: archive-content bytes **PARTIAL**, full-archive
verification **OPEN**, checkpoint-weight distribution terms **OPEN**,
natural-clips stand-alone license **OPEN**, gap 1 overall **PARTIAL**,
**G0 PENDING and may not be passed**. The recheck is not an authorisation and
does not replace an R9 independent four-gap review.

## Guard against R114's 7 / R115's 6 recheck lessons

Same-source multi-views are labelled as **not** independent verification (D1).
Fields are never called LICENSE text; no item promoted to CLOSED (D2).
Verbatim strings program-extracted FOUND/ABSENT (D3). The 591.42 MB
Correig-Fraga archive is a **different object** from the 602 MB Sintel-derived
data excluded earlier and is given no one-sided compliance endorsement (D4).
The top-level UTC field is named **product-generation time** and explicitly
forbidden for recomputing fetch timing (D5 / R115 W3). 403 pages named as
throttling pages, not content (D6). The two API JSON files are labelled
metadata containers, not archive content files; a local frozen copy from a
previous round is not presented as this round's first-hand upstream bytes
(D7 / R115 W1). `R116-manifest.py` / `R116-verify.py` are explicitly a
consistency check, not independent cross-verification (R115 W4); the
independent recomputation was done by the fresh isolated sub-agent.
"0 credential hits" is scoped to this round's evidence directory (R115 W2/W6).

## Whole-repo content scan

Repeated on all files after adding this round's evidence file: **0 hits** for
credentials, API-key literals, bearer tokens, email addresses, private keys
or local absolute paths (`/Users/...`). No file over 50 MiB (max is a small
text file); no datasets, weights, binaries, third-party source trees, or
unpublished manuscript. Local absolute paths in the primary project are
represented as `<local>/` or omitted. The 12 large archive files are **not**
in this repo; only their names, sizes and checksums appear in sanitized text.
The credential-bearing local script from R115 remains in the primary project
only and is not part of this upload set.

`metrics.csv` is deliberately absent. No experiment, model forward pass,
training, labels or scientific measurement was run this round; the numbers
above are HTTP statuses, byte counts and hashes of evidence files, not research
metrics.

## Claims supported / still unproven

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
criterion. The R1 / **gap 1 overall remains PARTIAL — NOT closed; G0 stays
`pending`.**

## Risks and next action

R116's 200 is a reachability observation, not a correction of R115's 403. Do
not turn a PARTIAL into a pass, do not edit a published independent review, do
not self-certify any gate, and do not extrapolate a record-level CC BY
statement, repository MIT or public-download availability into redistribution
rights for model weights or Sintel-derived stimuli.

Next: continue the ordered gates G0–G8 with the designated gate owner's
judgment for gap 4; obtain the remaining first-hand license/hosting bytes when
the relevant channels are reachable. The confirmation panel (<=32 h / K=45)
remains unauthorised pending an explicit user decision. Do not execute any
machine-gate fix from the R111 decision package without approval.

## Governing state (unchanged)

Independent full review **6.0**, validator `NOT_QUALIFIED`, guard `INCOMPLETE`,
0 qualifying papers, no COMPLETE. The R108 harbor engineering reward 1.0 is
unrelated and implies no scientific result and no 4090 capability claim.

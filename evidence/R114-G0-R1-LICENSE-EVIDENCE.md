# R114 — G0 gap 1 first-hand license evidence (sanitized summary)

Status: `READONLY_FIRSTHAND_EVIDENCE_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`.
Round: R114 heartbeat, 2026-11-13 22:2x +0800 (14:2x UTC).
**Updated after an independent recheck — see "Corrections" below.**

This is a **sanitized summary**. Raw response bytes, the full source manifest,
and byte-level verification JSON stay in the primary project at `<local>/` and
are **not** uploaded here. No dataset, model weights, third-party source tree,
unpublished manuscript, credential or local absolute path is included.

## Why this round exists

An earlier independent gate review (R106) required, for G0 gap 1, that each
`asset/license/code path` annotation in the literature-baseline matrix be
backed by a **recomputable attachment** (saved license text + SHA) or an
**explicit negative conclusion with search evidence**. Byte SHAs of our own
copies do not count as license verification. A prior closure attempt (R107)
recorded all Zenodo routes as HTTP 403 and concluded
`NO LICENSE FIELD OBTAINED` (OPEN).

R114 re-probed the same authoritative routes with a plain HTTP client. They
were reachable this time. All responses were saved as raw bytes; SHA-256 and
byte counts were recomputed from disk independently: **14/14 matched**.

## Two previously OPEN items advanced — still PARTIAL

| Item | Earlier state | R114 first-hand evidence | Final state |
|:--|:--|:--|:--|
| Correig-Fraga data archive, Zenodo record 21549559, **license** | `NO LICENSE FIELD OBTAINED` / OPEN | Zenodo REST API `metadata.license.id = cc-by-4.0`, DataCite `rightsList[0].rightsIdentifier = cc-by-4.0`, Zenodo OAI-PMH `<rights rightsIdentifier="cc-by-4.0">`; CC BY 4.0 legalcode full text (18,657 B) saved. HTTP 200. | **PARTIAL** — see correction D2 |
| MPI Sintel optical-flow benchmark **license** (matrix row 24) | OPEN (only our own derived-clip SHAs existed) | Official `/license` page (13,208 B, HTTP 200): heading `Software Copyright License for non-commercial scientific research purposes`, with a third-party redistribution prohibition (decoded/normalized quote in the primary project). | **PARTIAL** — see correction D4 |

Additional cross-check: the official flyvis repository license file (1,146 B,
`MIT License`) is byte-identical (SHA-256 `1e0e24112aaccf40…`) to the copy
already held in the primary project; the GitHub repo API reports
`license.spdx_id = MIT`, `default_branch = main`. The uppercase `LICENSE` path
and the `master` branch path both return HTTP 404 — kept as negative evidence.

## Corrections (from a fresh isolated independent recheck)

A **new isolated sub-agent** re-examined the saved bytes with no expected
conclusion supplied. Report (primary project):
`gate-G0-R114/R114-G0-R1-INDEPENDENT-REVIEW.md`, final 26,104 B, SHA-256
`879ecb78ec229742dd532299f2fc09b0ff3b3dce1cb1a706c4c89883071f7c3e`, first line
`PARTIAL | G0 may be passed: NO | Scientific result claimed: NO`.
Its original text is preserved unchanged; a separate correction register
`R114-POST-REVIEW-CORRECTION.md` records the following **only by appending**.

- **D1 (substantive overclaim, withdrawn):** describing Zenodo REST / DataCite /
  OAI as "three independent endpoints, not a single point" was wrong. All three
  point to record `21549559` / DOI `10.5281/zenodo.21549559`; DataCite has
  `publisher = Zenodo`; OAI uses `oai_datacite` with
  `<datacentreSymbol>CERN.ZENODO</datacentreSymbol>` and its `<rights>` is
  verbatim the DataCite `rightsList[0]`. They are **three views of one Zenodo
  backend's single license record (same-source multi-view)**, not independent
  cross-verification. The claim rests on **one underlying source** plus one
  generic CC legalcode text.
- **D2 (substantive overclaim, withdrawn):** marking the "LICENSE text" item
  CLOSED was wrong. Zenodo exposes only the `metadata.license.id` **identifier
  field**; the archive's 20 files contain **no LICENSE file**; the saved
  `cc_by_4_0_legalcode.txt` is the **generic** CC text, not this asset's own
  LICENSE file. The item is **PARTIAL**, not CLOSED.
- **D3:** the Sintel redistribution quote is a **decoded/normalized
  transcription** (`&amp;` entity, U+2019 apostrophe), not a strict verbatim
  byte quote.
- **D4 (withdrawn):** the claim that this gives "a first-hand legal basis for
  excluding the 602 MB Sintel-derived data from this public repo" was a
  one-sided compliance inference mounted on bytes that do not contain `R109`
  or `602`; 591.42 MB belongs to a **different** archive (Correig-Fraga). The
  license also restricts use to `non-commercial scientific research`. Correct
  statement: the official page contains a third-party redistribution
  prohibition and is **directionally consistent** with the R109 exclusion
  decision, but these bytes do **not** independently validate that historical
  decision.
- **D5:** two `fetched_utc` values contain a literal `x` (invalid UTC); the
  original manifest bytes are preserved, and those fields must not be used for
  recomputation. Time order rests on file mtimes, HTTP status bytes and `date`.
- **D6:** the filename `correig_fraga_zenodo_oai_badarg.xml` is misleading —
  its bytes are a **valid successful `GetRecord` response**, not an error. The
  name is kept to preserve the SHA inventory.
- **D7:** byte-identity of two local copies does not by itself prove one is
  "the official original"; official provenance rests on the recorded fetch URL
  and repo API identity.

The recheck **confirmed** no overclaim in three areas: code MIT was **not**
extended to checkpoint weights, metadata listings were **not** presented as
content verification, and evidence collection was **not** presented as a G0
pass or a scientific result. It also confirmed 14/14 SHA/byte agreement and
that the primary `pipeline-state.json` still has G0 as
`pending / inputs: [] / evidence: []` with zero byte changes.

## Honest accounting of failures and limits

- R107 measured HTTP 403 (763 B each) for these Zenodo routes at its own time.
  R114 measured HTTP 200. This is a **time-dependent reachability difference**,
  not a correction of R107. All historical bytes remain untouched, undeleted,
  and with original dates. R114 only appends new-time-point evidence.
- GitHub API routes returned HTTP 200 on a first probe and HTTP 403 (rate
  limit) on a re-fetch within the same round. **Both** raw states are retained.
- The Zenodo OAI route first returned 422/403 because of shell argument
  escaping; with correct quoting it returned HTTP 200 with the rights field.
  Both states are recorded.
- **Still PARTIAL / OPEN:** the 591.4 MB archive **contents** were not
  downloaded — only the 20-file metadata listing with md5 checksums was
  obtained, and metadata is not content verification. The distribution terms
  of **pretrained checkpoint weights** were not obtained; code being MIT does
  not license the weights. No first-hand license was located for **natural
  clips**. The baseline matrix was **not rewritten** or re-frozen. ⇒ **R1
  overall remains PARTIAL; gap 1 is NOT closed.**
- gap 2, gap 4 (designated gate owner's scientific/visual judgment), and the
  written G0 pass criterion are all still open and require external approval.
  No gate was marked passed; the primary `pipeline-state.json` was not
  modified. The isolated recheck states: **G0 may NOT be passed**.

## Scope boundary

Zero training, labels, datasets, forward passes or inference. This is
**evidence acquisition**, not a G0 pass, not a scientific result, not an
independent full manuscript review, and not a hardware-capability claim. It is
unrelated to the R108 harbor engineering reward. Governing independent full
review remains **6.0**, validator `NOT_QUALIFIED`, guard `INCOMPLETE`,
0 qualifying papers, no COMPLETE.

# R115 — G0 gap 1 / R106 §6 R1: remaining first-hand evidence (sanitized summary)

Status: `READONLY_FIRSTHAND_EVIDENCE_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
Round: R115 heartbeat, 2026-11-13 23:5x +0800.
This is a **sanitized public summary**. Raw bytes, hashes and manifests stay in
the primary local project and are NOT uploaded. No local absolute paths appear
here; they are written as `<local>/`.

## Why this round

R111 concluded that every remaining machine-gate fix needs explicit user /
designated gate-owner approval. R114 instead did first-hand license evidence
acquisition; its fresh isolated recheck returned
`PARTIAL | G0 may be passed: NO` and identified 7 flaws, 2 of them substantive
overclaims (withdrawn by an appended correction). R114's handoff explicitly
named the three still-missing R1 items. This round addresses those three with
first-hand bytes only — no gate fix, no text patch, no self-certification.

## Concurrency guard (step 0)

Not triggered: primary ledger mtime was ~62.5 min stale (>10 min); a full-tree
scan found 0 project writes in the last 15 min; no independent main session or
polling process was running; both review-report directories had no new file;
no R115 artifacts existed. Governing independent full review therefore stays
at **6.0**.

## What was actually collected

10 raw response-byte files, SHA-256 and byte count recomputed from disk by the
local Conda Python. Two independently generated JSON artifacts
(`R115-G0-R1-SOURCE-MANIFEST.json`, `R115-G0-R1-VERIFICATION.json`) cross-check
10/10 SHA agreement; manifest UTC is a single valid ISO-8601 `+00:00` window.

| Group | Route | HTTP | Count |
|:--|:--|:--|--:|
| A | Zenodo 21549559 archive-content files (README.md, MANIFEST.csv, SHA256SUMS, DATA_DICTIONARY.md) | 403 | 4 |
| A | Zenodo record-level API + files listing | 403 | 2 |
| B | flyvis official upstream raw: CLI registry, response_norms.py, CHANGELOG.md, datasets/sintel.py | 200 | 4 |

All six 403 artifacts are 763-byte **anti-crawler / traffic-throttling** pages
(verbatim: `Access to this resource has been restricted due to unusual traffic
from your network.`), retained verbatim as negative evidence. They are **not**
archive content. Their six byte strings are **not identical** (six distinct
SHA-256 values; differences in per-page Reference hash and Timestamp), and this
is a rate-limit response, not a content-level authorization denial.

**One credential-bearing file was excluded.** The official upstream
`flyvis_cli/download_pretrained_models.py` raw route returned HTTP 200 / 4692 B
but embeds a hard-coded API credential. It was deleted before disk persistence
(`DELETED_BEFORE_DISK_PERSISTENCE`): the credential value was never printed,
copied, recorded or uploaded. A rescan of **this round's evidence directory and
its `sources/`** found **0 credential byte hits**. A pre-existing project-local
copy of that same script (outside this round's collected bytes, not introduced
or modified this round, never uploaded) still contains a credential; the
"0 hits" statement is scoped to this round's collection, **not** project-wide.

## Three R1 items, judged conservatively

1. **Correig-Fraga archive content bytes — OPEN / explicit negative evidence.**
   All 6 Zenodo routes returned HTTP 403 this timepoint. Timepoint discipline:
   R107 (05:4x) also 403, R114 (22:3x) record-level API 200, R115 (23:5x) 403
   again. All three are observations at their own timepoints; no historical
   bytes were rewritten, deleted, redated, or promoted. R114's 200 remains
   valid at its timepoint. The archive content (591.42 MB from metadata size
   sum) was **not** obtained. A metadata listing is not content verification.

2. **Pretrained checkpoints — hosting indicated (PARTIAL); distribution terms
   still OPEN.** The four official upstream raw files collected this round
   establish, verbatim, that the CLI exposes a `download-pretrained` entry; they
   do **not** contain the weight-download script itself (that script was
   excluded because it embeds a credential). The folder id and two published
   SHA-256 checksums (`results_pretrained_models.zip` → `71c78d40…db1`,
   `results_umap_and_clustering.zip` → `6300ec1e…9b19`) were extracted via
   `ast` as **public constants from a pre-existing project-local frozen copy**
   of that script (4692 B, SHA-256 `ce48e7d6…9be9`) — i.e. from **outside this
   round's ten first-hand byte files**. They indicate a **Google Drive public
   folder**, not the GitHub code repository. After the isolated recheck, the
   claim "hosting located from official upstream first-hand bytes this round"
   was **withdrawn**: the hosting is *indicated by a local frozen copy's public
   constants*, whose SHA is independently recomputable but which is not a byte
   file fetched this round. A script constant is **not** a LICENSE text;
   public-download availability is **not** a redistribution grant; the
   repository's MIT license covers "software and associated documentation
   files" and is **not extrapolated** to model weights. Weight distribution
   terms remain OPEN; the whole item stays PARTIAL.

3. **Natural clips — identity confirmed first-hand (PARTIAL); independent
   license still OPEN.** Verbatim program extraction from official upstream
   source found `~30 minutes of naturalistic stimuli (Sintel)` in
   `response_norms.py` and `class AugmentedSintel` in `datasets/sintel.py`.
   The matrix's "natural clips" are therefore **MPI Sintel-derived stimuli**,
   not a separate third-party asset; license attribution folds back into the
   Sintel official non-commercial scientific-research license obtained in R114
   (which also prohibits third-party redistribution). This removes the
   ambiguity of an unidentified license object. It is **not** a new license
   text, and this round gives **no one-sided compliance endorsement** to the
   historical decision to exclude Sintel-derived data from this public repo.

**Result: gap 1 (R1) overall remains PARTIAL; G0 stays `pending`.** No item was
promoted to CLOSED.

## Fresh isolated recheck (recovered this round)

A **fresh isolated** sub-agent rechecked this round's bytes without any expected
conclusion supplied. Report: `PARTIAL | G0 may be passed: NO | Scientific
result claimed: NO`, **24,958 B**, SHA-256 `5758007a…62e0`, original text
unchanged. (An earlier 22,396 B / `ef2b0e21…d55b3` reading was an
intermediate state before the sub-agent's final delivery; both SHA-256 values
are retained in the primary project, and the final on-disk bytes govern — the
same intermediate/final pattern as R114.) It is a gate/evidence review, not a `ccf-paper-reviewer full`
manuscript review: no `**Overall:**` line, no numeric paper score, no
confidence field, no change to the governing score. It independently confirmed
10/10 SHA-256 and byte agreement (disk ↔ manifest ↔ verification), 10/10
verbatim fields, 0 credential hits in this round's directory, that the
credential-bearing download was indeed deleted, and that the main
`pipeline-state.json` is byte-identical to the R106 frozen value (G0 still
`pending`). It found **no instance** of the ten named overclaim categories.

It did find six boundary/precision issues (W1–W6), all recorded as
**append-only corrections** in the primary project, with this public summary
(and the other unpublished files) corrected **before** publication:

- **W1 (withdrawn)**: the "pretrained-weight hosting from official upstream
  first-hand bytes" claim — the constants came from a local frozen copy outside
  this round's bytes; see item 2 above.
- **W2**: "0 credential hits" is scoped to this round's collection only.
- **W3 (LOW–MEDIUM, as narrowed in the review's final version)**: the `acquisition_window_utc`
  field is **misnamed** — both scripts generate it with `datetime.now()` at
  file-write time, so it records artifact-generation time, **not** a fetch time
  recoverable from the bytes; and the round did **not** use the six 403 bodies'
  embedded server timestamps (15:59–16:00 UTC, shown as +01:00) to calibrate it.
  The final review explicitly states that the embedded bytes being earlier than
  the script time is **normal fetch ordering and is NOT judged a factual
  contradiction**, and that the top-level UTC is valid and consistent with file
  mtime. The claim that R114's D5 lesson was fully implemented is withdrawn
  (satisfied only at the valid-format level). The manifest field must not be
  used to recompute fetch timing; its original bytes are preserved unchanged.
  The round awakened at 23:51 (+0800, 11-13) and acquisition ran past midnight
  into 00:0x (+0800, 11-14 = 16:0x UTC, 11-13).
- **W4 (withdrawn)**: "cross-checked 10/10 by two independent scripts" — both
  scripts read the same `sources/`, the same ten files, with the same
  `hashlib.sha256`; agreement is a **necessary consistency check**, not an
  independent cross-verification. The genuine independent recomputation was done
  separately by the isolated sub-agent.
- **W5**: the 403 pages are anti-crawler throttling, six distinct byte strings,
  not a content-level denial (see above).
- **W6**: this round's verification script scans 3 credential pattern classes;
  the isolated sub-agent re-scanned with 5 broader classes and still found 0
  hits, so the conclusion is unaffected but the self-check scope was narrower
  than its wording.

The recheck explicitly states these are **not fabrications**, that byte
authenticity is unaffected, and that the core honesty holds. The three R1
items remain **OPEN / PARTIAL / PARTIAL**; gap 1 overall is **not closed** and
G0 stays `pending`. The recheck is not an authorisation and does not replace an
R9 independent four-gap review.

## Guard against R114's 7 recheck lessons

Same-repository upstream modules are explicitly labelled as **not** mutually
independent cross-checks (D1); script constants are called fields, never
LICENSE text, and every item is PARTIAL/OPEN (D2); all verbatim strings are
program-extracted with FOUND/ABSENT (D3); no historical decision outside this
round's bytes is endorsed (D4); the top-level UTC is **format-valid and
consistent with file mtime**, though with the W3 field-semantics caveat above
(the timestamp is generated at write time and must not be used to recompute
fetch timing) and with the original manifest bytes kept (D5); the 403 pages
are named as throttling pages and an ABSENT result is retained with its reason
(D6); the 4 upstream files are identified as official raw bytes rather than
local copies, and the separate local frozen copy is explicitly labelled as
such (D7).

The recheck also recorded a **concurrency condition**: while it was working,
the main session appended a section 7 to its own evidence report and created
two new files. None of those were created by the sub-agent, were relied upon,
or entered its conclusion chain; it re-verified that 13 quoted phrases still
existed verbatim, so the byte-level evidence and the first-line verdict were
unchanged. Under R106 §6 R9, the main session's appended self-correction is
**not** a self-certification of gap-1 closure and does not change the
`pipeline-state.json` bytes or the verdict.

## Read-only double gate (this round, reports to /tmp)

| Gate | Result |
|:--|:--|
| validator | `EXIT=1 / NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`; `score_meets_threshold=false`; D1✓ D2✗ D3✗ D4✓ D5✗ |
| guard | `EXIT=1 / INCOMPLETE`; A2 and A6 FAIL; S1–S7 all pending; 0 recorded actions |
| ledger integrity | SHA-256 prefix `73043b4e164a5a5f` and mtime identical before/after ⇒ zero write-back |

The A6 report text still uses the ledger's legacy `> 8.0` wording (a known
dual-wording issue registered in R109/R111); read-only registered, not changed.

## Strict boundary

Zero gate promotion: main `pipeline-state.json` bytes unchanged, G0
`pending / inputs=[] / evidence=[]`, G0–G8 / validation / handoff all pending.
No change to any historical byte, review, score, threshold, manuscript, gate,
frozen artifact, matrix, criterion register or gate config. No
`ccf-paper-reviewer full` was launched, no `**Overall:**` line produced, no
self-authored governing review, no repeated review of an unchanged manuscript,
no gate skipping. D1/v3 and predictor v4 not reopened; the `<=32 h / K=45`
confirmation panel remains **unauthorised**. EXEC LOCK: zero model forward pass,
training, labels, dataset inference or injection. Unrelated to the R108 harbor
engineering reward; **no 4090 capability claim**. Primary project: no
submission, commit or push. Heartbeat schedule unchanged.

## Result

The step-3 precondition (a substantive positive new scientific result) is not
met, so no new manuscript copy, no 9-page compliance compile, and no fresh
isolated full manuscript review. **0 qualifying papers, no COMPLETE**; governing
independent review **6.0 / Confidence 4.0**, `NOT_QUALIFIED`, `INCOMPLETE`.
Only two stop gates remain: (1) reach >= 7.0, (2) user stops the loop.

`metrics.csv` is deliberately absent: no experiment, measurement, forward pass
or training was run. All numbers here are HTTP statuses, byte counts and hashes
of evidence files, not research metrics.

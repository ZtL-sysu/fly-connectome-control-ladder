# R123 — Gap 1 first-hand licence & code-path text acquisition (sanitized public summary)

**Nature**: `READONLY_GAP1_FIRST_HAND_LICENCE_TEXT_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`

This is a **sanitized** summary of a read-only evidence-acquisition round in the primary
project. Primary-project round audits, scripts, JSON, raw third-party bytes, and the
independent-review report are **not uploaded**. All local absolute paths are written as
`<local>/`. No credential value, no email, no dataset, no weight, no binary, no third-party
source code, no unsubmitted manuscript.

## Direction change (why this round is not a 9th process dossier)

R114–R121 were eight consecutive process/infrastructure audits. R121 derived from the sole
governing independent full review's own score-change rule (its section 13 "No quick change"
passage) a **negative closure**: read-only audits of that class cannot raise the
evidence-capped Overall; upward movement requires new scientific evidence. That conclusion
**still holds** and this round does not claim otherwise.

Instead, this round executes the standing step-1 item explicitly authorized by the goal owner:
**R106 section 6 R1 (close gap 1)**, which the R106 independent gate review flagged verbatim as
"no LICENSE text was read", and which the R120 decision register lists as a remaining
first-hand acquisition item, undone for 11+ rounds. These are real first-hand bytes, not a
wording patch.

## What was frozen (13 files, all HTTP 200, 262,728 bytes, all < 200 KB)

Third-party **public small texts only**: record metadata, licence text, README, asset
manifests, checksum lists, one official licence HTML page, one repo licence file, one
checkpoint-distribution script, two arXiv abstract pages, one GitHub repo-search response.
No dataset, no weights, no binary, no large file, no local path, no project credential.

One official upstream script embeds a hard-coded **third-party public** API-key literal. It is
not a credential of this project. That raw file is marked `upload_to_public_repo=false`, stays
local for byte reproducibility, and every derivative uses `<redacted>`. Following the
R117/R119/R120/R121/R122 precedent, **no raw file is uploaded**; only this sanitized summary.

## Substantive first-hand findings (third-party text facts, strictly scoped)

1. **Zenodo 21549559**: record-level `license.id=cc-by-4.0`, `access_right=open`, 20 files.
   Its README contains a verbatim `Licence and attribution` section stating the record is
   released under CC BY 4.0 and asking that both the record and upstream resources be cited.
   MANIFEST.csv lists 18 data assets with per-file SHA-256; SHA256SUMS has 19 lines.
   **Scoped**: this is a record-level statement plus archive-authored explanation text,
   **not** 18 independent per-asset licence texts, and the upstream FlyWire/Schlegel licence
   claim is a README transcription that was **not** independently verified against those
   archives. The local README SHA-256 matches MANIFEST.csv and SHA256SUMS, so one small asset
   is reproducible **without downloading any of the 159 MB / 179 MB data files**.
2. **Self-reference nesting 18 / 19 / 20**: MANIFEST.csv lists 18 data assets (not itself,
   not SHA256SUMS); SHA256SUMS lists 19 (adds MANIFEST.csv, not itself); the record API lists
   20 (adds SHA256SUMS). A nesting effect, **not** a data inconsistency.
3. **Sintel official licence (natural clips)**: "License for non-commercial scientific
   research purposes", with `License Grant`, verbatim "single-user, non-exclusive,
   non-transferable", Max-Planck-Gesellschaft ownership, and automatic termination on
   infringement. `CC BY` and `Creative Commons` each appear **0 times**. It is a **custom MPI
   non-commercial licence, not CC BY** — the baseline matrix line requiring separate
   asset/licence checks for optical-flow benchmarks, pretrained checkpoints and natural clips
   now has first-hand text support.
4. **Code licence is not checkpoint-weight licence**: the official repo API reports
   `spdx_id=MIT` on `main`, and its `license` file is the full MIT text (Copyright (c) 2023).
   But pretrained weights are **not** distributed under that text: the download script goes
   through a Google Drive folder plus a hard-coded key and `results_pretrained_models.zip`
   (SHA-256 prefix `71c78d40...`), and contains **zero** independent licence or distribution
   terms for weights/checkpoints. Weight distribution terms remain **OPEN**.
5. **FlyHack code path, negative evidence**: the arXiv abstract page has 0 `github.com` and 0
   Zenodo mentions; a GitHub repository search returns `total_count=0` / `items=[]`.
   **Scoped** to one specific query plus one abstract page — **not** a claim that no code
   exists anywhere.

## Reproducibility

An independent verifier (does not import the collector, does not use any round-produced JSON
as a data source for substantive claims) recomputes from raw bytes: **91 checks / 91 MATCH /
0 MISMATCH**. Group A is explicitly declared a same-machine byte-identity check, **not**
independent cross-verification. A v1 verifier had one wrong expected value (assumed 20
MANIFEST rows; true 18) — an expectation-assumption error, not a data inconsistency; both
v1 and v2 scripts and both readings are retained.

## Strict boundary

No forward pass / inference / training / labels / dataset / EPE or l2 metric / scientific
metric / new positive evidence. **Zero gate promotion** (G0 stays pending), zero
self-certification, zero state write-back: baseline matrix, source manifest, pipeline state,
and the primary ledger were **byte-unchanged** at collection time. No change to any review,
score, threshold, manuscript, gate, frozen artifact, registry, or gate configuration.

**Acquisition complete is NOT gap 1 closed**: R106 section 6 R1 requires the matrix to be
corrected and frozen entry-by-entry; R6 requires a designated gate owner's explicit
scientific/visual gate judgment; R7 requires the gate owner to record an explicit pass; R9
requires a fresh independent recheck after R1–R8. Matrix finalization, registry registration,
and the disposition of the Sintel and weight-distribution findings belong to decision groups
G5/G6/G7/G4 of the R120 consolidated decision register and require written gate-owner
adjudication. This round supplies **first-hand reproducible attachments only**.

No fresh isolated full manuscript review was launched; no scored verdict line was produced;
governing was not self-assessed; no gate was skipped; no v4 contract created; no P3 forward
pass started while G0 is pending; no `<=32h / K=45` confirmation authorization assumed; no
4090/L4/H20 capability claim. Primary project: no submission, no commit, no push.

## Result

The step-3 precondition (substantive positive new scientific evidence) is **not** met, so no
new manuscript copy, no compilation, no fresh isolated full review. **0 qualifying papers,
no COMPLETE written**; governing remains the R95 independent review, validator
`NOT_QUALIFIED`, guard `INCOMPLETE`. Stop gates still only: (1) qualify, (2) goal owner stops.

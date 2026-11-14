# Checkpoint: 20261113T161442Z-r115-g0-remaining

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: this round's evidence acquisition and
  bookkeeping are finished; NOT a scientific or paper-acceptance claim)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Cites: `20261113T121816Z-r109-init`, `20261113T130720Z-r108-build`,
  `20261113T140607Z-r108-final`, `20261113T144313Z-r114-g0-license`

## Changes and actual commands

R115 heartbeat, awakened 2026-11-13 23:51 +0800. Concurrency guard checked
first: primary ledger mtime was ~62.5 min stale (>10 min); full-tree scan found
0 project writes in the last 15 min; no independent main session or polling
process; both review-report directories had no new file; no R115 artifacts
existed. Governing independent full review therefore stays at **6.0**.

Instead of any machine-gate fix (R111 established that all such fixes need
explicit user / designated gate-owner approval), this round continued R114's
handoff item 2: first-hand evidence acquisition for the three still-missing
R1 / G0 gap-1 items. Commands actually run:

```bash
curl -sS -L --max-time 30 -A <UA> -o <file> -w '%{http_code}' <url>  # 10 saved
python -c 'hashlib.sha256(...).hexdigest()'       # recomputed from disk bytes
readonly-validator/validate_single_paper.py --out /tmp/r115_validator.json
guard_engine.py check -l guard/ledger-null-ladder.json -o /tmp/r115_guard_report.md --no-report
```

Two independent scripts produced `R115-G0-R1-SOURCE-MANIFEST.json` and
`R115-G0-R1-VERIFICATION.json`; their SHA-256 entries cross-check 10/10.

## Checks and results

| Check | Result |
|:--|:--|
| Raw response bytes saved | 10 files (6× HTTP 403 negative evidence, 4× HTTP 200 official upstream raw) |
| SHA-256 + byte recompute from disk | **10/10 consistency match** between two scripts reading the same `sources/` with the same `hashlib.sha256` (a necessary consistency check, NOT independent cross-verification); the **fresh isolated sub-agent** separately recomputed 10/10 from disk |
| Verbatim field extraction | `~30 minutes of naturalistic stimuli (Sintel)` FOUND; `class AugmentedSintel` FOUND; `download-pretrained` FOUND; an ABSENT result retained with its reason; 10/10 fields re-extracted independently by the isolated sub-agent |
| Zenodo 21549559 archive-content routes | **6× HTTP 403**, 763-byte **anti-crawler / traffic-throttling** pages (verbatim `…unusual traffic from your network.`), six distinct byte strings ⇒ archive content bytes NOT obtained (OPEN) |
| Pretrained checkpoint hosting | **Corrected after isolated recheck (W1)**: this round's 4 official upstream raw files establish the CLI `download-pretrained` entry only. The `folder_id` and two published SHA-256 checksums were extracted via `ast` from a **pre-existing project-local frozen copy outside this round's ten byte files** (4692 B, SHA-256 `ce48e7d6…9be9`) and indicate a Google Drive public folder, not the GitHub code repo. The claim "hosting located from official upstream first-hand bytes" is **withdrawn** ⇒ hosting PARTIAL, distribution terms OPEN |
| Natural clips identity | Official upstream source verbatim shows Sintel-derived `AugmentedSintel` stimuli, not a separate third-party asset ⇒ identity PARTIAL, independent license OPEN |
| Credential handling | One official script returning HTTP 200 / 4692 B embedded a hard-coded API credential; **deleted before disk persistence**, value never printed/copied/recorded/uploaded. **Scoped correction (W2)**: 0 credential hits holds for **this round's evidence directory and `sources/` only**; a pre-existing project-local copy of that script still contains a credential (not introduced/modified/uploaded this round). The isolated sub-agent re-scanned with 5 broader pattern classes and still found 0 hits in this round's directory (W6) |
| Validator (read-only) | `EXIT=1 / NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`; `score_meets_threshold=false`; D1✓ D2✗ D3✗ D4✓ D5✗ |
| Guard (read-only) | `EXIT=1 / INCOMPLETE`; A2 and A6 fail; S1–S7 pending; ledger SHA prefix `73043b4e164a5a5f` + mtime identical before/after ⇒ zero write-back |
| Main pipeline state | SHA-256 `bcb48bb9…a33d` / 3723 B; G0 `pending / inputs=[] / evidence=[]`; G0–G8 / validation / handoff all pending ⇒ **byte-level zero change** |

## Timepoint discipline (no history rewriting)

R107 (05:4x) recorded HTTP 403 for these Zenodo routes; R114 (22:3x) recorded
HTTP 200 for the record-level API; R115 (23:5x) recorded HTTP 403 again. All
three are observations at their own timepoints. No historical bytes were
rewritten, deleted, redated, or promoted; R114's 200 remains valid at its
timepoint. A metadata listing (R114) and a 403 page (R115) are both **not**
archive content verification.

**Timestamp correction (W3, LOW–MEDIUM in the review's final version)**: the
top-level UTC fields are **format-valid ISO-8601 and consistent with file
mtime**, but the `acquisition_window_utc` field is **misnamed** — both scripts
generate it with `datetime.now()` at file-write time, so it records
artifact-generation time, not a fetch time recoverable from the bytes; and the
round did not use the six 403 bodies' embedded server timestamps (15:59–16:00
UTC, shown as +01:00) to calibrate it. The final review explicitly states that
embedded bytes being earlier than the script time is **normal fetch ordering
and is NOT judged a factual contradiction**. The claim that R114's D5 lesson
was fully implemented is **withdrawn** (satisfied only at valid-format level).
Manifest original bytes are preserved unchanged; the field must not be used to
recompute fetch timing. The heartbeat awakened at 23:51 (+0800, 11-13) and
acquisition ran past midnight into 00:0x (+0800, 11-14 = 16:0x UTC on 11-13).

## Fresh isolated recheck (recovered this round, before publication)

A **fresh isolated** sub-agent rechecked the bytes with no expected conclusion
supplied. Report: `PARTIAL | G0 may be passed: NO | Scientific result claimed:
NO`, **24,958 B**, SHA-256 `5758007a…62e0`, original text unchanged. (An
earlier 22,396 B / `ef2b0e21…d55b3` reading was an intermediate state before
the sub-agent's final delivery; both SHA-256 values are retained in the primary
project and the final on-disk bytes govern — the same intermediate/final
pattern as R114.) Gate/evidence review, not a manuscript full review: no
`**Overall:**` line, no numeric paper score, no confidence field, no change to
governing. It independently confirmed
disk ↔ manifest ↔ verification **10/10** SHA/bytes, **10/10** verbatim fields,
0 credential hits in this round's directory, deletion of the credential-bearing
download, and `pipeline-state.json` byte-identical to the R106 frozen value.

It found **no instance** of the ten named overclaim categories, but six
boundary/precision issues (W1–W6): W1/W2 MEDIUM, W3 LOW–MEDIUM, W4/W5/W6 LOW.
W1 ("weight hosting from official upstream first-hand bytes") and W4
("cross-check 10/10 = independent verification") were **withdrawn**; W2
(credential-hit scope), W3 (timestamp field semantics; the final version
explicitly does NOT judge the time difference a factual contradiction), W5
(403 is anti-crawler throttling, six distinct byte strings) and W6 (scanner
covers 3 pattern classes) were **narrowed**. All are
**append-only corrections** in the primary project; the four unpublished files
in this repo were corrected **before** this publication. The recheck explicitly
states these are not fabrications, byte authenticity is unaffected, and the
core honesty holds. The three R1 items remain OPEN / PARTIAL / PARTIAL; gap 1
overall is not closed; G0 stays `pending`. The recheck is not an authorisation
and does not replace an R9 independent four-gap review.

## Guard against R114's 7 recheck lessons

Same-repository upstream modules are explicitly labelled as **not** mutually
independent cross-checks (D1). Script constants are called fields, never a
LICENSE text, and no item is promoted to CLOSED (D2). All verbatim strings are
program-extracted with FOUND/ABSENT (D3). No historical decision outside this
round's bytes is given one-sided compliance endorsement — in particular the
earlier decision to exclude Sintel-derived data from this public repo (D4).
Top-level UTC is **format-valid and consistent with file mtime**, with the W3
field-semantics caveat (write-time timestamp, not usable to recompute fetch
timing), and the original manifest bytes are preserved (D5). 403 pages are named as throttling
pages and an ABSENT result is retained with its reason (D6). The four upstream
files are identified as official raw bytes, and the separate local frozen copy
is explicitly labelled as outside this round's bytes (D7).

## Whole-repo content scan

Repeated on all 27 files after adding this round's evidence file: **0 hits**
for credentials, API-key literals, bearer tokens, email addresses, or local
absolute paths. No file over 50 MiB (max 12,523 B); no datasets, weights,
binaries, third-party source trees, or unpublished manuscript. This round's new
evidence file had 0 dangerous-pattern hits. Local absolute paths in the primary
project are represented as `<local>/` or omitted. The credential-bearing local
script referenced in W2 is in the primary project only and is **not** part of
this upload set.

`metrics.csv` is deliberately absent. No experiment, model forward pass,
training, labels or scientific measurement was run this round; the numbers
above are HTTP statuses, byte counts and hashes of evidence files, not research
metrics.

## Claims supported / still unproven

Supported: the CLI `download-pretrained` entry and the two published checksums
as **public constants of a local frozen copy** (W1-corrected: not a first-hand
upstream byte file fetched this round); the Sintel-derived identity of the
"natural clips" from official upstream bytes; the fact that Zenodo
archive-content bytes were unavailable at this timepoint (throttling 403); that
all saved bytes are recomputable (10/10, independently confirmed); that no gate
state changed.

Still unproven / OPEN: the 591.42 MB archive **contents** (metadata size sum
only); checkpoint **weight distribution terms** (a script constant is not a
LICENSE, code MIT does not license weights, public download is not a
redistribution grant); a stand-alone **natural-clips LICENSE text**; the
baseline matrix was not corrected or re-frozen; gap 2 and gap 4 remain open;
no designated gate-owner scientific/visual judgment; G0 written pass criterion
still a non-effective draft. **R1 overall remains PARTIAL; gap 1 is NOT closed;
G0 stays `pending`.**

## Risks and next action

R115's 403 is a reachability observation, not a correction of R114. Do not turn
a PARTIAL into a pass, do not edit a published independent review, do not
self-certify any gate, and do not extrapolate repository MIT or public-download
availability into model-weight redistribution rights.

Next: continue the ordered gates G0–G8 with the designated gate owner's
judgment for gap 4; obtain the remaining first-hand license/hosting bytes when
the relevant channels are reachable. The confirmation panel (<=32 h / K=45)
remains unauthorised pending an explicit user decision.

## Governing state (unchanged)

Independent full review **6.0**, validator `NOT_QUALIFIED`, guard `INCOMPLETE`,
0 qualifying papers, no COMPLETE. The R108 harbor engineering reward 1.0 is
unrelated and implies no scientific result and no 4090 capability claim.

# Checkpoint: 20261113T144313Z-r114-g0-license

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: this round's evidence acquisition and its
  independent recheck are finished; NOT a scientific or paper-acceptance claim)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Cites: `20261113T121816Z-r109-init`, `20261113T130720Z-r108-build`,
  `20261113T140607Z-r108-final`

## Changes and actual commands

R114 heartbeat. Concurrency guard checked first: primary-project ledger mtime
was 18 minutes old, no independent main session was running, and a full-tree
scan found zero project writes after the ledger timestamp. No new files in
either review-report directory, so the governing independent full review is
unchanged at 6.0.

Instead of another gate-configuration patch (all such fixes require explicit
user / designated gate-owner approval), this round did the R106 §6 R1 work:
first-hand license/asset evidence acquisition for G0 gap 1. Commands actually
run:

```bash
curl -sS -L --max-time 30 -A <UA> -o <file> -w '%{http_code}' <url>   # 12 routes
python -c 'hashlib.sha256(...).hexdigest()'                            # 14/14 recomputed
readonly-validator/validate_single_paper.py --out /tmp/r114-validator.json
guard_engine.py check -l guard/ledger-null-ladder.json -o /tmp/r114-guard-report.txt --no-report
```

A fresh isolated sub-agent independently rechecked the saved bytes; the main
session supplied no expected conclusion.

## Checks and results

| Check | Result |
|:--|:--|
| Raw response bytes saved | 14 files, including 2× HTTP 404 and 2× HTTP 403 negative evidence |
| SHA-256 + byte recompute from disk | **14/14 matched**, no fabricated hashes |
| Zenodo record 21549559 | HTTP 200; `metadata.license.id = cc-by-4.0`, DOI `10.5281/zenodo.21549559`, 20 files, 591.42 MB from size sum |
| DataCite / Zenodo OAI | HTTP 200; `cc-by-4.0` in `rightsList` / `<rights>` |
| MPI Sintel official `/license` | HTTP 200, 13,208 B; `Software Copyright License for non-commercial scientific research purposes` + third-party redistribution prohibition |
| flyvis official `license` | HTTP 200, 1,146 B, MIT; byte-identical to the primary-project copy (`1e0e2411…`); repo API `spdx_id = MIT` |
| GitHub API routes | HTTP 200 on first probe, HTTP 403 (rate limit) on re-fetch — both raw states kept |
| Validator (read-only) | `NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`; D1✓ D2✗ D3✗ D4✓ D5✗ |
| Guard (read-only) | `INCOMPLETE / EXIT=1`; A2 and A6 fail, S1–S7 pending; ledger SHA unchanged |
| Isolated independent recheck | **`PARTIAL \| G0 may be passed: NO \| Scientific result claimed: NO`**; final 26,104 B, SHA-256 `879ecb78…3e` |

## Corrections appended (not overwrites)

The recheck found 7 flaws in the round's own write-up. Two were substantive
overclaims and were **withdrawn by an appended correction register**:

- **D1**: Zenodo REST / DataCite / OAI are **same-source multi-views** of one
  Zenodo license record, not three independent cross-checks. The claim rests
  on one underlying source.
- **D2**: a `license.id` field plus the generic CC legalcode is **not** this
  asset's own LICENSE text; that item is PARTIAL, not CLOSED.

Also withdrawn: a one-sided "602 MB Sintel-derived-data exclusion compliance
basis" claim (D4 — the license also restricts use to non-commercial scientific
research, and 591.42 MB refers to a different archive). D3 (normalized quote,
not strict verbatim), D5 (two invalid UTC timestamp fields, original manifest
preserved), D6 (misleading `badarg` filename for a successful OAI response),
D7 (local byte-identity does not prove official provenance). An intermediate
26,088 B / `f83a0c13…36` reading of the review is recorded rather than
silently replaced. The independent review's own text is unchanged.

The recheck confirmed no overclaim in three areas: code MIT was not extended
to checkpoint weights, metadata listings were not presented as content
verification, and evidence collection was not presented as a G0 pass or a
scientific result.

## Whole-repo content scan

Repeated on all 24 files: **0 hits** for credentials, tokens, account
identifiers, local absolute paths, or email addresses. Four *descriptive*
mentions of repository names remain only in already-published immutable
checkpoints / HANDOFF / LOG and state that a private repo was excluded; they
contain no credentials. No file over 50 MiB (max 12,523 B); no datasets,
weights, binaries, third-party source trees or unpublished manuscript.
This round's new evidence file had 0 dangerous-pattern hits.

`metrics.csv` is deliberately absent. No experiment, model forward pass,
training, labels or scientific measurement was run this round; the numbers
above are HTTP statuses, byte counts and hashes of license/asset evidence, not
research metrics.

## Claims supported / still unproven

Supported: the license identifier for Zenodo record 21549559 is `cc-by-4.0`;
the Sintel official license restricts use to non-commercial scientific
research and prohibits third-party redistribution; the flyvis repository is
MIT-licensed; the saved bytes are recomputable (14/14); no gate state changed.

Still unproven / OPEN: the 591.4 MB archive **contents** were not downloaded;
checkpoint **weight** distribution terms were not obtained (code MIT does not
license weights); no first-hand license for **natural clips**; the baseline
matrix was not corrected or re-frozen; gap 2 and gap 4 remain open; no
designated gate-owner scientific/visual judgment; G0 written pass criterion
still a non-effective draft. **R1 overall remains PARTIAL; gap 1 is NOT
closed; G0 stays `pending`.**

## Risks and next action

R107 recorded HTTP 403 for these Zenodo routes; R114 recorded HTTP 200. This
is a time-dependent reachability difference, not a correction of R107 — all
historical bytes stay untouched and dated. Do not turn a PARTIAL into a pass,
do not edit the published independent review, do not self-certify any gate.

Next: close the remaining R1 items with first-hand evidence, then continue the
ordered gates G0–G8 with the designated gate owner's judgment for gap 4. The
confirmation panel (<=32 h / K=45) remains unauthorised pending an explicit
user decision.

## Governing state (unchanged)

Independent full review **6.0**, validator `NOT_QUALIFIED`, guard `INCOMPLETE`,
0 qualifying papers, no COMPLETE. The R108 harbor engineering reward 1.0 is
unrelated and implies no scientific result and no 4090 capability claim.

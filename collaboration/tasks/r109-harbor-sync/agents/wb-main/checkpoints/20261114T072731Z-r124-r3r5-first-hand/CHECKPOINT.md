# CHECKPOINT — 20261114T072731Z-r124-r3r5-first-hand

- Task / agent / branch: `r109-harbor-sync` / `wb-main` / `agent/r109-harbor-sync/wb-main`
- Status: `completed` (work-state label, NOT scientific validation)
- Round: R124 heartbeat, 2026-11-14 15:08–15:3x +0800
- Created (UTC): 2026-11-14T07:27:31Z
- Input HEAD at manifest creation: see `manifest.json` (`input_git_head`)
- Immutable: all 19 earlier checkpoints' bytes are **not rewritten**.

## Why this checkpoint exists

The standing step-1 item 1 (explicitly authorized by the goal owner) requires closing
G0's substantive gaps per the R106 independent gate review's Concern-to-action list, with
first-hand reproducible attachments rather than wording patches. R122 closed the
evidence-acquisition half of **R4** (arXiv v2 dual-abstract byte freeze); R123 closed the
evidence-acquisition half of **R1** (gap 1 licence / code-path texts). This round closes
the last two R106 §6 items that do **not** require a designated gate owner's ruling:
**R3** (2026 geometry study first-hand source + version marking + verbatim recheck of the
`p<10^-13` / trained-ER / OFF-closure claims + secondary-mirror status) and **R5**
(first-hand byte verification of the W5/W8 factual corrections), and produces the first
per-item convergence table for R106 §6 R1–R9.

R105 / R107 / R109 halted the process-dossier loop three times; R121 derived from the
sole governing independent full review's own section 13 "No quick change" rule a negative
closure: read-only audits of that class cannot raise the evidence-capped Overall. That
conclusion still holds. This round is **not** a 9th process dossier and does **not**
present acquisition as progress toward qualifying.

## What was done (read-only)

- 13 third-party public small texts frozen under `<local>/`: 8 × HTTP 200, 1 × HTTP 301,
  4 × HTTP 429 (Cloudflare `error code: 1015`, preserved verbatim as negative evidence),
  total **323,740 B**, largest single file 64,741 B, each SHA-256 anchored in a round-local
  source manifest with an idempotent acquisition map. No dataset, no weights, no binary,
  no large file, no local path, no project credential.
- Sources: bioRxiv official details API; the same API with `/1` suffix (byte-identical ⇒
  not a version selector, negative evidence); Crossref official work API; Europe PMC
  official search API; bioRxiv connect page; second-hand mirror 301 + followed 200; two
  arXiv abs pages; four rate-limited bioRxiv v1/v3 page probes.
- **No raw file is uploaded** (R117/R119/R120/R121/R122/R123 precedent); only
  `evidence/R124-R3-R5-FIRST-HAND-SANITIZED.md`. Primary round audit, scripts, JSON,
  verification outputs and the independent-review original are local-only.

## Substantive first-hand findings (third-party text facts, NOT project results)

1. bioRxiv official details API returns **12 version records** for DOI
   `10.64898/2026.06.10.731214` (v1 `2026-06-12` → v12 `2026-10-16`). The **v1 title**
   differs from the **v2–v12 title**, which is identical across all eleven later records.
2. **All 12 `abstract` fields are byte-identical** (4,816 chars, SHA-256 prefix
   `555e28f9fef3`), each verbatim containing `p < 10-13 in every case`,
   `closes the gap completely`, `trained Erdos-Renyi on OFF-polarity structure`.
   ⇒ The API `abstract` is a **current-abstract backfill into every version record**, not
   a per-version historical abstract; treating the v1 record's abstract as v1's abstract
   is invalid.
3. An early probe of the v1 HTML page returned HTTP 200 / 105,400 B but was **not saved**;
   its abstract was a **positive** one (RSA Spearman `r = 0.686`, `0.846`,
   `0.930 vs. 0.603`) without the three negative phrases. Four later probes all returned
   Cloudflare 429 ⇒ **no local v1 page byte freeze**; the positive abstract is recorded
   as a WebFetch transcription only, explicitly NOT a first-hand frozen artifact.
4. **Crossref** `abstract` is likewise the negative version, yet `created = 2026-06-12`
   (v1 date), title is the v2+ title, `indexed = 2026-10-21` ⇒ metadata-layer version
   mismatch: `created` is the first-publication date, not the current abstract's version.
5. The **second-hand mirror** `datePublished = 2026-10-16` equals the API **v12 date** and
   its body verbatim contains all three negative phrases ⇒ v12 scope. R106 recorded this
   URL as Cloudflare-blocked; this round obtained HTTP 200 / 37,429 B after a 301. This is
   a **time-point / endpoint difference**, not a claim that R106 fabricated anything; the
   mirror remains second-hand, used only for cross-corroboration.
6. **Strict scope for R3**: R106 §6 R3 asks to mark "v1 positive vs v3 largely negative".
   The first-hand bytes show "v3 is the turning version" is **unsupported** (v3 is one
   of 12 records, the API supplies no per-version abstracts, and the first appearance of
   the negative conclusion cannot be determined from local bytes). This round narrows to:
   v1 page (positive, no local bytes) vs current/v12 scope (negative, three independent
   first-hand byte sources); the middle ten versions' abstracts were not obtained and no
   version attribution is claimed for them. R106's central W6 finding still stands; **no
   R106 byte is rewritten**.
7. **R5 byte verification**: first-hand arXiv abs pages verbatim contain `22871090` (1 hit)
   / `22891264` (0), and `9 Oct 2026` (2) / `12 Oct 2026` (0), confirming both W8
   corrections. W5's retracted "v1 abstract" claim was already appended-only withdrawn
   inside R106's own round audit and byte-confirmed in R122; this round does not duplicate
   that correction or rewrite any historical byte.

## R106 §6 R1–R9 per-item convergence (first produced)

R1 (R123 evidence) → G5/G6/G7/G4; **R2** → G6; **R3 (this round)** → G6/G7 with no local
v1 page bytes; R4 (R122 evidence) → G7; **R5 (this round)** → G4/R9 (corrections may not
self-certify); **R6** → G4; **R7** → G4 + W13; **R8** depends on R1–R7; **R9** depends on
R1–R8. ⇒ All autonomously completable §6 items (R1/R3/R4 acquisition + R5 byte
verification) are now **exhausted**; every remaining item sits behind a designated gate
owner's ruling, converging on R120's minimal set `G1 + G4 + G10`.

**Acquisition complete is NOT gap closure**: matrix finalization, registry registration,
an explicit scientific/visual gate judgment, the written G0 pass criterion, and a fresh
independent recheck all require the designated gate owner. The heartbeat does not
self-write, self-certify, or promote any gate.

## Reproducibility

`R124-verify.py` does **not** import the acquisition module and does **not** use any
round-produced JSON as a substantive data source (source manifest only for group A
declarative SHA/byte identity); groups B–I recompute from raw bytes and independent
project files with its own logic, zero network access ⇒ **145 checks / 145 MATCH /
0 MISMATCH** (A 45 / B 27 / C 14 / D 10 / E 6 / F 9 / G 16 / H 12 / I 6). Group A is a
same-host necessary-consistency check, NOT an independent cross-check. The v1 verifier and
its 145/141/4 output are **retained verbatim**; six v1 script/expectation defects plus one
acquisition defect (unsaved HTTP 200 page) are documented — no data inconsistency, no
fabrication, no report fact error.

## Live read-only double gate (at collection time)

validator `NOT_QUALIFIED / 6.0 / >=7.0 / score_meets_threshold=false` (D1✓ D2✗ D3✗ D4✓
D5✗); guard `INCOMPLETE` (A2/A6 fail, S1–S7 all pending, 0 action entries), guard ledger
SHA unchanged ⇒ read-only; main-line `pipeline-state.json` 12 stages with
`CCFA-startup=passed` and **G0–G8 / validation / handoff all pending**, `G0.inputs=[]` /
`evidence=[]`. Byte-unchanged structural authorities at collection time: primary ledger,
main-line state, baseline matrix, source manifest, guard configuration.

## Strict boundary

Zero write-back to `pipeline-state.json`, `literature-baseline-matrix.md`,
`literature-search/source-manifest.json`, the primary ledger (at collection time), or any
gate configuration. Zero gate promotion (G0 pending), zero self-certification, zero state
change. EXEC LOCK: zero forward pass / inference / training / labels / dataset / EPE·l2 /
scientific metric / new positive evidence; network used only for read-only acquisition.
No change to any review / score / threshold / manuscript / gate / frozen artifact /
registry. No `ccf-paper-reviewer full`, no numeric `**Overall:**` line, no self-authored
governing review, no gate skipping, no v4 contract, no P3 while G0 pending, no assumption
of the `≤32h / K=45` confirmation authorization (D1 stays `BLOCKED_ON_CONFIRMATION`), no
4090 / L4 / H20 capability claim. Primary project: no submission / commit / push.

**Increment is evidence-layer, NOT score-layer**: per R121's negative closure, a first-hand
literature freeze does not change the governing 6.0 and is explicitly not presented as
progress toward qualifying.

## Fresh isolated independent recheck

A fresh isolated sub-agent was launched with **no expected verdict / score anchor /
conclusion anchor**. At this checkpoint's write time it was **not recovered**, so this
checkpoint claims **no recheck conclusion, no defect list, and no confirmation**. The
recovered conclusion and any append-only corrections will be published in a **new immutable
checkpoint**; these bytes are not rewritten. Gate/evidence-layer recheck, **not** a
`ccf-paper-reviewer full` manuscript review.

## Content safety

Full-repository strict pattern scan before push: credential value, token assignment,
email, local absolute path, credential filename, webhook, connection string, and real
scored-verdict line — 0 new hits. No >50 MiB file, no binary, no dataset, no weight, no
third-party source code, no unsubmitted manuscript. Only explicit files staged via
`git add --`; no `git add .`; `git diff --cached --check` clean; push to own agent branch;
`git ls-remote` remote SHA must equal local HEAD before claiming uploaded. 19 earlier
published checkpoints untouched; private `ZtL-sysu/novix-platform` untouched; no merge /
force push / branch deletion / Release.

## Result

Step-3 precondition (**substantive new positive scientific evidence**) unmet ⇒ no new
manuscript copy, no 9-page compliant compilation, no fresh isolated full review.
**0 papers qualified, no COMPLETE**; governing unchanged (R95 = 6.0 / Confidence 4.0),
`NOT_QUALIFIED` / `INCOMPLETE`; G0 pending; zero gate promotion / zero self-certification
/ zero state change. Stop gates remain only (1) qualify (>= 7.0) (2) goal owner stops.
A checkpoint `completed` is work state, not scientific validation.

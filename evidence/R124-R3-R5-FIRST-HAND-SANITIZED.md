# R124 — R106 §6 R3 / R5 first-hand text acquisition (sanitized public summary)

**Nature**: `READONLY_R3_R5_FIRST_HAND_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`

This is a **sanitized** summary of a read-only evidence-acquisition round in the primary
project. Primary-project round audits, scripts, JSON, the 13 raw third-party byte files,
and the independent-review report are **not uploaded**. All local absolute paths are
written as `<local>/`. No credential value, no author email, no dataset, no weight,
no binary, no third-party source code, no unsubmitted manuscript.

## Direction change (why this round is not a 9th process dossier)

R105 / R107 / R109 halted the "keep producing evidence dossiers" loop three times. R121
derived from the sole governing independent full review's own score-change rule (its
section 13 "No quick change" passage) a **negative closure**: read-only audits of that
class cannot raise the evidence-capped Overall; upward movement requires new scientific
evidence. That conclusion **still holds**; this round does not claim otherwise and does
not present acquisition as progress toward qualifying.

R122 closed the evidence-acquisition half of **R4** (arXiv v2 dual-abstract byte freeze);
R123 closed the evidence-acquisition half of **R1** (gap 1 licence / code-path texts).
This round executes the standing step-1 item explicitly authorized by the goal owner:
the last two items of R106 section 6's R1–R9 condition list that do **not** require a
designated gate owner's adjudication — **R3** (2026 geometry study: first-hand source,
version marking, verbatim recheck of the `p<10^-13` / trained-ER / OFF-closure claims,
secondary-mirror status) and **R5** (first-hand byte verification of the W5/W8 factual
corrections). It also produces, for the first time, a **per-item convergence table for
R106 §6 R1–R9** that localizes the remaining blockage to the R120 decision register's
minimal ruling set `G1 + G4 + G10`. This is **evidence acquisition**, not a wording
patch, not a gate pass, not a manuscript review.

## First-hand freeze (13 files / 323,740 B)

All third-party PUBLIC small texts, each SHA-256 anchored in a round-local source
manifest: 8 × HTTP 200, 1 × HTTP 301, 4 × HTTP 429 (Cloudflare `error code: 1015`,
preserved verbatim as negative evidence). Largest single file 64,741 B. Zero dataset /
weight / binary / large file / local path / project credential. Sources: bioRxiv
official details API, the same API with a `/1` suffix, Crossref official work API,
Europe PMC official search API, bioRxiv connect page, a second-hand mirror page
(301 + followed 200), two arXiv abs pages, and four rate-limited bioRxiv v1/v3 page
probes.

## Substantive first-hand findings (third-party text facts, NOT project results)

1. **bioRxiv official details API returns 12 version records** for DOI
   `10.64898/2026.06.10.731214` (v1 `2026-06-12` → v12 `2026-10-16`). The **v1 title**
   (`Connectome wiring shapes population-level neural geometry...`) differs from the
   **v2–v12 title** (`Representational geometry as a fidelity metric...`), which is
   identical across all eleven later records.
2. **All 12 `abstract` fields are byte-identical** (4,816 chars, same SHA-256 prefix
   `555e28f9fef3`), and each verbatim contains `p < 10-13 in every case`,
   `closes the gap completely`, and `trained Erdos-Renyi on OFF-polarity structure`.
   ⇒ The API `abstract` field is a **current-abstract backfill into every version
   record**, NOT a per-version historical abstract. It is therefore invalid to treat
   "the v1 record's abstract" as the v1 abstract.
3. An early probe of the v1 HTML page returned HTTP 200 / 105,400 B but was **not saved
   to disk**; its abstract was a **positive** one (RSA Spearman `r = 0.686`, `0.846`,
   `0.930 vs. 0.603`) and lacked the three negative-version phrases. Four subsequent
   probes all returned Cloudflare 429 ⇒ **no local byte freeze of the v1 page exists**;
   that positive abstract is recorded as a WebFetch transcription only, explicitly NOT
   counted as a first-hand frozen artifact.
4. **Crossref** `abstract` is likewise the negative version (with
   `<jats:sup>−13</jats:sup>`, `closes the gap`, `size-matched`, `Erdős–Rényi`), yet
   `created = 2026-06-12` (the v1 date) and the title is the v2+ title, with
   `indexed = 2026-10-21` ⇒ a **metadata-layer version mismatch**: `created` is the
   first-publication date, not the version of the current abstract.
5. The **second-hand mirror** has `datePublished = 2026-10-16`, exactly the API **v12
   date**, and its body verbatim contains all three negative-version phrases ⇒ the
   mirror reflects the **v12 scope**. R106 recorded this URL as Cloudflare-blocked;
   this round obtained HTTP 200 / 37,429 B after a 301 redirect. This is a **time-point /
   endpoint difference**, not a claim that R106 fabricated anything; the mirror remains
   a **second-hand** source used only for cross-corroboration, never as a first-hand
   conclusion source.
6. **Strict scope for R3**: R106 §6 R3 asks to mark "v1 positive vs v3 largely
   negative". The first-hand bytes show the "v3 is the turning version" claim is
   **unsupported**: v3 is merely one of 12 records (`2026-06-23`), the API supplies no
   per-version abstracts, and **it cannot be determined from local bytes in which
   version the negative conclusion first appeared**. This round can only narrow the
   finding to: v1 page (positive, no local bytes) vs current/v12 scope (negative, three
   independent first-hand byte sources). The middle ten versions' abstracts were not
   obtained and no version attribution is claimed for them. R106's central W6 finding
   (version ambiguity; the matrix cites a second-hand mirror without DOI/version) still
   stands; no R106 byte is rewritten.
7. **R5 byte verification**: first-hand arXiv abs pages verbatim contain `22871090`
   (1 hit) with `22891264` (0 hits), and `9 Oct 2026` (2 hits) with `12 Oct 2026`
   (0 hits), confirming both W8 corrections. W5's retracted "v1 abstract" claim was
   already appended-only withdrawn inside R106's own round audit and byte-confirmed in
   R122; this round does **not** duplicate that correction or rewrite any historical
   byte. Per R9, correction actions may not self-certify; matrix finalization and
   registry registration remain adjudication items (G6 / G7).

## R106 §6 R1–R9 per-item convergence (first produced)

| Item | Autonomous-evidence status | Remaining blocker |
|:--|:--|:--|
| R1 (gap 1) | R123 delivered 13 first-hand texts | classification / registration → G5/G6/G7/G4 |
| R2 (gap 2) | matrix still 9,445 B, stale rows intact | G6 ruling |
| **R3** | **this round: 13 first-hand files + 145/145 recompute + scoped narrowing** | registration / finalization → G6/G7; no local v1 page bytes |
| R4 | R122 delivered 5 raw files / 321,571 B | registry registration → G7 |
| **R5** | **three correction values byte-confirmed** | corrections may not self-certify → G4 / R9 |
| R6 (gap 4) | none | G4 ruling |
| R7 | `G0.inputs=[]` / `evidence=[]` / `pending` unchanged | G4 ruling + W13 pass criterion |
| R8 | incomplete | depends on R1–R7 |
| R9 | incomplete | depends on R1–R8 |

⇒ All R106 §6 items that the heartbeat can autonomously complete (R1 / R3 / R4
acquisition + R5 byte verification) are now **exhausted**; every remaining item sits
behind a designated gate owner's ruling, converging exactly on R120's minimal set
`G1 + G4 + G10` (G2/G3/G5/G6/G7/G8/G9 depend on or refine those). This confirms R111's
"autonomous reachable actions exhausted" at the per-item, first-hand-byte level.

**Acquisition complete is NOT gap closure**: matrix finalization, `source-manifest.json`
registration, an explicit scientific/visual gate judgment, the written G0 pass criterion,
and a fresh independent recheck all require the designated gate owner. The heartbeat
does not self-write, self-certify, or promote any gate.

## Reproducibility

`R124-verify.py` does **not** import the acquisition module and does **not** use any
round-produced JSON as a substantive data source (the source manifest is used only for
group A declarative SHA/byte identity); groups B–I recompute from raw source bytes and
independent project files with the verifier's own logic, with zero network access ⇒
**145 checks / 145 MATCH / 0 MISMATCH** (A 45 / B 27 / C 14 / D 10 / E 6 / F 9 / G 16 /
H 12 / I 6). Group A is explicitly a same-host necessary-consistency check, NOT an
independent cross-check. A v1 verifier and its 145/141/4 output are **retained verbatim**;
all six v1 defects (one module-import failure, one bytes-serialization failure, four
expectation-assumption errors) plus one acquisition defect (an unsaved HTTP 200 page) are
documented. All seven are script/expectation defects: **no data inconsistency, no
fabrication, no report fact error**.

## Live read-only double gate (at collection time)

- validator: `NOT_QUALIFIED`, `overall_score = 6.0`, `threshold = 7.0`, `>=`,
  `score_meets_threshold = false`, D1 pass / D2 fail / D3 fail / D4 pass / D5 fail.
- guard: `INCOMPLETE` (A2 / A6 fail, S1–S7 all pending, action sequence 0 entries);
  guard ledger SHA unchanged across the check ⇒ read-only.
- main-line `pipeline-state.json`: 12 stages, `CCFA-startup = passed`, **G0–G8 /
  validation / handoff all `pending`**, `G0.inputs = []` / `evidence = []`.

## Strict boundary

Zero write-back to `pipeline-state.json`, `literature-baseline-matrix.md`,
`literature-search/source-manifest.json`, the primary ledger (at collection time), or
any gate configuration — all byte-unchanged. Zero gate promotion (G0 pending), zero
self-certification, zero state change. EXEC LOCK: zero forward pass / inference /
training / labels / dataset / EPE·l2 / scientific metric / new positive evidence; network
used only for read-only acquisition. No change to any review / score / threshold /
manuscript / gate / frozen artifact / registry. No `ccf-paper-reviewer full`, no numeric
`**Overall:**` line, no self-authored governing review, no gate skipping, no v4
contract, no P3 while G0 pending, no assumption of the `≤32h / K=45` confirmation
authorization (D1 stays `BLOCKED_ON_CONFIRMATION`), no 4090 / L4 / H20 capability claim.
Primary project: no submission / commit / push.

**Increment is evidence-layer, NOT score-layer**: per R121's negative closure, a
first-hand literature freeze does not change the governing 6.0 and is explicitly not
presented as progress toward qualifying.

## Fresh isolated independent recheck

A fresh isolated sub-agent was launched with **no expected verdict / score anchor /
conclusion anchor**. At this checkpoint's write time it was **not recovered**, so this
checkpoint claims **no recheck conclusion, no defect list, and no confirmation**. The
recovered conclusion and any append-only corrections will be published in a **new
immutable checkpoint**; these bytes are not rewritten. This is a gate/evidence-layer
recheck, **not** a `ccf-paper-reviewer full` manuscript review.

## Result

Step-3 precondition (**substantive new positive scientific evidence**) unmet ⇒ no new
manuscript copy, no 9-page compliant compilation, no fresh isolated full review.
**0 papers qualified, no COMPLETE**; governing unchanged (R95 = 6.0 / Confidence 4.0),
`NOT_QUALIFIED` / `INCOMPLETE`; G0 pending; zero gate promotion / zero self-certification
/ zero state change. Stop gates remain only (1) qualify (>= 7.0) (2) goal owner stops.
A checkpoint `completed` is work state, not scientific validation.

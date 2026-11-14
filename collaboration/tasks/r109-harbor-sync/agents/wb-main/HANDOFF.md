# HANDOFF — wb-main / r109-harbor-sync

- Task / agent / branch: `r109-harbor-sync` / `wb-main` /
  `agent/r109-harbor-sync/wb-main`
- Status: **in_progress** (24 checkpoints published; R126 full-open research archive uploaded; research itself unfinished)
- Last update: 2026-11-14 18:2x +0800 (R126 owner-instructed full-open upload of 233 research files; twenty-fourth checkpoint)
- Protocol: `collaboration/PROTOCOL.md` v1; `collaboration/PROJECT.md`
- Repo: `ZtL-sysu/fly-connectome-control-ladder` (public)

## Completed

- **R126 full-open research archive (latest, twenty-fourth checkpoint).** Per
  the owner's 2026-11-14 instruction, `research/` now holds **233 files /
  ~8.6 MiB** of actual outputs, progress and ideas: manuscripts (TeX/PDF),
  real 10-seed metrics, **all 23 review reports in full**, guidance and frozen
  protocols, D1 proposals and independent reviews, the complete
  `goal-ledger.md` and daily work logs, R106–R125 round audits, and the harbor
  trial. `research/UPLOAD-MANIFEST.json` gives per-file SHA-256. Text is no
  longer redacted ("open 就对了"). Large weights/datasets and files with a real
  credential value remain excluded. `AGENTS.md`, `PROJECT.md`, `TASK.md` were
  updated to the new scope; R110–R113 coverage gap explained (R112/R113 were
  read-only concurrency-guard rounds with no substantive output). See
  `checkpoints/20261114T102224Z-r126-full-open/`.

- **R125 isolated independent recheck RECOVERED + append-only corrections (latest,
  twenty-third checkpoint).** The twenty-second checkpoint truthfully stated AT ITS
  WRITE TIME that a fresh isolated recheck had been launched but was NOT yet recovered
  and claimed no conclusion; its `CHECKPOINT.md` mtime `17:38:35` precedes the report
  `17:42:59`, so that statement was TRUE and its bytes are NOT rewritten. Fresh isolated
  sub-agent `general-purpose-1`, **no expected verdict / score anchor / conclusion
  anchor**: final `R125-INDEPENDENT-REVIEW.md` **14,138 B / 94 lines / SHA-256
  `15b5879315ed9c784c19dadc16b88c52365291dbe25d1a6bc2a6b2c6f482dcdf`** (mtime 17:42:59,
  one write, no intermediate state, original unchanged).
  `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO |
  Forward pass performed: NO`. Reviewer used ONLY 13 raw byte files + R124's two frozen
  authority files with its own logic (no collector/verifier import, no round JSON as
  substantive data source, round audit read LAST), ran no verifier / validator / guard /
  git / network, modified no existing file; 0 scored-verdict lines / 0 email literals /
  0 credential values. **A-H all group values reproduce** (13 sizes+SHA, 135,063 B,
  5 x 17 B Cloudflare 1015 one digest, EPMC lite N-flags, both 500 bodies, EPMC core
  metadata + 4,847-char abstract + 5 negative wordings + four v1-positive numbers
  total 0, bioRxiv 12 records / string '1'..'12' / 1 abstract / 2 titles / **10
  distinct jatsxml URLs** / 1 licence / v3=v4 + v8=v9 collisions, Wayback `[]` +
  no-snapshot page, api-jats 404, both byte-identity checks, scope/safety).
  **12 named overclaim categories CONFIRMED 0 / REFUTED 12**; defects **HIGH 0 /
  MEDIUM 1 / LOW 1**; **1 factual error / 1 data inconsistency (same line) / 0
  fabrication**. **Five findings ALL ACCEPTED append-only** in NEW primary
  `R125-POST-REVIEW-CORRECTION.md` (9,234 B, SHA prefix `42506bff7a15e89b`): **M1
  [MED]** round audit `:41` "all 13 <= 58,714 B" false (byte-max **64,741 B**);
  reviewer read a **pre-correction snapshot** - main session had independently found
  the same error via byte-wise max during `metrics.csv` generation and corrected it in
  place in this round's OWN unpublished drafts BEFORE publication (22nd CHECKPOINT.md
  mtime 17:38:35 < report 17:42:59, so published bytes were already correct); impact
  strictly one derived aggregate in a local unuploaded draft, no frozen byte rewritten,
  reviewer NOT claimed wrong. **L1 [LOW]** frozen verifier's `noEmail` check requires
  BOTH `@` and `.com` => silent false negative for the two `.org` strings; independent
  domain-agnostic recheck `R125-EMAIL-RECHECK.py/.json` finds **occurrences=2,
  distinct=1 (a single public Internet Archive contact address (`.org` domain, redacted here))** in `wayback-v1.html`; strictly a cited-checker
  weakness (audit's own safety claims independently confirmed true; no published
  document claims zero email literals in raw; the word `email` in the 22nd checkpoint
  is only an upload-set scan category; all 13 raw NOT uploaded; public IA contact,
  not a project credential); frozen verifier NOT rewritten, 93/93 stays reproducible.
  **C1** `connect-jats.xml` is actually a bioRxiv **about-page HTML**, NOT JATS, has
  no abstract => strengthens "duplicate, not a new source" and "endpoint +1 != source
  +1". **C2** similarity `0.9906` is specific to `difflib.SequenceMatcher(None,
  biorxiv_api_abstract, epmc_core_abstract).ratio()` with default autojunk and that
  argument order; reviewer got 0.8997 reversed, 0.9945 autojunk-off, 0.9953-0.9978
  normalised - all SAME qualitative conclusion; must declare order + normalisation
  (R122 C-1 / R124 M1). **C3** status codes are declared curl values (no literal 429
  / 404 in raw bodies); Wayback page has no literal `404`; reviewer cannot verify
  independent re-fetch or workspace-level counts / governing / gates / SHAs / mtimes /
  history - collected separately by the main session. **Reviewer scope limits
  accepted**: statuses declarative, group A same-host identity, verifier not run so 93
  checks checked for category + self-consistency only. **Scope of impact**: all five
  are wording / convention / supplementary-fact narrowings, NONE adds a claim; none
  changes 13 raw bytes/SHA, SOURCE-MANIFEST, v3 **93/93 MATCH / 0 MISMATCH**, A-H,
  12 REFUTED 12, double gate (`NOT_QUALIFIED / 6.0 / >=7.0`, `INCOMPLETE`), gate state
  (G0 pending, G1-G8 pending, `inputs=[]`/`evidence=[]`), governing **R95 = 6.0 /
  Confidence 4.0**, **0 papers qualified / no COMPLETE**, R106 section 6 convergence
  table, or heartbeat ACTIVE schedule. **Independent-review original NOT uploaded**
  (1 local-path literal + scan-pattern literals; R117 precedent) - only
  `evidence/R125-INDEPENDENT-REVIEW-SANITIZED.md`. Result: step-3 precondition
  (substantive new positive scientific evidence) unmet => no manuscript copy / no
  9-page compilation / no fresh full review. **0 papers qualified, no COMPLETE**,
  governing unchanged; G0 pending; zero gate promotion / zero self-certification /
  zero state change. Stop gates only (1) qualify >=7.0 (2) goal owner stops.
  Checkpoint `completed` is work state, not scientific validation.


- **R125 version-attribution first-hand route exhaustion (latest, twenty-second
  checkpoint).** Read-only, NOT a gate pass / scientific result / forward pass.
  Motivation: R124's own isolated-review correction **M3** narrowed the "v1 page
  (positive)" abstract to a **WebFetch transcription with NO local byte freeze**; R124's
  hand-off grouped "whether to fetch v1 bytes" with "classification / registration" and
  passed all to a designated gate owner. R125 executes **only** the autonomous half
  (first-hand byte acquisition) and leaves classification / registration / matrix
  finalisation / pass-criterion freezing to the gate owner (G1 / G4 / G6 / G7).
  **New route never tried before**: the bioRxiv official details API publishes a
  per-version `jatsxml` URL for each of its 12 version records; R124 had tried only the
  `.full` HTML v1 path (4 x 429). Also exhausted EBI Europe PMC full text, Internet
  Archive Wayback, and a hypothesised `api.biorxiv.org` JATS endpoint.
  **13 raw files / 135,063 B**, each frozen verbatim + SHA-256; largest 64,741 B.
  5 x HTTP 429 / 17 B `error code: 1015` (official per-version JATS v1/v3/v12 variants,
  all five sharing one digest); 2 x HTTP 500 / 150 B (EPMC `fullTextXML`); 1 x HTTP 200
  / 6,367 B (**EPMC `resultType=core` = new third first-hand endpoint**); CDX `[]` +
  Wayback 404; `api.biorxiv.org/jats` 404; details `/1` 200 byte-identical to R124's
  un-suffixed response (independently reproduces "/1 is not a version selector");
  connect page 200 byte-identical to R124 frozen copy (duplicate, not a new source).
  **Substantive findings**: (1) EPMC core `abstractText` 4,847 chars, similarity
  **0.9906** to the bioRxiv API abstract (4,816 chars), all 22 diff ops typographic /
  whitespace / hyphen / comma / name-transliteration normalisation, no semantic
  difference; carries `largely null result` / `disappears entirely` /
  `statistically indistinguishable` / `size-matched` / `not the confirmation we set out
  to find`; the four "v1 positive" numbers `0.686 / 0.846 / 0.930 / 0.603` occur
  **zero** times. Per R124 M2/M3 the same abstract at several endpoints is NOT several
  independent sources => **endpoint count +1, independent-source count unchanged**, no
  version-attribution claim; R124 M3 narrowing is **strengthened, not overturned**.
  (2) From R124 frozen API bytes: `version` is a **string** `'1'..'12'`; **12 records
  share ONE abstract** and **2 distinct titles** (v1 differs from v2-v12); but
  `jatsxml` has only **10 distinct URLs** - v3/v4 both `2026-06-23`, v8/v9 both
  `2026-06-30` => even with 429 cleared and all JATS full texts retrievable, **two
  version pairs remain indistinguishable at the official endpoint**. Endpoint-side
  structural limit, not a rate-limit artefact. All 12 `license=cc_by` and EPMC
  `license="cc by"` are **record-level metadata**, NOT per-asset licence text (R123
  lesson), do NOT close gap 1. (3) EPMC 500 is **structural**: lite + core agree
  `hasPDF=N / inEPMC=N / inPMC=N / isOpenAccess=N`, `fullTextUrlList` has exactly one
  DOI-resolver entry => EPMC holds no full text, not a retry candidate. Index dates
  are NOT the current abstract's version. (4) **Negative conclusion reported as
  such**: the "v1 page no local byte freeze" gap remains OPEN; the "v1 positive vs
  current negative" dichotomy still has no first-hand byte support; **R3 stays OPEN**;
  no R106/R124 byte rewritten; acquisition completion is NOT gap closure.
  **Time-point/scope limits**: all 429/500/404/empty-CDX results scoped strictly to the
  R125 acquisition instant (~17:0x +0800) and exact URLs/hosts; 429 is Cloudflare 1015
  host-side rate limiting, NOT permanent unavailability (R124 got 200 from
  api.biorxiv.org / connect.biorxiv.org the same day and reported an unsaved 200 /
  105,400 B v1 HTML response); CDX query used `statuscode:200`, `limit=5`, one URL form;
  char counts / similarity bound to specific derived files with declared normalisation.
  **Reproducibility**: `R125-verify.py` does not import the acquisition module and uses
  no R125-produced JSON as a substantive data source - recomputes from 13 raw byte
  files + R124's two frozen authority files: **93 checks / 93 MATCH / 0 MISMATCH**
  (A27 B6 C10 D24 E14 F4 G2 H6). Group A is a same-machine byte-identity consistency
  check, not independent cross-source verification; SHA literals from a separate
  `shasum -a 256`, none invented. Two verifier defects retained and reproducible, both
  script / expectation defects (NOT data inconsistency, NOT fabrication): **V-1** v1
  `bytes` not JSON-serializable -> `TypeError`; **V-2** v2 expected `version` as ints
  but API returns strings -> `91/92 MATCH, 1 MISMATCH (E-versions)`; v3 fixes both +
  adds explicit field-type check -> 93/93. v1/v2 files and v2 VERIFICATION kept.
  Three further self-caught corrections in this round's OWN unpublished drafts, all
  logged: v2 reproduction overwrote final VERIFICATION (restored by v3 re-run);
  `Path('.').parent` resolution in the metrics generator; "largest file 58,714 B"
  corrected to **64,741 B** by byte-wise max computation. No frozen byte / historical
  checkpoint changed. **Double gates (read-only)**: validator `NOT_QUALIFIED / 6.0 /
  >=7.0 / score_meets_threshold=false`; guard `INCOMPLETE` (A2/A6); seven structural
  authorities byte-identical before/after; mainline G0-G8/validation/handoff all
  pending, `G0.inputs=[]`/`evidence=[]`. **Boundary**: zero forward / training /
  labels / dataset / EPE-l2 / scientific metrics, zero gate promotion, zero
  self-certification, zero stage change; no `ccf-paper-reviewer full`, no scored-verdict
  line, no v4, no gate skipping, no <=32h/K=45 assumption, no 4090/L4/H20 claim;
  D1 stays `BLOCKED_ON_CONFIRMATION`. **Fresh fully isolated independent recheck
  launched (no expected verdict / score anchor / conclusion anchor); at this
  checkpoint's write time NOT yet recovered and NO recheck conclusion claimed** -
  that statement is TRUE at write time, these bytes are not rewritten, and the
  recovered conclusion / any append-only corrections go to a NEW immutable checkpoint
  per R117/R119-R124. Gate/evidence-layer recheck, NOT a full manuscript review.
  Result: step-3 precondition (substantive new positive scientific evidence) unmet =>
  no new manuscript copy / no 9-page compilation / no fresh full review. **0 papers
  qualified, no COMPLETE**, governing unchanged R95 = 6.0 / Confidence 4.0,
  `NOT_QUALIFIED` / `INCOMPLETE`, G0 pending, zero gate promotion / zero
  self-certification / zero state change. Stop gates only (1) qualify >=7.0 (2) goal
  owner stops. Checkpoint `completed` is work state, not scientific validation.


- **R124 isolated independent recheck RECOVERED + append-only corrections (latest,
  twenty-first checkpoint).** Fresh isolated sub-agent `general-purpose-1`, **no expected
  verdict / score anchor / conclusion anchor**: final `R124-INDEPENDENT-REVIEW.md`
  **28,602 B / SHA-256 `76abf752a8ea1fb57804400d05c6ef8baff168a4cb07455fb03cf5c2584a5293`**
  (mtime 15:47, one write, no intermediate state, original unchanged).
  `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO |
  Forward pass performed: NO`. Reviewer used ONLY the 13 raw byte files with its own logic
  (no collector/verifier import, no round JSON as substantive data source, round audit read
  LAST), ran no verifier / git / network, modified no existing file; 0 credential values /
  0 scored verdict lines / 0 emails. **66 checks / 66 MATCH / 0 MISMATCH** (A7 B12 C12 D5
  E6 F3 G7 H8 I6); all first-hand numbers independently reproduced by byte summation.
  **12 named overclaim categories CONFIRMED 0 / REFUTED 12**; defects **HIGH 0 /
  MEDIUM 3 / LOW 3**, 0 fabrication / 0 data inconsistency / 0 fact error. **All six
  defects ACCEPTED append-only** in NEW primary `R124-POST-REVIEW-CORRECTION.md` (9,718 B,
  SHA prefix `1405ed027e3151902ccd`): **M1 [MED]** `:29` zero-local-path claim lacked an
  explicit file set (group I scoped to 13 raw files, 0 hits; this round's guard-readout copy
  has 13 local-path literals, local-only and NOT uploaded) => narrowed to a file-set
  declaration, not a factual misstatement. **M2 [MED | substantive narrowing]** ":55 three
  INDEPENDENT first-hand byte sources including the mirror body" conflicted with the audit's
  own 'mirror always second-hand'; all three are renderings of the SAME current abstract =>
  corrected to ONE current abstract at **2 first-hand endpoints** (bioRxiv details API,
  Crossref work API) **+ 1 second-hand mirror endpoint**, mirror cross-corroboration only,
  NOT 3 independent sources. **M3 [MED | substantive narrowing]** "12 versions" + "v1
  positive vs v12 scope" was not fully consistent with the round's own negative conclusion;
  v1 positivity came only from an un-saved WebFetch transcription (`0.686` etc. total 0 in
  raw bytes), and 'v12 scope' attributed one abstract backfilled into all 12 records to a
  single version => corrected to **12 version RECORDS sharing ONE abstract** (not 12
  distinguishable abstracts), **v1 page abstract = WebFetch transcription with NO local
  byte freeze, NOT a first-hand conclusion**, and **'current abstract scope' with no
  version attribution** (mirror `datePublished` only a time-point corroboration); R3's
  negative conclusion (v3 not the turning version, no attribution for the middle ten) is
  unchanged and now more explicit; no R106 byte rewritten. **L1 [LOW]** `:16` "19 lines /
  19 files" had no counting scope; strict line-start numeric Overall = **15 lines /
  13 files** (incl. provenance/isolated byte-identical copies), **excluding copies =
  12 lines / 10 files**; '19' was the file count WITHOUT the numeric constraint
  (same class as R121 J-1). Core `new_governing_candidates=0` unchanged. **L2 [LOW]** `:27`
  "first-hand freeze (13 files)" included 2 second-hand mirror files => narrowed to "13 raw
  byte files, 2 second-hand mirror endpoints for cross-corroboration only"; 323,740 B / 13
  unchanged. **L3 [LOW]** `:90` "/tmp report not in project tree" is true for the original
  `guard check -o`; a read-only `R124-GUARD-READOUT.txt` (4,871 B) copy was later cp'd into
  the round dir as a reading trace, identical and not uploaded. **Clarification**: the
  reviewer's 'concurrent write' observation (`R124-VALIDATOR-READOUT.json` at 15:26:29
  after audit 15:25:58) was produced by the main session itself 31 s later, not an
  external session; raw/ mtimes stable, reviewer stated conclusion unaffected. **Reviewer
  scope limits accepted** (HTTP statuses declarative; group A same-host identity; reviewer
  did not run verifier so 145/145 checked for consistency only; v1 HTML 105,400 B first
  probe unverifiable; concurrency guard / ledgers / pipeline-state read independently).
  Pre-existing 7 v1 script/expectation defects independently confirmed correctly
  classified, both versions retained. **All six are wording / scope / attribution
  narrowings**: none changes 13 raw bytes + SHA, SOURCE-MANIFEST, v2 **145/145 MATCH / 0
  MISMATCH**, 66/66, 12 categories REFUTED 12, either gate reading, gate state,
  governing, 0 qualifying papers, R106 section 6 convergence, or heartbeat schedule.
  Independent report original **NOT uploaded** (R117 precedent: local absolute-path
  literals + scan-pattern literals), only `evidence/R124-INDEPENDENT-REVIEW-SANITIZED.md`.
  **Twentieth checkpoint** truthfully claimed at its write time 'recheck launched, not
  recovered, no verdict claimed'; its bytes are NOT rewritten. Gate / evidence-layer
  recheck, **NOT** `ccf-paper-reviewer full`: no scored verdict line, no numeric paper
  score, no governing change. A checkpoint `completed` is work state, not scientific
  validation.

- **R124 heartbeat: R106 section 6 R3 / R5 first-hand text acquisition (latest,
  twentieth checkpoint).** Concurrency guard NOT triggered (primary ledger mtime
  14:04:15 = ~64.8 min stale > 10 min; no main research session / polling process;
  zero project writes in preceding 12 min; newest full review still r95 / 11-11;
  19 line-start numeric scored-verdict lines all historical reports or byte-identical
  copies, 0 unregistered async full reviews; no R124 artifacts at wake; governing still
  6.0). **Direction change**: NOT a 9th process dossier (R105/R107/R109 halted that loop;
  R121's negative closure from the governing review's own section 13 still holds). R122
  closed R4 acquisition, R123 closed R1 acquisition; this round closes the LAST TWO
  R106 section-6 items not requiring a gate-owner ruling: **R3** (2026 geometry study
  first-hand source, version marking, verbatim recheck of the p<10^-13 / trained-ER /
  OFF-closure claims, secondary-mirror status) and **R5** (first-hand byte verification
  of W5/W8 corrections), plus the FIRST per-item convergence table for R1-R9. 13
  third-party PUBLIC small texts frozen (8x200 / 1x301 / 4x429 Cloudflare 1015 preserved
  as negative evidence, 323,740 B total, largest 64,741 B, SHA-256 anchored).
  **Substantive first-hand findings (third-party text facts, NOT project results)**:
  (1) bioRxiv official details API returns **12 version records** for DOI
  10.64898/2026.06.10.731214 (v1 2026-06-12 -> v12 2026-10-16); v1 title differs from
  the v2-v12 title (identical across all 11 later records). (2) **All 12 `abstract`
  fields are byte-identical** (4,816 chars, SHA prefix 555e28f9fef3), each verbatim
  containing `p < 10-13 in every case`, `closes the gap completely`,
  `trained Erdos-Renyi on OFF-polarity structure` => the API abstract is a CURRENT
  abstract backfill into every version record, NOT a per-version historical abstract.
  (3) An early probe of the v1 HTML page returned HTTP 200 / 105,400 B but was NOT saved;
  its abstract was POSITIVE (RSA Spearman r=0.686 / 0.846 / 0.930 vs 0.603) without the
  three negative phrases; four later probes all 429 => **NO local v1 page byte freeze**,
  the positive abstract is a WebFetch transcription only, explicitly NOT a first-hand
  frozen artifact. (4) Crossref abstract is likewise the negative version but
  created=2026-06-12 (v1 date), title is the v2+ title, indexed=2026-10-21 =>
  metadata-layer version mismatch. (5) Second-hand mirror datePublished=2026-10-16
  equals API v12 date and its body verbatim has all three negative phrases => v12 scope;
  R106 recorded that URL as Cloudflare-blocked, this round got HTTP 200 / 37,429 B after a
  301 => TIME-POINT / ENDPOINT difference, NOT a claim R106 fabricated anything; the
  mirror remains second-hand, used only for cross-corroboration. (6) **Strict scope for
  R3**: R106's 'v1 positive vs v3 largely negative' version marking is UNSUPPORTED by the
  first-hand bytes (v3 is one of 12 records; the API supplies no per-version abstracts;
  the first appearance of the negative conclusion cannot be determined from local bytes).
  Narrowed to: v1 page (positive, no local bytes) vs current/v12 scope (negative, three
  independent first-hand byte sources); the middle ten versions' abstracts not obtained,
  no version attribution claimed. R106's central W6 finding still stands, NO R106 byte
  rewritten. (7) R5: first-hand arXiv abs pages verbatim contain 22871090 (1 hit) /
  22891264 (0), and 9 Oct 2026 (2) / 12 Oct 2026 (0) => both W8 corrections confirmed;
  W5 already appended-only withdrawn inside R106's own round audit and byte-confirmed in
  R122, NOT duplicated, NO historical byte rewritten. **R1-R9 convergence**: all
  autonomously completable items (R1/R3/R4 acquisition + R5 byte verification) are now
  EXHAUSTED; every remaining item (R2 matrix finalization, R6 gate judgment, R7 state
  registration + pass criterion, R8 refreeze, R9 fresh recheck) sits behind a designated
  gate owner, converging exactly on R120's minimal set G1+G4+G10. **Independent verifier**
  (no collector import, no round JSON as substantive data source): **145 checks / 145
  MATCH / 0 MISMATCH** (A 45 / B 27 / C 14 / D 10 / E 6 / F 9 / G 16 / H 12 / I 6);
  group A is a same-host necessary-consistency check, NOT independent cross-verification.
  v1 verifier and its 145/141/4 output RETAINED verbatim; 6 v1 script/expectation defects
  + 1 acquisition defect (unsaved HTTP 200 page) documented, 0 data inconsistency,
  0 fabrication, 0 report fact error. **Acquisition complete is NOT gap closure**.
  Read-only double gate: validator NOT_QUALIFIED / 6.0 / >=7.0 / score_meets_threshold=
  false (D1 pass D2 fail D3 fail D4 pass D5 fail); guard INCOMPLETE (A2/A6, S1-S7 all
  pending, 0 action entries), guard ledger SHA unchanged => read-only; main-line 12
  stages, CCFA-startup=passed, G0-G8/validation/handoff all pending, G0 inputs=[]
  evidence=[]. **Strict boundary**: zero write-back to pipeline-state.json /
  literature-baseline-matrix.md / source-manifest.json / primary ledger (collection
  time) / any gate config, all byte-unchanged; zero gate promotion (G0 pending), zero
  self-certification, zero state change; EXEC LOCK zero forward / inference / training /
  labels / dataset / EPE-l2 / scientific metric / new positive evidence, network only for
  read-only acquisition; no review / score / threshold / manuscript / gate / frozen
  artifact / registry change; no ccf-paper-reviewer full, no numeric **Overall:** line,
  no self-authored governing review, no v4 contract, no P3 while G0 pending, no
  <=32h/K=45 authorization assumption (D1 stays BLOCKED_ON_CONFIRMATION), no 4090/L4/H20
  claim; primary project no submission / commit / push. **Increment is evidence-layer,
  NOT score-layer** (R121 negative closure): a first-hand literature freeze does NOT
  change governing 6.0, explicitly NOT presented as progress toward qualifying. Fresh
  isolated sub-agent LAUNCHED with NO expected verdict / score anchor / conclusion anchor;
  **at checkpoint write time NOT recovered, so NO recheck conclusion is claimed** -
  recovery + append-only corrections go to a NEW immutable checkpoint, these bytes not
  rewritten. NO raw file uploaded (R117/R119/R120/R121/R122/R123 precedent), only
  evidence/R124-R3-R5-FIRST-HAND-SANITIZED.md. Full-repo strict pattern scan 0 new
  hits; no >50 MiB / binary / dataset / weight / third-party source / unpublished
  manuscript. Strict `git add --` explicit files only; 19 earlier published checkpoints
  untouched; private ZtL-sysu/novix-platform untouched; no merge / force / branch
  deletion / Release. **Result unchanged: 0 papers qualified, no COMPLETE, governing
  R95 = 6.0 / Confidence 4.0, NOT_QUALIFIED / INCOMPLETE, G0 pending; heartbeat ACTIVE
  unchanged.** A checkpoint `completed` is work state, not scientific validation.

- **R123 isolated independent recheck recovered + append-only corrections (latest,
  nineteenth checkpoint).** The eighteenth checkpoint truthfully stated that the recheck was
  launched but not recovered and claimed no verdict; its bytes are **not rewritten**. Fresh
  isolated sub-agent `general-purpose-1` (no expected verdict / score anchor / conclusion
  anchor): final `R123-INDEPENDENT-REVIEW.md` **16,565 B / 105 lines**, SHA-256
  `40edc181845f5d5086e7ee3dc71c6515861d2061c41be8d688301f45cb744408`, one write, mtime
  13:57, original unchanged. `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific
  result claimed: NO | Forward pass performed: NO`. Reviewer recomputed from the 13 raw byte
  files with its own logic (no collector/verifier import, no round JSON as data source, round
  audit read LAST), ran no verifier / git / network, modified no existing file; 0 credential
  values, 0 scored verdict lines, 0 score anchors. **A–F 6 MATCH / 0 MISMATCH**; **12 named
  overclaim categories CONFIRMED 0 / REFUTED 12**; defects **HIGH 0 / MEDIUM 1 / LOW 1**,
  fabrication 0. **Both defects accepted append-only** in primary
  `R123-POST-REVIEW-CORRECTION.md`: **W-1 [MEDIUM | fact error, NOT fabrication]** round
  audit section 3 wrote the six Zenodo files as `152,578` bytes; byte-exact recount is
  **152,628** (50 B delta). Main-session recount 10,603 + 131,225 + 4,061 + 2,615 + 2,267 +
  1,857 = 152,628; four-group total **262,728** matches the heading, manifest and reviewer's
  A-group recount. Impact scoped to one derived summary number — no propagation to raw bytes,
  SHA, either verifier reading, machine gates, gate state, governing, A–F or the 12 rulings;
  round audit and eighteenth checkpoint not rewritten. **W-2 [LOW | scope]** "zero local
  paths" was not limited to the 13 raw frozen files; those 13 do have 0 hits (A/F unaffected),
  but two same-directory guard outputs and the independent report contain local
  absolute-path literals — corrected wording limits the claim and states those files are
  local-only, not uploaded. Pre-existing V-1 confirmed correctly classified, not a new
  defect. Independent report original **not uploaded** (contains local path literals); only
  `evidence/R123-INDEPENDENT-REVIEW-SANITIZED.md`. Gate / evidence-layer recheck, **not** a
  full manuscript review; no scored verdict line. All machine-gate readings, gate states,
  governing (R95), `0 qualifying papers`, `no COMPLETE`, zero forward pass / zero scientific
  result / zero state write-back, and the heartbeat schedule are unchanged.

- **R123 gap-1 first-hand licence / code-path text acquisition (latest, eighteenth
  checkpoint).** Executed the standing step-1 item 1 (goal-owner authorized): R106 section 6
  R1 / R98 gap 1, which the R106 gate review flagged verbatim as "no LICENSE text was read"
  and the R120 decision register listed as a remaining first-hand item undone for 11+ rounds.
  This is **not** a ninth process dossier — R121's negative closure (from the governing
  review's own score-change rule) still holds. 13 third-party public small texts frozen
  (all HTTP 200, 262,728 B, each < 200 KB), SHA-256 anchored, 200 KB hard size cap, no
  dataset / weights / binary / large file / local path / project credential. One official
  upstream script embeds a hard-coded **third-party public** API-key literal: marked
  `upload_to_public_repo=false`, local only, `<redacted>` in every derivative; **no raw file
  uploaded**, only `evidence/R123-GAP1-LICENCE-SANITIZED.md`. Independent verifier (no
  collector import, no round JSON as data source for substantive claims): **91 checks / 91
  MATCH / 0 MISMATCH**; group A declared same-machine byte-identity, not independent
  cross-verification. A v1 wrong expected value (assumed 20 MANIFEST rows; true 18 from the
  18/19/20 self-reference nesting) is retained verbatim with both scripts and both readings —
  an expectation-assumption error, not a data inconsistency. Substantive findings are
  **third-party text facts, not project results**: Zenodo 21549559 record-level CC BY 4.0
  statement + README `Licence and attribution` (NOT 18 per-asset licence texts; upstream
  claim is a transcription, not independently verified); Sintel official licence is a **custom
  MPI non-commercial scientific-research licence, not CC BY** (`CC BY` / `Creative Commons`
  each 0 mentions); official flyvis code is MIT but weights go through a Google Drive folder
  with **zero** independent weight licence text (code licence is not weight licence, terms
  remain OPEN); FlyHack code path negative evidence (abs page 0 github.com / 0 Zenodo, one
  repo search `total_count=0`), scoped to that query. **Acquisition complete is NOT gap 1
  closed**: R1 requires matrix correction + freeze, R6/R7 a designated gate owner's explicit
  judgment and recorded pass, R9 a fresh independent recheck; matrix/registry disposition
  belongs to decision groups G5/G6/G7/G4. Primary baseline matrix, source manifest,
  pipeline state, and ledger byte-unchanged. Read-only machine gates: validator
  `NOT_QUALIFIED / 6.0 / >=7.0`, guard `INCOMPLETE` (A2/A6); guard ledger SHA unchanged.
  Zero gate promotion (G0 pending), zero self-certification, zero state write-back, zero
  forward pass / training / dataset / scientific metric / new positive evidence. No
  `ccf-paper-reviewer full`, no scored verdict line, no v4, no P3 while G0 pending, no
  `<=32h / K=45` authorization assumed, no 4090/L4/H20 claim. Primary project: no
  submission / commit / push. A fresh isolated sub-agent was **launched** with no expected
  verdict / score anchor / conclusion anchor; at checkpoint write time it was **not
  recovered**, so **no recheck conclusion is claimed** — recovery and append-only corrections
  go to a new immutable checkpoint. Result still **0 qualifying papers, no COMPLETE**.

- **R122 isolated independent recheck recovered + append-only corrections
  (latest, seventeenth checkpoint).** The sixteenth checkpoint truthfully
  claimed no verdict while the fresh isolated sub-agent was running; its
  bytes are **not rewritten**. Final independent report (primary project,
  **not uploaded** per R117 precedent): **24,434 B**, SHA-256
  `bcc78c27ab05ccee699199f8c01899f4a6bd912a6e24202a82397df080cace4e`,
  one write, mtime 12:25:48, original unchanged. Verdict
  `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result
  claimed: NO | Forward pass performed: NO`. Reviewer used only the five raw
  byte files with its OWN parsing logic (no collector/verifier import, no
  R122 JSON as data source), read the round audit LAST. A-F **57 MATCH / 3
  MISMATCH** (A 13/0, B 6/0, C 8/0, D 9/2, E 19/1, F 2/0); **12 named
  overclaim categories CONFIRMED 0 / REFUTED 12**; **defects HIGH 0 /
  MEDIUM 0 / LOW 2**, 0 fact error / 0 data inconsistency / 0 fabrication;
  0 expected-score or score-anchor tokens in the report. **3 MISMATCHes all
  accepted as reviewer parsing-scope differences, not report errors**: v2
  body abstract 1,943 vs 1,938 (naive 1,941) and similarity 0.4717 vs 0.4724
  (naive 0.4719) come from inline-formula `46x` rendering (LaTeX alttext vs
  MathML glyphs + annotation); the **38 diff opcodes are identical under all
  four scopes**; plaintext 45,960 vs 45,430 / 46,545 is whitespace
  normalization degree. Reviewer measured each derived artifact itself and
  confirmed the report values are accurate for their own artifacts. Reviewer's
  own script defect retained verbatim: initial `str.find()` for `What remains
  open` sliced into the TOC (`False / 18 chars`), fixed with `rfind()` to
  `True / 561 chars`. **2 LOW defects all ACCEPTED, append-only** in a NEW
  primary `R122-POST-REVIEW-CORRECTION.md`: **C-1 [LOW | wording]** the
  section 8 quotation at `R122-ROUND-AUDIT.md:75` labeled "verbatim" is a
  MathML-cleaned rendering, not a contiguous byte substring of the derived
  plaintext (which has `+ 0.033 +0.033 [ 0.015 , 0.050 ] [0.015,0.050]`) =>
  narrowed to "numeric tokens verbatim-matchable; full sentence after
  whitespace/MathML normalization"; all tokens (verifier E5/E6) and the
  section 8 conclusion unchanged. **C-2 [LOW | scope]** `:60` "37 / 16
  section headings" is correct under "all h1-h6 tags minus modal title and
  Abstract pseudo-heading" but includes the h1 document title, six h4
  subheadings and bibliography heading without declaring the counting scope;
  reviewer's section/subsection count is v1 14 / v2 28, and **v2 > v1 holds
  under every scope**. Reviewer explicitly found NO time-point / scope-mixing
  defect and noted the report's separation of feed query time from
  entry-level version times as a strength. Additional first-hand facts:
  v1/v2 `citation_title` differ while `citation_date` = 2026/09/21 for both
  (`citation_online_date` distinguishes 09/21 vs 09/22); the atom opaque
  query id is NOT a credential; 5 raw byte files have 0 local-path /
  credential-style hits. Reviewer's scope limitation accepted (concurrency
  guard, ledgers, pipeline-state readings, "all HTTP 200" not verifiable from
  the 5 raw byte files alone; no truth claim made). **No historical artifact
  and not the independent report itself was rewritten**: round audit,
  independent review, verification JSON, source manifest, all 5 raw byte files
  and the sixteenth checkpoint byte-unchanged. Gate/evidence-layer recheck,
  **NOT** `ccf-paper-reviewer full`: no scored-review Overall line, no numeric
  paper score, no governing change. Independent report original **NOT
  uploaded** (R117 precedent: only sanitized summaries), only
  `evidence/R122-POST-REVIEW-SANITIZED.md`. **Result unchanged: 0 papers
  qualified, no COMPLETE, governing R95 = 6.0 / Confidence 4.0,
  `NOT_QUALIFIED` / `INCOMPLETE`, G0 pending; heartbeat ACTIVE unchanged.**

- **R122 R106 section 6 R4 first-hand source freeze (latest, sixteenth checkpoint).**
  Direction change: no ninth process dossier (R105/R107/R109 halted that loop;
  R121 proved from the governing review's own section 13 rules that read-only
  audits cannot raise the evidence-capped Overall). Instead closed the
  *evidence-acquisition* half of R4 — repeatedly named in R106/R107/R118/R120,
  undone for 11 rounds — with 5 SHA-anchored raw byte files for
  `arXiv:2609.24565` v1/v2 (abs pages, HTML full text, atom API), all HTTP 200.
  **Substantive first-hand finding (third-party version fact, NOT a project
  result)**: the same v2 carries two materially different official abstracts —
  abs/API (1,534 chars) vs HTML body-embedded (1,943 chars), similarity
  **0.4717**, 38 diff opcodes; the abs/API one contains the time-scale sweep
  conclusion, the body one does not. v1 differs from both in abstract and
  title. v2 section 7.3 / section 8 `+0.033 [0.015,0.050]` / "Two gaps
  remain." / section 9 all verified verbatim from raw bytes, supporting
  R106's G4 positioning. Atom **feed-level** `updated` is query time,
  explicitly separated from **entry-level** version times (abs Submission
  history agrees). Independent verifier recomputes from raw bytes without
  importing the collector or reading any R122 JSON: **47 / 47 MATCH / 0
  MISMATCH**; A1-A4 declared same-host necessary-consistency checks, B-F
  substantive observations. **No write-back**:
  `literature-search/source-manifest.json` (R4's register half, decision G7),
  `literature-baseline-matrix.md` (R2/G6) and `pipeline-state.json`
  byte-unchanged; G0 still `pending`. EXEC LOCK zero forward / training /
  dataset / metric; no `ccf-paper-reviewer full`, no numeric scored-verdict
  line, no v4, no P3, no gate skipping. Fresh isolated sub-agent launched with
  **no verdict / score / conclusion anchor**; **at checkpoint write time NOT
  recovered => this checkpoint claims NO recheck verdict, NO defect list, NO
  confirmation**; recovered conclusions + append-only corrections go into a
  NEW immutable checkpoint, these bytes not rewritten. Raw third-party HTML
  (contains an author email) and all primary project artifacts NOT uploaded;
  only `evidence/R122-FIRST-HAND-R4-SANITIZED.md` with `<local>/` masking.
  **Result unchanged: 0 papers qualified, no COMPLETE, governing R95 = 6.0 /
  Confidence 4.0, `NOT_QUALIFIED` / `INCOMPLETE`, G0 pending.** Heartbeat
  ACTIVE schedule unchanged.

- **R121 isolated recheck recovered + append-only corrections (latest,
  fifteenth checkpoint).** The fourteenth checkpoint truthfully claimed no
  verdict while the fresh isolated sub-agent was running; its bytes are **not
  rewritten**. Final independent report (primary project, **not uploaded** —
  quotes 2 local paths): **28,736 B / 237 lines**, SHA-256
  `9650a024f84c9b1ec308db4a96c18fee26e5cfd67e3b73b0b9a50f1a0891200c`, one
  write, mtime 10:42:30, original unchanged. Verdict
  `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result
  claimed: NO`, `Forward pass performed: NO`. A–H **all MATCH**; reviewer
  used **no** R121 JSON as a data source and read the round audit only last,
  for defect grading. **12 named overclaim categories CONFIRMED = 0 (all
  REFUTED)**; **6 items (0 HIGH / 1 MEDIUM / 3 LOW / 1 disclosed snapshot
  observation / 1 scope limitation)**, all accepted **append-only** in
  private `R121-POST-REVIEW-CORRECTION.md`. Most substantive is **J-1
  (MEDIUM)**: "14 numeric scored-verdict lines" was the wake-time (10:03)
  truth; at audit-write time (10:28), after this round's own byte-identical
  `isolated/` copy existed, the count is **15 lines / 13 files** (main
  session re-measured). Both later-than-r95 files are byte-identical to r95,
  `new_governing_candidates = 0`, no new score. J-2/J-3/J-6 are label,
  token-spelling, and paraphrase narrowings; J-4 is the already-disclosed
  capture-time snapshot (corroborates "no historical byte rewritten"); J-5
  is a declared reviewer scope limit (74/74 is same-host consistency, never
  independent cross-validation). Reviewer found **no overclaim** in the
  negative closure finding. Gate/evidence-layer recheck, **NOT**
  `ccf-paper-reviewer full`. Sanitized summary only:
  `evidence/R121-INDEPENDENT-REVIEW-SANITIZED.md`.

- **R121 read-only success-criterion closure audit (latest, fourteenth
  checkpoint).** Lane change: instead of an eighth process-layer dossier, R121
  reconciles the **governing R95 independent full review's own score-change
  taxonomy** (§8/§11/§13/§15, 18 byte-exact needles all matched) against the
  seven R114–R120 rounds, the three "raise score" conditions, the two machine
  gates, and the ordered gate chain. All three raise conditions are
  `satisfied = False` from source bytes: (a) 6 real MaleCNS
  `hypothesis_supported = False` (4 synthetic controlled graphs are `True`,
  the surrogate M1 excludes); (b) version-locked manuscript 40,175 B / md5
  `e4bfad51…158c6` states at line 637 that the flyvis stack was not rerun,
  0 rerun metric files; (c) real visual task MLP baseline 0.97222 dominates,
  real-minus-null delta −0.000463 with CI95 including 0. 7/7 prior rounds
  declare `READONLY…NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`, 0 new positive
  evidence, 0 gate passes, 0 numeric verdict lines. **Negative closure
  finding**: by the governing review's own §13 "No quick change" rule, this
  class of work **cannot** raise the evidence-capped Overall from 6.0 to
  >= 7.0 — a criterion-level impossibility, not slow progress. Validator
  `NOT_QUALIFIED / 6.0 / >=7.0`, guard `INCOMPLETE` (A2/A6, 7 steps pending),
  G0–G8/validation/handoff all `pending` with empty inputs/evidence, zero new
  governing full reviews. Independent verifier: **74/74 MATCH, 0 MISMATCH**;
  21 sources + 21 byte-identical isolated copies; six v1 script defects
  documented and both readings retained. EXEC LOCK, zero gate promotion, zero
  state write-back. **Fresh isolated independent sub-agent launched with no
  expected verdict / score anchor; at checkpoint write time NOT recovered —
  this checkpoint claims NO recheck verdict.** Recovered conclusion goes into a
  new immutable checkpoint; earlier checkpoints are not rewritten. Sanitized
  summary only: `evidence/R121-SUCCESS-CONDITION-SANITIZED.md`.

- **R120 isolated recheck recovered + append-only corrections (latest,
  thirteenth checkpoint).** The twelfth checkpoint truthfully claimed no
  verdict while the fresh isolated sub-agent was running; its bytes are **not
  rewritten**. Final independent report (primary project, **not uploaded** —
  quotes 2 local paths): **23,074 B**, SHA-256
  `c7c613c54bd08cad1b945c5affcdf371522430e63fff84d702ac86625cf3d9ea`, one
  write, mtime 08:55:00, original unchanged. Verdict
  `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result
  claimed: NO`, `Forward pass performed: NO`. A–H/J/L **MATCH**; **I/K
  MISMATCH**; reviewer used **no** R120 JSON as a data source. **12 named
  overclaim categories CONFIRMED = 0 (all REFUTED)**; **7 defects (1 HIGH /
  3 MEDIUM / 3 LOW / 0 fabrication / 0 data inconsistency)**, all accepted
  **append-only** in private `R120-POST-REVIEW-CORRECTION.md`. **W1 (HIGH,
  substantive withdrawal)**: the literal "no newer file with a numeric
  scored-verdict line anywhere" claim is refuted (reviewer 13,704 files →
  647 literal / 109 inline numeric / 14 line-start numeric lines across 12
  files, newer files quoting/copying existing scores), and R120's own field
  was an **empty never-populated placeholder** with no verifier check ⇒ closed
  by a **NEW first-hand recomputation, not a wording patch**:
  `R120-I2-EVIDENCE.py/json` (13,706 files, 662/109/14, plus **39 files / 83
  lines newer than r95**, all quotations/copies); narrowed claim "zero new
  independent full reviews after r95, zero newly produced numeric verdict
  lines" supported by `qualifying_files=[] / supported=true`. W2 "first /
  never" narrowed to a scope observation (R111:26 is a documented prior
  observation); W3 the four R107 restatements are different wording/numbering
  versions (spliced quotation; line numbers 175/175/116/180 correct); W4 the
  **whole** item ② must not be called satisfied — only the "create P0 state /
  no P stages in guidance state" sub-clause exists as a draft scaffold,
  "versioned contract handling of the guidance handoff" unmet (handoff
  pending), and the reviewer confirmed
  `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED` is **accurate, neither overclaim nor
  underclaim**; W5 "12" was a file count (exact 14 lines / 12 files); W6 3
  byte-identical closure copies on disk, evidence set collected 2; W7 R115
  added no new gate-owner decision. None changes any A–H/J byte-level value,
  the non-scientific-result boundary, absence of G0 promotion or governing.
  Sanitized `evidence/R120-INDEPENDENT-REVIEW-SANITIZED.md`; `metrics.csv`
  holds real read-only measurements. **0 papers qualified, no COMPLETE,
  governing still 6.0 / Confidence 4.0, `NOT_QUALIFIED` / `INCOMPLETE`, G0
  pending.** A checkpoint `completed` is work state, not scientific validation.
- **R120 standing-instruction / on-disk-state reconciliation (latest,
  twelfth checkpoint).** Lane change: no machine-gate fix, no Nth G0 text
  patch, no P3 forward pass, no v4 contract. First byte-anchored item-by-item
  reconciliation of the standing heartbeat step-1 list against disk, plus a
  single deduplicated **10-group (G1–G10) external-decision register** with
  exact `file:line` anchors and dependency order; minimal unblocking set
  **G1 + G4 + G10**. Central finding (narrowly stated): standing step-1 item
  ② ("U6/W2 versioned contract → NEW f-research-v1 P0 state, no P stages in
  guidance state") **was already executed at R108 as a DRAFT scaffold** —
  5,190 B / `c246468e50712522`, 26 P0–P21 stages all pending, empty history,
  contract `DRAFT, not activated` / `PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF`
  — and main-line guidance state has zero P-stage IDs. Status
  `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED`, **not** a pass/activation/evidence.
  R111 line 26 already observed the prompt/ledger drift, so this is
  quantification + consolidation, **not** a first-ever discovery. Three
  distinct state namespaces with distinct hashes (main-line 12 stages; R108
  draft 26 all pending; historical v2 `v2-R51` 26 = 13 passed + 13 pending,
  read by validator D2 / guard A2) ⇒ consistent with R110 C5, not new.
  Live double gate: validator `NOT_QUALIFIED / 6.0 / >=7.0` (D1,D4 pass;
  D2,D3,D5 fail), guard `INCOMPLETE` (A2,A6 fail; S1–S7 all 7 pending; 0
  actions); readouts byte-anchored in the private run root, not `/tmp`.
  Reproducibility: 31 sources, independent verifier (no collector import, no
  R120 JSON read) **75 checks / 75 MATCH / 0 MISMATCH**, 31/31 isolated
  byte-identical copies. **v1 collector defect preserved verbatim**: project
  root one level too high → empty project-root reads, plus three needle
  mismatches; script/search-scope defects, not data inconsistencies; fixed in
  v2, both readings retained. Content safety: strict secret-value patterns 0
  hits, staged public files 0 local-absolute-path hits, 0 real numeric
  scored-verdict lines, no >50 MiB / dataset / weight / binary / third-party
  source / unpublished manuscript. Fresh isolated sub-agent launched with no
  expected conclusion and no score anchors; **at checkpoint write time NOT
  recovered ⇒ no verdict claimed**; recovered conclusion goes into a new
  immutable checkpoint. Step-3 precondition unmet ⇒ no manuscript copy, no
  compile, no full review. **0 papers qualified, no COMPLETE, governing still
  6.0, `NOT_QUALIFIED` / `INCOMPLETE`.** A checkpoint `completed` is work
  state, not scientific validation.
- **R119 isolated recheck recovered + append-only corrections (eleventh,
  eleventh checkpoint).** The tenth checkpoint was written while the fresh
  isolated sub-agent was still running and truthfully claimed no verdict; its
  bytes are **not rewritten**. Final independent report (primary project,
  **not uploaded**) is **28,594 B** / SHA-256
  `55dbfbf130ac2fde9d7ff950d70c5718cd07d491901ac5459f173446cfd89219`, one
  write, no intermediate state, original unchanged. Verdict
  `REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result
  claimed: NO`, `Forward pass performed: NO`. A–L **all MATCH**, zero
  MISMATCH; reviewer used **no** R119 JSON as a data source and recomputed
  from source bytes. **12 named overclaim categories CONFIRMED = 0 (all
  REFUTED)**; **8 defects (2 medium / 6 low / 0 high)**, no fabrication, no
  score line, no forward pass, no gate promotion, no existing file modified
  by the reviewer. **All 8 accepted, append-only** in primary
  `R119-POST-REVIEW-CORRECTION.md`: M1 masking-scope inconsistency (private
  artifacts vs sanitized public summary; staged public files 0 local-path
  hits), M2 snapshot-scope wording on ledger SHA (append-only entries landed
  after capture; no historical byte changed), L1 prefix-glob count scope, L2
  `-null-ladder` filenames, L3 broad historical negative narrowed to a scope
  observation, L4 inventory timing, L5 "v4 never created" narrowed to a
  pending gate-owner decision + "R51 **protocols/** brief", L6 "main-line"
  qualifier retained. Only `evidence/R119-INDEPENDENT-REVIEW-SANITIZED.md` is
  uploaded; the independent report original stays private. Gate/evidence
  recheck, **not** a `ccf-paper-reviewer full` manuscript review. All ten
  earlier published checkpoints untouched. **Result unchanged: 0 papers
  qualified, no COMPLETE, governing R95 = 6.0 / Confidence 4.0.**

- **R119 — read-only review-launch protocol chain audit (tenth
  checkpoint).** Concurrency guard not triggered (primary ledger `05:26:24`,
  ~62 min stale >10 min; 0 project writes in preceding 20 min; only this
  automation session; newest review still r95; no R119 artifacts).
  Direction change: R110 already proved acceptance-machinery reachability,
  R111's five decision points remain unanswered, and R114–R118 exhausted the
  approval-free first-hand acquisition channel with three earlier loop halts.
  This round audits a layer untouched in 118 prior rounds: the **launch brief
  of the sole success-criterion action**. Zero network requests, zero
  write-back to pre-existing bytes. Measured from raw bytes: exactly **one**
  `independent-review-brief*` file (4,803 B / `8771dea8…`), titled
  `(Contract v2, R51)`, carrying `X > 8.0`, `If X <= 8.0`,
  `score_gt_threshold = true`, a hard-coded `…20261108` output filename and an
  `8 pages` clause. `GOAL-ITERATION-R107.md` lines 90–92 deliberately freeze
  `protocols/` and name a *future* v4 versioned contract, but **zero** R107/v4
  launch briefs exist ⇒ a **versioned-contract gap** on the launch path.
  Strictly **not** claimed: no anchor leak to the reviewer (the verbatim
  handoff block lines 21–66 has zero `8.0`/`7.0` tokens and explicit
  non-anchoring clauses; R51 numbers live only in the preamble and post-review
  gate, and R58/R60 registered them as background only), no missing machine
  field (`score_gt_threshold` retained with `>=` semantics plus
  `score_meets_threshold`), no R95 anchoring (R95 used a different 5,275 B
  frozen brief), no new A6 finding, no first-ever brief-path-imprecision
  discovery (R95 already logged a different brief's `paper/sources/` path).
  One real incidental fact: the brief's cited
  `ccf-paper-reviewer/references/review-output-standards.md` does not exist;
  the real file is under `ccf-common/references/` and the reviewer `SKILL.md`
  lines 27/40/90 cite that path. 36 verification checks / 36 MATCH / 0
  MISMATCH; 6/6 isolated byte-identical copies; two collector-v1 script
  defects (directory `read_bytes()`, wrapped-line exact-substring false
  negative) logged as script judgment defects, not data inconsistencies.
  Read-only double gate: validator `NOT_QUALIFIED / 6.0 / >=7.0` (D1✓ D2✗
  D3✗ D4✓ D5✗), guard `INCOMPLETE` (A2/A6, S1–S7 pending), ledger SHA-16
  `f98b69369db6eb80` + mtime and main `pipeline-state.json` `bcb48bb9…` /
  3,723 B identical before/after. **Fresh isolated sub-agent launched with no
  expected conclusion; at this checkpoint's write time its report had NOT been
  recovered, so this checkpoint claims no recheck verdict** — per the R117
  precedent the recovered conclusion and any append-only corrections go into a
  new separate immutable checkpoint. Content scan: 44 files, 0 pattern hits,
  0 files >50 MiB, 0 binary/dataset/weight/third-party/unpublished-manuscript
  files, largest 29,482 B. Primary reports/scripts/JSON/independent-review
  original **not uploaded**; only `evidence/R119-REVIEW-LAUNCH-PROTOCOL-SANITIZED.md`.
  All nine earlier published checkpoints untouched. **Result: 0 papers
  qualified, no COMPLETE, governing still R95 = 6.0 / Confidence 4.0.**
  The versioned-contract decision belongs to the designated gate owner; the
  heartbeat does not create a v4 contract or self-certify.

- **R118 — read-only first-hand source registry gap audit + isolated recheck
  recovered (ninth checkpoint).** Concurrency guard not triggered
  (primary ledger `03:34:35`, ~61.6 min stale >10 min; 0 project writes in the
  preceding 20 min; no independent main session / polling; no new file in
  either review-report directory; no R118 artifacts). Direction change: no
  machine-gate fix, no Nth G0 text patch, no P3 forward pass. Instead quantified
  two debts R107's **independent gate review** named verbatim and left open
  across 11 rounds: **W7 / R4 PARTIAL** (R106 §6 R4 requires registering the
  SHA-pinned `arXiv:2609.24565v2` bytes into `literature-search/source-manifest.json`;
  R107 froze 5 Kuklev files but never registered them — measured now still
  `1124 B / 541880ab… / 5 entries / no 2609.24565`, byte-identical to R107's
  record) and **R98 "23 saved public sources" vs a 5-entry manifest**.
  Read-only, **zero network requests**, zero write-back to pre-existing project
  bytes. Measured from raw bytes: `literature-search/` **167** files, **26**
  suffix-filtered first-hand candidates, **5** registered, **21** unregistered,
  **141** project-owned artifacts; registry 5 declared bytes+SHA **10/10 match**;
  Kuklev 5 frozen bytes **5/5 SHA match** R107; verification **50 checks, 0
  MISMATCH** (plus 5 `PROBED`, 1 `REGISTERED`). **26 is a candidate count, not
  26 verified sources**; no single rule reproduces R98's 23, so it is neither
  confirmed nor refuted. **Incremental observation** (not a first-ever
  discovery): registry entry 5 `flyvis2024` is SHA-intact but its plain text is
  only **165 chars**, a reCAPTCHA / browser challenge page; R98 excluded only
  the failed `.txt` CAPTCHA response, so the registered `.html` is also a
  challenge page ⇒ 5/5 SHA-intact but only **4/5 content usable**.
  `flyvis2024-primary.xml` / `-body.txt` still hold the EuropePMC body; the
  registry was not rewritten. **gap 2 still OPEN**: matrix `9445 B / 31b5098b…`
  byte-identical to the R106 freeze, lines 46–47 still contain the stale
  `the open question` + `Kuklev leaves`. **Not the first** Kuklev field-level
  recomputation (R107 already did it); the increment is exact abstract lengths,
  verbatim key sentences, `abs/latest == abs/v2`, and a two-scope search readout.
  Read-only double gate: validator `NOT_QUALIFIED / 6.0 / >=7.0`, guard
  `INCOMPLETE` (A2, A6), ledger SHA-16 `73043b4e164a5a5f` + mtime and main
  `pipeline-state.json` `bcb48bb9…` / 3723 B identical before/after; G0 and
  G1–G8 / validation / handoff all `pending`. Fresh isolated sub-agent, **no
  expected conclusion supplied**: `R118-INDEPENDENT-REVIEW.md` final
  **23,653 B / SHA-256 `3ffc37c9fe71ad8daeb677d62bfafd9dd789d4220a93cd1c7d5643fa0d2d7bc7`**,
  one write, no intermediate state, original unchanged. Verdict
  `REPRODUCIBLE_WITH_WORDING_AND_JUDGMENT_DEFECTS | G0 may be passed: NO |
  Scientific result claimed: NO`, `Forward pass performed: NO`. 168 readings
  reproduced; **12 named overclaim / self-certification categories (a)–(l) all
  REFUTED**, no high-severity defect, no fabrication, no existing file modified.
  **9 defects (3 medium / 6 low) all accepted** via append-only correction:
  W1 mislabelled "closing sentence" (it is the penultimate sentence), **W2
  substantive wording withdrawal** — "12/12 all hit the frozen raw bytes" →
  reconstructed plain text 12/12 FOUND but raw-byte exact substring for the 10
  §7.3/§8/§9 phrases is **6 FOUND / 4 ABSENT** (MathML / U+2002 splits), and
  2 of the 12 fields are abstract sentences not §7.3/§8/§9; W3 three mixed
  abstract-length conventions; W4 truncated verbatim CAPTCHA quote; W5 two
  classification conventions; W6 "new discovery" → "incremental observation";
  W7 zero-write-back scope + `/tmp` double-gate readouts not independently
  recomputable; W8 "0 mismatch" is not all-green (5 `PROBED` include one
  `CHALLENGE_PAGE`); W9 R98 "23" wording. None changes core counts, byte
  integrity, the non-scientific-result boundary or absence of a G0 promotion.
  A **v1 verifier false negative** is preserved verbatim (17,627 B /
  `5f44c8e4…57fe`): a keyword-too-broad script judgment defect, not a data
  inconsistency; v2 adds a two-condition rule plus 5 content-validity probes,
  both readings retained. Gate/evidence recheck, **not** a
  `ccf-paper-reviewer full` manuscript review: no scored-review Overall line,
  no numeric paper score, no governing change. Primary reports / scripts / JSON
  / review original **not uploaded**; only `evidence/R118-REGISTRY-GAP-SANITIZED.md`
  is. All eight earlier published checkpoints byte-for-byte untouched.
  Governing still 6.0, 0 qualifying papers, no COMPLETE.
- **R117 isolated recheck recovered (eighth checkpoint).** Fresh isolated
  sub-agent, no expected conclusion supplied: final 22,725 B / SHA-256
  `0d133eaca0684bc61b927378923aaf09489adb6e33b979b8c4e9be33df030a3b`,
  one write, no intermediate state, original unchanged. Verdict
  `PARTIAL | G0 may be passed: NO | Scientific result claimed: NO`,
  `Forward pass performed: NO`. Independently recomputed 19/19 sources, 6/6
  artifacts, 8/8 clips, checkpoint + both digest framings, main
  `pipeline-state.json` (all pending), and 7 import configs. **Twelve named
  overclaim/self-certification categories: CONFIRMED = 0 (all REFUTED).**
  Six low / low-medium defects accepted by append-only correction; the
  low-medium one (R101-rule digest lacked a first-hand on-disk artifact) was
  closed with a NEW recomputation script + JSON, not a text patch. The review
  contains two real local paths in its own section 0, so **the original is not
  uploaded**; only `evidence/R117-INDEPENDENT-REVIEW-SANITIZED.md` is. 14 strict
  credential patterns 0 hits. Gate/evidence recheck, **not** a
  `ccf-paper-reviewer full` manuscript review; no scored-review Overall line,
  no numeric paper score, no governing change. All seven earlier published
  checkpoints byte-for-byte untouched. Governing still 6.0, 0 qualifying
  papers, no COMPLETE.
- **R117 — mainline P3 forward-pass execution premises, measured read-only.**
  Sanitized summary: `evidence/R117-EXEC-PREMISE-SANITIZED.md`;
  checkpoint `20261113T192349Z-r117-exec-premise`. Direction change: R114–R116
  exhausted the approval-free first-hand acquisition channel, so R117 returned
  to the mainline P3 real forward (U5) and measured the **execution
  environment** that R106 had only inferred. Local Conda, zero network
  requests, strict EXEC LOCK (zero forward / inference / training / labels /
  EPE·l2 / scientific metric). **7 import configs: 5 FAIL / 2 OK** — default
  environments and the official source tree all fail; only the R101 sandbox
  with a reconstructed, explicitly non-official `flyvis/version.py` plus
  explicit `PYTHONPATH`/`FLYVIS_ROOT_DIR` imports OK. Historical readouts are
  reproducible but **not portable**. **Device premise**: MPS available in all 7
  configs but `flyvis.device = cpu` in both OK configs; upstream `cuda if
  available else cpu` + global `set_default_device` means a default-path P3
  forward runs entirely on CPU, and using MPS requires explicit `.to("mps")`.
  No device migration/forward performed, no 4090/L4/H20 claim. **Asset bytes
  confirmed**: official checkpoint SHA + `weights_only=True` (14 tensors, all
  finite), digest under R101's original rule MATCH, 8 Sintel npz CRC/SHA 8/8
  match R106 (zero array instantiation). A first probe digest differed only by
  one extra trailing `\0` => framing difference, **not** a data conflict.
  v1 verifier false negative (credential vs local-path categories merged) is
  preserved verbatim; final 45/45 MATCH. Read-only double gate unchanged:
  validator `NOT_QUALIFIED / 6.0 / >=7.0`, guard `INCOMPLETE` (A2/A6), zero
  write-back. **No gate passed, G0 `pending`, no scientific result.** Three P3
  premises are now explicit and need a designated gate owner to freeze a
  versioned execution contract (non-official `version.py` acceptability, MPS
  adaptation vs global default device, executable frozen-seed/noise/
  zero-injection runner). Governing still 6.0, 0 qualifying papers, no COMPLETE.
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

# HANDOFF — wb-main / r109-harbor-sync

- Task / agent / branch: `r109-harbor-sync` / `wb-main` /
  `agent/r109-harbor-sync/wb-main`
- Status: **in_progress** (13 checkpoints published; harbor trial closed, research itself unfinished)
- Last update: 2026-11-14 09:0x +0800 (R120 heartbeat: isolated independent recheck recovered, all 7 defects accepted append-only; thirteenth checkpoint; awakened 2026-11-14 08:16)
- Protocol: `collaboration/PROTOCOL.md` v1; `collaboration/PROJECT.md`
- Repo: `ZtL-sysu/fly-connectome-control-ladder` (public)

## Completed

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

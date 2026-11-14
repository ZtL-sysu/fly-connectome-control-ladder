# Checkpoint: 20261113T212138Z-r118-registry-gap

- Task / agent: `r109-harbor-sync` / `wb-main`
- Status: **completed** (work state: one read-only audit round completed,
  independent recheck recovered, append-only corrections registered and
  published; **NOT** a scientific result, **NOT** a paper-acceptance claim,
  **NOT** a gate pass)
- Protocol: `collaboration/PROTOCOL.md` v1
- Manifest: [manifest.json](manifest.json)
- Measurements: [metrics.csv](metrics.csv) (this round has real read-only
  measurements; all rows are counts / SHA / byte sizes, no scientific metric)
- Sanitized summary: `evidence/R118-REGISTRY-GAP-SANITIZED.md`
- Cites the eight earlier checkpoints (`r109-init`, `r108-build`,
  `r108-final`, `r114-g0-license`, `r115-g0-remaining`,
  `r116-archive-content`, `r117-exec-premise`, `r117-post-review`)

## Direction change (RGE4)

R114–R116 exhausted the approval-free first-hand license / archive-byte
channel; R116's isolated recheck assigned gap 1's three remaining items to a
designated gate owner. R117 measured P3 forward-pass execution premises and
handed three P3 prerequisites to a gate owner for a versioned contract.
R111's five-point decision package is unanswered; R105/R107/R109 already
stopped the "another evidence document" loop three times.

This round performs **no** machine-gate fix (all need user / gate-owner
approval), **no** Nth G0 text patch, **no** P3 forward pass, **no** probe /
guard / runner patch cycle. It quantifies, purely read-only, two concrete debts
that R107's **independent gate review** named verbatim and that stayed open
across R107–R117 (11 rounds):

1. **W7 / R4 = PARTIAL**: R106 §6 R4 requires registering the SHA-pinned
   `arXiv:2609.24565v2` first-hand bytes into
   `literature-search/source-manifest.json`. R107 froze 5 Kuklev byte files
   (this round: 5/5 SHA match R107's declaration) but never did the specified
   registration. Measured now: registry still **1124 B / `541880ab…` /
   5 entries / no `2609.24565`**, byte-for-byte identical to R107's independent
   review record ⇒ **11 rounds of zero change, gap still open**.
2. **R98 "23 saved public sources" vs a 5-entry manifest**, called out by
   R107's review but never quantified.

## Measured readouts (from raw disk bytes; zero network requests)

`literature-search/` **167** files; **26** first-hand candidates by declared
suffix rule; **5** registered; **21** unregistered; **141** project-owned
artifacts. Candidate classes: EXTERNAL_FIRSTHAND_PAGE **13** / DERIVED_TEXT
**7** / NEGATIVE_OR_ERROR_PAGE **3** / UNCLASSIFIED **3** (all PDFs, left for
owner judgment). Registry's 5 declared bytes+SHA vs disk: **10/10 match**.
Kuklev frozen bytes: **5**, 5/5 SHA match R107. Verification: **50 checks,
0 MISMATCH** (plus 5 `PROBED` and 1 `REGISTERED` status rows).

**26 is a suffix-filtered candidate count, not 26 verified first-hand
sources**; 13 is a script text-heuristic classification. No single declared
rule reproduces R98's 23 ⇒ this round **neither confirms nor refutes 23**,
only registers the decomposition.

## Incremental observation: byte integrity != content validity

Registry entry 5 `flyvis2024` (declared `21444 B / ec7eb823…615`) matches disk
bytes exactly, but its plain text is **165 characters** verbatim:
`Checking your browser - reCAPTCHA Checking your browser before accessing
pmc.ncbi.nlm.nih.gov ... Click here if you are not automatically redirected
after 5 seconds.` — no Abstract, no body ⇒ a **CAPTCHA / browser challenge
page**. R98 line 21 records and excludes only the failed `flyvis2024.txt`
CAPTCHA response; the registered `.html` is also a challenge page but was not
excluded ⇒ 5/5 entries SHA-intact, only **4/5 content usable**.

**No overclaim**: one content probe of a registry entry, not "FlyVis primary
literature missing". `flyvis2024-primary.xml` (443,143 B) and
`flyvis2024-primary-body.txt` (125,982 B) hold the EuropePMC body and remain
in the primary workspace. The registry was not rewritten or deleted; not a gap
closure or scientific result. The independent recheck narrowed "new first-hand
discovery" to **"incremental observation"**.

## Kuklev v2 abstract bytes (not a first-time recomputation)

R107 already did a field-level recomputation; this round is **not the first**.
Increment: exact lengths, verbatim key sentences, `abs/latest == abs/v2`
equality, and a two-scope search readout. Three length conventions are **not
directly comparable** (1544/1443 include the `Abstract: ` prefix, +10 each;
1943 is the body Abstract core without prefix/`Keywords.`). The earlier label
"closing sentence" is **withdrawn**: `Longer observations…` is the penultimate
sentence, the v1 line is a trailing clause, only the body line is a true
closing sentence.

**Search-scope correction**: of 12 verbatim fields, 2 are abstract key
sentences and 10 are §7.3/§8/§9 phrases. Reconstructed plain text: 12/12
FOUND. Raw-byte exact substring: the 10 phrases are **6 FOUND / 4 ABSENT**
(`+ 0.033`, `[ 0.015 , 0.050 ]`, `7.3 The stimulus never completes a cycle`,
`9 Limitations`, split by MathML tags / U+2002 / U+2006 spaces). They genuinely
exist in the paper. The earlier "all hit the frozen raw bytes" wording is
**withdrawn**: a search-scope wording defect, not a data inconsistency or
fabrication.

## gap 2 still OPEN

`literature-baseline-matrix.md` **9445 B / `31b5098b…a9b2`**, byte-identical
to the R106 freeze ⇒ no silent rewrite. Lines 46–47 still contain
`the open question` + `Kuklev leaves`, the stale phrasing R106 §6 R2 requires
deleting. R107's `…R107-final.md` is an unsigned `G0_EVIDENCE_DRAFT`, not a
final map. This round wrote nothing to the matrix, did not finalize it, did
not re-freeze its SHA, did not self-certify.

## Read-only double gate (main-session run; not independently rechecked)

validator `NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`
(D1 pass, D2 fail, D3 fail, D4 pass, D5 fail); guard `EXIT=1 / INCOMPLETE`
(7 deliverables pass, failures exactly **A2, A6**; S1–S7 all pending, 0
actions). A6 report text still uses the ledger's legacy `> 8.0` wording, the
known dual-convention issue registered in R109/R111, logged read-only and
unchanged. Zero write-back: guard ledger SHA-16 `73043b4e164a5a5f` + mtime,
main `pipeline-state.json` SHA-16 `bcb48bb964e657a4` / 3723 B identical
before/after; G0 and G1–G8 / validation / handoff all `pending`.

**Scope note**: the two gate reports were written to project-external `/tmp`
paths and cannot be independently recomputed from this checkpoint's bytes; the
isolated recheck did not rerun them. "Zero write-back" means zero write-back
**to pre-existing project bytes**, confirmed from SHA by the isolated recheck.

## Isolated recheck (recovered same round)

Fresh isolated sub-agent, no expected conclusion supplied.
`R118-INDEPENDENT-REVIEW.md` final **23,653 B / SHA-256
`3ffc37c9fe71ad8daeb677d62bfafd9dd789d4220a93cd1c7d5643fa0d2d7bc7`**,
one write, no intermediate state, original unchanged. First line
`REPRODUCIBLE_WITH_WORDING_AND_JUDGMENT_DEFECTS | G0 may be passed: NO |
Scientific result claimed: NO`; second `Forward pass performed: NO`.
168 readings reproduced; **12 named overclaim / self-certification categories
(a)–(l) all REFUTED**; no high-severity defect, no fabrication, no existing
file modified. **9 defects (3 medium / 6 low) all accepted** by append-only
correction: W1 closing-sentence label, W2 raw-byte search wording, W3 mixed
length conventions, W4 truncated verbatim quote, W5 two classification
conventions, W6 "new discovery" → "incremental observation", W7 write-back
scope, W8 "0 mismatch" not all-green, W9 R98 "23" wording. None changes core
counts, byte integrity, the non-scientific-result boundary or absence of a G0
promotion. Gate/evidence recheck, **not** a `ccf-paper-reviewer full`
manuscript review; no scored-review Overall line, no numeric paper score, no
governing change.

Also registered: a **v1 verifier false negative** preserved verbatim
(17,627 B / `5f44c8e4…57fe`) — a keyword-too-broad script judgment defect
that misclassified one real bioRxiv page and one Client Challenge page; v2 uses
a two-condition rule and adds 5 registry content-validity probes. Both readings
retained; **script judgment defect, not data inconsistency**.

## Content safety and publication scope

- Primary round directory: 14 files, 11 strict patterns (credentials / tokens /
  private keys / emails / local absolute paths / scored-review line /
  confidence field) **0 hits** for credentials, emails and real local paths.
  The two descriptive occurrences of a scored-review marker literal are
  negative statements, not score lines; the public summary avoids the literal.
- Public summary uses `<local>/` for all paths. Full-repo scan before push:
  13 strict patterns 0 hits, no file > 50 MiB, no dataset / weight / binary /
  third-party source / unpublished manuscript.
- Only new public files: this CHECKPOINT.md, its manifest.json, metrics.csv,
  the sanitized summary, plus append-only HANDOFF/LOG updates. Explicit
  `git add --` only; no `git add .`.
- The primary-project reports, scripts, JSON and the independent review
  original are **not uploaded**; only the sanitized summary is.
- Private `ZtL-sysu/novix-platform` untouched. No merge, force push, branch
  deletion or Release. All eight earlier published checkpoints untouched.

## Strict boundary

EXEC LOCK: zero forward pass / inference / training / labels / dataset arrays /
EPE·l2 / scientific metrics; no weights loaded, no npz instantiated. Zero gate
promotions, zero self-certification, zero state changes. No change to historical
bytes, reviews, scores, thresholds, manuscripts, gates, frozen artifacts,
matrix, criteria registry, gate configuration or `source-manifest.json`.
No `ccf-paper-reviewer full`, no governing self-assessment, no gate skipping,
no repeated review of an unchanged manuscript; no D1/v3 reopen, no predictor
v4, **no assumption of `<=32h / K=45` confirmation-panel authorization**;
unrelated to harbor 25092 engineering reward; no 4090 / L4 / H20 capability
claim. Primary project: no submission / commit / push. Heartbeat ACTIVE schedule
unchanged.

## Result

**0 qualifying papers, no COMPLETE written.** Governing stays **R95 = 6.0 /
Confidence 4.0**, `NOT_QUALIFIED` / `INCOMPLETE`. G0 stays `pending`. Stop gates
remain (1) achieve >= 7.0, (2) user stops.

## Next

The quantified **R4 registration**, disposition of the CAPTCHA registry entry,
classification of the 3 PDFs and 21 unregistered candidates, and **gap-2 matrix
finalization + SHA re-freeze** all require a designated gate owner's written
judgment and signature; the heartbeat does not write back the registry or
matrix. gap-1's three remaining items keep R116's judgment; R117's three P3
prerequisites keep "must be frozen as a versioned execution contract by a gate
owner", and P3 does not start while G0 is pending. Ordered G0–G8 (G4 handling
Kuklev v2 §7.3/§8/§9) → validation → handoff → P0 → P1A/P1B → P2 → P3 real
forward. Only with `failed_runs=0`, all finite, independent recomputation
agreement and substantive positive evidence may a new manuscript copy → 9-page
compile → fresh isolated full review proceed; **X >= 7.0** plus QUALIFIED +
COMPLETE is required before writing COMPLETE.

**Checkpoint status `completed` is a collaboration work state, not a scientific
conclusion.**

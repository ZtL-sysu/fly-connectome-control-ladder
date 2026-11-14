# R118 — first-hand source registry gap, recomputable read-only audit (sanitized)

**Nature**: `READONLY_REGISTRY_GAP_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
**Network requests**: 0. Every number below was recomputed from frozen local
disk bytes with `<local>/miniconda3/bin/python`. No new fetch, no timestamp
contamination.
**Write-back**: 0 for all pre-existing project bytes. All local paths in this
public copy are `<local>/`; no credentials, account identifiers or tokens.

This is a **sanitized summary**. The primary-project reports, scripts and JSON
stay in the private workspace and are not uploaded.

---

## Why this round

R114–R116 exhausted the approval-free first-hand license / archive-byte
channel; R116's isolated recheck assigned gap 1's three remaining items to a
designated gate owner. R117 measured P3 forward-pass execution premises and
handed three P3 prerequisites to a gate owner for a versioned contract. R111's
five-point decision package remains unanswered, and R105/R107/R109 already
stopped the "another evidence document" loop three times.

So this round performs **no** machine-gate fix, **no** Nth G0 text patch, **no**
P3 forward pass. Instead it quantifies two concrete debts that R107's
**independent gate review** named verbatim and that stayed open across R107–R117
(11 rounds):

- **W7 / R4 = PARTIAL**: R106 §6 R4 requires saving a SHA-pinned local
  first-hand copy of `arXiv:2609.24565v2` **and registering it in
  `literature-search/source-manifest.json`**. R107 did freeze 5 Kuklev byte
  files (this round: 5/5 SHA match the R107 declaration), but the specified
  registration was never done. Measured now: that registry is still **1124 B /
  `541880ab…` / 5 entries / no `2609.24565`**, byte-for-byte identical to what
  R107's independent review recorded ⇒ **11 rounds of zero change, gap still
  open**.
- **R98 "23 saved public sources" vs a 5-entry manifest**, a discrepancy R107's
  review called out but never quantified.

## Measured readouts (from raw bytes, not quoted from older conclusions)

| Item | Value |
|:--|:--|
| All files under `literature-search/` | **167** |
| First-hand **candidates** by suffix rule | **26** |
| …registered in registry | **5** |
| …unregistered | **21** |
| Project-owned artifacts (py/png/npz/npy/ipynb/zip/md/json) | **141** |
| Candidate classes | EXTERNAL_FIRSTHAND_PAGE **13** / DERIVED_TEXT **7** / NEGATIVE_OR_ERROR_PAGE **3** / UNCLASSIFIED **3** (all PDFs; this script does not extract PDF text) |
| Registry's 5 declared bytes+SHA vs disk | **10/10 match** |
| Kuklev frozen byte files (R107 dir) | **5**, 5/5 SHA match R107 declaration |
| Verification checks | **50**, MISMATCH **0** (plus 5 `PROBED` and 1 `REGISTERED` status rows, which are not MATCH/MISMATCH verdicts) |

**Boundary**: 26 is a **suffix-filtered candidate count**, not 26 verified
first-hand sources; 13 is a script's text-heuristic classification, and the 3
PDFs are explicitly left for owner judgment. R98's "23" matches no single
declared counting rule. This round **did not find a single rule that reproduces
23, and therefore neither confirms nor refutes it**; it only registers the
decomposition.

## Incremental observation this round: byte integrity != content validity

Registry entry 5, `flyvis2024` (declared `21444 B / ec7eb823…615`), matches its
disk bytes exactly, but its plain text is only **165 characters**, verbatim:
`Checking your browser - reCAPTCHA Checking your browser before accessing
pmc.ncbi.nlm.nih.gov ... Click here if you are not automatically redirected
after 5 seconds.` — no Abstract, no body ⇒ it is a **CAPTCHA / browser
challenge page**, not usable first-hand literature content.

R98 line 21 records and excludes only the **failed `flyvis2024.txt` CAPTCHA
response**; the registered `.html` is also a challenge page but was not
excluded. So the 5 registry entries are 5/5 SHA-intact but only **4/5 content
usable**.

**No overclaim**: this is one content probe of a registry entry, not a claim
that the FlyVis primary literature is missing. `flyvis2024-primary.xml`
(443,143 B) and `flyvis2024-primary-body.txt` (125,982 B) hold the EuropePMC
body and remain in the workspace; R106 already independently verified them.
This round does not rewrite or delete the registry entry, and does not call
this a gap closure or a scientific result. Per the independent recheck this is
an **incremental observation**, not a first-ever discovery.

## Kuklev v2: the two differently-worded abstracts, frozen verbatim

From R107's frozen bytes, zero network requests. **R107 already did a
field-level recomputation** of these bytes; this round is **not the first**. The
increment here is freezing the exact lengths, verbatim key sentences, and the
`abs/latest == abs/v2` equality into an independently recomputable readout.

| Source | Length | Verbatim key sentence |
|:--|--:|:--|
| `/abs/2609.24565` metadata abstract (`kuklev_abs_latest.html`, identical to `kuklev_abs_v2.html`) | 1544 incl. `Abstract: ` prefix; pure abstract 1534 | `Longer observations reverse the circuit-receptor ordering once the stimulus spans a period, but not through T4/T5.` — this is the **penultimate** sentence, not the closing one |
| `/html/2609.24565v2` body Abstract | 1943 core segment (2069 with prefix + `Keywords.` tail) | `Exact structure remains insufficient to beat what the moving retina already provides.` — actual closing sentence |
| v1 `/abs/2609.24565v1` abstract | 1443 incl. prefix; pure 1433 | `while the topology contribution and end-to-end BIM utility remain open questions.` — a trailing clause of the last sentence |

**The three lengths use three different conventions and are not directly
comparable.** All three sentences are verbatim true and were rechecked against
disk bytes this round.

### Search-scope correction (from the isolated recheck)

Of 12 verbatim fields, **2 are abstract key sentences** and **10 are
§7.3/§8/§9 phrases**. On the **reconstructed plain text** all 12 are FOUND.
On the **raw-byte exact-substring** reading, the 10 §7.3/§8/§9 phrases are
**6 FOUND / 4 ABSENT**: `+ 0.033`, `[ 0.015 , 0.050 ]`,
`7.3 The stimulus never completes a cycle`, `9 Limitations` are split by
MathML tags / entities / special spaces (U+2002, U+2006) and only form a
contiguous spaced string after tag removal. They are genuinely present in the
paper, just not in that exact form in the raw bytes. ⇒ The earlier phrase
"all hit the frozen raw bytes" is **withdrawn**; this is a search-scope wording
defect, not a data inconsistency or fabrication.

## gap 2 still OPEN

`literature-baseline-matrix.md` measured **9445 B / `31b5098b…a9b2`**,
byte-identical to the R106 freeze ⇒ no silent rewrite. Lines 46–47 still
contain `the open question` + `Kuklev leaves`, the stale phrasing R106 §6 R2
requires deleting and R107's independent review judged gap 2 OPEN. R107's
`…R107-final.md` is a `G0_EVIDENCE_DRAFT` (unsigned draft), not a final map.
This round wrote nothing to the matrix, did not finalize it, did not re-freeze
its SHA, and did not self-certify.

## Read-only double gate (main-session run; not independently rechecked)

| Gate | Reading |
|:--|:--|
| validator | `NOT_QUALIFIED` / governing **6.0** / threshold **7.0** / `>=`; D1 pass, D2 fail, D3 fail, D4 pass, D5 fail |
| guard | `EXIT=1 / INCOMPLETE`; 7 deliverables pass, failures exactly **A2 and A6**; S1–S7 all pending, 0 recorded actions. A6 report text still uses the ledger's legacy `> 8.0` wording — the known dual-convention issue registered in R109/R111, logged read-only and unchanged |
| zero write-back | guard ledger SHA-16 `73043b4e164a5a5f` + mtime, main `pipeline-state.json` SHA-16 `bcb48bb964e657a4` / 3723 B identical before/after; G0 and G1–G8 / validation / handoff all `pending` |

**Scope note**: reports for these two gates were written to project-external
`/tmp` paths, so they cannot be independently recomputed from this checkpoint's
bytes; the isolated recheck did not rerun them. "Zero write-back" means
**zero write-back to pre-existing project bytes**, and the independent recheck
confirmed that from SHA values.

## Isolated recheck (recovered same round)

`R118-INDEPENDENT-REVIEW.md` final **23,653 B / SHA-256
`3ffc37c9fe71ad8daeb677d62bfafd9dd789d4220a93cd1c7d5643fa0d2d7bc7`**, one
write, no intermediate state, original unchanged. First line
`REPRODUCIBLE_WITH_WORDING_AND_JUDGMENT_DEFECTS | G0 may be passed: NO |
Scientific result claimed: NO`; second line `Forward pass performed: NO`.
168 readings reproduced; **12 named overclaim / self-certification categories
(a)–(l) all REFUTED**; **no high-severity defect**, no fabrication, no existing
file modified. **9 defects (3 medium / 6 low) all accepted** via append-only
correction: W1 mislabelled "closing sentence"; W2 the raw-byte search-scope
wording; W3 mixed abstract-length conventions; W4 truncated verbatim quote;
W5 two classification conventions not distinguished; W6 "new first-hand
discovery" → "incremental observation"; W7 zero-write-back scope; W8 "0
mismatch" is not all-green; W9 R98 "23" wording. None changes the core counts,
byte integrity, the non-scientific-result boundary, or the absence of a G0
promotion. Gate/evidence-layer recheck, **not** a `ccf-paper-reviewer full`
manuscript review; no scored-review Overall line, no numeric paper score, no
governing change.

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

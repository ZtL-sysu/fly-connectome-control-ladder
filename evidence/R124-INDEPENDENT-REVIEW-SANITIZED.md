# R124 — isolated independent recheck recovered + append-only corrections (sanitized public summary)

**Nature**: gate / evidence-layer recheck recovery. **NOT** a `ccf-paper-reviewer full`
manuscript review; no numeric `**Overall:**` line; no score; no governing change.
The primary independent-review original is **NOT uploaded** (per the R117 precedent it
contains local absolute-path literals, scan-pattern literals and negation statements);
only this sanitized summary. All local paths are `<local>/`. No credential value, no
email, no dataset, no weight, no binary, no third-party source code, no unsubmitted
manuscript.

## Recheck result

Fresh isolated sub-agent `general-purpose-1`, launched with **no expected verdict / score
anchor / conclusion anchor**. Final primary `R124-INDEPENDENT-REVIEW.md`:
**28,602 B / SHA-256 `76abf752a8ea1fb57804400d05c6ef8baff168a4cb07455fb03cf5c2584a5293`**,
one write, mtime 15:47, original unchanged. First line:
`REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO |
Forward pass performed: NO`.

Reviewer used ONLY the 13 raw byte files with its own parsing logic (did **not** import the
acquisition module or verifier, did **not** use any R124-produced JSON as a substantive
data source, read the round audit LAST for defect grading), ran no verifier / git /
network, modified no existing file and wrote to no other directory. Existing file mtimes
(round audit 15:25:58, source manifest 15:23:24, verifier 15:24:52, raw 15:17–15:21) are
unchanged. Report contains 0 credential values / 0 scored verdict lines / 0 emails.

- **66 checks / 66 MATCH / 0 MISMATCH** (A 7 / B 12 / C 12 / D 5 / E 6 / F 3 / G 7 /
  H 8 / I 6): 13 filenames + byte counts + SHA-256 match the manifest, total 323,740 B
  by per-file summation, HTTP 200/301/429 = 8/1/4; bioRxiv collection has exactly 12
  records, versions '1'–'12', v1 2026-06-12 → v12 2026-10-16, v1 title differs from the
  eleven identical v2–v12 titles; **all 12 abstracts byte-identical, 4,816 chars, SHA
  `555e28f9fef30a3a…56702`**, containing `p < 10-13 in every case`,
  `closes the gap completely`, `trained Erdos-Renyi on OFF-polarity structure`, and
  containing **none** of `0.686` / `0.846` / `0.930 vs` (total 0 across all 13 raw files);
  `/1` suffix response byte-identical to details; Crossref DOI/type/dates/JATS
  `<jats:sup>−13</jats:sup>` (U+2212) / CC BY 4.0 licence; mirror `datePublished` =
  2026-10-16 = API 12th-record date; arXiv corrections `22871090`=1 / `22891264`=0,
  `9 Oct 2026`=2 / `12 Oct 2026`=0; four 429 files each 17 B `error code: 1015`;
  **no local v1 HTML byte freeze**; R106 §6 has R1–R9 plus the DOI and
  "v1 positive vs v3 largely negative", and R106-ROUND-AUDIT has an append-only section
  withdrawing W5 and correcting Zenodo / date; `pipeline-state.json` has CCFA-startup
  passed and G0 + G1–G8/validation/handoff all pending with `G0.inputs=[]`/`evidence=[]`;
  13 raw files have 0 local-path / credential-filename / Bearer hits, max 64,741 B, all
  UTF-8 JSON/HTML text with zero NULs and no dataset / weight / binary.
- **12 named overclaim categories (a)–(l): CONFIRMED 0 / REFUTED 12**, each with verbatim
  evidence. No fabrication, no data inconsistency, no fact error. Reviewer independently
  confirmed all classified aggregate numbers (323,740 B; 8+1+4; 145 group sum
  45+27+14+10+6+9+16+12+6; 12 records; 11 titles; 4,816 chars) are reproducible by
  byte summation / counting.
- Defects: **HIGH 0 / MEDIUM 3 / LOW 3**.

## Six defects ALL ACCEPTED, append-only

Recorded in primary `R124-POST-REVIEW-CORRECTION.md` (9,718 B, SHA-256 prefix
`1405ed027e3151902ccd`). **No historical byte is rewritten**: round-audit original,
independent-review original, both v1/v2 verifiers and VERIFICATION outputs,
SOURCE-MANIFEST, all 13 raw files, and the twentieth checkpoint are byte-unchanged.

- **M1 [MEDIUM | scope not delimited]**: `R124-ROUND-AUDIT.md:29` "zero local paths /
  project credentials" did not state its file set; verifier group I is scoped to the 13
  raw files (0 hits confirmed independently by the reviewer), while this round's
  `R124-GUARD-READOUT.txt` contains 13 local absolute-path literals. Narrowed to an
  explicit file-set declaration; that derived guard copy is local-only and NOT in the
  public upload set. **Not a factual misstatement**; no first-hand number changes.
- **M2 [MEDIUM | substantive narrowing]**: ":55 three INDEPENDENT first-hand byte
  sources: API abstract + Crossref abstract + mirror body" conflicted with the
  round-audit's own "mirror is always second-hand, never a first-hand conclusion source",
  and the three are three renderings of the SAME current abstract, not independent
  sources. Corrected to: **the same current abstract rendered at 2 first-hand endpoints
  (bioRxiv details API, Crossref work API) + 1 second-hand mirror endpoint**; the mirror
  is cross-corroboration only and not counted as a first-hand source; they do **not**
  constitute 3 independent sources. All occurrences of "3 independent first-hand byte
  sources" in the round audit, this sanitized summary and the twentieth checkpoint are
  read through this narrowing; bytes are NOT rewritten. **Reduces, not expands, claims.**
- **M3 [MEDIUM | substantive narrowing]**: the "12 versions" + "v1 positive vs v12
  scope" dichotomy was not fully consistent with the round's own negative conclusion
  (the first appearance of the negative conclusion cannot be determined from local
  bytes; no version attribution for intermediate versions). v1 positivity came only
  from an un-saved WebFetch transcription (`0.686` etc. total 0 in raw bytes); "v12
  scope" attributed a single abstract backfilled into all 12 records to one version.
  Corrected to: **12 version RECORDS** (metadata v1..v12 sharing ONE abstract, not 12
  distinguishable abstracts); **v1 page abstract = WebFetch transcription with NO local
  byte freeze, NOT a first-hand conclusion of this round**; **"current abstract scope"
  (no version attribution)**, with the mirror's `datePublished=2026-10-16` equal to the
  12th record's date only as a time-point corroboration, NOT version attribution. The
  R3 negative conclusion (v3 is not the turning version, no attribution for the middle
  ten) is **unchanged and now more explicit**. No R106 byte is rewritten.
- **L1 [LOW | undeclared counting scope / time-point mixing]**: `:16` "19 lines / 19
  files" had no stated counting scope. Main-session independent recount: strict
  line-start `^\*\*Overall:\*\* [0-9]` = **15 lines / 13 files** (including
  `provenance/` and `isolated/` byte-identical copies); **excluding copies = 12 lines /
  10 files**; the wake-time "19" was the file count for `^\*\*Overall:\*\*` **without**
  the numeric constraint. Same class as R121 J-1. **Core conclusion unchanged**:
  `new_governing_candidates=0`, latest independent full review still r95 (11-11), the
  two later-than-r95 files byte-identical to r95, no new score, no unregistered async
  review. All "19/19" occurrences are read through this correction, bytes not rewritten.
- **L2 [LOW | title scope]**: `:27` "first-hand freeze (13 files)" included the 2
  second-hand mirror files. Narrowed to "**13 raw byte files, 2 of which are
  second-hand mirror endpoints (301 + followed), cross-corroboration only, not counted
  as first-hand sources**". Total 323,740 B / 13 files unchanged.
- **L3 [LOW | coexistence unexplained]**: `:90` "report written to `/tmp`, not in
  project tree" is true for the original `guard check -o` output; a read-only copy
  `R124-GUARD-READOUT.txt` (4,871 B) was later `cp`'d into the round directory as a
  reading trace. Both are identical and unmodified; the copy contains local-path
  literals (see M1) and is not uploaded.

**Clarification on the reviewer's "concurrent write" observation**:
`R124-VALIDATOR-READOUT.json` (15:26:29) appearing after the round audit (15:25:58) was
produced by the main session itself 31 s after that audit, not by an external session;
`raw/` mtimes were stable throughout (15:17–15:21), bytes and SHA unchanged; the reviewer
explicitly stated the conclusion is unaffected.

**Reviewer scope limits (accepted)**: HTTP statuses are declarative values and cannot be
replayed from bytes; group A is a same-host identity check, not cross-source
cross-validation; the reviewer did not run the verifier, so the "145 checks / group
counts" were checked for category and self-consistency only, not independently
reproduced (145/145 is by design a same-host necessary-consistency check, stated in the
verifier `scope_note` and round audit §7); the v1 HTML 105,400 B "first probe" has no
local bytes and cannot be verified; concurrency guard, ledgers and `pipeline-state.json`
live readings are outside what the 13 raw files can prove and were collected
independently by the main session. The pre-existing 7 v1 script/expectation defects were
independently confirmed as correctly classified and both versions retained; not counted
as new defects.

## Scope of impact

All six defects are wording / scope / attribution narrowings. **None changes**: the 13
raw bytes and SHA-256, SOURCE-MANIFEST, v2 **145/145 MATCH / 0 MISMATCH**, 66/66 MATCH,
12 categories REFUTED 12, the double-gate readings (`NOT_QUALIFIED / 6.0 / >=7.0`,
`INCOMPLETE`), gate state (G0 pending, G1–G8 all pending, `inputs=[]`/`evidence=[]`),
governing **R95 = 6.0 / Confidence 4.0**, **0 papers qualified / no COMPLETE**, the
R106 §6 convergence table conclusion, or the heartbeat ACTIVE schedule.

The twentieth checkpoint truthfully stated at its write time that the recheck was
launched but not recovered and claimed no verdict; **its bytes are NOT rewritten**. This
**twenty-first immutable checkpoint** carries the recovered conclusion and append-only
corrections. Gate / evidence-layer recheck, NOT a `ccf-paper-reviewer full` manuscript
review; no scored verdict line, no self-authored governing review.

## Result

Step-3 precondition (**substantive new positive scientific evidence**) unmet ⇒ no new
manuscript copy, no 9-page compilation, no fresh isolated full review. **0 papers
qualified, no COMPLETE**; governing unchanged (R95 = 6.0 / Confidence 4.0),
`NOT_QUALIFIED` / `INCOMPLETE`; G0 pending; zero gate promotion / zero self-certification
/ zero state change. Stop gates remain only (1) qualify (>= 7.0) (2) goal owner stops.
A checkpoint `completed` is work state, not scientific validation.

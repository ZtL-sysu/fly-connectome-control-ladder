# CHECKPOINT — 20261114T075040Z-r124-post-review

- Task / agent / branch: `r109-harbor-sync` / `wb-main` / `agent/r109-harbor-sync/wb-main`
- Status: `completed` (work-state label, NOT scientific validation)
- Round: R124 isolated independent recheck RECOVERED + append-only corrections
- Created (UTC): 2026-11-14T07:50:40Z
- Input HEAD at manifest creation: see `manifest.json` (`input_git_head`)
- Immutable: all 20 earlier checkpoints' bytes are **not rewritten**.

## Why this checkpoint exists

The twentieth checkpoint `20261114T072731Z-r124-r3r5-first-hand/` truthfully stated at
its write time that a fresh isolated independent recheck had been launched but was **not
yet recovered**, and claimed **no recheck conclusion, no defect list and no
confirmation**. That statement was TRUE at write time and its bytes are **not rewritten**.
Per the R117/R119/R120/R121/R122/R123 precedent, the recovered conclusion and any
append-only corrections are published in a **new immutable checkpoint** — this one.

## Recovered recheck (gate / evidence layer, NOT a manuscript review)

Fresh isolated sub-agent `general-purpose-1`, launched with **no expected verdict / score
anchor / conclusion anchor**. Final primary `R124-INDEPENDENT-REVIEW.md`:
**28,602 B / SHA-256 `76abf752a8ea1fb57804400d05c6ef8baff168a4cb07455fb03cf5c2584a5293`**
(mtime 15:47, one write, no intermediate state, original unchanged). First line:
`REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO |
Forward pass performed: NO`.

Reviewer used ONLY the 13 raw byte files with its own parsing logic — did **not** import
the acquisition module or verifier, did **not** use any R124-produced JSON as a
substantive data source, read the round audit LAST for defect grading — ran no verifier /
git / network, modified no existing file and wrote to no other directory. Existing file
mtimes (round audit 15:25:58, source manifest 15:23:24, verifier 15:24:52, raw
15:17–15:21) unchanged. Report has 0 credential values / 0 scored verdict lines /
0 emails. **Independent-review original NOT uploaded** (contains local absolute-path
literals, scan-pattern literals and negation statements; R117 precedent) — only
`evidence/R124-INDEPENDENT-REVIEW-SANITIZED.md`.

**66 checks / 66 MATCH / 0 MISMATCH** (A 7 / B 12 / C 12 / D 5 / E 6 / F 3 / G 7 /
H 8 / I 6). Confirms: 13 filenames + bytes + SHA-256 vs manifest, total 323,740 B by
per-file summation, 8/1/4 HTTP split; bioRxiv 12 records, versions '1'–'12', v1
2026-06-12 → v12 2026-10-16, v1 title ≠ eleven identical v2–v12 titles; **all 12
abstracts byte-identical** (4,816 chars, SHA `555e28f9fef30a3a…56702`) with
`p < 10-13 in every case` / `closes the gap completely` / `trained Erdos-Renyi on
OFF-polarity structure` and **none** of `0.686` / `0.846` / `0.930 vs` (total 0 across
all 13 raw files); `/1` suffix byte-identical; Crossref DOI/type/dates/`<jats:sup>−13
</jats:sup>` (U+2212)/CC BY 4.0; mirror `datePublished` = 2026-10-16 = API 12th-record
date; arXiv `22871090`=1 / `22891264`=0 and `9 Oct 2026`=2 / `12 Oct 2026`=0; four 429
files each 17 B `error code: 1015`; **no local v1 HTML byte freeze**; R106 §6 R1–R9 and
R106 append-only corrections present; `pipeline-state.json` CCFA-startup passed and
G0 + G1–G8/validation/handoff all pending with `G0.inputs=[]`/`evidence=[]`; 13 raw
files 0 local-path / credential / Bearer hits, all UTF-8 text with zero NULs, no
dataset / weight / binary, max 64,741 B.

**12 named overclaim categories (a)–(l): CONFIRMED 0 / REFUTED 12**, each with
verbatim evidence. Defects **HIGH 0 / MEDIUM 3 / LOW 3**, **0 fabrication / 0 data
inconsistency / 0 fact error**. Reviewer independently confirmed all classified
aggregate numbers are reproducible by byte summation / counting.

## Six defects ALL ACCEPTED, append-only

In primary `R124-POST-REVIEW-CORRECTION.md` (9,718 B, SHA-256 prefix
`1405ed027e3151902ccd`). **No historical byte rewritten**: round-audit original,
independent-review original, both v1/v2 verifiers + VERIFICATION, SOURCE-MANIFEST,
all 13 raw files, and the twentieth checkpoint are byte-unchanged.

- **M1 [MEDIUM | scope not delimited]** `:29` "zero local paths / project credentials"
  lacked an explicit file set; group I is scoped to the 13 raw files (0 hits, reviewer
  confirmed), while this round's `R124-GUARD-READOUT.txt` has 13 local absolute-path
  literals. Narrowed to a file-set declaration; that derived copy is local-only and NOT
  uploaded. Not a factual misstatement; no first-hand number changes.
- **M2 [MEDIUM | substantive narrowing]** ":55 three INDEPENDENT first-hand byte
  sources: API abstract + Crossref abstract + mirror body" conflicted with the audit's
  own "mirror always second-hand, never a first-hand conclusion source"; the three are
  three renderings of the SAME current abstract. Corrected to **one current abstract at
  2 first-hand endpoints (bioRxiv details API, Crossref work API) + 1 second-hand mirror
  endpoint**, mirror cross-corroboration only, NOT 3 independent sources. Reduces claims.
- **M3 [MEDIUM | substantive narrowing]** "12 versions" + "v1 positive vs v12 scope"
  was not fully consistent with the round's own negative conclusion. v1 positivity came
  only from an un-saved WebFetch transcription (`0.686` etc. total 0 in raw bytes);
  "v12 scope" attributed one abstract backfilled into all 12 records to a single
  version. Corrected to **12 version RECORDS sharing ONE abstract** (not 12
  distinguishable abstracts); **v1 page abstract = WebFetch transcription with NO local
  byte freeze, NOT a first-hand conclusion**; **"current abstract scope" with no version
  attribution**, mirror `datePublished` only a time-point corroboration. R3's negative
  conclusion (v3 not the turning version, no attribution for the middle ten) is
  unchanged and now more explicit. No R106 byte rewritten.
- **L1 [LOW | undeclared counting scope]** `:16` "19 lines / 19 files" had no counting
  scope. Independent recount: strict line-start `^\*\*Overall:\*\* [0-9]` = **15 lines /
  13 files** (incl. `provenance/` and `isolated/` byte-identical copies), **excluding
  copies = 12 lines / 10 files**; "19" was the file count for `^\*\*Overall:\*\*`
  **without** the numeric constraint (same class as R121 J-1). Core conclusion
  `new_governing_candidates=0` unchanged: latest independent full review still r95
  (11-11), the two later-than-r95 files byte-identical to r95, no new score, no
  unregistered async review.
- **L2 [LOW | title scope]** `:27` "first-hand freeze (13 files)" included the 2
  second-hand mirror files. Narrowed to "**13 raw byte files, 2 of which are second-hand
  mirror endpoints (301 + followed), cross-corroboration only, not first-hand
  sources**". Total 323,740 B / 13 files unchanged.
- **L3 [LOW | coexistence unexplained]** `:90` "/tmp report not in project tree" is
  true for the original `guard check -o`; a read-only copy `R124-GUARD-READOUT.txt`
  (4,871 B) was later `cp`'d into the round directory as a reading trace. Identical and
  unmodified; contains local-path literals (see M1); not uploaded.

**Clarification on the reviewer's "concurrent write" observation**:
`R124-VALIDATOR-READOUT.json` (15:26:29) after the round audit (15:25:58) was produced
by the main session itself 31 s later, not an external session; `raw/` mtimes stable
(15:17–15:21), bytes/SHA unchanged; reviewer explicitly stated conclusion unaffected.

**Reviewer scope limits (accepted)**: HTTP statuses declarative and not replayable from
bytes; group A same-host identity check not cross-source validation; reviewer did not
run the verifier, so 145 checks / group counts were checked for category and
self-consistency only (145/145 is by design a same-host necessary-consistency check);
v1 HTML 105,400 B "first probe" has no local bytes and cannot be verified; concurrency
guard / ledgers / pipeline-state live readings are outside what the 13 raw files prove
and were collected independently by the main session. Pre-existing 7 v1
script/expectation defects independently confirmed correctly classified, both versions
retained, not counted as new defects.

## Scope of impact

All six are wording / scope / attribution narrowings. **None changes**: 13 raw bytes
and SHA-256, SOURCE-MANIFEST, v2 **145/145 MATCH / 0 MISMATCH**, 66/66 MATCH, 12
categories REFUTED 12, double gate (`NOT_QUALIFIED / 6.0 / >=7.0`, `INCOMPLETE`), gate
state (G0 pending, G1–G8 all pending, `inputs=[]`/`evidence=[]`), governing **R95 = 6.0
/ Confidence 4.0**, **0 papers qualified / no COMPLETE**, the R106 §6 convergence table,
or the heartbeat ACTIVE schedule.

## Content safety

Full-repository strict pattern scan before push: credential value, token assignment,
email, local absolute path, credential filename, webhook, connection string, real
scored-verdict line — 0 new hits. No >50 MiB file, no binary, no dataset, no weight, no
third-party source code, no unsubmitted manuscript. Only explicit files staged via
`git add --`; no `git add .`; `git diff --cached --check` clean; push to own agent
branch; `git ls-remote` remote SHA must equal local HEAD before claiming uploaded. 20
earlier published checkpoints untouched; private `ZtL-sysu/novix-platform` untouched;
no merge / force push / branch deletion / Release.

## Result

Step-3 precondition (**substantive new positive scientific evidence**) unmet ⇒ no new
manuscript copy, no 9-page compliant compilation, no fresh isolated full review.
**0 papers qualified, no COMPLETE**; governing unchanged (R95 = 6.0 / Confidence 4.0),
`NOT_QUALIFIED` / `INCOMPLETE`; G0 pending; zero gate promotion / zero self-certification
/ zero state change. Stop gates remain only (1) qualify (>= 7.0) (2) goal owner stops.
A checkpoint `completed` is work state, not scientific validation.

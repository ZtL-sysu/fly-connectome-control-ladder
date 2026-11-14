# CHECKPOINT — 20261114T093526Z-r125-version-route-exhaustion

- Task / agent / branch: `r109-harbor-sync` / `wb-main` / `agent/r109-harbor-sync/wb-main`
- Status: `completed` (work-state label, NOT scientific validation)
- Round: R125 read-only first-hand route exhaustion for the R124 M3 version-attribution gap
- Created (UTC): 2026-11-14T09:35:26Z
- Input HEAD at manifest creation: see `manifest.json` (`input_git_head`)
- Immutable: all 21 earlier checkpoints' bytes are **not rewritten**.

## Why this checkpoint exists

R124's own isolated-review correction **M3** narrowed a claim to: the "v1 page
(positive)" abstract is a **WebFetch transcription with no local byte freeze**, NOT a
first-hand conclusion (the four positive numbers `0.686 / 0.846 / 0.930 / 0.603` occur
zero times across R124's 13 raw files). R124's hand-off grouped "whether to fetch the v1
page bytes" together with "classification / registration into the matrix and source
manifest" and passed the whole group to a designated gate owner.

R125 executes **only** the autonomous half — first-hand byte acquisition — and leaves
classification / registration / matrix finalisation / written-pass-criterion freezing
with the designated gate owner (decision groups G1 / G4 / G6 / G7). Byte acquisition is
read-only and is not a gate decision. No 9th process-audit layer, no G0 text patch, no
v4 contract, no P3 forward pass while G0 is pending.

R124 had tried only the `www.biorxiv.org/content/...v1` HTML path (four times, all HTTP
429). The bioRxiv official details API itself publishes a `jatsxml` per-version URL for
each of its 12 version records; that **official per-version full-text route had never
been tried**. Two independent hosts (EBI Europe PMC, Internet Archive Wayback) and a
hypothesised `api.biorxiv.org` JATS endpoint were also untested.

## Acquisition (13 raw files / 135,063 B, each frozen verbatim + SHA-256)

| Route family | Result | Reading |
|:--|:--|:--|
| official per-version JATS, 5 variants (v1 canonical, v1 alternate path, v1 DOI form, v3, v12) | 5 x HTTP 429 / 17 B / `error code: 1015`, all five share one digest | negative, time-point scoped |
| EBI Europe PMC `fullTextXML`, 2 variants | 2 x HTTP 500 / 150 B | **structural**, not transient |
| EBI Europe PMC `resultType=core` | HTTP 200 / 6,367 B | **new third first-hand endpoint** |
| Internet Archive CDX + `/web/2026/` | `[]` (3 B) + HTTP 404 / 4,657 B | negative |
| `api.biorxiv.org/jats/...` | HTTP 404 / 196 B | endpoint does not exist |
| `api.biorxiv.org/details/.../1` | HTTP 200 / 64,741 B | byte-identical to R124 un-suffixed details; independently reproduces "`/1` is not a version selector" |
| `connect.biorxiv.org/relate/content/181` | HTTP 200 / 58,714 B | byte-identical to R124 frozen copy; duplicate, not a new source |

Largest file 64,741 B (`api-details-v1.json`); second largest 58,714 B
(`connect-jats.xml`). A draft of this round's own unpublished documents stated
58,714 B as the maximum; byte-wise max computation during `metrics.csv` generation
exposed the error and it was corrected in place before publication. Zero local
absolute paths, credentials, datasets, weights,
binaries or scored-verdict lines in the raw set (verifier group H: 6/6). All 13 raw
files, the round audit, the verifier scripts, the verification JSON, the validator /
guard readouts and the independent-review original are **NOT uploaded** (local-only at
`<local>/`). Only `evidence/R125-VERSION-ROUTE-EXHAUSTION-SANITIZED.md` is published.

## Substantive findings (third-party text facts, strictly bounded)

1. **Third independent first-hand endpoint carrying the SAME current abstract.**
   Europe PMC `resultType=core` (EBI host, distinct from bioRxiv / Crossref / the
   second-hand mirror) returns `abstractText` of 4,847 characters; similarity to the
   bioRxiv details API abstract (4,816 chars) = **0.9906**; all 22 difference ops are
   typographic / whitespace / hyphen / comma / name-transliteration normalisation, no
   semantic difference. It carries the negative wordings `largely null result`,
   `disappears entirely`, `statistically indistinguishable`, `size-matched`,
   `not the confirmation we set out to find`; the four "v1 positive" numbers occur
   **zero** times. Per R124 M2/M3, the same abstract at several endpoints is **not**
   several independent sources: R125 registers **endpoint count +1**, NOT
   independent-source count +1, and makes **no version-attribution claim**. R124's M3
   narrowing is **strengthened, not overturned**.
2. **The official per-version JATS route is structurally unusable for version
   attribution.** `version` is a **string** `'1'..'12'`; **12 records share ONE
   abstract** (4,816 chars, SHA-256 prefix `555e28f9…`) and **2 distinct titles**
   (v1 differs from v2–v12); but `jatsxml` has only **10 distinct URLs** — v3/v4 both
   point to `2026-06-23`, v8/v9 both to `2026-06-30`. Even if the 429 cleared and all
   JATS full texts were retrievable, **two version pairs would remain indistinguishable
   at the official endpoint**. Endpoint-side structural limit, not a rate-limit artefact.
   All 12 `license = cc_by` and EPMC `license = "cc by"` are **record-level metadata
   declarations**, NOT per-asset licence text (R123 lesson); they do **not** close gap 1.
3. **The Europe PMC 500 is structural, not transient.** R124 lite metadata and R125 core
   metadata agree on `hasPDF=N / inEPMC=N / inPMC=N / isOpenAccess=N`;
   `fullTextUrlList` has exactly one entry pointing only to a DOI resolver ⇒ EPMC holds
   no full text for this preprint. `dateOfCreation` / `firstPublicationDate` /
   `firstIndexDate` are index / first-publication dates, **not** the current abstract's
   version (R124 lesson).
4. **Negative conclusion, reported as such.** The "v1 page has no local byte freeze" gap
   left by R124 M3 **remains open** after exhausting official per-version JATS, EPMC
   full text, Wayback and `api.biorxiv.org` routes. The "v1 positive vs current negative"
   dichotomy still has **no first-hand byte support**. **R3 stays OPEN.** No byte of
   R106 or R124 is rewritten; acquisition completion is NOT presented as gap closure.

## Time-point / scope limits (anti-overclaim)

- HTTP 429 / 500 / 404 / empty-CDX results are scoped **strictly to the R125 acquisition
  instant (2026-11-14 ~17:0x +0800) and the exact URLs / hosts in the acquisition map**.
- 429 is a **Cloudflare 1015 host-side rate limit, NOT permanent unavailability**: R124
  obtained HTTP 200 from `api.biorxiv.org` and `connect.biorxiv.org` the same day and
  reported an unsaved 200 / 105,400 B v1 HTML response. No "permanently unfetchable"
  claim.
- Wayback CDX used `statuscode:200`, `limit=5` and one URL form; "zero snapshots" is
  scoped to that query, not "no archive anywhere".
- Character counts / similarity are bound to specific derived files with a declared
  normalisation convention (R122 C-1 / R124 M1 lessons).

## Reproducibility

`R125-verify.py` does **not** import the acquisition module and does **not** use any
R125-produced JSON as a substantive data source; it recomputes from the 13 raw byte
files plus R124's two frozen authority files: **93 checks / 93 MATCH / 0 MISMATCH**
(A 27 / B 6 / C 10 / D 24 / E 14 / F 4 / G 2 / H 6). Group A is a **same-machine
byte-identity consistency check, not independent cross-source verification**; SHA
literals come from a separate `shasum -a 256` measurement, none invented.

Two verifier defects retained and reproducible, both **script / expectation defects, not
data inconsistencies, not fabrication**: **V-1** (v1) `bytes` not JSON-serializable →
`TypeError`; **V-2** (v2) expected `version` as ints but the API returns strings →
`91/92 MATCH, 1 MISMATCH (E-versions)`. v3 fixes both and adds an explicit field-type
check → 93/93. v1 and v2 files kept; neither overwritten.

## Double gates (read-only, at acquisition instant)

- validator: `NOT_QUALIFIED / 6.0 / >=7.0 / score_meets_threshold=false` (D1, D4 pass;
  D2, D3, D5 fail).
- guard: `INCOMPLETE` (A2, A6 fail).
- Seven structural-authority files byte-identical before / after readouts (primary
  ledger, validator script, guard criteria, guard ledger, mainline `pipeline-state.json`,
  baseline matrix, source manifest) ⇒ **zero write-back**.
- Mainline `pipeline-state.json`: `CCFA-startup passed`; **G0–G8 / validation / handoff
  all `pending`**; `G0.inputs=[]`, `G0.evidence=[]`.

## Strict boundary

Zero model forward / training / labels / dataset / EPE·l2 / scientific metrics; zero
gate promotion, zero self-certification, zero stage-status change; no change to
historical bytes, reviews, scores, thresholds, manuscript, gates, matrix, registry or
gate config; no `ccf-paper-reviewer full` run, no scored-verdict line, no self-assessed
governing; no v4 contract, no gate skipping, no assumption of the <=32h / K=45
confirmation authorisation, no 4090/L4/H20 capability claim; main project not submitted
/ committed / pushed. D1 discriminative prediction stays `BLOCKED_ON_CONFIRMATION`.

## Independent isolated recheck

A fresh fully isolated sub-agent was launched with **no expected verdict, no score
anchor and no conclusion anchor**, instructed to recompute groups A–H from source bytes,
adjudicate 12 named exaggeration classes and grade defects. **At the write time of this
checkpoint the report has NOT been recovered and NO recheck conclusion is claimed.**
This statement is TRUE at write time and these bytes will not be rewritten. The recovered
conclusion and any append-only corrections will be published in a **new immutable
checkpoint**, per the R117/R119–R124 precedent. This is a gate / evidence-layer recheck,
**NOT** a full manuscript review.

## Content safety

Full-repository strict pattern scan before push: credential value, token assignment,
email, local absolute path, credential filename, webhook, connection string, real
scored-verdict line — 0 new hits. No >50 MiB file, no binary, no dataset, no weight, no
third-party source code, no unsubmitted manuscript. Only explicit files staged via
`git add --`; no `git add .`; `git diff --cached --check` clean; push to own agent
branch; `git ls-remote` remote SHA must equal local HEAD before claiming uploaded. 21
earlier published checkpoints untouched; private `ZtL-sysu/novix-platform` untouched;
no merge / force push / branch deletion / Release.

## Result

Step-3 precondition (**substantive new positive scientific evidence**) unmet ⇒ no new
manuscript copy, no 9-page compliant compilation, no fresh isolated full review.
**0 papers qualified, no COMPLETE**; governing unchanged (R95 = 6.0 / Confidence 4.0),
`NOT_QUALIFIED` / `INCOMPLETE`; G0 pending; zero gate promotion / zero
self-certification / zero state change. Stop gates remain only (1) qualify (>= 7.0)
(2) goal owner stops. A checkpoint `completed` is work state, not scientific validation.

# R125 — version-attribution first-hand route exhaustion (SANITIZED summary)

**Nature**: read-only third-party public-text acquisition. `READONLY_VERSION_ROUTE_EXHAUSTION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`.
**Verdict at round level**: `G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`.
**Round**: R125 automation heartbeat, 2026-11-14 ~16:56–17:3x +0800. Heartbeat schedule unchanged (ACTIVE).

This document is a **redacted summary**. The 13 raw frozen byte files, the round
audit, the verifier scripts, the verification JSON, the validator/guard readouts and
the independent-review original are **NOT uploaded** (local-only under `<local>/`).
No dataset, weight, binary, credential, local absolute path, third-party source code
or unsubmitted manuscript is included in the public upload set.

## Why this round exists

R124's own isolated-review correction **M3** narrowed a prior claim to: the "v1 page
(positive)" abstract is a **WebFetch transcription with no local byte freeze**, NOT a
first-hand conclusion; the four positive numbers `0.686 / 0.846 / 0.930 / 0.603` occur
**zero** times across R124's 13 raw files. R124's hand-off then grouped "whether to
fetch the v1 page bytes" together with "classification / registration into the matrix
and source manifest" and passed the whole group to a designated gate owner.

R125 performs **only** the autonomous half — first-hand byte acquisition — and leaves
classification / registration / matrix finalisation / written-pass-criterion freezing
with the designated gate owner (decision groups G1 / G4 / G6 / G7 in the consolidated
decision register). Byte acquisition is a read-only action, not a gate decision.

R124 had tried only the `www.biorxiv.org/content/...v1` HTML path (four times, all
HTTP 429). The bioRxiv official details API itself publishes a `jatsxml` per-version
URL for each of its 12 version records; that **official per-version full-text route had
never been tried**. Two independent hosts (EBI Europe PMC, Internet Archive Wayback)
and a hypothesised `api.biorxiv.org` JATS endpoint were also untested.

## What was acquired (13 raw files / 135,063 B, each frozen verbatim + SHA-256)

| Route family | Result | Reading |
|:--|:--|:--|
| official per-version JATS, 5 variants (v1 canonical, v1 alternate path, v1 DOI form, v3, v12) | 5 x HTTP 429 / 17 B / `error code: 1015` — all five share one digest | negative, time-point scoped |
| EBI Europe PMC `fullTextXML`, 2 variants | 2 x HTTP 500 / 150 B | **structural**, not transient |
| EBI Europe PMC `resultType=core` | HTTP 200 / 6,367 B | **new third first-hand endpoint** |
| Internet Archive CDX + `/web/2026/` | `[]` (3 B) + HTTP 404 / 4,657 B | negative |
| `api.biorxiv.org/jats/...` | HTTP 404 / 196 B | endpoint does not exist |
| `api.biorxiv.org/details/.../1` | HTTP 200 / 64,741 B | byte-identical to R124's un-suffixed details response; independently reproduces "`/1` is not a version selector" |
| `connect.biorxiv.org/relate/content/181` | HTTP 200 / 58,714 B | byte-identical to R124's frozen copy; duplicate, not a new source |

Largest file 64,741 B (`api-details-v1.json`); second largest 58,714 B
(`connect-jats.xml`). A draft of this round's own unpublished documents stated
58,714 B as the maximum; byte-wise max computation during `metrics.csv` generation
exposed the error and it was corrected in place before publication. Zero local
absolute paths, credentials, datasets, weights,
binaries, or scored-verdict lines in the raw set (independent verifier group H: 6/6).

## Substantive findings (third-party text facts, strictly bounded)

**1. A third independent first-hand endpoint, carrying the SAME current abstract.**
Europe PMC `resultType=core` (EBI host, distinct from bioRxiv / Crossref / the
second-hand mirror) returns a complete `abstractText` of 4,847 characters. Its
similarity to the bioRxiv details API abstract (4,816 chars) is **0.9906**; all 22
difference operations are typographic / whitespace / hyphen / comma / name-transliteration
normalisation (`Erdős–Rényi` vs `Erdos-Renyi`, inserted `Maisak et al.`, Unicode minus),
with no substantive semantic difference. The abstract contains the negative wordings
`largely null result`, `disappears entirely`, `statistically indistinguishable`,
`size-matched`, `not the confirmation we set out to find`; the four "v1 positive"
numbers occur **zero** times.

Per the R124 M2/M3 correction, **the same abstract appearing at several endpoints is
not several independent sources**. R125 registers an **endpoint count +1**, NOT an
independent-source count +1, and makes **no version-attribution claim**. R124's M3
narrowing is therefore **strengthened, not overturned**.

**2. The official per-version JATS route is structurally unusable for version attribution.**
From R124's frozen details API bytes: `version` is a **string** field `'1'..'12'`;
**12 records share ONE abstract** (4,816 chars, SHA-256 prefix `555e28f9…`) and **2
distinct titles** (v1 differs from v2–v12); but `jatsxml` has only **10 distinct URLs** —
v3/v4 both point to `2026-06-23` and v8/v9 both to `2026-06-30`. So **even if the 429
cleared and every JATS full text were retrievable, two version pairs would remain
indistinguishable at the official endpoint**. This is an endpoint-side structural
limit, not a rate-limit artefact, and it is the first byte-level confirmation of the
practical ceiling on R106 section 6 item R3 ("mark the specific version").
All 12 records carry `license = cc_by` and EPMC carries `license = "cc by"` — these are
**record-level metadata declarations**, which per the R123 lesson are **NOT per-asset
licence text** and do **not** close gap 1.

**3. The Europe PMC 500 is structural, not transient.**
R124's frozen lite metadata and R125's core metadata agree on
`hasPDF=N / inEPMC=N / inPMC=N / isOpenAccess=N`; `fullTextUrlList` has exactly one
entry and it points only to a DOI resolver, i.e. Europe PMC holds **no full text** for
this preprint. The `fullTextXML` 500 is therefore not a retry candidate. EPMC
`dateOfCreation=2026-06-15`, `firstPublicationDate=2026-06-12`,
`firstIndexDate=2026-06-15` are index / first-publication dates, **not** the current
abstract's version (R124 lesson).

**4. Negative conclusion, reported as such.** The "v1 page has no local byte freeze"
gap left by R124 M3 **remains open** after exhausting the official per-version JATS,
Europe PMC full text, Wayback archive and `api.biorxiv.org` routes. The "v1 positive vs
current negative" version dichotomy **still has no first-hand byte support**. **R3 stays
OPEN.** No byte of R106 or R124 is rewritten; acquisition completion is NOT presented as
gap closure.

## Time-point / scope limits (anti-overclaim)

- HTTP 429 / 500 / 404 / empty-CDX results are scoped **strictly to the R125 acquisition
  instant (2026-11-14 ~17:0x +0800) and the exact URLs / hosts recorded in the
  acquisition map**.
- 429 is a **Cloudflare 1015 host-side rate limit, NOT permanent unavailability**:
  R124 obtained HTTP 200 from `api.biorxiv.org` and `connect.biorxiv.org` on the same
  day and reported an unsaved 200 / 105,400 B v1 HTML response. No claim of "permanently
  unfetchable" is made.
- The Wayback CDX query used `statuscode:200`, `limit=5` and a single URL form; "zero
  snapshots" is scoped to that query, not to "no archive anywhere".
- Character counts and similarity values are bound to the specific derived files and a
  declared normalisation convention (R122 C-1 / R124 M1 lessons).

## Reproducibility

`R125-verify.py` does **not** import the acquisition module and does **not** use any
R125-produced JSON as a substantive data source; it recomputes from the 13 raw byte
files plus R124's two frozen authority files: **93 checks / 93 MATCH / 0 MISMATCH**
(A 27 / B 6 / C 10 / D 24 / E 14 / F 4 / G 2 / H 6). Group A is a **same-machine
byte-identity consistency check, not an independent cross-source verification**; its
SHA literals come from a separate `shasum -a 256` measurement and none is invented.

Two verifier defects are retained and reproducible in place, both **script / expectation
defects, not data inconsistencies and not fabrication**: **V-1** (v1) `bytes` is not
JSON-serializable → `TypeError`; **V-2** (v2) expected `version` as ints but the API
returns strings → `91/92 MATCH, 1 MISMATCH (E-versions)`. v3 fixes both and adds an
explicit field-type check → 93/93. v1 and v2 files are kept; neither is overwritten.

## Double gates (read-only, at acquisition instant)

- validator: `NOT_QUALIFIED / 6.0 / >=7.0 / score_meets_threshold=false` (D1, D4 pass;
  D2, D3, D5 fail).
- guard: `INCOMPLETE` (A2, A6 fail).
- Seven structural-authority files are byte-identical before and after the readouts
  (primary ledger, validator script, guard criteria, guard ledger, mainline
  `pipeline-state.json`, baseline matrix, source manifest) ⇒ **zero write-back**.
- Mainline `pipeline-state.json`: `CCFA-startup passed`; **G0–G8 / validation / handoff
  all `pending`**; `G0.inputs=[]` and `G0.evidence=[]`.

## Strict boundary

Zero model forward / training / labels / dataset / EPE·l2 / scientific metrics;
zero gate promotion, zero self-certification, zero stage-status change; no change to
historical bytes, reviews, scores, thresholds, manuscript, gates, matrix, registry or
gate config; no `ccf-paper-reviewer full` run, no scored-verdict line, no self-assessed
governing; no v4 contract, no gate skipping, no assumption of the <=32h / K=45
confirmation authorisation, no 4090/L4/H20 capability claim; main project not
submitted / committed / pushed. D1 discriminative prediction stays
`BLOCKED_ON_CONFIRMATION`.

## Independent isolated recheck

A fresh fully isolated sub-agent was launched with **no expected verdict, no score
anchor and no conclusion anchor**, instructed to recompute groups A–H from source bytes,
adjudicate 12 named exaggeration classes and grade defects. **At the write time of this
checkpoint the report has NOT been recovered and NO recheck conclusion is claimed.**
The recovered conclusion and any append-only corrections will be published in a **new
immutable checkpoint**, per the R117/R119–R124 precedent; this checkpoint's bytes will
not be rewritten. This is a gate / evidence-layer recheck, **NOT** a full manuscript
review.

## Result

The step-3 precondition (**substantive new positive scientific evidence**) is unmet ⇒
no new manuscript copy, no 9-page compliant compilation, no fresh isolated full review.
**0 papers qualified, no COMPLETE**; governing unchanged (R95 = 6.0 / Confidence 4.0),
`NOT_QUALIFIED` / `INCOMPLETE`; G0 pending; zero gate promotion / zero
self-certification / zero state change. Stop gates remain only (1) qualify (>= 7.0)
(2) goal owner stops. A checkpoint `completed` is a work-state label, not scientific
validation.

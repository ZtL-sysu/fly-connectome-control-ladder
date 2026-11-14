# R125 — recovered independent recheck (SANITIZED summary)

**Nature**: gate / evidence-layer recheck by a fresh fully isolated sub-agent. **NOT** a
`ccf-paper-reviewer full` manuscript review; no scored-verdict line, no numeric paper
score, no self-assessed governing. Round verdict:
`G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`.

The independent-review **original is NOT uploaded** (contains one local absolute-path
literal and scan-pattern literals; R117 precedent). The 13 raw byte files, round audit,
verifier scripts, verification JSONs and validator/guard readouts are also local-only
under `<local>/`. No dataset, weight, binary, credential, local absolute path,
third-party source code or unsubmitted manuscript is in the public upload set.

## Recovery

The twenty-second checkpoint `20261114T093526Z-r125-version-route-exhaustion/`
truthfully stated **at its write time** that a fresh isolated recheck had been launched
but was NOT yet recovered, and claimed no recheck conclusion. Its `CHECKPOINT.md` mtime
was `17:38:35 +0800`; the independent report landed at `17:42:59 +0800` — so that
statement was TRUE at write time. Its bytes are **not rewritten**. Per the
R117/R119–R124 precedent, the recovered conclusion and append-only corrections are
published in a **new immutable checkpoint** — this one (twenty-third).

**Primary independent report**: **14,138 B / 94 lines / SHA-256
`15b5879315ed9c784c19dadc16b88c52365291dbe25d1a6bc2a6b2c6f482dcdf`**,
mtime 17:42:59, one write, no intermediate state, original unchanged. First line:
`REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO |
Forward pass performed: NO`.

The reviewer used ONLY the 13 raw byte files plus R124's two frozen authority files with
its own parsing logic — did not import the acquisition module or verifier, did not use
any R125-produced JSON as a substantive data source, read the round audit LAST as a
claim to be checked — ran no verifier / validator / guard / git / network, and modified
no existing file. Report has 0 numeric scored-verdict lines, 0 email literals, 0
credential values.

## Recheck outcome

**A–H all group values reproduce.** 13 filenames + sizes + SHA-256; total 135,063 B;
5 x 17 B Cloudflare `error code: 1015` bodies all sharing one digest; EPMC lite
`hasPDF=N / inEPMC=N / inPMC=N / isOpenAccess=N`, both preserved 500 bodies carrying
`"status":500` and the fullTextXML path; EPMC core metadata, one DOI-resolver full-text
URL, abstractText 4,847 chars, five negative wordings present, four "v1 positive"
numbers total 0; bioRxiv details API 12 records, `version` is a **string** `'1'..'12'`,
1 distinct abstract (4,816 chars, SHA prefix `555e28f9…`), 2 distinct titles,
**10 distinct jatsxml URLs**, 1 distinct licence value `cc_by`, v3/v4 and v8/v9 URL
collisions, v1 title differs from v2; Wayback CDX `b'[]\n'`, Wayback no-snapshot page,
api-jats 404 body; both byte-identity checks; scope/safety checks.

**12 named overclaim categories: CONFIRMED 0 / REFUTED 12**, each with byte evidence.
Defects **HIGH 0 / MEDIUM 1 / LOW 1**; **1 factual error / 1 data inconsistency (same
line) / 0 fabrication**. Reviewer independently confirmed all classified aggregate
numbers are reproducible by byte summation / counting.

**Reviewer scope limits (accepted)**: HTTP status codes are declared values not
replayable from bytes; group A is a same-host identity check, not cross-source
validation; reviewer did not run the verifier so the 93 checks / group counts were
checked for category and self-consistency only; workspace-level review-line counts,
governing / validator / guard / pipeline-state live readings, 7 structural-authority
SHAs, mtimes and historical narrative are outside what the 13 raw files prove and were
collected independently by the main session.

## Findings ALL ACCEPTED, append-only

In primary `R125-POST-REVIEW-CORRECTION.md` (9,234 B, SHA-256 prefix `42506bff7a15e89b`).
**No historical byte rewritten**: round-audit original, independent-review original,
v1/v2/v3 verifiers + VERIFICATION/V2, SOURCE-MANIFEST, all 13 raw files, and the
twenty-second checkpoint are byte-unchanged.

- **M1 [MEDIUM | factual error + internal inconsistency] — accepted.** Round audit
  `:41` "all 13 files <= 58,714 B" was false: the byte-max is **64,741 B**
  (`api-details-v1.json`), and 58,714 B is `connect-jats.xml`. **Time-point
  clarification (reviewer is NOT claimed wrong)**: the reviewer in its isolated session
  read a **pre-correction snapshot**; the main session had independently found the same
  error via byte-wise max computation during `metrics.csv` generation and corrected it
  in place in **this round's own unpublished drafts** (round audit, sanitized summary,
  twenty-second `CHECKPOINT.md`), with a self-correction note logged at `:42`. The
  twenty-second `CHECKPOINT.md` mtime 17:38:35 is EARLIER than the report 17:42:59, so
  the **published bytes were already corrected before the reviewer read them**. Impact
  is strictly one derived aggregate in a local unuploaded draft; no frozen byte,
  negative conclusion, double-gate reading, gate state, governing, 0-papers result or
  schedule changes. No byte of the round audit is rewritten.
- **L1 [LOW | cited-checker design weakness] — accepted.** The frozen verifier's H-group
  `noEmail` check counts a file only if it contains BOTH `@` and `.com`; the email-shaped
  strings are `.org`, so the check cannot establish "zero email literals". An
  independent domain-agnostic recheck (`R125-EMAIL-RECHECK.py/.json`) finds
  **occurrences=2, distinct=1 (a single public Internet Archive contact address (`.org` domain, redacted here))**, all in `wayback-v1.html`; the
  frozen weak check counted 0. Scope strictly limited: a **cited-checker weakness**,
  not an incorrect byte-level assertion in the audit (the audit's safety claims — no
  local paths / credentials / scored-verdict lines — were independently confirmed
  true); no published document claims "zero email literals in raw"; the word `email` in
  the twenty-second checkpoint appears only as a category name for the **full-repo
  upload-set** 8-class strict scan (0 hits); all 13 raw files are NOT uploaded and the
  address is a public Internet Archive contact, not a project credential. Frozen
  verifier versions are NOT rewritten (93/93 stays reproducible).
- **C1 [supplementary byte fact] — accepted.** `connect-jats.xml` is actually a bioRxiv
  **about-page HTML** (canonical `http://biorxiv.org/about-biorxiv`), NOT JATS full text,
  and contains **no abstract**; the current negative abstract appears in the 13 raw
  files only in `epmc-core.json` and `api-details-v1.json` (the latter byte-identical to
  R124's frozen file). This STRENGTHENS "connect is a duplicate, not a new source" and
  "endpoint count +1 != independent-source count +1". The `jats` in the filename is
  only an acquisition label.
- **C2 [convention narrowing] — accepted.** Similarity `0.9906` is specific to
  `difflib.SequenceMatcher(None, biorxiv_api_abstract, epmc_core_abstract).ratio()`
  with default `autojunk` and that argument order. The reviewer obtained 0.8997 with
  reversed order + default autojunk, 0.9945 with autojunk off, 0.9953–0.9978 after
  Unicode/hyphen/whitespace normalisation — all supporting the SAME qualitative
  conclusion (same text, typographic differences only). Reviewer judged this a
  convention difference, not a data error. The numeric value must not be quoted
  without declaring argument order and normalisation (R122 C-1 / R124 M1 lesson).
- **C3 [time-point / declared-value limits] — accepted.** No literal `429` in raw;
  `1015` is a Cloudflare body; HTTP 429/500/404/200 are declared curl status values.
  `wayback-v1.html` is a Wayback "not archived" page with no literal `404`/`Not Found`.
  Reviewer cannot verify whether `api-details-v1.json` / `connect-jats.xml` were
  independently re-fetched (only byte-identity to R124 frozen files), nor workspace-level
  counts / governing / gates / SHAs / mtimes / history — all collected separately by the
  main session.

## Scope of impact

All five findings are wording / convention / supplementary-fact narrowings; **none adds
a claim**. None changes: 13 raw bytes and SHA-256, SOURCE-MANIFEST, v3 **93/93 MATCH / 0
MISMATCH**, A–H group values, 12 categories REFUTED 12, double gate
(`NOT_QUALIFIED / 6.0 / >=7.0`, `INCOMPLETE`), gate state (G0 pending, G1–G8 all
pending, `inputs=[]`/`evidence=[]`), governing **R95 = 6.0 / Confidence 4.0**,
**0 papers qualified / no COMPLETE**, the R106 §6 convergence table, or the heartbeat
ACTIVE schedule.

## Content safety

Full-repository strict pattern scan before push: credential value, token assignment,
email, local absolute path, credential filename, webhook, connection string, real
scored-verdict line — 0 new hits. No >50 MiB file, no binary, no dataset, no weight, no
third-party source code, no unsubmitted manuscript. Only explicit files staged via
`git add --`; no `git add .`; `git diff --cached --check` clean; push to own agent
branch; `git ls-remote` remote SHA must equal local HEAD before claiming uploaded. 22
earlier published checkpoints untouched; private `ZtL-sysu/novix-platform` untouched;
no merge / force push / branch deletion / Release.

## Result

Step-3 precondition (**substantive new positive scientific evidence**) unmet ⇒ no new
manuscript copy, no 9-page compliant compilation, no fresh isolated full review.
**0 papers qualified, no COMPLETE**; governing unchanged (R95 = 6.0 / Confidence 4.0),
`NOT_QUALIFIED` / `INCOMPLETE`; G0 pending; zero gate promotion / zero self-certification
/ zero state change. Stop gates remain only (1) qualify (>= 7.0) (2) goal owner stops.
A checkpoint `completed` is work state, not scientific validation.

## New lessons carried forward

1. A cited checker's "zero hits" check must use a domain/shape-agnostic regex;
   conjunctive conditions like `@`+`.com` produce silent false negatives, and any
   "zero X literals" claim must be bound to a concrete file set with a program value.
2. A similarity number must be bound to argument order / autojunk / normalisation;
   different conventions can differ by ~0.09.
3. A third-party error page may contain no literal HTTP status code; status is a
   declared value and must be listed separately.
4. Filename / label != content type (this round's `connect-jats.xml` is an about-page
   HTML with no JATS and no abstract); judge from bytes.
5. When the same derived-aggregate error is found independently by both the reviewer
   and the main session, state the **snapshot time-point difference**; claim neither
   party wrong and rewrite no published byte.

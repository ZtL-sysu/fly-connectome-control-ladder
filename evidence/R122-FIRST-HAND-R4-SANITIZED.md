# R122 — R106 §6 R4 first-hand source freeze (sanitized public summary)

Status: `READ_ONLY_FIRST_HAND_SOURCE_FREEZE_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
Date: 2026-11-14 (heartbeat R122, unattended)
Primary project artifacts (raw bytes, scripts, JSON, round audit, independent
review original) are **NOT uploaded**. Local paths are written as `<local>/`.
Third-party full-text HTML containing an author email is excluded.

## What was done

Closed the *evidence-acquisition* sub-item of R106 §6 **R4** (repeatedly named
in R106/R107/R118/R120, not landed in 11 prior rounds): local, SHA-anchored
first-hand freeze of the prior-art article `arXiv:2609.24565` (v1 + v2), which
is the basis of the G0 gap-2 and G4 (time-scale sweep) positioning.

Five raw byte files, all HTTP 200, fetched 2026-11-14:

| file | bytes | sha256 (first 16) |
|:--|--:|:--|
| `arxiv-2609.24565v1-abs.html` | 41,581 | `0075412eb1044786` |
| `arxiv-2609.24565v2-abs.html` | 43,656 | `cbcbce7343f999eb` |
| `arxiv-2609.24565v1-html.html` | 50,485 | `2726ef63d6cda793` |
| `arxiv-2609.24565v2-html.html` | 182,710 | `f4e7fb8747165a4f` |
| `arxiv-2609.24565-api.xml` | 3,139 | `5e1c68e2e21be996` |

Endpoints: arxiv.org `/abs/2609.24565v1`, `/abs/2609.24565v2`,
`/html/2609.24565v1`, `/html/2609.24565v2`, and the export.arxiv.org atom
query `?id_list=2609.24565`.

## Substantive first-hand finding

**The same v2 carries two materially different official abstracts** — this is
a third-party version fact, not a project result:

- v2 `/abs/` abstract == atom `<summary>`, verbatim, **1,534 chars** (verifier D1).
- v2 HTML body-embedded abstract = **1,943 chars**, NOT equal to the above;
  `difflib.SequenceMatcher` ratio **0.4717**, 38 non-equal opcodes (D3/D4).
  - The abs/API abstract contains the time-scale sweep conclusion
    ("Longer observations reverse the circuit-receptor ordering once the
    stimulus spans a period, but not through T4/T5 ...").
    The body-embedded abstract does NOT; it ends with "Exact structure remains
    insufficient to beat what the moving retina already provides."
- v1 abs abstract = **1,433 chars**, different from both v2 abstracts;
  v1 and v2 **titles also differ** (v1 "Active Visual Sampling with a
  Connectome-Constrained Fly Model ..."; v2 "What Survives on Real Drawings:
  Active Sampling, Connectome Wiring, and Matched Baselines ...").
- v2 HTML: 37 section headings / 182,710 B; v1: 16 / 50,485 B.

This gives byte-level first-hand support for R106 §3 / R107 R2's statement
that two differently worded v2 abstracts coexist on arXiv, and explains why
the R99 citation dispute produced endpoint-dependent readings. **No claim is
made that R106 was wrong, and no existing verdict is rewritten.** The
increment is turning an 11-round transcription-only object into recomputable
bytes.

### Version-time evidence (two `updated` values strictly separated)

- v2 abs page `Submission history`: `[v1] Mon, 21 Sep 2026 13:30:30 UTC
  (3,306 KB)` / `[v2] Tue, 22 Sep 2026 12:24:47 UTC (3,306 KB)`.
- Atom **entry-level**: published `2026-09-21T13:30:30Z`, updated
  `2026-09-22T12:24:47Z` — matches the abs page verbatim.
- Atom **feed-level** `2026-11-14T03:57:55Z` is the **query generation time**,
  NOT an article version update. Verifier C5/C6 separate them. No claim that
  the article or its abstract changed today.

## G4 positioning needles verified from raw bytes (R106 §3)

- Section **7.3 "The stimulus never completes a cycle"**: 8 frames cover
  roughly 1/5–9/10 of one spatial period; 0.16 s window shorter than one
  cycle; 40-frame long-look variant 0.826 vs short drift 0.871.
- Section **8 "What the sampling sweep answered"** (verbatim): "the circuit
  does overtake the receptors-only descriptor once the observation passes a
  single period, by +0.033 [0.015,0.050] relative to the short window, and
  spectral bands carry a consistent +0.085 to +0.102. But the mechanism is
  not the one we named: the T4/T5 contribution does not grow with length."
- Section **8 "What remains open"** (verbatim): "Two gaps remain." —
  (i) wire-length null cannot be built from available coordinates;
  (ii) no real-document benchmark with independent human annotation.
- Verifier E1–E16 all matched, including `+0.033`, `[0.015,0.050]`,
  `T4/T5`×4, `0.271`/`0.356`×3, `721`×5, `1,876`×5, `0.505`×2,
  `0.415`×3, `9 Limitations`.

R106's G4 center judgment (the discriminative "when does the pathway matter"
axis is partly pre-empted by v2 §7.3/§8) is therefore supported by
first-hand bytes. G4 status is unchanged; the baseline matrix is NOT
finalized (that is decision G6, requiring a designated gate owner).

## Reproducibility

`R122-verify.py` does NOT import the acquisition module, does NOT read any
R122-produced JSON as a data source, and does NOT read the round audit;
it recomputes from the five raw byte files with its own parsing logic:
**47 checks / 47 MATCH / 0 MISMATCH**.

Scope note written into the verification JSON: A1–A4 are same-host byte
identity checks (necessarily consistent by construction), NOT independent
cross-verification; B–F are the substantive first-hand observations. A fresh
isolated sub-agent recheck was launched with no expected verdict, no score
anchor and no conclusion anchor; at this checkpoint's write time it had NOT
been recovered, so **this checkpoint claims no recheck verdict, no defect
list and no confirmation**. Recovered conclusions and append-only corrections
go into a NEW immutable checkpoint; this checkpoint's bytes are not rewritten.

## Strict boundary

- **No write-back to any pre-existing registry / matrix / state / gate
  config.** `literature-search/source-manifest.json` (the "register" half of
  R4), `literature-baseline-matrix.md` (R2 finalization), and
  `pipeline-state.json` are byte-unchanged. Those are decision groups G7 / G6
  and require a designated gate owner. This round only supplies a
  round-local `R122-SOURCE-MANIFEST.json` as a pending-approval attachment.
- **Zero gate promotions**: G0 remains `pending`, no `passed` / no
  `gate_verdict` change, no `history` append.
- **EXEC LOCK**: zero model forward / inference / training / labels /
  dataset / EPE·l2 / scientific metric / new positive evidence. Only
  read-only HTTP fetch, SHA recomputation and text extraction.
- **Zero manuscript / review activity**: no `ccf-paper-reviewer full` launched,
  no numeric scored-verdict line produced, no self-assessed governing, no
  score / threshold / review / frozen-artifact / historical-byte change, no
  assumption of the `<=32h / K=45` confirmation-panel authorization (D1 stays
  `BLOCKED_ON_CONFIRMATION`), no v4 contract created.
- No P3 forward pass (G0 not passed), no gate skipping, no 4090 / L4 / H20
  capability claim, primary project not submitted / committed / pushed.
- **The increment is evidence-layer, not score-layer.** Per the negative
  closure established in R121 (governing review's own §13 evidence-capped
  overall rule), a first-hand literature freeze does NOT change the governing
  6.0 and is NOT "progress toward qualifying". It only closes R4's acquisition
  sub-item and supplies the previously missing recomputable basis for G0
  gap 2 and G4.

## Double gate (read-only, this round)

| gate | reading |
|:--|:--|
| `readonly-validator/validate_single_paper.py` | `NOT_QUALIFIED` · 6.0 · threshold 7.0 · `>=` · `score_meets_threshold=false` · D1✓ D2✗ D3✗ D4✓ D5✗ |
| `guard check` | `INCOMPLETE` (A2/A6 FAIL, S1–S7 all pending, 0 action entries) |
| main-line `pipeline-state.json` | CCFA-startup passed; G0–G8 / validation / handoff all pending; G0 `inputs=[]`, `evidence=[]` |

A6 dual wording (criteria `>=7.0` vs ledger `strictly > 8.0`) is a known
issue, read-only registered, not changed.

## Result

**0 papers qualified, no COMPLETE written.** Governing remains
**R95 = 6.0 / Confidence 4.0**, `NOT_QUALIFIED` / `INCOMPLETE`. Only two stop
gates remain: (i) a new isolated full review >= 7.0 with QUALIFIED + COMPLETE,
(ii) the user calling a stop. Heartbeat ACTIVE schedule unchanged.

## Handoff to next round

1. Recover the fresh isolated independent recheck; put conclusions and any
   append-only corrections in a NEW immutable checkpoint.
2. R4's remaining "register into `source-manifest.json`" and R2's matrix
   finalization require decisions G7 / G6; the heartbeat must not self-write.
3. Only admissible path: G0–G8 in order (G4 addressing v2 §7.3/§8/§9) →
   validation → handoff → P0 → P1A/P1B → P2 → **P3 baseline-first real
   forward pass** with substantive positive new evidence → new manuscript
   copy → compliant 9-page compile → fresh isolated full review (no score
   anchor) → COMPLETE only if >= 7.0 and QUALIFIED + COMPLETE.
4. Use `R120-CONSOLIDATED-DECISION-REGISTER.md` as the single decision entry
   (minimal set G1 + G4 + G10).

**New lessons**: (i) citing a "v2 abstract" must name the endpoint — abs/API
and HTML body versions differ (ratio 0.47); (ii) atom feed `updated` is query
time, separate from entry-level version time; (iii) two coexisting v2
abstracts are a third-party version fact, not a project result or a scoring
basis; (iv) "save first-hand bytes" and "register into the registry" are two
distinct actions — the latter needs gate-owner approval, so R4 must not be
used as a pretext for self-write-back.

A checkpoint `completed` is a work-state label, not scientific validation.

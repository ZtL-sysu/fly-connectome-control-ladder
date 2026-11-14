# Discriminative prediction proposal v2 — PROPOSED, NOT ACCEPTED

Date: 2026-11-12. Supersedes `discriminative-prediction-proposal-v1.md` after the
independent review in `discriminative-prediction-independent-review-v1.md`
(verdict `revise`, close to `reject`, with a FATAL R–Δ coupling finding).
v1 is retained as superseded design evidence, not deleted.

Status: **still a proposal.** No contract, gate, frozen artifact, identity,
threshold, score or manuscript is changed by this document. Under
`f-guidance-builder-v1` / `f-research-v1`, acceptance requires an independent
design + idea review, then a versioned v4 contract that reopens P0 and reaccepts
P1A/P1B in order. No number has been computed.

---

## 0. Dispositions of the review, in order

| Review finding | v2 response |
|:--|:--|
| **FATAL**: `R` and `Δ` share the original decoder output (as subtraction reference AND `q` denominator) → mechanical coupling; falsifiers did not test it | §2 replaces the raw slope with a **partial / incremental-validity** gate plus five explicit original-output placebos; §3 adds a coupling-specific killer falsifier D0 and a diagnostic panel |
| **MAJOR**: new primary gate silently changes `K=45` / α=.05 structure; seven comparators are defined for `q`, not `Δ`; "unchanged" is inaccurate | §4 declares D1 as **co-binding with an explicitly revised K**, freezes comparator adaptation, and withdraws the "unchanged" wording |
| **MAJOR**: `R` needs flow labels but Sintel TEST labels are withheld; 4 scene clusters have no power; D1 undecidable without unauthorized confirmation | §5 redefines the labelled split honestly, states D1 is **not decidable in the development pilot**, and separates pilot-diagnostic claims from confirmation claims |
| Sign convention, unit of `Δ`, "either way discriminating" overclaim | §1 freezes the sign convention and units; the overclaim is withdrawn |

---

## 1. Frozen definitions (corrected)

For frozen checkpoint `m`, clip `c`, arm `a ∈ {response, geometry, magnitude,
shuffled, random}` on the **same edited original edges**:

- `q(c,a)` = RMS(null vs original decoder flow) / RMS(original output), floor
  `1e-6`, exactly as in `response-null-prediction-dataflow-v1.md`.
- `Δ(c) = median_a q(c,a) − q(c,response)` — path-preservation advantage.
  **Unit: dimensionless `q` units** (not `delta_noise` units). Ties and the
  allowed case where a random draw coincides with the response arm are resolved
  by a predeclared deterministic rule and logged; coincident masks are reported,
  never excluded.
- `R(c) = EPE_input-only-ridge(c) − EPE_frozen-circuit(c)`. **EPE is an error,
  lower is better; `R > 0` therefore means the frozen circuit is MORE accurate
  than the input-only ridge on that clip** (the circuit's extra computation is
  task-useful). This sign convention is now frozen. Kuklev's held-out finding
  (receptors `0.894` > fly `0.835`) corresponds to `R < 0` under the analogous
  comparison; the mapping is stated, not assumed to transfer across metrics.
- Both are aggregated equally over clips within a scene, then over scenes; the
  same cluster structure is used in every bootstrap replicate.

**No ground-truth flow labels from official Sintel TEST are used.** See §5.

---

## 2. Primary gate: incremental validity, not raw correlation

The v1 primary gate (clustered lower bound > 0 for the raw within-scene slope of
`Δ` on `R`) is **withdrawn**: it cannot distinguish a path-preservation mechanism
from shared-output coupling.

### 2.1 Nuisance basis `N(c)` (frozen before any outcome is opened)

`N` contains only quantities available without null outcomes or labels beyond
the frozen labelled development split:

1. `RMS(original decoder output)` — the `q` denominator itself.
2. original-output temporal variance and channel-wise RMS profile.
3. a **clip-difficulty proxy**: scene-mean input luminance contrast and the
   input-only ridge's own EPE.
4. achieved evoked dose / active mass of the edited edge set.
5. realized geometry features (endpoint length, direction bins) and magnitude
   features from `paired-edge-set-executable-spec-v3.md`.
6. **arm-mean** `q̄(c) = mean_a q(c,a)` — the clip's overall perturbability.

All columns are standardized on calibration rows only.

### 2.2 Gate G-D1 (one-sided, co-binding)

Fit `Δ ~ N` and `Δ ~ N + R` with the same prespecified scene-grouped estimator.
**G-D1 passes iff the clustered 95% lower bound on the partial coefficient of
`R` (within-scene, nuisance-conditioned) is > 0**, AND the nested paired
bootstrap improvement in out-of-scene prediction of `Δ` over `N` alone excludes
zero. Cluster bootstrap preserves arm/checkpoint/scene/mask pairings and
recomputes calibration inside each replicate, as in the frozen protocol.

### 2.3 Five original-output placebos (all must be beaten)

`R` must show strictly larger held-out incremental validity than each of:

- **P1 scale placebo**: `RMS(original output)` used *as the predictor*.
- **P2 difficulty placebo**: the clip-difficulty proxy alone.
- **P3 norm-matched shuffled trajectory**: a trajectory with matched per-frame
  norms but shuffled neuron correspondence (fixed family seed), carried through
  the same frozen decoder.
- **P4 difficulty-matched scene permutation**: `R` values permuted within
  difficulty strata across scenes.
- **P5 dose placebo**: achieved evoked dose / active mass alone.

Beating a placebo = paired out-of-scene improvement interval excluding zero,
frozen before outcomes. **Any placebo performing as well as `R` fails D1.**

### 2.4 Coupling diagnostic panel (reported regardless of outcome)

`corr(R, original-output RMS)`, `corr(R, q̄)`, `corr(R, dose)`,
`corr(Δ, original-output RMS)`, and the variance-inflation of `R` given `N`.
If `|corr(R, q̄)|` or `|corr(R, RMS)|` is large, the result is reported as
**non-discriminating** even if G-D1 passes. This panel is descriptive and cannot
rescue a failed gate.

**Terminology correction from the review**: this is a **shared-variable
mechanical coupling**, not classical outcome leakage (no null outcome enters
`R`). The remedy is conditioning + placebos, not further isolation sentinels —
although the frozen isolation sentinel of
`response-null-prediction-dataflow-v1.md` remains mandatory for the forecast
side.

---

## 3. Falsifiers (rewritten; D0 is the coupling killer)

- **D0 (coupling)**: after conditioning on `N`, `R` adds no held-out predictive
  value, OR any of P1–P5 predicts `Δ` as well as `R`, OR the coupling diagnostic
  panel shows the relation is driven by output scale / clip difficulty. **D0
  alone kills D1.**
- **D1 (incremental gate)**: G-D1 fails (partial slope CI includes zero, or the
  out-of-scene improvement interval includes zero).
- **D2 (controls)**: `geometry`, `magnitude` or `shuffled-response` arms predict
  `Δ` as well as the response arm, or `corr(R, dose)` is large and a
  dose-matched subgroup loses the relation.
- **D3 (selection/isolation)**: `R` computed without any mask-selection
  information reverses the conclusion, or the frozen isolation sentinel fails.
- **D4 (generalization)**: the relation holds only on development scenes,
  reverses on the scene-disjoint labelled split, or fails on independent mask
  families.
- **D5 (prerequisites / integrity)**: `delta_noise` ineligible or unstable;
  competence gates fail; `rawSMD > .1` on any arm; sensitivity to the `1e-6`
  normalization floor changes the sign (report the ineligible fraction and a
  varied-floor analysis); any frozen identity, seed or stop rule was altered.

Failures are retained and returned to the earliest affected design gate. A null
D1 is **not** claimed as a discriminating result (the v1 overclaim is withdrawn).

---

## 4. Contract status: explicitly co-binding, NOT "unchanged"

The v1 wording "nothing is relaxed / K=45 unchanged" was **inaccurate** and is
withdrawn. Adding a primary endpoint changes the multiplicity structure.

- D1's G-D1 is declared a **new co-binding directional endpoint**. A versioned
  v4 contract must specify the revised `K` and the family-wise `alpha=.05`
  allocation across the frozen 21 E1 gates, 24 E2 gates, and the new D1 gate(s),
  **before** any confirmation outcome is opened. No alpha is spent twice; no
  post-hoc endpoint is added after seeing results.
- The seven frozen comparators of `response-null-prediction-dataflow-v1.md` are
  defined for predicting `q`. Their adaptation to predicting `Δ` must be frozen
  and sealed (same calibration split, same ridge grid, no outcome access).
- LOGO sign/rank is **secondary/descriptive**, not a binding gate: with four
  scene clusters it lacks power. Its majority-baseline threshold and tie rule are
  frozen but it cannot carry the main claim.
- Everything **not** named above remains frozen: three arms, noise-only
  calibration (std `.08`, lower clamp, four draws, frozen seed key), paired-edge
  common edited support, `rawSMD<=.1`, 100,000 bootstrap replicates, sealed
  confirmation identities, stop rules. **These are unchanged; the endpoint
  family is not.**

---

## 5. Executability, stated honestly

- **Labelled split**: official Sintel TEST flow ground truth is withheld, so `R`
  cannot be computed on TEST. The "held-out" evaluation set for D1 is therefore
  a **scene-disjoint split of the labelled development scenes only**, frozen in
  `prospective-identities-v1.json`. Any claim of generalization beyond that
  labelled pool is explicitly out of scope. TEST images remain available for
  paired function agreement only, as the frozen protocol already states.
- **Power**: with 2 models × 4 scenes × 2 windows × crop1 (16 clip units, 4
  scene clusters), a clustered partial-slope CI and a 5-placebo comparison have
  **essentially no power**. A precision analysis from actual pilot variance is a
  **prerequisite** (P2 → before confirmation, per the frozen protocol). If the
  conservative precision requirement for G-D1 is infeasible within the cap,
  return to design; do not relax alpha or the placebo set.
- **Therefore D1 is NOT decidable in the development pilot.** The pilot can only
  establish: competence, dose/common support, noise calibration, geometry
  balance, control separation, transfer, and the coupling diagnostic panel as
  feasibility evidence. **No pilot result may be presented as a D1 test.**
- **Confirmation**: the ≤32h / K=45 formal panel remains **unauthorized** by
  `execution-contract-v3.md`. D1 can only be adjudicated after an explicit user
  authorization of a confirmation contract that includes the revised K. Request
  it only when pilot evidence is credible.
- **Runner**: `startup-stage-plan.md` says the scientific null runner and
  predictor are not yet completed/isolated/reviewed. They must be finished,
  SHA-frozen and independently audited before any D1-relevant number exists.
  `run_local_baseline_v2.py`'s `P0/P1/P1A/P1B/P2` guard is not bypassed.
- **Compute**: inference-only work is plausible on the working L4 23GB route,
  but no GPU capability is claimed for this proposal and no experiment is
  launched by this document.

---

## 6. Ordered prerequisites (unchanged in spirit from v1, tightened)

1. Independent design + idea review of **v2** (v1 review was `revise`; a fresh
   independent verdict on v2 is required — no self-acceptance).
2. Versioned **v4 contract** reopening P0, reaccepting P1A/P1B, with the revised
   K/alpha allocation and the sealed `Δ`-comparator adaptation.
3. G0–G8, validation, handoff in canonical order, each with its own substantive
   review. G4 must resolve prior art against Kuklev 2026, Park 2026,
   Dhawan 2026 and the 2026 representational-geometry study.
4. Complete / isolate / SHA-freeze / independently audit the scientific null
   runner and predictor.
5. Pilot gates in order: competence → dose/common support → noise calibration →
   geometry balance → control separation → transfer → **precision analysis**.
   Any failure returns to the earliest affected design gate.
6. Explicit user authorization of the confirmation contract; only then may
   sealed confirmation outcomes be opened and G-D1 adjudicated.

---

## 7. Explicit non-claims

- No positive visual effect, no D1 result, no number is reported here.
- No existing contract, gate status, frozen identity, score, threshold or
  artifact is changed.
- No claim that Kuklev 2026 is wrong; it is prior art that sharpens the question.
- No assertion that a null D1 would be informative at the pilot's sample size.
- No commit, push, submission or publication.

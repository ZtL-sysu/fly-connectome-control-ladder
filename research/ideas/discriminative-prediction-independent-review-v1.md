# Independent review — discriminative-prediction-proposal-v1

Reviewer: isolated `general-purpose` reasoning sub-agent `d1-independent-reviewer`,
no visibility into the authoring conversation. Date: 2026-11-12.
Mode: independent scientific review of a **proposal** (not a manuscript review,
not a score, not a governing CCFA full review).

Verdict: **`revise` (close to `reject`)** — because the central loop between the
predictor `R` and the outcome `Δ` is a shared-variable mechanical coupling that
the current falsifiers do not test, and because the proposal is not executable
inside the authorized evidence envelope.

This file preserves the review verbatim in substance. It is retained as evidence;
no part of it is softened or deleted.

---

## 1. Novelty — `revise` / partially non-trivial, but at risk of being definitional

The proposal correctly identifies that Kuklev 2026 already supplies the positive
topology effect (`0.857` vs `0.539`, `+0.318 [0.296,0.339]`, 3 seeds; R7/R8
positive control `0.092`) and then bounds it (held-out `receptors only 0.894` vs
`fly+drift 0.835`; `0.961` vs `0.962` with a CNN decoder; T4/T5 dispensable).
Asking *when* path preservation matters rather than *whether* wiring helps is a
legitimate and more discriminating question.

But as written, D1 risks being a **definitional restatement**: `R > 0` means the
frozen circuit beats an input-only descriptor, which is close to saying "the
circuit's computation is used"; `Δ > 0` means the response-matched null disrupts
the frozen function less. A reviewer can read "clips where the circuit is used
are clips where preserving its path matters" as near-tautological. The proposal
must state exactly what observation would be surprising, and must show that the
relation is **incremental over** dose, geometry, magnitude, and output-scale
placebos — not just present.

## 2. Circularity / tautology — **FATAL as written** (most important finding)

Both `R` and `Δ` are functions of the **same frozen circuit output** on clip `c`:

- `EPE_frozen-circuit(c)` is computed from that output.
- `q = RMS(null − original decoder flow) / RMS(original-output)` also uses that
  output, both as the subtraction reference and as the denominator.

Consequences the proposal does not currently address:

1. **Shared-denominator / shared-reference coupling.** Any clip-level variation
   in the original output's norm or structure moves `R` and `Δ` together,
   mechanically, with no path-preservation mechanism involved. A low-RMS clip
   can inflate `q` for every arm; a high-RMS clip compresses them.
2. **Clip difficulty is a common cause.** Hard clips raise `EPE_frozen-circuit`,
   lower `R`, and plausibly change `q` for all arms. The observed slope could be
   a difficulty effect.
3. **The five falsifiers do not test this.** Falsifier 3 (shuffled-response `R`)
   permutes a *different* object and does not remove the shared output. Falsifier
   2 (other arms predict equally well) is about arm discrimination, not about
   `R`–`Δ` coupling. No falsifier compares the primary relation against an
   output-scale or clip-difficulty placebo.

**Required fix**: replace the raw correlation/slope primary gate with an
**incremental-validity** design:
- Regress `Δ` on a prespecified nuisance basis (original-output RMS, clip
  difficulty proxy, evoked dose, geometry/magnitude features, arm-wise mean `q`),
  then test whether `R` explains residual variance.
- Add explicit placebo predictors derived only from the original output:
  output RMS, output temporal variance, a norm-matched shuffled trajectory,
  and a difficulty-matched scene permutation. `R` must beat all of them on
  held-out scenes.
- Add a **partial-slope** gate (slope of `Δ` on `R` conditional on the nuisance
  basis) with a clustered CI lower bound > 0, plus a scene-level permutation
  test that preserves each scene's `q` distribution.
- Report `corr(R, arm-mean q)` and `corr(R, original-output RMS)` as diagnostics;
  if either is large, the "prediction" is not discriminating.
- State that this is a shared-variable coupling, not classical outcome leakage;
  the fix is different (conditioning/placebos), and the proposal currently
  conflates the two.

## 3. Falsifiers — incomplete

Beyond the coupling placebos above, missing cases:

- **Dose/confound collinearity**: `R` may simply proxy the achieved evoked dose
  or active mass. Must report corr(R, dose) and a dose-matched subgroup analysis.
- **Balance failure**: if `rawSMD > .1` on any arm, `Δ` is confounded; this is
  listed as a stop rule but must be an explicit falsifier with the realized
  values reported.
- **Normalization-floor artefacts**: clips near the `1e-6` RMS floor can
  generate extreme `q`; the rule "mark reference-ineligible and report" is good
  but must include a sensitivity analysis with the floor varied and the
  ineligible fraction stated.
- **Selection leakage**: response-arm masks are selected using development
  responses; if the same responses enter `R`, the relation is partly selected.
  Need an isolation sentinel showing `R` computed without any mask-selection
  information gives the same conclusion.
- **Multiple endpoints**: the new D1 slope plus LOGO sign/rank creates new
  endpoints. Their relation to the frozen `K=45` family and family-wise
  `alpha=.05` is undecided — see §4.

## 4. Consistency with the frozen protocol — **not fully consistent**

The proposal says "nothing is relaxed", but it **adds** a new primary gate
(clustered slope lower bound > 0) and a new LOGO sign/rank requirement without
specifying how they enter the frozen multiplicity structure:

- `response-null-protocol-closure-v4.md` fixes `K=45` one-sided directional
  gates at family-wise `alpha=.05` (21 E1 + 24 E2 across three arms). Adding D1
  endpoints either (a) increases K, or (b) tests outside the family. Both must
  be declared and versioned; neither is "unchanged".
- The seven frozen comparators in `response-null-prediction-dataflow-v1.md` are
  defined for **predicting q**, not for predicting `Δ`. Their adaptation to `Δ`
  must be frozen and sealed before outcomes, with the same calibration split.
- "LOGO sign/rank beating the majority baseline" needs its baseline threshold
  and tie handling frozen; the majority baseline depends on the sign balance of
  `Δ`, which is unknown a priori.
- `median_a q_control` over five arms needs a predeclared rule for ties and for
  the (allowed) case where random-arm matching coincides with the response arm.

**Required**: either declare D1 as an explicitly **new, co-binding** endpoint
with a revised K and alpha allocation in a versioned contract (which reopens
P0/P1A/P1B as the proposal already says), or state it as a secondary/exploratory
analysis that cannot carry the paper's main claim. Do not call it "unchanged".

## 5. Feasibility inside the authorized envelope — **not executable as written**

- `R` requires `EPE` against **flow labels** on held-out scenes.
  `response-null-prediction-dataflow-v1.md` states official Sintel TEST flow
  ground truth is withheld, and `response-null-protocol-closure-v4.md` says
  TEST supports *paired function agreement only*. So `R` cannot be computed on
  genuine held-out TEST scenes. The proposal's "held-out scenes" must be
  redefined as **development-only, scene-disjoint labelled splits**, and that
  weakens the generalization claim.
- With `pilot-input-manifest-v2.json` = 2 models × 4 scenes × 2 windows × crop1
  (=16 clip-level units, 4 scene clusters), a clustered slope CI and LOGO over
  4 clusters has essentially no power. This is a precision/power problem, not a
  reason to relax thresholds.
- Therefore D1 is **not decidable in the development pilot**. It necessarily
  depends on the ≤32h confirmation panel, which `execution-contract-v3.md`
  says is **not authorized**. The proposal acknowledges the authorization gap
  but still frames D1 as the pilot's payoff; that framing is misleading.
- On L4 23GB the compute is plausible for inference-only work (the frozen
  scripts are pure NumPy / frozen forward), but the scientific null runner and
  predictor do not yet exist per `startup-stage-plan.md`, so no D1 number can be
  produced now.

## 6. Other corrections

- `EPE_input-only-ridge − EPE_frozen-circuit`: sign convention must be stated
  (EPE is an error, so lower is better; `R>0` as written means the ridge is
  *worse*, i.e. circuit is better — confirm and freeze this).
- "Either way it is a discriminating result, not a benchmark increment" is an
  overclaim. A null/failed D1 with 4 scene clusters is uninformative, not
  discriminating. Withdraw or condition on a power analysis.
- `q` is unit-normalized by `delta_noise` in E2 but `Δ` is a difference of `q`s;
  state units and whether the half-unit criterion transfers.

## 7. Verdict and the three most important revision requirements

**Verdict: `revise` (close to `reject`).**

1. **Remove the R–Δ shared-variable coupling as the primary design**: make the
   gate a partial/incremental-validity test with explicit original-output placebos
   and nuisance conditioning, and rewrite the falsifiers so at least one directly
   kills the proposal if the coupling explains the relation. (FATAL)
2. **Resolve the contract inconsistency**: declare D1's endpoint multiplicity
   status (co-binding with revised K/alpha, or explicitly secondary), freeze the
   seven comparators on `Δ`, and stop describing the frozen protocol as
   "unchanged". (MAJOR)
3. **Resolve executability**: redefine the labelled held-out split honestly,
   provide a power/precision analysis for 4 scene clusters, and state plainly
   that D1 is undecidable without the currently-unauthorized confirmation.
   Do not present pilot work as a D1 test. (MAJOR)

## What the reviewer did credit

- The route change itself is well motivated and the prior-art reading is accurate.
- Reusing the frozen five-arm paired-edge construction, sealed forecast and
  isolation discipline is the right instinct; no new "method" module is invented.
- The proposal correctly refuses to lower K, alpha, seeds, or stop rules, and
  correctly flags the confirmation authorization gap.
- It is a **proposal**, explicitly not accepted, so no evidence has been
  contaminated. Fixing it at design time is cheap.

---

**Main-session disposition (R99, recorded, not a rebuttal):** accepted in full.
`discriminative-prediction-proposal-v1.md` is **NOT accepted** and is retained
as superseded design evidence. A v2 must address all three requirements before
any further independent review. This review does not change the goal, any score,
any gate status, or any frozen artifact.

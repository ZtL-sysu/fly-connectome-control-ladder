# Independent review — discriminative-prediction-proposal-v2

Reviewer: isolated `general-purpose` reasoning sub-agent `d1-v2-reviewer`,
no visibility into the authoring conversation or the v1 reviewer. 2026-11-12.
Scope: the proposal **as a design-contract candidate** only; no result or score
implication. Verdict: **`revise`** (v2 is a clear improvement over v1, but the
core FATAL is not fully removed and one new fatal-class defect was introduced).

Read: v1 review, v1 proposal, v2 proposal, `response-null-protocol-closure-v4.md`,
`response-null-prediction-dataflow-v1.md`,
`paired-edge-set-executable-spec-v3.md`, `execution-contract-v3.md`,
`prospective-identities-v1.json`, `response-null-design-repair-v2.md`,
`startup-stage-plan.md`. NOT opened: `code-audit/`, `novix/`, runner scripts,
`competence-baseline-spec-v1.md`, `pilot-input-manifest-v2.json`,
`correction-ledger.md` — runner status and script guards are therefore only
relayed from the proposals, not independently confirmed. Stated verbatim by the
reviewer; preserved here.

---

## A. Is the FATAL coupling resolved? **No — fatal-class residue (A1)**

Credited: replacing the raw slope with conditional incremental validity (§2.2),
P1–P5 original-output placebos (§2.3), D0 coupling killer (§3), §2.4 diagnostic
panel, frozen sign/unit (§1), and the explicit correction that this is
shared-variable mechanical coupling, not outcome leakage (end of §2.4). The
architecture requested by v1's review is largely in place.

**A1 (FATAL): putting `q̄` into N is "regressing an outcome on a function of
itself", creating endogeneity/collider bias and an internal contradiction.**
- §2.1 claims N contains only quantities available *without null outcomes*, but
  item 6 `q̄(c)=mean_a q(c,a)` is by §1's own definition built from
  `RMS(null vs original)/RMS(original)` — **it is itself a null outcome** and
  requires running all five rewired arms. The claim is false, and an
  outcome-derived quantity was promoted into the supposedly pre-outcome
  conditioning set.
- Worse: with five arms `{q_r,q_g,q_m,q_s,q_rand}`, `Δ = median(five) − q_r`
  and `q̄ = mean(five)` are **two deterministic functions of the same 5-vector**.
  `q̄` contains `+q_r/5`; `Δ` contains `−q_r`; they are mechanically
  negatively correlated regardless of any mechanism. Under the common case
  where between-clip variation is driven by overall perturbability `P_c` and
  scale `S_c` (`q_a ≈ P_c·ε_a/S_c`), `Δ ≈ [(median ε−ε_r)/mean ε]·q̄`, i.e.
  Δ is nearly proportional to q̄. So `Δ ~ N + R` is effectively
  `Δ ~ α·Δ + … + R`: a textbook endogenous regression of a dependent variable
  on its own function. The partial coefficient of R then lands on the tiny
  residual left after Δ absorbs itself, and its sampling behaviour is governed
  by the joint noise of the five q's — no longer a clean incremental-validity
  measure.
- R and q̄ are additionally correlated through shared scale S (A2), so
  conditioning on q̄ can create or erase a partial slope in unpredictable
  directions. For a co-binding confirmatory endpoint, an uninterpretable gate
  is disqualifying.
- v1's review intended arm-mean q as a **diagnostic only** (v1 review §2: report
  `corr(R, arm-mean q)`, if large → non-discriminating). v2 promoted it into the
  gate's conditioning set without handling the resulting endogeneity. This is
  exactly the collider/endogeneity the review was asked to check, and it exists.

**A2 (MAJOR): the scale/denominator coupling is only conditioned out linearly.**
R is absolute EPE (flow-error units); Δ is dimensionless q with `q=D/S`, so Δ
carries `1/S`. Their dependence on S is respectively linear/absolute and
reciprocal; a linear partial regression on standardized columns cannot exactly
remove a `1/S` coupling. §2.1 includes only `S` and (via q̄) something
`∝1/S` — deleting q̄ loses the `1/S` column. Moreover `EPE_frozen` is a
per-pixel error against GT flow, not a functional of output RMS / temporal
variance / channel RMS (items 1–2); and q's numerator `RMS(null−orig)` depends
on the *fine structure* of the original flow. So the path "original-output fine
structure → both EPE_frozen (→R) and q numerator (→Δ)" is not spanned by N's
low-order moments. P3 (one norm-matched shuffled trajectory) is a single
alternative trajectory and cannot cover all output-derived functionals.

**A3 (MAJOR): the coupling killer's trigger thresholds are not frozen.** D0
kills when `|corr|` is "large" or the relation is "driven by output scale /
difficulty"; §2.4 says "large → non-discriminating". No numeric threshold, yet
D0 alone kills D1. An unquantified killer falsifier is not frozen; §2.4 also
calls the panel "descriptive and cannot rescue a failed gate", leaving its
logical status undefined relative to D0's veto.

**Required fixes for A, in order**:
1. Move `q̄` **out of N**, keep it only as a §2.4 diagnostic (restore v1's
   intent); replace with **pre-outcome** `1/S` and `log S` (from the original
   model output, no null needed) to span the nonlinear `1/S` denominator
   coupling. Write out the Δ–q̄–S algebra and state that N contains no function
   of Δ's own components. Run sensitivity with/without any outcome-derived
   covariate and require the partial coefficient to be stable.
2. Orthogonalize R against the full output-moment basis (use the residual R as
   predictor), and require R to beat P3 **and** a "full original-output
   reconstruction" placebo; add S-stratified / scale-matched subgroup analyses.
3. Numerically freeze D0/§2.4 `|corr|` thresholds, VIF ceiling, and the
   "driven by" criterion; unify their logical status as binding falsifier vs
   descriptive label.
4. Optional cleaner route: define Δ as a scale-free contrast (log-ratio or an
   unnormalized-D contrast) so the common `1/S` factor cancels algebraically —
   but this changes the frozen q definition and must be explicitly versioned in
   v4.

## B. Contract consistency: direction right, boundary wrong, one silent weakening

Credited: withdrawal of "unchanged", D1 declared co-binding new endpoint, v4
must give revised K and family-wise α allocation, seven comparators' Δ-adaptation
frozen, LOGO demoted to descriptive. **E1/E2 were NOT demoted** (§4 still lists
21 E1 + 24 E2 as binding); §2.4 "panel cannot rescue a failed gate" and §4
"LOGO cannot carry the main claim" preserve protocol-closure-v4 §33.

**B1 (MAJOR): revised K is badly under-enumerated.** `design-repair-v2` §31 and
protocol-closure-v4 §33 freeze **Bonferroni `1−0.05/K`** and "freeze K and all
conditions before opening confirmation; failed comparisons cannot be removed".
v2's G-D1 is a conjunction of **up to 7 directional claims**: partial
coefficient 95% LB>0, out-of-scene improvement interval excluding 0, and five
P1–P5 "beating" intervals excluding 0. §4 only says "21 E1 + 24 E2 + new D1
gate(s)" — no D1 gate count, no α allocation or gate structure
(IUT? Holm? gatekeeping?), and "no alpha is spent twice" is an assertion. v4
must enumerate each claim and say how it enters K, else "revised K" is not
executable.

**B2 (MAJOR): adding a co-binding endpoint necessarily changes E1/E2 inference
strictness.** Under Bonferroni `1−0.05/K`, merging D1 into the same family-wise
.05 budget increases K → **tightens every existing E1/E2 gate's confidence
bound** (or, if each gate keeps its original α, family-wise .05 no longer holds
unless hierarchical gatekeeping is declared). v2 §4 confines the effect to "the
endpoint family", but the frozen Bonferroni rule propagates it to all 45
existing gates. Must choose explicitly: (a) acknowledge E1/E2 bounds tighten,
or (b) declare hierarchical gatekeeping (D1 tested after all E1/E2 pass, with
its own α slice) and restate what family-wise .05 means. This is not a
"weakening" but an **undeclared reallocation/tightening** that equally makes
"the rest is unchanged" inaccurate.

**B3 (MAJOR): the seven comparators' "must beat" requirement silently
disappeared.** v1's primary gate required R to beat the majority baseline **and
all seven frozen comparators**; v1 §4 required their Δ-adaptation to be frozen.
v2 §4 does freeze the adaptation, but **G-D1 no longer requires beating those
seven** — it only requires beating five NEW placebos (P1–P5), a different set.
The seven are `zero-divergence, calibration median, development-output transfer,
forcing L2, forcing ∞, structural/geometry regression, magnitude regression`
(design-repair-v2 §31); P1–P5 are scale/difficulty/shuffled/scene-perm/dose.
This is a substantive weakening of D1's own binding gate relative to v1, and §4
does not state that it was removed. Must declare whether the seven remain a
gate or are purely descriptive; if removed, give a power rationale and declare
it.

**B4 (minor): thresholds/rules not frozen.** median-over-5 tie rule and the
"predeclared deterministic rule" for random/response coincidence — §1 only
promises a rule and a log, without giving the rule; whether coincident arms are
deduplicated in median/mean is undefined. §2.4 "large" unquantified. For
"frozen before outcomes", a promise ≠ a freeze.

## C. Executability: mostly honest, one factual error, precision prerequisite insufficient

Credited: TEST labels withheld → retreat to labelled development scene-disjoint
split; 4 clusters lack power; "D1 is NOT decidable in the development pilot";
"No pilot result may be presented as a D1 test"; confirmation remains
unauthorized (execution-contract-v3 §25/§70–76); v1's "either way
discriminating" overclaim withdrawn in three places (§0/§3/§7); LOGO honestly
demoted; precision analysis a prerequisite with "infeasible → return to design,
do not relax α or placebo set". **No residual wording presenting pilot work as
a D1 test.** Precision prerequisite's position matches protocol-closure-v4 §35
and design-repair-v2 §23/§33.

**C1 (MAJOR, factual error): §5 claims a "scene-disjoint split … frozen in
`prospective-identities-v1.json`" — that file has no such split.** Its `status`
is `"proposed_before_any_task_model_outcome_not_yet_accepted_guidance"` (not
accepted), it lists only four `development_scenes` and eight windows, and has
**no train/holdout scene partition field**. v2 cites a frozen split that does
not exist. Either create and freeze it in v4 (itself a change to a frozen
identity/split artifact, to be counted as "changed", not "unchanged"), or
withdraw the assertion.
- Related: `natural_confirmation` uses **different scene families**
  (`excluded_families` are the four development families) but
  `accuracy_labels: withheld; function agreement only` — held-out scenes exist
  but have no labels. That is R's dead end, and v2's retreat logic holds.
- But v2 **never mentions that `procedural_confirmation` provides known
  labels**: its `source_target_flow_rule` (constant flow) and
  `reference_sanity: "known-motion directional alignment"`, and dataflow-v1 §37
  says "separate procedural confirmation supplies known task labels where
  appropriate". So the confirmation stage **does have a labelled held-out
  evaluation set**; v2 asserts the development scene-disjoint split is the only
  option without including or explicitly excluding it (e.g. on decoder-flow
  scale vs "native source target units" grounds). The "honesty" is incomplete:
  a restricted set of options presented as the only one, and "generalization
  beyond that labelled pool is out of scope" is self-contradictory in scope.
  Must add whether/why R can or cannot be computed on the procedural labelled
  arm.

**C2 (MAJOR): the precision prerequisite is present but insufficient.** It only
covers CI width/variance, not:
- N has ~10+ columns (RMS, temporal variance, multi-column channel RMS profile,
  2 difficulty columns, dose, multiple geometry columns, magnitude, q̄) while
  the pilot has **16 clip units / 4 scene clusters** → `Δ ~ N` is near-saturated
  or rank-deficient; the partial coefficient has almost no residual df.
- A **4-cluster bootstrap 95% lower bound is inherently discrete** (~35 distinct
  multisets from resampling 4 clusters; 100,000 replicates just repeat ~35
  values); LB resolution ~1/35, so >0 is nearly unattainable.
- Multiplicity-adjusted power for the 5 placebo comparisons.
design-repair-v2 §33 requires conservative precision "under the finite available
scene/mask counts", so C2 fails to implement a frozen requirement. More subtly,
§5 allows the pilot to report "coupling diagnostic panel as feasibility
evidence", but that panel includes `corr(Δ,RMS)` and `variance-inflation of R
given N`; the latter requires fitting a 10-column regression on 16 points / 4
clusters — **part of the pilot's own diagnostic panel is unreliable**. Restrict
pilot diagnostics to reliably estimable quantities and make the precision
prerequisite cover df / cluster discreteness / multiplicity-adjusted power.

**C3 (minor): D4 (generalization falsifier) is unmeasurable in the pilot** — the
"scene-disjoint labelled split" is a split *within* the same 4 development
scenes, not independent scenes; and development has only 2 mask-family seeds
(prospective-identities lines 467–471) while "independent mask families" need
confirmation's 3. Since v2 says confirmation is unauthorized, D4 idles. Also
v1 §2's "scene-level permutation test preserving each scene's q distribution"
was never implemented: P4 permutes R within difficulty strata (predictor-side),
and G-D1 uses cluster bootstrap — neither is that permutation test.

**C4 (minor, misattribution): §5 says "`startup-stage-plan.md` says the
scientific null runner and predictor are not yet completed/isolated/reviewed" —
that sentence is not in `startup-stage-plan.md`.** It only discusses the startup
stage, blockers, gates and authorized task 21782. The quote is inherited from
v1 proposal §3 and misattributed; runner status should cite actual
`code-audit/`/`novix/` evidence (which this reviewer did not open).

## D. New risks (absent in v1 or amplified in v2)

1. Multiplicity inflation unaccounted (=B1): 5 placebos + improvement + partial
   slope = up to 7 directional decisions, all binding ("any placebo performing
   as well as R fails D1"), none entered into K/α. "All must be beaten" as an
   IUT conjunction is not type-I inflation, but R-over-N improvement is an
   independent gate, and the 5 "beating" intervals share the same nested
   bootstrap with the improvement → mutually correlated; joint structure
   undeclared.
2. Partial slope unestimable at 4 clusters / saturated N (=C2), a new gate's
   direct estimation instability. Even with more confirmation clusters (natural
   6 families + procedural 10 seeds), the extrapolation of power from 4-cluster
   pilot variance to ~16 confirmation clusters is unexplained.
3. median-over-5 tie rule still unspecified (=B4).
4. The added q̄ endogeneity is itself a new v1-absent risk (=A1).
5. P4 ≠ "preserve each scene's q distribution" (=C3); VIF-of-R-given-N
   unreliable at 16 points / 10 columns; D0's "large/driven by" unquantified,
   so the killer may idle.

## E. Verdict: `revise`

Reason: the core architecture (conditioning + placebos + D0), contract
direction, and executability wording are largely right and closable by cheap
design-time edits, so not `reject`; but **A retains a fatal-class residue (A1
q̄ endogeneity)**, and B/C contain factual errors and under-enumeration, so
**absolutely not `accept-as-is`**. If fix 1 is refused, escalate to `reject`.
Even a future `accept` accepts only **the proposal as a design-contract
candidate** — not a result, not a score.

**Three most important requirements, in priority order:**
1. **[FATAL residue, must fix] Rebuild the conditioning set**: move `q̄` out of
   N (diagnostic only in §2.4), add pre-outcome `1/S` and `log S`, orthogonalize
   R against the output-moment basis, numerically freeze D0/§2.4 `|corr|`, VIF
   and "driven by" thresholds and unify their logical status; write the
   Δ–q̄–S algebra and show N contains no function of Δ's own components.
   Otherwise the partial-coefficient gate is uninterpretable and the FATAL
   stands.
2. **[Contract executability] In v4, enumerate every D1 directional claim**
   (partial slope / improvement / P1–P5, ≤7), give the revised K and an explicit
   Bonferroni/gatekeeping α allocation, declare the effect on the 45 existing
   E1/E2 gates' strictness, correct "the rest is unchanged"; state whether the
   seven Δ-comparators remain a binding pass condition; freeze the median tie
   rule and coincident-arm rule.
3. **[Facts and precision] Withdraw the false claim that a scene-disjoint split
   is frozen in `prospective-identities-v1.json`** (unaccepted, 4 scenes, no
   split), and include or explicitly exclude the labelled
   `procedural_confirmation`; extend the precision prerequisite from CI width
   to df/saturation, 4-cluster bootstrap discreteness and multiplicity-adjusted
   power; restrict pilot diagnostics to reliably estimable quantities; fix the
   `startup-stage-plan.md` misattribution.

**Credited (mirroring v1's "credited")**: incremental-validity primary gate,
P1–P5 and D0 introduction, shared-variable vs leakage terminology correction,
sign/unit freeze, comprehensive D2–D5 falsifiers (dose / balance / `1e-6` floor
/ selection / multiple endpoints each mapped to v1 §3), honest LOGO demotion,
co-binding declaration, overclaim withdrawal, confirmation-unauthorized status
preserved, refusal to relax α/placebo/seed/stop rules. These are real progress
and are not negated by the `revise` verdict.

---

## Main-session fact check (R99, performed locally, not a rebuttal)

All three factual challenges were independently re-checked against disk and
**confirmed**:

1. `ccfa-startup-packet/prospective-identities-v1.json` has `status =
   "proposed_before_any_task_model_outcome_not_yet_accepted_guidance"`, keys
   contain no `split` / `holdout` field, `development_scenes` = exactly the four
   `alley_1 / bamboo_1 / market_2 / mountain_1`, 8 windows. **No frozen
   scene-disjoint split exists.** v2 §5's citation is false.
2. The sentence "The scientific null runner and predictor must be completed,
   isolated and reviewed at their later research gates" is in
   **`ccfa-startup-packet/candidate-E-local-v2/startup-decision.md:7`**, not in
   `startup-stage-plan.md`. The v2 proposal (and earlier ledger entries)
   misattributed it; corrected here.
3. `procedural_confirmation` **does** specify `source_target_flow_rule` /
   known-motion directional alignment (constant configurable flow), i.e. a
   labelled held-out arm exists in the confirmation design. v2 §5's "only
   option" wording is wrong. `mask_family_seeds` = development `[2 seeds]`,
   confirmation `[3 seeds]`, confirming the independent-family shortage.

**Disposition**: accepted in full. `discriminative-prediction-proposal-v2.md`
is **NOT accepted**; v1 remains superseded. Rather than issuing a v3 that
patches algebra while the design is **statistically unestimable at 4 scene
clusters and confirmation remains unauthorized**, this session records the
design as **BLOCKED_ON_CONFIRMATION** and returns to the ordered engineering
and pilot gates. See `R99-design-block-decision.md`.
No score, gate status, frozen artifact or contract changed by this review.

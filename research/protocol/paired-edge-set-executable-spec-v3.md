# Candidate E finite constructor specification v3

Status: proposed closure for review, not startup acceptance. Uses the approximate binned variant in construction-v2; v1 exact-displacement support failed its bounded screen and remains preserved. Source-only structural checks support planning, not active-dose or functional success.

## Graph-only shared support

1. Under actual runtime-verified complete parameter groups, exclude self-loop rows. For each group, order rows by a frozen graph-only RNG, divide into blocks of eight, and record remainders. Require distinct source/target endpoints within each block. Enumerate its105 perfect matchings and reject loops or existing/duplicate new arcs. The carried parameter assignments remain unchanged; endpoint geometry is separately recomputed.
2. Partition legal matchings by the exact **binned** signature from block-geometry-support-v2.json: new displacement length/direction × source boundary bin, plus signed source-pair displacement length/direction. Choose the largest stratum, tie-breaking lexicographically on its signature, and require at least four distinct matchings. All decisions here use graph information only.
3. Across retained blocks enforce global candidate compatibility before using responses: form the union of every possible new arc in the chosen stratum. Reject a block if this union intersects that of an already retained block. Original-edge rows are already disjoint. This conservative graph-only rule guarantees that any subsequent independent choice of matching per block cannot create cross-block duplicate arcs. Freeze the resulting block order/support and all rejection reasons. It may reduce support and must be counted rather than assumed affordable.

## Four finite complete candidates per arm

Calculate the28 pair features once per retained block, shared across arms. The response feature is weight-scaled squared full absolute gray/development response-vector difference. The magnitude feature uses scalar RMS of those same complete absolute vectors; evoked mass remains only the dose measure. Geometry uses weight-scaled squared exact source separation in Euclidean hex coordinates. Shuffled response vectors are permuted within source cell type and `(floor(u/4),floor(v/4))` spatial bins with a fixed family seed; singleton bins remain unchanged and are counted.

Sum the corresponding pair feature over each legal block matching and sort, tie-breaking by the sorted original-edge-row pairing. For k=0,1,2,3, form a complete candidate by using each block's kth-ranked matching. Thus all four complete candidates use the same edited rows and common binned geometry. Select the response candidate by the smallest full-mask aggregate forcing objective from protocol-closure-v4, not its summed local scores. Geometry, magnitude and shuffled arms select by their own complete feature sums; random uses an independently shuffled matching order per block and a frozen uniform choice among its four candidates. Record duplicate candidates across arms instead of forbidding them.

The four-response-candidate rule can miss globally optimal cancellation patterns; no optimality claim is made. It bounds search prospectively. No additional candidates or mask families may be generated merely because outcomes are unfavorable. Scientific pilot still uses at most two development RNG families per arm.

## Dose, balance and topology checks

Every arm uses the same graph-only block prefix for each development evoked-dose target. Entire blocks are indivisible. Keep the dose grid .01,.025,.05,.10,.20 and report realized dose and maximum indivisible-block error. A target is ineligible if support ends before it is reached; do not imply all five targets exist. Cross-model transferred masks keep their source-selected prefix.

After choosing complete candidates, verify exact degree, original self-loop rows, group-count and realized-weight invariants, identical edited original edges/mass, exact common binned geometry and no parallel new arcs. Require an unweighted topology certificate for every mandatory arm; an unchanged reciprocal-pair invariant is inconclusive and cannot be labelled nonisomorphic. With no stronger certificate in budget, reject the complete family uniformly and record it.

Predeclare raw-geometry balance diagnostics: mean and second moment of new Euclidean edge length and source-pair Euclidean separation; their correlations with the source boundary indicator; and typepair-wise versions for groups represented in all arms. Standardize differences by graph-only variability across the retained support's legal matchings, calculated before response selection. Require absolute standardized difference<=.1 between the response and each control for every mandatory nondegenerate diagnostic. If graph-only variance is zero, require equality. This is an operational small-imbalance rule, not proof that geometry has been fully controlled. Report the raw distributions and maximum imbalance. A failure makes that dose/family ineligible under the fixed search, not permission for repeated mask search.

The geometry arm deliberately minimizes exact source separation inside the shared binned support. Response superiority to that arm is a binding primary comparison; remaining continuous geometry is disclosed and enters the secondary covariate analysis. The scientific claim concerns response-conditioned comparisons under these named controls, without claiming that all geometry or biological confounding has disappeared.

## Search/compute stop rules

The1.1-million unique pair-score bound covers at most314,285 edited rows with blocks of eight, before rejection; four complete candidates reuse those pair scores. Bound graph-only inspected pair opportunities at2million per family; count every structural rejection. Stream pair scores in8192-pair chunks, keep no all-pairs tensor. Complete-mask forcing is computed from cached original development trajectories with time/edge chunking; no extra nonlinear null run is used for selection.

The four cumulative GPU-hour pilot cap and at most two sequential tasks remain binding. If setup/restore, support, geometry balance, empirical active dose, informative control separation, noise-scale stability or confirmation precision fails, return to design with all failures preserved. The proposed constructor has not been scientifically executed or accepted. Runtime equality/group mapping and resource timing still need their engineering gate.

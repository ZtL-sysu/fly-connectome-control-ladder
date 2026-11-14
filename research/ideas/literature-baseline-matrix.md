# Public-source literature and baseline map

Owner: ccf-literature-searcher, standard. Access: 2026-11-11. Public keyword queries only; no private manuscript sentences disclosed. Preprints remain preprints. Core arXiv full texts and official source repos saved locally (source-manifest.json and code-audit acquisition hashes). Discovery snippets are not used as final evidence.

| Work | Year / venue-status | Task / contribution | Code and role | Differentiation / risk | Insight, completeness, empirical-evidence (1–5; provisional source-based assessment) |
|---|---|---|---|---|---|
| [Lappalainen et al.](https://www.nature.com/articles/s41586-024-07939-3) | 2024 Nature | Connectome/task-constrained optic flow; official flyvis | [official](https://github.com/TuragaLab/flyvis), must-rerun official network; MovingEdge is a separate diagnostic adaptation, not original optic-flow benchmark replication | Provides real spatial dynamics; natural optic-flow evaluation required for full vision-transfer claim | 5,5,5 |
| [Dhiman, Topological Sensitivity](https://arxiv.org/abs/2604.04033) | 2026 arXiv v1 | Matched early optimization 5/10 steps, init and degree controls | [official](https://github.com/nalin-dhiman/Connectome-Constrained-Neural-Networks), must-rerun corrected fromscratch; no checkpoint needed there | Already control ladder + activity-scale + edge-carried parameters §4.2; do not claim those are undisclosed. Open question is competence-conditioned interpretation under longer, validated training and independent motion inputs | 4,4,3 |
| [Correig-Fraga et al., Structure alone](https://arxiv.org/abs/2610.10023) | 2026 arXiv v1 | Eye geometry + connectome; shape/color/numerosity under wiring cost | public paper links Zenodo 21549559; asset contents/license not yet individually verified; adaptation-attempt, not yet runnable | Geometry and wiring cost comparisons already present, so adding spatial null alone is incremental | 4,4,4 |
| [Dhawan, FlyHack](https://arxiv.org/abs/2610.13018) | 2026 arXiv v1 | 50-model flyvis ensemble, task-matched CNN, intervention/attribution alignment | Official flyvis models + CNN baselines reported; project code path not yet verified; literature-context until direct assets verified | Mechanistic conditionality and task-matched controls already studied; required differentiation from attribution alignment and circuit pruning | 4,4,4 |
| [Park, sensory-motor boundary nulls](https://arxiv.org/abs/2609.39248) | 2026 arXiv v1 | Registered ten-seed embodied control, boundary-preserving rewiring, dose/sham | [official](https://github.com/gyujeongion/flyconnectome-nulls); literature-context, different nonvisual evolutionary task | Severe prior-art risk for generic 'protect task paths' claim. Candidate A alone is insufficient. Distinct visual learning-regime validity question remains to test | 4,5,4 |
| [Milisav et al., weighted network nulls](https://www.nature.com/articles/s43588-024-00735-z) | 2025 Nature Computational Science 5:48–64 (2024 in DOI/online history) | Strength-sequence-preserving rewiring with annealing | [official](https://github.com/netneurolab/milisav_strength_nulls), adaptation-attempt for strength-matched control if degree/activity mechanism implicated; primary text via [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11774763/) | Degree matching alone is known insufficient; not a novelty claim | 4,4,4 |
| [Maslov & Sneppen](https://pubmed.ncbi.nlm.nih.gov/11988575/) | 2002 Science | Degree-preserving network rewiring | technique-family control implemented in official toposens source | Foundational comparator; no new null-model novelty inferred | 5,4,4 |
| [Milo et al.](https://pubmed.ncbi.nlm.nih.gov/12399590/) | 2002 Science | Motifs relative to graph-null ensembles | literature-context for motif counts | Motif enrichment does not by itself establish functional/causal role; count collapse already fails in our evidence | 5,4,4 |

## Screening and opportunity clusters
Control semantics, boundary structure and dynamics/initialization are crowded/partly covered. A reusable 'protect important paths' standard is substantially anticipated by Park. Training-free path-count predictions already failed internally and are excluded as a current central claim.

Potential opening: directly expose when an early near-constant visual predictor makes a topology comparison scientifically underinformative, and provide a task-competence + perturbation-visibility validity criterion with independent motion/generalization tests. This is a hypothesis, not searched proof of high novelty. Must show more than 'train longer'; must measure sensory/dynamic interference and a meaningful downstream inference change after matching competence.

Search coverage: screened public result clusters spanning control-study, structure-alone, FlyHack, boundary study, weighted nulls, geometry nulls/navigation, visual connectome atlas, motif/function caution, representation equivariance, attribution, graph-fibration symmetry (unverified SSRN; not accepted evidence), computational retinotopy, lesion nulls (different task), learning-baseline analogies. Unrelated medical MRI equivariance / registration / segmentation hits and discovery-only project catalogs excluded. MDPI excluded. Recent core coverage 2024–2026; no positive novelty verdict from snippets.

## Task/data/metric availability
The official flyvis repo bundles the averaged measured optic-lobe connectivity specification fib25-fib19_v2.2.json. It is an averaged/repeated-column connectome model, not individual MaleCNS. MovingEdge stimuli are generated by official source code; no restricted raw dataset is required for corrected fromscratch direction decoding. Optical-flow benchmark, pretrained checkpoints and natural clips require separate asset/license checks before being claimed complete.

Baseline metrics: official toposens packaged revision_metrics.csv reports 10-step connectome MSE .504455 vs degree null .502693; these are third-party reports, not our measurements. Targets are 2D unit motion directions and balanced: zero predictor MSE .5. Their stated early-optimization estimand remains valid; interpreting near-zero gap as equality of competent behavior needs direct checks. Need CIs clustered at independent training seed, not pooling repeated copies of the same connectome across null masks.

## Local/remote feasibility
Source snapshots acquired, exact candidate commands and GPU caveats checked. Local machine has 16GB and MPS; full official network is reserved for authorized exp-4090. Remote task 21782 confirms RTX4090 and 44.388GiB usable nominal total; source/asset audit still running. No training has been run under this recovery.

## R99 live recency addition — 2026-11-12 (independent web check)

Source: live web search + full-text fetch, recorded in
`gate-G0-recency-review-R99.md`. These are **newly found** entries; the original
matrix above is preserved unmodified.

| Work | Year / venue-status | Task / contribution | Code and role | Differentiation / risk |
|---|---|---|---|---|
| [Kuklev, *What Survives on Real Drawings*](https://arxiv.org/html/2609.24565v2), arXiv:2609.24565v2 | 2026 arXiv v2, September | Frozen fly optic-lobe connectome driven by prescribed motion over architectural drawings; hatch matching and wall segmentation; matched graph nulls on 45,669 nodes / 1,513,231 edges | **literature-context for now** (no code rerun attempted); strongest prior art for a *positive* topology effect | **Severe G4 risk.** Reports intact `0.857` vs degree-preserving rewiring `0.539` (`+0.318 [0.296,0.339]`, 3 seeds), type-pair/sign-preserving `0.586` (`+0.271`), ER `0.500` (`+0.356`); segmentation null `0.483→0.089` IoU; R7/R8 silencing positive control `0.092`. **This already supplies the positive, strictly-null-controlled visual topology effect our recovery was aiming to add.** It then bounds the claim: held-out `receptors only 0.894` vs `fly+drift 0.835`; CNN on raw receptors `0.961` vs fly front-end `0.962`; T4/T5 silencing leaves tasks intact. Held-out split was NOT used for rewiring nulls. Wire-length null infeasible (1.08% of edges have both-endpoint coordinates); production drawings proprietary. Any "we show wiring matters on a visual task" claim is now incremental. |
| [*Representational geometry as a fidelity metric for connectome-constrained networks*](https://www.aimedicalcompendium.com/article.cfm?id=253759) | 2026 | Flyvis pretrained ensemble vs weight-shuffled / degree-preserving / ER nulls; individual-pairwise RDM, CKA, validated non-circular biology reference | literature-context; no rerun | Real vs random wiring distinguishable **before** training (`p<10^-13`) but largely indistinguishable once both are trained to task adequacy; one trained-ER/OFF case closes the gap completely. Honest largely-null result. Close to Candidate E's competence-conditioned framing; must be cited and differentiated. |

**Net effect on the goal**: the "add a positive visual effect" gap is partially
pre-empted. Candidate E's remaining distinct angle is a *response-conditioned,
path-preserving null under a frozen competent visual function with sealed
forecasts, on optic-flow inputs*, plus a discriminating prediction of **when**
path preservation matters versus when the input alone suffices (the open question
Kuklev leaves). G4 is flagged high-risk, not passed. No stage status, score or
frozen identity was changed.

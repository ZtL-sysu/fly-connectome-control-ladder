# CCFA standard idea review: OccluFly-CRG

## Verdict

**Weighted score: 2.54/5 = 5.08/10. Recommendation: `pivot-with-rescue-route`.** This candidate does not pass the user's strict `Overall > 8.0/10` gate. Do not start a full experiment or move it to the guidance/writing pipeline. A Novix 4090 software smoke is separately in progress because the user requested a lightweight smoke; it can establish implementation feasibility only.

**Target venue:** CVPR 2027 main conference, assumed. **Stage:** early idea seed. **Current readiness:** low. **Development potential:** medium if the connectome contributes a specific, falsifiable algorithmic advantage after strong VOS and graph-null controls; that contribution is not established here.

## Search basis

Standard-mode public-safe searches covered long-term/occluded video object segmentation, re-identification after occlusion, connectome-constrained fly vision, and spiking visual tracking. Sources included CVF proceedings pages, arXiv, and the Nature paper page. This is a targeted search, not an exhaustive search for every motif-routing or SNN hypergraph method. Claims about whether the exact motif router has appeared elsewhere remain uncertain.

## Normalized idea

- **Problem:** Maintain visible instance masks and persistent track identities when multiple objects undergo long occlusion and later reappear.
- **Proposed gap:** The candidate claims a connectome-derived typed motif library with state-dependent routing can improve recovery beyond generic temporal memory.
- **Mechanism:** Compile a chosen fly connectome into typed motifs, route object slots among motif modules based on current visual evidence, visibility uncertainty, and object memory, and use adaptive-LIF states during occlusion and re-capture.
- **Expected evidence:** OVIS/BURST, with per-occlusion-length IDF1, HOTA, mask AP, and identity-switch rate; compare to current VOS/VIS methods, graph-free SNN, and degree-preserving rewires.
- **Key limit:** The proposed compiler, graph-to-visual-cell mapping, and reason the fly graph should improve this computer-vision task are not yet specified or supported by evidence.

## Closest prior art

| Work | What it already does | Overlap and remaining delta | Risk |
|---|---|---|---|
| Li et al., ECCV 2018, [Video Object Segmentation with Joint Re-identification and Attention-Aware Mask Propagation](https://openaccess.thecvf.com/content_ECCV_2018/html/Xiaoxiao_Li_Video_Object_Segmentation_with_Joint_Re-identification_and_Attention-Aware_Mask_Propagation_ECCV_2018_paper.html) | Jointly segments/tracks video objects and explicitly re-identifies them after prolonged occlusion. | The central capability “recover identity after prolonged occlusion” is already established. The proposed connectome motif route differs, but no evidence shows it creates a new capability or superior mechanism. | High |
| Qi et al., [Occluded Video Instance Segmentation (OVIS)](https://arxiv.org/abs/2102.01558), 2021 | Defines a video-instance-segmentation benchmark for detection, masks, tracking, and severe occlusion. | OVIS is an appropriate dataset, but choosing it does not create novelty. Its task overlaps directly with the proposed visible-mask/identity recovery. | High |
| Liang et al., CVPR 2026, [Long-RVOS](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_Long-RVOS_A_Comprehensive_Benchmark_for_Long-term_Referring_Video_Object_Segmentation_CVPR_2026_paper.html) | Adds long-duration video segmentation with occlusion, disappearance/reappearance, and shot changes. | Language-conditioned setting differs, but long-term reappearance is a current, already benchmarked vision problem. The candidate needs a sharper contribution than “use fly motifs.” | High |
| Ding et al., ICCV 2025, [SAM2Long](https://openaccess.thecvf.com/content/ICCV2025/html/Ding_SAM2Long_Enhancing_SAM_2_for_Long_Video_Segmentation_with_a_ICCV_2025_paper.html) | Uses uncertainty-aware memory-path search to improve long-video segmentation, including occlusion/reappearance. | Competes on the same temporal-memory failure mode. The motif router would need a controlled advantage over strong memory-path methods. | High |
| [SpikingMOT](https://arxiv.org/abs/2607.19875), 2026 preprint | Proposes a spike-driven multi-object tracker and reports tracking metrics on MOT benchmarks. | Establishes active SNN-based identity/tracking work. It may not solve instance masks or use a connectome; those differences are not sufficient on their own for a CVPR novelty delta. | High |
| Zhang et al., CVPR 2026, [SpikeTrack](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpikeTrack_A_Spike-driven_Framework_for_Efficient_Visual_Tracking_CVPR_2026_paper.html) | Presents spike-driven RGB visual tracking and temporal dynamics for tracking. | Overlaps with the SNN tracking component. Candidate must explain why connectome-derived motifs outperform modern SNN and graph-free temporal-memory baselines. | High |
| Lappalainen et al., Nature 2024, [Connectome-constrained networks predict neural activity across the fly visual system](https://www.nature.com/articles/s41586-024-07939-3) | Uses connectome-constrained networks and biologically plausible dynamics for Drosophila optic-flow estimation. | The task differs (video instance segmentation vs optic flow), but the connectome-constrained visual model is a direct architectural neighbor and required baseline family. | High |
| [Structure alone supports efficient visual computation in the Drosophila visual system](https://arxiv.org/abs/2610.10023) | Studies connectome/eye-geometry-constrained visual computation with learned scalar synaptic gains and thresholds. | The proposed motif compiler differs from scalar-gain training, but both claim an advantage from fly visual structure. A degree-/wiring-matched test is essential; exact task overlap and motif-route overlap are unresolved. | High |

## Novelty delta

The task-level claim of mask/identity recovery after long occlusion is not novel: an ECCV 2018 paper explicitly performs re-identification after prolonged occlusion, OVIS formalizes severe-occlusion video instance segmentation, and recent long-term VOS papers address disappearance/reappearance. The plausible remaining delta is the **specific** use of a connectome-derived motif grammar to route recurrent SNN state. The idea does not yet define a reproducible motif grammar, show that the motif selection follows verified circuit annotations, or explain why the structure should outperform learned memory routing. Prior art on connectome visual computation, SNN tracking, and degree-preserving nulls further narrows the novelty claim. Exact motif-routing novelty has not been searched deeply enough to call it novel.

## Serious blockers

1. **The central visual capability is prior art.** Re-identification after prolonged occlusion is explicit in ECCV 2018, and long-duration segmentation/reappearance remains active in CVPR/ICCV work. Reframing the same objective as “circuit grammar” does not establish a new vision contribution.
2. **The connectome-to-method link is asserted, not derived.** “Compile all nodes and edges into typed motifs” lacks a deterministic algorithm, a validated node/region mapping, and a reason those motifs should encode object identity or occlusion recovery.
3. **The graph source is ambiguous.** The card alternates between complete FlyWire and MaleCNS. These are distinct reconstructions; the primary dataset, release/version, included cells, sign/type fields, and visual-node annotations must be fixed before implementation. The visual input projection is a learned design choice, not a demonstrated correspondence to retinal neurons.
4. **The null design needs refinement.** Rewiring 50 graphs while preserving degree, sign, region pair, edge weights, and computational budget may be expensive and may not preserve all necessary constraints simultaneously. The primary null and its invariants need a precise algorithm and verification.
5. **Benchmark fairness is difficult.** SAM2Long and other large pretrained models cannot be compared fairly to a small scratch-trained SNN without matched inputs, prompts, pretraining, and compute reporting. The candidate's current baseline list mixes model families and training regimes.

## Independent reviewer panel

- **Field expert:** Long-occlusion recovery is important, but the capability already has direct VOS/re-identification prior art. Recast the paper around a new, measurable visual phenomenon only if one exists beyond the current mask/ID objective. **Tendency: 2/5.**
- **Method expert:** The router, motif library, and adaptive-LIF state are compatible as software modules, but the idea provides no derivation linking connectome motifs to identity persistence. Specify the compiler and a mechanistic prediction before claiming soundness. **Tendency: 2/5.**
- **Experiment expert:** OVIS labels and a rewiring ladder make a test possible. The decisive comparison is the original graph versus matched rewires and strong modern VOS/SNN baselines, stratified by occlusion duration. The current 4090 smoke is synthetic and cannot satisfy this evidence burden. **Tendency: 3/5.**
- **AC / venue expert:** CVPR main-track fit is weak in the current form because the contribution reads as an existing VOS problem plus a brain-inspired module. A demonstrated new capability or a generalizable algorithmic insight would be needed. **Tendency: 2/5.**
- **Skeptical prior-art expert:** The strongest objection is “long-occlusion re-identification is known; connectome motifs are a new prior with no demonstrated benefit.” ECCV 2018, OVIS, SAM2Long, SpikeTrack, and connectome-constrained FlyVis make the current novelty delta fragile. Exact motif-route overlap remains unsearched. **Tendency: 2/5.**

## Rubric

| Dimension | Weight | Score (1–5) | Confidence (1–5) | Deduction / evidence basis | Repair condition |
|---|---:|---:|---:|---|---|
| Problem importance | 12 | 4 | 4 | OVIS and Long-RVOS establish severe occlusion and long-term reappearance as real video-segmentation challenges. | Keep a precisely defined failure mode and show it matters beyond a dataset slice. |
| Novelty against likely prior work | 14 | 2 | 3 | ECCV 2018 already re-identifies after prolonged occlusion; OVIS, Long-RVOS, SAM2Long and SNN tracking overlap. | Find a different testable capability and search exact motif-routing/memory prior art. |
| Conceptual innovation | 12 | 2 | 3 | “Typed motif library + state-dependent router” is a proposed composition without a non-obvious insight connecting circuit motifs to visual identity. | Derive a specific algorithmic property or prediction from the connectome and validate the mapping. |
| Method soundness | 14 | 2 | 3 | Motif compilation, graph-to-visual-node projection, and the role of nonvisual cells are underspecified. | Fix one graph/release and provide a reproducible compiler and a falsifiable mechanism. |
| Elegance and simplicity | 8 | 2 | 3 | Full-connectome motif extraction, object slots, uncertainty routing, adaptive-LIF modules, and a vision backbone add multiple unconstrained parts. | Remove components that do not contribute under matched ablations. |
| Feasibility under resources | 8 | 3 | 3 | A 4090 is available for a small smoke; full VOS training, graph compilation, and 50 nulls are not yet costed. | Profile graph preprocessing and one controlled short run, then cost the full matrix. |
| Experimental convincibility | 10 | 3 | 3 | OVIS labels and reappearance-stratified metrics support testing, but the null invariants and fair foundation-model comparison are unresolved. | Freeze a primary metric, exact null algorithm, matched training protocol, and data split. |
| Venue and audience fit | 8 | 2 | 3 | In current form it is an application of a biological prior to an established video task; no demonstrated CVPR-level algorithmic advance. | Show generality or a new capability beyond this dataset/task. |
| Timeliness and topic heat | 6 | 4 | 4 | Long-term video segmentation and SNN vision have recent CVPR/ICCV work, though this also means competition is high. | Differentiate from current long-VOS and spike-tracking work. |
| Risk-adjusted acceptance potential | 8 | 2 | 3 | Novelty and mechanism blockers jointly dominate; no smoke can resolve those conceptual gaps. | Pass exact prior-art search and show a distinct, reproducible topology effect. |

**Weighted score:** `(4×12 + 2×14 + 2×12 + 2×14 + 2×8 + 3×8 + 3×10 + 2×8 + 4×6 + 2×8)/100 = 2.54/5`.

**Overall:** `5.08/10`. This is a decision aid, not an acceptance probability. **Confidence:** medium (3/5); the task-level prior art and baseline landscape are well supported, but exact motif-routing prior art and graph-field availability remain unverified.

## Recommendation and next gate

`pivot-with-rescue-route`. Do not continue this exact OccluFly formulation into a full training program. The smallest valid rescue is not to rename the router: first define the connectome compiler from a fixed MaleCNS release and verify that its cell annotations support the proposed input projection; then propose a vision claim not already covered by prolonged-occlusion re-identification and long-term VOS. If that search finds no separate claim, retire this candidate. The pending synthetic GPU smoke can only establish that the module compiles, backpropagates, and runs on a 4090; it cannot change this score or justify a paper.

**Score gate:** User threshold is strictly greater than 8.0/10. Current score is 5.08/10, so no `f-guidance-builder-v1` or `f-research-v1` paper pipeline is authorized for this candidate. Continue idea generation for other genuinely distinct candidates.

### Smoke status at review time

Novix task `17346` is assigned to `exp-4090`, node `aliyun-hz-exp-4090-1`, with one GPU and `eligible_nodes=2`; its backend is still running. No CUDA/GPU result has yet been observed. Wait for the same task ID and inspect returned logs/artifacts; do not resubmit while it remains live.

## Sources

1. Li et al., ECCV 2018: https://openaccess.thecvf.com/content_ECCV_2018/html/Xiaoxiao_Li_Video_Object_Segmentation_with_Joint_Re-identification_and_Attention-Aware_Mask_Propagation_ECCV_2018_paper.html
2. OVIS, arXiv:2102.01558: https://arxiv.org/abs/2102.01558
3. Liang et al., CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Liang_Long-RVOS_A_Comprehensive_Benchmark_for_Long-term_Referring_Video_Object_Segmentation_CVPR_2026_paper.html
4. Ding et al., ICCV 2025: https://openaccess.thecvf.com/content/ICCV2025/html/Ding_SAM2Long_Enhancing_SAM_2_for_Long_Video_Segmentation_with_a_ICCV_2025_paper.html
5. SpikingMOT, arXiv:2607.19875: https://arxiv.org/abs/2607.19875
6. SpikeTrack, CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpikeTrack_A_Spike-driven_Framework_for_Efficient_Visual_Tracking_CVPR_2026_paper.html
7. FlyVis/DMN, Nature 2024: https://www.nature.com/articles/s41586-024-07939-3
8. Structure alone, arXiv:2610.10023: https://arxiv.org/abs/2610.10023

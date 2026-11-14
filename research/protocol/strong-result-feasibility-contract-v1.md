# Strong-result feasibility contract v1 — unresolved, not accepted

Owner: ccf-experiment-designer. Binding scope, if accepted by subsequent gates: connectome/null-control sufficiency in visual computation, CVPR. This is an explicit prospective candidate and not a replacement for the still-missing final accepted contract. All observed entries below are prior-source facts; no recovery training has run.

## Calibration evidence and finite resources

Official TopoSens source reports a 45,669-node / 1,513,231-edge network, 734 free network parameters, 12 × 269-frame training stimuli (721 receptors), and 25.4/25.9 seconds per bio/degree-null update for seed 0 in its packaged ten-step run. These are third-party timing values on unverified hardware, not our 4090 timings. The decoder adds its own trainable parameters. Three official ten-step seeds have final average MSE .504455/.502693; balanced unit-direction zero output gives .5 analytically. These observations motivate a baseline audit but do not establish recoverable information or plausible effect size.

Our completed remote source/hardware-only task21782 measured RTX4090, Torch2.11.0+cu130, 44.388GiB total device memory. It ended without the requested audit outputs; its run.log is partial evidence. Local Conda/MPS matrix smoke passed; full flyvis MPS feasibility is unknown. Training should run on the authorized exp-4090 pool.

Pilot ceiling: two sequential single-GPU tasks, each <=2h, <=4h cumulative including setup. At the third-party nominal 26s/update, two models ×128 updates ≈1.85h before evaluation/setup; therefore the 128 ceiling is not a guaranteed runnable horizon. Fixed checkpoints 0,5,10,20,40,80,128; abort earlier when remaining time cannot complete and save artifacts. No extra seeds or optimizer search hidden in reruns. One Adam learning rate (official .001), fixed objective, no test tuning. Ridge regularization grid fixed before probes, selected on validation. Record every attempt, including OOM/nonfinite/unfinished jobs.

Confirmation planning envelope, conditional on S0/S1 measurements and scientific review: at most 64 single-GPU hours total additional compute. At nominal 26s/update, 12 seeds ×(1 bio+3 null)×128 ≈44.4h before evaluation; overhead may exceed64h, in which case lower cost via verified equivalent batching/checkpointing or reject the design. Do not silently reduce statistical precision or claim12 seeds are automatically sufficient. Expansion within this envelope still requires a recorded budget/feasibility gate; none is passed now.

## Targets are evidence rules, not desired score gains

| Claim | Minimum, sufficient only to retain a candidate | expected_strong, required before drafting | Failure / return |
|---|---|---|---|
| C0 implementation | Correct full model, actual CUDA parameters/tensors, finite update; same graph/parameter/split semantics | Reproduction and numerical-equivalence checks pass at documented tolerance; outputs/checkpoints/environment hashes available | Any mismatch stops the pilot until corrected. Passing C0 is not a paper finding. |
| C1 readout/projection dissociation | Both task competence and topology-gap estimability assessed against train-mean, input-only and temporal-CNN baselines; a specific reproducible assay interaction appears on validation | Fresh confirmation data show a practically meaningful seed-clustered assay × topology interaction, independent mask replication, and a matched readout/projection ablation that removes or predicts it; competence itself is not the explanation | No competence, no assay dissociation, probe-only training fit, or effect indistinguishable from decoder/scale controls returns to design; no generic train-longer paper. |
| C2 predictive mechanism | Train/validation predictor beats structural/scale baselines on a held-out validation-mask group, without using its outcomes for model selection twice | Frozen predictor improves held-out intervention prediction beyond every prespecified structural/scale comparator with a seed-clustered interval excluding zero improvement and with precision resolving the prespecified useful effect; replicate on independent workload. Algebraic test-label reconstruction does not count | Test-label residuals used in predictor, no out-of-sample improvement, rank driven by a single seed/mask, or readout label leakage invalidates claim. |
| C3 visual consequence | Independent procedural task provides coherent measured scope | At least one independently accessed natural/standard visual workload plus procedural setting confirms the stated mechanism against a task-matched strong baseline. If only procedural tasks are feasible, seek a fresh venue-fit decision before drafting | Unavailable natural data, unmanageable model adaptation or task-matched baseline failure blocks a broad CVPR story. |

## Pre-confirmation numeric lock, mandatory and currently unresolved

No defensible numeric scientific effect threshold can yet be inferred from a mean third-party loss near .5 without seed×mask variance or task-matched baseline behavior. It would be fabrication to select a headline gap now. The following algorithm is frozen prospectively, but its inputs are still absent:

1. Compute normalized skill against the train-target mean predictor. Estimate the strongest feasible simple/domain baseline's validation advantage over constant, and its seed variability.
2. Define practical-resolution margin from a documented task-level decision consequence, with validation-only baseline skill as a unit. Do not choose the margin to sit below the observed proposed-method gain. If no useful margin can be justified, C1/C3 are blocked.
3. Use pilot seed/mask variance only for cost and sample-size planning. With very few pilot seeds, use a conservative variance bound and report its uncertainty; never claim an exact powered sample size from n=1/2.
4. Freeze primary task, competence criterion, common horizon, effect direction or two-sided interaction, practical/equivalence margins, seed×mask count and predictor formula before confirmation labels/outcomes are opened. Publish both observed null and positive effects. A wide interval is inconclusive, not equivalence.
5. If required precision cannot fit the measured64h cap, return to mechanism/scenario selection. Do not lower expected_strong or reuse exposed tests as confirmation.

This contract explicitly fails acceptance today: a useful practical margin, independent predictive mechanism, competent training feasibility and natural-workload access remain unresolved. The final canonical strong-result-feasibility-contract.md and feasibility-contract.json must be written only after those issues have a scientifically defensible plan. A successful structural validator would not repair them.

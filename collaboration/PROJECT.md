# PROJECT — structure-sensitive null ladders in connectome-constrained vision

Recorded 2026-11-13 (Asia/Shanghai). Integrator: the project owner.
Status: **active, no qualifying manuscript yet**.

## User goal

One complete CVPR 2027 main-conference manuscript on whether biological wiring
topology confers a measurable advantage to visual computation, evaluated by
strict null-model controls. Acceptance (user-authorised iteration R107,
2026-11-13): a **new, isolated, independent `ccf-paper-reviewer full` report**
with `**Overall:** X` where **X >= 7.0**, plus machine gates
`QUALIFIED` + `COMPLETE`. Earlier standard was strictly > 8.0; R1–R106 were
judged under it and are not retroactively reinterpreted.

"Latest independent full review governs" is unchanged. Lowering the threshold
does not promote a historical 7.5 report to governing and does not make the
current 6.0 qualify. A new full review of a revised manuscript is required.

Big direction unchanged: evidence-first, real visual positive effect as the
scientific route, no submission / commit / push of the manuscript, no
fabricated results, no edited on-disk reviews.

## Current scientific protocol (primary project, not in this repo)

- Primary run root: `<local>/auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/`.
- Frozen protocol files: `ccfa-startup-packet/response-null-protocol-closure-v4.md`,
  `response-null-prediction-dataflow-v1.md`,
  `paired-edge-set-executable-spec-v3.md`,
  `prospective-identities-v1.json`, `pilot-input-manifest-v2.json`,
  `execution-contract-v3.md`. All unchanged.
- Frozen: 10 seeds, K=45 one-sided directional gates, family-wise alpha .05,
  noise-only calibration (std .08, lower clamp, 4 draws), `rawSMD<=.1`,
  sealed confirmation identities. Confirmation (<=32h panel) is **not
  authorised**; this is an explicit pending user decision.
- Ordered gates: `CCFA-startup` passed; **G0–G8, validation, handoff all
  pending**. f-research-v1 P0/P1A/P1B/P2 not started. Do not skip gates.

## True status (verified 2026-11-13)

- Governing independent full review: R95, **Overall 6.0 / Confidence 4.0**.
- Machine validator: `NOT_QUALIFIED` (6.0 < 7.0); guard: `INCOMPLETE`.
- Historical chain 7.5 → 6.9 → 6.3 → 5.4 → 5.2 → 6.0 all retained.
- **0 qualifying papers; no COMPLETE written.**
- No new full manuscript review has been run since R95.

## Established scientific facts (do not re-litigate without evidence)

- Controlled 96-node graph: real `0.8152` vs all null rungs / no-graph /
  shuffled-input `0.4795–0.5133`, 10 frozen seeds, BH q=0.0002. But the four
  nested rungs differ by at most `0.0244` and monotonicity is violated — the
  ladder has no localising power.
- A task-aware null preserving 18 injected motif edges recovers the advantage
  (`0.8346` vs `0.8371`, q=0.40); the motif-dose ladder collapses at <=9 edges.
- Real MaleCNS / real image tasks: negative or non-replicated boundaries,
  retained verbatim. Never delete these.
- Prior art (R99/R106 first-hand review): arXiv:2609.24565v2 (Kuklev 2026)
  already reports a large positive topology effect on a real visual task
  (intact 0.857 vs degree-preserving 0.539, +0.318 [0.296,0.339], 3 seeds,
  R7/R8 positive control 0.092), then bounds it (receptors-only 0.894 > fly
  0.835 on held-out; T4/T5 dispensable). G4 novelty risk is **high**.
  Note: two differently-worded v2 abstracts coexist on arXiv; the R99 citation
  used the paper-body abstract and is correct.
- Discriminative-prediction proposal D1 (v1, v2) was rejected in two
  independent reviews (`revise`, both with fatal flaws) and is
  `BLOCKED_ON_CONFIRMATION`. Do not reopen a v3 patch loop. Documents are in
  the primary project; reviews are retained unedited.

## Historical artefacts (primary project only, not uploaded)

- Main-matrix metrics from a 2026-11-08 exp-4090 job (`device=cuda`,
  `cuda_smoke_ok=True`), 10 seeds. That job also suffered a corrupted
  transferred script and an agent-authored repair that did not verify CRC;
  the local source was proven authoritative by CRC. Always EXEC LOCK + SHA.
- 8 Sintel-derived development clips, official model000/001 checkpoints and
  frozen runners exist locally; `import flyvis` verified in local Conda/MPS.
  The bottleneck is gate order and G4 positioning, not missing data or compute.

## Repo purpose and boundaries

This public repo is the collaboration/checkpoint layer. It contains sanitized
protocols, decision records, small reproducible scripts and evidence
manifests. It contains **no** credentials, datasets, model weights, third-party
source trees, local absolute paths, or unpublished manuscript. See
`../AGENTS.md`.

Integrator alone updates this file and `PROTOCOL.md`. Agent branches cannot
promote their self-reported results into a global acceptance claim.

# Task: r129-story-v3 — mechanism-discovery story selection + v3 manuscript + grid experiment

- Owner: project owner (integrator). Executing agent: `claude-fable` (this session, 2026-11-14).
- Input revision/branch: `main` @ 7d328c3 (post r128). Branch: `agent/r129-story-v3/claude-fable`.
- Protocol: `collaboration/PROTOCOL.md` v1. Scientific protocol unchanged: no threshold/split/seed edits, no fabricated numbers, negative results reported.
- Goal: per owner instruction (2026-11-14): keep the fly-connectome mechanism-discovery direction; re-read all current experimental results; pick and combine them into one coherent story (with reference to how CVPR 2026-era mechanism papers frame multi-scale adjudication, e.g. Kuklev et al. arXiv:2610.13018); optionally add fast local experiments (Apple M1 CPU only, must finish quickly); deliver a v3 manuscript and sync the record to this public archive.
- Story selected: **"When Does the Wiring Help? Path Survival and Density Gating Govern Topology Advantage in Connectome Vision"** — a two-factor mechanism (task-relevant path survival × background in-degree density) that unifies (i) the controlled null-ladder campaign, (ii) the real MaleCNS density sweep, (iii) the published cross-system disagreement (adult visual gains / flyvis null / larval-connectome null / whole-connectome cognitive gains / sensory-motor boundary null), and (iv) a NEW pre-registered density×survival grid (`results/r129_density_survival_grid/` in the primary project).
- New experiment: `r129_density_survival_grid` — 4 density scales × 3 motif-survival levels × 6 frozen seeds, controlled 96-node family, config + SHA frozen before training, ~13 min on Apple M1 CPU. This is a real, measured result; reported as-is.
- Acceptance (measurable):
  1. v3 manuscript compiles: 9 pages (8 body + refs/LLM page), 0 Overfull, 0 undefined refs, all numbers traceable to on-disk metrics.
  2. Grid experiment artifacts complete in primary project (config.json, PRE-REGISTRATION.sha256, run_grid.py, run.log, metrics.json, summary.txt).
  3. Public archive gains: v3 manuscript, grid results, this task record, agent handoff, checkpoint + manifest; no credential-containing file, nothing >50 MiB.
  4. Remote branch SHA == local HEAD after push (verified via `git ls-remote`).
  5. No claim of acceptance/qualification; governing review remains R95 = 6.0 until a new independent full review of the v3 manuscript.
- Out of scope: changing frozen protocols/thresholds/seeds; merging to main (integrator only); declaring the paper qualified; submitting anywhere.
- Writers: `claude-fable` → `collaboration/tasks/r129-story-v3/**`, new files under `research/manuscript/story-v3-when-wiring-helps/`, `research/results/r129_density_survival_grid/`, `research/ideas/story-v3-selection.md`, `research/rounds/R129-*`, `research/UPLOAD-MANIFEST-R129.json`. Does NOT rewrite `research/README.md`, `UPLOAD-MANIFEST.json`, `AGENTS.md`, or any wb-main file; integrator merges.

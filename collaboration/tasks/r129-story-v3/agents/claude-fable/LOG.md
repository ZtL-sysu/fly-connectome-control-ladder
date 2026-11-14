# LOG — claude-fable @ r129-story-v3

## 2026-11-14 (single session)

- Re-read project per research-github-sync phase A; inventoried all verified
  result families (controlled null-ladder campaign, r39 real-wiring density
  sweep, R63 chains incl. the R68-audited degenerate `r63_spectral_repl`
  positive flag).
- Story selected: two-factor gating mechanism ("When Does the Wiring Help?").
  Rationale: `research/ideas/story-v3-selection.md`. Learned narrative pattern
  from Kuklev et al. (arXiv:2610.13018): multi-level claim decomposition +
  preregistered scoreboard + conditional verdicts.
- Live collision check: added larval-connectome null repo, Park 2609.39248,
  Cho 2610.10014 as citations (all fetched first-hand).
- New pre-registered experiment `r129_density_survival_grid` (Apple M1 CPU,
  ~13 min): 4 densities × 3 survivals × 6 seeds.
  - Pre-reg v1 defect caught BEFORE training (wrong graph seed) → corrected
    to exact main config, recorded in config.json.
  - Run-1 implementation defect caught by inspecting output (deleted motif
    edges not removed at high density; s32/s64 cells identical) →
    `RUN1-DEFECT-AND-FIX.md`, run-1 preserved, fix enforces exact survival,
    run-2 is the reported result. All three preregistered predictions PASS.
- v3 manuscript compiled: 9 pages, 0 Overfull, 0 undefined, 18 refs,
  Conclusion complete on p8, p9 = LLM statement + refs. All 12 grid effects in
  the PDF verified == run-2 metrics.json (programmatic, unicode-minus aware).
- Synced: this task record, v3 manuscript, grid results, story-selection note.
- Governing review unchanged: R95 = 6.0. v3 not independently reviewed.
  No protocol/threshold/seed changed. No submission performed.

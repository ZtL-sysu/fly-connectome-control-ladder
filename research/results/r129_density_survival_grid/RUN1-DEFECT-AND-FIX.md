# R129 grid — run-1 implementation defect and fix (registered before rerun)

- **Defect (found by inspecting run-1 output, 2026-11-14)**: for density scales
  s>=8, the background graph independently re-contains some or all of the 18
  motif edges (intra-module edge probability 0.48 at s=8, ~1.0 at s>=32).
  run-1 code only *added* kept motif edges but never *removed* deleted ones, so
  the k=9 and k=0 deletions were silently not enforced at s>=8. Symptom, found
  by inspection: s32/s64 cells identical across k to 4 decimals. Run-1 files
  preserved: `metrics_run1_defective.json`, `summary_run1_defective.txt`,
  `run1_defective.log`. Conclusion of run 1 is NOT used in the paper.
- **Fix (design unchanged; enforcement corrected)**: `grid_graph` now sets
  every motif edge to 1 iff kept else 0, so survival k is exact at every
  density. The frozen pre-registered design (config.json) always stated
  "delete (18-k) uniformly chosen motif edges"; the fix enforces it.
- **Rerun**: run 2, same frozen config, seeds, data and code import; new
  SHA of run_grid.py recorded in PRE-REGISTRATION.sha256.
- The defect itself is recorded honestly and kept on disk per project
  discipline (no silent reruns).

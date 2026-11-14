# CHECKPOINT 2026-11-14T123000Z — r129-story-v3 complete (work state, not scientific validation)

## Facts
- v3 manuscript "When Does the Wiring Help? Path Survival and Density Gating
  Govern Topology Advantage in Connectome Vision" compiled: 9 pages, 0 Overfull,
  0 undefined refs, 18 refs; main.tex == paper.tex byte-identical.
- Grid experiment r129_density_survival_grid run 2 (defect-fixed) complete:
  P1/P2/P3 all True; 12/12 cell effects verified present in the PDF and equal
  to research/results/r129_density_survival_grid/metrics.json.
- Run-1 defect preserved and documented (RUN1-DEFECT-AND-FIX.md).
## Commands
- Recompile: pdflatex main && bibtex main && pdflatex main && pdflatex main
  (in research/manuscript/story-v3-when-wiring-helps/manuscript).
- Grid rerun: python run_grid.py (in research/results/r129_density_survival_grid).
## Checks
- Credential scan of the 33 staged files: NONE. >50 MiB: NONE.
## Supported vs unsupported
- Supported: the two-factor interaction on ONE controlled graph family with
  six seeds; density gating on one real MaleCNS sweep; cross-system
  literature coordinates (qualitative).
- Unsupported: any claim of qualification/acceptance (governing review still
  R95=6.0); quantitative grid generalisation across graphs.
## Artifacts
- research/manuscript/story-v3-when-wiring-helps/ (v3 manuscript)
- research/results/r129_density_survival_grid/ (config, SHA, code, logs, metrics)
- research/ideas/story-v3-selection.md; research/UPLOAD-MANIFEST-R129.json
## Risks
- v3 manuscript not independently reviewed; linespread 0.845 is aggressive.
- `\paperID{*****}` placeholder; LLM statement wording to be owner-verified.
## Next action
- Fresh isolated `ccf-paper-reviewer full` on the v3 manuscript if the owner
  wants a governing score; otherwise widen the grid across graph realizations.
Status: completed (work state).

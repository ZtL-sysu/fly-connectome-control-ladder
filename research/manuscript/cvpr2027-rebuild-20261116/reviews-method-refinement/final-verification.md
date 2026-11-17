# Final verification: revision-method-refinement

- Main paper: 9 PDF pages, with scientific content ending on page 8 and the LLM statement and references on page 9.
- Supplement: 7 pages.
- LaTeX compiles with `latexmk -pdf -halt-on-error`; no undefined references, undefined citations, or overfull boxes remain.
- Figures are rebuilt from archived records by `analysis/make_figures.py`. No model training or new evaluation was performed.
- Verified against archived records: narrow transfers `[[2,1],[2,1]]`, `[[1,0],[1,1]]`, `[[1,0],[1,0]]` after scaling by 16; source-109 residuals 0, 0.001953125, 0; CIFAR source readouts 0.164/0.566/0.096 and preserved source 0.440.
- Independent full review: Overall 6.0, confidence 5; recommends replacing the 5.5 locked draft.
- Reviewer-posted fixes applied: the private residual is cross-referenced in the Introduction, the abstract no longer says the geometry "explains" behavior generally, and Fig. 4 is labelled as a schematic in transfer-feature space.
- Remaining substantive risks are unchanged: one animal, related graph extractions, a fixed linear operator, post-hoc reconstruction of historical interventions, and narrow visual readout probes.

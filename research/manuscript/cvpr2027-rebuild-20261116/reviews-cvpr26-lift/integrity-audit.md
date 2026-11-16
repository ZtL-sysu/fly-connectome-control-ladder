# Superseded draft audit

This audit covered an earlier draft containing a coefficient-noise margin.
That bound and its table were removed after detecting inconsistent
normalization between the written definition and the numerical script. Do
not use this file as a final audit. See `final-verification.md` for the
current status.

Mode: full (historical draft)

Artifacts checked:
- revision-cvpr26-lift/main.pdf (9 pages: 8 content pages plus LLM statement and references)
- revision-cvpr26-lift/supplement.pdf (8 pages)
- revision-cvpr26-lift/sections/*.tex and supplement.tex
- analysis-cvpr26-lift/visibility-margin.json and visibility_margin.py
- archived analysis/executed-readout.json, population-identity-readout.json, cifar-identity-readout.json, ideal-task-assumption-checks.json
- existing reviews in reviews/

Claim-evidence matrix:
- Two matched zero-common-relay graphs with different source access: supported by narrow k=4 reconstructed transfers and archived accuracies; provenance remains post-hoc.
- Nonzero k=8 doses retain ideal label information while finite accuracy rises: supported by reconstructed gains, Proposition 1, and archived accuracies.
- Executed MLP replay separates source visibility and transfer rank: supported by executed-readout.json; numbers match table.
- CIFAR private-column result: supported by cifar-identity-readout.json and the 0.571 encoder ceiling; no connectome-specific recognition is claimed.
- Closed-form coefficient-noise margin: supported by visibility-margin.json and archived basis singular values; scoped to nearest-union-subspace decisions and explicitly not a learned-model guarantee.
- Structural labels as functional certificates: explicitly rejected; claim is reporting-level.

Numeric consistency findings:
- Abstract CIFAR numbers (0.566, 0.096, 0.440) match the CIFAR identity record and Table 8.
- The retained UCI digit-identity sentence (0.852, 0.099, 0.698) matches population-identity-readout.json.
- Margin ratios 0.115/0.231/0.461/1.153/2.305 for base and 0.058/0.115/0.231/0.576/1.153 for named-edge match the new JSON.
- Minimum concatenated-basis singular value 5.42e-3 matches the archived ten-seed assumption check.
- No numeric contradictions or stale parity values remain in the revised abstract.

Citation metadata findings:
- All cite keys used in main and supplement resolve in references.bib.
- No new citation was added during this revision.

Citation-context findings:
- Park and Dhiman remain positioned as closest boundary/staged-control precedents.
- The CVPR/NIPS mechanism papers support the protocol framing; no unsupported novelty claim was added.

Severity: no major integrity issue. Residual medium risk is the original missing k=4 dose-instance hashes and one-animal scope, both disclosed.

Safe edit suggestions:
- Keep the supplement's explicit statement that the margin bound is sufficient and does not cover arbitrary readout noise.
- Preserve the 8-page content boundary by leaving the margin table in the supplement.

Next CCFA owner: ccf-paper-reviewer for independent full review.

No-invention status: no new number, citation, dataset, or experiment was invented. The added analysis is a deterministic closed-form computation over archived matrices and basis recipes.

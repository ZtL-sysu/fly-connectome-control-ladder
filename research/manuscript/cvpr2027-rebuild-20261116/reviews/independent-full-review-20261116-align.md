# Independent full review

Overall: 5 | Scholarly Confidence: 4

Target: CVPR 2027 main conference. Reviewed from the current `revision/main.pdf` (9 pages, compiled 2026-11-16 10:31) and `revision/supplement.pdf` (7 pages). Table 6 and the executed-readout record were checked against the rewritten introduction and the LLM usage statement. The 120 training runs were not repeated.

## Decision

Borderline reject. The audit is coherent, the executed numbers match the table, and the two passages that previously overstated the visual result now agree with it. The paper still does not show that this audit changes a visual computation. The new evidence is a parity-XOR probe of three reconstructed \(2\times 2\) transfers.

## The corrected passages against Table 6

Table 6, as printed, is:

| Graph | \(\lvert\mathcal C\rvert\) | rank | Subspace | Visual |
| --- | ---: | ---: | ---: | ---: |
| Base | 2 | 1 | 0.976 | 0.663 |
| Named-edge zero | 0 | 2 | 0.979 | 0.746 |
| Path zero | 0 | 1 | 0.504 | 0.506 |

The introduction now says that, among graphs that retain both sources, visual accuracy follows transfer rank, and that it falls to chance only when a source column is deleted. That is what the table shows. Base and named-edge zero both keep both sources; rank 2 reaches 0.746 and the parallel rank-1 mixture reaches 0.663. Path zero deletes the source-\(b\) column and falls to 0.506. The abstract’s order, invertible then parallel then deleted, is the same comparison. The old claim that visual accuracy follows whether both sources are isolated is gone from the PDF.

The usage statement now says the new comparisons train the archived MLP and a linear control on reconstructed transfers, and that original archived weights were not reloaded. That matches the experiment: same \(32\to 64\to 1\) ReLU architecture, Adam at learning rate 0.006, 120 epochs of 32 batches of 128, ten recorded seeds, with a linear control that removes the hidden layer. The subspace means 0.976, 0.979, and 0.504 sit next to the historical fits 0.9772, 0.9745, and 0.5055 without being presented as reloaded weights.

The contribution bullet is coarser. It says the visual parity XOR follows transfer rank rather than the common-relay count. Rank does beat the relay count: two relays score 0.663, while zero relays with rank 2 score 0.746. Rank alone does not separate the two rank-1 rows, 0.663 and 0.506. The introduction supplies the missing deletion clause, so this is a compression, not a contradiction.

## Scores

| Criterion | Score | Reason |
| --- | ---: | --- |
| Soundness | 3 | Proposition 1, the reconstructions, and Table 6 are consistent, and the visual sentence now follows the table. Dose-instance hashes are still absent. |
| Novelty | 2 | Motif count, column support, and rank are separated cleanly. The transport step and the parity probe are standard. |
| Significance | 2 | The audit changes these intervention reports. It does not change a visual model or a recognition result. The CIFAR control is negative. |
| Clarity | 3 | Ideal and finite accuracy, reconstruction limits, and the visual ordering are stated carefully. The contribution bullet is less precise than the introduction. |
| Experimental rigor | 3 | Ten seeds, matched graphs, and a linear control are in place. The new runs were checked from the recorded readout, not retrained here. |

## What the evidence supports

On the subspace XOR, source visibility is enough. The rank-1 base and the rank-2 named-edge graph both stay near 0.98, and the deleted-source graph stays at 0.504. Every linear readout stays near one half, including where the MLP exceeds 0.97. That answers the objection that the result is only a linear image of \(T\).

On the visual parity XOR, visibility is not enough. The label is the XOR of two digit parities after a fixed projection of 32-pixel halves to 16 dimensions. Independent columns beat parallel columns, and a zero column returns chance. A linear readout remains at chance on all three graphs, so this is not the supplement’s digit-field ceiling. The paper says that explicitly.

The older audit remains the stronger result. Named-edge zero and path zero share an empty common-relay family and the same degree and module counts, but only one keeps both sources. Nonzero \(k=8\) doses retain ideal label information while finite accuracy still rises from about 67% to above 94%; the zero dose is separately at chance. Degree and protected nulls can regain the task after a zero-dose graph has lost it. The nearest-subspace check is perfect at every positive source gain, including \(1/64\).

## What keeps it below the bar

Both task sources are known, every other node is silent, and two linear steps reduce the connectome to \(T\). The visual task then asks a small MLP to recover a parity XOR of those two inputs. That is a useful diagnostic of three matrices. It is not evidence about connectome-constrained vision. The reverse-support CIFAR-10 subset remains negative, with gaps \(-0.0044\) and \(-0.0019\). The graphs come from one male connectome, the \(k=8\) extractions overlap, and the dose operators are post-hoc replays.

The supplement’s provenance paragraph still describes the digit-field assay as a new linear fit and says the archived-accuracy analysis did not retrain archived models. That is true of those older analyses. It does not mention the executed MLP section, which does train new readouts. The main-text usage statement is the accurate one.

## Confidence

Four. The current PDF, Table 6, and the recorded readout agree on the ordering and on the corrected sentences. Confidence is not higher because the training runs were not executed again for this review.

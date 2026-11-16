# Independent full review

Overall: 5 | Scholarly Confidence: 4

CVPR 2027 main conference. Read from the current `revision/main.pdf` (9 pages) and `revision/supplement.pdf` (7 pages). Every new digit-identity mean was checked against `analysis/population-identity-readout.json`. The training runs were not repeated. The earlier parity readout is a separate comparison and is not Table 7.

## Decision

Borderline reject. Changing the label from digit parity to digit identity makes the assay a real 10-way classification, and the printed numbers match the recorded readout. The dissociation is clean: a private column supports identity, a deleted column returns chance, and the same path-zero graph still identifies a preserved source. The images nevertheless never enter a visual model. Four or eight projected digits are written onto selected neurons, mixed by a two-step linear operator, and read at two sinks.

## The identity numbers

Sources `{109, 107, 152, 6}` each receive an independent digit. The label is the class of one source, so chance is 0.1. A `32→64→10` MLP and a linear `32→10` control see sinks `(4, 5)` after incoming-normalized `W^2`. The JSON records cross-entropy, Adam at learning rate 0.006, 120 epochs of 32 batches of 128, ten seeds, and MPS. Each accuracy is 2,048 draws with replacement from 450 held-out digits, as the paper now says. Training uses the other 1,347 images.

Table 7 matches the four-source means after rounding to three decimals:

| Label | Graph | Private energy | MLP | Linear |
| --- | --- | ---: | ---: | ---: |
| 109 | Base | 0 | 0.192383 | 0.192383 |
| 109 | Named-edge zero | 0.001953125 | 0.851807 | 0.652539 |
| 109 | Path zero | 0 | 0.098633 | 0.101807 |
| 107 | Base | 0 | 0.353418 | 0.356494 |
| 107 | Named-edge zero | 0 | 0.691699 | 0.628955 |
| 107 | Path zero | 0 | 0.697656 | 0.640381 |

The abstract’s 0.852, 0.099, and 0.698 are the named-edge MLP, the path-zero MLP on that same source, and the path-zero MLP on the preserved source. The body is equally exact: path zero reads source 107 at 0.698 and source 109 at 0.099; the named-edge MLP reaches 0.852 and its linear control 0.653; both base readouts are 0.192.

The geometry claims hold for this record. Named-edge source 109 has energy `0.00390625` and private residual `0.001953125`, exactly half. The base column has energy `0.0078125`, twice that value, and no private residual. Path zero removes the column. Source 107 has column `[0.125, 0.125]` and energy `0.03125` on every graph.

Eight active digits preserve the MLP split, and the sentence names the MLP. Source 109 scores 0.801123, 0.179150, and 0.097559 on named-edge, base, and path zero, printed as 0.801, 0.179, and 0.098. Source 107 scores 0.464502, 0.320508, and 0.468555, printed as 0.465, 0.321, and 0.469. The old parity figures 0.870 and 0.822 are not in this PDF.

## What the identity result shows

Path zero and named-edge zero remain degree- and module-matched, with no common-relay triples. Identity does not collapse globally. Source 107 stays near 0.69 on both graphs, while source 109 falls from 0.852 to chance. The linear map follows the same division at a lower level, so the 10-way result is not an MLP-only artifact.

The base graph is the useful negative. It delivers more energy from source 109 than the named-edge graph, but that column lies in the span of the other three. Accuracy stays at 0.192, above the 0.1 chance line and far below 0.852. Column norm is not the predictor. The private residual is. The paper states 0.192 rather than calling the base result chance, which is the correct reading.

Source 107 also shows that an identical column is not an identical task. Its transfer column matches across the three graphs, but the base MLP reaches only 0.353 while the two zero-dose graphs reach 0.692 and 0.698. The paper does not claim those three accuracies are equal. The matched comparison is the two zero-dose graphs; the base mixture has a different interfering column.

## Scores

| Criterion | Score | Reason |
| --- | ---: | --- |
| Soundness | 4 | Table 7, the abstract, the base-energy claim, and the eight-source MLP sentence match the identity JSON. |
| Novelty | 2 | Identity is a harder label than parity, but the separation of motif count, column energy, and private residual is still linear transport. |
| Significance | 2 | The assay changes the reading of these edits. It does not change a visual system, and the CIFAR control remains negative. |
| Clarity | 3 | Chance, the resampling rule, and the MLP-versus-linear gap are stated. Table 7 splits the eight-source sentence across a page. |
| Experimental rigor | 3 | Ten seeds, a preserved source, a linear control, and a disclosed 450-image held-out pool are in place. The sources were selected for their known columns. |

## What keeps it below the bar

The designated sources are the columns already known to differ at these two sinks. A deleted column returning chance is the linear prediction. The empirical content is that both readouts track that geometry under simultaneous 10-way labels, and that extra energy without a private direction adds only a small lift over chance.

The digits are the 1,797 UCI `8×8` images, reduced by one fixed `64×16` projection. Evaluation resamples 450 held-out images. This is not a standard recognition protocol, and the discussion correctly says so. The reverse-support CIFAR-10 subset remains a negative control, with gaps `-0.0044` and `-0.0019`.

The remaining scope is unchanged: one male connectome, overlapping `k=8` extractions, unavailable original dose-instance hashes, and a fixed linear prefix. Proposition 1 is still the noiseless subspace criterion. The discussion uses “population result” both for that criterion and for source access in this subgraph; the identity assay should not be read as the Bayes proposition.

## Confidence

Four. All printed identity means were recomputed from the JSON, and the compiled PDF contains those rounded values rather than the earlier parity figures. Confidence is not higher because the training was not run again.

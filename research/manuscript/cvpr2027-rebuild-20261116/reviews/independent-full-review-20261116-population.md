# Independent full review

Overall: 5 | Scholarly Confidence: 4

CVPR 2027 main conference. Read from the current `revision/main.pdf` (9 pages) and `revision/supplement.pdf` (7 pages). The four- and eight-source means were recomputed from `analysis/population-label-readout.json`. Column energy and private residual were recomputed from the three reconstructed narrow graphs. The training runs were not repeated.

## Decision

Borderline reject. The new assay is the right control for the audit, and its printed numbers are accurate. It shows that a degree-matched deletion can remove one digit label while leaving another readable, and that a larger column norm is not a substitute for a private direction. That is still a parity readout on four or eight projected digits driven through a two-step linear mixer. It does not establish a connectome visual model or a recognition result.

## The population readout

Sources `{109, 107, 152, 6}` are driven together on the base, named-edge-zero, and path-zero reconstructions. Propagation is the incoming-normalized operator `W^2`. The archived `32→64→1` ReLU MLP, and a linear control, see only sinks `(4, 5)`. The label is the parity of one source. Means are ten seeds, and the recorded device is MPS.

Table 7 matches the four-source JSON after rounding to three decimals:

| Label | Graph | Private energy | MLP | Linear |
| --- | --- | ---: | ---: | ---: |
| 109 | Base | 0 | 0.563965 | 0.569092 |
| 109 | Named-edge zero | 0.001953125 | 0.869629 | 0.754150 |
| 109 | Path zero | 0 | 0.502344 | 0.497217 |
| 107 | Base | 0 | 0.661768 | 0.644141 |
| 107 | Named-edge zero | 0 | 0.814258 | 0.723486 |
| 107 | Path zero | 0 | 0.822461 | 0.725781 |

The geometry sentences are also exact. On the named-edge graph, source 109 has column `[0, 0.0625]`, energy `0.00390625`, and private residual `0.001953125`, which is half. The base column is `[0.0625, 0.0625]`, energy `0.0078125`, exactly twice the named-edge energy, with a numerical private residual of zero. Path zero removes that column. Source 107 has the same column `[0.125, 0.125]` and energy `0.03125` on all three graphs, with no private residual. The abstract’s 0.870, 0.502, and 0.822 are the named-edge, path-zero, and preserved-source MLP means.

Eight active sources preserve the MLP split. Source 109 scores 0.822705, 0.556641, and 0.500391 on named-edge, base, and path zero, printed as 0.823, 0.557, and 0.500. Source 107 scores 0.706836, 0.637402, and 0.709277, printed as 0.707, 0.637, and 0.709. The sentence does not name the readout. Those values are the MLP means. The unreported linear means keep the same pattern: 0.743, 0.564, and 0.506 for source 109, and 0.667, 0.626, and 0.666 for source 107.

## What this adds

The two-source parity XOR left every other node silent, so deleting one source also removed half of the task. Four simultaneous digits separate those effects. Path zero and named-edge zero still share the empty common-relay family. On source 107 the MLP stays at 0.822 against 0.814. On source 109 it falls from 0.870 to 0.502. The deletion is source-specific.

The base graph blocks the other easy explanation. It puts more energy on source 109 than the named-edge graph does, but that column lies in the span of the other three. Both readouts stay near 0.56. A private residual of `1/512`, not the column norm and not the relay count, is what the named-edge readout can use. The linear control follows the same division, at a lower level: 0.754 where the MLP reaches 0.870, and chance where the column is absent. This task does not need the nonlinearity that the subspace XOR required.

## Scores

| Criterion | Score | Reason |
| --- | ---: | --- |
| Soundness | 4 | Table 7, the half-energy claim, the doubled base energy, and the eight-source MLP means match the graphs and the recorded readout. |
| Novelty | 2 | Private residual, column support, and motif count are cleanly separated. The transport and the parity probe are standard. |
| Significance | 2 | The contrast changes the interpretation of these matched edits. It does not change a visual system or a recognition benchmark. |
| Clarity | 3 | The four-source comparison is stated with the right caveats. The eight-source sentence omits the word MLP, and Table 7 floats onto the next page ahead of its discussion. |
| Experimental rigor | 3 | Ten seeds, a preserved-source control, and a linear control are present. The evaluation resamples 2,048 draws from 450 held-out digits, which the paper does not say. |

## What keeps it below the bar

The sources were chosen because their columns already differ at the two audited sinks. Once `T` is known, chance after a deleted column is the expected linear consequence. The empirical residue is that the MLP and the linear map both follow that geometry while distractor digits are active, and that raw energy without a private direction is not enough. That is a good check on three `2×4` slices of `W^2`. It is not evidence about the connectome as a visual population.

The images are the 1,797 UCI `8×8` digits, projected by one fixed `64×16` map. Training uses 1,347 images. Evaluation draws 2,048 samples with replacement from the remaining 450, so the reported accuracy is not one pass over 2,048 independent images. The label is parity, not identity. The discussion correctly refuses a natural-image benchmark, and the reverse-support CIFAR-10 subset remains negative at gaps `-0.0044` and `-0.0019`.

The older limits remain. One male connectome, overlapping `k=8` extractions, unavailable original dose-instance hashes, and a fixed linear two-step prefix. Proposition 1 still applies to the noiseless subspace task, not to this digit parity assay. The paper keeps those boundaries.

## Confidence

Four. Every printed four-source mean, the eight-source MLP sentence, and the private-energy claims were checked against the JSON and recomputed from the reconstructed adjacency. Confidence is not higher because the 120-step training was not run again.

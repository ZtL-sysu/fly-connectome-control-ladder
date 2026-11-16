# Independent full review

Overall: 5 | Scholarly Confidence: 4

CVPR 2027 main conference. Read from the current `revision/main.pdf` (9 pages) and `revision/supplement.pdf` (7 pages). CIFAR means and the 0.571 ceiling were checked against `analysis/cifar-identity-readout.json`. The retained UCI sentence was checked against `analysis/population-identity-readout.json`. The training runs were not repeated.

## Decision

Borderline reject. The CIFAR assay is the right stress test, and the printed means match the record. A private column passes a frozen image code at the code's own accuracy, a deleted column returns chance, and the same path-zero graph still reads another source. The connectome does not see the images. A small convolutional net makes a 16-dimensional code, four codes are mixed by a two-step linear operator, and two sinks are decoded. Matching the ceiling shows that the code survived. It does not show that the wiring recognizes CIFAR-10.

## The CIFAR numbers

The encoder is trained on 30,000 images from local batches 2--4, then frozen. Its own linear head scores 0.5708 on the official 10,000-image test set, printed as 0.571. Sources `{109, 107, 152, 6}` receive independent codes. The label is the class at one source, so chance is 0.1. The recorded readout is a `32→64→10` MLP or a linear `32→10` map, Adam at learning rate 0.006, cross-entropy, 80 epochs of 24 batches of 128, ten seeds, and 2,048 resampled official test images. The device is MPS. The PDF states the resampling and the ten seeds. It does not state the 80-by-24 budget, which is shorter than the archived 120-by-32 protocol.

Table 7 matches the JSON after rounding to three decimals:

| Label | Graph | Private energy | MLP | Linear |
| --- | --- | ---: | ---: | ---: |
| 109 | Base | 0 | 0.163818 | 0.166211 |
| 109 | Named-edge zero | 0.001953125 | 0.566260 | 0.558057 |
| 109 | Path zero | 0 | 0.096387 | 0.098291 |
| 107 | Base | 0 | 0.281006 | 0.277148 |
| 107 | Named-edge zero | 0 | 0.441162 | 0.434229 |
| 107 | Path zero | 0 | 0.440088 | 0.434424 |

The abstract's 0.571, 0.566, 0.096, and 0.440 are the ceiling, the named-edge MLP, the path-zero MLP on that source, and the path-zero MLP on the preserved source. The body is also right that path zero reads source 107 at 0.440 and source 109 at 0.096, and that the linear control reaches 0.558. One sentence is slightly tighter than the table: it says both base readouts stay at 0.164, while the linear mean rounds to 0.166. The table itself is correct.

The UCI comparison is a separate record and is quoted correctly. On four-source digit identity, the named-edge MLP is 0.851807, path zero is 0.098633, and the preserved source is 0.697656, printed as 0.852, 0.099, and 0.698.

The column geometry is the same transfer used for that digit assay. Named-edge source 109 has energy `0.00390625` and private residual `0.001953125`, exactly half, printed as 0.00195. The base column has twice that energy and no private residual. Path zero removes it. Source 107 has the same high-gain column on all three graphs and no private residual.

## What the ceiling comparison shows

Named-edge recovery is real. The MLP mean is 0.566 against a ceiling of 0.571, and the ten seeds run from 0.553 to 0.581. The linear control is 0.558. Once the column has a private direction, both readouts extract essentially the class information already present in the frozen code. The hidden layer is not doing a separate visual computation.

Path zero keeps the comparison source-specific. Source 107 remains at 0.440, well above chance and well below the ceiling, while source 109 falls to 0.096. Degree, module count, and the empty common-relay family do not explain that split. The base graph blocks the other easy account: it delivers more energy from source 109, but the column lies in the span of the other three, and accuracy stays near 0.16. Extra aligned energy is not a private direction. The preserved source also shows that an identical column is not an identical mixture. Source 107 is only 0.281 on the base graph and about 0.44 on the two zero-dose graphs.

## Scores

| Criterion | Score | Reason |
| --- | ---: | --- |
| Soundness | 4 | The ceiling, Table 7, and the UCI sentence match the two JSON records. The base sentence rounds 0.166 down to 0.164. |
| Novelty | 2 | CIFAR replaces an easy digit label, but the object being tested is still a known 2-by-4 transfer of a frozen code. |
| Significance | 2 | The audit changes these matched edits. It does not produce a connectome recognition result, and the reverse-support control remains negative. |
| Clarity | 3 | The ceiling is in the abstract, and the paper refuses a benchmark claim. The main text does not give the readout's epoch budget. |
| Experimental rigor | 3 | Ten seeds, an official test pool, a linear control, and the missing local batches are recorded. The four sources were chosen because their columns differ. |

## What keeps it below the bar

The images stop at the encoder. That encoder is a two-convolution network trained for five epochs at learning rate 0.001, and its linear head is only 0.571 accurate. The supplement states why the training set is 30,000 images: local batch 1 is absent and batch 5 does not unpickle. The graph then transports the resulting 16-dimensional codes. Recovering 0.566 is evidence that the private column preserved this weak code, not that MaleCNS wiring classifies CIFAR-10.

The separate reverse-support subset control still finds no connectome-specific gain, with gaps `-0.0044` and `-0.0019`. The older limits remain: one male connectome, overlapping `k=8` extractions, unavailable original dose-instance hashes, and a fixed linear prefix. Proposition 1 is the noiseless subspace criterion. The discussion's "population result" should not be read as this CIFAR assay.

## Confidence

Four. Every printed CIFAR mean, the ceiling, and the retained UCI sentence were recomputed from the JSON files and found in the compiled PDF. Confidence is not higher because neither the encoder nor the ten readout seeds was run again.

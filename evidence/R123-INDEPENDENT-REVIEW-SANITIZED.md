# R123 — Independent recheck recovered (sanitized public summary)

**Nature**: gate / evidence-layer recheck, NOT a full manuscript review. No scored verdict
line was produced; governing was not self-assessed; no `**Overall:**` numeric line.

The primary-project independent report itself is **not uploaded** (per the R117 precedent it
contains local absolute-path literals). This is a sanitized summary; all local absolute paths
are written as `<local>/`. No credential value, no email, no dataset, no weight, no binary, no
third-party source code, no unsubmitted manuscript.

## Recovered verdict

Fresh isolated sub-agent, no expected verdict / score anchor / conclusion anchor supplied.
Final report **16,565 bytes / 105 lines**, SHA-256
`40edc181845f5d5086e7ee3dc71c6515861d2061c41be8d688301f45cb744408`, one write, original
unchanged. Verdict:
`REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`.

- **A–F: 6 MATCH / 0 MISMATCH.** Reviewer used only its own logic on the 13 frozen raw byte
  files (no collector/verifier import, no round-produced JSON as a data source, round audit
  read LAST for defect grading); ran no verification script, no git, no network, modified no
  existing file.
- **12 named overclaim categories: CONFIRMED 0 / REFUTED 12.**
- **Defects: HIGH 0 / MEDIUM 1 / LOW 1** (2 total); one "fact error / data inconsistency",
  one "scope not delimited", **fabrication 0**.

Key independent confirmations: 13/13 raw byte counts and SHA-256 match the manifest, all
< 200 KB, no binary / weights / dataset, `upload_to_public_repo=false` exactly 1 file;
Zenodo record-level CC BY 4.0 is the only licence field (20 file objects have no per-file
licence key), README `Licence and attribution` verbatim, MANIFEST.csv 18 data rows,
SHA256SUMS 19 lines, record API 20 files, 18/19/20 self-reference nesting holds, README
SHA-256 matches in three places; Sintel licence is a custom MPI non-commercial
scientific-research licence with `CC BY` / `Creative Commons` each 0 mentions; official flyvis
`spdx_id=MIT` and full MIT `license` text, but the weights download script goes through a
Google Drive folder plus an `api_key` and contains zero weight/checkpoint licence text;
FlyHack abstract page has 0 github.com / 0 Zenodo mentions and one repo search returned
`total_count=0` / `items=[]`, scoped as query-scoped negative evidence.

## Two defects, both accepted append-only

**W-1 [MEDIUM — fact error / data inconsistency, NOT fabrication]**: the round audit's
section-3 category-byte table wrote the six Zenodo files as `152,578` bytes; byte-exact
recount gives **152,628** (a 50-byte difference). The other three rows (13,208 / 12,065 /
84,827) are correct; the erroneous row makes the four-row sum 262,678, contradicting the
same document's heading (262,728) and the manifest `total_bytes=262728`. Recount by the main
session: 10,603 + 131,225 + 4,061 + 2,615 + 2,267 + 1,857 = **152,628**; four-group total
**262,728**, consistent with the heading, manifest, and the reviewer's own A-group recount.
Impact strictly scoped: the error exists **only in one derived summary number** in the round
audit; it does not propagate to any raw byte, SHA, manifest, either verifier reading (v2
91/91), machine gate, gate state, governing, A–F conclusions, or the 12 overclaim rulings.
Per append-only discipline the round audit bytes are **not rewritten** and the already
published eighteenth checkpoint is unchanged.

**W-2 [LOW — scope not delimited]**: "zero local paths / no local path" in the manifest
`scope_note` and round audit section 3 was not explicitly limited to "**the 13 raw frozen
files only**". Those 13 raw files do have 0 hits (A/F unaffected), but two same-directory
derived guard-output files and the independent report itself contain local absolute-path
literals. This is **not a factual misstatement**, only an imprecise scope. Corrected wording:
local absolute paths 0 hits **in the 13 raw frozen files**; guard outputs and the independent
report are local-only and are not uploaded to the public repository. The 6-file public upload
set has 0 local-absolute-path hits.

The pre-existing V-1 verifier defect (expected 20 MANIFEST rows, true 18; 86/87 in v1, fixed
to 91/91 in v2, both versions retained) was independently confirmed by the reviewer as
correctly classified and is **not** counted as a new defect of this recheck.

## Unchanged

13 raw bytes and SHA-256 values, `artifact_count=13 / total_bytes=262728`, v2 91/91 MATCH,
A–F 6/6, 12 overclaim categories 0 CONFIRMED, machine gates (validator `NOT_QUALIFIED`,
guard `INCOMPLETE`), G0 and G0–G8 all pending, zero gate promotion / zero self-certification /
zero state write-back, zero forward pass / zero scientific result, governing R95, 0 qualifying
papers, no COMPLETE written, and the eighteenth checkpoint's bytes. The eighteenth checkpoint
truthfully stated at write time that the recheck was launched but not recovered and claimed no
verdict; that statement was true and its bytes are not rewritten.

Per the R117/R119/R120/R121/R122 precedent, the recovered verdict and append-only corrections
are published in a **new immutable checkpoint** instead of editing the earlier one.

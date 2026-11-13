# R117 isolated gate/evidence recheck — sanitized summary

**Not the original review.** The primary-project review has two real local
absolute paths in its section 0, so the original is **not uploaded** to this
public repository. All machine-local paths below are written as `<local>/`.
No credentials, tokens, account identifiers, private keys, datasets, model
weights, third-party source trees or unpublished manuscript content appear.

- Original: primary local project `exec-premise-R117/R117-INDEPENDENT-REVIEW.md`,
  final **22,725 B**, SHA-256
  `0d133eaca0684bc61b927378923aaf09489adb6e33b979b8c4e9be33df030a3b`,
  mtime 03:30:17, **one write, no intermediate state, original unchanged**.
- First line: `**Verdict:** PARTIAL | **G0 may be passed:** NO | **Scientific result claimed:** NO`
- Second line: `**Forward pass performed:** NO`

This is a **gate/evidence-layer recheck**, NOT a `ccf-paper-reviewer full`
manuscript review. It has no scored-review Overall line, no numeric paper
score, no scholarly-confidence field, and does not change the governing
independent full review (still 6.0).

## What the isolated sub-agent recomputed from disk bytes

| Item | Result |
|:--|:--|
| 19 sources / 6 artifacts | bytes + SHA-256 **19/19 and 6/6 MATCH** vs the source manifest |
| 8 Sintel npz | SHA-256 matches R106 declarations 8/8; zip CRC / `testzip` pass; zero array instantiation |
| Official checkpoint | `d0e42857…ccc3f`; `weights_only=True` -> `dict{network,decoder}`, 14 tensors, all finite; no network constructed |
| State-dict digest, **both framings** | R101 original rule -> `67ce06c5…a82` MATCH; R117 probe variant -> `bd3f2cc8…5e74` MATCH. Same 14 tensors / 44,552 B raw bytes; **framing difference, not a data conflict** |
| Main `pipeline-state.json` | `bcb48bb9…a33d`, 3,723 B, byte-identical to the R107 frozen value; G0 and G0–G8 / validation / handoff all `pending` |
| 7 import configs (A–G) | independently reproduced: **5 FAIL / 2 OK**, successful configs `flyvis.device = cpu`; upstream `__init__.py:13-14` has no mps branch; sandbox `version.py` contains `NOT an official FlyVis file` |
| Verbatim source lines | `device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")` and `torch.set_default_device(device)` present |

## Twelve named overclaim / self-certification categories

**(a)–(l): CONFIRMED = 0, all REFUTED.** The only honestly retained local
exception is the v1 verifier false negative under (h) (local paths merged into
the credential boolean), which the final version split out and which was never
used as a final conclusion. Categories covered: asset bytes vs environment
ready; import vs forward pass; MPS available vs MPS used / 4090-L4-H20 claims;
weights-only restore vs scientific result; zip CRC vs dataset/label read;
collection vs G0 pass; same-host script agreement vs independent cross-check;
local-path zero-hit claim / misclassifying paths as credentials; framing-different
digests vs data conflict; meta `seed: 0` vs frozen seed set; claiming a full
manuscript review or numeric score; claiming state/review/score/manuscript edits.

## State judgement

- **May G0 be passed: NO.** `NOT_GATE_PASS` classification, four readiness
  items `is_gate_pass=false`, zero forward pass, zero scientific metric.
  Byte integrity and environment readings do not constitute the substantive
  positive evidence a gate promotion requires.
- **Substantive positive new scientific evidence: NO.** All findings are
  engineering / gate-layer read-only measurements.
- **Keep G0 pending: YES.** Matches the on-disk all-pending state.
- **Verdict PARTIAL** because every core measurement was independently
  reproduced with no fabrication, boundary breach or overclaim, while six
  low / low-medium documentation and evidence-chain defects exist (below), and
  the round by design is not a G0 pass, scientific result or forward pass.

## Six defects, all accepted, append-only corrections

1. **[low-medium] R101-rule digest lacked a first-hand on-disk artifact** —
   it was a text assertion; the on-disk probe used a different framing and no
   verify check covered the R101 rule. The value itself was independently
   confirmed correct; this was a reproducibility gap, **not a data error or
   fabrication**. Closed by NEW artifacts `R117-digest-r101.py` +
   `R117-DIGEST-RECOMPUTE.json` (2,072 B / `1d724e96…`): both framings
   recomputed from disk, `both_match=true`, same 14 tensors / 44,552 B raw
   bytes. A first-hand recomputation, not a text patch.
2. **[low]** `R117-EXEC-PREMISE-EVIDENCE.md:85` said "12 source bytes";
   accurate reading is **19 sources in `SOURCE-MANIFEST.json`**, while
   `RAW.json`'s `source_manifest[]` has **12** (4 non-clip + 8 clip).
3. **[low]** `R117-ROUND-AUDIT.md:44` transcribed a VERIFICATION.json SHA as
   63 hex chars (missing one `f`); correct on-disk value is
   `aa1372d2bbf91e4bc5127d636dac00cbfc7de7942253ca714895a7fed625946a`.
   The manifest registration and EVIDENCE.md prefix `aa1372d2…` are correct.
4. **[informational]** `R117-SOURCE-MANIFEST.json` does not list the 7th
   artifact `R117-ROUND-AUDIT.md` (manifest generated 03:19, audit added
   03:22). A snapshot-timing issue, not a data conflict. The round audit
   gained an appended "snapshot boundary" note; manifest bytes unchanged.
5. **[low]** "official meta single line `seed: 0`" is imprecise: the file has
   **2** `seed: 0` lines (25, 108), and `RAW.json` lists both. Not category
   (j) overclaim since the products already say `NOT_ESTABLISHED` / zero
   calibration runs.
6. **[low, sub-agent self-reported]** The review's own section 0 quotes two
   real conda local paths, slightly inconsistent with its section 5 "we
   redacted throughout" wording. The sub-agent left the original unchanged
   (one-write rule) and disclosed it. Accurate scope: section 5 covers the
   **8 primary-project artifacts**, not the review itself; the review has 2
   additional local paths. => **original review not uploaded**, only this
   sanitized summary; local-path count 25 -> 27, **credential hits still 0**.

None of the six changes the core judgement: byte integrity holds, no scientific
result, no G0 promotion, no forward pass. None involves fabrication or a data
inconsistency.

## Content safety

14 strict credential patterns: **0 hits**. Local absolute paths are configuration
facts inside the primary project, counted separately (25 in the 8 artifacts,
27 including the review's own section 0), and must be redacted to `<local>/` in
every public copy (R109). The 17 / 19 / 23 / 25 readings differ because the
scanned file set changed over time and the pattern counts differed — explicitly
**not** fabrication or contradiction.

## Concurrency condition and published checkpoints

During the review window the main session concurrently appended the primary
ledger (03:22:47), STATUS / work log (03:23:08), round audit section 4 (03:27),
and completed the seventh checkpoint sync (remote `1caf00c6…`). The sub-agent
recorded verbatim that it scanned the 03:22 8,082 B audit and did not rely on
any concurrent main-session write. Under R106 §6 R9 a main-session
self-correction is not a self-certification of gap closure.

The seventh checkpoint was written and pushed **before** this recheck was
recovered and states truthfully at its write time that the recheck was launched
but not yet recovered and that no conclusion was claimed. All **7 published
checkpoints stay byte-for-byte untouched**; this eighth, immutable checkpoint
carries the recovered conclusion and the append-only corrections.

## Result and boundary (unchanged)

G0 stays `pending`, gap 1 overall PARTIAL, zero gate promotions, zero
self-certification, zero state write-back. Step-3 precondition (substantive
positive new scientific evidence) not met => no new manuscript copy, no
9-page compile, no fresh isolated full manuscript review.
**0 qualifying papers, no COMPLETE written**, governing still
**R95 = 6.0 / Confidence 4.0**, `NOT_QUALIFIED` / `INCOMPLETE`. Stop gates
remain (1) achieve >= 7.0, (2) user stops.

**Checkpoint status `completed` is a collaboration work state, not a scientific
conclusion.**

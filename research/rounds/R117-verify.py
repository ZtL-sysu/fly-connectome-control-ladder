#!/usr/bin/env python
"""R117 second-script verification: recompute from disk bytes.

IMPORTANT (R115 W4 / R114 D1 lessons): this script shares the same host and
the same hashlib with R117-probe.py. Agreement between the two products is a
NECESSARY consistency check, NOT an independent cross-validation. The genuine
independent recomputation is delegated to a fresh isolated sub-agent.

Run with: /Users/xhf/miniconda3/bin/python R117-verify.py
"""
from __future__ import annotations

import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


raw = json.loads((HERE / "R117-EXEC-PREMISE-RAW.json").read_text(encoding="utf-8"))
checks = []


def check(cid, desc, ok, detail=""):
    checks.append({"id": cid, "description": desc, "result": "MATCH" if ok else "MISMATCH",
                   "detail": str(detail)[:300]})


# 1. source manifest recomputed from disk
for s in raw["source_manifest"]:
    p = RUN / s["path"]
    if not p.exists():
        check("SRC-" + s["label"], s["path"], False, "missing")
        continue
    b, h = p.stat().st_size, sha256(p)
    check("SRC-" + s["label"], s["path"], (b == s["bytes"] and h == s["sha256"]),
          f"bytes={b} sha={h[:16]}")

# 2. clip SHA vs R106 independently declared values
r106 = json.loads((RUN / "gate-G0-R106/R106-ASSET-SHA-VERIFICATION.json").read_text(encoding="utf-8"))
decl = {c["file"]: c["declared_sha256"] for c in r106["sintel_clips"]}
for c in raw["sintel_clips"]:
    expected = decl.get(c["file"])
    check("CLIP-" + c["file"], "R106 declared SHA", expected == c["sha256"],
          f"declared={str(expected)[:16]} measured={c['sha256'][:16]}")
    check("CRC-" + c["file"], "zip central-directory CRC", c.get("zip_testzip_crc_ok") is True)

# 3. checkpoint vs official/R101 values (read from disk, not from raw)
CHKPT = RUN / "sources/flyvis-pretrained-access/unpacked/results/flow/0000/000/chkpts/chkpt_00000"
check("CHKPT-sha", "official chkpt_00000 SHA vs R101", sha256(CHKPT) ==
      "d0e42857e738d0315897c2d50fde9eb3fb1a3fb1f071d55dfc13d53d72bccc3f")
restore = raw["official_checkpoint"]["weights_only_restore"]
check("CHKPT-restored", "weights_only restore dict{network,decoder}/14 tensors",
      restore.get("top_level_type") == "dict" and
      restore.get("top_level_keys") == ["decoder", "network"] and
      restore.get("tensor_count") == 14, str(restore.get("tensor_count")))
check("CHKPT-finite", "all restored tensors finite", restore.get("all_finite") is True)

# 4. verbatim source-field checks
init_lines = (RUN / "local-provisioning/flyvis-work/flyvis/__init__.py").read_text(encoding="utf-8", errors="replace").splitlines()
dev_line = 'device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")'
check("VERBATIM-device", "FlyVis upstream device line", dev_line in init_lines)
check("VERBATIM-setdefault", "torch.set_default_device(device)", "torch.set_default_device(device)" in init_lines)
ver = (RUN / "local-provisioning/flyvis-work/flyvis/version.py").read_text(encoding="utf-8", errors="replace")
check("VERBATIM-reconstructed", "version.py explicitly NON-official reconstruction",
      "NOT an official FlyVis file" in ver and "__version__ = '1.2.0'" in ver)

# 5. import matrix structural assertions
im = raw["import_matrix"]
check("IMPORT-count", "7 configurations measured", len(im) == 7)
fails = [k for k, v in im.items() if v.get("import_flyvis") == "FAIL"]
oks = [k for k, v in im.items() if v.get("import_flyvis") == "OK"]
check("IMPORT-5fail", "5 non-sandbox configs FAIL", len(fails) == 5, str(fails))
check("IMPORT-2ok", "2 sandbox configs OK", len(oks) == 2, str(oks))
check("IMPORT-device-cpu", "both OK configs resolve flyvis.device=cpu",
      all(im[k].get("flyvis_device") == "cpu" for k in oks))
check("IMPORT-mps-available", "MPS available in all configs",
      all(v.get("mps_available") is True for v in im.values()))
check("IMPORT-cuda-absent", "CUDA unavailable in all configs",
      all(v.get("cuda_available") is False for v in im.values()))

# 6. strict boundary flags
sb = raw["strict_boundary"]
check("BOUNDARY-all-zero", "all 9 scientific-execution flags false",
      all(sb[k] is False for k in ("forward_pass", "inference", "training", "label_read",
                                   "epe_or_l2_computation", "scientific_metric", "gate_promotion",
                                   "pipeline_state_json_written", "npz_arrays_instantiated")))

# 7. frozen-contract readiness: no self-certification
rd = raw["frozen_contract_readiness"]
check("READINESS-no-gate-pass", "no readiness item claims a gate pass",
      all(v.get("is_gate_pass") is False for v in rd.values()))

# 8. Content scan. Two categories are deliberately SEPARATED (R115 W2 lesson):
#    (a) credentials/tokens/accounts/private keys -> MUST be zero hits anywhere.
#    (b) machine-local absolute paths -> a configuration fact inside the main
#        project's own artifacts, but MUST be redacted to '<local>/' in every
#        copy that goes to the public GitHub sync repo (R109 red line).
#    Merging (a) and (b) into one boolean produced a false MISMATCH on the
#    first run; that v1 reading is preserved, not silently overwritten.
CREDENTIAL_PATTERNS = [
    r"AIza[0-9A-Za-z_\-]{20,}", r"sk-[0-9A-Za-z]{20,}", r"ghp_[0-9A-Za-z]{20,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"api[_-]?key\s*[:=]\s*['\"][^'\"]{12,}",
    r"Bearer\s+[A-Za-z0-9_\-\.]{20,}", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    r"password\s*[:=]\s*['\"][^'\"]{8,}", r"client_secret\s*[:=]\s*['\"][^'\"]{8,}",
]
LOCAL_PATH_PATTERN = r"/Users/[A-Za-z0-9_.\-]+/"
cred_hits, local_hits = [], []
for p in sorted(HERE.rglob("*")):
    if p.is_file():
        try:
            t = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for pat in CREDENTIAL_PATTERNS:
            for m in re.finditer(pat, t):
                cred_hits.append({"file": p.name, "pattern": pat, "match_len": len(m.group(0))})
        for m in re.finditer(LOCAL_PATH_PATTERN, t):
            local_hits.append({"file": p.name, "match": m.group(0)})
check("SECRET-free", "9 credential/token/account/key patterns: 0 hits", len(cred_hits) == 0, str(cred_hits[:5]))
check("LOCALPATH-registered", "local absolute paths registered, NOT claimed zero",
      len(local_hits) > 0,
      f"{len(local_hits)} hits, all '/Users/<user>/' interpreter/config paths; public sync copies must use '<local>/' (R109).")
hits = cred_hits

# 9. main pipeline-state bytes unchanged vs R107 frozen value
ps = RUN / "pipeline-state.json"
ps_sha = sha256(ps)
check("STATE-unchanged", "pipeline-state.json SHA vs R107 frozen",
      ps_sha == "bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d",
      ps_sha)

out = {
    "round": "R117",
    "classification": "SECOND_SCRIPT_CONSISTENCY_CHECK_NOT_INDEPENDENT_CROSS_VALIDATION",
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "generated_utc_note": "Product-generation wall clock; NOT an acquisition timestamp (R115 W3).",
    "python": "/Users/xhf/miniconda3/bin/python",
    "independence_note": "Shares host + hashlib with R117-probe.py; agreement is necessary consistency, not independent verification. Fresh isolated sub-agent performs the genuine recomputation.",
    "checks": checks,
    "total": len(checks),
    "matches": sum(1 for c in checks if c["result"] == "MATCH"),
    "mismatches": [c for c in checks if c["result"] != "MATCH"],
    "credential_hits": cred_hits,
    "local_absolute_path_hits": len(local_hits),
    "local_path_disposition": "Main-project internal artifacts only. Every public GitHub sync copy redacts them to '<local>/' before staging (R109). Zero local paths are claimed absent.",
    "v1_false_mismatch_note": "First verify run merged credential and local-path patterns into one boolean and reported SECRET-free=MISMATCH with 17 hits; all 17 were '/Users/<user>/' paths and zero were credentials. Category split applied in this final version; both readings are registered, the v1 product is preserved as .v1-superseded.json (R116 v1/v2 precedent).",
    "pipeline_state_sha256": ps_sha,
    "pipeline_state_bytes": ps.stat().st_size,
}
dest = HERE / "R117-EXEC-PREMISE-VERIFICATION.json"
dest.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({"output": str(dest.relative_to(RUN)), "bytes": dest.stat().st_size,
                  "sha256": sha256(dest), "total": out["total"], "matches": out["matches"],
                  "mismatches": out["mismatches"], "credential_hits": len(cred_hits),
                  "local_path_hits": len(local_hits)}, indent=2, ensure_ascii=False))

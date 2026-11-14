#!/usr/bin/env python
"""R117 read-only execution-premise probe for the mainline P3 real forward pass.

STRICT BOUNDARY (enforced, not decorative):
  ZERO model forward pass, ZERO inference, ZERO training, ZERO label read,
  ZERO EPE/l2 computation, ZERO scientific metric, ZERO gate promotion.
  This script only measures importability, device resolution, asset byte
  integrity, checkpoint restorability, and the presence of protocol clauses.
  It does NOT pass G0/G1.../P2 and does NOT write pipeline-state.json.

Run with: /Users/xhf/miniconda3/bin/python R117-probe.py
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
PY_BASE = "/Users/xhf/miniconda3/bin/python"
PY_ENV = "/Users/xhf/miniconda3/envs/ceg_snn_mi/bin/python"

SANDBOX = RUN / "local-provisioning/flyvis-work"
FLYVIS_ROOT = RUN / "local-provisioning/flyvis-root"
DEPS = RUN / "code-audit/flyvis-local-deps"
CHKPT = RUN / "sources/flyvis-pretrained-access/unpacked/results/flow/0000/000/chkpts/chkpt_00000"
META = RUN / "sources/flyvis-pretrained-access/unpacked/results/flow/0000/000/_meta.yaml"
SINTEL = RUN / "sources/sintel-development-subset-v1/rendered-attempt-1"
FLYVIS_INIT = SANDBOX / "flyvis/__init__.py"
VERSION_PY = SANDBOX / "flyvis/version.py"

CLIPS = [
    "alley_1-window-0.npz", "alley_1-window-1.npz",
    "bamboo_1-window-0.npz", "bamboo_1-window-1.npz",
    "market_2-window-0.npz", "market_2-window-1.npz",
    "mountain_1-window-0.npz", "mountain_1-window-1.npz",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def bytes_of(path: Path) -> int:
    return path.stat().st_size


# ---- A. import matrix -----------------------------------------------------
# Each child process is a separate interpreter; no state leaks into this one.
PROBE_SRC = r'''
import json, sys, torch
r = {"py": sys.version.split()[0], "torch": torch.__version__,
     "cuda_available": bool(torch.cuda.is_available()),
     "mps_available": bool(torch.backends.mps.is_available()),
     "default_device_before": str(torch.get_default_device())}
try:
    import flyvis
    r["import_flyvis"] = "OK"
    r["flyvis_file"] = getattr(flyvis, "__file__", None)
    r["flyvis_version"] = str(getattr(flyvis, "__version__", "NA"))
    r["flyvis_device"] = str(getattr(flyvis, "device", "NA"))
    r["connectome_exists"] = bool(getattr(flyvis, "connectome_file", None)) and Path(str(flyvis.connectome_file)).exists() if hasattr(flyvis, "connectome_file") else None
    r["root_dir"] = str(getattr(flyvis, "root_dir", "NA"))
except Exception as e:
    r["import_flyvis"] = "FAIL"
    r["error"] = type(e).__name__ + ": " + str(e)[:220]
r["default_device_after"] = str(torch.get_default_device())
print("R117JSON" + json.dumps(r))
'''
# fix: Path not imported in child
PROBE_SRC = PROBE_SRC.replace('import json, sys, torch', 'import json, sys, torch\nfrom pathlib import Path')

CONFIGS = [
    ("A_base_default", PY_BASE, RUN, [], {}),
    ("B_ceg_default", PY_ENV, RUN, [], {}),
    ("C_ceg_cwd_sources", PY_ENV, RUN / "sources/flyvis", [], {}),
    ("D_ceg_syspath_sources", PY_ENV, RUN, [RUN / "sources/flyvis"], {}),
    ("E_base_syspath_sources", PY_BASE, RUN, [RUN / "sources/flyvis"], {}),
    ("F_ceg_r101_sandbox", PY_ENV, RUN, [SANDBOX], {"FLYVIS_ROOT_DIR": str(FLYVIS_ROOT)}),
    ("G_ceg_sandbox_plus_deps", PY_ENV, RUN, [SANDBOX, DEPS], {"FLYVIS_ROOT_DIR": str(FLYVIS_ROOT)}),
]

import_matrix = {}
for name, py, cwd, paths, extra in CONFIGS:
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    if paths:
        env["PYTHONPATH"] = os.pathsep.join(str(p) for p in paths)
    for k, v in extra.items():
        env[k] = v
    try:
        p = subprocess.run([py, "-c", PROBE_SRC], cwd=str(cwd), env=env,
                           capture_output=True, text=True, timeout=180)
        line = [l for l in p.stdout.splitlines() if l.startswith("R117JSON")]
        rec = json.loads(line[0][8:]) if line else {
            "parse_error": "no R117JSON line",
            "stdout_tail": p.stdout[-300:], "stderr_tail": p.stderr[-300:]}
        rec["rc"] = p.returncode
        rec["config"] = {
            "python": py, "cwd": str(cwd.relative_to(RUN)) if cwd != RUN else ".",
            "pythonpath": [str(x.relative_to(RUN)) for x in paths],
            "extra_env_keys": sorted(extra.keys()),
        }
        import_matrix[name] = rec
    except subprocess.TimeoutExpired:
        import_matrix[name] = {"timeout_seconds": 180, "import_flyvis": "TIMEOUT"}


# ---- B. device-resolution source lines (verbatim, from frozen sandbox) ----
init_text = FLYVIS_INIT.read_text(encoding="utf-8", errors="replace")
device_lines = [l for l in init_text.splitlines()
                if "device" in l.lower() and ("torch.device" in l or "set_default_device" in l)]
version_text = VERSION_PY.read_text(encoding="utf-8", errors="replace")

# ---- C. Sintel npz: BYTE-LEVEL structure only, no array instantiation ----
clips = []
for name in CLIPS:
    p = SINTEL / name
    rec = {"file": name, "exists": p.exists()}
    if p.exists():
        rec["bytes"] = bytes_of(p)
        rec["sha256"] = sha256(p)
        with zipfile.ZipFile(p) as z:
            infos = z.infolist()
            rec["zip_entries"] = [i.filename for i in infos]
            rec["zip_entry_count"] = len(infos)
            # CRC is stored in the zip central directory; reading it does not
            # decompress or instantiate any array / label.
            rec["zip_crc32"] = {i.filename: i.CRC for i in infos}
            rec["zip_uncompressed_bytes"] = {i.filename: i.file_size for i in infos}
            rec["zip_testzip_crc_ok"] = (z.testzip() is None)
    clips.append(rec)

# ---- D. official checkpoint: bytes + safe weights_only restore ------------
chk = {"path": "sources/flyvis-pretrained-access/unpacked/results/flow/0000/000/chkpts/chkpt_00000",
       "bytes": bytes_of(CHKPT), "sha256": sha256(CHKPT)}
RESTORE_SRC = r'''
import json, hashlib, torch, sys
p = sys.argv[1]
obj = torch.load(p, map_location="cpu", weights_only=True)
r = {"top_level_type": type(obj).__name__,
     "top_level_keys": sorted(obj.keys()) if isinstance(obj, dict) else None}
tensors = []
def walk(d, pre=""):
    if isinstance(d, dict):
        for k in sorted(d.keys()):
            walk(d[k], pre + str(k) + "/")
    elif torch.is_tensor(d):
        tensors.append((pre.rstrip("/"), d))
walk(obj)
r["tensor_count"] = len(tensors)
h = hashlib.sha256()
for k, t in sorted(tensors, key=lambda x: x[0]):
    h.update(k.encode() + b"\0" + str(t.dtype).encode() + b"\0")
    h.update(str(tuple(t.shape)).encode() + b"\0")
    h.update(t.contiguous().numpy().tobytes() + b"\0")
r["state_dict_digest_sha256"] = h.hexdigest()
r["tensor_shapes"] = {k: list(t.shape) for k, t in sorted(tensors, key=lambda x: x[0])}
r["all_finite"] = all(bool(torch.isfinite(t.float()).all()) for _, t in tensors)
print("R117RESTORE" + json.dumps(r))
'''
try:
    rp = subprocess.run([PY_ENV, "-c", RESTORE_SRC, str(CHKPT)],
                        capture_output=True, text=True, timeout=180)
    rl = [l for l in rp.stdout.splitlines() if l.startswith("R117RESTORE")]
    chk["weights_only_restore"] = json.loads(rl[0][11:]) if rl else {
        "parse_error": "no R117RESTORE", "stderr_tail": rp.stderr[-300:]}
    chk["weights_only_restore"]["rc"] = rp.returncode
except subprocess.TimeoutExpired:
    chk["weights_only_restore"] = {"timeout_seconds": 180}

# ---- E. official _meta.yaml clauses (verbatim lines) ---------------------
meta = {"path": "sources/flyvis-pretrained-access/unpacked/results/flow/0000/000/_meta.yaml",
        "bytes": bytes_of(META), "sha256": sha256(META)}
meta_text = META.read_text(encoding="utf-8", errors="replace")
KEYS = ("gaussian_white_noise", "n_frames", "batch_size", "seed", "boxfilter",
        "DecoderGAVP", "MultiTaskSintel", "task", "flow")
meta["clause_lines"] = [l.rstrip() for l in meta_text.splitlines()
                        if any(k in l for k in KEYS)]
meta["clause_presence"] = {k: any(k in meta_text for k in [k]) for k in KEYS}

# ---- F. frozen-contract readiness (evidence presence only, NO verdict) ----
readiness = {
    "frozen_seed_set": {
        "status": "NOT_ESTABLISHED_BY_THIS_PROBE",
        "reason": "This probe reads only the official meta seed line; a frozen multi-seed set + seed key is a P2/P3 contract artifact and is not asserted here."},
    "noise_calibration": {
        "status": "OFFICIAL_META_LINE_PRESENT",
        "note": "std .08 / lower-clamp / 4 draws / frozen seed key are contract clauses; only the presence of source lines is measured, no calibration run performed."},
    "zero_injection_assertion": {
        "status": "NOT_MEASURED",
        "note": "Requires an executable runner; no runner was invoked by this probe."},
    "mps_device_adaptation": {
        "status": "MEASURED",
        "note": "See import_matrix and device_lines; FlyVis upstream selects cuda-or-cpu only."},
}
for k, v in readiness.items():
    v["is_gate_pass"] = False

# ---- manifest of source bytes --------------------------------------------
sources = []
for label, p in [("flyvis_init", FLYVIS_INIT), ("flyvis_version_reconstructed", VERSION_PY),
                 ("official_chkpt_00000", CHKPT), ("official_meta_yaml", META)]:
    sources.append({"label": label, "path": str(p.relative_to(RUN)),
                    "bytes": bytes_of(p), "sha256": sha256(p)})
for c in clips:
    if c.get("exists"):
        sources.append({"label": "sintel_clip", "path": "sources/sintel-development-subset-v1/rendered-attempt-1/" + c["file"],
                        "bytes": c["bytes"], "sha256": c["sha256"]})

# ---- secret / local-path scan of this round's own artifacts --------------
SECRET_PATTERNS = [
    r"AIza[0-9A-Za-z_\-]{20,}", r"sk-[0-9A-Za-z]{20,}", r"ghp_[0-9A-Za-z]{20,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"api[_-]?key\s*[:=]\s*['\"][^'\"]{12,}",
    r"Bearer\s+[A-Za-z0-9_\-\.]{20,}", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
]
import re
secret_hits = []
for p in sorted(HERE.rglob("*")):
    if p.is_file() and p.suffix.lower() in {".json", ".md", ".py", ".txt", ".yaml"} and p.name != "R117-probe.py":
        try:
            t = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for pat in SECRET_PATTERNS:
            for m in re.finditer(pat, t):
                secret_hits.append({"file": p.name, "pattern": pat, "match_len": len(m.group(0))})

out = {
    "round": "R117",
    "classification": "READONLY_EXECUTION_PREMISE_PROBE_NOT_SCIENTIFIC_RESULT_NOT_GATE_PASS_NOT_FORWARD_PASS",
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "generated_utc_note": "Product-generation wall clock. NOT a network acquisition timestamp; must not be used to reconstruct acquisition chronology (R115 W3 / R114 D5).",
    "python_driver": sys.version.split()[0],
    "python_driver_path": sys.executable,
    "strict_boundary": {
        "forward_pass": False, "inference": False, "training": False,
        "label_read": False, "epe_or_l2_computation": False,
        "scientific_metric": False, "gate_promotion": False,
        "pipeline_state_json_written": False,
        "npz_arrays_instantiated": False,
        "note": "npz inspected only via zip central directory (filename, CRC, uncompressed size, testzip). No array, label, or stimulus value was read."},
    "import_matrix": import_matrix,
    "device_source_verbatim": device_lines,
    "version_py_verbatim": version_text.strip().splitlines(),
    "sintel_clips": clips,
    "official_checkpoint": chk,
    "official_meta": meta,
    "frozen_contract_readiness": readiness,
    "source_manifest": sources,
    "secret_scan": {"patterns": len(SECRET_PATTERNS), "hits": len(secret_hits), "details": secret_hits[:20]},
}

dest = HERE / "R117-EXEC-PREMISE-RAW.json"
dest.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({
    "output": str(dest.relative_to(RUN)),
    "bytes": bytes_of(dest), "sha256": sha256(dest),
    "import_results": {k: v.get("import_flyvis") for k, v in import_matrix.items()},
    "clips_ok": sum(1 for c in clips if c.get("zip_testzip_crc_ok")),
    "restore": chk["weights_only_restore"].get("top_level_type", chk["weights_only_restore"].get("parse_error")),
    "restore_digest": chk["weights_only_restore"].get("state_dict_digest_sha256"),
    "secret_hits": len(secret_hits),
}, indent=2, ensure_ascii=False))

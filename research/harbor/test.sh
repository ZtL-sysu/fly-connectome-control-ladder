#!/usr/bin/env bash
# R108 verifier. Recomputes the probe arithmetic from raw values and checks
# artifact hashes. Empty-environment run must take the apparatus exit.
set -u
LOG_DIR="${HARBOR_VERIFIER_LOG_DIR:-$PWD/logs/verifier}"
mkdir -p "$LOG_DIR"
REWARD="$LOG_DIR/reward.json"
ERR="$LOG_DIR/verifier_error.json"

apparatus() {
  python3 - "$1" "$ERR" <<'PY'
import json, sys
from pathlib import Path
Path(sys.argv[2]).write_text(json.dumps({"apparatus_fault": sys.argv[1]}, indent=2) + "\n")
PY
  exit 1
}

trap 'apparatus "verifier exited without writing a score"' EXIT

RESULT="results/r108_probe/result.json"
MANIFEST="results/r108_probe/manifest.json"
[ -f "$RESULT" ] || apparatus "missing $RESULT"
[ -f "$MANIFEST" ] || apparatus "missing $MANIFEST"

python3 - "$RESULT" "$MANIFEST" "$LOG_DIR" <<'PY'
import hashlib, json, math, sys
from pathlib import Path
res_p, man_p, log_dir = map(Path, sys.argv[1:4])
res = json.loads(res_p.read_text())
man = json.loads(man_p.read_text())
err = log_dir / "verifier_error.json"

def fault(msg):
    err.write_text(json.dumps({"apparatus_fault": msg}, indent=2) + "\n")
    raise SystemExit(1)

if res.get("status") != "success":
    fault("probe did not succeed: " + str(res.get("status")) + " " + str(res.get("error", "")))
if res.get("scientific_result") is not False or res.get("training") is not False:
    fault("probe violated engineering-only boundary")
if res.get("probe_script_sha256") != hashlib.sha256(Path("tests/probe.py").read_bytes()).hexdigest():
    fault("probe script SHA changed")
# Independent recomputation from raw values, never trusting the reported scalar.
m = res.get("probe_matrix_flat")
if not isinstance(m, list) or len(m) != 16:
    fault("probe matrix missing or wrong length")
recomputed = sum(m)
if not all(math.isfinite(float(v)) for v in m):
    fault("non-finite probe values")
if abs(recomputed - float(res["probe_expected"])) > 1e-9:
    fault("expected value inconsistent with raw matrix")
if abs(float(res["probe_observed"]) - recomputed) > 1e-9:
    fault("observed value inconsistent with raw matrix")
if res.get("all_finite") is not True or res.get("probe_ok") is not True:
    fault("probe self-check flags inconsistent")
# Manifest hash verification.
for name, digest in man.get("files", {}).items():
    p = res_p.parent / name
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
        fault("manifest hash mismatch: " + name)
for req in ("result.json", "manifest.json"):
    p = res_p.parent / req
    if not p.is_file():
        fault("required artifact missing: " + req)
(log_dir / "reward.json").write_text(json.dumps({
    "reward": 1.0,
    "status": "verified",
    "metric": "environment_verification",
    "probe_device": res.get("probe_device"),
    "scope": "ENGINEERING_ONLY_NO_SCIENTIFIC_RESULT",
}, indent=2) + "\n")
PY
RC=$?
if [ "$RC" -ne 0 ]; then
  trap - EXIT
  exit 1
fi
trap - EXIT
echo "R108 verifier: PASS (engineering environment probe only)"
exit 0

#!/usr/bin/env python3
"""Build R124-SOURCE-MANIFEST.json from raw/ bytes. Run with the local conda python.

No network access. Reads raw/ files verbatim and records SHA-256 + byte counts.
Acquisition map is imported only for URL/status metadata (declarative), never as
a data source for verification.
"""
import hashlib
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
# V-1 defect (preserved): a plain `from R124_ACQUIRE import ...` failed because
# the module filename contains hyphens. Load by explicit file path instead.
_spec = importlib.util.spec_from_file_location(
    "r124_acquire", os.path.join(HERE, "R124-ACQUIRE.py"))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
ACQUISITION, SCOPE_NOTE = _mod.ACQUISITION, _mod.SCOPE_NOTE

rows = []
for name, method, url, status, declared_bytes, note in ACQUISITION:
    path = os.path.join(RAW, name)
    if not os.path.isfile(path):
        print("MISSING", name)
        sys.exit(1)
    b = open(path, "rb").read()
    rows.append({
        "file": name,
        "method": method,
        "url": url,
        "observed_http_status": status,
        "bytes": len(b),
        "declared_bytes_at_acquisition": declared_bytes,
        "bytes_match_declaration": len(b) == declared_bytes,
        "sha256": hashlib.sha256(b).hexdigest(),
        "note": note,
    })

manifest = {
    "round": "R124",
    "kind": "READONLY_FIRST_HAND_TEXT_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
    "scope_note": SCOPE_NOTE,
    "raw_dir": "raw/",
    "files": rows,
    "totals": {
        "file_count": len(rows),
        "bytes_total": sum(r["bytes"] for r in rows),
        "http_200_count": sum(1 for r in rows if r["observed_http_status"] == 200),
        "http_301_count": sum(1 for r in rows if r["observed_http_status"] == 301),
        "http_429_count": sum(1 for r in rows if r["observed_http_status"] == 429),
    },
}
out = os.path.join(HERE, "R124-SOURCE-MANIFEST.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("WROTE", out)
print("files", manifest["totals"]["file_count"], "bytes", manifest["totals"]["bytes_total"])
print("200/301/429", manifest["totals"]["http_200_count"],
      manifest["totals"]["http_301_count"], manifest["totals"]["http_429_count"])
for r in rows:
    print(" ", r["file"], r["bytes"], r["sha256"][:16], r["observed_http_status"])

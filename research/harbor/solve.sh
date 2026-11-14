#!/usr/bin/env bash
# R108 reference solution: run the frozen probe, then let the verifier score it.
# This script must NOT touch logs/verifier or reward.json.
set -eu
cd "$(dirname "$0")/.."
python3 tests/probe.py
bash tests/test.sh

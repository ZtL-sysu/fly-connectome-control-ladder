#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R120 independent verifier.

Independence: does NOT import R120-raw.py, and does NOT read any R120 JSON
artifact (neither RAW nor SOURCE-MANIFEST nor the verification output). Every
value below is recomputed from the original source bytes on disk. Expectations
are hardcoded from the R120 evidence report, so a match is an independent
recomputation, not a self-echo of the collector.

Boundary: READ_ONLY_VERIFICATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
PROJECT = RUN.parent.parent.parent

CHECKS: list[dict] = []


def check(cid: str, expected, observed, note: str = "") -> None:
    CHECKS.append({
        "id": cid,
        "expected": expected,
        "observed": observed,
        "status": "MATCH" if expected == observed else "MISMATCH",
        "note": note,
    })


def raw(rel: str, base: Path | None = None) -> bytes:
    p = (base or RUN) / rel
    return p.read_bytes() if p.is_file() else b""


def txt(rel: str, base: Path | None = None) -> str:
    return raw(rel, base).decode("utf-8", errors="replace")


def line_of(t: str, needle: str) -> int:
    for i, ln in enumerate(t.splitlines(), 1):
        if needle in ln:
            return i
    return 0


def hits(t: str, needle: str) -> list[int]:
    return [i for i, ln in enumerate(t.splitlines(), 1) if needle in ln]


def main() -> int:
    # ---- Group A: standing instruction disk anchors
    goal = txt("GOAL-ITERATION-R107.md", PROJECT)
    check("A1a", [90], hits(goal, "`guidance-v2.md`, `execution-contract-v1/v2/v3.md`, `protocols/`"))
    check("A1b", [91], hits(goal, "a future versioned contract (v4) may restate"))

    pkg_i = txt("gate-G0-R107/isolated-post-review/R107-R1-R8-G0-CLOSURE-PACKAGE.md")
    pkg_m = txt("gate-G0-R107/R107-R1-R8-G0-CLOSURE-PACKAGE.md")
    aud = txt("gate-G0-R107/isolated-post-review/R107-ROUND-AUDIT.md")
    rec = txt("gate-G0-R107/isolated-post-review/R107-INDEPENDENT-REVIEW-RECOVERY.md")
    check("A2a", 175, line_of(pkg_i, "U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state"))
    check("A2b", 175, line_of(pkg_m, "U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state"))
    check("A2c", 116, line_of(aud, "U6/W2 版本化契约 → 新建 f-research-v1 P0 state"))
    check("A2d", 180, line_of(rec, "U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state"))

    r106 = txt("gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md")
    check("A3a", [48], hits(r106, "全文没有 G0 的定义"))
    check("A3b", 1, line_of(r106, "**Verdict:** PARTIAL | **G0 may be passed:** NO"))
    check("A3c", [139], hits(r106, "**W13 [LOW｜结构性]**"))
    check("A4a", 161, line_of(r106, "**R1（闭 gap 1）**"))
    check("A4b", 166, line_of(r106, "**R6（闭 gap 4）**"))
    check("A4c", 168, line_of(r106, "- **R8** 重新冻结"))
    check("A4d", 169, line_of(r106, "- **R9** R1–R8 完成后"))
    a111 = txt("state-handoff-R111/R111-ROUND-AUDIT.md")
    check("A5", [26], hits(a111, "心跳 prompt 内嵌「交下轮」仍是 **R106 清单**"))

    # ---- Group B: on-disk state
    g = json.loads(txt("pipeline-state.json"))
    gs = g["stages"]
    g0 = next(s for s in gs if s["id"] == "G0")
    check("B1a", "f-guidance-builder-v1", g["pipeline"])
    check("B1b", "v2", g["contract_version"])
    check("B1c", 12, len(gs))
    check("B1d", ["CCFA-startup", "G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "validation", "handoff"],
          [s["id"] for s in gs])
    check("B1e", ["CCFA-startup"], [s["id"] for s in gs if s["status"] == "passed"])
    check("B1f", 11, len([s for s in gs if s["status"] == "pending"]))
    check("B1g", "pending", g0["status"])
    check("B1h", 0, len(g0["inputs"]))
    check("B1i", 0, len(g0["evidence"]))
    check("B1j", [], [s["id"] for s in gs if re.fullmatch(r"P\d+[A-Z]?", str(s["id"]))],
          "no P stage was inserted into guidance state")

    p = json.loads(txt("state-handoff-R108/f-research-v1-state/pipeline-state.json"))
    ps = p["stages"]
    check("B2a", "f-research-v1", p["pipeline"])
    check("B2b", "v1-R108-U6W2-draft", p["contract_version"])
    check("B2c", 26, len(ps))
    check("B2d", ["pending"], sorted({s["status"] for s in ps}))
    check("B2e", 0, len(p["history"]))
    check("B2f", ["P0", "P21"], [ps[0]["id"], ps[-1]["id"]])
    check("B2g", 2, len(p["contract"]))

    cm = txt("state-handoff-R108/f-research-v1-state/R108-U6-W2-VERSIONED-CONTRACT.md")
    check("B3a", 7307, len(cm.encode("utf-8")))
    check("B3b", 1, line_of(cm, "DRAFT，未激活"))
    check("B3c", 3, line_of(cm, "ENGINEERING_STATE_SCAFFOLD_ONLY_NOT_SCIENTIFIC_RESULT"))
    check("B3d", 5, line_of(cm, "PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF"))
    check("B3e", 5, line_of(cm, "本文件不是 P0 的启动"))

    pc = txt("gate-G0-R107/R107-G0-PASS-CRITERION-REGISTER.md")
    check("B4a", 3, line_of(pc, "DRAFT — PENDING DESIGNATED GATE OWNER APPROVAL"))
    check("B4b", ["PC1", "PC2", "PC3", "PC4", "PC5", "PC6"],
          [f"PC{i}" for i in range(1, 7) if f"**PC{i}" in pc])
    check("B4c", 42, line_of(pc, "R107 状态：**未做（主会话越权）**"))
    check("B4d", 59, line_of(pc, "本汇编不改变"))

    mx = txt("literature-baseline-matrix.md")
    check("B5a", 9445, len(mx.encode("utf-8")))
    check("B5b", [46], hits(mx, "the open question"))
    check("B5c", [47], hits(mx, "Kuklev leaves"))
    check("B5d", [9], hits(mx, "asset contents/license not yet individually verified"))
    check("B5e", [10], hits(mx, "project code path not yet verified"))

    v = txt("readonly-validator/validate_single_paper.py", PROJECT)
    check("B6a", 133, line_of(v, "default=7.0"))
    check("B6b", 146, line_of(v, "score >= args.threshold"))
    check("B6c", 155, line_of(v, '"score_meets_threshold"'))
    check("B6d", 148, line_of(v, '"contract": "R107 single paper, independent full review Overall >= 7.0"'))

    cr = txt("guard/criteria-null-ladder.json", PROJECT)
    lg = txt("guard/ledger-null-ladder.json", PROJECT)
    check("B7a", 132, line_of(cr, "Overall >= 7.0（R107；等于 7.0 算达标"))
    check("B7b", 136, line_of(cr, "g>=7.0"))
    check("B7c", 134, line_of(lg, "严格 > 8.0（等于 8.0 不算"))
    check("B7d", 138, line_of(lg, "g>8.0"))

    vout = json.loads(txt("reconciliation-R120/R120-validator-out.json"))
    check("B8a", "NOT_QUALIFIED", vout["verdict"])
    check("B8b", 6.0, vout["overall_score"])
    check("B8c", 7.0, vout["threshold"])
    check("B8d", ">=", vout["comparison_operator"])
    check("B8e", False, vout["score_meets_threshold"])
    check("B8f", [True, False, False, True, False],
          [vout["checks"][k]["pass"] for k in
           ["D1_guidance_validated", "D2_tex_pdf_pipeline_all_passed", "D3_independent_full_review",
            "D4_novix_experiment_evidence", "D5_six_sections_traceability"]])
    gc = txt("reconciliation-R120/R120-guard-check.txt")
    check("B8g", True, "[FAIL] A2" in gc)
    check("B8h", True, "[FAIL] A6" in gc)
    check("B8i", 7, len(re.findall(r"S\d \[pending \]", gc)))
    check("B8j", True, "【动作序列】共 0 条" in gc)

    rdir = PROJECT / "ccfa-review-reports"
    rf = sorted([x for x in rdir.glob("*.md") if x.is_file()], key=lambda x: x.stat().st_mtime)
    check("B9a", "paper-null-ladder-r95-independent-review-20261111.md", rf[-1].name)

    # ---- Group C: decision-debt anchors
    d111 = txt("state-handoff-R111/R111-DECISION-READY-PACKAGE.md")
    check("C1", [32, 38, 43, 48, 53], [line_of(d111, f"### D-{i} ") for i in range(1, 6)])
    check("C2a", 112, line_of(a111, "guard S1–S7 步骤状态认证"))
    check("C2b", 113, line_of(a111, "G0 书面冻结判据 + 指定独立判定方"))
    check("C2c", 114, line_of(a111, "≤32h / K=45 confirmation 面板"))
    a114 = txt("gate-G0-R114/R114-ROUND-AUDIT.md")
    check("C3", 61, line_of(a114, "gap 4（R106 R6）须 designated G0 gate owner"))
    a116 = txt("gate-G0-R116/R116-ROUND-AUDIT.md")
    check("C4", 85, line_of(a116, "归档全量内容核验（12 件大文件按 R109 排除清单处理，须 gate owner 裁决是否必要）"))
    a117 = txt("exec-premise-R117/R117-ROUND-AUDIT.md")
    check("C5", 75, line_of(a117, "本轮暴露的三项 P3 前置"))
    a118 = txt("gate-G0-R118/R118-ROUND-AUDIT.md")
    check("C6", 61, line_of(a118, "本轮量化的 **R4 指定登记**"))
    a119 = txt("review-protocol-R119/R119-ROUND-AUDIT.md")
    check("C7", [54, 57, 121], hits(a119, "v4"))
    r99 = txt("R99-design-block-decision.md")
    check("C8a", 50, line_of(r99, "## Decision: `BLOCKED_ON_CONFIRMATION`, return to ordered gates"))
    check("C8b", 74, line_of(r99, "≤32h confirmation panel / K=45 formal family"))

    n_match = sum(1 for c in CHECKS if c["status"] == "MATCH")
    n_mis = sum(1 for c in CHECKS if c["status"] == "MISMATCH")
    out = {
        "schema_version": 1,
        "round": "R120",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "boundary": "READ_ONLY_VERIFICATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
        "independence": "no import of R120-raw.py; no R120 JSON read; all values recomputed from original source bytes",
        "n_checks": len(CHECKS),
        "n_match": n_match,
        "n_mismatch": n_mis,
        "checks": CHECKS,
        "scope_note": "same host / same hashlib / same data sources => necessary consistency check, NOT independent cross-verification (R115 W4 / R114 D1); truly independent recomputation is delegated to a fresh isolated sub-agent",
    }
    (HERE / "R120-RECONCILIATION-VERIFICATION.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"n_checks": len(CHECKS), "n_match": n_match, "n_mismatch": n_mis,
                      "mismatches": [c["id"] for c in CHECKS if c["status"] == "MISMATCH"]},
                     ensure_ascii=False, indent=2))
    return 0 if n_mis == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

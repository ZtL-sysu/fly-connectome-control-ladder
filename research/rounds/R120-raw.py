#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R120 read-only collector: standing-instruction <-> on-disk state reconciliation.

Boundary: READ_ONLY_RECONCILIATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT.
Zero network requests, zero forward pass / inference / training / dataset /
label / EPE-l2 / scientific metric. Reads raw bytes only. Emits exactly two
files inside this directory: R120-RECONCILIATION-RAW.json and
R120-SOURCE-MANIFEST.json. Does not modify any pre-existing project byte.

All absolute local paths in emitted JSON are masked to <local>/ (R119 M1).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
PROJECT = RUN.parent.parent.parent  # .../fly-gnn-snn-vision
OUT = Path(__file__).resolve().parent

LOCAL_PREFIXES = [str(PROJECT), str(Path.home()), "/Users/"]


def mask(s: str) -> str:
    for p in (str(PROJECT), str(Path.home())):
        s = s.replace(p, "<local>/")
    s = re.sub(r"/Users/[A-Za-z0-9._-]+/", "<local>/", s)
    return s


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def read(rel: str, base: Path | None = None) -> bytes:
    p = (base or RUN) / rel
    if not p.is_file():
        return b""
    return p.read_bytes()


def text(rel: str, base: Path | None = None) -> str:
    return read(rel, base).decode("utf-8", errors="replace")


def line_hits(t: str, needle: str) -> list[int]:
    return [i for i, ln in enumerate(t.splitlines(), 1) if needle in ln]


def find_line(t: str, needle: str) -> int:
    h = line_hits(t, needle)
    return h[0] if h else 0


# ---------------------------------------------------------------- source table
SOURCES: list[tuple[str, Path]] = [
    ("GOAL-ITERATION-R107.md", PROJECT),
    ("goal-ledger.md", PROJECT),
    ("readonly-validator/validate_single_paper.py", PROJECT),
    ("guard/criteria-null-ladder.json", PROJECT),
    ("guard/ledger-null-ladder.json", PROJECT),
    ("R99-design-block-decision.md", RUN),
    ("pipeline-state.json", RUN),
    ("guidance-pipeline-state.md", RUN),
    ("literature-baseline-matrix.md", RUN),
    ("gate-G0-evidence-review-R98.md", RUN),
    ("gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md", RUN),
    ("gate-G0-R107/R107-G0-PASS-CRITERION-REGISTER.md", RUN),
    ("gate-G0-R107/R107-R1-R8-G0-CLOSURE-PACKAGE.md", RUN),
    ("gate-G0-R107/isolated-post-review/R107-R1-R8-G0-CLOSURE-PACKAGE.md", RUN),
    ("gate-G0-R107/isolated-post-review/R107-ROUND-AUDIT.md", RUN),
    ("gate-G0-R107/isolated-post-review/R107-INDEPENDENT-REVIEW-RECOVERY.md", RUN),
    ("state-handoff-R108/f-research-v1-state/pipeline-state.json", RUN),
    ("state-handoff-R108/f-research-v1-state/R108-U6-W2-VERSIONED-CONTRACT.md", RUN),
    ("state-handoff-R108/f-research-v1-state/R108-U6-W2-STATE-INPUT-MANIFEST.json", RUN),
    ("state-handoff-R108/R108-ROUND-AUDIT.md", RUN),
    ("state-handoff-R110/R110-ROUND-AUDIT.md", RUN),
    ("state-handoff-R111/R111-DECISION-READY-PACKAGE.md", RUN),
    ("state-handoff-R111/R111-ROUND-AUDIT.md", RUN),
    ("gate-G0-R114/R114-ROUND-AUDIT.md", RUN),
    ("gate-G0-R115/R115-ROUND-AUDIT.md", RUN),
    ("gate-G0-R116/R116-ROUND-AUDIT.md", RUN),
    ("exec-premise-R117/R117-ROUND-AUDIT.md", RUN),
    ("gate-G0-R118/R118-ROUND-AUDIT.md", RUN),
    ("review-protocol-R119/R119-ROUND-AUDIT.md", RUN),
    ("reconciliation-R120/R120-validator-out.json", RUN),
    ("reconciliation-R120/R120-guard-check.txt", RUN),
]

# ------------------------------------------------------------------ collectors
def main() -> int:
    src = []
    for rel, base in SOURCES:
        b = read(rel, base)
        p = base / rel
        src.append({
            "path": mask(rel) if base == PROJECT else rel,
            "base": "project" if base == PROJECT else "run",
            "exists": p.is_file(),
            "bytes": len(b),
            "sha256": sha256(b) if b else None,
            "mtime_epoch": p.stat().st_mtime if p.is_file() else None,
        })

    # -- A. standing instruction anchors (disk restatements of step 1 list)
    goal = text("GOAL-ITERATION-R107.md", PROJECT)
    r107pkg = text("gate-G0-R107/isolated-post-review/R107-R1-R8-G0-CLOSURE-PACKAGE.md")
    r107pkg_main = text("gate-G0-R107/R107-R1-R8-G0-CLOSURE-PACKAGE.md")
    r107audit = text("gate-G0-R107/isolated-post-review/R107-ROUND-AUDIT.md")
    r107rec = text("gate-G0-R107/isolated-post-review/R107-INDEPENDENT-REVIEW-RECOVERY.md")
    r106 = text("gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md")

    A = {
        "A1_goal_frozen_contracts_clause": {
            "needle": "`guidance-v2.md`, `execution-contract-v1/v2/v3.md`, `protocols/`",
            "lines": line_hits(goal, "`guidance-v2.md`, `execution-contract-v1/v2/v3.md`, `protocols/`"),
            "v4_clause_lines": line_hits(goal, "a future versioned contract (v4) may restate"),
        },
        "A2_r107_handoff_step1b": {
            "needle": "U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state",
            "closure_pkg_isolated_line": find_line(r107pkg, "U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state"),
            "closure_pkg_main_line": find_line(r107pkg_main, "U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state"),
            "round_audit_line": find_line(r107audit, "U6/W2 版本化契约 → 新建 f-research-v1 P0 state"),
            "recovery_line": find_line(r107rec, "U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state"),
        },
        "A3_r106_no_g0_written_criterion": {
            "needle": "全文没有 G0 的定义",
            "lines": line_hits(r106, "全文没有 G0 的定义"),
            "w13_lines": line_hits(r106, "**W13 [LOW｜结构性]**"),
            "verdict_line": find_line(r106, "**Verdict:** PARTIAL | **G0 may be passed:** NO"),
        },
        "A4_r106_r1_r9": {
            "r1_line": find_line(r106, "**R1（闭 gap 1）**"),
            "r6_line": find_line(r106, "**R6（闭 gap 4）**"),
            "r7_line": find_line(r106, "**R7**"),
            "r8_line": find_line(r106, "- **R8** 重新冻结"),
            "r9_line": find_line(r106, "- **R9** R1–R8 完成后"),
        },
        "A5_r111_stale_prompt_note": {
            "needle": "心跳 prompt 内嵌「交下轮」仍是 **R106 清单**",
            "lines": line_hits(text("state-handoff-R111/R111-ROUND-AUDIT.md"), "心跳 prompt 内嵌「交下轮」仍是 **R106 清单**"),
        },
    }

    # -- B. on-disk state reconciliation
    guidance = json.loads(text("pipeline-state.json") or "{}")
    p_state = json.loads(text("state-handoff-R108/f-research-v1-state/pipeline-state.json") or "{}")
    g_stages = guidance.get("stages", [])
    p_stages = p_state.get("stages", [])
    g0 = next((s for s in g_stages if s.get("id") == "G0"), {})
    contract_md = text("state-handoff-R108/f-research-v1-state/R108-U6-W2-VERSIONED-CONTRACT.md")
    pc = text("gate-G0-R107/R107-G0-PASS-CRITERION-REGISTER.md")
    matrix = text("literature-baseline-matrix.md")
    validator = text("readonly-validator/validate_single_paper.py", PROJECT)
    crit = text("guard/criteria-null-ladder.json", PROJECT)
    ledg = text("guard/ledger-null-ladder.json", PROJECT)

    B = {
        "B1_guidance_state": {
            "pipeline": guidance.get("pipeline"),
            "contract_version": guidance.get("contract_version"),
            "n_stages": len(g_stages),
            "stage_ids": [s.get("id") for s in g_stages],
            "passed_ids": [s.get("id") for s in g_stages if s.get("status") == "passed"],
            "pending_ids": [s.get("id") for s in g_stages if s.get("status") == "pending"],
            "G0_status": g0.get("status"),
            "G0_inputs_len": len(g0.get("inputs", [])),
            "G0_evidence_len": len(g0.get("evidence", [])),
            "G0_gate_verdict": g0.get("gate_verdict"),
            "p_stage_ids_present_in_guidance": [s.get("id") for s in g_stages if re.fullmatch(r"P\d+[A-Z]?", str(s.get("id")))],
        },
        "B2_r108_f_research_v1_p0_state": {
            "pipeline": p_state.get("pipeline"),
            "contract_version": p_state.get("contract_version"),
            "n_stages": len(p_stages),
            "stage_ids": [s.get("id") for s in p_stages],
            "statuses": sorted({s.get("status") for s in p_stages}),
            "n_history": len(p_state.get("history", [])),
            "n_contract_entries": len(p_state.get("contract", [])),
            "contract_paths": [c.get("path") for c in p_state.get("contract", [])],
        },
        "B3_r108_versioned_contract": {
            "bytes": len(contract_md.encode("utf-8")),
            "draft_line": find_line(contract_md, "DRAFT，未激活"),
            "boundary_line": find_line(contract_md, "ENGINEERING_STATE_SCAFFOLD_ONLY_NOT_SCIENTIFIC_RESULT"),
            "authorization_line": find_line(contract_md, "PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF"),
            "not_p0_start_line": find_line(contract_md, "本文件不是 P0 的启动"),
        },
        "B4_r107_g0_pass_criterion_register": {
            "status_line": find_line(pc, "DRAFT — PENDING DESIGNATED GATE OWNER APPROVAL"),
            "not_effective_line": find_line(pc, "不生效"),
            "pc_ids": [f"PC{i}" for i in range(1, 7) if f"**PC{i}" in pc],
            "pc4_not_done_line": find_line(pc, "R107 状态：**未做（主会话越权）**"),
            "pc5_not_done_line": find_line(pc, "R107 状态：**未做**"),
            "no_byte_change_line": find_line(pc, "本汇编不改变"),
        },
        "B5_gap2_matrix_stale": {
            "bytes": len(matrix.encode("utf-8")),
            "stale_open_question_lines": line_hits(matrix, "the open question"),
            "stale_kuklev_leaves_lines": line_hits(matrix, "Kuklev leaves"),
            "asset_unverified_lines": line_hits(matrix, "asset contents/license not yet individually verified"),
            "code_path_unverified_lines": line_hits(matrix, "project code path not yet verified"),
        },
        "B6_validator_live_config": {
            "default_threshold_line": find_line(validator, "default=7.0"),
            "ge_operator_line": find_line(validator, 'score >= args.threshold'),
            "score_meets_threshold_line": find_line(validator, '"score_meets_threshold"'),
            "contract_line": find_line(validator, '"contract": "R107 single paper, independent full review Overall >= 7.0"'),
        },
        "B7_guard_a6_dual_wording": {
            "criteria_ge7_line": find_line(crit, '"id": "A6"'),
            "criteria_ge7_text_line": find_line(crit, "Overall >= 7.0（R107；等于 7.0 算达标"),
            "criteria_cmd_ge_line": find_line(crit, "g>=7.0"),
            "ledger_gt8_text_line": find_line(ledg, "严格 > 8.0（等于 8.0 不算"),
            "ledger_cmd_gt_line": find_line(ledg, "g>8.0"),
        },
        "B8_double_gate_readouts_this_round": {
            "validator": json.loads(text("reconciliation-R120/R120-validator-out.json") or "{}"),
            "guard_check_sha256": sha256(read("reconciliation-R120/R120-guard-check.txt")),
            "guard_incomplete_line": find_line(text("reconciliation-R120/R120-guard-check.txt"), "INCOMPLETE"),
            "guard_a2_fail_line": find_line(text("reconciliation-R120/R120-guard-check.txt"), "[FAIL] A2"),
            "guard_a6_fail_line": find_line(text("reconciliation-R120/R120-guard-check.txt"), "[FAIL] A6"),
            "guard_s_pending_count": len(re.findall(r"S\d \[pending \]", text("reconciliation-R120/R120-guard-check.txt"))),
            "guard_action_sequence_line": find_line(text("reconciliation-R120/R120-guard-check.txt"), "【动作序列】共 0 条"),
        },
        "B9_review_dir_governing": {
            "newest_review_file": None,
            "numeric_overall_lines_after_r95": [],
        },
    }

    # review dir scan (read-only)
    rdir = PROJECT / "ccfa-review-reports"
    files = sorted([p for p in rdir.glob("*.md") if p.is_file()], key=lambda p: p.stat().st_mtime)
    if files:
        B["B9_review_dir_governing"]["newest_review_file"] = files[-1].name
        B["B9_review_dir_governing"]["n_review_files"] = len(files)
    idir = PROJECT / "ccfa-idea-review-reports"
    ifiles = sorted([p for p in idir.glob("*.md") if p.is_file()], key=lambda p: p.stat().st_mtime)
    B["B9_review_dir_governing"]["newest_idea_review_file"] = ifiles[-1].name if ifiles else None

    # -- C. decision-debt atoms, with exact anchors
    d111 = text("state-handoff-R111/R111-DECISION-READY-PACKAGE.md")
    a111 = text("state-handoff-R111/R111-ROUND-AUDIT.md")
    a114 = text("gate-G0-R114/R114-ROUND-AUDIT.md")
    a116 = text("gate-G0-R116/R116-ROUND-AUDIT.md")
    a117 = text("exec-premise-R117/R117-ROUND-AUDIT.md")
    a118 = text("gate-G0-R118/R118-ROUND-AUDIT.md")
    a119 = text("review-protocol-R119/R119-ROUND-AUDIT.md")
    r99 = text("R99-design-block-decision.md")

    C = {
        "C1_r111_five_decisions": {
            f"D-{i}_line": find_line(d111, f"### D-{i} ") for i in range(1, 6)
        },
        "C2_r111_round_decision_table": {
            "header_line": find_line(a111, "逐条对照 R110 交下轮与红线后"),
            "a6_row_line": find_line(a111, "guard S1–S7 步骤状态认证"),
            "g0_row_line": find_line(a111, "G0 书面冻结判据 + 指定独立判定方"),
            "confirm_row_line": find_line(a111, "≤32h / K=45 confirmation 面板"),
        },
        "C3_r114_gap4": {"line": find_line(a114, "gap 4（R106 R6）须 designated G0 gate owner")},
        "C4_r116_gap1_remaining_three": {
            "line": find_line(a116, "归档全量内容核验（12 件大文件按 R109 排除清单处理，须 gate owner 裁决是否必要）"),
            "needle": "checkpoint 权重分发条款、natural clips 独立许可文本",
            "present": "checkpoint 权重分发条款、natural clips 独立许可文本" in a116,
        },
        "C5_r117_p3_preconditions": {"line": find_line(a117, "本轮暴露的三项 P3 前置")},
        "C6_r118_registry_matrix": {"line": find_line(a118, "本轮量化的 **R4 指定登记**")},
        "C7_r119_versioned_contract": {
            "v4_lines": line_hits(a119, "v4"),
            "decision_lines": line_hits(a119, "gate owner"),
        },
        "C8_r99_confirmation_block": {
            "line": find_line(r99, "## Decision: `BLOCKED_ON_CONFIRMATION`, return to ordered gates"),
            "k45_line": find_line(r99, "≤32h confirmation panel / K=45 formal family"),
        },
    }

    out = {
        "schema_version": 1,
        "round": "R120",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "generated_at_local": datetime.now().astimezone().isoformat(),
        "python": mask(sys.executable),
        "python_version": sys.version.split()[0],
        "boundary": "READ_ONLY_RECONCILIATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
        "network_requests": 0,
        "forward_pass_performed": False,
        "scientific_result_claimed": False,
        "pre_existing_bytes_modified": 0,
        "path_masking": "all absolute local paths masked to <local>/ in emitted JSON fields",
        "notes": [
            "The standing heartbeat instruction is an in-context automation prompt, NOT a disk file; disk restatements of its step-1 list are anchored in group A.",
            "Double-gate readouts are byte-anchored inside this directory (R120-validator-out.json / R120-guard-check.txt), addressing R118 W7 / R119 M2 snapshot-scope defects.",
            "Ledger / state SHA entries are snapshot-at-collection-time readings; standard append-only ledger bookkeeping after capture changes live hashes but no historical byte.",
        ],
        "sources": src,
        "group_A_standing_instruction_anchors": A,
        "group_B_on_disk_state": B,
        "group_C_decision_debt_anchors": C,
    }

    (OUT / "R120-RECONCILIATION-RAW.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "R120-SOURCE-MANIFEST.json").write_text(
        json.dumps({
            "schema_version": 1,
            "round": "R120",
            "generated_at_utc": out["generated_at_utc"],
            "base": "run root for unprefixed paths; project root for base=project",
            "source_count": len(src),
            "sources": src,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "sources": len(src),
        "guidance_stages": len(g_stages),
        "p_stages": len(p_stages),
        "validator_verdict": B["B8_double_gate_readouts_this_round"]["validator"].get("verdict"),
        "guard_s_pending": B["B8_double_gate_readouts_this_round"]["guard_s_pending_count"],
        "A": len(A), "B": len(B), "C": len(C),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

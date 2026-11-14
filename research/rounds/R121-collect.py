#!/usr/bin/env python3
# R121 read-only collector. Single purpose: reconcile the GOVERNING independent
# full review's own score-change conditions against (a) the eight prior heartbeat
# rounds' declared output classes, (b) first-hand evidence status of the three
# "raise score" conditions, (c) the two machine gates, (d) the ordered gate chain.
# READ-ONLY with respect to every pre-existing byte. No forward pass, no training,
# no inference, no labels, no EPE/l2, no scientific metric, no network.
# Emits RAW json only. The independent verifier (R121-verify.py) must NOT import
# this module and must NOT read any R121-produced JSON.
import hashlib
import json
import os
import re
import subprocess
import sys
import time

PR = "/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision"
AP = os.path.join(PR, "auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision")
OUT = os.path.join(AP, "success-condition-R121")
PY = "/Users/xhf/miniconda3/bin/python"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def read(rel):
    p = os.path.join(PR, rel) if not rel.startswith("/") else rel
    with open(p, "rb") as f:
        return f.read()


def stat(rel):
    p = os.path.join(PR, rel) if not rel.startswith("/") else rel
    st = os.stat(p)
    return {"bytes": st.st_size, "mtime": st.st_mtime,
            "mtime_str": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(st.st_mtime))}


R95 = "ccfa-review-reports/paper-null-ladder-r95-independent-review-20261111.md"
V2 = "papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2"

ROUND_DIRS = {
    "R114": "gate-G0-R114/R114-ROUND-AUDIT.md",
    "R115": "gate-G0-R115/R115-ROUND-AUDIT.md",
    "R116": "gate-G0-R116/R116-ROUND-AUDIT.md",
    "R117": "exec-premise-R117/R117-ROUND-AUDIT.md",
    "R118": "gate-G0-R118/R118-ROUND-AUDIT.md",
    "R119": "review-protocol-R119/R119-ROUND-AUDIT.md",
    "R120": "reconciliation-R120/R120-ROUND-AUDIT.md",
}

SOURCES = {
    "S01_governing_r95": R95,
    "S02_r106_gate_review": os.path.join(AP, "gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md"),
    "S03_r107_goal_iteration": "GOAL-ITERATION-R107.md",
    "S04_r107_pass_criterion": os.path.join(AP, "gate-G0-R107/R107-G0-PASS-CRITERION-REGISTER.md"),
    "S05_r111_decision_package": os.path.join(AP, "state-handoff-R111/R111-DECISION-READY-PACKAGE.md"),
    "S06_r120_decision_register": os.path.join(AP, "reconciliation-R120/R120-CONSOLIDATED-DECISION-REGISTER.md"),
    "S07_mainline_state": os.path.join(AP, "pipeline-state.json"),
    "S08_r108_scaffold_state": os.path.join(AP, "state-handoff-R108/f-research-v1-state/pipeline-state.json"),
    "S09_r108_versioned_contract": os.path.join(AP, "state-handoff-R108/f-research-v1-state/R108-U6-W2-VERSIONED-CONTRACT.md"),
    "S10_validator": "readonly-validator/validate_single_paper.py",
    "S11_guard_ledger": "guard/ledger-null-ladder.json",
    "S12_guard_criteria": "guard/criteria-null-ladder.json",
    "S13_goal_ledger": "goal-ledger.md",
    "S14_real_connectome_metrics": os.path.join(V2, "results/r39_real_connectome_v2/metrics.json"),
    "S15_visual_task_metrics": os.path.join(V2, "results/r39_visual_task/metrics.json"),
    "S16_main_tex": os.path.join(V2, "paper/main.tex"),
}
for k, v in ROUND_DIRS.items():
    SOURCES["S17_" + k + "_audit"] = os.path.join(AP, v)


def main():
    raw = {
        "round": "R121",
        "kind": "READONLY_SUCCESS_CRITERION_CLOSURE_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
        "python": sys.version.split()[0],
        "sources": {},
        "needles": {},
        "rounds": {},
        "conditions": {},
        "gates": {},
        "numeric_overall_scan": {},
        "capture_time_hashes": {},
    }

    # ---- capture-time integrity anchors (declared snapshot, not an all-time claim)
    for tag, rel in [("goal_ledger", "goal-ledger.md"),
                     ("mainline_state", os.path.join(AP, "pipeline-state.json")),
                     ("scaffold_state", S08_r108_scaffold := SOURCES["S08_r108_scaffold_state"]),
                     ("guard_ledger", "guard/ledger-null-ladder.json")]:
        b = read(rel)
        raw["capture_time_hashes"][tag] = {"bytes": len(b), "sha256": sha(b),
                                           "mtime": stat(rel)["mtime"]}

    # ---- source registry
    for tag, rel in SOURCES.items():
        b = read(rel)
        raw["sources"][tag] = {"path": rel if rel.startswith("/") else rel,
                               "bytes": len(b), "sha256": sha(b), **stat(rel)}

    r95 = read(R95).decode("utf-8", "replace")
    r95_lines = r95.splitlines()

    # ---- governing review's own score-change taxonomy: exact byte needles
    needles = {
        "N01_overall_line": "**Overall:** 6  | **Scholarly Confidence:** 4",
        "N02_no_quick_change_head": "| **No quick change** | 继续补流程/披露/格式",
        "N03_no_quick_change_reason": "不新增支持中心主张的科学证据",
        "N04_no_quick_change_effect": "不改变 evidence-capped overall",
        "N05_raise_row": "单项 +0.5；三项齐备 Overall 6→7~7.5",
        "N06_raise_a": "真实 MaleCNS 图上以预注册协议**确认** motif-survival 阈值迁移",
        "N07_raise_b": "在 flyvis/`toposens2026` 栈复跑同协议对证",
        "N08_raise_c": "至少一项真实视觉任务上该诊断标准改变了一个实际结论",
        "N15_revision": "Raising the score would require: 真实图上确认 motif-survival 阈值迁移",
        "N09_m1_noprope": "需新的真实图实验确认机制迁移（非 prose 可修）",
        "N10_m2_noprope": "无法靠 prose 补出视觉贡献",
        "N11_m3_rerun": "在 flyvis / toposens2026 栈上跑一次同协议比较",
        "N12_evidence_dim3": "| Evidence | 3 | 5 |",
        "N13_significance_dim3": "| Significance | 3 | 4 |",
        "N14_tiebreaker7": "这组 ≥3 个决定性关切不允许 Overall 上到 7",
        "N16_c2_experiment": "| C2 | major | 中心机制真实图未复现",
        "N17_c3_experiment": "| C3 | major | 零视觉证据",
        "N18_c4_experiment": "| C4 | major | 强基线（flyvis / `toposens2026`）未复跑",
        "N19_panel_min": "一条真实图上确认机制迁移的独立结果 → 8",
    }
    for tag, needle in needles.items():
        found = [i + 1 for i, ln in enumerate(r95_lines) if needle in ln]
        raw["needles"][tag] = {"needle": needle, "found_lines": found,
                               "count": len(found)}

    # ---- eight prior rounds: declared output class + any positive-evidence claim
    for tag, rel in ROUND_DIRS.items():
        p = os.path.join(AP, rel)
        t = open(p, encoding="utf-8", errors="replace").read()
        first8 = t.splitlines()[:8]
        label_tokens = [tok for tok in ("READONLY", "READ_ONLY", "NOT_GATE_PASS",
                                        "NOT_SCIENTIFIC_RESULT", "NOT_FORWARD_PASS")
                        if any(tok in ln for ln in first8)]
        raw["rounds"][tag] = {
            "path": rel,
            "bytes": len(t.encode()),
            "sha256": sha(t.encode()),
            "declared_label_tokens_first8": label_tokens,
            "declared_first8": first8,
            "claims_new_scientific_result": bool(re.search(
                r"(hypothesis_supported\s*=\s*true|实质正向新证据已取得|真实视觉正结果|已复跑 flyvis)",
                t)),
            "claims_gate_passed": bool(re.search(
                r"(G0\s*(may be passed|已通过|passed)\s*[:：]\s*YES|G0\s*=\s*passed)", t)),
            "numeric_overall_line_count": len(re.findall(
                r"^\s*\*\*Overall:\*\*\s*[0-9]", t, re.M)),
        }

    # ---- condition (a): real-graph mechanism transfer, first-hand value
    hs = {}
    for dp, dn, fn in os.walk(os.path.join(PR, "papers")):
        if "/.git" in dp:
            continue
        for f in fn:
            if not f.endswith(".json"):
                continue
            p = os.path.join(dp, f)
            try:
                obj = json.load(open(p, encoding="utf-8", errors="replace"))
            except Exception:
                continue
            if isinstance(obj, dict) and "hypothesis_supported" in obj:
                hs[os.path.relpath(p, PR)] = obj["hypothesis_supported"]
    raw["conditions"]["a_real_graph_transfer"] = {
        "source": "all papers/**/*.json with a top-level hypothesis_supported",
        "observed": hs,
        "n_files": len(hs),
        "any_true": any(v is True for v in hs.values()),
        "note": "R95 §8 M1 / §13 (a) requires hypothesis_supported=true on a REAL graph under a pre-registered protocol.",
    }

    # ---- condition (b): strong baseline rerun on flyvis/toposens stack
    rerun_candidates = []
    for dp, dn, fn in os.walk(PR):
        if "/.git" in dp or "research-sync-public" in dp:
            continue
        for f in fn:
            low = f.lower()
            if ("rerun" in low or "reproduce" in low) and (
                    "flyvis" in low or "toposens" in low):
                rerun_candidates.append(os.path.relpath(os.path.join(dp, f), PR))
    main_tex = open(os.path.join(PR, S16_main_tex := SOURCES["S16_main_tex"]),
                    encoding="utf-8", errors="replace").read()
    raw["conditions"]["b_strong_baseline_rerun"] = {
        "rerun_metric_files_by_name": rerun_candidates,
        "n_rerun_metric_files": len(rerun_candidates),
        "main_tex_admission": "We did not rerun their flyvis stack and make no benchmark-reproduction claim" in main_tex,
        "note": "R95 §8 M3 / §13 (b); a rerun is a forward-pass experiment, not a document.",
    }

    # ---- condition (c): real visual task where the diagnostic changes a conclusion
    vm_path = os.path.join(PR, SOURCES["S15_visual_task_metrics"])
    vobj = json.load(open(vm_path, encoding="utf-8", errors="replace"))

    def find_keys(obj, key, acc, depth=0):
        if depth > 8:
            return
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key or "negative" in k.lower() or "delta" in k.lower():
                    acc.append((k, v if isinstance(v, (int, float, str, bool, type(None))) else type(v).__name__))
                find_keys(v, key, acc, depth + 1)

    acc = []
    find_keys(vobj, "hypothesis_supported", acc)
    raw["conditions"]["c_real_visual_task"] = {
        "metrics_path": SOURCES["S15_visual_task_metrics"],
        "top_level_keys": list(vobj.keys())[:30],
        "negative_or_delta_fields": acc[:30],
        "note": "R95 §8 M2 / §13 (c) records the real visual task as a NEGATIVE result; no claim of a changed conclusion.",
    }

    # ---- machine gates: live, read-only
    vproc = subprocess.run([PY, os.path.join(PR, "readonly-validator/validate_single_paper.py")],
                           cwd=PR, capture_output=True, text=True)
    raw["gates"]["validator"] = {"exit": vproc.returncode,
                                 "stdout": vproc.stdout.strip()[:6000]}
    gproc = subprocess.run([PY, "/Users/xhf/.workbuddy/skills/task-completion-guard/guard_engine.py",
                            "check", "-l", "guard/ledger-null-ladder.json",
                            "-o", os.path.join(OUT, "R121-guard-report.md")],
                           cwd=PR, capture_output=True, text=True)
    raw["gates"]["guard"] = {"exit": gproc.returncode,
                             "verdict_line": [ln for ln in gproc.stdout.splitlines()
                                              if "COMPLETE" in ln or "INCOMPLETE" in ln][:6],
                             "fail_lines": [ln.strip() for ln in gproc.stdout.splitlines()
                                            if "[FAIL]" in ln][:10],
                             "step_pending_count": len([ln for ln in gproc.stdout.splitlines()
                                                        if re.search(r"S[1-7] \[pending", ln)])}

    # ---- mainline ordered gate chain
    st = json.load(open(os.path.join(PR, SOURCES["S07_mainline_state"]), encoding="utf-8"))
    raw["gates"]["mainline_stages"] = [
        {"id": s.get("id"), "status": s.get("status"),
         "inputs": len(s.get("inputs", [])), "evidence": len(s.get("evidence", [])),
         "gate_verdict": s.get("gate_verdict")}
        for s in st.get("stages", [])]

    # ---- no newer governing full review
    pat = re.compile(r"^\s*\*\*Overall:\*\*\s*([0-9]+(?:\.[0-9]+)?)", re.M)
    hits = []
    r95_mtime = stat(R95)["mtime"]
    for dp, dn, fn in os.walk(PR):
        if "/.git" in dp or "research-sync-public" in dp:
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            try:
                t = open(p, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for m in pat.finditer(t):
                hits.append({"path": os.path.relpath(p, PR), "score": m.group(1),
                             "mtime": os.stat(p).st_mtime})
    hits.sort(key=lambda x: x["mtime"], reverse=True)
    newer = [h for h in hits if h["mtime"] > r95_mtime]
    for h in newer:
        h["byte_identical_to_r95"] = (sha(read(h["path"])) == sha(read(R95)))
    raw["numeric_overall_scan"] = {
        "total_lines": len(hits),
        "r95_mtime": r95_mtime,
        "newer_than_r95": newer,
        "new_governing_candidates": [h for h in newer if not h["byte_identical_to_r95"]],
    }

    with open(os.path.join(OUT, "R121-RAW.json"), "w", encoding="utf-8") as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)
    print("RAW written:", os.path.join(OUT, "R121-RAW.json"))
    print("sources:", len(raw["sources"]), "needles:", len(raw["needles"]),
          "rounds:", len(raw["rounds"]))
    print("needle misses:", [k for k, v in raw["needles"].items() if v["count"] == 0])
    print("validator exit:", raw["gates"]["validator"]["exit"],
          "| guard exit:", raw["gates"]["guard"]["exit"],
          "| newer numeric lines:", len(newer))


if __name__ == "__main__":
    main()

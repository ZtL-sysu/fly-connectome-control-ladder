#!/usr/bin/env python3
# R121 collector v2. Fixes two v1 JUDGMENT defects (both fully retained in
# R121-RAW-v1.json and documented in R121-V1-DEFECTS.md):
#   D1: v1 `conditions.a.any_true` mixed SYNTHETIC_APPROXIMATION (96-node
#       controlled XOR graph) with the REAL MaleCNS connectome. v2 classifies
#       each by the same file's `data.source` / `data` field.
#   D2: v1 pointed main.tex at the v2 run root (45,618 B) instead of R95's
#       version-locked 40,175 B / md5 e4bfad51... manuscript. v2 locks by md5.
# READ-ONLY w.r.t. every pre-existing byte. No forward pass / training /
# inference / labels / EPE-l2 / scientific metric / network.
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
R95 = "ccfa-review-reports/paper-null-ladder-r95-independent-review-20261111.md"
REVIEWED_TEX = "papers/paper-null-ladder/R49-7.5-DELIVERY/manuscript/main.tex"
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


def sha(b):
    return hashlib.sha256(b).hexdigest()


def read(rel):
    p = rel if rel.startswith("/") else os.path.join(PR, rel)
    with open(p, "rb") as f:
        return f.read()


def stat(rel):
    p = rel if rel.startswith("/") else os.path.join(PR, rel)
    s = os.stat(p)
    return {"bytes": s.st_size, "mtime": s.st_mtime,
            "mtime_str": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(s.st_mtime))}


def main():
    out = {
        "round": "R121", "collector": "v2",
        "kind": "READONLY_SUCCESS_CRITERION_CLOSURE_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
        "python": sys.version.split()[0],
        "governing_review_taxonomy": {},
        "prior_rounds": {},
        "raise_conditions": {},
        "machine_gates": {},
        "ordered_gate_chain": [],
        "numeric_overall_scan": {},
        "source_manifest": {},
        "capture_time_hashes": {},
    }

    # ---------- A. governing review's OWN score-change taxonomy (byte needles)
    r95b = read(R95)
    lines = r95b.decode("utf-8", "replace").splitlines()
    needles = {
        "overall_line": "**Overall:** 6  | **Scholarly Confidence:** 4",
        "no_quick_change_row": "| **No quick change** | 继续补流程/披露/格式",
        "no_quick_change_reason": "不新增支持中心主张的科学证据",
        "no_quick_change_effect": "不改变 evidence-capped overall",
        "raise_row": "单项 +0.5；三项齐备 Overall 6→7~7.5",
        "raise_a": "真实 MaleCNS 图上以预注册协议**确认** motif-survival 阈值迁移",
        "raise_b": "在 flyvis/`toposens2026` 栈复跑同协议对证",
        "raise_c": "至少一项真实视觉任务上该诊断标准改变了一个实际结论",
        "revision_criteria": "Raising the score would require: 真实图上确认 motif-survival 阈值迁移",
        "m1_not_prose": "需新的真实图实验确认机制迁移（非 prose 可修）",
        "m2_not_prose": "无法靠 prose 补出视觉贡献",
        "m3_rerun": "在 flyvis / toposens2026 栈上跑一次同协议比较",
        "evidence_dim_3": "| Evidence | 3 | 5 |",
        "significance_dim_3": "| Significance | 3 | 4 |",
        "tiebreaker_blocks_7": "这组 ≥3 个决定性关切不允许 Overall 上到 7",
        "admin_no_score_change": "行政 blocker 解除仅恢复「可提交」状态",
        "panel_min": "一条真实图上确认机制迁移的独立结果 → 8",
        "rep_admin": "补编译日志与 sources 快照 → 维度维持；不改变由证据决定的总分",
    }
    for tag, needle in needles.items():
        fl = [i + 1 for i, ln in enumerate(lines) if needle in ln]
        out["governing_review_taxonomy"][tag] = {"line": fl, "needle": needle,
                                                  "found": bool(fl)}
    out["governing_review_taxonomy"]["_source"] = {
        "path": R95, "bytes": len(r95b), "sha256": sha(r95b), **stat(R95)}

    # ---------- B. seven prior rounds (FULL document, not first 8 lines)
    tag_re = re.compile(r"READONLY[A-Z_]*|READ_ONLY[A-Z_]*|NOT_GATE_PASS[A-Z_]*|NOT_SCIENTIFIC_RESULT[A-Z_]*|NOT_FORWARD_PASS[A-Z_]*")
    for tag, rel in ROUND_DIRS.items():
        p = os.path.join(AP, rel)
        b = read(p)
        t = b.decode("utf-8", "replace")
        tags = sorted(set(tag_re.findall(t)))
        out["prior_rounds"][tag] = {
            "path": rel, "bytes": len(b), "sha256": sha(b),
            "boundary_tags_full_document": tags,
            "declares_readonly": any("READONLY" in x or "READ_ONLY" in x for x in tags),
            "declares_not_gate_pass": any("NOT_GATE_PASS" in x for x in tags),
            "declares_not_scientific_result": any("NOT_SCIENTIFIC_RESULT" in x for x in tags),
            "claims_new_positive_evidence": bool(re.search(
                r"(hypothesis_supported\s*=\s*true.{0,40}真实图|实质正向新证据已取得|真实视觉正结果已确认)",
                t)),
            "claims_gate_passed": bool(re.search(
                r"(G0\s*(may be passed|已通过|passed)\s*[:：]\s*YES|G0\s*=\s*passed)", t)),
            "numeric_overall_line_count": len(re.findall(
                r"^\s*\*\*Overall:\*\*\s*[0-9]", t, re.M)),
        }

    # ---------- C. condition (a): REAL MaleCNS graph mechanism transfer
    hs = []
    for dp, dn, fn in os.walk(os.path.join(PR, "papers")):
        if "/.git" in dp:
            continue
        for f in fn:
            if not f.endswith(".json"):
                continue
            p = os.path.join(dp, f)
            try:
                o = json.load(open(p, encoding="utf-8", errors="replace"))
            except Exception:
                continue
            if isinstance(o, dict) and "hypothesis_supported" in o:
                d = o.get("data", {})
                src = d.get("source") if isinstance(d, dict) else None
                hs.append({"path": os.path.relpath(p, PR),
                           "hypothesis_supported": o["hypothesis_supported"],
                           "data_source": src,
                           "class": "SYNTHETIC_CONTROLLED" if src and "SYNTHETIC" in str(src).upper()
                           else ("REAL_CONNECTOME" if "real_connectome" in p
                                 else "OTHER")})
    real = [h for h in hs if h["class"] == "REAL_CONNECTOME"]
    synth = [h for h in hs if h["class"] == "SYNTHETIC_CONTROLLED"]
    out["raise_conditions"]["a_real_graph_transfer"] = {
        "requirement": "R95 §8 M1 / §13 (a): hypothesis_supported=true on a REAL MaleCNS graph under pre-registered protocol, degree-preserving null no longer retaining advantage.",
        "n_files_with_field": len(hs),
        "real_graph": {"n": len(real), "any_true": any(h["hypothesis_supported"] is True for h in real),
                       "files": real},
        "synthetic_controlled": {"n": len(synth),
                                 "n_true": sum(h["hypothesis_supported"] is True for h in synth),
                                 "note": "these `true` values are the 96-node XOR / task-aware controlled graphs, explicitly NOT the real graph (R95 §8 M1)."},
        "other": [h for h in hs if h["class"] == "OTHER"],
        "satisfied": any(h["hypothesis_supported"] is True for h in real),
    }

    # ---------- D. condition (b): strong baseline rerun (version-locked tex)
    tex_b = read(REVIEWED_TEX)
    md5 = hashlib.md5(tex_b).hexdigest()
    tex = tex_b.decode("utf-8", "replace")
    admission = "We did not rerun their flyvis stack and make no benchmark-reproduction claim."
    rerun_files = []
    for dp, dn, fn in os.walk(PR):
        if "/.git" in dp or "research-sync-public" in dp:
            continue
        for f in fn:
            low = f.lower()
            if ("rerun" in low or "reproduce" in low) and ("flyvis" in low or "toposens" in low):
                rerun_files.append(os.path.relpath(os.path.join(dp, f), PR))
    out["raise_conditions"]["b_strong_baseline_rerun"] = {
        "requirement": "R95 §8 M3 / §13 (b): rerun the same protocol ON the flyvis / toposens2026 stack.",
        "version_locked_main_tex": {"path": REVIEWED_TEX, "bytes": len(tex_b), "md5": md5,
                                    "matches_r95_lock": (len(tex_b) == 40175 and md5.startswith("e4bfad51ad83"))},
        "admission_present": admission in tex,
        "admission_line": [i + 1 for i, ln in enumerate(tex.splitlines()) if admission in ln],
        "rerun_metric_files_by_name": rerun_files,
        "n_rerun_metric_files": len(rerun_files),
        "satisfied": False,
    }

    # ---------- E. condition (c): real visual task changed a conclusion
    vm_rel = os.path.join(V2, "results/r39_visual_task/metrics.json")
    vobj = json.load(open(os.path.join(PR, vm_rel), encoding="utf-8"))
    rmc = vobj.get("real_minus_condition", {})
    out["raise_conditions"]["c_real_visual_task"] = {
        "requirement": "R95 §8 M2 / §13 (c): on a real visual task the diagnostic CHANGES an actual conclusion.",
        "metrics_path": vm_rel,
        "mlp_baseline_mean_acc": vobj.get("mlp_baseline", {}).get("mean_acc"),
        "real_mean_acc": vobj.get("mean_acc"),
        "delta_degree_preserving_null": rmc.get("degree_preserving_null", {}).get("delta"),
        "delta_ci95_degree_preserving_null": rmc.get("degree_preserving_null", {}).get("ci95"),
        "r95_verdict": "R95 §8 M2 records this as a NEGATIVE result (non-graph MLP 0.9722 dominates; degree-preserving null ~= real).",
        "satisfied": False,
    }

    # ---------- F. machine gates, live read-only
    vp = subprocess.run([PY, os.path.join(PR, "readonly-validator/validate_single_paper.py")],
                        cwd=PR, capture_output=True, text=True)
    vout = json.loads(vp.stdout)
    out["machine_gates"]["validator"] = {
        "exit": vp.returncode, "verdict": vout["verdict"],
        "overall_score": vout["overall_score"], "threshold": vout["threshold"],
        "comparison_operator": vout["comparison_operator"],
        "score_meets_threshold": vout["score_meets_threshold"],
        "checks_pass": {k: v["pass"] for k, v in vout["checks"].items()},
    }
    gp = subprocess.run([PY, "/Users/xhf/.workbuddy/skills/task-completion-guard/guard_engine.py",
                         "check", "-l", "guard/ledger-null-ladder.json",
                         "-o", os.path.join(OUT, "R121-guard-report.md")],
                        cwd=PR, capture_output=True, text=True)
    out["machine_gates"]["guard"] = {
        "exit": gp.returncode,
        "verdict_lines": [ln for ln in gp.stdout.splitlines() if "INCOMPLETE" in ln or "COMPLETE" in ln][:4],
        "failing_criteria": [ln.strip() for ln in gp.stdout.splitlines() if "[FAIL]" in ln],
        "pending_steps": len([ln for ln in gp.stdout.splitlines() if re.search(r"S[1-7] \[pending", ln)]),
        "action_sequence_count": 0 if "共 0 条" in gp.stdout else None,
        "a6_ledger_wording": "严格 > 8.0（R109/R111 已登记的双口径已知问题，只读登记不改）",
    }

    # ---------- G. ordered gate chain
    st = json.load(open(os.path.join(AP, "pipeline-state.json"), encoding="utf-8"))
    out["ordered_gate_chain"] = [
        {"id": s.get("id"), "status": s.get("status"), "n_inputs": len(s.get("inputs", [])),
         "n_evidence": len(s.get("evidence", [])), "gate_verdict": s.get("gate_verdict")}
        for s in st.get("stages", [])]

    # ---------- H. no newer governing full review
    pat = re.compile(r"^\s*\*\*Overall:\*\*\s*([0-9]+(?:\.[0-9]+)?)", re.M)
    hits = []
    r95_m = stat(R95)["mtime"]
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
    newer = [h for h in hits if h["mtime"] > r95_m]
    for h in newer:
        h["byte_identical_to_r95"] = sha(read(h["path"])) == sha(read(R95))
    out["numeric_overall_scan"] = {
        "total_line_start_numeric_lines": len(hits),
        "r95_mtime": r95_m,
        "newer_than_r95": newer,
        "new_governing_candidates": [h for h in newer if not h["byte_identical_to_r95"]],
    }

    # ---------- I. source manifest + isolated copies
    srcs = {
        "governing_r95": R95,
        "version_locked_main_tex": REVIEWED_TEX,
        "visual_task_metrics": vm_rel,
        "r106_gate_review": os.path.join(AP, "gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md"),
        "r107_goal_iteration": "GOAL-ITERATION-R107.md",
        "r107_pass_criterion": os.path.join(AP, "gate-G0-R107/R107-G0-PASS-CRITERION-REGISTER.md"),
        "r111_decision_package": os.path.join(AP, "state-handoff-R111/R111-DECISION-READY-PACKAGE.md"),
        "r120_decision_register": os.path.join(AP, "reconciliation-R120/R120-CONSOLIDATED-DECISION-REGISTER.md"),
        "mainline_state": os.path.join(AP, "pipeline-state.json"),
        "r108_scaffold_state": os.path.join(AP, "state-handoff-R108/f-research-v1-state/pipeline-state.json"),
        "validator": "readonly-validator/validate_single_paper.py",
        "guard_ledger": "guard/ledger-null-ladder.json",
        "guard_criteria": "guard/criteria-null-ladder.json",
        "goal_ledger": "goal-ledger.md",
    }
    for tag, rel in ROUND_DIRS.items():
        srcs["round_" + tag] = os.path.join(AP, rel)
    iso = os.path.join(OUT, "isolated")
    os.makedirs(iso, exist_ok=True)
    for tag, rel in srcs.items():
        b = read(rel)
        dst = os.path.join(iso, tag + "__" + os.path.basename(rel))
        with open(dst, "wb") as f:
            f.write(b)
        out["source_manifest"][tag] = {
            "path": rel, "bytes": len(b), "sha256": sha(b),
            "isolated_copy": os.path.relpath(dst, OUT),
            "isolated_copy_byte_identical": sha(read(dst)) == sha(b),
        }

    # capture-time integrity anchors (declared snapshot scope only)
    for tag, rel in [("goal_ledger", "goal-ledger.md"),
                     ("mainline_state", os.path.join(AP, "pipeline-state.json")),
                     ("scaffold_state", os.path.join(AP, "state-handoff-R108/f-research-v1-state/pipeline-state.json")),
                     ("guard_ledger", "guard/ledger-null-ladder.json")]:
        b = read(rel)
        out["capture_time_hashes"][tag] = {"bytes": len(b), "sha256": sha(b),
                                           "mtime": stat(rel)["mtime"]}

    with open(os.path.join(OUT, "R121-RAW-v2.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("RAW-v2 written")
    print("taxonomy needles:", len(out["governing_review_taxonomy"]) - 1,
          "| misses:", [k for k, v in out["governing_review_taxonomy"].items()
                        if isinstance(v, dict) and "found" in v and not v["found"]])
    print("prior rounds:", len(out["prior_rounds"]),
          "| all readonly+notgate+notsci:",
          all(v["declares_readonly"] and v["declares_not_gate_pass"]
              and v["declares_not_scientific_result"] for v in out["prior_rounds"].values()))
    print("raise conditions satisfied:",
          {k: v["satisfied"] for k, v in out["raise_conditions"].items()})
    print("real graph any_true:", out["raise_conditions"]["a_real_graph_transfer"]["real_graph"])
    print("version-locked tex:", out["raise_conditions"]["b_strong_baseline_rerun"]["version_locked_main_tex"])
    print("validator:", out["machine_gates"]["validator"]["verdict"],
          out["machine_gates"]["validator"]["overall_score"],
          "| guard:", out["machine_gates"]["guard"]["verdict_lines"])
    print("new governing candidates:", out["numeric_overall_scan"]["new_governing_candidates"])
    print("isolated copies:", len(out["source_manifest"]))


if __name__ == "__main__":
    main()

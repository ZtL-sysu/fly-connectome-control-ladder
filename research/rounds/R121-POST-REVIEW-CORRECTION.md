# R121 · 独立复核后更正登记（只追加，历史正文与独立报告原文零改动）

**独立报告**：`R121-INDEPENDENT-REVIEW.md`，28,736 B / 237 行 /
SHA-256 `9650a024f84c9b1ec308db4a96c18fee26e5cfd67e3b73b0b9a50f1a0891200c`
（`shasum -a 256` 实算；复核者回报同值），mtime `2026-11-14 10:42:30`，一次写入、无中间态，
**原文一个字节都不改**。

**裁定**：`REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`。
A–H 十组从原始源字节用复核者自有逻辑独立复现 **全 MATCH**；
I 组 12 类点名夸大 / 自我认证 **CONFIRMED = 0（12/12 全 REFUTED）**；
J 组 **HIGH = 0，MEDIUM = 1，LOW = 3**，另 1 项已披露时点快照观察 + 1 项复核范围限制；
**无编造、无数据不一致**。复核者未把任何 R121 JSON / py / isolated 副本当数据源，
按要求在 A–I 结论形成后**最后**才读取轮次审计用于 J 对照。

**6 项全部接受，均以本文件只追加更正，不回写 `R121-ROUND-AUDIT.md` 原文。**

| ID | 等级 | 复核者指出 | 接受后的准确表述 | 是否改变核心结论 |
|:--|:--|:--|:--|:--|
| J-1 | **MEDIUM** | 审计 §1 与 §4.4 写「全项目行首数值 `**Overall:**` 14 行」，但 §4.4 标「只读 live」且写于 10:28，此时应为 **15 行 / 13 文件**；14 是唤醒时点（10:03）真值，当时本轮 `isolated/` 自产副本尚未生成。存在时点混用 + 全项目口径未声明排除自产副本 | **本轮主会话已实测确认当前 15 行 / 13 文件**。准确表述：唤醒时点（10:03）为 14 行；本轮 `isolated/` 逐字节副本于 10:24 生成后为 15 行 / 13 文件。两份晚于 r95 的文件（既有 `provenance/` 副本 + 本轮 `isolated/` 副本）**均与 r95 逐字节相同**，`new_governing_candidates = 0`、无新分值。`R121-verify.py` 的 H1/H1b 已把「既有一份」与「本轮自产一份」分列，核对口径本身正确；不精确在轮次审计的汇总措辞 | **否** |
| J-2 | LOW | §4.2「4 份 `SYNTHETIC_APPROXIMATION` 受控图为 `True`」——数量 4 正确，但严格说只有 **2 份**带 `data.source='SYNTHETIC_APPROXIMATION'`，另 2 份为 `p3_p4_taskaware/metrics_from_trajectory.json`（两 run）**无 `data.source` 字段**，是合成任务的 trajectory 镜像；另有 1 份 `r51_motif_survival/task_a_results.json`（`False`，无 source）未列举 | 接受标签口径收窄：准确为「2 份显式 `SYNTHETIC_APPROXIMATION` + 2 份合成 task-aware trajectory 镜像 = 4 份 `True`，另有 1 份无 source 的 `False`」。**6 份 `REAL_MALECNS_VISUAL_SUBGRAPH` 全 `False`** 的判定与 (a) `satisfied=False` 不变 | **否** |
| J-3 | LOW | §4.3「7/7 轮次全文均声明 `READONLY…`」——R120 复合 token 实为 `READ_ONLY_RECONCILIATION_…`（带下划线），字面不含 `READONLY` | 接受：准确为「7/7 轮次全文均声明**只读语义**（`READONLY…` 或 `READ_ONLY…`）+ `NOT_GATE_PASS` + `NOT_SCIENTIFIC_RESULT`」，属命名泛化，`R121-collect-v2.py` 已同时匹配两种拼写 | **否** |
| J-4 | 观察项（**已披露，非缺陷**） | `isolated/` 21 份中 20 份与当前源文件逐字节相同；仅 `goal_ledger__goal-ledger.md`（687,472 B @10:24）与当前 `goal-ledger.md`（697,046 B @10:34）不同，但**前 687,472 B 逐字节相同**、尾部纯追加 +9,574 B R121 账本段 | 审计 §3 已明示「采集时刻快照口径，不覆盖采集后只追加记账造成的时间差（R119 M2）」⇒ 该项**已披露**，且反向佐证 I 组 (f)「R121 未改写任何历史字节」。无需新增更正 | **否** |
| J-5 | 范围限制（非缺陷） | 复核者按约束不得把任何 R121 JSON 当数据源，故 `R121-VERIFICATION.json` 内部「74/74」条数未独立核验；只能确认审计中可与源字节对照的 A–H 事实全 MATCH | 接受并明确边界：**74/74 是同机 verifier 的必然一致性核对，本就不构成独立交叉核验**（审计 §3 与 `R121-verify.py` 的 `scope_note` 已逐字声明）。真正独立的是本次 A–H 复核；J-5 不是审计瑕疵、也不削弱 A–H | **否** |
| J-6 | LOW | 审计第 4 行把 governing 概述为 `` `**Overall:** 6 \| Scholarly Confidence 4` ``，相对 r95 :419 逐字（双空格 + `**Scholarly Confidence:**` 粗体）是改写式摘要而非逐字引用 | 接受：准确逐字形式为 `**Overall:** 6  | **Scholarly Confidence:** 4`（审计 §4.1 表格已给出正确形式）；第 4 行属状态概述、非引文 | **否** |

## 复核者补充澄清（一并登记）

- §5「否定性闭环」结论由 r95 原文 + (a)(b)(c) 全 `False` + 七轮只读自述支撑，
  明确限定为「**这类只读审计**」，并指出唯一 admissible 路径仍是 P3 真实前向后的
  全新隔离 full 评审 ⇒ **复核者未发现 overclaim**。
- `r39_visual_task/metrics.json` 中的 `cuda_device: "NVIDIA GeForce RTX 4090"`
  是既有实验的设备元数据（mtime 11-08），**不是 R121 的能力主张**。
- §6 边界逐条与 I 组 12 类 REFUTED 一致。

## 结论与边界不变

- 更正全部为**措辞 / 口径 / 时点 / 标签精度**收窄，不改变任何一手测量数字、
  字节完整性、三项升分条件 `False`、双门读数、门状态、governing 或否定性闭环结论。
- `R121-ROUND-AUDIT.md` 原文、`R121-INDEPENDENT-REVIEW.md` 原文、
  v1/v2 RAW 与 VERIFICATION、`isolated/` 副本、第十四检查点字节 **全部零改动**。
- 这是**门 / 证据层复核，不是 `ccf-paper-reviewer full` 稿件评审**；
  无 `**Overall:**` 数值行、不改 governing、不产生科学结果、不做前向。
- **0 篇达标，未写 COMPLETE**；governing 仍 **R95 = 6.0 / Confidence 4.0**，
  `NOT_QUALIFIED` / `INCOMPLETE`；G0 pending、零门晋级 / 零自我认证 / 零状态改动；
  心跳 ACTIVE 调度无变化。

# R121 轮次审计（心跳 · 2026-11-14 10:02–10:3x +0800）

**性质：`READONLY_SUCCESS_CRITERION_CLOSURE_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`**
**governing 仍 R95 = `**Overall:** 6 | Scholarly Confidence 4`，`NOT_QUALIFIED` / `INCOMPLETE`；0 篇达标，未写 COMPLETE。**

---

## 1. 第 0 步：并发保护（不触发）

| 检查 | 读数 |
|:--|:--|
| `goal-ledger.md` mtime | `2026-11-14 08:57:51`（epoch `1794617871`）；唤醒 `10:03:40`（`1794621820`）⇒ **65.8 min > 10 min** |
| 近 10 min 写入 | 无（本轮产物创建前） |
| 进程扫描 | 仅本自动化会话自身 `codebuddy --serve --session-id d961f1bb…`（10:02:30 启动）+ WorkBuddy 宿主；**无独立主会话 / novix 轮询 / tracker / runner** |
| `ccfa-review-reports/` | 最新仍 `paper-null-ladder-r95-…-20261111.md`（11-11 15:01） |
| `ccfa-idea-review-reports/` | 最新 11-10 |
| 数值 `**Overall:**` 行（全项目 md，行首） | 14 行；晚于 r95 的仅 1 份 = `provenance/` 下 r95 **逐字节副本**；`new_governing_candidates = []` |
| R121 产物 | 唤醒前全项目无 `*r121*` ⇒ **本轮首次唤醒** |

⇒ 主动推进。无未登记异步 full 评审，governing 不变。

## 2. 换道理由（RGE4）

R114–R120 连续七轮各审计一层**流程 / 基础设施**：gap-1 一手取证、Zenodo 归档字节、
P3 执行前提、来源登记缺口、评审启动协议、常驻指令↔落盘状态对账、决策债合并。
R105 / R107 / R109 已三次判停「继续产出证据文档」同构循环；R120 把决策债去重为
10 组（最小可解锁集 `G1+G4+G10`），并交下轮逐项裁决。

**本轮换道**：不再新增第 8 层流程审计，也不写第 N 份 G0 文字补丁、不碰须批准的机器门、
不起 P3 前向、不创建 v4 契约。改做**前 120 轮未做、且离成功标准最近**的一层：
把**唯一 governing 独立 full 评审（R95）自己的升分 / 不升分判据**，与
① 七轮产出的自述类别、② 三项升分条件的一手证据状态、③ 两道机器门、
④ 有序门链，做逐条字节对账。

- 这不是「再写一份证据文档」：其结论是**否定性闭环判定**（见 §5），
  即由 governing 评审**自身规则**证明 R114–R120 全部落在 §13「No quick change」类，
  因此**结构上不可能**把 Overall 从 6.0 抬到 7.0。
- 采信优先级：评审原文字节 > 一手 JSON/TeX 字节 > 活配置 > 轮次自述。
  不采信任何自评、不注入期望分、不起 `ccf-paper-reviewer full`。

## 3. 方法（只读，EXEC LOCK）

`R121-collect.py`（v1，留痕）→ `R121-collect-v2.py`（修正两处判定缺陷）→
`R121-verify.py`（**不 import 采集模块、不读任何 R121 JSON**，从源字节独立复算）→
`R121-VERIFICATION.json` = **74/74 MATCH / 0 MISMATCH**。
`isolated/` 21 份源字节逐字节副本；`R121-SOURCE-MANIFEST` 内嵌于 RAW-v2。

- 本机 conda：`/Users/xhf/miniconda3/bin/python`（Py 3.14.6）。
- **零网络、零前向 / 推理 / 训练 / 标签 / EPE·l2 / 科学指标**；npz/权重/数据一律不读内容。
- 双门在 run root 落只读报告（`R121-guard-report.md`），不写 `/tmp`（R120 教训）。
- 采集时刻四份结构权威 SHA 见 `R121-RAW-v2.json::capture_time_hashes`；
  「SHA 前后一致」为**采集时刻快照口径**，不覆盖采集后只追加记账造成的时间差（R119 M2）。

## 4. 一手读数

### 4.1 governing 评审自身的判据（18 条字节 needle 全命中）

| 位置 | 原文要点 |
|:--|:--|
| :419 | `**Overall:** 6  | **Scholarly Confidence:** 4` |
| :450 | `**No quick change**` —— 流程 / 披露 / 格式「**不新增支持中心主张的科学证据**」⇒「**不改变 evidence-capped overall**」；行政 blocker 解除仅恢复「可提交」状态 |
| :448 | Raise score 三项 (a)(b)(c)；「单项 +0.5；三项齐备 Overall 6→7~7.5」 |
| :473 | `Raising the score would require: 真实图上确认 motif-survival 阈值迁移` + 强基线复跑 + 一项真实视觉任务改变实际结论 |
| :240 / :249 | M1「需新的真实图实验确认机制迁移（**非 prose 可修**）」；M2「**无法靠 prose 补出视觉贡献**」 |
| :413 / :414 | Evidence `3`、Significance `3` |
| :454 | tie-breaker：「这组 ≥3 个决定性关切不允许 Overall 上到 7」 |

### 4.2 三项升分条件的一手状态（全部 `satisfied=False`）

| 条件 | 一手证据 | 判定 |
|:--|:--|:--|
| (a) 真实图机制迁移 | 6 份 `REAL_MALECNS_VISUAL_SUBGRAPH` metrics 的 `hypothesis_supported` **全 `False`**；另有 4 份 `SYNTHETIC_APPROXIMATION` 96 节点 XOR / task-aware 受控图为 `True` —— 正是 M1 明确不计入的替身 | **未满足** |
| (b) 强基线复跑 | R95 版本锁定稿件 `R49-7.5-DELIVERY/manuscript/main.tex` = 40,175 B / md5 `e4bfad51ad834fdccdb6db7821e158c6`（与 R95 §1 版本锁逐字一致），:637 逐字 `We did not rerun their flyvis stack and make no benchmark-reproduction claim.`；全项目 flyvis/toposens **复跑指标文件 0 份** | **未满足** |
| (c) 真实视觉任务改变结论 | `r39_visual_task/metrics.json`：`mlp_baseline.mean_acc = 0.97222…` 主导；`real − degree_preserving_null` delta `−0.000463`，CI95 含 0；R95 §8 M2 记为**负结果** | **未满足** |

> 两处防误判（v1 缺陷留痕见 `R121-V1-DEFECTS.md`）：把 synthetic 的 `True`
> 当成真实图会造出「(a) 已满足」的假阳性；把 v2 run root 的 45,618 B `main.tex`
> 当作被评版本会造出「(b) 无基质」的假阴性。

### 4.3 七轮产出 vs. 评审自己的分类

7/7 轮次全文均声明 `READONLY…NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`；
7/7 `claims_new_positive_evidence=False`、`claims_gate_passed=False`、
`numeric_overall_line_count=0`。⇒ 按 R95 :450 的「No quick change」定义，
这些产物属透明度 / 可核验性层，**不新增支持中心主张的科学证据**。

### 4.4 双门与有序门链（只读 live）

- validator `NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`（`score_meets_threshold=false`；D1✓ D2✗ D3✗ D4✓ D5✗）。
- guard `INCOMPLETE`（A2、A6 FAIL；S1–S7 全 7 pending；动作序列 0 条）。
  A6 报告文本仍 ledger 口径「严格 > 8.0」= R109/R111 已登记**双口径已知问题**，只读登记不改。
- 主线 `pipeline-state.json`：12 阶段，`CCFA-startup=passed`，
  **G0–G8 / validation / handoff 全 `pending`，`inputs=[]`、`evidence=[]`**。
- 全项目行首数值 `**Overall:**` 14 行；晚于 r95 的 1 份为逐字节副本 +
  本轮 `isolated/` 自产副本 1 份（v2 已分列）；**新 governing 候选 = 0**。

## 5. 否定性闭环判定（本轮唯一实质结论）

由 governing 评审**自己的规则**而非主会话判断：

1. 成功标准（R107 用户授权终值）= 一份**全新隔离独立 `ccf-paper-reviewer full`** 报告，
   唯一一行 `**Overall:** X | **Scholarly Confidence:** Y`，`X >= 7.0`，
   且 validator `QUALIFIED` + guard `COMPLETE`；主会话 / 自评不算；最新独立 full 评审 governs。
2. R95 :448/:473 规定 Overall 由 6 上移只能靠 (a)(b)(c) 三项**新科学证据**；
   :450 明确流程 / 披露 / 格式**不改变 evidence-capped overall**；
   :240/:249 明确「非 prose 可修」「无法靠 prose 补出视觉贡献」。
3. §4.2 三项 (a)(b)(c) 一手状态**全部未满足**；§4.3 七轮产出全部落在 :450 类别。
4. ⇒ **R114–R120 及本轮这类只读审计，结构上不可能把 governing 6.0 抬到 >= 7.0**。
   这不是进度慢，是判据层面的不可行。R105/R107/R109 三次「同构循环」判停
   到此有了来自评审原文的字节级依据。
5. ⇒ 唯一 admissible 路径仍是：按序 G0–G8 → validation → handoff → P0 →
   P1A/P1B → P2 → **P3 baseline-first 真实前向**取得实质正向新证据 →
   稿件**新副本目录** → 9 页合规编译 → 全新隔离 full 评审。
   门槛降低（8.0→>=7.0）**不降低证据质量**，也不改变 :448/:473 的证据性要求。
6. 阻塞点仍为 R120 `R120-CONSOLIDATED-DECISION-REGISTER.md` 的
   `G1+G4+G10`（交付对象 / 门路径、G0 判据 + 独立判定方、≤32h / K=45 confirmation 面板），
   全部须 designated gate owner / 用户裁决；心跳不自我认证、不自行回写 state / 矩阵 /
   registry / 门配置、不自行创建 v4、不在 G0 未过时启动 P3。
   D1 判别性预测维持 `BLOCKED_ON_CONFIRMATION`。

## 6. 边界（逐条）

`READONLY_SUCCESS_CRITERION_CLOSURE_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`。
零门晋级、零自我认证、零状态写回（G0 仍 pending）；未改历史字节 / 评审 / 分数 / 阈值 /
稿件 / 门 / 冻结件 / 矩阵 / registry / 门配置；未起 `ccf-paper-reviewer full`、
未产生新的 `**Overall:**` 数值行、未自评 governing、未跳门、未创建 v4、
未假定 `≤32h / K=45` 授权、无 4090 / L4 / H20 能力主张；EXEC LOCK；
主项目未投稿 / commit / push；心跳 ACTIVE 调度无变化。

## 7. 结果

第 3 步前置（实质正向新科学证据）**未满足** ⇒ 不进稿件、不编译、不起 full 评审。
**0 篇达标，未写 COMPLETE**；governing 仍 **R95 = 6.0 / Confidence 4.0**，
`NOT_QUALIFIED` / `INCOMPLETE`。停止门只剩 ①达标（>= 7.0）②用户叫停。

# R106 — G4（Novelty / Non-Duplication）精确差异化陈述

状态：`POSITIONING_ANALYSIS_ONLY_NOT_SCIENTIFIC_RESULT`。
**G4 维持 `pending` 且风险等级上调，本文件不宣称 G4 通过、不产出任何科学结果。**
依据：`f-guidance-builder-v1/references/fail-fast-gates.md` §G4 —— 「If related
papers exist but do not duplicate the core contribution, write the difference as a
precise positioning statement.」

## 1. 判定所依据的四篇一手 prior art（均已独立复核）

| 文献 | 已发表的、与本方向重叠的内容 | 重叠维度 |
|:--|:--|:--|
| **Kuklev 2026**, `arXiv:2609.24565v2` | 冻结 connectome 视觉前端在**真实视觉任务**上严格匹配的图 null（degree / type-pair+sign / ER）、3 seeds、带置信区间的大幅正向效应（`+0.318 [0.296,0.339]` 等）、R7/R8 正对照、预注册 held-out；**外加 v2 新增的时间尺度 sweep**：观测跨一个周期后 circuit 反超 receptors-only（`+0.033 [0.015,0.050]`），且明确该反转**不经 T4/T5** | 方法族（connectome-constrained 冻结视觉模型）、任务类（视觉）、中心 claim（wiring load-bearing）、实验协议（matched null + 正对照 + prereg）**四项全中** |
| **Park 2026**, `arXiv:2609.39248v1` | 十 seed 预注册、boundary-preserving vs degree-preserving null、dose / sham 阶梯、匹配 swap 数的 sham 对照、注册等价预测失败并如实报告 | null 语义与对照设计 |
| **Dhawan / FlyHack 2026**, `arXiv:2610.13018` | flyvis 50-model 集成、task-matched CNN、intervention / attribution 对齐、结论须 scope 到 model family / intervention / representation / trained solution；**指出官方 checkpoint 的 launch-time split 不可恢复** | 同一模型族、同一类干预、同一「机制结论有效性」问题 |
| **Correig-Fraga 2026**, `arXiv:2610.10023` + 2026 几何研究（**后者本轮未独立复核，保留 R99 状态**） | eye geometry / wiring cost 下的结构对照；训练到 task adequacy 后 real-vs-null 表征几何差异大幅收窄，一例完全闭合 | 「competence-conditioned null」这一 framing 已被接近 |

## 2. 精确差异化陈述（写清楚「不是什么」，比写「是什么」更重要）

冻结契约的候选方向是：在**冻结且 competent 的官方 flyvis optic-flow 函数**上，
用 **response-conditioned / path-preserving rewiring null**，配合**密封预测**
（sealed forecasts）与 dose / common support / geometry balance / control separation。

与 Kuklev v2 的**可核验差异**只有以下三条，且不夸大：

1. **输入与任务不同**：Kuklev 是建筑图纸上的 prescribed drift → hatch matching /
   wall segmentation；本方向是 Sintel 渲染 optic flow，用官方 flyvis 的 734 参数
   循环网络与 flow decoder。Kuklev 的「路径重要」结论是在**非 optic-flow** 的
   下游读出上得到的。
2. **null 的构造条件不同**：Kuklev 的 null 是 degree / type-pair / ER 图重写；
   本方向的 null 以**冻结原始响应**为条件、在 compat block 内做有限候选匹配
   （`response_null_ops_v2.py`），目的是把「响应差异」与「几何/幅度差异」分离。
   但必须注意：**Park 已证明 null 保留什么决定结论**，所以这条差异本身
   **不是 novelty 保证**，反而要求本项目补上同等严格的 sham / dose 对照。
3. **机制问题不同但被 v2 明确点名**：Kuklev §8 留下
   `The remaining question is which stage integrates the extra time, and a
   per-type tuning analysis over the sweep would answer it.`。
   本方向的 per-type / response-conditioned 分析在原则上可以回答它。

### 必须同时写下的反向限定（不掩饰）

- **R99 提出的换道轴「判别性预测何时路径重要 vs 输入即够」已被 v2 部分抢发**：
  判别变量（观测是否跨周期）、效应量与方向、以及「不经 T4/T5」的阴性机制结论
  都已发表。因此该轴**不能**再被写成「回答一个开放问题」，只能写成
  「在 optic-flow 上复现并做机制归因」。这**加重** G4 风险。
- Kuklev 的 sweep 已自带严格性警告：绝对数值不可跨配置比较、只有 sweep 内差异有效、
  long-look 初次尝试因 pooled area 与 observation length 同时改变而 confounded、
  作者自称 prediction「half held」。任何借用该轴的工作必须继承这些限定。
- Dhawan 指出官方 flyvis checkpoint 的 launch-time split 不可恢复 ⇒
  本项目的 TEST 标签扣留与 held-out 语义问题是**真实且已发表的障碍**，不是可略过的细节。
- 本项目**至今没有任何真实模型前向**、没有 competence 证据、没有 null 结果。
  U5（真实 FlyVis decoder / rewired recurrence / `delta_noise` 端到端）仍 UNVERIFIED。
  定位陈述是**计划**，不是结果；按 G4 不能拿计划当差异化证据。

## 3. 四个阻塞维持不变（与 `R99-design-block-decision.md` 一致）

| 阻塞 | 状态 |
|:--|:--|
| 功效：16 clip units / 4 scene clusters，N ~10+ 列近饱和；4 簇 bootstrap 仅约 35 个不同重采样，95% LB>0 几乎不可达 | **未解决** |
| TEST 标签扣留 / `prospective-identities-v1.json` 无 split/holdout 字段 | **未解决**，且 Dhawan 的 split 不可恢复结论使其更严重 |
| ≤32h / K=45 confirmation 面板**用户未授权** | **未授权**，本轮不假定、不询问、不启动 |
| scientific null runner 与 predictor 的完成 / 隔离 / 独立审计、G0–G8 有序门 | **未完成 / 全 pending** |

**因此：G4 维持 `pending`，风险由 R99 的「high」上调为「high + 判别轴已被部分抢发」。
本轮不做任何修复提案、不出 v3/v4、不重开 D1 补丁循环。**

## 4. 对主线第 2 步的实际含义（这是本轮换道的落点）

用户 16:31 要的「视觉的正面的一个效果」**不能靠再出一个正数来达成** ——
Kuklev 已经有 `+0.318`，且它的 v2 连「何时」都给了部分答案。按用户底线
「正向效果必须真实测出，不能补出来」「阴性照报并换道」，唯一站得住的路径是：

- 先把**有序门**走完：G0（本轮补正 + 独立 gate review）→ G1–G8 → validation →
  handoff → f-research-v1 P0 → P1A/P1B → P2 → P3 baseline-first；
- P3 的**真实前向**是 U5 与所有定位陈述的物理前提，且本机 MPS 与 FlyVis 默认 cpu
  device 的适配、Sintel 8 clips、官方 model000/001 资产已由本轮只读盘点确认**齐备**；
- 在**不跳门**的前提下，先做出真实、有限、可独立复算的 competence / null 证据，
  再由证据决定 claim 的范围；若结果为阴性，照报并再次换道。

本轮**没有**跨过任何一个门，也**没有**产生可用于稿件的正向证据。

## 5. 红线

不把「文献核对吻合 / arXiv 可访问 / 资产齐备 / 本机可 import」包装成科学结果或
4090/L4 能力；不改任何已落盘报告、评审、分数、阈值、冻结件、gate 状态；
不自行打分、不自评当 governing；不起 `ccf-paper-reviewer full`；
不假定 confirmation 授权；零前向 / 零训练 / 零标签 / 零数据集；
未投稿 / commit / push。

# R106 — G0 文献证据独立复核（主会话侧记录，非独立 gate review）

状态：`LITERATURE_VERIFICATION_ONLY_NOT_SCIENTIFIC_RESULT`。
日期：2026-11-13 03:2x +0800。自动化心跳 `b88e368e` 第 R106 轮。

> **性质界定（防止口径漂移）**：本文件是**主会话侧**的一手文献复核记录，
> **不是** `ccf-paper-reviewer full` 稿件评审、**不是** G0 gate owner 的独立审查，
> **不产生任何分数行**、不改变 governing（仍 R95 = 6.0 / NOT_QUALIFIED / INCOMPLETE）。
> 本轮另起全新隔离子代理做 G0 gate review，其报告单独落盘、原文不改。
> 本文件**不标 G0 passed**，不晋级任何门。

## 0. 为什么做这件事（换道原因）

R105 已判定并停止 R101–R105 连续五轮的「实现 → 验收脚本 → 独立核验 PARTIAL →
新 DEFER → 下轮补丁」循环，把资源移回主线第 2 步。用户指令明确：
「按序推 G0–G8（每门各自实质证据与独立审查）」「别在提案文字上继续空转」。
R98 的 G0 证据审查列出 4 个缺口，其中第 3 条为「本会话未跑新文献检索；
按 f-guidance-builder-v1，recency 必须由 gate owner 独立确认」。R99 做了 live web
check 并发现 Kuklev 2026，但那是主会话侧检索，且 R98 明确写「a main-session read
of an existing matrix is not an independent gate review」。

本轮因此：① 用**独立的一手来源**复核 R99 所引 prior art 的数字与结论口径；
② 把复核结果作为 G0 的实质证据补正落盘；③ 起全新隔离子代理做独立 gate review。
不做 predictor v4、不重开 D1/判别式 v3 补丁循环、不假定 ≤32h/K=45 confirmation 授权。

## 1. 复核方法与来源（可复现）

| 项 | 内容 |
|:--|:--|
| 检索 | 独立 web 检索，关键词保留 arXiv 编号与原标题；未采信 R99 的任何转述数字作为输入 |
| 一手全文 | `https://arxiv.org/abs/2609.24565`（v1/v2 版本历史）、`https://arxiv.org/html/2609.24565v2`（v2 正文 Table 1–6 / §5 / §7 / §8 / §9） |
| 对照文献 | `https://arxiv.org/abs/2609.39248v1`（Park 2026）、`https://arxiv.org/abs/2610.13018`（Dhawan / FlyHack 2026） |
| 本地证据冻结 | `R106-G0-EVIDENCE-FREEZE.json`（8 份字节 SHA + `pipeline-state.json` 门状态快照） |
| 未做 | 未重新验证 2026 几何研究那条 secondary hit（aimedicalcompendium）；保留 R99 记录状态，**不宣称已复核**。未下载/重跑任何第三方代码。未做任何模型前向。 |

## 2. R99 数字的核对结果：**全部逐字吻合**（不掩饰也不夸大）

R99 `gate-G0-recency-review-R99.md` 记录的数字，在 v2 正文 §7.1 / §7.2 / Table 3 中
逐条找到一手出处：

| R99 记录 | v2 一手出处 | 判定 |
|:--|:--|:--|
| intact `0.857` | §7.1 hatch matching rewiring 基线；Table 1 `Fly + drift (P,R) 0.857` | 吻合 |
| degree-preserving `0.539`，`+0.318 [0.296,0.339]`，3 seeds | §7.1 逐字：`drops accuracy from 0.857 to 0.539 ... paired differences of +0.318 [0.296,0.339] ... over three rewiring seeds` | 吻合 |
| type/sign `0.586` / `+0.271 [0.248,0.293]` | §7.1 | 吻合 |
| ER `0.500` / `+0.356 [0.334,0.379]` | §7.1 | 吻合 |
| 45,669 节点 / 1,513,231 边 | §7.1 | 吻合 |
| 分割 `0.483 → 0.089` IoU、`0.964 → 0.514` ROC-AUC、`0.397 [0.365,0.431]` | §7.1 逐字 | 吻合 |
| R7/R8 正对照 `0.092 [0.079,0.104]` | §7.1 逐字 | 吻合 |
| held-out `receptors-only 0.894 > fly 0.835` | Table 3 `Receptors only (P,A,R) 0.894` / `Fly + drift (P,A,R) 0.835` | 吻合 |
| CNN raw receptors `0.961` ≈ fly 前端 `0.962` | §7.2 逐字 `yields 0.962 ... on raw receptors yields 0.961` | 吻合 |
| held-out split **未**用于 rewiring nulls | §7.1 `on the development split, since the held-out split was opened only for the model comparison`；§3.2 / §5.4 一致 | 吻合 |
| T4/T5 可沉默 | Table 6 / §7.2 | 吻合 |

**结论：R99 没有编造数字，也没有把 development 与 held-out 混淆。**

## 3. 但 R99 有两处**实质遗漏**（本轮核心发现）

### 3.1 R99 引用的是 **v1 的结论表述**，v2 已修订

arXiv 提交历史（`/abs/2609.24565` 逐字）：
`[v1] Mon, 21 Sep 2026 13:30:30 UTC`；`[v2] Tue, 22 Sep 2026 12:24:47 UTC`，
v2 是 `Major revision with a preregistered held-out evaluation, matched graph nulls,
temporal sampling controls, real-drawing evaluation`。

R99 引作该文结论的句子 *"Exact structure remains insufficient to beat what the
moving retina already provides"* 出现在 **v1 摘要**（检索结果 #1 的 PDF 文本）。
**v2 摘要不含该句**，改为：

> "Yet the intact circuit does not beat its moving retina, and T4/T5 silencing
> leaves both tasks intact. **Longer observations reverse the circuit-receptor
> ordering once the stimulus spans a period, but not through T4/T5.** Thus active
> sampling and exact structure matter, while clean-data practical performance
> remains dominated by task-trained networks and the useful transfer margin is
> largely retinal."

R99 的 G0 报告写的是 `arXiv:2609.24565v2`，却引用了 v1 的收束句，且未记录 v2 新增的
时间尺度反转。这不是数字错误，是**结论口径的版本错配**。

### 3.2 v2 §7.3 / §8 已给出「何时保路径重要 vs 输入即够」的**部分答案**

R99 把「*A result that predicts **when** path-preserving controls matter (vs when the
input alone suffices)*」列为尚开放、可作为换道方向的问题。v2 已经用预注册 sweep
部分回答了它。§7.3 逐字：

> "Holding the pooled area fixed and varying only the number of analysed frames
> settles part of it. With the pool frozen, the circuit trails the receptors-only
> descriptor by `0.011` at eight frames and leads it by `0.018`, `0.021` and `0.022`
> at twenty, thirty-four and sixty, so **the ordering reverses once the observation
> runs past a single period**; the change from eight frames is `+0.033 [0.015,0.050]`.
> The gain comes from the receptors degrading with length while the circuit holds,
> which is what a recurrent stage that integrates over time should do. Spectral
> bands are worth `+0.085` to `+0.102` at every length, so the frequency content is
> real. **The mechanism, however, is still not the one we proposed: the T4/T5
> contribution does not grow with observation length**, at `+0.008 [−0.003,0.018]`,
> whereas silencing eight random types separates from the intact circuit only at
> the longest window, by `+0.034 [0.022,0.046]`. These runs use a wider pool and a
> smaller eye than the headline configuration, so their absolute values are not
> comparable with the rest of the paper; only the differences within the sweep are."

§8 逐字：

> "That prediction was run, and it half held. ... **But the mechanism is not the one
> we named: the T4/T5 contribution does not grow with length. The remaining question
> is which stage integrates the extra time, and a per-type tuning analysis over the
> sweep would answer it.**"

§7.3 还给出了机制解释的前提（§7.2 / §9）：短窗口 `0.16 s` 内刺激只走完约
`1/5 ~ 9/10` 个空间周期，`"A frequency cannot be estimated from less than a period"`；
long-look 初次尝试因同时改变了 pooled area 而 confounded，§8 明确只把 sweep 内的
差异当作有效。

**对 G4 的后果（不淡化）**：R99 建议的换道轴「判别性预测何时路径重要」，
其**判别变量（观测时长是否跨周期）、效应量（`+0.033 [0.015,0.050]`）以及
一个阴性机制结论（不经 T4/T5）都已被 v2 发表**。因此该轴不再是「回答一个开放问题」，
而是「复现并解释一个已发表的、且作者自己承认只 half held 的结果」。
这**加重**而非减轻 G4 prior-art 风险。详见 `R106-G4-POSITIONING.md`。

## 4. 同时复核的另两篇 prior art（均为真实、非编造）

| 文献 | 一手核对要点 | 对 G4 的含义 |
|:--|:--|:--|
| Park 2026, `arXiv:2609.39248v1`（2026-09-30）, Zenodo 22891264 v4.0 | 十 seed 预注册；标准 degree/column null 把 `10.6–10.7%` 嗅觉输出直连下行运动组（connectome 为 `0.012%`）；保 sensory-motor 边界的 null 使 connectome 差异落入 `±0.10` 等价界（`+0.002` / `−0.074`）；加 shortcut 的干预 `+0.44`（10/10 seeds）、full dose 领先同 swap 数 sham `+0.53`（10/10）；**sham 的注册等价预测失败并如实报告为失败** | 「null 保留了什么」决定结论，且**匹配 swap 数的 sham** 是必需对照。这与冻结契约里 control separation / geometry balance 的要求同源 |
| Dhawan / FlyHack 2026, `arXiv:2610.13018`（2026-10-12） | flyvis 50-model 集成 + task-matched causal CNN；参数匹配 CNN 的对抗方向反转差距在大 CNN 上基本消失；edge attribution patching  pooled AUROC `0.970` / Spearman `0.872` vs 零对齐 `0.933` / `0.126`；贪心 T4/T5 细胞类型集在 50 模型中 25 个达标、加双侧响应幅度检查后 6 个里只剩 2 个；**明确写 released flyvis 模型的 launch-time split 不可恢复，故共同评测只是描述性** | 机制结论须 scope 到 model family / intervention / representation / trained solution；**且直接指出官方 checkpoint 的 split 不可恢复**——这与本项目冻结尾 `official-model-input-identities` 与 TEST 标签扣留问题正面相撞 |

> 注：Dhawan 摘要含 "AI assistants were used for software development and manuscript
> editing..." 的披露，如实照录，不作评价。

## 5. 本轮不做的事（红线逐条）

- **不标 G0 passed**。R98 明确写「Marking it passed from this review alone would
  violate 'Never skip, reorder, or infer completion' and would be stale-evidence
  promotion」；且 R98 的 gap 1（若干条目 asset/license/code path 未逐一验证）、
  gap 2（矩阵须 final）、gap 4（scientific/visual gate judgment）**均未闭合**。
- 不改 `literature-baseline-matrix.md`、`gate-G0-recency-review-R99.md`、
  `gate-G0-evidence-review-R98.md` 任何一个字节（本轮是**新增补正**，不回写历史）。
- 不改 `pipeline-state.json`、任何 gate 状态、任何分数/阈值/冻结件、任何稿件或评审。
- 不把「文献核对吻合」「arXiv 可访问」包装成科学结果、模型前向、competence 或 4090/L4 能力。
- 不重开 D1 / 判别式预测 v3 补丁循环（已 `BLOCKED_ON_CONFIRMATION`）；
  不假定用户已授权 ≤32h / K=45 confirmation 面板。
- 零前向 / 零训练 / 零标签 / 零数据集；未投稿 / commit / push。

## 6. 交 G0 gate owner 的实质输入

1. 本文 §2 的数字核对表（R99 数字可用，但须标注来源为 v2 §7.1/§7.2/Table 3）。
2. 本文 §3 的版本错配与 v2 新增时间尺度 sweep —— **必须并入 G4 定位**，
   否则矩阵仍是 stale 的。
3. `R106-G4-POSITIONING.md` 的精确差异化陈述与「未被抢发的最小剩余问题」。
4. `R106-G0-EVIDENCE-FREEZE.json` 的 8 份字节 SHA 与门状态快照。
5. 未闭合项如实保留：2026 几何研究 secondary hit 未复核；矩阵中若干
   asset/license/code path 标注仍未逐一验证；无独立 gate owner 审查结论前 G0 保持 pending。

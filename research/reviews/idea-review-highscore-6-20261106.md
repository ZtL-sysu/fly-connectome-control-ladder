# CCFA idea review — 6 个面向 8/10 门槛的候选（2026-11-06）

> 项目：`fly-gnn-snn-vision`｜候选卡片：`docs/ccfa-highscore-idea-cards-20261106.md`
> 模式：`ccf-idea-reviewer` **standard**（`ccf-common/references/task-modes.md` §standard）
> 协议：`ccf-idea-reviewer/SKILL.md`、`references/rubric.md`、`calibration.md`、`strict-idea-review.md`、`expert-panel.md`；`ccf-common/references/review-output-standards.md`

## 0 判读前必须看清的四条

1. **这是诊断性评分，不是达标声明。** 按项目纪律，只有本地 `ccf-idea-reviewer` standard 落盘报告 + 只读校验脚本解析的 `**Overall:** X` 才进入达标计数；本报告**不计入** `qualified_papers.json`、不触发 guidance、不授权跑实验。
2. **分数不是接收概率**，且必须与 fatal risks、检索状态、development potential 一起读（`rubric.md` §Quantitative Feedback）。
3. **三值分离**：criterion score（1–5）/ Overall（1–10，= weighted × 2）/ Confidence（High·Medium·Low）。低置信不自动降分，只降确定性。
4. **Novelty grounding 只是 partial**：本轮做了 7 次公开关键词检索，每个簇只拿到 1–3 条一手来源且多停留在摘要层，未达到 standard 要求的 3–8 条逐条核验。按 `strict-idea-review.md` §Score Guardrails，**novelty 一律封顶 3**（I6 因该子领域完全未检索给 2）。这直接决定了本轮不可能出现 >8/10 的诚实分数。

## 1 汇总（先独立打分，后按 serious-risk-adjusted 排序）

| 排名 | idea | weighted (1–5) | **Overall (1–10)** | Confidence | Fatal gate | Recommendation | 到 8.0 所需加权点 |
|---:|---|---:|---:|---|---|---|---:|
| 1 | I1 `null_ladder` | 3.54 | **7.08** | Medium | 无 | pivot-with-rescue-route | +46 |
| 2 | I5 `energy_pareto` | 3.40 | **6.80** | Medium-Low | 无 | pivot-with-rescue-route | +60 |
| 3 | I2 `merging_partition` | 3.38 | **6.76** | Medium-Low | 无 | pivot-with-rescue-route | +62 |
| 4 | I3 `spectral_ssm` | 3.18 | **6.36** | Low | 无 | pivot-with-rescue-route | +82 |
| 5 | I6 `continual_isolation` | 3.06 | **6.12** | Low | novelty 2 + 未检索 → needs-literature-search | pivot / needs-search | +94 |
| 6 | I4 `onoff_restoration` | 3.04 | **6.08** | Low | feasibility 2 且固定期限 → 封顶 pivot | pivot-with-rescue-route | +96 |

**达到 >8/10 门槛的：0 / 6。** 最高 7.08（I1），仍比门槛低 0.92 分。全部 6 个落在 `pivot-with-rescue-route` 带（3.0–3.6），没有一个进入 `revise`（3.7–4.2）或 `accept-to-develop`（4.3–5.0）。

加权公式与实算：`weighted = Σ(维度分 × 权重)/100`，`Overall = weighted × 2`；10 个维度分与「达到 8.0 所需增量」均用 `/Users/xhf/miniconda3/bin/python` 实算复核，不是估分。

**与项目历史对照**：既有十余个已评审 idea 最高 6.28/10（`idea_causal`、looming 桥接并列），本轮 I1/I5/I2 因问题更锋利、且直接对准 2604.04033 自述缺口，诊断分略高，但**仍未过门槛**；项目 0/5 达标状态不变。

## 2 逐 idea 评审

### I1 `null_ladder` — 高阶结构零模型阶梯

| Dimension | W | Score | Conf. | Deduction / evidence basis / repair condition |
|---|---:|---:|---:|---|
| Problem importance | 12 | 4 | 4 | — |
| Novelty vs prior work | 14 | 3 | 3 | 2604.04033 已用保度零模型做控制阶梯；修复：完成 3–8 条一手核验，证明「高阶零模型 + 长时程 + 多任务」无人做过并取得可预测指标 |
| Conceptual innovation | 12 | 4 | 3 | — |
| Method soundness | 14 | 4 | 3 | — |
| Elegance | 8 | 3 | 3 | 嵌套零模型阶梯的层级定义可能任意；修复：预注册每阶匹配的统计量与等价性检验 |
| Feasibility | 8 | 3 | 3 | 全图 1.1GB 下载/解析未实测，4090 池 offline；修复：先做视觉子图 CPU smoke 并写明恢复门槛 |
| Experimental convincibility | 10 | 4 | 3 | — |
| Venue fit | 8 | 3 | 3 | 分析/协议型在 CVPR 主轨定位不稳；修复：明确 D&B track 定位并给出社区可复用协议与基线表 |
| Timeliness | 6 | 4 | 4 | — |
| Acceptance potential | 8 | 3 | 3 | 可能被归为「更严格的消融」；修复：给出能预测留出图 delta 的闭式/可计算指标 |

**Weighted final score: 3.54｜Overall: 7.08｜Confidence: Medium｜Current conference readiness: medium｜Development potential: high**

- **Fatal gates**：none（novelty 3、method 4、evidence 4、venue 3 均未触线）。
- **Panel（独立后综合）**：Field — 争议是真问题，2604.04033 与 FlyGM 结论相左值得裁决；Method — 零模型族构造是主要技术风险，保 motif/模块/谱的采样需可证明；Experiment — 长时程 + 多 seed CI + 留出图预测是决定性证据；AC/Venue — 「只是消融」是 desk-reject 级措辞风险，必须先立 protocol 贡献；Skeptical — 最强反对是「2604.04033 的未来工作段落已经把这个 idea 写出来了」。
- **Score-change conditions（到 8.00）**：novelty 3→5（+28）、evidence 4→5（+10）、venue 3→4（+8）= **+46 点 → 4.00 / 8.00**。具体：① 逐条核验 3–8 条一手 closest work；② 多任务、多 seed 的 delta CI 与留出图预测力；③ 明确 D&B 定位。**这些是条件，不是预测分数，更不是达标承诺。**
- **Recommendation**：`pivot-with-rescue-route`（best development route；若全为负结果，收敛成预注册争议裁决 + 零模型标准）。

### I5 `energy_pareto` — 能耗-精度 Pareto 统一协议

| Dimension | W | Score | Conf. | Deduction / evidence basis / repair condition |
|---|---:|---:|---:|---|
| Problem importance | 12 | 4 | 4 | — |
| Novelty vs prior work | 14 | 3 | 3 | SynOps 与能效对照已有（arXiv:2610.17154、UniSparse、SDTrack）；修复：证明「跨实现统一口径 + 结构 vs 等稀疏随机 Pareto + 预注册否证」无近邻 |
| Conceptual innovation | 12 | 3 | 3 | 目前是测量协议而非新洞见；修复：给出「结构稀疏何时省能」的可预测边界条件 |
| Method soundness | 14 | 4 | 3 | — |
| Elegance | 8 | 4 | 4 | — |
| Feasibility | 8 | 3 | 2 | 需硬件或多实现/模拟器复现，资源口径未锁；修复：先定义参考实现与代理指标分解表 |
| Experimental convincibility | 10 | 3 | 3 | 负结果要「教会社区东西」才够；修复：预注册假设、跨实现方差、最小可检测效应量 |
| Venue fit | 8 | 3 | 3 | 测量/负结果在 CVPR 主轨定位中等；修复：绑定 D&B 或高效视觉 track 的真实需求 |
| Timeliness | 6 | 4 | 4 | — |
| Acceptance potential | 8 | 3 | 3 | 审稿人可能认为「只是把已有指标统一」；修复：给出反直觉的跨实现方差结论 |

**Weighted final score: 3.40｜Overall: 6.80｜Confidence: Medium-Low｜Readiness: medium｜Development potential: high**

- **Fatal gates**：none。
- **Panel**：Field — 口径不可比是真痛点；Method — 能耗代理必须分解 SynOps/MAC/内存，否则不可复现；Experiment — 等精度约束与多实现复现是决定性设计；AC/Venue — 纯负结果需明确社区收益；Skeptical — 最强反对是「SDTrack/SpikeTrack 已报告 mJ/SOPs，你只是重测」。
- **Score-change conditions（到 8.08）**：novelty 3→5（+28）、evidence 3→5（+20）、venue 3→4（+8）、acceptance 3→4（+8）= **+64 点 → 4.04 / 8.08**。
- **Recommendation**：`pivot-with-rescue-route`（与 I1 共享图指标思想时须登记独立结论、不共用原始运行）。

### I2 `merging_partition` — 连接组模块分区 × model merging

| Dimension | W | Score | Conf. | Deduction / evidence basis / repair condition |
|---|---:|---:|---:|---|
| Problem importance | 12 | 4 | 4 | — |
| Novelty vs prior work | 14 | 3 | 2 | CVPR 2026 DuetMerging / AlphaMerging / ESM 已把分区做得很密；修复：核验是否有外部结构先验合并工作，并给出非重复 delta |
| Conceptual innovation | 12 | 4 | 3 | — |
| Method soundness | 14 | 3 | 2 | **连接组模块→ViT 神经元映射是人为先验**；修复：预注册映射、打乱映射/保度重连分区消融、证明斜率优势不靠调参 |
| Elegance | 8 | 3 | 3 | 生物结构可能只是任意分组；修复：给出为什么该分组必要的可检验理由 |
| Feasibility | 8 | 4 | 4 | — |
| Experimental convincibility | 10 | 3 | 3 | 只报 8 任务精度不足以支持「干扰增长更慢」；修复：8/14/20 任务斜率 + CI |
| Venue fit | 8 | 4 | 4 | — |
| Timeliness | 6 | 4 | 4 | — |
| Acceptance potential | 8 | 2 | 2 | 「外部生物结构」易被读成噱头；修复：证明它优于随机分组与数据驱动分区且不需任务信息 |

**Weighted final score: 3.38｜Overall: 6.76｜Confidence: Medium-Low｜Readiness: medium｜Development potential: high**

- **Fatal gates**：none（acceptance 2 不是 fatal gate 项，但已单独列入 serious risk）。
- **Panel**：Field — 任务干扰是真瓶颈；Method — 映射任意性是致命点；Experiment — 必须有任务数扫描与 matched 计算；AC/Venue — CVPR 主轨适配好；Skeptical —「为什么不直接用 activation mask（DuetMerging 已有）」是最强反对。
- **Score-change conditions（到 8.04）**：novelty 3→5（+28）、method 3→5（+28）、acceptance 2→3（+8）= **+64 点 → 4.02 / 8.04**。
- **Recommendation**：`pivot-with-rescue-route`（rescue：退为「外部结构分区 vs 数据驱动分区」的诊断结论）。

### I3 `spectral_ssm` — motif 谱 × 视觉 SSM

| Dimension | W | Score | Conf. | Deduction / evidence basis / repair condition |
|---|---:|---:|---:|---|
| Problem importance | 12 | 3 | 3 | 记忆时程可解释性是否 CVPR 社区关心的瓶颈未证实；修复：用长视频失败案例量化 |
| Novelty vs prior work | 14 | 3 | 2 | MambaTrack（arXiv:2604.13426）已做事件自适应 A；修复：完成 SSM 初始化一手检索 |
| Conceptual innovation | 12 | 4 | 3 | — |
| Method soundness | 14 | 3 | 2 | 图谱→A 的映射人为，非对称谱的数值稳定性未知；修复：给出可证明的衰减率对应关系 |
| Elegance | 8 | 3 | 3 | 结构先验 + 学来 A 的混合增加复杂度；修复：证明冻结 A 已足够 |
| Feasibility | 8 | 3 | 3 | 长视频训练代价、4090 offline；修复：先小子图短序列 smoke |
| Experimental convincibility | 10 | 3 | 3 | 需跨 3 任务 + 同秩随机谱对照才能排除「只是初始化」；修复：预注册谱间隙-记忆长度回归 |
| Venue fit | 8 | 4 | 4 | — |
| Timeliness | 6 | 4 | 4 | — |
| Acceptance potential | 8 | 2 | 2 | 容易被归为「换初始化」；修复：证明谱可事前预测有效记忆长度 |

**Weighted final score: 3.18｜Overall: 6.36｜Confidence: Low｜Readiness: low｜Development potential: medium**

- **Fatal gates**：none。
- **Panel**：Field — 问题需更锋利；Method — 谱与记忆时程的因果链是核心；Experiment — 同秩随机谱是最关键对照；AC/Venue — 骨干类工作需超过强基线；Skeptical —「MambaTrack 已让 A 自适应，你只是固定 A」。
- **Score-change conditions（到 8.04）**：novelty 3→5（+28）、method 3→5（+28）、evidence 3→5（+20）、venue 4→5（+8）= **+84 点 → 4.02 / 8.04**。
- **Recommendation**：`pivot-with-rescue-route`（若性能无增益但预测力成立，转分析型论文）。

### I6 `continual_isolation` — E/I 模块边界 × 持续视觉学习

| Dimension | W | Score | Conf. | Deduction / evidence basis / repair condition |
|---|---:|---:|---:|---|
| Problem importance | 12 | 4 | 4 | — |
| Novelty vs prior work | 14 | 2 | 1 | **本轮完全未检索「生物启发持续学习」子领域**；修复：先做 3–8 条一手检索，否则 novelty 只能按未知处理 |
| Conceptual innovation | 12 | 3 | 2 | 与 EWC/PackNet 类「冻结重要参数」思路同族；修复：给出与任务无关先验的非重复主张 |
| Method soundness | 14 | 3 | 2 | E/I 标签到人工网络参数的映射人为；修复：打乱标签/保度重连掩码消融 |
| Elegance | 8 | 3 | 3 | 分组规则可能只是任意稀疏；修复：证明必要性 |
| Feasibility | 8 | 4 | 4 | — |
| Experimental convincibility | 10 | 3 | 3 | 需 forgetting-容量前沿 + 强基线 matched 预算；修复：预注册划分与多种子 |
| Venue fit | 8 | 4 | 4 | — |
| Timeliness | 6 | 3 | 3 | 持续学习热度存在但 2026 拥挤；修复：给出 why now 的具体证据 |
| Acceptance potential | 8 | 2 | 2 | 「生物启发抗遗忘」很可能已有工作；修复：先检索再谈 |

**Weighted final score: 3.06｜Overall: 6.12｜Confidence: Low｜Readiness: low｜Development potential: medium**

- **Fatal gates**：novelty 2 但置信为 Low，`fatal gate: novelty <=2 with high confidence` 不触发；`novelty unknown + no closest-work search` 触发 **`needs-literature-search`**，recommendation 上限为 pivot。
- **Panel**：Field — 抗遗忘是真问题；Method — 映射与规则任意性；Experiment — 类增量划分与预算匹配；AC/Venue — 主轨可行但需超强基线；Skeptical —「这只是另一种 fixed mask」。
- **Score-change conditions（到 8.08）**：novelty 2→5（+42）、method 3→5（+28）、evidence 3→5（+20）、acceptance 2→3（+8）= **+98 点 → 4.04 / 8.08**；前置条件是把该子领域检索补齐。
- **Recommendation**：`needs-literature-search` / `pivot-with-rescue-route`。

### I4 `onoff_restoration` — ON/OFF 双通路联合退化恢复

| Dimension | W | Score | Conf. | Deduction / evidence basis / repair condition |
|---|---:|---:|---:|---|
| Problem importance | 12 | 3 | 3 | 联合退化是否真实高频需求未量化；修复：给出现实场景与失败案例 |
| Novelty vs prior work | 14 | 3 | 2 | 未检索 CV 侧「生物通路分离低层视觉」一手文献；修复：补检索 |
| Conceptual innovation | 12 | 4 | 3 | — |
| Method soundness | 14 | 3 | 2 | **物种对应性错误风险**：本轮一手 ON/OFF + 侧抑制文献是脊椎动物视网膜（Frontiers 2026、PNAS 2026），果蝇 ON/OFF 在 lamina LMC / T4-T5；修复：核验 MaleCNS 注释或去掉生物叙述 |
| Elegance | 8 | 4 | 4 | — |
| Feasibility | 8 | 2 | 2 | 无现成联合退化基准、需自建合成协议，且 CVPR 2027 只剩约 10 天；修复：预注册合成协议 + 明确时间不可行则换 venue |
| Experimental convincibility | 10 | 3 | 3 | 自建协议容易被质疑；修复：等参通用前端对照 + 跨数据集泛化 |
| Venue fit | 8 | 3 | 3 | 低层视觉主轨但生物动机占比过高；修复：收敛为纯 CV 机制主张 |
| Timeliness | 6 | 3 | 3 | 退化恢复拥挤；修复：给出联合退化的独特失效证据 |
| Acceptance potential | 8 | 2 | 2 | 易被读成「生物启发模块拼接」；修复：通路分离的必要性消融 |

**Weighted final score: 3.04｜Overall: 6.08｜Confidence: Low｜Readiness: low｜Development potential: medium**

- **Fatal gates**：`feasibility <= 2 under fixed deadline` → **封顶 `pivot-with-rescue-route`**（CVPR 2027 submission 2026-11-16，官方声明无延期）。
- **Panel**：Field — 联合退化是真问题但需证据；Method — 物种对应性是致命点；Experiment — 自建基准的可复现性；AC/Venue — 生物动机过重；Skeptical —「ON/OFF 差分就是两帧相减」。
- **Score-change conditions（到 8.24）**：novelty 3→5（+28）、method 3→5（+28）、feasibility 2→4（+16）、evidence 3→5（+20）、venue 3→5（+16）= **+108 点 → 4.12 / 8.24**；这是 6 个里升幅最大、最难的路径。
- **Recommendation**：`pivot-with-rescue-route`（rescue：去掉生物叙述，改为「通路分离是联合退化可解性必要条件」的纯 CV 机制论文）。

## 3 为什么本轮诚实地给不出 6 个 >8/10

| 原因 | 依据 |
|---|---|
| novelty 只能封顶 3 | `strict-idea-review.md` §Score Guardrails：closest work 未逐条核验且 novelty 决策关键时封顶 3；本轮检索覆盖 partial |
| 门槛等价于「10 维全 4–5 且零 fatal」 | `rubric.md` 权重合计 100；`Overall 8.0` = `weighted 4.0`，在 novelty 封顶 3 的情况下，其余维度几乎必须全 5 才可能补回 |
| 证据维度不能凭空给 5 | `ccf-experiment-designer` / `privacy-and-evidence.md` 禁止发明结果；本轮 6 个 idea 全部**未跑任何实验、未复跑强基线、未产生指标文件** |
| 项目硬约束 | 4090 池 `eligible_nodes=0`、CVPR 2027 剩约 10 天、总 idea 上限 12 个、既有候选已十余个；这些都会压 feasibility / acceptance potential |

**共同达标前置（6 个都一样）**：① 每个 idea 补齐 3–8 条一手 closest work 并逐条核验；② 预注册零模型/消融与 kill criteria；③ 在 4090 恢复后（或先用 CPU 合成图）跑最小可信证据包：强基线复跑、机制消融、鲁棒/压力测试、失败分析、可审计复现细节；④ 重新走一次 standard 评审。在此之前，任何 >8/10 的数字都是编造。

## 4 状态与纪律

- 本报告为**诊断性 idea review**，不是 `ccf-paper-reviewer` full review，不含 `**Overall:** X` 论文级达标结论。
- 未编造文献、数据集、实验结果或分数；所有分数由 rubric 权重实算，所有近邻来自本轮公开检索或项目 `verification-report.md` 已核实清单，二手来源已标注。
- 未使用 `abandon`；6 个都给了 rescue route（`task-modes.md:63`）。
- 结论：**0/6 达到 >8/10**；项目 0/5 达标状态不变；不写 guidance、不进 P2、不占 4090、不投稿、不 commit/push。

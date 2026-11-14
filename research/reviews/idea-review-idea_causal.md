# CCFA Idea Review — 固定连接组上的稀疏因果子回路发现 (`idea_causal`)

Mode: standard（ccf-idea-reviewer）。评审对象：平台 AI 任务 15274 的 `novix-idea-tree.json` 中一个 idea（原文见 `docs/platform-ai-ideas-15274.md`）。
**性质：idea 阶段评审，不是论文 P9 full 评审；分数不计入 `qualified_papers.json`，不计入 Overall >= 8.0 达标计数。**

## Verdict first

- **Weighted final score (1-5): 3.14**
- **Overall score (1-10, derived): 6.28**（weighted × 2；非论文评审分）
- **Current conference readiness: low**｜**Development potential: medium**
- **Confidence: Medium（2610.10023 已核实；门控/隐变量方向检索不足）**
- **Recommendation: needs-literature-search + pivot-with-rescue-route（fatal gate：method soundness<=2）；rank 2 / 备份方向**

## Target venue and assumptions

CVPR 2027 主轨（官方 CFP：8 页 + 参考文献、双盲、2026-11-16 AoE，AI for Science / biological vision 在范围内）。假设：单卡 48GB、公开连接组数据、无新增生理实验记录、不实际投稿。当前 exp-4090 池 `eligible_nodes=0` 属外部资源约束，计入 feasibility，不记为 idea 本身缺陷。

## Search basis

已做 public-safe 通用关键词检索，未把未公开 idea 原文贴入查询。已逐条核实：2610.10023、2604.04033、2610.29205、2404.17128（PMC + ar5iv 附录）、Nature Neuroscience 2025 HS 网络、Lappalainen Nature 2024 / flyvis。平台 AI 145 篇清单中标注「未独立核验」者仅作线索，不作决定性证据。凡 novelty 决策关键且检索不足者按 strict 协议封顶 3 并标 `needs-literature-search`。

## Normalized idea

问题：connectome-constrained 视觉模型通常调参，难回答哪些真实边/模组对任务因果必要，且随机图控制不严时易夸大拓扑优势；洞见：真实连接作候选边集，组稀疏/细胞类型级门控 + 突触预算约束的 GNN-SNN，门控后做逐边/逐模组反事实消融并使用活动表征；证据：误差-边预算 Pareto、反事实损失、跨种子门控稳定性、细胞类型响应一致性；局限：百万级边逐边消融昂贵，无生理记录时『因果』仅是模型内反事实。

## Closest prior art table

| 工作 | 年份/venue | 来源 | 核实状态 | 已做的事 |
|---|---|---|---|---|
| arXiv:2610.10023, Structure alone supports efficient visual computation in the Drosophila visual system | arXiv 2026-10 | https://arxiv.org/abs/2610.10023 | 已核实 | 固定图+复眼几何，只学 scalar synaptic gains 与阈值，Kenyon-cell 线性读出；颜色/形状/数量多任务；随机化图集成对照 |
| arXiv:2604.04033, Topological Sensitivity in Connectome-Constrained Neural Networks | arXiv 2026-04 | https://arxiv.org/abs/2604.04033 | 已核实 | flyvis control ladder：共享随机初始化 + degree-preserving null 后，此前报告的拓扑优势基本消失 |
| arXiv:2505.13011, Unveiling and Steering Connectome Organization with Interpretable Latent Variables | arXiv 2025 | 平台 AI 检索清单 | 未独立核验（仅线索） | 可解释隐变量操控连接组组织；可能压缩门控/反事实方向的新颖性 |
| Lappalainen et al., Connectome-constrained networks predict neural activity across the fly visual system | Nature 2024 | doi:10.1038/s41586-024-07939-3 / TuragaLab/flyvis | 已核实 | 64 类细胞连接组约束 DMN，只优化突触/激活参数；提供光流任务、预训练与复现 notebooks |

## Novelty delta

2610.10023 已做固定图+只学 gains+Kenyon-cell 读出+随机化对照，但无组稀疏门控、突触预算 Pareto、逐模组反事实与跨种子稳定性；2505.13011（未核验）可能压缩可解释操控空间。剩余 delta 是『预算约束下的可复核回路清单』，须与剪枝/NAS 明确区分。

## Serious blockers / fatal gates

- 高风险（方法/措辞）：无生理记录时『因果』只是模型内反事实；平台 AI 自标『可能只是剪枝/架构搜索的增量』。
- 高风险（新颖性未定）：2505.13011 未核验，且 2610.10023 的固定图+增益框架与主干高度相邻。
- 中风险（可行性）：百万级边逐边反事实昂贵，需限定 optic-lobe 子图与预算扫描。

## Per-expert reviewer notes（独立，先于汇总）

- **Field Expert**：最强论点：『哪些真实边对视觉任务必要』尚未系统回答，2610.10023 只回答结构够不够；拒稿级担忧：若只是门控稀疏化，与剪枝文献无法区分。锚点：closest work。修复：稳定命中的细胞类型与已知视觉通路做富集检验。置信：中。
- **Method Expert**：最强论点：组稀疏门控+预算形式可控；拒稿级担忧：因果 ≠ 模型内反事实，逐边消融不可判定，这是 soundness<=2 的直接原因。锚点：内部矛盾。修复：改称 task-necessary subgraph + 逐模组 + 预注册协议。置信：高。
- **Experiment Expert**：最强论点：随机门控、度保持图、按度/空间门控、冻结动力学、跨种子稳定性可证伪『只是剪枝』；拒稿级担忧：2610.10023 已用随机化图集成做 wiring-economy 对照，主表只放 Pareto 会显重复。锚点：已核实预印本。修复：主指标改跨种子稳定性与类型富集。置信：中高。
- **AC / Venue Expert**：最强论点：CVPR 2027 CFP 含 efficient and scalable vision / AI for Science；拒稿级担忧：标题里的 causal 会让审稿人要求干预性证据，回路清单更像 workshop。锚点：venue criterion + 措辞。修复：改标题与 claim，主表放视觉收益。置信：中高。
- **Skeptical Prior-Art Expert**：最强论点：组门控+逐模组反事实在 2610.10023 中未出现；拒稿级担忧：2505.13011 未核验且 pruning/NAS 线未检索，现在不能给高 novelty。锚点：检索不足。修复：逐条核验 + 补 pruning/NAS 非重复检索。置信：低。

**Panel synthesis** — Agreement：五角色都认为证据协议可判定，但中心主张的新颖性/机制存在一致严肃担忧。Disagreement：Experiment Expert 正面评价实验设计，Skeptical Prior-Art Expert 负面评价可发表性，二者不冲突（设计好 ≠ 主张新）。Decisive reject axis：见 fatal gates。Final calibrated stance：needs-literature-search + pivot-with-rescue-route（fatal gate：method soundness<=2）；rank 2 / 备份方向。

## Rubric scores

| Dimension | Weight | Score (1-5) | Confidence | Deduction / evidence basis / repair condition |
|---|---:|---:|---|---|
| Problem importance | 12 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Novelty against likely prior work | 14 | 3 | 低 | 锚点：2610.10023 已发表固定图+增益+随机对照；门控/反事实线还缺 2505.13011 核验，检索不足按 strict 封顶 3；修复：逐条核验 + 给出与 pruning/NAS 的非重复表。 |
| Conceptual innovation | 12 | 3 | 低 | 锚点：组稀疏门控+预算 Pareto+反事实是已知可解释工具组合，只产出回路清单易被读成剪枝；修复：给出门控稳定性与细胞类型注释间的可证伪预测（跨种子稳定命中的类型富集）。 |
| Method soundness | 14 | 2 | 低 | 锚点：内部矛盾——『因果子回路』与实际证据『模型内反事实消融』不等价，且逐边消融在百万边不可判定；<=2 触发 fatal gate。修复：改称 task-necessary subgraph、逐模组评估、预注册反事实定义。 |
| Elegance and simplicity | 8 | 3 | 低 | 锚点：门控/预算/反事实/活动表征四套机制叠加，必要性未论证；修复：随机门控与只训练读出层列为两个必要对照。 |
| Feasibility under resources | 8 | 3 | 低 | 锚点：需 optic-lobe 子图预算扫描 + 3 seeds，且 exp-4090 池 eligible_nodes=0；修复：等节点恢复，先单 seed 原型测峰值显存。 |
| Experimental convincibility | 10 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Venue and audience fit | 8 | 3 | 低 | 锚点：CVPR 对稀疏/可解释视觉网络有兴趣，但 causal 措辞易引发 desk-level 质疑，回路清单的视觉贡献不突出；修复：主表放误差-边预算 Pareto，回路清单放第二节。 |
| Timeliness and topic heat | 6 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Risk-adjusted acceptance potential | 8 | 3 | 低 | 锚点：soundness<=2 的 fatal gate + 与 2610.10023 相邻，最可能写 this is pruning with a new name；修复：claim 降级 + 非重复检索后重评。 |

> 加权由脚本计算：sum(score × weight)/100 = 3.14；1-10 换算 = 6.28。所有 <=3 分数均给出锚点、扣分理由与修复条件。

## Score-change conditions

完成 claim 降级（causal→task-necessary）+ 逐模组反事实预注册 + 2505.13011 与 pruning/NAS 非重复检索 + 跨种子细胞类型富集：soundness 2→3/4、novelty 3→4，加权约 +0.5~+0.8，可达 revise 下沿。

## Fixability table

| Issue | Affected dimension | Severity | Fix class | Before writing? | Required change | Owner |
|---|---|---|---|---|---|---|
| Serious blockers 第 1 条 | Novelty / acceptance | high | novelty-grounding + problem-refinement | partly | 非重复检索 + 重写中心主张 | ccf-literature-searcher / ccf-idea-optimizer |
| 机制或措辞层面的中心风险 | Method soundness | high | method-redesign | yes | 预注册定义、降级 claim、逐模组评估 | ccf-experiment-designer |
| exp-4090 池当前不可用 | Feasibility | medium | feasibility-check | no（外部） | 等 eligible_nodes>0，先单 seed 原型 | 外部平台 |

## Upgrade / pivot actions（最小可救路线）

保留『预算约束下跨种子稳定的子图』，去掉因果措辞；主干收缩为固定拓扑 vs 组门控 vs 随机门控 vs 度保持图四臂，optic-lobe 子图、3 seeds、预算扫描，以稳定命中的细胞类型富集作为区分剪枝的关键证据。

## Evidence that would change my score

见 Score-change conditions；所有条目要求可落盘证据（非重复检索表、预注册协议、实测指标或配对表），口头声明不改变分数。

## Checklist status

1 venue/assumptions 明确 PASS｜2 问题-方法卡 PASS｜3 文献状态标注 PASS｜4 closest-work 表 PASS｜5 五角色独立 PASS｜6 十维度全评分且 <=3 有扣分/修复 PASS｜7 致命与可修复分离 PASS｜8 confidence 独立 PASS｜9 推荐词来自协议集合 PASS｜10 未调用被禁模块 PASS。

## Output self-check

表格列数一致；分数由脚本计算并复核；无未填字段；无「有一定创新性/建议进一步完善」类空话；每条批评带锚点。

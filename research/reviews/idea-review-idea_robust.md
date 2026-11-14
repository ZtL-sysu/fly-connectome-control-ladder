# CCFA Idea Review — 不确定性鲁棒的跨连接组 SNN (`idea_robust`)

Mode: standard（ccf-idea-reviewer）。评审对象：平台 AI 任务 15274 的 `novix-idea-tree.json` 中一个 idea（原文见 `docs/platform-ai-ideas-15274.md`）。
**性质：idea 阶段评审，不是论文 P9 full 评审；分数不计入 `qualified_papers.json`，不计入 Overall >= 8.0 达标计数。**

## Verdict first

- **Weighted final score (1-5): 3.06**
- **Overall score (1-10, derived): 6.12**（weighted × 2；非论文评审分）
- **Current conference readiness: low**｜**Development potential: medium**
- **Confidence: High（两篇关键近似工作已逐条核实）**
- **Recommendation: pivot-with-rescue-route（fatal gate：novelty<=2 且高置信，封顶 pivot）**

## Target venue and assumptions

CVPR 2027 主轨（官方 CFP：8 页 + 参考文献、双盲、2026-11-16 AoE，AI for Science / biological vision 在范围内）。假设：单卡 48GB、公开连接组数据、无新增生理实验记录、不实际投稿。当前 exp-4090 池 `eligible_nodes=0` 属外部资源约束，计入 feasibility，不记为 idea 本身缺陷。

## Search basis

已做 public-safe 通用关键词检索，未把未公开 idea 原文贴入查询。已逐条核实：2610.10023、2604.04033、2610.29205、2404.17128（PMC + ar5iv 附录）、Nature Neuroscience 2025 HS 网络、Lappalainen Nature 2024 / flyvis。平台 AI 145 篇清单中标注「未独立核验」者仅作线索，不作决定性证据。凡 novelty 决策关键且检索不足者按 strict 协议封顶 3 并标 `needs-literature-search`。

## Normalized idea

问题：单重建训练的模型可能把测量误差当成机制；缺口：跨版本迁移与校准未知；洞见：把边存在概率/突触置信度做成随机消息传递门；方法：固定稀疏拓扑、细胞类型级参数、LIF、风险敏感训练；证据：跨重建性能下降、校准误差、脉冲预算，零模型为 weight-noise 与随机边噪声；局限：跨数据集节点对齐困难。

## Closest prior art table

| 工作 | 年份/venue | 来源 | 核实状态 | 已做的事 |
|---|---|---|---|---|
| arXiv:2610.29205, Reconstruction differences rival individual differences in the fly compass connectome | arXiv 2026-10 | https://arxiv.org/abs/2610.29205 | 已核实 | MaleCNS/hemibrain/FlyWire/BANC 共 9 布线版本；测量差异 rival 个体差异；模型跨重建不迁移；噪声训练降精度仅部分改善迁移 |
| arXiv:2604.04033, Topological Sensitivity in Connectome-Constrained Neural Networks | arXiv 2026-04 | https://arxiv.org/abs/2604.04033 | 已核实 | flyvis control ladder：共享随机初始化 + degree-preserving null 后，此前报告的拓扑优势基本消失 |
| arXiv:2610.10023, Structure alone supports efficient visual computation in the Drosophila visual system | arXiv 2026-10 | https://arxiv.org/abs/2610.10023 | 已核实 | 固定图+复眼几何，只学 scalar synaptic gains 与阈值，Kenyon-cell 线性读出；颜色/形状/数量多任务；随机化图集成对照 |
| Lappalainen et al., Connectome-constrained networks predict neural activity across the fly visual system | Nature 2024 | doi:10.1038/s41586-024-07939-3 / TuragaLab/flyvis | 已核实 | 64 类细胞连接组约束 DMN，只优化突触/激活参数；提供光流任务、预训练与复现 notebooks |

## Novelty delta

减去 2610.29205 后只剩『把边置信度做成可学习随机门』这一实现细节：跨重建评测协议、噪声训练、迁移失败与『需报告重建版本』的诉求均已被该文给出；2604.04033 又要求跨图比较先排掉初始化与零模型混淆。

## Serious blockers / fatal gates

- 致命（新颖性）：2610.29205 已用 9 个布线版本完成跨重建鲁棒性诊断并给出结论。
- 高风险（可行性）：MaleCNS 与 FlyWire 的 cell-type/坐标无公开严格一一映射，配对错误会把鲁棒性变成对齐误差的度量。
- 高风险（证据）：不确定性门若不显著优于 weight-noise 基线，中心机制被证伪。

## Per-expert reviewer notes（独立，先于汇总）

- **Field Expert**：最强论点：重建依赖性是真问题（2610.29205 用成像显示真实罗盘渐变漂移而模型崩溃）；拒稿级担忧：该文已把问题、诊断、建议全部给出。锚点：arXiv:2610.29205。修复：换视觉通路并证明结论不迁移。置信：高。
- **Method Expert**：最强论点：随机门形式自洽；拒稿级担忧：跨数据集无共同节点身份，门控不确定性无法归因于测量误差，且与 weight-noise 的区别未定义。锚点：缺失机制。修复：同一重建内做阈值扰动。置信：高。
- **Experiment Expert**：最强论点：去门/weight-noise/随机边噪声/单图训练/跨图留出是可判定零模型组；拒稿级担忧：最关键跨图留出正是该文 Fig 5，重复不构成新证据。锚点：closest work。修复：主指标改视觉校准误差。置信：高。
- **AC / Venue Expert**：最强论点：CVPR 2027 有 AI for Science / biological vision；拒稿级担忧：中心贡献是数据版本敏感性诊断，视觉受众要可迁移架构结论。锚点：venue criterion。修复：以架构配置规则收尾。置信：中高。
- **Skeptical Prior-Art Expert**：最强论点：无；拒稿级担忧：2610.29205 与 2604.04033 合起来覆盖重建差异与严格对照，术语不改变实验结论。锚点：两篇已核实预印本。修复：先做针对性非重复检索。置信：高。

**Panel synthesis** — Agreement：五角色都认为证据协议可判定，但中心主张的新颖性/机制存在一致严肃担忧。Disagreement：Experiment Expert 正面评价实验设计，Skeptical Prior-Art Expert 负面评价可发表性，二者不冲突（设计好 ≠ 主张新）。Decisive reject axis：见 fatal gates。Final calibrated stance：pivot-with-rescue-route（fatal gate：novelty<=2 且高置信，封顶 pivot）。

## Rubric scores

| Dimension | Weight | Score (1-5) | Confidence | Deduction / evidence basis / repair condition |
|---|---:|---:|---|---|
| Problem importance | 12 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Novelty against likely prior work | 14 | 2 | 低 | 锚点：arXiv:2610.29205 已核实摘要（9 版本、跨重建不迁移、噪声训练）；修复：收窄到 MaleCNS v1.0 视叶子图的突触检测阈值扰动 + 校准 Pareto，并做非重复检索。 |
| Conceptual innovation | 12 | 3 | 低 | 锚点：随机门+风险敏感训练是已知不确定性模块组合，无新能力/解释；修复：给出边置信度与突触检测置信度的可证伪映射及新的校准-精度 Pareto。 |
| Method soundness | 14 | 3 | 低 | 锚点：跨数据集节点身份未定义，对齐误差与真实重建差异不可分辨；修复：发布可复审共同子图与配对置信度表，主对照改为同数据集内扰动。 |
| Elegance and simplicity | 8 | 3 | 低 | 锚点：五个组件必要性未论证；修复：逐一消融证明单独贡献。 |
| Feasibility under resources | 8 | 3 | 低 | 锚点：需多套全脑数据+对齐工程，且 exp-4090 池 eligible_nodes=0；修复：等节点恢复，先做单数据集阈值扰动最小原型。 |
| Experimental convincibility | 10 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Venue and audience fit | 8 | 3 | 低 | 锚点：诊断型贡献更接近计算神经/建模方法学，CVPR 主轨会问可迁移架构结论；修复：主结果改为视觉任务的鲁棒性-精度 Pareto。 |
| Timeliness and topic heat | 6 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Risk-adjusted acceptance potential | 8 | 2 | 低 | 锚点：两篇 2026 预印本叠加，strict reviewer 最可能写 already studied；修复：完成收窄+非重复检索后重评。 |

> 加权由脚本计算：sum(score × weight)/100 = 3.06；1-10 换算 = 6.12。所有 <=3 分数均给出锚点、扣分理由与修复条件。

## Score-change conditions

完成视觉通路非重复检索 + 可复审配对表 + 证明门显著优于 weight-noise 且给出校准-精度 Pareto：novelty 2→3/4、acceptance 2→3，加权约 +0.4~+0.7；若检索确认仍被覆盖则转 pivot。

## Fixability table

| Issue | Affected dimension | Severity | Fix class | Before writing? | Required change | Owner |
|---|---|---|---|---|---|---|
| Serious blockers 第 1 条 | Novelty / acceptance | high | novelty-grounding + problem-refinement | partly | 非重复检索 + 重写中心主张 | ccf-literature-searcher / ccf-idea-optimizer |
| 机制或措辞层面的中心风险 | Method soundness | high | method-redesign | yes | 预注册定义、降级 claim、逐模组评估 | ccf-experiment-designer |
| exp-4090 池当前不可用 | Feasibility | medium | feasibility-check | no（外部） | 等 eligible_nodes>0，先单 seed 原型 | 外部平台 |

## Upgrade / pivot actions（最小可救路线）

收窄为『MaleCNS v1.0 视叶子图内突触检测阈值扰动下的脉冲模型校准』，主对照改同重建内扰动，跨数据集仅作次要验证；先跑单卡 3 seeds 最小原型验证门控是否带来非平凡校准收益。

## Evidence that would change my score

见 Score-change conditions；所有条目要求可落盘证据（非重复检索表、预注册协议、实测指标或配对表），口头声明不改变分数。

## Checklist status

1 venue/assumptions 明确 PASS｜2 问题-方法卡 PASS｜3 文献状态标注 PASS｜4 closest-work 表 PASS｜5 五角色独立 PASS｜6 十维度全评分且 <=3 有扣分/修复 PASS｜7 致命与可修复分离 PASS｜8 confidence 独立 PASS｜9 推荐词来自协议集合 PASS｜10 未调用被禁模块 PASS。

## Output self-check

表格列数一致；分数由脚本计算并复核；无未填字段；无「有一定创新性/建议进一步完善」类空话；每条批评带锚点。

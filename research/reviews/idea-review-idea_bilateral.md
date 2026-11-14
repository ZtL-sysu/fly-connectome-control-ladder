# CCFA Idea Review — 双侧对称等变与损伤鲁棒视觉 SNN (`idea_bilateral`)

Mode: standard（ccf-idea-reviewer）。评审对象：平台 AI 任务 15274 的 `novix-idea-tree.json` 中一个 idea（原文见 `docs/platform-ai-ideas-15274.md`）。
**性质：idea 阶段评审，不是论文 P9 full 评审；分数不计入 `qualified_papers.json`，不计入 Overall >= 8.0 达标计数。**

## Verdict first

- **Weighted final score (1-5): 2.68**
- **Overall score (1-10, derived): 5.36**（weighted × 2；非论文评审分）
- **Current conference readiness: low**｜**Development potential: low**
- **Confidence: High（两篇直接近似工作已核实全文/附录）**
- **Recommendation: pivot-with-rescue-route / venue-switch（两个 fatal gate：novelty<=2、venue<=2）；发展潜力最低**

## Target venue and assumptions

CVPR 2027 主轨（官方 CFP：8 页 + 参考文献、双盲、2026-11-16 AoE，AI for Science / biological vision 在范围内）。假设：单卡 48GB、公开连接组数据、无新增生理实验记录、不实际投稿。当前 exp-4090 池 `eligible_nodes=0` 属外部资源约束，计入 feasibility，不记为 idea 本身缺陷。

## Search basis

已做 public-safe 通用关键词检索，未把未公开 idea 原文贴入查询。已逐条核实：2610.10023、2604.04033、2610.29205、2404.17128（PMC + ar5iv 附录）、Nature Neuroscience 2025 HS 网络、Lappalainen Nature 2024 / flyvis。平台 AI 145 篇清单中标注「未独立核验」者仅作线索，不作决定性证据。凡 novelty 决策关键且检索不足者按 strict 协议封顶 3 并标 `needs-literature-search`。

## Normalized idea

问题：左右对称是否提供视觉缺失/局部损伤下的冗余，尚未用严格等参数量模型与度保持随机图证明；洞见：建立双侧对应、共享细胞类型参数的双侧等变 GNN-SNN + 显式跨侧稀疏边；证据：干净误差、性能-损伤曲线、左右交换等变误差、跨侧活动相关性；局限：左右节点匹配与视野映射有歧义。

## Closest prior art table

| 工作 | 年份/venue | 来源 | 核实状态 | 已做的事 |
|---|---|---|---|---|
| arXiv:2404.17128, Network Structure Governs Drosophila Brain Functionality | arXiv 2024 / PMC | https://arxiv.org/abs/2404.17128 | 已核实（含附录 S3/S4） | 度保持重连、2000/12000 节点区域删除鲁棒性、左右半球单侧刺激与双侧协同响应曲线 |
| A competitive disinhibitory network for robust optic flow processing in Drosophila | Nature Neuroscience 2025 | https://www.nature.com/articles/s41593-025-01948-9 | 已核实 | EM 重建 HS 细胞网络；双侧去抑制提升旋转光流选择性；单侧操纵验证转向贡献 |
| arXiv:2610.29205, Reconstruction differences rival individual differences in the fly compass connectome | arXiv 2026-10 | https://arxiv.org/abs/2610.29205 | 已核实 | MaleCNS/hemibrain/FlyWire/BANC 共 9 布线版本；测量差异 rival 个体差异；模型跨重建不迁移；噪声训练降精度仅部分改善迁移 |
| arXiv:2604.04033, Topological Sensitivity in Connectome-Constrained Neural Networks | arXiv 2026-04 | https://arxiv.org/abs/2604.04033 | 已核实 | flyvis control ladder：共享随机初始化 + degree-preserving null 后，此前报告的拓扑优势基本消失 |

## Novelty delta

减去 2404.17128 后，单侧刺激→双侧响应、局部节点删除鲁棒性、度保持重连对照都已被做过；减去 Nature Neuroscience 2025 后，单侧操纵与双侧去抑制对光流的机制也已发表。只剩『把等变约束写成显式架构项』这一形式化差异。

## Serious blockers / fatal gates

- 致命（新颖性）：2404.17128 已做左右单侧刺激、双侧协同、约 12000 节点局部删除与度保持重连；Nature Neuro 2025 已用 EM+双光子+单侧操纵证明 HS 网络机制。
- 高风险（venue fit）：核心是网络结构/损伤鲁棒性分析，CVPR 主轨读成计算神经/网络科学的概率高。
- 高风险（机制）：等变约束若只提升干净集、损伤下无增益，平台 AI 自列证伪条件即命中。

## Per-expert reviewer notes（独立，先于汇总）

- **Field Expert**：最强论点：双侧协同与损伤鲁棒性真实成立（2404.17128 S4 给出单侧刺激下双侧激活曲线）；拒稿级担忧：正是该文让『尚未被证明』前提失效。锚点：已核实附录。修复：改为等参数量等变架构比较。置信：高。
- **Method Expert**：最强论点：等变约束形式化干净；拒稿级担忧：配对无置信度时等变误差可被配对算法任意调节，且共享参数与跨侧边必要性未分离。锚点：缺失机制。修复：配对表 + 逐组件消融。置信：中高。
- **Experiment Expert**：最强论点：四类损伤、左右交换、度保持空模型、等变误差是完整可判定协议；拒稿级担忧：Fig 6/S3/S4 已跑过大部分曲线。锚点：closest work。修复：主表改等变约束开/关对照。置信：高。
- **AC / Venue Expert**：最强论点：CVPR 有 AI for Science 轨道；拒稿级担忧：更可能分配到计算神经/网络科学审稿池，venue fit<=2 触发 venue-switch。锚点：官方 CFP + 贡献类型。修复：重写为视觉架构收益或换 venue。置信：中高。
- **Skeptical Prior-Art Expert**：最强论点：无；拒稿级担忧：2404.17128（含 PMC 全文与附录）与 Nature Neuro 2025 合起来覆盖双侧响应、单侧操纵、局部攻击、度保持重连，『等变』只是重命名。锚点：两篇已核实来源。修复：非重复检索后仍无 delta 则放弃该分支。置信：高。

**Panel synthesis** — Agreement：五角色都认为证据协议可判定，但中心主张的新颖性/机制存在一致严肃担忧。Disagreement：Experiment Expert 正面评价实验设计，Skeptical Prior-Art Expert 负面评价可发表性，二者不冲突（设计好 ≠ 主张新）。Decisive reject axis：见 fatal gates。Final calibrated stance：pivot-with-rescue-route / venue-switch（两个 fatal gate：novelty<=2、venue<=2）；发展潜力最低。

## Rubric scores

| Dimension | Weight | Score (1-5) | Confidence | Deduction / evidence basis / repair condition |
|---|---:|---:|---|---|
| Problem importance | 12 | 3 | 低 | 锚点：2404.17128 已给出『区域攻击下保持响应、随机重连才破坏功能』结论，本 idea 未提出该文答不了的新瓶颈；修复：收窄到等参数量下等变约束的可迁移架构增益。 |
| Novelty against likely prior work | 14 | 2 | 低 | 锚点：两篇已核实工作覆盖核心实验与机制；修复：非重复检索后把 contribution 限定为等变误差的可证伪度量。 |
| Conceptual innovation | 12 | 2 | 低 | 锚点：共享参数+等变+跨侧边是已知模块组合，无新能力/解释；修复：推导等变约束下的冗余下界或参数效率界形成理论增量。 |
| Method soundness | 14 | 3 | 低 | 锚点：左右配对与视野映射歧义未解决，配对错误可制造或抹掉等变误差；修复：发布带置信度配对表 + 配对失败敏感性分析。 |
| Elegance and simplicity | 8 | 3 | 低 | 锚点：等变约束、共享参数、跨侧边、四类损伤叠加，必要性未论证；修复：逐组件消融。 |
| Feasibility under resources | 8 | 3 | 低 | 锚点：需可复审配对表 + 多类损伤实验，且 exp-4090 池 eligible_nodes=0；修复：等节点恢复，先在子图单 seed 原型。 |
| Experimental convincibility | 10 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Venue and audience fit | 8 | 2 | 低 | 锚点：主结果是损伤-性能曲线与等变误差，视觉贡献不突出，venue fit<=2 触发 fatal gate；修复：改投计算神经/网络科学 venue，或主结果换成视觉架构收益。 |
| Timeliness and topic heat | 6 | 3 | 低 | 锚点：2024–2025 已有两篇直接相关工作，细分方向趋饱和；修复：依赖收窄后的新瓶颈重建 timeliness。 |
| Risk-adjusted acceptance potential | 8 | 2 | 低 | 锚点：两个 fatal gate 叠加，最强反对是 already shown in 2404.17128 Fig 6/S4；修复：收窄 + venue 判断后重评。 |

> 加权由脚本计算：sum(score × weight)/100 = 2.68；1-10 换算 = 5.36。所有 <=3 分数均给出锚点、扣分理由与修复条件。

## Score-change conditions

即便完成配对表与等变理论增量，novelty 上限约 3、venue fit 上限约 3，加权最多 +0.5；要进 revise 需同时换问题（等参数量架构增益）与换/重写 venue framing。

## Fixability table

| Issue | Affected dimension | Severity | Fix class | Before writing? | Required change | Owner |
|---|---|---|---|---|---|---|
| Serious blockers 第 1 条 | Novelty / acceptance | high | novelty-grounding + problem-refinement | partly | 非重复检索 + 重写中心主张 | ccf-literature-searcher / ccf-idea-optimizer |
| 机制或措辞层面的中心风险 | Method soundness | high | method-redesign | yes | 预注册定义、降级 claim、逐模组评估 | ccf-experiment-designer |
| exp-4090 池当前不可用 | Feasibility | medium | feasibility-check | no（外部） | 等 eligible_nodes>0，先单 seed 原型 | 外部平台 |

## Upgrade / pivot actions（最小可救路线）

保留『左右交换等变误差』这一可复用度量，放弃双侧鲁棒性作为主贡献；把等变收益改写为等参数量架构比较，并重新判断是否改投计算神经科学 venue。

## Evidence that would change my score

见 Score-change conditions；所有条目要求可落盘证据（非重复检索表、预注册协议、实测指标或配对表），口头声明不改变分数。

## Checklist status

1 venue/assumptions 明确 PASS｜2 问题-方法卡 PASS｜3 文献状态标注 PASS｜4 closest-work 表 PASS｜5 五角色独立 PASS｜6 十维度全评分且 <=3 有扣分/修复 PASS｜7 致命与可修复分离 PASS｜8 confidence 独立 PASS｜9 推荐词来自协议集合 PASS｜10 未调用被禁模块 PASS。

## Output self-check

表格列数一致；分数由脚本计算并复核；无未填字段；无「有一定创新性/建议进一步完善」类空话；每条批评带锚点。

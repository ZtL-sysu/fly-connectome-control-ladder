# CCFA Idea Review — 形态代理约束的突触延迟与时间编码 (`idea_delay`)

Mode: standard（ccf-idea-reviewer）。评审对象：平台 AI 任务 15274 的 `novix-idea-tree.json` 中一个 idea（原文见 `docs/platform-ai-ideas-15274.md`）。
**性质：idea 阶段评审，不是论文 P9 full 评审；分数不计入 `qualified_papers.json`，不计入 Overall >= 8.0 达标计数。**

## Verdict first

- **Weighted final score (1-5): 3.28**
- **Overall score (1-10, derived): 6.56**（weighted × 2；非论文评审分）
- **Current conference readiness: medium**｜**Development potential: high**
- **Confidence: Medium-Low（撞车文献已核实，但本方向专门检索覆盖不足）**
- **Recommendation: needs-literature-search（novelty 决策关键且检索不足）；tournament rank 1 / 最佳可救方向**

## Target venue and assumptions

CVPR 2027 主轨（官方 CFP：8 页 + 参考文献、双盲、2026-11-16 AoE，AI for Science / biological vision 在范围内）。假设：单卡 48GB、公开连接组数据、无新增生理实验记录、不实际投稿。当前 exp-4090 池 `eligible_nodes=0` 属外部资源约束，计入 feasibility，不记为 idea 本身缺陷。

## Search basis

已做 public-safe 通用关键词检索，未把未公开 idea 原文贴入查询。已逐条核实：2610.10023、2604.04033、2610.29205、2404.17128（PMC + ar5iv 附录）、Nature Neuroscience 2025 HS 网络、Lappalainen Nature 2024 / flyvis。平台 AI 145 篇清单中标注「未独立核验」者仅作线索，不作决定性证据。凡 novelty 决策关键且检索不足者按 strict 协议封顶 3 并标 `needs-literature-search`。

## Normalized idea

问题：GNN-SNN 时间步常只是计算展开，未证明延迟/细胞类型时间常数对视觉运动有因果贡献；缺口：缺可审计可证伪的延迟先验；洞见：用突触空间/层级信息构造延迟先验，按细胞类型共享延迟、膜常数与阈值，比较 rate/latency/delay-aware；证据：光流误差、方向准确率、时间反演、速度 OOD、脉冲率-性能曲线；局限：连接表未必含真实轴突传导延迟，事件仿真开销与梯度不稳。

## Closest prior art table

| 工作 | 年份/venue | 来源 | 核实状态 | 已做的事 |
|---|---|---|---|---|
| Lappalainen et al., Connectome-constrained networks predict neural activity across the fly visual system | Nature 2024 | doi:10.1038/s41586-024-07939-3 / TuragaLab/flyvis | 已核实 | 64 类细胞连接组约束 DMN，只优化突触/激活参数；提供光流任务、预训练与复现 notebooks |
| arXiv:2604.04033, Topological Sensitivity in Connectome-Constrained Neural Networks | arXiv 2026-04 | https://arxiv.org/abs/2604.04033 | 已核实 | flyvis control ladder：共享随机初始化 + degree-preserving null 后，此前报告的拓扑优势基本消失 |
| arXiv:2508.16792, Neuromorphic Simulation of Drosophila Brain Connectome on Loihi 2 | arXiv 2025 | 平台 AI 检索清单 | 未独立核验（仅线索） | 全脑 LIF 神经形态仿真；可能压缩时间编码方向的新颖性 |
| Range-Limited Scale Stability of Dynamic Direction Representations in a Connectome-Constrained Fly Visual Model | 2026 / doi:10.1007/s12021-026-09811-3 | 平台 AI 检索清单 | 未独立核验（仅线索） | 连接组约束视觉模型的动态方向表征；可能压缩时间机制方向的新颖性 |

## Novelty delta

通用检索未找到『形态代理 + 细胞类型共享延迟 + 时间反演/速度 OOD 证伪』的直接重复；但 flyvis 已用时间展开 DMN，2604.04033 已把 flyvis 对照标准化，且 Loihi 2 仿真与动态方向表征两篇未核验条目可能压缩空间。novelty 只能判『未知偏高』，不得判高。

## Serious blockers / fatal gates

- 高风险（机制）：『形态代理』并非真实传导延迟，若只是层级/列间距离则必须降级为结构性时间先验，否则是生物学过度声称。
- 高风险（新颖性未定）：三条 2025–2026 相关条目未逐条核验，按 strict 协议封顶 novelty=3 并需补检索。
- 中风险（可行性）：事件驱动 LIF 时间展开在 48GB 单卡的显存/吞吐与梯度稳定性未实测；当前 exp-4090 池 eligible_nodes=0。

## Per-expert reviewer notes（独立，先于汇总）

- **Field Expert**：最强论点：flyvis 证明连接组可预测神经活动，但未回答时间常数/传导延迟的功能角色；拒稿级担忧：若延迟只是自由参数，结论退化成多给参数就更好。锚点：缺失机制 + 2604.04033 混淆教训。修复：预注册代理 + 参数量匹配无延迟对照。置信：中。
- **Method Expert**：最强论点：按细胞类型共享延迟/膜常数/阈值是合理且参数高效的结构化先验；拒稿级担忧：空间距离与传导延迟无验证过的单调关系。锚点：缺失机制。修复：claim 降级 + 代理敏感性分析。置信：中高。
- **Experiment Expert**：最强论点：随机化延迟、打乱细胞类型常数、时间反演、速度 OOD 是四者中最好的证伪组；拒稿级担忧：缺『等参数量无延迟 LIF-GNN』在共享随机初始化下的对照，2604.04033 已证明不共享初始化会伪造优势。锚点：已核实预印本。修复：共享初始化写进协议。置信：高。
- **AC / Venue Expert**：最强论点：CVPR 2027 CFP 明列 AI for Science 与 biological/medical vision；拒稿级担忧：主结果若只是神经活动/脉冲率曲线会被读成计算神经科学。锚点：官方 CFP。修复：主表放视觉指标。置信：中高。
- **Skeptical Prior-Art Expert**：最强论点：通用关键词未发现直接重复；拒稿级担忧：未核验的 Loihi 2 仿真与 2026 动态方向表征可能已占用时间动力学+连接组组合。锚点：检索不足。修复：逐条核验后才允许 novelty 上调。置信：低。

**Panel synthesis** — Agreement：五角色都认为证据协议可判定，但中心主张的新颖性/机制存在一致严肃担忧。Disagreement：Experiment Expert 正面评价实验设计，Skeptical Prior-Art Expert 负面评价可发表性，二者不冲突（设计好 ≠ 主张新）。Decisive reject axis：见 fatal gates。Final calibrated stance：needs-literature-search（novelty 决策关键且检索不足）；tournament rank 1 / 最佳可救方向。

## Rubric scores

| Dimension | Weight | Score (1-5) | Confidence | Deduction / evidence basis / repair condition |
|---|---:|---:|---|---|
| Problem importance | 12 | 3 | 低 | 锚点：对 CVPR 视觉主轨这是方法内问题，缺一个视觉任务上无法被现有模型解决的命名瓶颈；修复：绑定到变速/高速光流下 rate-code 模型的系统性退化并给出量化证据。 |
| Novelty against likely prior work | 14 | 3 | 低 | 锚点：2508.16792 与动态方向表征两篇仅来自平台 AI 清单、未核验；按 strict-idea-review 第 126 行，novelty 决策关键且检索不足时封顶 3；修复：逐条核验 + 补查 synaptic delay / spike timing / connectome temporal coding。 |
| Conceptual innovation | 12 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Method soundness | 14 | 3 | 低 | 锚点：公开连接表通常不含真实延迟，空间路径→传导延迟的单调关系未验证（平台 AI 自己也写明需改用代理）；修复：预注册代理定义、公开误差上界，claim 降级为结构性时间先验。 |
| Elegance and simplicity | 8 | 3 | 低 | 锚点：三种编码 × 学习/冻结延迟 × 细胞类型常数，网格大且组件必要性未论证；修复：以『延迟是否可学习』为主二元消融，其余降附录。 |
| Feasibility under resources | 8 | 3 | 低 | 锚点：时间展开显存/吞吐未实测，且 10 台 4090 节点全 offline；修复：optic-lobe 子图单 seed 原型测峰值显存，等节点恢复。 |
| Experimental convincibility | 10 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Venue and audience fit | 8 | 3 | 低 | 锚点：SNN 时间编码更接近 NeurIPS/ICLR 或神经形态专场，CVPR 需视觉任务收益；修复：主结果放变速 OOD 光流/方向准确率提升。 |
| Timeliness and topic heat | 6 | 4 | 中高 | 无需扣分：有明确证据支撑，见 closest-work 与专家意见。 |
| Risk-adjusted acceptance potential | 8 | 3 | 低 | 锚点：novelty 未定 + 代理机制可质疑，strict reviewer 可能同时给 already known 与 not biological；修复：补检索 + 预注册代理后重评。 |

> 加权由脚本计算：sum(score × weight)/100 = 3.28；1-10 换算 = 6.56。所有 <=3 分数均给出锚点、扣分理由与修复条件。

## Score-change conditions

完成三条未核验文献核验 + 预注册代理定义与误差上界 + 共享随机初始化对照 + 变速 OOD 光流显著收益：novelty 3→4、soundness 3→4、acceptance 3→4，加权约 +0.5~+0.8，可进 revise 区间；若核验发现直接重复，novelty 降 2 转 pivot。

## Fixability table

| Issue | Affected dimension | Severity | Fix class | Before writing? | Required change | Owner |
|---|---|---|---|---|---|---|
| Serious blockers 第 1 条 | Novelty / acceptance | high | novelty-grounding + problem-refinement | partly | 非重复检索 + 重写中心主张 | ccf-literature-searcher / ccf-idea-optimizer |
| 机制或措辞层面的中心风险 | Method soundness | high | method-redesign | yes | 预注册定义、降级 claim、逐模组评估 | ccf-experiment-designer |
| exp-4090 池当前不可用 | Feasibility | medium | feasibility-check | no（外部） | 等 eligible_nodes>0，先单 seed 原型 | 外部平台 |

## Upgrade / pivot actions（最小可救路线）

把主张从『生物突触延迟』降级为『可审计的结构性时间先验』；主干收缩为共享随机初始化下可学习延迟 vs 无延迟 vs 随机延迟三臂 + 时间反演 + 速度 OOD，optic-lobe 子图单卡 3 seeds 先跑原型。

## Evidence that would change my score

见 Score-change conditions；所有条目要求可落盘证据（非重复检索表、预注册协议、实测指标或配对表），口头声明不改变分数。

## Checklist status

1 venue/assumptions 明确 PASS｜2 问题-方法卡 PASS｜3 文献状态标注 PASS｜4 closest-work 表 PASS｜5 五角色独立 PASS｜6 十维度全评分且 <=3 有扣分/修复 PASS｜7 致命与可修复分离 PASS｜8 confidence 独立 PASS｜9 推荐词来自协议集合 PASS｜10 未调用被禁模块 PASS。

## Output self-check

表格列数一致；分数由脚本计算并复核；无未填字段；无「有一定创新性/建议进一步完善」类空话；每条批评带锚点。

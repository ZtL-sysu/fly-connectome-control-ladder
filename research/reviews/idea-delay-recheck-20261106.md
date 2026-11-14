# CCFA idea 复核：形态约束的时间动力学（2026-11-06）

## 结论

- **Current version：5.16/10（weighted 2.58/5）**；这是 idea readiness 分，不是论文全文分或接收概率。
- **Recommendation：pivot-with-rescue-route**。不满足 >8/10 门槛，不进入 guidance、训练或写作。
- 复核对象：用 MaleCNS 视觉图和形态信息设定细胞类型共享突触延迟/膜时间常数，以 SNN/GNN 做运动视觉，主证据拟为变速 OOD 光流、时间反演和事件预算。
- 搜索后，新颖性不再是“没找到直接工作”的未知状态：果蝇运动视觉的延迟/非延迟通路已研究多年，通用 SNN 的可学习时延也已有方法，connectome 约束模型的方向表征及 event optical-flow SNN 正在快速扩展。

## 关键近邻

| 工作 | 来源/年份 | 已覆盖内容 | 对当前 idea 的影响 |
|---|---|---|---|
| A visual motion detection circuit suggested by Drosophila connectomics | [Nature/PMC, 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3799980/) | 果蝇视觉运动检测中以空间偏移输入和差分时间延迟形成方向选择性的电路假设。 | “延迟是果蝇视觉运动机制”不是新 insight；剩余贡献必须落在新颖、可验证的结构先验或 CV 能力上。 |
| Processing properties of ON and OFF pathways for Drosophila motion detection | [Nature, 2014](https://www.nature.com/articles/nature13427) | 实测 Mi1、Tm3、Tm1、Tm2 对 ON/OFF 延迟与非延迟通路的处理。 | 当前方案若只重新实现 delay/non-delay 视觉通路，novelty 很低。 |
| Excitatory and inhibitory neural dynamics jointly tune motion detection | [PMC, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9474608/) | 通过操控果蝇运动检测细胞的离子通道和动力学，研究时间整形对方向检测的作用。 | 细胞类型动力学与运动性能的联系已有实验支撑；模型需解释超出已知类型动力学的贡献。 |
| Connectome-constrained networks predict neural activity across the fly visual system | [Nature, 2024](https://www.nature.com/articles/s41586-024-07939-3) | 连接组约束、神经动力学和任务训练结合，使用光流任务，并展示多种可学习模型变体。 | SNN/DMN + optic-flow 本身不是 novelty delta。 |
| Adapting to time: Why nature may have evolved a diverse set of neurons | [PLOS Computational Biology, 2024](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012673) | 在 SNN 中联合优化轴突延迟、突触时间常数、bursting 与权重，评估时间任务。 | “让时延可学习能提升时序任务”已经是通用 SNN 研究方向。 |
| Temporal Spiking Neural Networks with Synaptic Delay for Graph Reasoning | [arXiv:2405.16851](https://arxiv.org/abs/2405.16851) | 将突触延迟和时间编码用于图推理 SNN。 | GNN/SNN + synaptic-delay 组合也并非空白。 |
| Range-Limited Scale Stability of Dynamic Direction Representations in a Connectome-Constrained Fly Visual Model | [Neuroinformatics, 2026](https://pubmed.ncbi.nlm.nih.gov/42627449/) | 在 connectome-constrained fly vision model 中研究动态方向表征的尺度泛化，发现稳定性有范围边界。 | 直接占用 connectome visual dynamics + scale/OOD 方向；新方案不能只把 OOD 设为速度/尺度变化。 |
| SICAF: Time-Varying Focus Bottleneck for Self-Supervised Event-Based Optical Flow with SNN | [arXiv:2610.29158](https://arxiv.org/abs/2610.29158) | 提出自监督 event optical-flow SNN，并报告噪声和对抗条件下的鲁棒性。 | 降低了以 event-flow 鲁棒性为主要 CV 贡献的空间。 |
| Graph Neural Network Combining Event Stream and Periodic Aggregation for Low-Latency Event-Based Vision | [CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Dampfhoffer_Graph_Neural_Network_Combining_Event_Stream_and_Periodic_Aggregation_for_Low-Latency_Event-based_Vision_CVPR_2025_paper.html) | event stream 与 periodic aggregation 的低延迟 GNN 光流路线。 | 新稿需超越已有 CVPR event-GNN，而非只把图换成 connectome。 |
| FlyHack: Stress-Testing Mechanistic Claims in a Connectome-Constrained Visual Model | [arXiv:2610.13018](https://arxiv.org/abs/2610.13018) | 对 flyvis 进行多模型、task-matched CNN、干预和机制稳健性压力测试。 | 单做机制消融与视觉基线不够形成新评测贡献。 |

## 新颖性剩余量与阻断点

最窄的可辩护差异是：**用可审计的 MaleCNS 神经元路径/形态作为时序先验，检验事件视觉速度分布外推是否优于同初始化、同参数量和严格图零模型。**但还存在三个断点：

1. 形态路径长度不是生理传导延迟的直接测量；如果不把该代理和真实神经响应校准，论文只能称“结构性时间先验”，不能称“生物突触时延”。
2. 即使视觉性能有增益，也需要排除多参数、时间展开或随机稀疏结构带来的收益；既有 connectome 拓扑审计和 FlyHack 都提高了对照要求。
3. 变速 OOD 光流仍与 connectome 方向表征和 event-flow SNN 接近；需要一个清楚且不可由现有方法复现的 CV 能力，才能达到 CVPR 主会的贡献强度。

## 五角色独立判断

- **Field Expert**：问题具体但当前把经典飞行昆虫延迟电路重新作为“新机制”。最小修复：声明要解释的未解误差模式，并证明现有 flyvis / direction-scale 工作无法覆盖。
- **Method Expert**：形态代理与真实时延之间缺少可验证映射；可学习时延已是通用 SNN 方法。最小修复：用已标注神经响应估计/约束代理，并公开敏感性区间。
- **Experiment Expert**：时间反演、随机延迟、matched graph null 是可判定设计；但缺少真实活动校准和最新 event-flow SNN 强基线。最小修复：先完成响应拟合与同预算强基线协议，再谈模型性能。
- **AC / Venue Expert**：如果主贡献只是 connectome/neuroscience 的动力学复现，CVPR 适配弱；必须把视觉分布外能力、算力/延迟或新 benchmark 做成首要结论。
- **Skeptical Prior-Art Expert**：连接组延迟视觉机制、可学习 SNN 延迟、connectome 动态方向表征和 event-flow SNN 分别已有近邻。当前差异像组件组合，不像可独立审稿的 insight。

## 量化复核

| Dimension | Weight | Score (1–5) | Evidence / deduction |
|---|---:|---:|---|
| Problem importance | 12 | 3 | 变速视觉有意义，但 idea 未证明现有方法在哪个具体现象上失败。 |
| Novelty | 14 | 2 | 经典果蝇延迟线路、SNN 时延学习、2026 connectome 方向表征和 SNN event-flow 工作均近邻。 |
| Conceptual innovation | 12 | 3 | 结构先验可形成可检验假设，但当前主要是将已知时延机制与既有任务组合。 |
| Method soundness | 14 | 2 | 形态距离→传导时间未经验证；缺活动拟合会使机制解释欠定。 |
| Elegance | 8 | 3 | 延迟对比清晰，但还需区分 delay、膜常数、时间展开和图稀疏效应。 |
| Feasibility | 8 | 2 | 计算子图可行，但关键数据/4090 worker 尚未可调度，形态和活动对齐也未实证。 |
| Experimental convincibility | 10 | 4 | 已有明确证伪组；补齐最新强基线后可以判定中心主张。 |
| Venue fit | 8 | 2 | 目前更像计算神经科学/神经形态研究，CVPR 需要更强的视觉能力贡献。 |
| Timeliness | 6 | 3 | connectome 与 event vision 都活跃，但同题密度上升。 |
| Risk-adjusted potential | 8 | 2 | novelty、机制映射和 CVPR 主张三项同时有高风险。 |

加权分：`2.58 / 5 = 5.16 / 10`。该分数是本地 CCFA idea 复核，不是模型输出、实验结果或论文全文评分。

## 最小 rescue route

保留“时间结构是否带来可迁移视觉能力”这个可证伪问题，先暂停“形态推导生理延迟”的措辞。只有同时满足下列条件，才值得再做 idea review：

1. 用官方 MaleCNS/FlyVis 数据明确一类可重复的速度 OOD 视觉失败，并复现至少一个强 event-flow SNN、CVPR event-GNN 和 connectome DMN；
2. 共享参数初始化与训练预算，显示 MaleCNS 结构性时间先验优于无延迟、随机延迟、度保持图和通用可学习时延；
3. 用公开神经活动记录检验该时间先验对细胞类型响应的预测，而不是只看下游光流误差；
4. 结果形成独立于“换生物图/加时延”的视觉方法贡献。

任一前置条件失败，就放弃这条方向作为 CVPR 主会 idea。当前不生成 smoke，因为 idea gate 未通过，4090 worker 也不可用。

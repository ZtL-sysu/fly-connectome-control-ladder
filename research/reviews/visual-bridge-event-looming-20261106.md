# CCFA idea review — 视觉输入到 MaleCNS 的事件 looming 桥接

## Verdict first

- **加权分：3.14/5 = 6.28/10**；未达到项目设定的 >8/10 idea gate。
- **阶段判断：**有明确可复现的系统断点，development potential 中等；CVPR readiness 低。
- **置信度：中高。**关键近邻包括同行评审的果蝇启发 looming 方法、事件相机 TTC 工作，以及近期 connectome/whole-brain 相关预印本和公开工程项目。
- **建议：pivot-with-rescue-route。**暂不写 guidance、不跑训练或远程 GPU 实验。若能把“视觉输入映射与连接组传播的诊断”升级为跨设备、跨场景可复用的 CV 方法，再重新评审。

## 目标与假设

目标按 CVPR 主会视觉方法评审；工作主题为 MaleCNS/connectome × GNN/SNN × visual computing。拟用事件相机的稀疏异步输入，经视网膜/视叶映射进入 MaleCNS 的时序图网络，以 descending/GF 相关 readout 预测 looming 事件的 time-to-collision (TTC)。MaleCNS 不包含真实相机或生物眼部传感器，像素/事件到光感受器的映射必然是需要建模、并受 matched baseline 约束的输入接口。

## 规范化 idea

**问题：**异步事件图像中的膨胀边缘能否通过解剖约束的果蝇视觉通路，稳定地产生碰撞时间估计？

**缺口：**事件视觉已有 TTC 任务与数据；果蝇的 LPLC2/GF looming 机制已有计算模型；连接组全脑模型也已接收手工设定的视觉/looming 输入。当前可能的差异只在于像素事件到全 MaleCNS 视觉路径的具解剖约束、时间保真桥接，并用真实 TTC 标签评估。

**机制草图：**事件时空坐标 → 按复眼几何映射到视网膜采样点 → 事件/膜电位状态驱动 MaleCNS optic-lobe graph → LPLC2/GF 或 descending readout 预测每对象 TTC 与碰撞概率。关键假设是：时间精确的输入映射能避免稀疏膨胀边缘在前端聚合时消失；这必须与 frame/rate 输入、非生物事件 GNN、经典 fly-inspired loom detector 匹配比较。

**视觉证据草图：**EvTTC 上 TTC 误差、危险/非危险 AP、决策延迟；按目标尺寸、膨胀率、照明、背景运动分层；留出场景/相机运动评估泛化。主张不得扩展为“果蝇大脑解决通用视觉”或生物真实性已经验证。

## Closest work / novelty delta

| 工作 | 来源/状态 | 已覆盖部分 | 剩余差异及风险 |
|---|---|---|---|
| *A fly inspired solution to looming detection for collision avoidance* | iScience 2023，同行评审，[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10073940/) | T4/T5 → LC/LPLC2 → GF 的果蝇启发网络，用于 looming/碰撞检测。 | 候选的 task 与线路机制非常接近。差异仅为事件输入和全 MaleCNS 图传播；若无 matched CV 结果，很像系统拼接。 |
| *Event-Aided Time-To-Collision Estimation for Autonomous Driving* / EvTTC | ECCV 2024，[论文项目页](https://nail-hnu.github.io/EventAidedTTC/)；另有 EvTTC 数据集论文 | 事件相机 TTC 估计和公开数据/评测。 | 直接覆盖相机模态与核心输出目标；候选必须显著优于强事件视觉基线并展示不同技术能力。 |
| *NeuroGraphBench* | **Frontiers in Computational Neuroscience 2026，已同行评审**，[期刊记录](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2026.1975699/abstract) | 通过 LPLC2 环状群体响应和 GF 双树突读出区分 direct-hit/near-miss，并包含碰撞时序分析；论文于 2026-11-04 接收。 | 对“connectome + looming + TTC”是直接且已发表的重叠，不再只是预印本风险；候选的中心视觉线路/问题进一步被覆盖。 |
| FlyBench task 32 | 社区 [GitHub 工程/实验记录](https://github.com/brandoncho369/flybench) | 使用 FlyVis 预训练视觉模型输入、驱动 connectome T4/T5/Tm；作者报告 loom 未到达 LPLC2/LC4/GF，而全场 flash 可触发 GF。 | 这是候选动机的直接先例，也是独立复核必要性警报；GitHub 自报结果，不等于独立复现或同行评审。 |
| FlyGM, *Whole-Brain Connectomic Graph Model Enables Whole-Body Locomotion Control in Fruit Fly* | arXiv 2026，[预印本](https://arxiv.org/abs/2602.17997) | 完整果蝇 connectome 作为 GNN 控制身体运动，已有 degree-preserving/random/MLP controls。 | “whole connectome + GNN + body/action control”不能作为独立 novelty。 |
| Minnick et al., *Sensorimotor behaviour from an untrained brain-and-nerve-cord connectome* | arXiv 2026，[预印本](https://arxiv.org/abs/2610.33881) | connectome SNN 通过 looming 输入和模拟身体完成避障导航，并报告 rewiring 与 sensory-off controls。 | 生物接线全脑视觉到行为闭环已有直接证据；候选必须从 locomotion/避障任务移开，聚焦新的视觉预测能力。 |

**Novelty delta：**当前只剩“时间保真的事件相机输入接口 + MaleCNS 视觉路径 + TTC 定量 CV 基准”。但前端的果蝇 looming 算法、事件 TTC 任务、全脑 connectome 行为控制分别已存在；三个模块拼接并不足以证明 CVPR 方法贡献。若无法提出新的输入/传播机制及相对于事件 GNN、FlyVis、rate-based connectome 的显著可迁移优势，idea 会被认为是 integration study。

## 专家评审意见

- **视觉领域：**TTC 是清楚的视觉任务，但已有事件 TTC 数据与方法。拒稿级问题是模型是否超越事件流运动几何的直接估计；只有神经活动可视化不能回答。
- **图/SNN 方法：**异步映射与稀疏图传播有结构合理性；但“把事件编码成 spikes 再跑 LIF”是标准组合。需要提出可学习但可解释的光感受器/视叶输入校准机制，且验证它不是额外参数/预处理优势。
- **实验设计：**EvTTC 可作为公开标签入口；需按场景拆分，补不同扩张率/物体尺度/背景运动分层，并比较 FlyVis、经典 looming、事件 GNN、ConvLSTM/Transformer 与简化零模型。真实事件是否覆盖 fly-like looming 的空间/时间条件还待查。
- **CVPR AC 视角：**完整 connectome 和生物灵感会吸引兴趣，但 venue 会要求一般计算机视觉方法贡献与强基线。单一 TTC 任务、一个动物模型和自述 connectome readout 容易被归为 niche neuromorphic application。
- **怀疑先例的审稿人：**果蝇启发碰撞检测（2023）与 NeuroGraphBench 的线路任务直接邻近；FlyBench task 32 已指出输入桥接失败。最有力的反驳不是“我们用完整 MaleCNS”，而需展示可重复的、超越已知方法的视觉能力。

## Rubric

| 维度 | 权重 | 分数 / 5 | 扣分依据与修复条件 |
|---|---:|---:|---|
| 问题重要性 | 12 | 4 | 低延迟碰撞预测有视觉/机器人意义。 |
| 相对新颖性 | 14 | 2 | 果蝇 looming 模型、事件 TTC、whole-brain looming 控制已覆盖核心问题；需要非组合式新机制。 |
| 概念创新 | 12 | 3 | 时间保真桥接可检验，但目前是接口集成；需从通路结构导出新的事件聚合/分配准则。 |
| 方法可靠性 | 14 | 3 | retina/photoreceptor 映射和 MaleCNS dynamics 是未确定假设；需定义输入校准、延迟和 readout。 |
| 简洁性 | 8 | 4 | TTC 单任务、单一主张较聚焦。 |
| 资源可行性 | 8 | 3 | 数据规模可控，但全脑时序模拟和 4090 当前不可用会增加周期；可先小子图。 |
| 实验证据说服力 | 10 | 4 | 有 EvTTC 与 TTC 指标入口，但 fly-like 条件覆盖和视觉真实场景待核实。 |
| CVPR 适配度 | 8 | 3 | 需比生物应用更一般的事件视觉贡献；目前范围偏窄。 |
| 时效性 | 6 | 4 | Event vision 与 MaleCNS 均活跃，近邻拥挤。 |
| 风险调整后潜力 | 8 | 2 | 高概率被评为已有 looming/TTC 方法的生物线路复现或系统集成。 |

加权分：`(12×4 + 14×2 + 12×3 + 14×3 + 8×4 + 8×3 + 10×4 + 8×3 + 6×4 + 8×2)/100 = 3.14/5`，换算 `6.28/10`。分数是 idea-stage 诊断，不是论文 Overall。

## 最小救援路线

1. 先读完 NeuroGraphBench、Minnick et al. 和 FlyBench task 32 的方法/代码，确认真实输入如何映射、其 readout 是否包含 TTC。
2. 若仍有缺口，把问题收窄为“事件时空编码如何在全脑稀疏图传播中保留 TTC 可观测性”，提出有理论可检验的充分条件或新型输入门控，而非另一个 LIF loom detector。
3. 与 EvTTC 强基线和已有飞行/避障 connectome 模型做完全匹配评测；以跨相机/跨场景 TTC 泛化为主张，神经读出只作机制证据。
4. 通过新增方法后重新 CCFA idea review；重新评审前不跑训练，不占用 4090。

## 状态

本 idea **未通过 >8/10 gate**。后续核验把 NeuroGraphBench 从“预印本警报”更正为已发表同行评审论文（Frontiers 页面列出两位匿名审稿人，accepted 2026-11-04）；这加强了 pivot 理由，但不改变原 rubric 数值。当前不生成 guidance，不接 f-research 流水线，不宣称有 smoke 或科研实验结果。Novix 的先前研究请求被自动审核拒绝，本文由本地公开文献证据形成，没有通过改写请求来绕行。

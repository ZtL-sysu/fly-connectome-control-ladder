# CCFA Idea Review — 果蝇并行视觉通路分歧用于事件目标跟踪置信度

日期：2026-11-06  
模式：ccf-idea-reviewer standard；目标：CVPR 2027 主轨；阶段：idea seed。  
结论：**当前表述 4.68/10，不通过项目 idea gate（>8/10）**。不建立 guidance，不开始 smoke 或论文链。

## 待评 idea

在 Drosophila connectome 约束的 GNN/SNN 中显式建模并行视觉通路，让通路输出分歧成为事件相机目标跟踪置信度信号；重点预测遮挡、背景自运动和高速运动下的跟踪失败，并在公开事件跟踪基准上评估校准、失效预警和选择性跟踪。

这是待审候选的规范化版本，不是 Novix 交付。Novix 对应 idea 请求被自动安全审核拒绝，未产生 idea 文件或模型回答。

## 检索依据与最近邻

采用公开关键词检索；检查了论文/项目公开页与可访问摘要。事件跟踪及 connectome/CV 相关项覆盖较好，但尚未逐篇全文核对置信度方法的实现细节，因此文献覆盖标记为 **partially searched**，置信度为中等。

| 最近邻 | 已有工作 | 与本 idea 的重叠和剩余差异 |
|---|---|---|
| [FlyVis / Lappalainen et al., Nature 2024](https://www.nature.com/articles/s41586-024-07939-3) | Connectome-constrained optic-flow 模型；提供 50 个满足同一 connectome 约束并执行同一任务的模型 | 已有生物连接组视觉模型及模型族。候选新增的是把通路分歧用于 tracker correctness 校准；但“ensemble disagreement”作为不确定性来源本身不新。 |
| [FlyHack, arXiv:2610.13018](https://arxiv.org/abs/2610.13018) | 在 FlyVis 50-model ensemble 上比较机制干预、模型表示、task-matched causal CNN 与跨模型稳定性 | 直接覆盖“并行/不同模型输出差异能否成为机制信号”的严格比较期待。该预印本尚非同行评审；即使如此，审稿人会要求与其 50 模型、干预及匹配 CNN 设计正面对照。 |
| [EventVOT, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Event_Stream-based_Visual_Object_Tracking_A_High-Resolution_Benchmark_Dataset_and_A_Novel_Baseline_CVPR_2024_paper.html) | 建立高分辨率事件流视觉目标跟踪基准与新 baseline | 提供直接任务与数据基准；本 idea 不拥有新的 tracking task/benchmark，必须在其基线上证明可校准的失败预测增益。 |
| [ETAP, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Hamann_ETAP_Event-based_Tracking_of_Any_Point_CVPR_2025_paper.html) | 事件相机任意点跟踪 | 继续压缩事件跟踪的方法空间；仅增加置信度输出不足以形成 CVPR 主贡献。 |
| [Model Uncertainty Guides Visual Object Tracking, AAAI 2021](https://ojs.aaai.org/index.php/AAAI/article/view/16473) | 以跟踪模型不确定性调节在线样本选择，处理遮挡/模糊造成的跟踪丢失 | 已把 tracking uncertainty 与在线跟踪策略结合；候选的区别只能落在经过校准的事件流失效概率和 connectome 双通路机制。 |
| [Detecting Object Tracking Failure via Sequential Hypothesis Testing, WACV 2026 workshop](https://openaccess.thecvf.com/content/WACV2026W/RWS/papers/Munoz_Detecting_Object_Tracking_Failure_via_Sequential_Hypothesis_Testing_WACVW_2026_paper.pdf) | 以序贯假设检验检测跟踪失败，并控制误报率 | 已有明确的 failure alert 目标和保证；本 idea 需优于统计检测器，且证明 connectome/SNN 的分歧信号提供独立增益。 |
| [Salem et al., J. Exp. Biol. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7272343/) | 果蝇在视野背景产生自运动幻觉时仍能追踪目标，支持并行视觉运动处理 | 生物动机真实，但研究问题“背景自运动与前景追踪可并行处理”已由行为实验直接涉及。新增的 CV 算法机制仍需独立证明。 |
| [ConnectomeX, arXiv:2610.08418](https://arxiv.org/abs/2610.08418) | 2026-10 预印本把 connectome-informed FlyVision 扩展到 MNIST、CIFAR、ImageNet、医学影像等通用视觉任务 | 广泛覆盖“将果蝇视觉 connectome 用于新 CV 任务”的应用主张。它是预印本，不能当同行评审结果，但新任务迁移本身很难再作为 novelty delta。 |

## Novelty delta

去掉已有 connectome-constrained motion vision、50 模型机制/干预比较、事件跟踪基准、不确定性跟踪与序贯失效检测后，剩余主张是：**用生物双通路分歧特征，学习事件跟踪正确概率，并在遮挡/ego-motion 下预警失败。**

当前没有证据说明双通路差异比普通 ensemble variance、跟踪器内部置信度、现有序贯检测器或事件特征质量指标更有信息。也没有指定公开基准上具有足够难度且现有方法失败的 protocol。因此 novelty delta 存在，但目前很窄，依赖未经证明的增益。

## 审稿风险与救援路线

- **核心机制未证实：** 通路分歧可能只反映模型 ensemble 方差或输入噪声；需要在相同参数/算力预算下优于随机双支路、单路加 ensemble、普通置信度头和序贯检测器。
- **生物证据与 CV 监督脱节：** 果蝇并行通路的行为证据不等于其输出能校准现代事件 tracker。若只用追踪标签训练 calibrator，connectome 可能成为装饰性 backbone。
- **现有目标拥挤：** EventVOT/ETAP 已提供任务与强基线，AAAI 已用 uncertainty 调节 tracker，WACV 已直接做失败检测。仅多报 ECE/Brier 或遮挡切片不足以支持 CVPR 新方法。
- **最佳救援路线：** 把中心问题收窄为“运动背景与前景对象共存时，connectome 分解的运动/图形通路能否产生可迁移、低误报的跟踪失效统计量”；预注册跨数据集/跨 tracker 测试，做冻结与训练两种协议，并将真实 fly physiology/行为响应作为独立约束。即使如此，仍需先做全文 closest-work 检索和公开数据可用性核实。

## 独立专家意见

- **Field Expert：** 强点是背景自运动下稳定追踪有实际意义，且果蝇有并行处理行为证据。拒稿点是生物现象与新 tracker 之间缺少因果桥；行为论文没有证明 connectome 分歧能预测 AI 跟踪失败。最小改动：具体定义该生物机制导致的 CV 统计量，并在多个 tracker 上迁移验证。置信度：中高。
- **Method Expert：** 分歧→正确概率在概念上可实现，但未区分 epistemic、aleatoric 与系统性偏差，也未定义在线校准目标。最小改动：锁定错误事件、概率估计对象和因果对照；否则只是把 uncertainty feature 拼入 head。置信度：中。
- **Experiment Expert：** EventVOT/ETAP 可提供任务锚点，WACV 序贯检验可作强基线。拒稿点是没有基准协议、split、失效定义及跨 tracker 证据，容易数据集内校准。最小改动：预定义按遮挡、ego-motion、速度切片的风险—覆盖曲线、校准误差、提前预警时间与误报率，并跨数据集验证。置信度：中。
- **AC / Venue Expert：** 事件视觉跟踪匹配 CVPR 社区，但 CVPR 会问新算法对 tracking 主指标或可靠部署的实质改善。若主要贡献只是辅助置信度估计，可能被认为是模块级应用或 workshop 工作。最小改动：证明置信策略改善端到端跟踪/重捕获且提供稳定的跨域安全收益。置信度：中。
- **Skeptical Prior-Art Expert：** 最强拒稿意见是该 idea 将 FlyVis 的并行机制、已有事件 tracker、模型不确定性与 tracking-failure detection 拼接；目前没有证据显示组合产生新能力。最小改动：相较上述方法提出并验证不可由通用 uncertainty/序贯检验替代的机制性预测。置信度：中高。

## Rubric 与加权分数

| 维度 | 权重 | 分数 / 5 | 信心 / 5 | 扣分依据与变化条件 |
|---|---:|---:|---:|---|
| 问题重要性 | 12 | 4 | 4 | 跟踪失败预警有明确 CV 价值；若能定义现实部署决策将更强。 |
| 新颖性 | 14 | 1 | 3 | 多条最近邻已分别覆盖 connectome vision、uncertainty tracking、failure detection；需证明双通路提供不能由普通统计方法替代的增量。 |
| 概念创新 | 12 | 2 | 3 | “通路分歧→置信度”目前是机制启发式特征，没有新的统计或学习原理；需形成可证伪的跨 tracker 预测。 |
| 方法可靠性 | 14 | 2 | 3 | 未定义概率标签、校准协议、分歧归因；需预注册目标和强控制组。 |
| 简洁性 | 8 | 3 | 3 | 两通路加轻量校准器可简洁，但不确定性分解会引入额外部件；需消融证明必要性。 |
| 资源可行性 | 8 | 3 | 4 | 单卡 4090 可做公开基准上的 SNN/校准实验，但池目前不可调度，且数据许可/下载仍待核查。 |
| 实验证明力 | 10 | 3 | 3 | 评测可执行，但缺少多数据集、跨 tracker 设计和合理错误标签；需达到上述 protocol。 |
| CVPR 匹配度 | 8 | 2 | 3 | 任务匹配，贡献尚像置信度附加模块；需显示端到端跟踪质量或可靠部署收益。 |
| 时效性 | 6 | 3 | 4 | EventVOT、ETAP 与 2026 connectome-to-CV 工作表明题目活跃，也显示迅速拥挤。 |
| 风险调整后的接收潜力 | 8 | 1 | 3 | 关键 novelty 与机制风险未解决；需要非替代性增益和复现证据后才能上调。 |

加权分 = 2.34/5；换算 4.68/10。分数是 idea 阶段诊断，不是论文全文评分或接收概率。置信度：中等（检索覆盖了直接任务与连接组近邻，但未完成所有相关置信度方法的全文比对）。

## 结论

**Current readiness：低。Development potential：低至中。推荐：pivot-with-rescue-route；不通过 >8/10 idea gate。** 目前不进入 `f-guidance-builder-v1`、`f-research-v1`、训练或写作。只有发现可复现的“connectome 分解统计量”并在跨数据集、跨 tracker 上显著优于通用不确定性/序贯检测器，才值得重新提交 CCFA idea review。

资源复核：本机 `scripts/check_4090.py` 于 2026-11-06 18:26 CST 返回两台 4090 worker offline、`usable_nodes=[]`、dispatch 未暂停；不得提交 GPU smoke。

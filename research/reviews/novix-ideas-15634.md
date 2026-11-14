# Novix 候选方向 CCFA idea review

**目标视角：** CVPR 主会 computer vision idea；评分只评价 idea readiness，不代表论文 P9 full review，也不是接收概率。用户设定的继续门槛是 idea review **>8/10**。

**证据状态：** 已检索并核对公开 primary sources；题目和 smoke 为 Novix 交付物。报告中的判断是本地 CCFA reviewer 独立评分。Novelty confidence 与分数分开记录。

## 结论

五个候选都低于 >8/10 门槛，目前没有方向进入 guidance / paper-writing 阶段。最高分 E 是事件视觉 SNN 的应用组合，但最近工作已经覆盖事件相机光流 + SNN，且与项目之前的方向性 SNN 相撞；它不适合作为旗舰 idea。发展潜力相对最高的是 A，但其“跨重建迁移”贡献紧邻 2026 年的果蝇连接组重建敏感性研究，视觉模型侧又紧邻 FlyHack，且当前未找到与图和神经数据配对的跨动物视觉标签。

Novix 报告给 A 自评 8.2/10；本评审为 **4.88/10**。核心差异：报告把「已有工作指出的问题」视作新贡献，却还没有提出解决该问题的新算法机制、CVPR 可验证的视觉任务，或可支撑该任务的跨 connectome 标注。

## 搜索与 closest work

搜索使用公开、通用关键词；确认了果蝇视觉 connectome 建模、连接组重建差异、干预稳健性、MaleCNS 资源和果蝇视觉行为数据。以下近邻足以显著改变 Novelty 和 Venue-fit 评分：

| Closest work | 已覆盖内容 | 对候选的影响 | 仍可能成立的 novelty delta |
|---|---|---|---|
| Lappalainen et al., Nature 2024, [connectome-constrained visual networks](https://www.nature.com/articles/s41586-024-07939-3) | 具生物约束的果蝇 optic-lobe 视觉网络，学习 optic-flow 行为任务并预测神经活动。 | A/C/E 的“连接组视觉模型 + 时序视觉任务”已有直接先例；不能把采用视觉任务和 GNN/SNN 本身作为新颖性。 | 需要新的、明确的 CV 任务与此前没有的解决机制，且有实数据增益。 |
| Dhawan, arXiv 2026, [FlyHack](https://arxiv.org/abs/2610.13018) | 对 FlyVis 的 50 个模型、task-matched causal CNN、视觉干预和机制结论做系统压力测试；研究干预、表示和训练解变化。 | B 的干预 benchmark、E 的模型/视觉鲁棒性，以及 A 的“把机制结论做成稳健评测”都与之相邻。Novix 初稿未列入。 | 需证明独特问题超出 FlyHack 的 optic-flow、机制干预和模型集分析，而不是换测试协议。 |
| Borowiecki et al., arXiv 2026, [reconstruction differences break fly compass models](https://arxiv.org/abs/2610.29205) | 比较多种果蝇头向 connectome 与同一只 fly 的重建变体；发现模型跨重建迁移失败，且小的 wiring change 可破坏已训练模型。 | A 的 central claim“跨 connectome 泛化与重建不确定性”已被非常接近地提出并实证（虽是 compass 而非 vision）。 | 只有视觉任务上的新机制、新评测或跨 reconstruction 生物验证能留下足够 delta。 |
| Berg et al., Cell 2026, [Male CNS connectome](https://doi.org/10.1016/j.cell.2026.08.015) 与[官方资源页](https://male-cns.janelia.org/download/) | MaleCNS 提供全 CNS 图、视觉/运动通路注释和跨数据集 cell-type 线索；连接图文件 1.1 GB。论文指出连接数据不等于功能 ground truth，proofread 端点覆盖也有限。 | 支撑题目和小型子图可行性，但没有提供视频—神经活动同步标签；整图及 synapse 数据也比候选卡的轻量表述复杂。 | 将 cell type 对齐、不确定性及真正的 held-out functional measurement 设计成具体方法。 |
| Nern et al., Nature 2025, [complete male visual-system inventory](https://www.nature.com/articles/s41586-025-08746-0) | 完整雄性视觉系统 cell-type inventory；与雌性 FlyWire 的视觉 cell types 有高度匹配。 | 使跨性别视觉 cell-type 对齐在解剖层面可行，但不能消除性别、动物、重建流程和功能标签差异。 | 要把对应关系作为可审计的 uncertainty，而不是把图视为同一图的 noisy copy。 |
| Shiu et al., Nature 2024, [computational brain model](https://doi.org/10.1038/s41586-024-07763-9) 与 [visual-neuron population code](https://www.nature.com/articles/s41586-024-07451-8) | 连接组计算模型描述 sensorimotor transformation；已有工作将视觉模型单元映射到视觉神经元并分析雄蝇社会行为。 | C/D 的视觉—动作预测和视频/神经解释已有相邻路线。 | 需公开的未见动物视觉任务、可测机制增益及独立 CV 方法贡献。 |
| Eyjolfsdottir et al., ECCV 2014, [Fly-vs-Fly dataset](https://data.caltech.edu/records/zrznw-w7386) | 22 小时、专家标注的果蝇社交行为视频和姿态轨迹；完整文件集 44.2 GB。 | 有行为视频，但没有与 MaleCNS 个体同步的神经活动；不能直接当作跨 connectome 的视觉功能标签。 | 先验证具体视频子集、标签、主体划分及图—行为映射，再声称可检验 graph-conditioned generalization。 |
| Lagorce et al., [event-based optical flow with SNN](https://arxiv.org/abs/2302.06492) | 已把事件相机输入和 SNN 用于 optical flow。 | E 的“事件输入 + SNN + 光流”是已有任务组合；MaleCNS wiring 的加入本身不够构成新贡献。 | 必须引入 CVPR 认为重要、且相对强 SNN/ANN 明确改善的视觉能力。 |

用户提供的 [awesome-fly](https://github.com/cobanov/awesome-fly) 可作为资源索引；Novix 也避开了用户列出的四类工作。本轮检索额外发现 FlyHack，需加入项目 prior-art denylist。

## 候选规范化与分数

权重采用 CCFA `ccf-idea-reviewer` rubric：Problem 12、Novelty 14、Conceptual innovation 12、Method soundness 14、Elegance 8、Feasibility 8、Experimental convincibility 10、Venue fit 8、Timeliness 6、Risk-adjusted acceptance potential 8。每格为 1–5；加权 1–5 分乘 2 得到 1–10。分数不是概率。

缩写：P=问题重要性，N=相对新颖性，I=概念创新，M=方法可靠性，E=简洁性，F=资源可行性，X=实验说服力，V=CVPR 适配度，T=时效性，R=风险调整后潜力。

| 候选 | P | N | I | M | E | F | X | V | T | R | 加权 /10 | 信心 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A 跨 connectome 不变的时序视觉动力学 | 4 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 4 | 2 | **4.88** | 中 |
| B 反事实 connectome intervention benchmark | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 4 | 2 | **4.72** | 中 |
| C neck-connective bottleneck 动作提前预测 | 4 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 4 | 2 | **4.88** | 中 |
| D 图—视频对齐的 few-shot 行为识别 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 4 | 2 | **4.64** | 中低 |
| E 事件视觉 SNN 与不确定性 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 4 | 2 | **5.08** | 中 |

### 逐项否决理由与最小修复

**A — 4.88/10，development potential：中，needs major redesign。** 核心假设是跨 connectome 的视觉迁移，但 2610.29205 已直接证明“果蝇 circuit model 跨重建迁移失败”，FlyHack 又已对连接组视觉模型的干预/解稳定性进行压力测试。方法目前是把 graph-noise augmentation、uncertainty adapter、SNN readout 拼接起来，没有说明 adapter 如何解决两种相互竞争的 variation：技术重建误差与真实性别/个体差异。MaleCNS、FlyWire、hemibrain、MANC 并非同一完整视觉图的多个等价 realization；跨数据集对齐会混入 coverage 和性别差异。CVPR 任务也没有观测图节点活动的标注。修复条件：先在明确同源、同视觉区域的 cell-type intersection 上定义一个视觉 benchmark；给出能分离 reconstruction noise 和 biology variation 的方法；证明相较 FlyHack/Lappalainen 的新视觉能力。否则只适合领域内 benchmark/robustness 工作。

**B — 4.72/10，development potential：中低。** “hold out intervention family + calibrated abstention”比展示单个 lesion 更具体，但 FlyHack 已在视觉 connectome 模型上做 replicated interventions、模型族和 task-matched CNN 对照。B 的预测目标还是 synthetic lesion 产生的动作变化，没有真实 paired perturbation 标签；这样只能测内部模拟器是否能拟合自身输出，不能证明干预泛化，更难成为 CVPR 主贡献。修复条件：取得可审计的真实视觉扰动/神经功能配对标签，或把贡献改为能迁移到独立视觉扰动数据的 CV 算法。

**C — 4.88/10，development potential：中低。** MaleCNS 的最大流和 neck connective 是静态结构摘要，不能推出视觉动作的毫秒级先后。Shiu et al. 已做 connectome-based sensorimotor transformation；候选又缺少与视觉输入、脑活动、下行动作同步的数据。若只用静态图生成 bottleneck 再用通用视频模型提前预测动作，图可能只是后验解释。修复条件：先给出真实同步任务和时间标签，并预注册 bottleneck ablation 能区分于行为-only temporal baseline 的方向性假设。

**D — 4.64/10，development potential：低到中。** 图侧 `pathway tokens` 与视频侧表征缺乏真实对应关系；把 cell-type token 接到视频 encoder 目前更像提示特征拼接。Fly-vs-Fly 有可用的行为视频，但不含同一 fly 的 connectome 或神经记录；cross-animal split 不能补出缺失的 biological alignment。修复条件：建立可追溯的视觉刺激—cell-type response 数据配对；否则移除 connectome token 这一主张，届时不再满足本项目范围。

**E — 5.08/10，development potential：中。** 已有事件相机 SNN 光流；用户也已要求避开方向性 SNN 近邻。MaleCNS 结构映射到 event camera 的节点/参数关系尚未定义，energy/latency Pareto 曲线属于常见评测，而不是新 insight。修复条件：指出连接组相对已有 SNN 光流模型带来的非平凡新能力，并用参数/FLOPs/SynOps 严格匹配的强 baseline 证明；否则换题。

### 五位 reviewer 独立意见

- **领域专家：** A 最贴近果蝇 visual connectomics，但没有把静态 connectivity 和视频行为之间的功能映射补上。先限定 visual cell-type intersection 并寻找功能 readout。
- **方法专家：** A 的 uncertainty adapter 没有可识别的学习目标，也没有说明如何区分 technical noise 与 biological variation。先给出显式 latent variation model 和可证伪 calibration claim。
- **实验专家：** 两种候选数据目前并不 paired；无论 accuracy、NLL 还是 ECE，若训练标签来自合成 graph simulator，就只能验证 simulator。先取得按个体/图版本分组的真实 held-out target。
- **CVPR AC/领域适配：** B/C/D 偏计算神经科学 benchmark，A/E 是生物启发方法组合；尚无明确胜过标准视觉模型的能力或 general CV protocol，当前更像 workshop/domain paper。
- **先验工作专家：** A 与 2610.29205 在 robustness across connectome reconstructions 的中心动机高度重叠，B 与 FlyHack 的视觉 connectome intervention tests 相邻，E 与既有 event-flow SNN 重合。将同一方向改成 SNN 或更换数据集不足以拉开 novelty。

## Smoke 复核

Novix CPU/NumPy smoke 使用 12 节点人工分层图、两枚 seed、degree-preserving shuffled control、固定 temporal message passing 和线性 softmax readout。其 `real_graph` OOD accuracy 均值为 0.675、control 为 0.569，transfer gap 均值 0.106、标准差 0.088；单 seed gap 分别为 0.019 和 0.194，结果高度依赖 seed。脚本标签由同一人工图动力学生成，真实图结构就是 teacher，所以这是预期的自洽 toy，不是无偏验证 connectome 优势。

本机使用 conda Python 3.14.6 / NumPy 2.5.1 复跑后，`per_seed` 与 aggregate 数值字段和 Novix 结果完全相同；Novix 环境为 Python 3.11.15 / NumPy 2.4.6。复跑只确认软件可运行及指标可复现。这个 smoke 没有 MaleCNS、视频/图像、真实 neural targets、可训练 GNN、spiking neuron dynamics 或 PyTorch；因此不通过科学 feasibility gate，也不改变以上 idea 分数。

## 决定与下一步

**最终推荐：** 暂停五个候选的 guidance 和写作，不降低 >8/10 门槛。保留 A 中“区分重建不确定性与真实生物差异”作为待救的研究问题；下一轮要求 Novix 先检索并比较 FlyHack、2610.29205、MaleCNS visual inventory 和可用功能数据，再给出至少一个真正不同于这些工作的 CV task/method，不先启动论文。

继续条件：①候选有明确可视化输入、输出和 CVPR 评估目标；②nearest-work delta 在 FlyHack 与重建鲁棒性之后仍清楚；③有真实、可追溯的图—视觉/神经功能数据；④至少一个初步、无 teacher leakage 的 smoke 通过 matched-control 检查；⑤本地 CCFA idea review >8/10。当前五项均未满足，所以没有候选进入 f-guidance-builder 或 f-research。

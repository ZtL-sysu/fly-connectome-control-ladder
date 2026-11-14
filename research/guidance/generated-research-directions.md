# Generated research directions

| timestamp | title | technique | scenario | gate | path | notes |
|---|---|---|---|---|---|---|

| 20261109-181000 | Connectome-Grounded Spiking Motion Vision (candidate family) | GNN 果蝇连接组 + SNN 视觉 | 运动/时序/闭环/结构→功能对齐（18 卡发散，top8 并行原型） | pending G0-G8 | auto-paper/20261109-181000/ConnectomeGroundedSpikingMotionVision/ | 大方向锁定；前 26 链静态分类一致阴性，换正交象限 |
| 20261109-211200 | Connectome-Grounded Spiking Predictive Motion (R82, 14 I-G cards) | GNN 果蝇 MaleCNS 连接组 + LIF-SNN 视觉 | 运动/时序/闭环/结构→功能对齐/脉冲能效；14 卡发散，top8 跨池下发 + 本机独立证据线 | pending G0-G8 | auto-paper/20261109-211200/ConnectomeGroundedSpikingPredictiveMotion/ | 大方向锁定；连续 30 条平台链零数据后启用本机 conda 证据线，首批真实数据为负（positive_result=false） |


## 附录 U — R83（2026-11-09 23:14:35 +0800）第 4 批发散：26 张全新卡 + 24 条链

- 目录：`auto-paper/20261109-225500/ConnectomeGroundedSpikingLesionGeometry/`
- **第一批 14 张 I-H 卡**（`ccfa-startup-packet/idea-cards-R83.md`）：单细胞消融表型 z / looming TTFS ρ / 等性能 SynOps / 拓扑×符号 2×2 / 对比度 AUC / TTFS 编码优势 / **圆形性校正几何残差** / 闭环稳定误差 / 同步谱 / 分层读出 / 未来帧 / 漂移几何 / 标度律 / 时滞×速度。
- **第 6 步 12 张 I-J 卡**（`idea-cards-R83-wave2.md`）：难度剂量斜率 / 连续结构剂量 / Pareto 前沿面积 / 单细胞 T4/T5 调谐对齐 / 类型特异消融 / ON-OFF 分离 / 跨刺激迁移 / 真实事件相机 / 真实光流 / 时间步剂量 / 噪声剂量 / 闭环扰动剂量 AUC。
- 撞车检索：`prior-art-collision-search-R83.md`（含 v5 撤回与圆形性混淆等不利证据）；红队/claim-evidence：`red-team-and-claim-evidence-R83.md`；决策：`scenario-decision-log.md`。
- **本机 8 链**：`papers/R63-results/r83_local/`（8/8 负，独立重算见 `R83-local-independent-audit.md`）。
- **平台 wave1**：19345, 19346, 19347, 19348, 19349, 19350, 19351, 19352；**wave2**：19355, 19356, 19357, 19358, 19359, 19360, 19361, 19362。两波协议 `papers/R63-results/r83_*-protocol.md`。
- 下批池：I-J4 / I-J9 / I-J10 / I-J11；I-J9/I-J10 数据可得性须先验证，不可得须如实终止。


## 附录 V — R84（2026-11-10 00:55:55 +0800）第 5 批发散：14 张全新 I-K 卡 + 换体制

- 目录：`auto-paper/20261110-002000/ConnectomeMaskTrainableSpikingDynamics/`
- **14 张 I-K 卡**（`ccfa-startup-packet/idea-cards-R84.md`）：样本效率 AUC / 收敛步数 / 泛化 gap / 正则斜率 / 训练后 Pareto 面积 / 训练后拓扑×符号 2×2 / 合成延迟×收敛 / 两级零分布（聚类保持重连）/ 稀疏度鲁棒 / control ladder 自我证伪器 / 跨刺激迁移学习效率 / 闭环误差学习曲线 / 结构×SNN 动态 2×2 / 结构剂量斜率。
- **体制变更**：连接组 = 可训练二值结构掩码（W=Θ⊙M），surrogate-gradient BPTT，24 图共享随机初始化；主指标全为学习动态量。
- 撞车检索：`prior-art-collision-search-R84.md`（4 轮 A/B/C 分级，含 Zenodo 与 2604.04033 阴性等不利证据）；红队/claim-evidence：`red-team-and-claim-evidence-R84.md`；决策：`scenario-decision-log.md`。
- **本机 8 链**：`papers/R63-results/r84_local/`（独立重算见 `R84-local-independent-audit.md`）；调试试跑 `r84_m3_TRIAL1_buggy_sensory_RETAINED/` 保留；校准 `R84-feasibility-calibration.md`。
- **平台主批**：19390, 19391, 19392, 19393, 19394, 19395, 19396, 19397；**跨池副本**：19398, 19399, 19400, 19401；**第 6 步 wave2**：19406, 19407, 19408, 19409, 19410, 19411, 19412, 19413。协议 `papers/R63-results/r84_ik*-protocol.md` 与 `r84_il*-protocol.md`。
- **第 6 步 12 张 I-L 卡**（`idea-cards-R84-wave2.md`）：训练后 RDM–图距离耦合 / 神经元专门化 PR / 校正圆形性残差 / 雪崩临界性 / 权重模体 / 抗剪枝与抗权重噪声剂量 / 持续学习保持率 / 跨 seed CKA / 同步谱 / 首脉冲 MI / 绝对脉冲能效 / 迁移学习。
- 下批池（不得复用旧卡充数）：I-K7 / I-K8 / I-K9 / I-K11 / I-K12 / I-K13 与 I-L4 / I-L6 / I-L8 / I-L11；I-K8 需构造 CLUSTER_PRESERVED 图族且必须通过度序列/边数校验。


## 附录 V（R87，2026-11-10 05:0x）— 第 8 批：可训练掩码 + 有限监督/部分观测解空间收缩

- **14 张 I-R 卡**：`auto-paper/20261110-050300/ConnectomeTrainableSpikingPredictiveVision/ccfa-startup-packet/idea-cards-R87.md`（样本效率 AUC、部分观测 M 扫描、teacher-student 简并、位置×强度、梯度归因、预算×horizon、TTFS、SynOps、LIF×rate、sensory 打乱、DEG/ER、漂移、闭环、参与比）。
- **12 张 I-S 卡（第 6 步换道）**：同目录 `idea-cards-R87-wave2.md`（Θ 参数容量阶梯 C0–C4、钳制 M、冻结 Θ teacher-student、延迟匹配 2×5、序列回放、容量×动态、h=1..5、符号打乱、sensory 打乱 × M、DEG/ER × 容量、SynOps × 容量、TTFS × 容量）。
- 依据：R87 本机 8 链真实负结果（8/8 学会外推但 8/8 结构效应不可区分）+ Beiran 2025 理论 + An 2026 稀疏化 + Dhiman 2026 零分布。
- **下批备选**：I-S4/I-S8/I-S10/I-S11/I-S12、闭环 I-S13（数据门：真实事件/光流 `DATA_UNAVAILABLE` 保持生效），以及下一批全新 I-T 卡。
- 结果：0/8 达标；validator NOT_QUALIFIED / 6.3、guard INCOMPLETE；0 篇达标，ACTIVE。
| 2026-11-10 12:12 | Effective In-Degree Is the Single Control Variable: Unifying Structural Pruning and Recurrent Gain in Connectome-Constrained Spiking Vision | gain-normalised temporal wiring; effective in-degree mu | MaleCNS v1.0 optic-lobe two-hop vision plus CIFAR-10 transfer | G0-G8 PASS (proceed) | auto-paper/20261110-121224/Effective-In-Degree-Unification-for-Connectome-Constrained-Spiking-Vision/guidance.md | New stand-alone idea inspired by the 7.5 null-ladder manuscript; T1-T3 proved and numerically verified before guidance; collapse is a falsifiable prediction, no result asserted |
| 2026-11-10 12:50 | Degree-Aware ANN-to-SNN Conversion for Connectome-Masked Visual Networks | degree-aware per-node threshold calibration; ANN-to-SNN conversion | CIFAR-10/100 vision with a fixed MaleCNS structural mask | G0-G8 PASS (proceed) | auto-paper/20261110-125000/Degree-Aware-ANN-to-SNN-Conversion-for-Connectome-Masked-Visual-Networks/guidance.md | Visual-dataset main task per user 12:40; One-Spike SNN already converts Text GCN so generic GNN conversion is NOT claimed; degree heterogeneity is the new axis |
| 2026-11-10 14:52 | Deterministic Two-Phase Conversion: Exact Spike-Count ANN-to-SNN Transfer across Vision and Graph Domains | deterministic temporal error diffusion replacing TPP Bernoulli firing | CIFAR-10/100 vision primary, Planetoid graphs secondary, MaleCNS optional | G0-G8 PASS (proceed) | /Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision/auto-paper/20261110-145235/Deterministic-Two-Phase-ANN-to-SNN-Conversion/guidance.md | R91-v3 versioned contract; theory verified before guidance (exact-count bound theta/2, zero variance); direct predecessor TPP ICML 2025 with official code; user prior unpublished 1.5pp graph result used as internal context only |

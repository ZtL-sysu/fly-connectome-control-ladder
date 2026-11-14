# CCFA idea review — Effective In-Degree Unification（2026-11-10）

> 模式：`ccf-idea-reviewer` **standard**（`ccf-common/references/task-modes.md` §standard）
> 协议：`SKILL.md`、`references/rubric.md`、`calibration.md`、`strict-idea-review.md`、`expert-panel.md`；`ccf-common/references/review-output-standards.md`
> 被评对象：`auto-paper/20261110-121224/Effective-In-Degree-Unification-for-Connectome-Constrained-Spiking-Vision/guidance.md` + `theory-verification.json/.md`
> **性质：idea 阶段诊断，不是论文 P9 full 评审；分数不计入 `qualified_papers.json`、不计入 Overall>8.0 达标计数、不触发 guidance、不授权跑实验。**

## 0 Verdict first

**Weighted final score: 3.48 / 5｜Overall: 6.96 / 10｜Confidence: Medium｜Recommendation: `pivot-with-rescue-route`。**
无 fatal gate 触发；`Current conference readiness: low-medium`，`Development potential: High`。
分数不是接收概率，须与 fatal risks、检索状态、发展潜力一起读。

## 1 Target venue / assumptions

目标 CCF-A 会议档（CVPR 2027 式 8 页 + 强制 LLM Statement，双盲）。假设：主指标为两跳可辨识性与跨族坍缩，不承诺视觉 acc 提升；真实 MaleCNS 二值子图可用；突触计数/递质符号/细胞类型层次 `DATA_UNAVAILABLE`；`planned_claim` 与 `observed_finding` 分离。

## 2 Search basis

`searched, partial coverage`。本会话累计 5 轮 public-safe 检索（4 轮 guidance 前撞车 + 1 轮本评审补充），命中 8 条以上，但多数停留在检索结果摘要/全文片段层，**未达 standard 要求的 3–8 条逐条一手核验**。按 `strict-idea-review.md` §Score Guardrails，**novelty 封顶 3**，并把 confidence 单独降为 Medium。未把未检索的新颖性当正分。

## 3 Stage and development potential

早期 seed（无正式实验、主 claim 为预注册预测）。`Current conference readiness: low-medium`——理论已验证但中心坍缩零实证。`Development potential: High`——T1–T3 三条已证引理可独立成文，且修补路径明确。`Main reason it is not ready`: 跨族坍缩是假设且前身机制实测阴性。`Best rescue route`: 先跑归一化 GN-TW 的正面 pilot + 逐条核验最近前作。`Evidence needed to decide`: 三族 matched-μ 的 collapse CI 与 α 边界消融。

## 4 Normalized idea

| 字段 | 内容 |
|---|---|
| Problem | dense 真实连接组上 2 跳 GNN 全 chance，现有补救是 ad hoc 不可逆 top-k 剪枝；文献对"连线是否带来增益"结论冲突 |
| Gap | 7.5 稿 §4.9 测到 density boundary（≈0.505 → k=4/2 ≈0.986/0.999）却主动放弃机制解释；无人把空间剪枝与时间增益放到同一自变量上，也无人给 dense 连接组 LIF 稳定条件 |
| Root challenge | 二值拓扑与其零分布共享粗粒度统计量 → 项目 40+ 链"比结构"一致阴性 |
| Insight | `W=AᵀD_in⁻¹` 行随机 → `ρ(W)=1` → `ρ(λI+αW)=λ+α`，稳定 iff `α<1−λ`；`μ=α·ρ_ext·k_eff` 统一两种降自由度方式 |
| Method | GN-TW：硬掩码不删边、入度归一化突触输入、有界增益；三族 matched-μ 坍缩检验 |
| Expected evidence | 3 族 × 7 匹配 μ × 5 seeds × ≥2 独立子图 + 度保持/等量随机/rate/时序打乱对照 + CIFAR-10 转移 |
| Limitation | T4 是假设非定理；合成 coincidence 刺激；230 节点单子图；真实视觉预期为负边界 |

## 5 Closest prior art table

| Closest work | Venue/year | Source | 已做的事 | 与本 idea 重叠 | 剩余 novelty delta | 风险 |
|---|---|---|---|---|---|---|
| **The Role of Degree Distribution in Shaping the Dynamics in Networks of Sparsely Connected Spiking Neurons** | Front. Comput. Neurosci. 2011 | https://www.frontiersin.org/Journal/10.3389/fncom.2011.00008/abstract | **"changes in the in-degree can significantly affect the global dynamical state by altering the effective steady state input–output gain"**，并用考虑 in-degree 的 rate equation 解释增益效应 | **直接占据"入度→有效增益"理论内核** | 连接组语境、跨空间/时间统一、闭式稳定界、视觉可辨识性 | **high** |
| **Metabolic Cost Asymmetry as a Structural Regulariser for Recurrent SNNs** (Sotero & Sánchez-Bornot) | bioRxiv 2026, 10.64898/2026.10.09.758141 | https://www.biorxiv.org/content/10.64898/2026.10.09.758141v1.full-text | 15 档 structural densities × 5 cost ratios（75 条件），定位 Pareto frontier 的 **collapse threshold**，涌现式剪枝层级 | "密度扫描 + 找临界阈值 + recurrent SNN"方法形态 | 自变量是代谢代价而非 μ；非连接组、非坍缩统一 | high |
| Lappalainen et al., connectome-constrained DMN | Nature 2024, s41586-024-07939-3 | https://www.nature.com/articles/s41586-024-07939-3 | 稀疏度提升神经活动预测（0.85 vs 0.38）；**有连接强度估计后稀疏不再必要** | 结构侧"稀疏 vs 强度"观察 | 跨空间/时间坍缩、稳定界 | high |
| An, function-preserving sparsification | bioRxiv 2026, 10.64898/2026.09.19.752860v2 | https://www.biorxiv.org/content/10.64898/2026.09.19.752860v2.full.pdf | 6 算子等边预算、cliff k*≈9、度保持/随机/权重打乱决定性对照 | 静态剪枝 + 决定性对照 | 视觉任务、时间体制 | medium |
| Clark et al., low-rank collective geometry | PRX 2025, 15(4):041019 | https://doi.org/10.1103/2jt7-c8cq | 维度只由耦合方差 + 有效秩决定 | 粗粒度集体统计量 | 任务条件化有效自由度 | medium |
| Beiran & Litwin-Kumar | Nat Neurosci 2025, PMID 41145885 | https://pubmed.ncbi.nlm.nih.gov/41145885/ | 自由权重补偿结构删除；"effective strength 不是统计连接度的函数" | 支持"别比结构"的诊断，同时**挑战单一 μ 可预测性** | 需证明训练后读出仍服从 μ | medium |
| Spectral Flow Certificates | arXiv:2607.21607, 2026 | https://arxiv.org/abs/2607.21607 | 训练前闭式标量预测 GNN 长程 acc，25 合成族 + 150 分子图 | **贡献类型**（training-free scalar） | 任务条件化 + 时间维度 + 连接组坍缩 | high |
| Over-squashing Jacobian (Alon & Yahav 2021; Topping et al. 2022) | ICLR 2021/2022 | https://arxiv.org/abs/2006.05205 | `‖∂h_v^K/∂x_u‖ ≤ (cw)^K (Â^K)_{vu}` | 路径衰减理论本身已被建立 | 连接组语境的可控自由度 | medium |
| 内部 7.5 null-ladder 稿 | 项目 2026 | 内部 | 嵌套零模型阶梯、对照协议一等变量、§4.9 密度隔离 | 动机与密度锚点 | 主张/贡献轴/证据独立 | low |

## 6 Novelty delta

减去最近前作后真正剩下的：`MaleCNS dense 全图 + 不删边的时间增益控制 + μ 作为唯一连续自变量 + 跨空间/时间三族坍缩 + 预注册决定性对照 + 视觉两跳可辨识性`。
**但这个 delta 的两侧都被挤压**：Frontiers 2011 已把"入度→有效增益"变成教科书式 rate equation，SFC 2026 已把"训练前标量预测可解性"卖过一次，Lappalainen 2024 已把"强度替代稀疏"报过一次。因此本 idea 的新意必须落在**统一与坍缩的实证**，而这一条恰好是零证据的。

## 7 Serious blockers

1. **中心主张零正面证据**：三族坍缩是 T4 假设；前身 I-V0（未归一化 temporal wiring）的概念验证 ρ 扫描 7 点全 chance（0.4891–0.5098，P3/P4 FAIL）。归一化版本未跑。严格审稿人会说"统一曲线是从两个已知现象拼出来的猜想"。
2. **理论内核撞车**：Frontiers 2011 的 in-degree→effective gain rate equation 使 T2 的"新意"降级为"在连接组语境的闭式应用"。
3. **贡献类型撞车**：SFC 2026 使"一个标量解释可解性"易被读成又一个 proxy。
4. **视觉价值弱 / venue 风险**：主指标是 XOR 可辨识性 + 坍缩，真实视觉预期为负边界（7.5 稿 §4.10 非图 MLP 0.9722 主导），CVPR 主轨 fit 存疑。
5. **定义滑移**：T1 的 `k_eff`（两跳核 IPR）与 T3 的 `μ`（阈值体制泊松强度）是两个不同可观测量，guidance 把两者并到一条 μ 轴时未给出等价性证明。
6. **构造平凡风险**：diamond 由 REAL 图绑定，度保持 null 的分离可能只是"保护了人工选的边"——R49 对 7.5 稿提过同一批评。
7. **数据受限**：230 节点单子图、无突触计数权重（top-k 只能用标签无关代理，与 7.5 权重 top-k 不等价）、无递质/细胞类型、合成刺激。

## 8 Per-expert reviewer notes

| Role | Score tendency | 最强可辩护论点 | 拒稿级关切 | Anchor | 最小修复 | Conf |
|---|---|---|---|---|---|---|
| Field Expert | 4 | 40+ 链一致阴性被归因为"自变量选错"，诊断有实测支撑，问题具体 | CVPR 视觉社区是否认为"两跳 XOR 可辨识性"重要；7.5 稿已证视觉负边界 | 7.5 §4.10、项目 R84–R88 账本 | 明确 D&B/理论 track 定位，或换 NeurIPS/ICLR | 4 |
| Method Expert | 4 | `ρ(A)=119.1006` → `ρ(W)=1.0000` → `α<0.5` 是**推导而非调参**，且解释了实测雪崩 | T1 的 IPR 与 T3 的 Poisson μ 未证明等价；线性化假设在饱和区失效 | `theory-verification.json` T1/T3 | 补一条两可观测量单调映射的证明或实证 | 5 |
| Experiment Expert | 3 | 三族 matched-μ + 5 个决定性对照 + 独立子图设计完整，负结果仍有信息量 | 全部是计划；前身机制实测为阴性；缺至少一个正面 pilot | `R90-local-independent-audit.json`（P3/P4 FAIL） | 先跑归一化 GN-TW 的最小三族 pilot | 4 |
| AC / Venue Expert | 3 | 可复现 artifacts 与预注册纪律完整 | "又一个 training-free scalar" 是 desk 级措辞风险；分析型贡献在 CVPR 主轨易被判 workshop | SFC 2026、CVPR 主轨口味 | 明确贡献类型为主张检验而非架构，或换 venue | 4 |
| Skeptical Prior-Art Expert | 3 | 未占据的四元组确实存在 | 最强反对："in-degree 控制有效增益 2011 年就写成了 rate equation；把稀疏和增益画在一条轴上是重新命名" | Frontiers 2011、Lappalainen 2024 | 逐条核验 3–8 条一手来源并写出精确 delta | 3 |

**Panel synthesis**：一致认为 T1–T3 的方法严谨性与可行性是本 idea 最硬的资产；分歧在"统一坍缩是否构成 CCF-A 主轨贡献"。最强接受轴 = 归一化稳定界可推导且解释了实测失败；最强拒稿轴 = 中心坍缩无实证 + 内核已被 2011/2024/2026 三条线挤压。synthesis 不被平均掉，最终立场跟随最强未解决关切。

## 9 Rubric scores（逐维分值，权重合计 100）

| Dimension | Weight | Score (1-5) | Confidence (1-5) | Deduction / evidence basis | Repair condition |
|---|---:|---:|---:|---|---|
| Problem importance | 12 | **4** | 4 | 瓶颈具体（dense 0.5008 / ad hoc 剪枝 / 文献冲突），有实测锚点；但对视觉社区的重要性依赖方法论而非视觉性能 | 用 CIFAR-10 转移给出"剪枝阈值可比性"的社区级收益证据 |
| Novelty against likely prior work | 14 | **3** | 3 | **封顶 3**：closest work 仅 partial coverage（多为摘要层、未逐条一手核验）；Frontiers 2011 占 in-degree→gain、Sotero 2026 占密度扫描找临界、SFC 2026 占训练前判据类型、Lappalainen 2024 占稀疏 vs 强度 | 逐条核验 3–8 条一手来源；证明"跨空间/时间坍缩 + 连接组稳定界"无近邻；若要 5 还需一条被审稿人认可的独占贡献 |
| Conceptual innovation | 12 | **3** | 4 | "归一化 → ρ(W)=1 → 稳定界"是标准线性代数；μ 统一是简洁洞察但 Frontiers 2011 的 rate equation 已给同类解释；非新框架 | 证明 T1 的 IPR 与 T3 的 μ 在统一轴上存在可证等价，否则拆成两个独立结果 |
| Method soundness | 14 | **4** | 5 | T1–T3 已证并在真实图数值验证（8 个 α 逐项、`ρ(A)=119.1006`、`ρ(W)=1.0000`）；扣分：T4 未证、线性化在饱和区失效、Poisson 背景假设未验证 | 补发放率曲线实证 + 饱和检测断言；把 T4 明确保持为假设 |
| Elegance and simplicity | 8 | **4** | 4 | 单一标量 μ + 一条不等式 α<1−λ，组件少、可解释；扣分：两个可观测量并轴存在定义滑移 | 给出两量的映射或改称"两个互补观测量" |
| Feasibility under resources | 8 | **4** | 5 | 本机实测 40.8 s / 195 行、真实图 SHA 硬校验、代码路径已有、8 远程任务为既有授权；扣分：官方 flyvis 可能装不上、真实突触权重不可得 | 先做 flyvis 安装 smoke 并写明降级路径；权重项保持 DATA_UNAVAILABLE |
| Experimental convincibility | 10 | **3** | 4 | 三族 + 决定性对照 + 独立子图 + α 边界消融设计完整，但**零正面证据**，且前身机制实测阴性（ρ 扫描全 chance、P3/P4 FAIL） | 先出归一化 GN-TW 的最小三族正面 pilot，再谈完整证据包 |
| Venue and audience fit | 8 | **3** | 4 | CVPR 主轨偏视觉性能；本稿主指标是 XOR 可辨识性 + 坍缩，真实视觉预期为负边界（7.5 §4.10 MLP 0.9722 主导） | 定位 D&B / 理论 track，或转 NeurIPS/ICLR 方法轨 |
| Timeliness and topic heat | 6 | **4** | 4 | 2024–2026 连接组/稀疏化/循环 SNN 密集（Lappalainen 2024、Clark 2025、An 2026、Sotero 2026）；扣分：热即拥挤 | 用近 12 个月新增前作做一次更新检索 |
| Risk-adjusted acceptance potential | 8 | **3** | 4 | 三条挤压线 + 中心坍缩零实证 + 前身阴性；可能被归为"更严格的消融/又一个 proxy" | 同时解决 novelty grounding 与正面 pilot，且明确 venue |

## 10 Weighted final score（本机 conda 实算复核）

```
weighted = Σ(维度分 × 权重)/100 = 348/100 = 3.48
Overall  = weighted × 2 = 6.96 / 10
Band     = 3.0–3.6 → pivot-with-rescue-route
到 8.0 所需加权点 = 400 − 348 = +52
```

逐维点数：48 / 42 / 36 / 56 / 32 / 32 / 30 / 24 / 24 / 24 = **348**。实算脚本输出已复核，不是估分。

**Fatal gates**：novelty 3（>2，未触发封顶）、method 4、experimental 3（>2）、venue 3（>2）、feasibility 4 → **none 触发**。检索已执行（partial coverage），故不触发 `needs-literature-search` 强制封顶，但 novelty 已按 guardrail 封顶 3。

## 11 Score-change conditions（是条件，不是预测分数，更不是达标承诺）

| 路径 | 维度变动 | 加权增量 | 结果 |
|---|---|---:|---|
| A：novelty 3→5、experimental 3→5、venue 3→4 | 逐条核验一手前作 + 正面三族 pilot + venue 明确定位 | **+56** | 404/100 → Overall **8.08** |
| B：五个维度各 +1（novelty/evidence/venue/elegance/acceptance） | 温和全面改进 | +48 | 396/100 → Overall 7.92，**仍不够** |

结论：必须至少让 novelty 或 experimental convincibility 之一升到 5；温和全面改进到不了 8.0。

## 12 Confidence

**Medium (3/5)**。依据：理论验证、真实图数值、本机实测 runtime、5 轮 public-safe 检索、保留的概念验证与审计均可得；扣分：closest work 多停留在摘要/片段层未逐条一手核验，中心坍缩主张无任何实证，venue 口味判断无官方 2027 CFP 逐条核对。低置信不自动降分，只降确定性。

## 13 Strict reviewer comments

1. 「把一个已知 2011 年的 in-degree–gain rate equation 换成连接组语境的谱半径，再取个名字叫 μ，不构成新机制。」——**Exact claim**：T2 为新稳定条件。**Anchor**：Frontiers 2011。**Why deduct**：conceptual innovation 3。**Repair**：证明跨空间/时间坍缩是 2011 理论无法推出的新预测，并实测它。**Score move**：novelty 3→4。
2. 「你连一个正面 pilot 都没有，前身版本还全 chance。」——**Exact claim**：三族坍缩。**Anchor**：`R90-local-independent-audit.json` P3/P4 FAIL。**Why deduct**：experimental convincibility 3。**Repair**：归一化 GN-TW 最小三族 pilot。**Score move**：evidence 3→4/5。
3. 「又一个训练前标量预测可解性。」——**Exact claim**：μ 是共享控制变量。**Anchor**：arXiv:2607.21607。**Why deduct**：acceptance potential 3。**Repair**：把交付物定位为"可证伪的统一主张 + 决定性消融"，不是 proxy 排行榜。**Score move**：acceptance 3→4。
4. 「CVPR 主轨为什么要一篇主指标是 XOR 的文章？」——**Exact claim**：视觉贡献。**Anchor**：7.5 §4.10 负边界。**Why deduct**：venue fit 3。**Repair**：D&B track 或换 venue；或给出真实视觉任务上剪枝阈值可比性的正面收益。**Score move**：venue 3→4。

## 14 Fixability table

| Issue | Affected dimension | Severity | Fix class | 写稿前可修? | 所需证据/设计改动 | 风险降低条件 | 发展潜力影响 | Owner skill |
|---|---|---|---|---|---|---|---|---|
| 中心坍缩零实证、前身阴性 | Experimental convincibility | high | evidence-design | partly | 归一化 GN-TW 最小三族 matched-μ pilot | 至少一个 collapse CI 含 0 且 α 边界如预测 | High → 维持 | `ccf-experiment-designer` |
| 前作仅 partial coverage | Novelty | high | novelty-grounding | yes | 逐条核验 3–8 条一手来源（尤其 Frontiers 2011、Sotero 2026、SFC 2026） | 写出可辩护的独占 delta | High → 维持 | `ccf-literature-searcher` |
| IPR 与 μ 并轴无等价证明 | Conceptual innovation / Elegance | medium | method-redesign | yes | 证明两量单调映射，或拆成两个独立结果 | 定义不再滑移 | Medium | `ccf-idea-optimizer` |
| CVPR 主轨 fit | Venue fit | medium | venue-switch | yes | 明确定位 D&B / 理论轨，或改投方法类会议 | 有官方 CFP 逐条核对 | Medium | `ccf-pipeline-orchestrator` |
| 真实突触权重/细胞类型不可得 | Feasibility / Method soundness | low | feasibility-check | no | 保持 DATA_UNAVAILABLE，不编造；top-k 代理标注不等价 | 明确 scope 即可 | Low | `ccf-experiment-designer` |

## 15 Upgrade / pivot actions

- **最小可救改动**：先跑归一化 GN-TW 的三族 matched-μ pilot（本机 conda，复用已冻结图族与 raw 纪律），把 experimental convincibility 从计划变成证据。
- **novelty-grounding**：逐条核验 Frontiers 2011 与 Sotero 2026 全文，写出"它们无法推出跨空间/时间坍缩"的精确论证。
- **venue-switch**：若 CVPR 主轨 fit 无法修复，转 NeurIPS/ICLR 方法轨或 CVPR D&B。
- **pivot 保留项**：即使坍缩失败，T1–T3 三条已证引理（稀释引理、稳定定理、重合信息单调性）可独立成一篇短方法/理论结果，不降低目标而是换主张。
- **不做的动作**：不降 `expected_strong`、不调参到显著、不挑 seed、不删负结果、不把阴性包装成正面。

## 16 Evidence that would change my score

- 上调：归一化 GN-TW 在两个独立子图上出现 collapse CI 含 0 且共同 μ* 重叠；α 边界消融如 T2 预测；flyvis 适配成功；逐条一手核验后仍无近邻。
- 下调：三族在 μ 上系统性分离；μ* 跨子图漂移 >2×；α≥0.5 仍可辨识（推翻 T2 相关性）；发现一篇已实现"稀疏度与循环增益统一标量 + 视觉坍缩"的 A 级前作。

## 17 Recommendation

**`pivot-with-rescue-route`**（3.48 / 6.96，Medium）。保留 T1–T3 与 μ 的形式化作为最佳成分，把"先出正面 pilot + 逐条核验前作 + 明确 venue"作为唯一救援路线。不标记 `abandon`：中心 claim 可检验、修补路径具体、且已有三条可独立发表的引理。

## 18 Optional next-module decision

按 CCFA handoff `PARTIAL`：本次仅输出评分与动作队列，**不自动调用** `ccf-idea-optimizer` / `ccf-experiment-designer` / `ccf-literature-searcher`。用户若要推进，需单独指明。

## 19 Checklist status

1 目标 venue/假设 ✔｜2 problem-method card 归一化 ✔｜3 检索状态标注 `searched, partial coverage` ✔｜4 closest-work 表（9 条，含 2 条新增）✔｜5 五角色独立 panel ✔｜6 十维全打分、每个 ≤3 分含扣分/证据/修复 ✔｜7 fatal 与可修弱点分离 ✔｜8 confidence 独立报告 ✔｜9 recommendation 五选一 ✔｜10 未跨模块执行 ✔

## 20 Output self-check

节序符合 single-idea standard 契约 ✔｜表格列数一致 ✔｜分数/置信/推荐内部一致（3.48→3.0–3.6 带→pivot）✔｜每条批评均有具体 anchor 与修复条件、无通用套话 ✔｜三值分离（criterion / Overall / Confidence）✔｜未编造文献/结果/接收概率 ✔｜未把 idea 分误作论文 Overall ✔｜中文标点一致 ✔

---

**与项目历史对照**：既有十余个已评 idea 最高 7.08（`null_ladder`，2026-11-06），本轮 6.96 略低，主要扣在"中心主张零实证 + 新增 2011/2026 两条理论内核撞车"，但 method soundness 4 与 feasibility 4 高于历史平均（因 T1–T3 已证并数值验证）。项目 **0 篇达标状态不变**；本分数**不参与 governing**（governing 仍 r60 独立 6.3）。

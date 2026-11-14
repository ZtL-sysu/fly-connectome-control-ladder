# Candidate D 独立 idea red-team：CVPR 主会

review_execution: independent-agent
review_mode: standard
review_scope: idea review only; no manuscript score or historical scoring targets inspected
inputs: 用户限定的 idea cards、prior-art map、competence-visibility-supplement-v1.md、code audits、sources/toposens、toposens2026.txt、boundary2026.txt、flyhack2026.txt
literature_status: partially searched (提供的公开来源及其机会图；本轮未外部补搜)

## Verdict first

**有条件支持有限成本 baseline-first pilot；目前不支持承诺整篇 CVPR 主会论文。** 补充设计增强了可判定性：同一网络/任务内加入输入身份置乱正对照（已知破坏输入-目标对应）与计算图同构负对照（应保持函数），再测实际 degree-null。但两类控制不能单独证明对细微 topology effect 有足够灵敏度：input scrambling 可能远强于真实 null，isomorphism 主要是实现 sanity check。合理核心不是“多训练几步”，而是检验**早期比较能否检出已知功能干预、能力达标后这种检测能力是否改变，以及实际拓扑 null 在独立视觉条件下如何表现**。这是可证伪假设，不是结果。校准范式本身是标准实验设计；仍未见足以证明 CVPR 主会价值的机制证据。

- 当前 CVPR readiness：低。
- Development potential：中。若验证 competence-by-intervention 交互，并连接到有意义的视觉泛化结论，可能形成论文；若只发现长训练后的 loss gap，应停止该 framing。
- Pilot 判定：可做，限于精确复现、能力校准和一个预注册的交互对比；先做小预算可行性检查，不预设延长训练后会出现 connectome 优势。
- 推荐：**pivot-with-rescue-route**。救援路线是把贡献从一般“undertraining 使 null 比较失效”收窄为任务 competence × intervention visibility 的视觉比较有效性条件，并提供独立泛化证据。文献新颖性仍需补查，不能据此宣称高新颖度。

## Target venue and assumptions

目标为 CVPR 主会，按视觉方法/机制评估论文而非生物学发现评价。假设可复现 TopoSens 官方任务、获得可用 CUDA 资源，且能完成更长训练和重复 null / seed。当前提供的材料没有证明本地 MPS 或远端资源已完成任务级性能验证，也没有报告新实验。Topological Sensitivity、Boundary nulls、FlyHack 均是 2026 arXiv v1（截至给定材料中的状态），不将其写作已正式发表结论。

## Normalized idea

| 项 | 评审重述 |
|---|---|
| 问题 | 视觉 connectome 与 rewired null 的近零差异，可能只是在某个低能力学习阶段、某种干预可见性下成立。 |
| Gap | 现有严格对照研究了短时匹配优化与 degree-preserving null；待验证的是能力受限时的行为指标能否掩盖拓扑干预在合格视觉行为/泛化任务上的效应。 |
| Root challenge | 训练水平本身改变表示、输出和动力学；单用 MSE 或训练步数不能区分“模型没学会”与“拓扑对该行为没有可测效应”。 |
| Insight（待证） | topology comparison 的结论应同时报告任务 competence 和 intervention visibility；只有在所需行为可解且干预对行为指标有足够灵敏度时，近零效应才支持该任务/尺度下的等效解释。 |
| Method（当前尚非完整方法） | 共享初始化、connectome 对 degree-preserving null 的成对训练；比较官方 5/10-step 与预设更长上限，validation-only 选 horizon；同一 regime 内做打乱 stimulus-target identity 的输入正对照、完整计算同构的函数保持负对照，再测实际 degree-null；冻结在 held-out motion 条件评估，检验 horizon/competence × intervention。分解 MSE、预测均值/方差、方向敏感性与输入依赖。 |
| 预期证据 | 能力直接达标；干预确有足够可见性；配对且按独立训练 seed/rewire mask 推断的交互；在独立速度/偏移/对比条件上重现，且超越 constant/input-linear、degree/geometry 等基线。 |
| 限制 | 若 competency 改变只反映优化器、参数尺度或控制模型不充分，无法归因为拓扑；有限刺激和单一 averaged flyvis 模型不能支持广义生物视觉结论。 |

## Closest-work table

| Work | 已做什么 | 与 D 重叠/风险 | 留下的差异（待实验证实） |
|---|---|---|---|
| Dhiman, *Topological Sensitivity in Connectome-Constrained Neural Networks*, arXiv:2604.04033v1 (2026)，给定 `literature-search/toposens2026.txt`，§4.2、§5.1–5.3、§7、§10 | flyvis 上比较 checkpoint 与 from-scratch、naive 与 degree-preserving null，固定 5/10 Adam steps；明确报告重连只改 incidence、沿用 metadata/parameter assignment；将结论限定在早期优化。 | D 不能把“纠正 checkpoint/空模型”“边属性沿用”或“早期 horizon 不代表所有学习阶段”本身说成新贡献。该文明确说固定 5/10 steps 与 parameterization/rewiring semantics。 | 若 D 证明“按 validation 定义的 competent horizon 下，某拓扑干预的独立泛化结论与早期窗口显著不同”，且非仅训练更久，则是在其限定边界上做有证据的扩展；目前没有这条结果。 |
| Park, *Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison*, arXiv:2609.39248v1 (2026)，`boundary2026.txt` | 讨论 null 保留哪些结构会改变比较，做 boundary-preserving、shortcut、sham/dose 与 equivalence 分析。 | “空模型约束要匹配科学问题”“无显著差异等于等效”均已有强先例。 | D 必须给视觉学习 regime / competence 的特异可测机制，而非复用一般 null-validity 口号；其非视觉进化设置不能直接回答视觉学习问题。 |
| Dhawan, *FlyHack: Stress-Testing Mechanistic Claims in a Connectome-Constrained Visual Model*, arXiv:2610.13018v1 (2026)，`flyhack2026.txt` | 50-model flyvis ensemble、任务匹配 CNN、干预匹配 attribution 与多种行为/机制 stress test；强调结论依赖比较模型、干预、表征和训练解。 | “模型相对、干预依赖、需任务匹配评估”已明确提出；D 的评估协议若只换标签会显得重包装。 | D 聚焦 connectome-vs-topology null 的学习阶段/能力条件，且需要显示其对视觉结论的增量；目前未和 FlyHack 的机制变量或模型族做有力区分。 |
| Correig-Fraga et al., *Structure alone*（来自给定 prior-art map） | 视觉相关任务和结构/接线成本分析。 | 仅加空间/retinotopic 匹配 control（Candidate A）不足以形成 novelty。 | A 只能用作 D 的控制轴，须显示它能解开特定交互，而不是再造一个 null。 |

**Novelty delta：** 补充提出“用已知功能破坏正对照和函数同构负对照，校准比较流程，再评估实际 null”，让实验问题更可判定；但 known positive controls、sanity checks 和 held-out validation 都是标准设计，不单独构成方法新颖性。可能的新差异仍是证明 early regime 未检出已知输入干预、competent regime 能检出，并由此改变对实际 topology null 的独立泛化解释。此预测尚无本项目证据；输入置乱与真实拓扑扰动效应大小不同，正控灵敏度不能直接外推成 topology-null 灵敏度。文献部分筛查，novelty confidence 低至中。

## 近 0.5 MSE 推断：严格边界

**材料事实：** 目标为平衡的二维单位方向向量；零向量预测的 MSE 解析值为 0.5。给定第三方报告的 degree-preserving 10-step MSE 是 connectome 0.504455、control 0.502693；两者都高于 0.5。报告值不是本项目重跑、不是统计检验，也不是“无信息”证据（`competence-source-observation.md`；`published-loss-calibration.json`）。

**可推断：** 该特定报告中，按均值看两者均未胜过零输出基线；二者 MSE 差约 0.001762，说明该点估计的相对差小，但没有联合配对误差、相应置信区间或预注册等效界值，不能判断差异精度或等效性。

**不可推断：** “近 .5”不证明表示没有方向信息、模型完全没学到、topology 无效，或 MSE 差异在所有 competent regime 仍为零。MSE = target second moment + prediction second moment − 2·prediction/target covariance；输出偏置、方差与 covariance 可能相互抵消。零预测校准只校准此处任务分布下的常量 baseline，不是通用 chance score，也不说明模型的潜在状态没有信息。

**测量漏洞与修复：** 同时报 held-out MSE 相对零/均值预测、预测均值与方差、方向 circular error/方向敏感性、线性 readout（训练刺激只用于训练 readout，validation 选 horizon）、input-only baseline、特征有效秩/反应对刺激的可重复性；所有 horizon 冻结后才看 held-out speed/offset/contrast。输入置乱须保持刺激边际、打破 stimulus-target 配对，并在 validation 固定策略；它只能证明 assay 对输入-目标信息丢失有反应，不能证明对弱拓扑效应有 power。函数同构须同步节点、参数/状态、输入输出索引，比较前向输出（必要时梯度/训练轨迹）到数值容差；它是实现检查，不是科学新发现。避免通过 decoder 重训、任意后处理或 test-set 选 checkpoint 把 competence 人为做高。定义 competence threshold、最小可检测效应和等效界，按重复 seed/mask pilot 变异预定，不可看完 test 再定。

## Fatal vs fixable

| 严重度 | 风险 | 为什么影响主会判断 | 修复/停止条件 |
|---|---|---|---|
| 当前 framing 的致命风险（可救） | 若中心结果只是“5/10 步时 MSE 近 .5，训练更久后变化”，这是对 TopoSens 已声明早期范围的直接延伸描述，缺少新方法或视觉洞见。 | 对 CVPR 主会，单纯更长训练的应用性结果不够支撑独立贡献。 | pilot 必须比较 competence regime 下的独立行为/泛化与控制交互；若交互没有超过重复/控制不确定性，停止 D 的强 claim。 |
| 高、可修复 | 输入身份置乱正对照可能远强于 degree-null；能检出它不等于能检出实际 topology effect。 | 不能从“失去视觉输入”的大效应推导 assay 对微弱拓扑效应具同等灵敏度。 | 报各对照效应量与不确定性；正对照只解释为最低限度的输入依赖验证。若声称 topology sensitivity，需预设可检测效应范围或 topology-dose/可校准干预，不要求 connectome 必须胜过 null。 |
| 中、可修复 | 同构负对照不是行为科学负结果，且错置参数、状态或刺激会制造假差异。 | 失败可能只是 permutation 实现错误；成功只证明重标记等价，不说明 null 比较有科学有效性。 | 单元级检查完整计算图共轭变换后的输出/梯度一致性；不计作 novelty 或 connectome 优势证据。 |
| 高、可修复 | Competence 是结果定义或训练选择代理；若按 test 优选 horizon/decoder，会循环论证。 | 不能解释 null 差异，更不能称 validity criterion。 | 预注册能力指标、validation-only horizon 和冻结 test；明确阈值来源、测试独立性、成对估计。 |
| 高、可修复 | 仅“未显著”或小 MSE 差被当成拓扑等效；null masks 和 seeds 的层级也可能混淆。 | 无等效界/层级设计时不能确认“结论不随能力改变”。 | 以训练 seed 为独立单元、rewire mask 嵌套/交叉建模；预设最小实质效应/等效区间，并报不确定性。 |
| 高、可修复 | 既有差异可能来自边元数据携带的 type/空间标签、权重分配，而非单一 adjacency。TopoSens §4.2 已披露该语义，不能当隐藏 bug。 | 机制因果归因需说清受干预的模型对象；沿用元数据是一种合法比较设定，但检验对象有限。 | 明确研究 estimand；比较既有 edge-carried 参数分配设定与同步端点属性的另一个匹配设定，或限定结论；不得混称为仅改 adjacency 的普遍结论。 |
| 高、可修复 | 小预算 baseline 未证实长训练可行、可达 competence 或 MPS/CUDA 实际吞吐。 | 失败可能是算力/训练稳定性而非理论假设。 | 首先运行短 smoke baseline 仅确认设备、显存、步时、loss/梯度有限性；完成上限内 pilot 后再决定投入。 |
| 中 | 单一 synthetic moving-edge split 只能说明窄任务；A 的 retinotopy null、B 的 transfer 指标容易成为已知控制的又一变量或 outcome leakage。 | 不能支撑“视觉拓扑”宽泛结论，transfer matching 可能把待检验结果直接匹配掉。 | 保留 A/B 作机制/负控制；至少用独立速度或空间偏移测试。B 若使用，只用不含 label 的训练刺激局部 transfer，并证明优于 degree/geometry 基线。 |
| 中 | prior-art 覆盖不全且核心工作皆 2026 preprint。 | novelty 与 venue taste 尚不稳。 | 进主实验前扩搜 competence/undertraining、null-model calibration、visual connectome training horizon、equivalence/representation sufficiency 相关工作并核对版本。 |

## 最小区分实验与有限成本 pilot

1. **极小控制校验，再复现基线：** 单一短 batch/seed 验证真实输入 vs stimulus-target identity permutation 能引起预期输入依赖变化；完整节点、参数/状态、输入输出映射的同构重标记在数值容差内保持输出。失败先修实现，不作科学解释。其后复核 TopoSens shared-from-scratch 5/10-step 结果；训练 seed 与 null mask 分开记录，不把第三方公开数当新结果。
2. **能力与正对照校准：** train/validation 上记录零/均值预测、input-only baseline、方向行为、输出方差、输入敏感性和 loss。固定保持刺激边际、打破 target 对应的 permutation 策略；validation-only 选择一个 competence horizon，预算内最大 horizon 预先固定。若早期也能稳定检出 input scrambling，则“早期 assay 对已知输入干预失明”的机制被否证；仍可单独检验实际 null 的 regime effect。
3. **实际 null 核心对比：** 冻结 horizon，在未见 speed 与 spatial offset 比较 connectome 和多个 degree-null；检验预注册 paired `competence/horizon × intervention` interaction，报告 seed 与 mask 两层不确定性。正控、同构负控和真实 null 分别报告，前两者不能代替真实 null 的效应精度。记录 activity/gradient 尺度；若 competence 改变伴随尺度大变，补匹配分析。
4. **有限 pilot 边界：** 一至数个 seed/mask 只回答 pipeline 正确性、设备/步时、控制方向和方差数量级；不声称检出率、等效或泛化结论。若同构误差、正控失败、validation competence 未达或预算不够，停止扩展或修复设计。
5. **全论文升级：** 用 pilot 方差和预设实质效应决定 seed×mask 重复数；预注册 competence/horizon、输入置乱、primary held-out 条件及等效边界。至少第二个独立视觉 setting 或标准 optic-flow benchmark，加入 task-matched strong nonbiological baseline；报告各干预效应尺度，确认不只是大正控可见而微弱 topology 变化不可分辨。若主张通用 assay，证明同一规则跨任务预测可识别性；单一窄任务的校准故事 CVPR fit 仍弱。
6. **解释纪律：** pilot 重复仅估工程成本/方差；non-significance 不等于等效，除非预设实质界且精度足够。

## Stopping conditions

- 预算上限内没有达到预设 validation competence，或只有输入泄漏/训练集读出达到：停止“competent视觉计算中的 topology inference”结论；只报告 pilot 不可识别，不能继续把更长训练当自动救援。
- 同构负对照输出不一致：先视为索引/参数/状态/随机性实现问题，不进入科学实验。若输入置乱在 task-matched competent baseline 中也无法产生可重复预期变化，重新定义正控；不可声称已校准输入可见性。
- 若早期和 competent regime 都能检出输入置乱，D 中“早期比较看不见已知功能干预”的机制被否证；只在实际 degree-null 的 competence interaction 独立复现时保留较窄问题。
- competence 达成，但在独立 motion 条件中没有可重复的拓扑相关行为变化；competence/horizon 交互落在预设最小效应/等效区间内：停止强 D 论文方向，转为有限的 null-validity 负结果或结束项目。
- 只有 MSE 相对 .5 的微小变化、只有训练指标变化、只在一个 seed/mask 或 test-selected horizon 出现：停止，不升级 claim。
- 若效应存在但匹配初始尺度/属性语义后消失，停止把它归因于 competence-conditioned topology；报告实际支持的参数化/尺度条件。
- 若验证出稳定、独立泛化的交互且多 mask/seed 同向，才进入扩展试验和全量 prior-art gate；此时仍需自然/标准 optic-flow 测试或明确收窄视觉任务范围，才判断 CVPR 主会可行。

## Independent expert panel

### Field expert
- Score tendency: 3/5；confidence: medium-low。
- Best argument: TopoSens 明确限定早期 5/10 步；从任务能力角度检验其结论边界有具体视觉任务基础。
- Strict concern: 只观察训练更久是其明确 limitation 的补充实验，尚未形成新的视觉科学发现。
- Anchor: `toposens2026.txt` §5.2、§7、§10；idea card D。
- Repair: 显示独立 motion generalization 上的预注册 competence × topology 交互，且排除 decoder/test 选择。
- Development-potential note: 有救援路径，但目前是问题假设，不是贡献。

### Method expert
- Score tendency: 3/5；confidence: medium。
- Best argument: 正/负对照加 paired factorial protocol 把“assay 是否能观察功能干预”转成可证伪小问题；MSE 分解提醒 .5 本身不诊断无信息。
- Strict concern: 输入置乱远强于可能微弱的 degree-null 效应，不能校准 topology sensitivity；同构测试只审计程序。若 competence 用 test 定义或 horizon 事后挑选，仍会有选择偏差；representation rank 不等于 task information。
- Anchor: `published-loss-calibration.json` caution；FlyHack 对模型、干预、表征依赖的结论。
- Repair: 预注册 validation 能力门槛与 horizon，独立 test 冻结；用不同指标验证能力、并对初始尺度与 edge-carried 语义作敏感性分析。
- Development-potential note: 方法能变严谨，但需要把“可见性”定义为测量量而非口号。

### Experiment expert
- Score tendency: 3/5；confidence: medium。
- Best argument: 官方代码、刺激和短 horizon 基线，加上已知输入正控/同构负控，支持低成本检查 pipeline 可判定性；近 .5 是校准动机但非无信息证据。
- Strict concern: 正控强度与真实 null 不同，负控本质是实现测试；缺 competence threshold、MDE/等效界、seed × mask 推断和足量独立泛化证据，目前不知长训练能否达标。
- Anchor: `prior-art-opportunity-map.md` 的 task/data/metric 与资源 caveats；third-party-only calibration JSON。
- Repair: 先基线复现和小样 smoke test，再以 validation 决定 horizon、test 固定、按层级报告重复；若未达能力按停机规则退出。
- Development-potential note: pilot 可行不代表全论文统计可行。

### AC / CVPR venue expert
- Score tendency: 2/5；confidence: medium-low。
- Best argument: 若形成可迁移的视觉对照有效性判据，并在外推条件下证明它改变 topology 解释，可能成为视觉评估/机制方法贡献。
- Strict concern: 当前材料是 connectome 领域一个模型/任务上的 early-vs-longer training 对比；单纯加训加测试容易被认为窄应用或对已声明 limitation 的补充，不足以构成 CVPR 主会方法贡献。
- Anchor: CVPR 主会定位；现有 idea card 尚未给出新算法/广泛验证；FlyHack 已有强机制评估包。
- Repair: 抽象出可预注册、可跨视觉任务复用的 inference-validity 方法，并做第二种视觉任务/模型或强标准 optic-flow evaluation；否则考虑更窄 venue。
- Development-potential note: venue fit 依赖结果形态，不可由正向 pilot 自动保证。

### Skeptical prior-art expert
- Score tendency: 2/5；confidence: low-medium（给定搜索覆盖不完整）。
- Best argument: 若把“能力与干预可见性”定为科学比较的必要条件，可能给 connectome topology study 一个可操作的 inference validity check。
- Strict concern: 主要元素分别已被 TopoSens（早期优化/参数化语义）、FlyHack（任务/干预/表示条件）、Boundary（null 条件及等效分析）覆盖；新术语可能只是组合已有提醒。
- Anchor: 三篇给定 2026 preprint 的摘要、方法与 discussion；prior-art opportunity map。
- Repair: 用差异化的预注册交互、held-out visual generalization 和 outcome-independent visibility measure 证明组合产生此前没有的预测能力；并完成更全近邻文献检索。
- Development-potential note: novelty 未知不能当低新颖的确定事实，但此风险已足以限制当前投入规模。

**Panel synthesis**
- Agreement: 5–10 step、MSE≈.5 和 degree-null 比较本身不能支撑能力不足/无信息结论；正/负控制提升可判定性但正控不代替 topology sensitivity 测量。D 的价值取决于能力、独立行为和实际 null 交互。
- Disagreement: Field/method 认为其作为 validity hypothesis 值得低成本检验；venue/prior-art 认为即使检验成立，主会贡献仍需广泛性或新方法证明。
- Strongest accept argument: 现有工作限定了 early dynamics，D 若在 competent held-out visual regime 下改变 topology inference，就填补有明确边界的空白。
- Strongest reject argument: 训练时长 sweep 是已声明边界的自然扩展；若无跨条件预测/新有效性方法，将是窄增量。
- Decisive next evidence: 正控效应大小与 regime 依赖、通过同构输出等价检查、再加冻结 validation horizon 下 held-out motion 的真实 degree-null 交互及其不确定性。

## Complete rubric scorecard (idea score, not manuscript score)

置信度表示本次判断的证据把握，不是分数的修正项。Weighted score = Σ(score × weight)/100。

| Dimension | Weight | Score (1–5) | Confidence (1–5) | Deduction / evidence basis | Repair condition |
|---|---:|---:|---:|---|---|
| Problem importance | 12 | 4 | 3 | 视觉拓扑比较是否处于可解释行为区间是具体问题；但当前仅 flyvis moving-edge adaptation，未证明普遍影响。 | 在标准 optic-flow 或第二任务显示结论对视觉社区有实际后果。 |
| Novelty against likely prior work | 14 | 3 | 2 | TopoSens 早期范围、FlyHack 的 conditionality、Boundary null treatment 均邻近；差异仅是待测交互。 | 补全近邻检索并给出此前没有的交互预测/validity criterion。 |
| Conceptual innovation | 12 | 3 | 2 | positive/negative controls 改善可判定性，但属于标准方法；输入置乱不等于 topology 可见性。 | 证明 regime 校准能预测 held-out topology comparison 的可识别性并超越常规能力检查。 |
| Method soundness | 14 | 4 | 3 | input-scramble + isomorphism + degree-null 组成逻辑清楚的 assay 栈；对照效应尺度不同，能力/尺度混杂仍在。 | 将正控解释限制为 sensory dependence；validation 冻结选择，并直接估计实际 null 效应精度。 |
| Elegance and simplicity | 8 | 3 | 3 | 小型 factorial 可简洁；若加多 null、多个 decoder/指标/新任务，会变成控制包而非单一机制。 | 只保留一个 primary competence 指标、一个 primary topology contrast、一个 held-out endpoint。 |
| Feasibility under resources | 8 | 4 | 3 | 有官方代码、刺激和公开 10-step 运行记录，可先小测；完整长训 GPU 时间和显存尚未现场确认。 | 探针测实际步时/显存，设置上限；用结果决定是否扩规模。 |
| Experimental convincibility | 10 | 3 | 2 | 现有方案有解题路径但无结果、power/MDE/等效界、充分独立条件；5 masks × 3 seeds 仅是来源报告，不保证适用 D。 | pilot 估层级方差；设效应界和足量独立 seed/mask，独立 stimuli 冻结评估。 |
| Venue and audience fit | 8 | 3 | 2 | 视觉机制与泛化可对 CVPR；当前单模型窄任务且缺方法通用性，易被认为应用性增量。 | 第二任务/模型或可复用方法价值；否则换窄 venue。 |
| Timeliness and topic heat | 6 | 3 | 3 | connectome visual models 与机制 stress test 当前活跃；同时 2026 相关工作密集，话题热不等于空白。 | 用近期正式/预印本近邻完整确定剩余差异。 |
| Risk-adjusted acceptance potential | 8 | 2 | 2 | 没有新证据前，novelty、归因、主会范围三项均高风险；不能从 pilot 可跑推断主会竞争力。 | 仅当交互可重复、独立泛化显著且机制区分有效，才把该维上调至 3。 |

**Weighted final score: 3.26 / 5**（加权 idea triage 分；不是接受概率、不是论文稿评分；补充设计令 method soundness 上调一分）。

- Current conference readiness: low。
- Development potential: medium。
- Overall confidence: 3/5（方法/任务材料较充分，novelty coverage 与实验可行性仍有限）。
- novelty confidence: low-medium；当前只根据给定的部分 prior-art package。

## Fixability table and action queue

| Issue | 维度/严重度 | 类型；写作前可修？ | 必须完成的设计/证据 | 风险下降条件 | Owner skill |
|---|---|---|---|---|---|
| D 与 TopoSens/FlyHack/Boundary 的剩余 novelty 尚未隔离 | Novelty、venue / high | novelty-grounding；部分 | 搜索 competence-conditioned evaluation、training horizon、visual topology controls 与 equivalence/intervention validity；逐项比较预测和 estimand。 | 找到确切差异或确认无差异，避免旧结果重包装。 | ccf-literature-searcher |
| “competence”与“intervention visibility”未操作化 | Concept、soundness / high | method-redesign；是 | 预设 validation competence 标准、outcome-independent visibility 指标和主要交互。 | 同一规则在 held-out motion 条件预测可观测效应，而非按 test 选阈值。 | ccf-idea-optimizer |
| 正对照强度与真实 null 不匹配；负控只检查计算 | Method、evidence / high | method-redesign；是 | 分开估计 input scramble、isomorphism、degree-null 的配对效应和误差；不把前两项当 topology effect power。 | 在 competent regime 中，真实 null 的不确定性可被量化，并在独立条件复核。 | ccf-experiment-designer |
| 近零/等效结论可能无统计支撑 | Evidence / high | evidence-design；部分 | 用 pilot 估计 seed×mask 方差，定 MDE/等效边界，按层级扩大独立重复。 | 区间精度足以区分“无法识别”与“实质等效”。 | ccf-experiment-designer |
| 训练长度/硬件上限未知 | Feasibility / medium | feasibility-check；是 | 短 smoke test 量步时、显存、梯度/有限性；对预算内无法到 competence 设置停机。 | 预算内有稳定 validation competence，才考虑完整设计。 | ccf-experiment-designer |
| null 重连时沿用 edge-carried metadata 的 estimand 易被误述 | Soundness / medium | problem-refinement；是 | 明确固定元数据参数化比较测什么；必要时加端点属性同步的新控制作为不同 estimand。 | 结论不把一个合法模型定义混称为纯 adjacency 变化，也不靠“修 bug”造新颖性。 | ccf-idea-optimizer |
| A/B 辅助候选可能让方法膨胀或循环 | Elegance / medium | method-redesign；是 | A 仅作可选 spatial control；B 仅用无标签 train stimuli 定义，并对照 degree/geometry 基线。 | visibility 指标对独立测试效应有增量预测力。 | ccf-experiment-designer |

### Score-change conditions

- 若冻结 horizon 下，connectome/null 已同等 competent，且独立 held-out 条件交互位于预设实质等效界内：D 的强主张不成立，接受潜力维持 2 或更低；停止推进主会论文。
- 若 competence 在预算内无法达到：不降格声称拓扑相同；把发现限定为当前能力不足以识别，并停止昂贵扩展。
- 若正控在 competent regime 可检、早期也可检，则否证“早期比较对已知输入干预不可见”这条机制；若正控只在 competent regime 可检，也仅支持输入依赖可见性变化，仍需实际 degree-null 的独立 interaction 才支持拓扑推断贡献。
- 若达到能力后出现跨 seed/mask、held-out 条件复现的非小交互，并且尺度、端点元数据/参数共享及 decoder 解释不能替代它：方法 soundness / experimental convincibility / venue fit 可各上调约 1 分（依赖完整证据，不预支）。
- 若结果只是训练 loss 变好、只在挑出的 horizon/test 条件成立，或 visibility 由目标结果本身计算：method、experiment、acceptance 维各下调，停止强 claim。
- 若更全近邻检索显示已有工作已经做同一视觉任务、同一 competence 交互和独立泛化判据：novelty ≤2，按 calibration 改为 pivot/换问题，而非加更多 seeds。

## Strict reviewer comments

> The positive/negative-control supplement improves falsifiability, but does not yet calibrate sensitivity to the actual topology effect. Input identity scrambling may be much larger than degree-preserving rewiring; passing an isomorphism check is implementation validation. Show whether detectability of the positive control changes across regimes, then independently estimate actual-null effects on held-out motion without requiring the connectome to win. Even a robust regime interaction may be a narrow extension of a study explicitly limited to early dynamics. CVPR value requires evidence that the calibrated rule predicts consequential visual inference across settings or a reusable method beyond this connectome pipeline.

## Output self-check

- Numeric scores are idea scores, with criterion confidence separated; all dimensions complete.
- Every dimension ≤3 has an evidence-based deduction and repair condition.
- Fatal risks are separated from fixable risks; no current code-semantic choice is mislabeled as a bug.
- No new run, result, acceptance probability, or unsupported literature claim is asserted.
- Recommendation follows current 3.26 score and unresolved novelty/evidence gates; pilot permission is explicitly narrower than whole-paper endorsement.

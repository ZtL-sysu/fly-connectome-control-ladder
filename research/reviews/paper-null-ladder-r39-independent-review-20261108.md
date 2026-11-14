# CCF Paper Reviewer — Full Mode 独立评审报告（R39 定稿版）

**Paper:** *A Structure-Sensitive Null Ladder Exposes a Blind Spot in Connectome-Control Protocols*
**Target venue:** CVPR 2027（主会，double blind）
**Review date:** 2026-11-08
**Reviewer:** general-purpose-1（独立 CCF-A 审稿人 / AC，与作者无关）
**Mode:** `full` — scientific + writing + format + revision-action synthesis
**Input materials:** `paper/main.tex`、`paper/main.bib`、`paper/main.pdf`、`paper/tables.tex`、`paper/tables_taskaware.tex`、`paper/tables_r39.tex`、`paper/main.log`、`paper/main.bbl`、`paper/main.aux`；`scripts/make_r39_tables.py`；`results/p3_p4/{metrics.json,metrics_completed.json}`、`results/p3_p4_taskaware/metrics.json`、`results/r39_heldout/metrics.json`、`results/r39_real_connectome/{metrics.json,r39_real_connectome.py}`、`results/r39_real_connectome_v2/{metrics.json,metrics_from_trajectory.json,r39_real_connectome_v2.py,run.log,summary.txt,config.json,README.md}`；`audits/P3-P4-evidence-report.md`、`audits/P4-taskaware-evidence-report.md`、`audits/R39-reference-venue-and-integrity-audit.md`；`experiment-traceability.md`；上一版评审 `paper-null-ladder-full-review-20261108.md`（7.5，仅作历史扣分点参考，未照抄）。
**Search basis:** 联网核验 CVPR 2027 AuthorGuidelines / CallForPapers 官方页面；联网核验 arXiv:2610.10023、arXiv:2604.04033（支撑「文献冲突」前提的两条引用）。其余题录以 `audits/R39-reference-venue-and-integrity-audit.md` 与 `main.bib` 为准。

## ⚠ 版本锁定与漂移声明（必读）

**本报告评审的是磁盘上 2026-11-08 09:00:08 版的 `main.tex`**（736 行 / 42088 B / md5 `cd17e1e6f2766d2c2f11996715c2b5ef`），对应同日 09:00:10 重编译的 `main.pdf`（9 个物理页）。

评审期间稿件被**三次并发改写**：简报所述 08:24 版（696 行）→ 08:39 版（749 行，新增 sparse follow-up 与 §5 对标段）→ 08:54 版（719 行，v2 provenance 闭合、`tables_r39.tex` 自动生成、§5 Reproducibility 改写）→ **09:00 版（本报告的评审基准：新增 dense 稀释解释的「未证」声明、follow-up「三变量混淆不能隔离密度」声明、Conclusion 因果断言限定与「不主张泛化/未复现」声明）**。因此简报与本团队前两版提示中的若干描述（尤其「§4.8 只有五条件全 chance 的负结果」「v2 证据仍为轨迹抓取」）对最终版均已过时，本报告按 09:00 版重新逐条判定。若之后版本再变，请以本声明锁定的 md5 复核。

---

## Mode

`full`。按 `SKILL.md` 输出契约与 `fixed-output-format.md` 节序；七维 Scorecard 与校准按 `calibration-and-rank.md`；面板纪律按 `review-output-standards.md` / `reviewer-panel.md`；桌面检查按 `desk-checks.md`；声明—证据审计按 `universal-review-rubric.md`。1–5 维分、1–10 总分、1–5 置信度。严守 **Never round scores**：总分取 7.0，不上取整到 8，也不因项目 8.2 目标而抬分。

## Venue and assumptions

- 目标 CVPR 2027 主会、双盲；按 `venue-review-styles.md` CVPR/ICCV/ECCV 口味（novelty、technical quality、empirical validation、visual evidence、clarity、fair comparison）评分。
- 官方规则已**独立联网核验**（非仅采信项目 audit）：
  - AuthorGuidelines：「Papers are limited to eight pages, including figures and tables... Additional pages containing only cited references and the mandatory LLM Usage Statement are allowed.」；「have more than eight pages (excluding references and the LLM Usage Statement)... will be rejected without review」；「Every submission must include a section titled 'LLM Usage Statement' after the main text and before the references. It does not count toward the page limit」；「CVPR reviewing is double blind」；「When in doubt, leave links out of the submission (even in the reference list).」
  - CFP 主题确认存在：「Data synthesis, datasets and benchmarks」「Theory, optimization, and statistical learning for vision」「AI for Science and Scientific Discovery」「Medical and biological vision, cell microscopy」。
  - LLM Statement 规则另要求「name the tool(s) used, identify the parts... and briefly describe the nature and extent of the use」，「A statement that leaves out significant information may lead to desk rejection or to referral to the ethics committee」。
- 假设：不实际投稿；不修改论文任何文件；按简报指定契约产出。评分视角为「严格但公平的 CVPR 审稿人 + AC」，不迎合任何目标分数（含 8.2 与上一版 7.5）。

## Paper summary

论文追问「连线拓扑是否给视觉计算带来可测优势」，指出文献结论冲突（fixed-connectome 报告增益 vs. 度保持 null 抹除增益）源于**比较协议**而非生物学，并预注册三方裁决：在 96 节点 / 8 模块 / 注入 4 个两跳收敛 motif 的受控有向图上，用仅可经注入 motif 求解的 XOR 标签，评估嵌套 null 阶梯（L0 边数 / L1 度 / L2 模块对边数 / L3 有向三元体普查；L4 为匹配上界对照），10 冻结种子、配对 bootstrap、BH 校正。主结果：real 0.8152，所有 null rung、A=0、shuffled-input 均在 chance（0.4795–0.5133），Δ=0.30–0.34，CI 排除 0，q=0.0002；但 rung 间仅差 0.0244、单调性反转，故阶梯**无法定位**效应——「null 家族本身是混杂变量」。Eq.(1)（已明确限定为非均匀交换下的上界直觉）预测未受保护路径在混合下被销毁；§4.7 用 task-aware null 恢复优势（0.8346 vs 0.8371，q=0.40）与剂量阶梯（18/14/9/4/0 → 0.8371/0.8316/0.4988/0.5104/0.5117）闭合机制环。§4.6 的 20 图 powered 留出研究：12 预注册特征、8 个 BH 后显著、LOGO 幅度 MAE 0.1046 vs 常数 0.1635、sign agreement 0.60 = majority 0.60。§4.8（最终版两组真实 MaleCNS 实验）：dense 768 节点 / 48,713 边 / 平均入度 63.4 五条件全 chance、CI 全含 0，结构敏感前提失效（论文明确「未跑 oracle 正对照，稀释仅为假设、非已证原因」）；同图 top-4 稀疏化后（3,072 边 / 入度 4.0）real 0.6423 显著高于 A=0（0.5283）与删 motif（0.5160），但**保度零模型保留优势**（0.6162，Δ=0.0260 CI 含 0）、task-aware 0.5850，`hypothesis_supported=false`，论文明确「不作 replication claim」「三变量同时改变，无法隔离密度，仅证明真实连线上存在可解体制」。§5 新增「Relation to the strongest published control ladder」诚实对标 arXiv:2604.04033 并声明未复跑 flyvis。Conclusion 已把因果断言限定为「Within this controlled, low-in-degree regime… motif survival is a measured predictor here, not an established universal cause」。贡献定位为评估方法学/诊断标准。

## Likely stance and calibrated score

**Weak accept，下沿。校准总分 7.0 / 10，学术置信度 5 / 5。**

判定链：
- **无致命缺陷**，且上一版我列出的两个 Major 关切已真实闭合：(M2) v2 稀疏结果的 provenance 不可核验 → 现已拉回 6 件权威产物、脚本 SHA 实算匹配、逐字段交叉核对、`_provenance.status=CROSS-CHECKED`；(M3) Conclusion 无限定因果外推 → 现已加「Within this controlled, low-in-degree regime」「We do not claim this mechanism generalises… not an established universal cause」。此外 §4.8 主动声明稀释解释「remains a hypothesis, not a demonstrated cause」、follow-up「Three variables changed together… cannot isolate density」，摘要/Introduction 的 20 图表述矛盾已修，`tables_r39.tex` 自动从 pulled metrics 生成，§5 Reproducibility 的 blanket 不实声明已改为准确表述并给出两次真实图运行的已验证 SHA。这些是我逐件实算/逐字读过的真实修复，不是口头声明，故分数从上一版 6.5 上调 +0.5。
- **但仍不达 7.5 或 8**：我上一版给出的上调条件为「补齐 v2 权威产物 + 单变量隔离 follow-up + 限定 Conclusion」三者齐备 → 7.5；实际只满足两项（单变量隔离消融未做，论文坦诚承认无法隔离密度），故按自身尺度只给 +0.5 而非 +1。更根本的是，**上述改进全部属于流程完整性、诚实披露与写作一致性，没有增加支持中心主张的科学证据**：中心机制（motif 生存为控制中的因果变量）仍只在合成替身上成立，真实图上阈值未复现（`hypothesis_supported=false`）；全篇仍无图像、视觉任务或视觉 benchmark。这两条决定了分数上限。
- Never round：7.0 是校准值，不是把 6.8 上取整；6.5→7.0 的 tie-breaker 是「两个 Major 完整性/外推关切闭合」，而阻止到 7.5 的 tie-breaker 是「中心机制的外部效度仍为负 + 零视觉证据 + 单变量隔离缺失」。不照抄上一版 7.5，不迎合 8.2。

### 外部效度与负结果的价值判定（团队提示的两条）

1. **dense 负结果不是成功复现，也不构成「外部效度证据」**：五条件全 chance、CI 全含 0，论文本身定性为「结构敏感前提失效的边界条件」。它证明的是「该诊断任务不能在稠密真实图上求解，故其上的 null 比较不可解释」——是**前提失效的边界刻画**，不是对受控图结论的验证。稀释机制论文已明确标注为未证假设（无 oracle 正对照），我不把它当作已确立的因果解释来加分，也不因其为负结果而额外扣分。
2. **sparse 结果同样不是复现，但比纯负结果有增量价值，应诚实计入**：real 0.6423 显著高于 A=0 与删 motif，说明**真实生物连线上确实存在依赖该 motif 的结构效应**；且度保持 null 保留优势、task-aware 更低，与受控图模式相反——这为论文**宽泛的方法学建议**（「gate / 生存计数必须在目标图上测，不能从受控代理外推」）提供了直接的经验支持。团队提示「不要忽略诚实披露与边界刻画的价值」：我据此在 Ethics/Limitations、Top strengths 与 panel 中明确加分；但**诚实披露一个限制不等于为该限制补上证据**——`hypothesis_supported=false`、论文自述「no replication claim」，中心 motif-survival 阈值在真实图上仍未确认，故 Evidence / Significance 仍维持扣分。
3. **provenance 闭合的性质**：它把「数字可信度」从不可用提升到可核验，改善的是 Reproducibility / Soundness，**不改变**「机制未迁移」这一科学事实。

### 新增内容对旧扣分点的逐条核验（含三次修订）

| 项目 | 独立核验结论 | 状态 |
|---|---|---|
| 摘要 / Introduction 的「five held-out graphs / nineteen statistics」旧矛盾 | 已改为 powered 20 图 + 12 预注册特征 + 8 显著 + BH 校正 + sign=majority baseline；摘要 lines 40–41、贡献列表 lines 115–119 一致 | **消除** |
| §5「Relation to the strongest published control ladder」 | 存在（line 553 起）：承认 toposens2026 已有 staged control ladder、本文从其 strict endpoint 起步、明确「We did not rerun their flyvis training stack」 | **消除**（旧「定位不清」扣分） |
| LLM Usage Statement | 存在（line 719 起），位于 Conclusion 后、references 前，匿名 | **消除**（旧 desk-reject 硬伤） |
| 9 页 / 第 9 页只含参考文献 | 最新 `main.pdf`（09:00:10）9 页；p8 结尾为 Conclusion 正文，p9 仅含 LLM Usage Statement + 15 条参考文献，0 处正文关键词；0 Overfull / 0 undefined / 0 LaTeX Warning。按官方「excluding references and the LLM Usage Statement」计合规 | **消除**（含 desk check 正确判定） |
| bib 3 条更正 + 移除 `\url{}` | `main.bib` 中外链与 URL 计数为 0；抽查 arXiv:2610.10023、arXiv:2604.04033 均真实 | **消除** |
| Eq.(1) 限定为上界直觉 | line 271「upper-bound intuition, not an exact per-rung probability」 | **消除** |
| 20 图 / 8 BH / MAE 0.1046 vs 0.1635 / sign 0.60=0.60 | `r39_heldout/metrics.json` 逐字段属实；`script_sha256` 本地实算匹配；`run_complete=true` | 数字属实；但「8 显著特征」多为 intact/degraded 操纵编码，符号零技能（见 C3） |
| **v2 provenance 缺口** | `results/r39_real_connectome_v2/` 现有 6 件 pulled 产物；`r39_real_connectome_v2.py` SHA 实算 `026bf88e…` = `environment.script_sha256`；`metrics.json` 与 `metrics_from_trajectory.json` 全部共有科学字段（environment/data/mean_acc/real_minus_condition/hypothesis_supported/runtime_sec/run_complete）完全一致，仅正式文件多 `accuracies` 与 `config`；`_provenance.status=CROSS-CHECKED`；`run.log` 尾行 `done 297.1 hypothesis_supported False` | **完全闭合**（Major 扣分移除） |
| §5 Reproducibility blanket 不实声明 | 已改为 Tables 1–4、5–6 与 4 图均由脚本从 **pulled** metric 文件生成，给出 dense `090d9535…` / sparse `026bf88e…` 两个已验证 SHA，并写明逐字段 cross-check；删去「no number was transcribed by hand」 | **消除** |
| 两张手写表 → 自动生成 | `main.tex` 仅剩 1 个 `\begin{table}`（claim-to-evidence）；`\input{tables_r39}`（line 60）；`tables_r39.tex` 由 `scripts/make_r39_tables.py` 从 3 个正式 `metrics.json` 生成；逐项核对 Table 6（dense 0.5186/0.5264/0.5088/0.5156/0.5306；sparse 0.6423/0.5283/0.6162/0.5850/0.5160）与 Table 5（20(10/10)、12/8、8/12、0.1046、0.1635、0.60、0.60）与工件一致 | **消除** |
| **Conclusion 外推**（我上一版 M3） | lines 703–709 加「Within this controlled, low-in-degree regime」「We do not claim this mechanism generalises: on the real MaleCNS visual subgraph the threshold was not reproduced… measured predictor here, not an established universal cause」 | **完全闭合**（Major 扣分移除） |
| dense 稀释解释 / follow-up 混淆的**过度断言** | 新增「we did not run an oracle positive control… remains a hypothesis, not a demonstrated cause」与「Three variables changed together, so this follow-up cannot isolate density as the cause; it establishes only that a solvable regime exists on real wiring」 | **过度断言消除**；但底层实验限制（无正对照、多变量混淆）仍在，只是已诚实披露 |
| 旧流程缺陷（FAILED 预检、18017 CRC、末块崩溃） | §5 Limitations lines 644–647 如实保留 | **保留**（未消除，已披露） |
| R37 并发会话 P2 门禁异议 | 全文 grep 无 `dissent`/`concurrent`/`R37`；仅存项目 ledger/audit | **仍未入稿件**（简报称「如实保留」与稿件实际不符） |
| `benjamini1995` 悬空 / BH 无 cite | `main.bib` 16 条 vs `main.bbl` 15 条；`cite{benjamini` = 0；BH 正文 4 处无引用 | **残留**（Minor） |
| LLM Statement 未点名工具 | 仅泛称「Large language models」，未 name the tool(s) | **残留**（Minor，低概率 desk/ethics 风险） |
| **新发现：稿件与产物不一致** | §4.8 lines 538–539 称「all other settings… unchanged」「Three variables changed together」；但 pulled `config.json` 对比 v1→v2 实为**5 项**变化：`hidden` 64→128、`lr` 0.006→0.008、`epochs` 120→300、读出 `mean(1)`→`sum(1)`、top-4 稀疏化。另边数：v2 `dense_graph.n_edges=48,723` vs 论文 48,713；`sparsified_graph.n_edges=3,072` vs `data.n_edges=3,062`（后者为删 10 条 a/b→sink 边后实际训练图） | **残留**（Minor，属披露准确性；论文的「不能隔离密度」结论本身正确且更保守） |

## Scorecard（七维）

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis（可核验引用） | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 4 | 4 | §1 第 3 段；§5「Relation to the strongest published control ladder」(lines 553–573)：把控制生成器当作一等实验变量，明确「begins at their strict endpoint」；§3.4 Eq.(1) 与 §4.7 task-aware null 闭环。独立联网核实 toposens2026（arXiv:2604.04033）**本身已提出 staged control ladder** | 扣分：delta 为「更高阶 rung + 全收敛 + 校正统计 + 构造性 task-aware 检验 + 生存计数」，各 rung 组件均为标准工具（`maslov2002`/`milo2002`/`wasserman1994`），属增量而非新框架，封顶 4。升至 5 需把该标准真正应用到一篇已发表 connectome-constrained 视觉模型或真实视觉任务 |
| Soundness | 4 | 5 | §3.4 line 271 上界直觉限定；§4.7 剂量阶梯 18/14/9/4/0 → 0.8371/0.8316/0.4988/0.5104/0.5117 与 task-aware 0.8346 vs 0.8371（q=0.40）；§4.2 泄露探针 0.4902/0.5000、clean 2 通道 oracle 0.9232 vs 天花板 0.9395；§4.8 主动声明稀释「not a demonstrated cause」与「cannot isolate density」；Conclusion 已限定 | 扣分（自 3 上调）：受控图核心逻辑与全部数值可复算、v2 provenance 闭合、外推已修，故升 4。剩余缺口：(i) 预注册 3-seed 门禁 `verdict=FAILED` 保留（§4.2、metrics 第 172 行）；(ii) dense 稀释解释无 oracle 正对照、sparse follow-up 5 个变量同时改变，无法隔离密度；(iii) 18017 CRC/末块崩溃保留（已披露）。升至 5 需单变量隔离消融 + dense 正对照 + 一条哈希可核验的端到端主实验重跑 |
| Evidence | 3 | 5 | Table 1/§4.4：10 seeds，real 0.8152，Δ=0.30–0.34，CI 排除 0，q=0.0002，种子方差 2.1e-4；Table 2 invariants（L3 三元体 L1 偏差 20 vs L2 1826）；Table 4 剂量阶梯；`r39_heldout/metrics.json`：20 图、8/12 显著、MAE 0.1046 vs 0.1635；`r39_real_connectome/metrics.json` 与 `_v2/metrics.json`（均已 SHA 验证）：dense 全 chance、sparse 0.6423/0.6162/0.5850/0.5160 | **≤3 具体扣分**：(i) 中心 motif-survival 阈值在真实图上**未复现**（`hypothesis_supported=false`、度保持 null 保留优势），真实数据证据是「不确认」而非验证；(ii) 8 个显著特征（reach_a 0.869、d_reach_ab 0.850、motif_fraction 0.753、motif_edges_kept 0.725）主要由 10 intact / 10 degraded 二分操纵编码驱动，`sign_agreement=0.60 = majority_baseline=0.60`，符号零技能；(iii) flyvis 与 toposens2026 强基线未重跑（§5 Limitations、`experiment-traceability.md` rows 17–18）。**修复条件**：在操纵之外的独立图族验证特征预测力，并给出至少一个确认机制迁移的真实数据结果；满足后 → 4。注：v2 provenance 闭合使此维度达到 3 的上沿，但未改变「机制未迁移」的事实 |
| Significance | 3 | 5 | §5 四步审计、Table 7 claim-to-evidence 表；CFP 已核实含「Data synthesis, datasets and benchmarks」「Theory, optimization, and statistical learning for vision」「AI for Science and Scientific Discovery」；§4.8 新增的「null 效果依赖目标图密度/组织」边界刻画 | **≤3 具体扣分**：全篇无图像、视觉任务、视觉数据集或 benchmark，标签为合成 XOR（§3.2；§5「this is not a vision benchmark result」）；核心贡献是对 96 节点受控替身的评估方法学诊断，真实数据显示机制不迁移，对 CVPR 受众价值间接。**修复条件**：在一个真实视觉任务或已发表 connectome-constrained 视觉管线上演示该标准，或提供机制迁移确认结果 → 4 |
| Clarity | 4 | 5 | 六节结构 + Table 7 claim-to-evidence 表 + 数字可回溯到自动生成表；§3.1 scope condition、§5 Limitations 边界；Conclusion 与 Table 7 限定现已一致；`main.log` 0 Overfull / 0 undefined / 0 LaTeX Warning | 扣分：摘要单段塞入 4 组结果（lines 26–55）；§4.2 与 §5 完整性披露冗长；Table 1/4/6/7 用 `\resizebox` 缩放，双栏打印数值偏小；§4.8「all other settings unchanged / Three variables」与 pulled config 的 5 项变化不一致（披露准确性）。升至 5 需：拆分摘要、披露表化、表格改 `\footnotesize` 或两栏拆分、修正变量计数 |
| Reproducibility | 4 | 5 | 冻结种子/配置、`metrics.json`(原始未改) 与 `metrics_completed.json`、`p3_p4_taskaware/metrics.json`；三次新运行脚本 SHA 均本地**实算匹配**（`764bbdc…`、`090d95…`、`026bf88e…`）；`run_complete=true`；v2 六件 pulled 产物 + `CROSS-CHECKED`；`tables_r39.tex` 自动生成且与工件逐项一致；§5 Reproducibility 表述准确 | 扣分（自 3 上调）：M2 与 blanket 声明已完全闭合，故升 4。剩余：(i) 18017 执行脚本 CRC 不符与末块崩溃保留（主矩阵数值经 18235 独立运行定性交叉验证，未逐行对账）；(ii) 边数口径 48,723/48,713 与 3,072/3,062 未统一；(iii) `benjamini1995` 悬空、`flyhack2026` 数字编号「taken from project record」。升至 5 需一条哈希可核验的端到端主实验重跑 + 统一边数口径 |
| Ethics / Limitations | 4 | 5 | §3.1 scope condition；§5 Limitations（数据/基线/统计/协议/任务五类）明确「not a vision benchmark result」；§5 Ethics（CC-BY 4.0、无人类被试/动物实验/部署系统）；保留 FAILED 门禁、崩溃运行、CRC 缺陷与所有负结果；§4.8 `hypothesis_supported=false`、「no replication claim」、「not a demonstrated cause」、「cannot isolate density」；Conclusion「We do not claim this mechanism generalises」 | 扣分：诚实披露与边界刻画属**明显优点**（已在 Top strengths 与 panel 加分），但仍残留三项具体披露缺口：(i) R37 并发会话对 P2 门禁的异议仅存项目 ledger，未见于稿件；(ii) LLM Usage Statement 未点名所用工具（2027 规则要求 name the tool(s)，重大遗漏可触发 desk rejection / ethics referral）；(iii) BH 方法正文 4 次无引用、`benjamini1995` 悬空。补齐三项 → 5 |

**Overall:** 7.0  | **Scholarly Confidence:** 5

**Recommendation:** weak-accept（下沿；偏严格的 fit 视角会判为 borderline 6）
**Verdict:** 分数上限由「中心机制外部效度为负 + 零视觉证据」决定，**继续修流程/披露/格式不会再抬高分数**，只能靠新实验：单变量隔离的稀疏化消融 + dense 图 oracle 正对照 → 7.5；再叠加一个真实视觉任务或已发表 connectome-constrained 视觉模型上的标准演示并确认 motif 阈值 → 8。下调触发：独立复核证明 v2 数值无法从 pulled 产物复现、或 sparse 效应被证为 sum 读出/更大 hidden 的伪影 → −1 或 fatal；或 18017 修复被证明改变任一报告数字 → −0.5。置信度给 5（全文、全部证据工件、官方规则、关键前作均可得且已实算核验；v2 权威产物缺口已闭合，故不再是 4）。

## Top strengths

1. **闭合的因果环，而非仅断言**：Eq.(1) 预测未受保护 motif 边在混合下被销毁；§4.7 剂量阶梯实测 18/14/9/4/0 存活边 → 0.8371/0.8316/0.4988/0.5104/0.5117 的离散阈值；task-aware null 在完全重连背景下恢复优势（0.8346 vs 0.8371，Δ=0.0025，CI [−0.0025,0.0084]，q=0.40），并给出「保留 14/18 边的 background-only null 仍有优势」的直接证据（Table 4）。逐数与 `p3_p4_taskaware/metrics.json` 一致。
2. **异常完整的负结果与边界披露，且已避免把负结果包装成成功**：dense 五条件全 chance 明确定性为「结构敏感前提失效的边界条件」；sparse 虽恢复 0.6423 但 `hypothesis_supported=false`、度保持 null 保留效应，论文明确「no replication claim」；新增「稀释仅为假设、未跑 oracle 正对照」「三变量同时改变、不能隔离密度、仅证明存在可解体制」；Conclusion 主动写「not an established universal cause」。失败预检、崩溃运行、CRC 缺陷全部保留。这是本次评分能从 6.5 上调的主要正能量之一。
3. **可核验性现在完整且经我逐件实算**：三次新运行脚本 SHA-256 与各自 metrics 自报值逐字节匹配；v2 六件 pulled 产物齐全、正式 `metrics.json` 与轨迹副本共有科学字段完全一致、`_provenance.status=CROSS-CHECKED`；`tables_r39.tex` 由脚本从 3 个正式 metrics 生成且与数字逐项一致；§5 Reproducibility 不再有 blanket 不实声明。
4. **对最接近前作的定位诚实**：§5 承认 arXiv:2604.04033 已有 staged control ladder、本文从其 strict endpoint 起步、明确未复跑 flyvis benchmark；不谎称视觉复现。
5. **格式/引文合规已独立核实**：CVPR 2027 AuthorGuidelines 与 CFP 官方页面、两条支撑「文献冲突」前提的引用均真实；9 页中正文 < 8 页、p9 仅 LLM Statement + references；双盲、`\url{}` 清零、0 Overfull / 0 undefined / 0 Warning。

## 已闭合的关切（不再扣分）

| 旧关切 | 闭合证据 |
|---|---|
| v2 稀疏结果 provenance 不可核验（上一版 Major M2） | 6 件 pulled 产物；SHA 实算匹配；逐字段一致；`CROSS-CHECKED`；`run.log` 尾 `done 297.1 hypothesis_supported False` |
| Conclusion 无限定因果外推（上一版 Major M3） | lines 703–709「Within this controlled, low-in-degree regime」「We do not claim this mechanism generalises… measured predictor here, not an established universal cause」 |
| §5 Reproducibility blanket 不实声明 | 改为 pulled metrics 生成 + 两个已验证 SHA + 逐字段 cross-check |
| 两张手写表 | 删除，改 `\input{tables_r39}` 自动生成 |
| 摘要/Introduction 20 图矛盾 | 已改为 powered 20 图 / 12 特征 / 8 显著 / BH / sign=majority |
| dense 稀释与 follow-up 混淆的过度断言 | 明确「not a demonstrated cause」「cannot isolate density」 |
| Eq.(1) 非均匀交换假设、LLM Statement 缺失、bib 外链与 3 条题录、页数 | 均已修（见逐条核验表） |

## Major/fatal concerns

**Fatal concerns：无。** 未发现可独立支撑拒稿的新颖性坍塌、中心主张完全无证据、评测整体失效或格式/伦理硬违规。

| # | Severity | Concern | Evidence basis | Fix class | Owner | Score-change condition |
|---|---|---|---|---|---|---|
| C1 | Major | 中心机制（motif 生存为因果变量）仍只在 96 节点合成受控图上成立；真实 MaleCNS 子图上阈值未复现（dense 全 chance、sparse `hypothesis_supported=false`、度保持 null 保留优势 0.6162 CI 含 0）。论文已**如实披露**且明确不作复现声明，故不再是内部一致性缺陷，但仍是限制贡献外推的实质缺口。 | §4.8 lines 547–561、Table 6、Conclusion lines 703–709、`r39_real_connectome/metrics.json`、`r39_real_connectome_v2/metrics.json` | experiment / scope | `ccf-experiment-designer` | 在一个稀疏、cell-type-resolved、任务可解的真实子图上确认 motif-生存阈值 → Evidence/Significance +0.5 至 +1 |
| C2 | Moderate | 零视觉证据：全篇无图像、视觉任务、视觉数据集或 benchmark；XOR 为诊断工具而非自然视觉任务。对 CVPR 属间接 fit（CFP 有合法挂载点）。 | §3.2、§5「this is not a vision benchmark result」、CFP（已核实） | venue-mismatch | `ccf-experiment-designer` / `ccf-paper-writer` | 一个真实视觉任务或已发表 connectome-constrained 视觉管线上的标准演示 → Significance +0.5 |
| C3 | Moderate | 20 图「8/12 显著」主要由实验者设置的 10 intact / 10 degraded 操纵编码驱动；`sign_agreement=0.60 = majority_baseline=0.60`，符号零技能。预测统计贡献被表述为正面结论。 | `r39_heldout/metrics.json`（`feature_stats_bh_corrected`、`heldout_rows` degraded 的 reach_a≈0、motif_fraction=0.25）、§4.6、Table 5 | experiment / writing | `ccf-experiment-designer` | 操纵之外独立图族验证，或降格为探索性观察 → Evidence +0.5 |
| C4 | Moderate | 最强已发表基线未重跑（flyvis `lappalainen2024`、toposens2026 共享初始化管线）；signed/typed 边未建模。L1 只实现「度保持思想」，非其管线。 | §5 Limitations lines 637–640、§5 对标段 line 565、`experiment-traceability.md` rows 17–18 | experiment | `ccf-experiment-designer` | 新实验纲领；投稿前难补齐（属与 C1/C2 不同性质的「缺少决定性比较」） |
| C5 | Moderate | dense 稀释解释未证（无 oracle 正对照）且 sparse follow-up 多变量混淆。论文已诚实承认「cannot isolate density」，故不再是过度断言；但底层实验仍无法回答其自设问题「失败是否源于密度」。 | §4.8 lines 521–525、534–541；`r39_real_connectome.py` vs `r39_real_connectome_v2.py`（读出 mean→sum）；`config.json` 对比 | experiment | `ccf-experiment-designer` | 单变量隔离消融 + dense 正对照 → Soundness +0.5 |
| C6 | Moderate | 旧流程缺陷如实保留但未消除：3-seed 预检 `FAILED`、18017 执行脚本 CRC 不符、末块崩溃后 LOGO 由持久化行本地重算；R37 并发会话 P2 门禁异议仅存 ledger 未入稿件。 | §4.2、§5 Limitations lines 644–647、`audits/P3-P4-evidence-report.md` §8、`audits/R39-...audit.md` §4 | reproducibility | `f-research-v1` | 一条哈希可核验的端到端主实验重跑 + ledger 异议对账与稿件披露 → Soundness/Reproducibility +0.5 |
| C7 | Minor | 稿件与产物小不一致：§4.8「all other settings unchanged / Three variables」实为 5 项变化（hidden 64→128、lr 0.006→0.008、epochs 120→300、mean→sum、top-4 稀疏化）；边数口径 48,723/48,713 与 3,072/3,062 未统一；`benjamini1995` 悬空、BH 4 处无 cite；LLM Statement 未点名工具。 | §4.8 lines 538–539、两份 `config.json`、两份脚本 readout 行、`main.bib`(16) vs `main.bbl`(15)、`main.tex` line 719 | writing / reproducibility | `ccf-paper-writer` | 修正变量计数与边数口径、引用 BH、点名工具 → 消除 low desk 风险，Clarity/Reproducibility +0.5 |
| C8 | Minor | 摘要单段 4 组结果过载；§4.2/§5 披露冗长；Table 1/4/6/7 `\resizebox` 缩放导致打印数值偏小。 | 摘要 lines 26–55、§4.2、§5、Tables 1/4/6/7 | writing | `ccf-paper-writer` | 拆摘要 + 披露表化 + 表格改 `\footnotesize`/两栏拆分 → Clarity +0.5 |

### Claim–Evidence Audit（主要主张）

| Claim | Where stated | Evidence provided | Strength | Reviewer deduction | Required fix |
|---|---|---|---|---|---|
| 受控图上结构优势真实且可复现 | 摘要、§4.4、Conclusion | Table 1：10 seeds，Δ=0.30–0.34，CI 排除 0，q=0.0002；A=0/clean_motif/shuffled 对照 | strong | 无 | 无 |
| 匹配全局高阶统计无法定位优势 | §1、§4.4–4.5、Table 7 | rung 间 Δ 仅差 0.0244；单调性 1 次反转；L1 已匹配 conv2 统计却仍 chance | adequate | 结论仅在受控图成立，稿件已限定 | 无（已 scope） |
| motif 生存（非 rung 顺序）是因果变量 | §1 贡献 2、§4.7、Conclusion lines 703–709 | Eq.(1) + 剂量阶梯 + task-aware null（受控图） | adequate（受控图）/ weak（真实图） | 真实图 `hypothesis_supported=false`；稿件已写「measured predictor here, not an established universal cause」 | 真实图确认实验；否则维持 scope |
| 幅度可预测、符号不可预测 | 摘要、§4.6、Table 5 | 20 图、8/12 BH 显著、MAE 0.1046 vs 0.1635、sign 0.60=0.60 | weak | 显著特征多为操纵编码；符号零技能 | 降格为探索性；补操纵外验证 |
| 真实 MaleCNS 结果界定协议边界、支持「在目标图上测 gate」 | §4.8 lines 554–561、摘要、Conclusion、Table 7 | dense 全 chance；sparse real 0.6423 但度保持 null 保留效应、假说未确认、no replication claim | adequate（对宽泛方法学建议）/ absent（对中心机制） | 是「不迁移边界」而非外部效度验证；稀释解释未证、follow-up 混淆已诚实披露 | 明确区分两类主张；补 oracle 与单变量消融 |
| 所有表格由 pulled metric 文件脚本生成 | §5 Reproducibility lines 655–666 | Tables 1–4、5–6 与 4 图；两个 SHA；逐字段 cross-check；`tables_r39.tex` 自动生成 | strong | 无（已实算核验） | 统一边数口径 |
| 全部参考文献已核实、无虚构题录 | R39 audit、main.bib | 抽查 2 条关键引用真实；`benjamini1995` 悬空未引；BH 正文 4 次无 cite | adequate | 15 条编译 vs 16 条 bib | 引用 BH / 清理悬空条目 |

## Writing concerns

- **摘要超载**：lines 26–55 一段塞入「主矩阵 + 阶梯失败 + 构造性检验 + 20 图 + 真实数据」四组结果；建议拆成「裁决结果」与「机制/边界」两句群。line 54「delimiting the protocol's scope」后换行略显突兀（排版细节）。
- **披露冗长**：§4.2 与 §5 Limitations 完整性披露占篇幅大且信息密度低；建议压成「defect / status / affected number / disposition」小表。
- **表格可读性**：Table 1、4、6、7 使用 `\resizebox`，双栏打印数值列偏小；建议 `\footnotesize` 或两栏拆分。
- **披露准确性（新发现，见 C7）**：§4.8「all other settings … unchanged / Three variables changed together」与 pulled `config.json` 不符（实为 5 项变化：hidden、lr、epochs、readout、稀疏化）。论文的「不能隔离密度」结论正确且更保守，但变量计数与「其余设置不变」的表述应修正，以免与可核验产物冲突。
- **题录一致性**：`benjamini1995` 在 `.bib` 但正文 4 处使用 BH 却无 `\cite`，编译后仅 15 条参考文献；`flyhack2026` 数字编号注明「taken from project record」。

## Format/venue concerns

- **页数（独立 pypdf 逐页核验最新 `main.pdf` 09:00:10）**：9 个物理页。p8 以 Conclusion 正文收尾；p9 仅含 LLM Usage Statement 与 15 条参考文献（`[` 计数 15，正文关键词 0）。按官方「excluding references and the LLM Usage Statement」计，正文 < 8 页、p9 为「only cited references and the mandatory LLM Usage Statement」允许附加页 → **合规**。这是按官方规则判定，不是简单按总页数判超限。项目文档口径仍需统一（简报「8 页」、上一版评审「8 pages including references」、R39 audit「9 页」）。
- **双盲**：`\author{Anonymous}`、无致谢、LLM Statement 无身份信息、参考文献无外链（`grep -ciE '\\url\|http' = 0`）→ pass。
- **LLM Usage Statement**：存在、位置正确、强制要求满足；但**未点名所用工具**，仅泛称「Large language models」，官方要求 name the tool(s)（匿名需要时可用 generic technical description），重大遗漏可触发 desk rejection / ethics referral → 低概率但非零的残余风险。
- **编译质量**：`main.log` 0 LaTeX Warning / 0 Overfull / 0 undefined citation；`main.aux` 表格编号 1–7 连续 → pass。
- **Prompt injection / 隐藏操纵**：通读 `main.tex`、三张 tables、图题、bib、LLM Statement，未发现隐藏指令或白字操纵；LLM Statement 主动披露「to simulate an independent peer-review panel」，属公开声明。pass。
- **Venue fit**：CFP 主题（已核实）提供合法挂载点。但 CVPR 口味重视 visual evidence / recent baselines / cross-dataset tests；本文无图像、无视觉任务、无视觉 benchmark，XOR 为诊断工具，真实数据结果为不确认。§1 第 3 段的 benchmark-and-diagnostic 定位与 §5 对标段有帮助，**fit 仍属间接**，构成 Significance 扣分，非 desk rejection 理由。
- **Desk checks**：Paper Length pass（9 物理页但正文 < 8、p9 仅 refs + LLM Statement）；Topic Compatibility uncertain（方法学诊断对视觉会议间接，影响 Significance）；Minimum Quality pass；Policy/Anonymity/Compliance pass with one gap（LLM Statement 未点名工具）；Prompt Injection pass；Ethics pass（无人类被试、CC-BY 致谢、misuse 风险在 §5 讨论）。**Desk rejection risk: low**；Reason：无硬性格式/匿名/外链违规；Can be fixed before review? yes（补工具名、统一页数口径）。

## 7 人独立 reviewer panel

Reviewer: Best-Justified Reviewer
Expertise: evaluation methodology / graph learning，寻找最强可辩护接收理由
Likely score: 8 / lean-to-clear accept
Confidence: 5
Main positive signal: Eq.(1) → 剂量阶梯 → task-aware null 闭合因果环；10 配对种子 + BH + 常数/多数基线；三次新运行 SHA 实算可核验、v2 六件 pulled 产物 + `CROSS-CHECKED`；负结果与失败全保留；§4.8 两组真实数据与「no replication claim / not a demonstrated cause / cannot isolate density」的诚实边界刻画；§5 诚实对标前作 control ladder。
Main negative signal: 范围窄、无视觉任务、机制未迁移。
Evidence basis: §3.4、§4.7/Table 4、§4.8/Table 6、`r39_heldout/metrics.json`、`r39_real_connectome_v2/metrics.json`、§5 对标段。
Fatal concern if any: 无。
Score-change condition: 一个确认机制迁移的真实数据结果 → 9。

Reviewer: Critical Reviewer
Expertise: 严格 CVPR 审稿人，寻找最强拒稿理由
Likely score: 5 / borderline to lean reject
Confidence: 5
Main positive signal: 承认内部逻辑自洽、统计未 cherry-pick、披露异常坦诚；provenance 与 Conclusion 外推已闭合，不再有完整性硬伤。
Main negative signal: 全部正向发现来自 96 节点合成 XOR 替身；零图像/视觉任务/benchmark；真实数据 dense 全 chance、sparse `hypothesis_supported=false` 且度保持 null 保留效应（中心机制反例）；sign 0.60=0.60；强基线未重跑；FAILED 预检与 18017 CRC 保留；稀释解释无正对照、follow-up 5 变量混淆。
Evidence basis: §3.1、§4.8/Table 6、§5 Limitations、`r39_real_connectome_v2/config.json`、`audits/P3-P4-evidence-report.md` §8。
Fatal concern if any: 无硬致命；「中心机制不迁移 + 无视觉证据」组合接近 major threshold。
Score-change condition: 真实视觉任务演示 + 机制确认 → 7。

Reviewer: Method / Soundness Reviewer
Expertise: 因果推断 / 图 null 模型 / 统计有效性
Likely score: 7 / lean accept
Confidence: 5
Main positive signal: Eq.(1) 已正确限定为上界直觉；剂量阶梯与 14/18 存活边对照直接检验机制；主矩阵数值与 CI 逐项可复算；§4.8 主动承认稀释未证与多变量混淆；Conclusion 已限定，内外一致。
Main negative signal: 预注册门禁仍 `FAILED`；sparse follow-up 实改 5 变量（稿件称 3 项）无法隔离密度；dense 无 oracle 正对照；`find_motif` 在稠密图未证明唯一信息路径。
Evidence basis: §3.4 line 271、§4.2、§4.8 lines 521–541、`r39_real_connectome.py` vs `_v2.py`、两份 `config.json`。
Fatal concern if any: 无。
Score-change condition: 单变量隔离消融 + 正对照 + 端到端哈希重跑 → 8。

Reviewer: Evidence / Experiment Reviewer
Expertise: baselines / ablations / 统计功效 / 复现
Likely score: 6 / borderline
Confidence: 5
Main positive signal: 10 seeds、配对 CI、全族 BH、鲁棒性 2×2 网格、两个证伪消融、20 图 powered 研究、三组运行全部 SHA 可核验、两张表自动生成、逐字段 cross-check、`run_complete=true`。
Main negative signal: 8/12 显著特征多为 intact/degraded 操纵编码；sign 等于多数基线；真实数据 `hypothesis_supported=false`；强基线未重跑；dense 无正对照、sparse 混淆；边数口径与变量计数不一致。
Evidence basis: Tables 1–6、`r39_heldout/metrics.json`、`r39_real_connectome_v2/{metrics.json,config.json}`、`experiment-traceability.md`。
Fatal concern if any: 无。
Score-change condition: 操纵外独立验证 + 真实图机制确认 + 强基线 → 8。

Reviewer: Novelty / Positioning Reviewer
Expertise: 最接近前作与真实 delta
Likely score: 6 / borderline
Confidence: 4
Main positive signal: 独立核实 toposens2026 已把更高阶 null/更长训练列为 future work；本文补足并新增 task-aware 构造性检验 + 生存计数框架；§5 定位诚实、明确未复跑 flyvis。
Main negative signal: 前作**本身已有 control ladder**，本文 delta 为更高阶 rung + 收敛训练 + 校正统计 + 构造检验，组件均为标准工具；venue fit 方法学而非视觉。
Evidence basis: §5 lines 553–573、arXiv:2604.04033 摘要（联网核实）、`maslov2002`/`milo2002`/`wasserman1994`。
Fatal concern if any: 无（新颖性未坍塌，封顶 4/5）。
Score-change condition: 在已发表视觉模型上应用该标准 → 8。

Reviewer: Writing / Clarity Reviewer
Expertise: 贡献可恢复性 / 图表可解释性
Likely score: 7 / lean accept
Confidence: 5
Main positive signal: 六节结构、claim-to-evidence 表、数字可回溯到自动生成表、显式 scope conditions、Conclusion 与 Table 7 现已一致、编译零警告、新增诚实声明措辞准确。
Main negative signal: 摘要过载；两处长披露；`\resizebox` 表格偏小；§4.8「Three variables / all other settings unchanged」与 pulled config 不符。
Evidence basis: 摘要 lines 26–55、§4.2、§4.8 lines 538–539、§5、Tables 1/4/6/7、`main.log`。
Fatal concern if any: 无。
Score-change condition: 拆摘要 + 披露表化 + 修正变量计数 → 8。

Reviewer: Ethics / Reproducibility Reviewer
Expertise: 许可 / 透明性 / 失败披露 / artifact 审计
Likely score: 8 / lean-to-clear accept
Confidence: 5
Main positive signal: CC-BY 4.0 致谢、无人类被试；FAILED 门禁、崩溃运行、CRC 缺陷、dense 负结果、`hypothesis_supported=false`、稀释未证、多变量混淆全部如实上报且不作复现/泛化声明；v2 六件 pulled 产物 + SHA 实算匹配 + `CROSS-CHECKED`；`tables_r39.tex` 自动生成；§5 Reproducibility 表述准确；无外链、双盲。
Main negative signal: R37 门禁异议未入稿件；LLM Statement 未点名工具；`benjamini1995` 悬空、BH 无 cite；边数口径不统一。
Evidence basis: §5 Limitations/Ethics/Reproducibility、`audits/R39-reference-venue-and-integrity-audit.md` §4、`main.bib`(16) vs `main.bbl`(15)、v2 目录清单。
Fatal concern if any: 无。
Score-change condition: 补齐三项披露 + 引用 BH + 统一边数 → 9。

### Panel synthesis

Agreement: 七位一致认为受控图内部逻辑、统计卫生与数值可复算性成立；v2 provenance、Conclusion 外推、blanket 复现声明、摘要矛盾等旧硬伤已真实闭合；论文对负结果与边界的诚实披露属罕见优点；无致命缺陷。
Disagreement: Best-Justified(8)/Ethics(8) 与 Critical(5)/Evidence(6) 在「一个完全由合成替身支撑、且真实数据显示机制不迁移的方法学诊断，是否够 CVPR 级贡献」上对立；Method(7) 强调 5 变量混淆与「3 变量」表述不符。
Decisive positive axis: 闭合因果环 + 完整可核验 artifacts（三次运行 SHA + pulled v2 + 自动生成表） + 异常透明的负结果纪律 + Conclusion/§4.8 的严格 scope。
Decisive negative axis: 零视觉证据 + 真实图 `hypothesis_supported=false` 且度保持 null 保留效应（中心机制未迁移） + sign 零技能 + 强基线未重跑 + 单变量隔离消融缺失。
Unresolved evidence: v2 后 dense 稀释机制是否成立（无 oracle 正对照）；sparse 恢复是否部分源于 sum 读出/更大 hidden；R37 P2 门禁异议对账；18017 CRC。
AC stance: **weak-accept 下沿，7.0**。最终立场跟随「最强未解决关切」——中心机制外部效度为负且全篇无视觉证据——不被「诚实披露 / provenance 闭合 / 格式合规」平均掉；两个 Major 完整性关切闭合使分数自 6.5 上调 +0.5，但流程改进不等于新增科学证据，故不达 7.5/8.2。

## Concern-to-action

| Concern | Action | Owner | Affected criterion | Score-change condition |
|---|---|---|---|---|
| C1 机制未迁移 | 在稀疏、路径可辨识的真实子图上确认 motif-生存阈值；维持现有严格 scope | `ccf-experiment-designer` | Evidence, Significance | +0.5 至 +1 |
| C2 零视觉证据 | benchmark/analysis-track 定位 + 至少一个真实视觉任务/已发表管线演示 | `ccf-experiment-designer` / `ccf-paper-writer` | Significance | +0.5 |
| C3 预测贡献 | 操纵外独立图族重测 12 特征；或把 §4.6 降格为探索性 | `ccf-experiment-designer` | Evidence | +0.5 |
| C4 强基线 | 重跑 flyvis / toposens2026 管线并加入 task-aware 控制 | `ccf-experiment-designer` | Evidence, Novelty | +0.5（投稿前难） |
| C5 稀释未证 / 多变量混淆 | 把稀疏化、hidden、lr、epochs、读出聚合拆成单变量消融；dense 补 oracle 正对照 | `ccf-experiment-designer` | Soundness | +0.5 |
| C6 流程缺陷 | 一条哈希可核验的端到端主实验重跑；ledger R37 异议对账并在稿件披露 | `f-research-v1` | Soundness, Reproducibility, Ethics | +0.5 |
| C7 披露准确性 | 修正「3 变量/其余不变」为实改项；统一边数 48,713/48,723 与 3,072/3,062；引用 `benjamini1995` 或清条目；LLM Statement 点名工具 | `ccf-paper-writer` | Clarity, Reproducibility, Ethics | 消除 low desk 风险 |
| C8 写作/排版 | 拆摘要、披露表化、`\resizebox` 改 `\footnotesize`/两栏拆分 | `ccf-paper-writer` | Clarity | +0.5 |

## Score-Change Conditions

| Change | Condition | Likely affected dimensions | Expected movement |
|---|---|---|---|
| Raise score | 单变量隔离的稀疏化消融 + dense 图 oracle 正对照（补齐上一版三条上调条件的第三条） | Soundness, Evidence | +0.5 overall（→ 7.5） |
| Raise score | 一个真实视觉任务/已发表 connectome-constrained 视觉模型上的标准演示，且确认 motif 阈值迁移 | Significance, Novelty, Evidence | +0.5 到 +1 overall（→ 8） |
| Raise score | 操纵外独立图族验证特征预测力 + 强基线重跑 | Evidence, Novelty | +0.5 overall |
| Raise score | 修正 5 变量计数 / 边数口径 / BH 引用 / LLM 工具名 / R37 披露 | Clarity, Reproducibility, Ethics | 消除 low desk 风险；+0.5 overall 上限 |
| Lower score | 独立复核证明 v2 数值无法从 pulled 产物复现，或 sparse 效应被证为 sum 读出 / hidden 128 的伪影 | Reproducibility, Soundness | −1 overall 或 fatal |
| Lower score | 确认 R37 异议意味着结构敏感前提从未通过、或 18017 修复影响任一报告数字 | Soundness, Reproducibility | −0.5 到 −1 overall |
| No quick change | 自然视觉任务上的外部效度、强基线重跑、机制迁移确认需新实验纲领；继续修流程/披露/格式不会再抬高总分 | Significance, Evidence | 投稿前不大可能改变 |

## Checks run

1. 三次重新锁定磁盘版本并通读最终 `main.tex`（09:00:08，736 行 / 42088 B / md5 `cd17e1e6…`）、`main.bib`、`tables.tex`、`tables_taskaware.tex`、`tables_r39.tex`、`main.bbl`、`main.aux`、`main.log`，逐页抽取最新 `main.pdf`（09:00:10，9 页）。
2. 逐数核对全部 metrics：`p3_p4/metrics.json`（原始，含 `main_matrix_partial`/`robustness_partial`/`heldout_partial` 崩溃痕迹）与 `metrics_completed.json`；`p3_p4_taskaware/metrics.json`；`r39_heldout/metrics.json`；`r39_real_connectome/metrics.json`；`r39_real_connectome_v2/metrics.json`（权威）与 `metrics_from_trajectory.json`。稿件数字与工件一致（real 0.8152、Δ 0.30–0.34、q=0.0002、rung 差 0.0244、剂量阶梯、8/12、MAE 0.1046/0.1635、sign 0.60/0.60、768/48,713/9,766/1,051,241,946 B、dense 五条件 CI 含 0、sparse 0.6423/0.6162/0.5850/0.5160、`hypothesis_supported=false`）。
3. **SHA-256 实算**：`r39_heldout_slim.py`→`764bbdc…`、`r39_real_connectome.py`→`090d95…`、`r39_real_connectome_v2.py`→`026bf88e…`，三者与各自 metrics 自报值逐字节匹配；`run_complete=true`。
4. **v2 provenance 闭合核验（本轮新增，结论：已闭合）**：v2 目录现有 `metrics.json`(3346B)、`summary.txt`、`run.log`、`config.json`、`README.md`、`r39_real_connectome_v2.py` 六件 pulled 产物；正式 `metrics.json` 与轨迹副本的全部共有科学字段（environment/data/mean_acc/real_minus_condition/hypothesis_supported/runtime_sec/run_complete）**逐字段相等**，仅正式文件多 `accuracies` 与 `config`；`_provenance.status=CROSS-CHECKED` 且 cross_check 文本与实算一致；`run.log` 尾行 `done 297.1 hypothesis_supported False`；`watch_18252.log` 的 `status: processing` 为收尾前快照，已被 pulled 产物取代。**性质：数字可信度问题已解决，不属「机制未迁移」类科学问题。**
5. **表格自动生成核验**：`scripts/make_r39_tables.py` 数据源为 3 个正式 `metrics.json`；`tables_r39.tex` 的 Table 6/Table 5 数值与工件逐项一致；`main.tex` 仅剩 1 个手写 `\begin{table}`（claim-to-evidence），`\input{tables_r39}`（line 60）。
6. **稿件—产物一致性核验（新发现 C7）**：逐字段对比 v1/v2 `config.json`，确认 v1→v2 实改 5 项（`hidden` 64→128、`lr` 0.006→0.008、`epochs` 120→300、readout `mean(1)`→`sum(1)`、top-4 稀疏化），而 §4.8 lines 538–539 称「all other settings unchanged / Three variables」；`dense_graph.n_edges=48,723` vs 论文 48,713，`sparsified_graph.n_edges=3,072` vs `data.n_edges=3,062`（后者为删 10 条 a/b→sink 边后实际训练图）。
7. 读 `r39_real_connectome.py`、`r39_real_connectome_v2.py` 全文，核验 `find_motif`/`cnorm`/读出实现与稀疏化逻辑，据此判断稀释解释与混淆。
8. 读 `audits/P3-P4-evidence-report.md`、`P4-taskaware-evidence-report.md`、`R39-reference-venue-and-integrity-audit.md`、`experiment-traceability.md`（rows 19–25、row 23 的 v2 条目）。
9. 编译/题录检查（最新 09:00:10）：`main.log` LaTeX Warning=0 / Overfull=0 / undefined=0；`grep -ciE '\\url\|http' main.bib = 0`；`main.bbl` 15 个 `\bibitem` vs `main.bib` 16 个 `@`；`cite{benjamini`=0、`Benjamini in bbl`=0；`\cite` 键 15 个；表格编号 1–7 连续；p9 仅 LLM Statement + 15 条 refs。
10. **联网独立核验**：CVPR 2027 AuthorGuidelines（页数/LLM Statement/双盲/外链/desk-reject 原文）与 CFP（主题、截止日期）；arXiv:2610.10023、arXiv:2604.04033（真实，后者确已使用 control ladder）。
11. 版本漂移核对：`stat`/`wc`/`md5` 对比 08:24 / 08:39 / 08:54 / 09:00 四版；`main.pdf`/`main.bbl` 09:00:10 重编译。
12. 读上一版评审（7.5）仅作历史扣分点；并复核我上一版报告的 Verdict 条件（三条上调条件中已满足两条），据此给出 +0.5 而非 +1。
13. 一致性自检：总分 7.0 与「最强未解决关切 = 机制外部效度为负 + 零视觉证据」匹配；两个 ≤3 维分（Evidence 3、Significance 3）均含具体扣分与修复条件；无致命缺陷故不 reject；未迎合 8.2。

## Unresolved

**A 类 — 已闭合（不再扣分，勿与下列混为一谈）**：v2 稀疏结果 provenance 缺口：六件 pulled 产物齐全、脚本 SHA 实算匹配、正式与轨迹 metrics 共有字段逐字段一致、`CROSS-CHECKED`、`run.log` 显示 `done`；§5 Reproducibility blanket 不实声明已改为准确表述；两张手写表已改为自动生成；Conclusion 外推、稀释过度断言、混淆 follow-up 过度断言均已限定或坦承；摘要 20 图矛盾、Eq.(1) 限定、LLM Statement、bib 外链/题录、页数合规均已完成。

**B 类 — 仍未解决，且属「缺少决定性实验/比较」性质（与 A 类不同）**：
- **flyvis / toposens2026 强基线仍未重跑**（§5 已诚实声明；L1 只实现度保持思想，非其管线）。
- **真实图 motif-survival 阈值仍未复现**：sparse `hypothesis_supported=false`、度保持 null 保留优势 0.6162（CI 含 0）；论文明确不作 replication claim。这不是「负结果被隐瞒」，而是中心机制外部效度的实质缺口。
- **dense 稀释解释仍为假设**：无 oracle 正对照；sparse 恢复同时改变 5 变量，无法隔离密度，sparse 效应是否部分源于 sum 读出 / hidden 128 / lr 0.008 未排除。
- **单变量隔离消融缺失**（上一版三条上调条件中唯一未满足项）。

**C 类 — 残留流程/披露小项**：R37 并发会话 P2 门禁异议仅存项目 ledger 未入稿件；18017 CRC 与末块崩溃保留；`benjamini1995` 悬空、BH 无 cite；LLM Statement 未点名工具；§4.8「3 变量/其余不变」与 5 项实际改动不符；边数口径 48,723/48,713 与 3,072/3,062 未统一；`flyhack2026` 数字编号「taken from project record」；peak GPU memory (18017) 未写入、runtime 由日志推导。

**D 类 — 版本漂移**：稿件在评审期间被三次并发改写；本报告锁定 09:00 版 md5 `cd17e1e6…`。若之后再变，尤其 §4.8 / Conclusion / §5 Reproducibility，请按锁定 md5 复核。

## Output self-check

- 节序遵循 full 契约：Mode / Venue and assumptions / Paper summary / Likely stance and calibrated score（内嵌「外部效度与负结果价值判定」「新增内容逐条核验」）/ 七维 Scorecard / Top strengths / 已闭合的关切 / Major-fatal concerns（内嵌 Claim–Evidence Audit）/ Writing concerns / Format-venue concerns（内嵌 Desk checks）/ 7 人独立 reviewer panel（含 Best-Justified 与 Critical，附 Panel synthesis）/ Concern-to-action / Score-Change Conditions / Checks run / Unresolved（A/B/C/D 分类）/ Output self-check。✔
- 所有 Markdown 表分隔符有效、每行列数一致（已用脚本逐表校验）。✔
- 分数、置信度、Recommendation 内部一致：7.0 = weak-accept 下沿、Confidence 5、无致命缺陷、两个 Major 关切闭合但科学上限由机制外部效度决定。✔
- 机器可读结论行**有且仅有一行**，采用简报指定的严格格式（Overall + Scholarly Confidence 两项、整数置信度）；另给 Recommendation 与 Verdict。✔
- 严守 Never round scores：7.0 未取整到 8，未因 8.2 目标抬分；6.5→7.0 的 +0.5 与「两个 Major 关切闭合、三条上调条件满足两条」的 tie-breaker 明确写出。✔
- 两个 ≤3 维分（Evidence 3、Significance 3）均含可核验引用、具体扣分与修复条件；其余维分亦各带引用与条件。✔
- 每个分数均有可核验引用（章节/表/行号或工件字段）。✔
- Checks run / Unresolved 如实区分 A 类（v2 provenance 已闭合）与 B 类（强基线未重跑、真实图阈值未复现）两类不同性质问题。✔
- 特别判定已给出：§4.8 dense 为「暴露前提失效的边界条件」、sparse 为「增量方法学价值但非复现」；venue fit 间接；格式按官方规则判定合规（9 页、p9 仅 refs + LLM Statement）。✔
- 无 `TBD`/`TODO`/`[fill]`/空标题；无「improve clarity / needs more experiments」类无定位泛化填充。✔
- 因果/递进逻辑显式：问题 → 证据 → 后果 → 动作。✔
- 未修改论文任何文件；仅写出本报告。✔

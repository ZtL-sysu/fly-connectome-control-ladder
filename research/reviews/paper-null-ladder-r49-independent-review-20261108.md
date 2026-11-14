# CCF Paper Reviewer — Full Mode 独立评审报告（R49 / 修订后定稿）

**Paper:** *A Structure-Sensitive Null Ladder Exposes a Blind Spot in Connectome-Control Protocols*
**Target venue:** CVPR 2027（主会，double blind）
**Review date:** 2026-11-08
**Reviewer:** general-purpose-1（独立 CCF-A 审稿人 / AC，与论文作者无关）
**Mode:** `full` — scientific + writing + format + revision-action synthesis
**Input materials:** 磁盘当前最新版 `paper/main.tex`（721 行 / 40,897 B / md5 `9cdb5ea637e741ae7e9d56fcb607b7ce`）、`main.bib`、`main.bbl`、`main.log`、`main.aux`、`main.pdf`（9 页）、`tables.tex`、`tables_taskaware.tex`、`tables_r39.tex`、`tables_r46.tex`、`scripts/make_r46_tables.py`、`scripts/make_r39_tables.py`；`results/` 下 7 组 `metrics.json`（`p3_p4`、`p3_p4_taskaware`、`r39_heldout`、`r39_real_connectome`、`r39_real_connectome_v2`、`r39_density_sweep`、`r39_visual_task`）及其 `config.json` / `run.log` / `summary.txt` / `graph_stats.json` / 执行脚本 `.py`；`audits/R46-correction-experiments-audit.md`、`experiment-traceability.md`、`goal-ledger.md`（R37）；历史评审链 `...full-review-20261108.md`(7.5)、`...r39-full-review-20261108.md`(8.2)、`...r39-independent-review-20261108.md`(7.0)、`...r47-independent-review-20261108.md`(7.5) 仅作扣分演化与校准条件参考，不照抄任何分数。
**Search basis:** 本次**未重新联网**；CVPR 2027 页数 / LLM Usage Statement / 双盲 / 外链条款与关键前作题录（arXiv:2610.10023、arXiv:2604.04033）沿用同日 R47 独立联网核实结论，已在 Confidence / Unresolved 标注。本报告分数不依赖该外部核实：版式合规只影响 desk 风险消除，不改变由证据决定的总分。

## ⚠ 版本锁定声明（必读）

本报告评审的是磁盘上 **2026-11-08 当前最新版** `main.tex`（`md5 9cdb5ea637e741ae7e9d56fcb607b7ce`，721 行 / 40,897 B），对应同目录 `main.pdf`（9 个物理页）。历史 R47 独立报告锁定的是 719 行 / 40,612 B / md5 `4afd89c155bb13af4153fe316f206f79` 版；本版相对它做了四项实质修订（§4.9 四条件表格与正文补报 + 削弱自身主张的限定 + Conclusion 重写、§4.10 MNIST delta 补报、visual 脚本拉回与第四 SHA + R37 两方分歧、压缩回 9 页合规）。历史 7.5 / 8.2 / 7.0 / 7.5 报告均为历史，不构成本次判定依据。若之后版本再变，请按本声明锁定 md5 复核。

---

## Mode

`full`。按 `SKILL.md` 输出契约节序；七维 Scorecard 与校准按 `calibration-and-rank.md`；面板纪律按 `review-output-standards.md` / `reviewer-panel.md`；桌面检查按 `desk-checks.md`；声明—证据审计按 `universal-review-rubric.md`。1–5 维分、1–10 总分、1–5 置信度。严守 **Never round scores**，不迎合任何目标分数（含 8.0 / 8.2 / 7.5），不照抄历史分数，独立从证据推演。

## Venue and assumptions

- 目标 CVPR 2027 主会、双盲；按 CVPR/ICCV/ECCV 口味（novelty、technical quality、empirical validation、visual evidence、clarity、fair comparison）评分。
- 页数 / LLM Statement 规则沿用 R47 同日联网核实结论：官方 AuthorGuidelines 确认「Eight pages, figures and tables included. References and the LLM Usage Statement may go on further pages」「LLM Usage Statement, after the main text and before the references. It does not count toward the eight pages」「Mandatory LLM Usage Statement… Papers without it will be desk-rejected」、desk-reject 清单含「missing LLM Usage Statement」「external links that expand the paper」「prompt injection and fabricated content」、双盲无外链。本次不重新联网，已在 Confidence 与 Unresolved 标注。
- 假设：不实际投稿；不修改论文任何文件；按指定契约产出唯一新报告。评分视角为「严格但公平、与作者无关的 CVPR 审稿人 + AC」。团队指令明确：不迎合 8.0；若「真实图机制迁移未确认」这一决定性缺口仍在，按本报告尺度维持不到 8；不因论文主动写出对自己不利的限定而额外惩罚，也不因其披露负结果而默认加分。

## Paper summary

论文追问「连线拓扑是否给视觉计算带来可测优势」，指出文献结论冲突源于**比较协议**而非生物学，并预注册三方裁决：在 96 节点 / 8 模块 / 注入 4 个两跳收敛 motif 的受控有向图上，用仅可经注入 motif 求解的 XOR 标签，评估嵌套 null 阶梯（L0 边数 / L1 度 / L2 模块对边数 / L3 有向三元体；L4 为匹配上界对照），10 冻结种子、配对 bootstrap、BH 校正。主结果：real 0.8152，所有 rung、A=0、shuffled-input 均在 chance（0.4795–0.5133），Δ=0.30–0.34，CI 排除 0，q=0.0002；但 rung 间仅差 0.0244、单调性反转，阶梯**无法定位**效应。Eq.(1)（限定为非均匀交换下的上界直觉）预测未受保护路径在混合下被销毁；§4.7 task-aware null（0.8346 vs 0.8371，q=0.40）与剂量阶梯（18/14/9/4/0 → 0.8371/0.8316/0.4988/0.5104/0.5117）闭合机制环。§4.6 的 20 图 powered 研究：12 预注册特征、8 个 BH 后显著、LOGO 幅度 MAE 0.1046 vs 常数 0.1635、sign agreement 0.60 = majority 0.60，已降格为 *corrected association* 并承认 8 个显著特征部分编码 intact/degraded 操纵。§4.8 两组真实 MaleCNS 实验：dense（768 节点 / 48,713 边）五条件全 chance；top-4 稀疏化后 real 0.6423 高于 A=0（0.5283）与删 motif（0.5160），但**度保持 null 保留优势 0.6162（CI 含 0）**、`hypothesis_supported=false`，已如实改为「Five settings changed together」并声明不能据此主张 motif-survival 阈值。

**§4.9 单变量密度隔离（本轮补报的关键）**：新流式真实 MaleCNS 视觉子图（44,815 边 / mean in-deg 58.35 / 29,442 visual body IDs）上只改 top-k（k=63/16/8/4/2），其余写死；oracle MLP 直接读 `[X_a,X_b]` 6 seeds 全 1.0000；real 0.5049→0.4886→0.5075→0.6227→**0.9863**→**0.9987**，A=0 恒 0.5062、度保持 null 恒 ~0.50、`density_isolated=true`。**本版表格补齐全部四条件**（real / A=0 / L1_degree_null / task_aware_null），`task_aware_null` 在 k=4/2 为 **0.9027 / 0.9971**，与 real 同步恢复，是受控图 task-aware 结论在真实图上的唯一呼应；正文同时**主动写入削弱自身主张的限定**：k=4/2 时受保护 relay→sink 边 `23→63` 已丢失而 real 仍近 ceiling，故可解体制不能唯一归因于该保护边集，论文明确「claim a density boundary, not a transferred motif-survival threshold」，Conclusion 重写为「Motif survival is a measured predictor in one regime, not a universal cause」。

**§4.10 真实视觉任务（本轮补报的关键）**：`sklearn.load_digits` 8×8 手写数字 10 类（1078/359/360）+ MNIST add-on，768 节点 MaleCNS 稀疏视觉子图作固定先验，五条件 6 seeds：real 0.7185 显著高于 A0 0.6190（Δ=+0.0995），但度保持 null 0.7190 与 real 无差异（Δ=−0.0005），非图 MLP **0.9722** 大幅主导（MNIST 0.8879 vs 0.7649）。本版正文补报此前被省略的 MNIST `real − degree_preserving_null = +0.0148, CI [0.0100,0.0192]`（显著为正、与 digits 方向相反），并写明「null behaviour is dataset-dependent… running control comparisons on the target task」。论文明确「wiring prior is not a competitive inductive bias」「no claim of improved visual accuracy」。

## Likely stance and calibrated score

**Weak accept 上沿（逼近 lean accept；不到 accept）。校准总分 7.5 / 10，学术置信度 5 / 5。**

判定链（**独立重新判定**，逐条对证据，不照抄 R47 的 7.5，而是独立从证据推演恰好收敛到同一数值）：

1. **决定性缺口本轮丝毫未动，且被论文主动固化，构成不到 8 的更硬 tie-breaker。** 历史独立评审（7.0 版）把分数上限写成「中心机制外部效度为负 + 零视觉证据」，并给出可核验、明码标价的 Score-Change Conditions：①「单变量隔离的稀疏化消融 + dense 图 oracle 正对照 → +0.5（→ 7.5）」；②「真实视觉任务演示**且确认 motif 阈值迁移** → +0.5 到 +1（→ 8）」；③操纵外独立验证 + 强基线 → +0.5；④流程/披露修补 → 仅消除 low desk 风险、`+0.5` 上限，且明确「继续修流程/披露/格式不会再抬高总分」。R47 据 ① 真实兑现给 7.5，并因 ② 的「且确认迁移」未满足而不到 8。本轮 R49 四项修复**没有新增任何支持中心主张的科学实验**：§4.9/§4.10 这两组决定性实验在 R47 版已完成并计入评分，本轮只是补报其被隐藏的条件列与 delta。更关键的是，本轮论文**主动、明确地把「机制迁移未确认」写成定论**——§4.9「it does *not* establish motif survival as the causal variable」「We claim a density boundary, not a transferred motif-survival threshold」「the earlier five-setting result must not be read as one either」（`main.tex` lines 581–587）；§4.8 `hypothesis_supported=false` 与度保持 null 0.6162 保留（lines 546–552）；Conclusion「the threshold was not reproduced… measured predictor in one regime, not a universal cause」（lines 694–698）。条件 ② 的硬门槛「**且确认 motif 阈值迁移**」本轮被证明未走通，且论文自己放弃了这条路。按 `calibration-and-rank.md` Consistency Check 第 1 条（overall 必须匹配最强未解决弱点）与 `review-output-standards.md` Synthesis Rule（final stance 跟随最强未解决关切、不被平均掉），总分不应上移。

2. **本轮四项修复全部真实落地，属实质科学数据补报 + 诚实限定 + 可核验性闭合，不是格式润色——如实计入维度分与 desk 风险，但不抬总分。** 逐层核验（见 Checks run）：
   - §4.9 `tables_r46.tex` 现含四条件列（real / A=0 / deg-null / task-aware），六行 k 值数值与 `r39_density_sweep/metrics.json` 逐字段一致（`task_aware_null` k=4/2 = 0.9027 / 0.9971）；`make_r46_tables.py` lines 24–33 已从 pulled metrics 读取 `L1_degree_null` 与 `task_aware_null`（R47 C5 的根因「脚本主动丢弃两列」已修）；正文 lines 578–580 补报同步恢复，lines 583–590 写入 `23→63` 边丢失而 real 近 ceiling 的不利限定（该事实在 `metrics.json` 的 `motif_edges_survived` 中 k=8/4/2 为 `false`，可核验）。
   - §4.10 lines 612–616 补报 MNIST `+0.0148, CI [0.0100,0.0192]`（与 `r39_visual_task/metrics.json` `mnist_addon.real_minus_condition.degree_preserving_null` 精确一致）、写明「opposite in sign to the digits result」「report both rather than selecting one」「null behaviour is dataset-dependent」。
   - `results/r39_visual_task/r39_visual_task.py`（21,679 B）拉回；实算 SHA-256 = `28f5744d3e3d3376aea4458555e8801013bde607615435059fd246208c8097b7`，与 team-lead 期望值、`metrics.json environment.script_sha256`、§5 第四 SHA 精确匹配；四个执行脚本（dense `090d9535…`、sparse `026bf88e…`、sweep `360a3808…`、visual `28f5744d…`）SHA **全部实算精确匹配**（R47 C7「visual 脚本不可实算」闭合）；R37 门禁异议由含糊措辞改为写明两方具体分歧（lines 655–659，与 `goal-ledger.md` R37 分歧②一致）。
   - 压缩后 9 页，pypdf 逐页确认主文含完整 Conclusion 在 p8 收尾、p9 仅 LLM Usage Statement + References，`main.log` 0 Overfull / 0 Underfull / 0 undefined / 0 LaTeX Warning / 0 Citation undefined。

3. **净影响如实评估：正，且落在透明度/完整性/内部一致性/可核验性/诚实度，不落在中心主张的证据强度。** 对 **Evidence**：补报四条件与 MNIST delta 消除 R47 C5 两处呈现选择性，证据包的**完整性与无 cherry-pick** 提升，达到 3 上沿；但补报的 `task_aware_null` 同步恢复 + `23→63` 丢失仍近 ceiling + MNIST delta 反向，恰恰**再证**「中心机制只在合成替身成立、真实数据不迁移」，R47 的 Evidence 三条扣分事实（真实图阈值未复现、8/12 编码操纵 + sign=0.60、强基线未重跑）**全部未变**。对 **Soundness**：§4.9 与 Conclusion 的诚实限定让内外一致更严谨，并**消除** R47 的一条 Lower 触发条件（「证实 §4.9 task_aware_null 同步恢复与 §4.8 度保持 null 保留优势构成**未解释**内部矛盾 → −0.5」）——本轮矛盾已被主动解释（密度边界 vs motif 生存、跨设置 / 跨运行 ID 差异），是「已解释」而非「未解释」，故不下调、也不额外加分。对 **Ethics**：补报被隐藏数据 + 主动写削弱自身主张的限定 + R37 两方具体分歧 + 拉回脚本，闭合 R47 三项残留中的两项（含 R37 含糊、两处省略未讨论），仅余 LLM 工具类别一项低概率残余；达 clear strength，维度分 4→5。对 **Clarity / Reproducibility**：C5 闭合、visual SHA 闭合、四 SHA 可实算、版式合规，均达各维上沿，但边数口径、29,564 漏报、`[5]` 题录说明、18017 CRC、端到端哈希重跑未做仍在，故维持 4。

4. **维度分提升不平均掉总分。** `review-output-standards.md` 明确三者分离（criterion / overall / confidence）且「Synthesis must not average away fatal flaws; the final stance follows the strongest unresolved decision-relevant concern」。本轮 Ethics 4→5、其余维度维持且多注明上沿，但总分由最强未解决关切（中心机制外部效度为负 + 真实视觉任务为负 + 强基线未重跑）锁定，不因维度分改善而上移。R47 自身也是 Soundness 4 / Evidence 3 / Significance 3 却给 7.5，本就说明总分 ≠ 维度平均，本报告逻辑与之自洽。

5. **三条纪律逐条遵守**：不迎合 8.0 / 8.2 / 7.5 任何目标；不因论文主动写出对自己不利的限定（§4.9 23→63 丢失、Conclusion 降级、MNIST 反向 delta）而额外惩罚；不因其披露负结果（§4.10 诚实负结果、dense 全 chance、v2 `hypothesis_supported=false`）而默认加分。

6. **Never round：** 7.5 是独立推演值，不是 7.0 上取整、不是 8 下取整、不是照抄 R47。阻止到 8 的 tie-breaker 是「真实图机制迁移未确认（且本轮被主动固化为不主张）+ 真实视觉任务为负结果 + 中心机制仍主要在 96 节点受控图 + 诊断性 XOR 标签上确立」；阻止回落到 7.0 的 tie-breaker 是「§4.9 单变量隔离 + oracle 正对照（历史条件 ①）真实兑现且本轮未被推翻，另加四脚本 SHA 可实算、C5/ C7 呈现与可核验性闭合」。

### 本轮四项修复的独立净影响判定（逐条）

- **§4.9 四条件补报 + 削弱自身限定（决定性透明性修复，非机制迁移确认）**：净增 Evidence 完整性与 Soundness 内外一致性、闭合 R47 C5(a)。但补报的 `task_aware_null` 同步恢复与 `23→63` 丢失仍近 ceiling 一并给出后，论文的结论不是「机制迁移被确认」，而是「solvable regime 不能唯一归因于保护边集、claim a density boundary」。这不闭合「真实图 motif-survival 阈值未复现」。
- **§4.10 MNIST delta 补报（决定性透明性修复，强化负结论）**：净增 Clarity / Ethics，闭合 R47 C5(b)。但 `+0.0148, CI[0.0100,0.0192]` 与 digits 方向相反，论文据此写「null behavior is dataset-dependent」，**再证**控制协议依赖目标任务、中心机制不迁移。不默认加分。
- **visual 脚本拉回 + 四 SHA 实算 + R37 两方分歧（可核验性 / 披露闭合）**：净增 Reproducibility / Ethics，闭合 R47 C7 与 Ethics 残留 (i)。属条件 ④ 类（消除 low desk 风险），不抬总分。
- **9 页 p8 收尾 + 编译零警告（版式合规闭合）**：消除 low desk 风险，不影响总分。

## Scorecard（七维）

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis（可核验引用） | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 4 | 4 | §1 贡献列表（`main.tex` lines 109–125）；§5「Relation to the strongest published control ladder」（lines 621–632，「begins at their strict endpoint」）；§3.4 Eq.(1)（lines 252–291）、§4.7 task-aware 闭环（lines 455–497）；arXiv:2604.04033 [6] 本身已提出 staged control ladder（历史联网核实） | 扣分：delta 为「更高阶 rung + 全收敛 + 校正统计 + 构造性 task-aware 检验 + 生存计数」，各 rung 组件均为标准工具（`maslov2002`/`milo2002`/`wasserman1994`），属增量而非新框架；本轮 §4.9/§4.10 补报是透明性修订、§4.9 隔离为验证与边界刻画，**不增加新颖性**。封顶 4。升至 5 需把该标准真正应用到一篇已发表 connectome-constrained 视觉模型或真实视觉任务并确认机制迁移 |
| Soundness | 4 | 5 | §4.9（lines 562–590）：`density_isolated=true`、oracle 6 seeds 1.0000、只变 k、`r44_density_sweep.py` SHA 实算 `360a3808…` 匹配；§3.4 lines 274–281 上界直觉限定；§4.7 剂量阶梯；§4.8 lines 528–560 五变量如实；**本轮** lines 583–590 主动写 `23→63` 丢失与「density boundary, not a transferred motif-survival threshold」、Conclusion lines 694–698 降级 → 内外一致 | 维持 4（上沿）。本轮诚实限定消除了 R47 的一条 Lower 条件（§4.9 同步恢复 vs §4.8 度保持 null 保留优势由「未解释矛盾」变「已解释」），不额外惩罚也不额外加分。剩余缺口：(i) 3-seed 预检 `FAILED`（lines 327–339）、(ii) 18017 CRC / 末块崩溃保留（lines 659–661）、(iii) §4.8 与 §4.9 度保持 null 行为差异未逐变量对账。按历史条件「升至 5 需单变量隔离 + 正对照 + **一条哈希可核验的端到端主实验重跑**」，前两项已做、第三项未做，维持 4 |
| Evidence | 3 | 5 | `tables_r39.tex` Table real（sparse 0.6423 / 度保持 0.6162 CI 含 0 / `hypothesis_supported=false` 见 lines 546–552）；Table heldout（8/12、sign 0.60=0.60）；`r39_density_sweep/metrics.json`（本轮四条件、monotone k、oracle、`motif_edges_survived` k=8/4/2 `23->63:false`）；`r39_visual_task/metrics.json`（real 0.7185 / null 0.7190 / MLP 0.9722 / MNIST `+0.0148`）；§5 lines 649–651 | **≤3 具体扣分**：(i) 中心 motif-survival 阈值在真实图上**未复现**——§4.8 `hypothesis_supported=false`、度保持 null 保留优势 0.6162；§4.9 隔离的是密度 k 而非 motif 生存计数，且本轮自述 k=4/2 时 `23→63` 丢失而 real 仍 0.9863/0.9987「not uniquely attributable to that protected edge set」；(ii) 8 个显著特征部分编码 10 intact / 10 degraded 操纵，`sign_agreement=0.60 = majority_baseline=0.60`（`r39_heldout/metrics.json`）；(iii) flyvis / toposens2026 强基线未重跑（`experiment-traceability.md` row 17「not executed」）。**修复条件**：在操纵之外的独立图族验证 12 特征预测力，并给出至少一个**确认机制迁移**的真实数据结果 → 4。注：本轮四条件/MNIST delta 补报使证据包**完整性与透明度**明显提升、消除 C5 呈现选择性、达到 3 上沿，但未改变上述三条事实，且补报内容再证机制不迁移 |
| Significance | 3 | 5 | §4.10 lines 592–616 + `tables_r46.tex` Table visual：真实 digits 10 类 + MNIST add-on，real 0.7185 / A0 0.6190 / null 0.7190 / 非图 MLP 0.9722；§5 line 667「this is not a vision benchmark result」；Conclusion lines 694–698 降级；CFP 含「Data synthesis…」「AI for Science…」 | **≤3 具体扣分**：旧扣分「全篇无图像/视觉任务」被 §4.10 部分化解（现有真实视觉任务），但结果为**负**——wiring prior 非竞争偏置、度保持 null=real、非图 MLP 大幅主导；本轮补报的 MNIST `+0.0148` 与 digits 方向相反，论文据此写「null behaviour is dataset-dependent」，**再证**中心机制不迁移、对 CVPR 的价值仍是「评估方法学诊断 + 负面边界刻画」，核心贡献仍是对 96 节点受控替身的协议诊断。**修复条件**：在一个真实视觉任务或已发表 connectome-constrained 视觉管线上演示该标准**并确认 motif 阈值迁移** → 4。给 3（上沿），不因补实验 / 披露负结果默认加到 4 |
| Clarity | 4 | 5 | 六节结构；8 张表全部由 `\input` 文件自动生成（lines 59–62）；数字可回溯；`main.log` 0 Overfull / 0 undefined / 0 Warning；**本轮** `tables_r46.tex` 四条件、§4.9 lines 578–580、§4.10 lines 612–616、R37 lines 655–659、Conclusion 重写 | 维持 4（上沿）。本轮闭合 R47 C5 两处呈现选择性（§4.9 省 `task_aware_null`/`L1_degree_null`、§4.10 省 MNIST delta），R37 具体分歧入稿，版式 9 页合规。剩余扣分：摘要单段塞 6 组结果（lines 26–56）；§4.8 正文 line 506 用 48,713 而 line 530 与 `tables_r39.tex` Table real caption 用 48,723（**仍未统一**）；Limitations line 664 只写「9,766 vs 29,442」漏 `graph_stats.json` 的 29,564；Table 1/4/6/8 用 `\resizebox` 偏小；题录内嵌「Verified by public search」不符体例。升至 5 需拆摘要、统一边数 / ID 口径、补 29,564、表格改 `\footnotesize` |
| Reproducibility | 4 | 5 | **本轮实算四脚本 SHA-256 全部精确匹配**：dense `090d9535ac49…`、sparse `026bf88e11d3…`、sweep `360a3808bb4a…`、visual `28f5744d3e3d…`（与各自 `metrics.json environment.script_sha256` 及 §5 lines 674–676 逐字节一致）；`r39_visual_task/r39_visual_task.py` 21,679 B 拉回；7 组 `metrics.json` 中两组决定性实验 `run_complete=true`；`make_r46_tables.py` 从 pulled metrics 自动生成；`main.bib` 16 = `main.bbl` 16、`grep -ciE '\url\|http'`=0 | 维持 4（上沿）。本轮闭合 R47 C7「visual 脚本不可实算」并补第四 SHA。剩余扣分：无哈希可核验的端到端主实验重跑；18017 执行脚本 CRC 不符保留；边数口径 48,713/48,723 未统一；Limitations 漏 29,564；`[5] flyhack`「numeric identifier taken from project record」保留（`main.bib` line 45）。升至 5 需端到端哈希重跑 + 统一口径 + 清理题录说明 |
| Ethics / Limitations | 5 | 5 | **本轮自 4 上调**：§4.9 lines 581–590 主动写对自己不利的限定（`23→63` 丢失仍近 ceiling、「density boundary, not a transferred motif-survival threshold」）；§4.10 lines 606–616 主动写负结果 + MNIST 反向 delta +「report both rather than selecting one」；Conclusion lines 694–698「measured predictor in one regime, not a universal cause」；§5 lines 654–667 保留 FAILED 门禁、R37 **两方具体分歧**、崩溃运行、CRC 缺陷、负图像任务、口径不可混用；补报被隐藏数据闭合 R47 C5；LLM Statement lines 703–713；§5 Ethics lines 680–686（CC-BY 4.0、无人类被试 / 动物 / 部署系统） | 上调依据：R47 给 4 的三项残留中，(i) R37 含糊措辞 → 已写明两方具体分歧、(iii) 两处省略未在正文讨论 → 已补报并讨论，均已闭合；另新增三项超出 R47 清单的诚实行为（主动不利限定、Conclusion 降级、MNIST 反向 delta 如实补报）。达 clear strength。剩余低概率残余：(ii) LLM Statement 点名工具**类别**而非具体 name the tool(s)（双盲下可接受）；边数口径 / 29,564 / `[5]` 说明属 Clarity / Reproducibility 残留。若严格审稿人认为「补报本就公开留存的数据仅属纠正呈现、非新增伦理实践」，可维持 4 上沿——已给出争议空间 |

**Overall:** 7.5  | **Scholarly Confidence:** 5

**Recommendation:** weak-accept（上沿，逼近 lean accept；一个严格 fit 视角仍可判 borderline 7，距 accept 8 差一个「真实图机制迁移确认」）。本轮修复使呈现完整性与可核验性明显优于 R47 版，但 stance 不变。
**Verdict:** 分数上限仍由「中心机制外部效度为负 + 真实视觉任务为负结果」决定；本轮四项修复（补报被隐藏数据、加入削弱自身主张的诚实限定、闭合脚本可核验性、版式压缩）属实质正向修订，如实计入维度分（Ethics 4→5）与 desk 风险消除，但**不新增支持中心主张的科学证据**，且论文主动把「motif 阈值迁移未确认」固化为定论，故不抬总分、不达 8。上调到 8 需：在稀疏、cell-type-resolved、任务可解的真实子图上**确认 motif-survival 阈值迁移**（翻转 `hypothesis_supported=false`），或在一个已发表 connectome-constrained 视觉管线上演示该标准并确认机制迁移。下调触发：独立复核证明 §4.9 数值无法从 `r44_density_sweep.py` 复现、或 `density_isolated` 因标签泄漏而无效（−1 或 fatal）；或证实 18017 修复改变任一报告数字（−0.5）；或补报的四条件 / MNIST delta 被证明与 pulled metrics 不符（−0.5 到 −1，本轮已实算排除）。置信度 5：全文、四表、PDF 逐页、编译日志、7 组 metrics 逐字段、四脚本 SHA 实算、R46 audit / traceability / R37 ledger、历史评审链均可得；本次未重新联网，官方规则与前作题录沿用 R47 同日核实并已标注，不改变整体判定置信度。

## Top strengths

1. **闭合的因果环（受控图）**：Eq.(1) 预测未受保护 motif 边在混合下被销毁 → §4.7 剂量阶梯实测 18/14/9/4/0 → 0.8371/0.8316/0.4988/0.5104/0.5117 的离散阈值 → task-aware null 在全重连背景下恢复优势（0.8346 vs 0.8371，Δ=0.0025，q=0.40），并给出「保留 14/18 边的 background-only null 仍有优势（0.8260）」的直接证据。逐数与 `tables_taskaware.tex`、`p3_p4_taskaware/metrics.json` 一致。
2. **§4.9 预注册单变量密度隔离 + oracle 正对照（历史点名决定性实验的真实兑现）**：`density_isolated=true`、oracle 6 seeds 1.0000 排除标签问题、只变 k、`r44_density_sweep.py` SHA 实算匹配、`run.log` 尾 `run complete`、1.05 GB 权重表 Arrow 流式仅投影端点列未 densify。本轮进一步把四条件全部呈现，消除了 R47 抓出的「脚本主动丢弃 `task_aware_null` 同步恢复」这一最相关列的呈现选择性。
3. **本轮主动写入削弱自身主张的科学诚实**：§4.9 明写 k=4/2 时保护边 `23→63` 丢失而 real 仍近 ceiling「solvable regime is not uniquely attributable to that protected edge set」，据此把结论限定为「density boundary, not a transferred motif-survival threshold」；Conclusion 降级为「measured predictor in one regime, not a universal cause」；§4.10 主动补报与自身「gain already explained by degree-preserving control」措辞张力、方向相反的 MNIST 显著 delta 并写「report both rather than selecting one」。这类主动呈递不利证据的纪律在投稿稿中罕见，按团队指令不额外惩罚、按证据如实计入 Ethics。
4. **异常完整的负结果与失败披露**：§4.8 dense 全 chance 定性为「前提失效的边界条件」、sparse `hypothesis_supported=false` 且度保持 null 保留优势、明言「no replication claim」「Five settings changed together… cannot isolate density」；§4.10「wiring prior is not a competitive inductive bias」「no claim of improved visual accuracy」；FAILED 门禁、R37 两方门禁异议、崩溃运行、CRC 缺陷、跨运行 visual-ID 不可混用、所有负结果全部保留。
5. **可核验性与题录 / 格式合规**：四个执行脚本 SHA-256 全部本地实算与 `environment.script_sha256`、§5 声明逐字节一致；两组决定性实验 `run_complete=true`；三张数据表由脚本从 pulled metrics 自动生成；`main.bib` 16 = `main.bbl` 16、无外链；9 页正文 p8 收尾、p9 仅 LLM Statement + References、编译零警告；§5 对最接近前作 [6] 定位诚实（「We did not rerun their flyvis stack」）。

## 已闭合的关切（不再扣分）

| 旧关切（R47 / 历史 7.0 报告） | 本版闭合证据 |
|---|---|
| **R47 C5(a)**：`make_r46_tables.py` 只输出 real / A=0，主动丢弃 `L1_degree_null` 与 `task_aware_null`（后者 k=4 0.9027 / k=2 0.9971 与 real 同步恢复，是受控图 task-aware 结论在真实图上的唯一呼应） | `tables_r46.tex` 现含四条件列与六行 k 值；`make_r46_tables.py` lines 24–33 从 pulled metrics 读 `L1_degree_null` / `task_aware_null`；§4.9 lines 578–580 正文补报「task-aware null recovers in parallel (0.9027/0.9971 at k=4/2), the only echo on real wiring…」。数值实算一致 |
| **R47 C5(b)**：§4.10 省略 MNIST `real − degree_preserving_null = +0.0148, CI[0.0100,0.0192]` 显著为正、与 digits 方向相反、与正文措辞张力 | §4.10 lines 612–616 完整补报并写「opposite in sign to the digits result」「report both rather than selecting one」「null behaviour is dataset-dependent」。与 `r39_visual_task/metrics.json` 精确一致 |
| **R47 C7**：`results/r39_visual_task/` 无 `.py` 脚本，`28f5744d…` 不可独立实算 | `r39_visual_task.py` 21,679 B 拉回；实算 SHA-256 = `28f5744d3e3d3376aea4458555e8801013bde607615435059fd246208c8097b7` = `environment.script_sha256` = §5 第四 SHA；四脚本 SHA 全部实算匹配；§5 lines 674–676「all four executed scripts were pulled and their hashes verified」 |
| **R47 Ethics 残留 (i)**：R37 门禁异议仅以「a recorded concurrent gate-dissent」含糊入稿 | §5 lines 655–659 写明两方具体分歧「one required a clean rerun before P2 could pass; the other accepted the ten-seed matrix and later hash-verifiable runs」，并注明「retained in `goal-ledger.md` R37 and scored as a risk」；与 ledger R37 分歧②一致 |
| **R47 版式张力**：补报后 Conclusion 一度挤到 p9 | 压缩 §4.2 / §5 / Conclusion / Ethics 后 9 页；pypdf 逐页确认主文含完整 Conclusion 在 p8 line 632 收尾、p9 仅 LLM Statement（633–646）+ References（647 起 [1]–[16]）；`main.log` 0 Overfull / 0 undefined |
| **历史 Lower 触发条件**：「证实 §4.9 `task_aware_null` 同步恢复与 §4.8 度保持 null 保留优势构成**未解释**内部矛盾 → −0.5」 | 本轮主动解释：§4.9「density boundary, not a transferred motif-survival threshold」、§4.9 lines 587–590 与 §5 lines 663–666 跨运行 visual-ID 口径说明、§4.8「Five settings changed together」；矛盾由「未解释」变「已解释」，下调条件不触发（亦不额外加分） |
| 单变量隔离消融缺失 + dense 无 oracle 正对照（历史条件 ① / 旧 C5） | §4.9 `density_isolated=true`、oracle 6 seeds 1.0000、只变 k、脚本 SHA 实算匹配、`run_complete=true` |
| §4.8「3 变量 / 其余不变」与 pulled config 不符（旧 C7） | lines 533–539 如实改为「Five settings changed together」并逐项列出，声明「cannot isolate density as the cause」 |
| §4.6 预测主张过度、未承认操纵编码（旧 C3） | lines 446–453 降格为 *corrected association*，明言显著特征「partly encode that manipulation itself」 |
| Conclusion 无限定因果外推（旧 M3） | lines 694–698「the threshold was not reproduced… measured predictor in one regime, not a universal cause」 |
| 「零视觉证据」（旧 Significance 硬扣分） | §4.10 真实 `sklearn` digits + MNIST add-on（部分化解；结论为负，见 Significance 扣分） |
| BH 悬空引用 / LLM Statement 点名工具 / 3 条编造题录 / 外链（旧 desk 风险） | `main.bib` 16 = `main.bbl` 16；`\cite{benjamini1995}` 出现于 lines 34/102/304；PDF p9 题录带核实说明；`grep -ciE '\url\|http' main.bib`=0 |
| 历史已闭合项（v2 provenance、blanket 复现声明、两张手写表、Eq.(1) 限定、摘要 20 图矛盾、双盲） | 沿用历史独立报告结论，本版未恶化 |

## Major/fatal concerns

**Fatal concerns：无。** 未发现可独立支撑拒稿的新颖性坍塌、中心主张完全无证据、评测整体失效或格式 / 伦理硬违规。

| # | Severity | Concern | Evidence basis | Fix class | Owner | Score-change condition |
|---|---|---|---|---|---|---|
| C1 | Major | 中心机制（motif 生存为控制协议中的判别因果变量）仍只在 96 节点合成受控图 + 诊断性 XOR 标签上确立；真实 MaleCNS 子图上阈值未复现。§4.9 隔离的是密度 k 而非 motif 生存计数，且 k=4/2 时 `23→63` 保护边丢失而 real 仍 0.9863/0.9987（本轮论文自述「not uniquely attributable to that protected edge set」）。论文已如实披露、明确不主张迁移，故非内部一致性缺陷，但仍是限制贡献外推的实质缺口 | §4.8 lines 546–561、Table real、`hypothesis_supported=false`；§4.9 lines 575–590、`r39_density_sweep/metrics.json motif_edges_survived`；Conclusion lines 694–698 | experiment / scope | `ccf-experiment-designer` | 在稀疏、路径可辨识的真实子图上确认 motif-生存阈值（翻转 `hypothesis_supported=false`）→ Evidence / Significance +0.5 至 +1（→ 8） |
| C2 | Major | 真实视觉任务为**负结果**且未确认机制迁移：非图 MLP 0.9722 大幅主导、度保持 null = real；本轮补报的 MNIST `+0.0148` 与 digits 方向相反，论文据此写「dataset-dependent」，反而再证不迁移。对 CVPR 的价值仍是方法学 / 负面边界而非正面贡献 | §4.10 lines 592–616、Table visual、`r39_visual_task/metrics.json`、§5 line 667 | experiment / positioning | `ccf-experiment-designer` / `ccf-paper-writer` | 真实视觉任务 / 已发表视觉管线演示**且确认 motif 阈值迁移** → Significance / Evidence +0.5 到 +1（→ 8） |
| C3 | Moderate | 最强已发表基线未重跑（flyvis `lappalainen2024`、toposens2026 共享初始化管线）；signed/typed 边未建模；L1 只实现度保持思想 | §5 lines 649–651、line 629「We did not rerun their flyvis stack」、`experiment-traceability.md` row 17「not executed」 | experiment | `ccf-experiment-designer` | 重跑并加入 task-aware 控制 → Evidence / Novelty +0.5（投稿前难） |
| C4 | Moderate | 20 图「8/12 显著」部分由 10 intact / 10 degraded 操纵编码驱动；`sign_agreement=0.60 = majority 0.60` 符号零技能。§4.6 已降格为 corrected association 并承认，但摘要 line 51 与贡献列表 lines 120–124 仍把「8 显著 / 36%」写作正面结论 | `r39_heldout/metrics.json`、`tables_r39.tex` Table heldout、§4.6 lines 436–453 | experiment / writing | `ccf-experiment-designer` | 操纵外独立图族验证，或把摘要 / 贡献列表同步降格 → Evidence +0.5 |
| C5 | Moderate | 旧流程缺陷如实保留但未消除：3-seed 预检 `FAILED`、18017 执行脚本 CRC 不符、末块崩溃后 LOGO 由持久化行本地重算；无哈希可核验的端到端主实验重跑；R37 门禁异议虽写明两方分歧，但「结构敏感前提曾否通过」的最终裁定仍未给出 | §4.2 lines 327–339、§5 lines 654–661、`goal-ledger.md` R37、traceability | reproducibility / disclosure | `f-research-v1` | 一条哈希可核验端到端主实验重跑 + 明确 R37 异议的最终裁定 → Soundness / Reproducibility / Ethics +0.5 |
| C6 | Minor | 口径 / 题录 / 排版残留：边数 48,713（§4.8 正文 line 506）vs 48,723（line 530 + `tables_r39.tex` caption）未统一；Limitations line 664 只写 9,766 vs 29,442 漏 `graph_stats.json` 的 29,564；`[5] flyhack`「numeric identifier taken from project record」保留；题录内嵌「Verified by public search」不符体例；Table 1/4/6/8 用 `\resizebox` 偏小；摘要单段 6 组结果 | `main.tex` line 506/530/664、`tables_r39.tex`、`main.bib` line 45、`tables*.tex`、摘要 lines 26–56 | writing / reproducibility | `ccf-paper-writer` / `f-research-v1` | 统一边数 / ID 口径、补 29,564、清理题录说明、拆摘要、表格改 `\footnotesize` → Clarity / Reproducibility +0.5 |
| C7 | Minor | LLM Usage Statement 点名工具**类别**（agentic coding assistant / LLM-based search assistant / general-purpose LLM agent）而非具体 name the tool(s)（官方要求）；双盲下可接受，留低概率 desk / ethics 残余 | `main.tex` lines 703–713、R47 联网核实的官方条款 | ethics / writing | `ccf-paper-writer` | 明确工具描述 → 消除 low desk 残余 |

### Claim–Evidence Audit（主要主张）

| Claim | Where stated | Evidence provided | Strength | Reviewer deduction | Required fix |
|---|---|---|---|---|---|
| 受控图上结构优势真实且可复现 | 摘要、§4.4、Conclusion | Table 1：10 seeds，Δ=0.30–0.34，CI 排除 0，q=0.0002；A=0 / clean_motif / shuffled 对照 | strong | 无 | 无 |
| 匹配全局高阶统计无法定位优势 | §1、§4.4–4.5 | rung 间 Δ 仅 0.0244；单调性 1 次反转；L1 已匹配 conv2 统计却仍 chance | adequate | 结论仅在受控图成立，稿件已 scope | 无（已 scope） |
| motif 生存（非 rung 顺序）是因果变量 | §1 贡献 2、§4.7、Conclusion | Eq.(1) + 剂量阶梯 + task-aware null（受控图） | adequate（受控图）/ weak（真实图，本轮进一步降为「明确不主张」） | 真实图 `hypothesis_supported=false`；§4.9 隔离密度 k，k=4/2 `23→63` 丢失 real 仍高；稿件已写「measured predictor in one regime, not a universal cause」 | 真实图确认实验；否则维持 scope（本轮已做到后者） |
| 单变量密度隔离成立、dense 失败是传播稀释 | 摘要 lines 52–53、§4.9、`density_isolated=true` | 四条件表格 + 正文、oracle 6 seeds 1.0000、只变 k、脚本 SHA 实算匹配 | strong | 本轮已补报 `task_aware_null` 同步恢复一列并主动声明「not uniquely attributable to protected edge set」「density boundary, not a transferred motif-survival threshold」，读者误读风险已消除 | 无（R47 的 required fix 已闭合） |
| 幅度可预测、符号不可预测（corrected association） | 摘要、§4.6、Table heldout | 20 图、8/12 BH 显著、MAE 0.1046 vs 0.1635、sign 0.60=0.60 | weak | 显著特征部分编码操纵、符号零技能；§4.6 已诚实降格，但摘要 / 贡献列表仍作正面表述 | 摘要与贡献列表同步降格；补操纵外验证 |
| 真实视觉任务上 wiring prior 不是竞争偏置 | 摘要 lines 53–54、§4.10、Conclusion | Table visual：real 0.7185 / null 0.7190 / A0 0.6190 / MLP 0.9722；MNIST 0.8879 vs 0.7649；**本轮补报** `+0.0148, CI[0.0100,0.0192]` 反向 delta | adequate（digits）/ adequate（MNIST 本轮补报并讨论） | 本轮已补报 MNIST 四条件并写明「dataset-dependent」「report both rather than selecting one」，张力已消除；补报内容再证机制不迁移 | 无（R47 的 required fix 已闭合） |
| 真实 MaleCNS 结果界定协议边界、支持「在目标图上测 gate」 | §4.8 lines 553–560、摘要、Conclusion | dense 全 chance；sparse real 0.6423 但度保持 null 保留效应、`hypothesis_supported=false` | adequate（宽泛方法学建议）/ absent（中心机制） | 是「不迁移边界」而非外部效度验证 | 明确区分两类主张（已做到） |
| 所有表格由 pulled metric 文件脚本生成 + 四个脚本 SHA 已核验 | §5 lines 667–678 | Tables 1–8 + 4 图；四个 SHA；`make_r46_tables.py` 现读四条件；visual 脚本拉回 | strong | 本轮 C5（脚本只选部分条件）与 C7（visual 脚本不可实算）均已闭合；四 SHA 本地实算匹配 | 无 |
| 全部参考文献已核实、无虚构题录 | PDF p9、`main.bib` | 16 条编译 = 16 条 bib；多条带核实说明；`[5]` 注明编号取自 project record | adequate | BH 悬空已闭合；`[5]` 编号来源未独立公开核实已披露 | 清理 `[5]` 等题录内验证说明 |

## Writing concerns

- **摘要超载**：`lines 26–56` 单段塞入「主矩阵 + 阶梯失败 + 构造性检验 + 20 图 + 密度隔离 + 真实视觉任务」六组结果；建议拆成「裁决结果」与「机制 / 边界」两句群。
- **呈现准确性（本轮已实质改善，剩余为口径残留）**：§4.9 Table density 与 §4.10 正文的两处呈现选择性已闭合（见已闭合表）。剩余为 48,713 / 48,723 边数口径不一致、Limitations 漏 29,564、题录内嵌元信息，属 minor 而非「隐藏科学数据」。
- **口径不一致（残留）**：§4.8 正文 line 506 用 48,713 边，line 530 与 `tables_r39.tex` Table real caption 用 48,723；R46 audit lines 90–93 已给出四 run 完整口径表（9,766 / 9,766 / 29,442 / 29,564），稿件应同步并补第三个数；Limitations line 664 只写两数。
- **披露冗长**：§4.2 与 §5 Limitations 完整性披露占篇幅大、信息密度低；建议压成「defect / status / affected number / disposition」小表（本轮已压缩过一轮，仍有空间）。
- **表格可读性**：Table 1/4/6/8 使用 `\resizebox`，双栏打印数值列偏小；建议 `\footnotesize` 或两栏拆分。
- **题录内验证说明**：多条参考文献条目内嵌「Verified by public search, 2026-11-08」「No external URL is included, per the CVPR 2027 author guidelines」等元信息，属诚实披露但不符合常规题录体例，建议移入附录 / 致谢说明。

## Format/venue concerns

- **页数（本次 pypdf 逐页核验当前 `main.pdf`，9 物理页）**：主文在**第 8 页收尾**——p8 line 632 为 Conclusion 末句「…explains conflicting reports.」；**第 9 页只含** LLM Usage Statement（lines 633–646，「Large language models were used…」至「The authors take full responsibility for the content.」）+ `References` 标题（line 647）+ `[1]`–`[16]` 共 16 条（lines 648–720）。逐页关键词检测 p9 中 `Conclusion` / `Discussion` / `Experiments` / `4.8` / `4.9` / `4.10` / `hypothesis_supported` / `density_isolated` 均无命中，**无任何正文残留**。按官方「Only references and the LLM Usage Statement may exceed this limit」「LLM Usage Statement… after the main text and before the references. It does not count toward the eight pages」，正文 = 8 页、p9 为不计数的 LLM Statement + 允许的 references → **合规**。与 R47 版差异：R47 版 LLM Statement 跨 p8/p9，本版因压缩后**全在 p9**、Conclusion 完整在 p8 收尾，两者均合规；本版与团队指令「主文（含完整 Conclusion）在 p8 收尾，p9 仅 LLM Usage Statement + References」精确一致。
- **双盲**：`\author{Anonymous}`（line 18）、无致谢、LLM Statement 无身份信息、`grep -ciE '\url\|http' main.bib` = 0 → pass。
- **LLM Usage Statement**：存在、位置正确（Conclusion 后、references 前）、强制要求满足；点名工具**类别**并说明环节与程度（lines 703–713）。官方要求 name the tool(s)，点「类别」在双盲下可接受但留低概率残余（见 C7 / Ethics）。
- **编译质量**：`main.log` LaTeX Warning=0 / Overfull=0 / Underfull=0 / undefined=0 / Citation undefined=0；`Output written on main.pdf (9 pages)`；`main.bib` 16 个 `@` = `main.bbl` 16 个 `\bibitem`；8 张表由 4 个 `\input` 文件提供、编号连续；`cvpr.sty` + `ieeenat_fullname.bst` + `10pt,twocolumn,letterpaper` 官方模板 → pass。
- **Prompt injection / 隐藏操纵**：通读 `main.tex`、4 张表、`main.bib`、LLM Statement、PDF 文本，未发现隐藏指令或白字操纵；LLM Statement 主动披露「to simulate an independent peer-review panel」，属公开声明 → pass。
- **Venue fit**：CFP 主题提供合法挂载点，但 CVPR 口味重视 visual evidence / recent baselines / cross-dataset tests；本版虽有真实视觉任务，结论为负、非图 MLP 主导、机制不迁移，fit 仍属**间接**，构成 Significance 扣分，非 desk rejection 理由。
- **Desk checks（逐条）**：

| Check | Status | Evidence | Consequence | Required action |
|---|---|---|---|---|
| Paper Length | pass | 9 物理页但正文 8 页、p8 完整 Conclusion 收尾、p9 仅 refs + LLM Statement；pypdf 逐页确认无正文残留 | 无 | 无 |
| Topic Compatibility | uncertain | 方法学诊断对视觉会议间接（§5「this is not a vision benchmark result」） | 影响 Significance，非 desk | benchmark/analysis-track 定位 |
| Minimum Quality | pass | 六节、核心方法、8 表 4 图、证据、局限、参考文献、可读性齐备 | 无 | 无 |
| Policy / Anonymity / Compliance | pass with residual | 双盲、`\author{Anonymous}`、无外链、LLM Statement 存在；点名工具类别而非具体工具 | 低概率 desk / ethics 残余 | 明确工具描述 |
| Prompt Injection / Hidden Manipulation | pass | 全文 / 表 / 题录 / LLM Statement / PDF 文本无隐藏指令 | 无 | 无 |
| Ethics and Reviewability | pass | 无人类被试、CC-BY 4.0、misuse 风险在 §5 讨论、负结果全保留、四 SHA 可实算 | 无 | 无 |

**Desk rejection risk: low**；Reason：无硬性格式 / 匿名 / 外链违规，LLM Statement 存在且位置正确；**Can be fixed before review? yes**（补工具描述、统一边数 / ID 口径、补 29,564、清理题录说明）。

## 7 人独立 reviewer panel

Reviewer: Best-Justified Reviewer
Expertise: evaluation methodology / graph learning，寻找最强可辩护接收理由
Likely score: 8 / lean-to-clear accept
Confidence: 5
Main positive signal: Eq.(1) → 剂量阶梯 → task-aware null 闭合因果环；10 配对种子 + BH + 常数 / 多数基线；§4.9 预注册单变量密度隔离 + oracle 6 seeds 1.0000 + 脚本 SHA 实算匹配 + `density_isolated=true`；本轮补报四条件（含 `task_aware_null` 同步恢复这一真实图唯一呼应）、主动写削弱自身主张的限定、四脚本 SHA 全部可实算，证据包完整性与诚实度达投稿稿罕见水平；§4.10 真实图像任务诚实报告负结果；§5 诚实对标前作 control ladder。
Main negative signal: 范围窄、中心机制未迁移、真实视觉任务结论为负。
Evidence basis: §3.4、§4.7、`r39_density_sweep/{metrics.json,run.log,r44_density_sweep.py}`、`r39_visual_task/metrics.json`、§4.9 / §4.10 / Conclusion、§5 对标段。
Fatal concern if any: 无。
Score-change condition: 一个确认机制迁移的真实数据结果 → 9。

Reviewer: Critical Reviewer
Expertise: 严格 CVPR 审稿人，寻找最强拒稿理由
Likely score: 6 / borderline
Confidence: 5
Main positive signal: 承认 §4.9 单变量隔离与 oracle 正对照是真实新增证据、内部逻辑自洽、统计未 cherry-pick；本轮两处呈现选择性与 visual 脚本可算性**已闭合**（故不再以 R47 的 C5/C7 扣分），披露异常坦诚，provenance 与 Conclusion 外推已闭合。
Main negative signal: 全部正向机制发现来自 96 节点合成 XOR 替身；§4.10 真实视觉任务为负（MLP 0.9722 主导、度保持 null=real、MNIST delta 反向且 dataset-dependent），再证机制不迁移；§4.8 `hypothesis_supported=false` 保留、度保持 null 保留优势 0.6162；§4.9 隔离的是密度 k 且 k=4/2 `23→63` motif 边丢失 real 仍高（本轮论文自己承认「not uniquely attributable to protected edge set」）；强基线未重跑；FAILED 预检与 18017 CRC 保留。本轮修复是「把已知数据报全 + 把主张降级」，不是新实验，中心机制外部效度反而被主动固化为负。
Evidence basis: §3.1、§4.8 / Table real、§4.9 / `metrics.json`、§4.10 / Table visual、§5 Limitations / Conclusion、R46 audit。
Fatal concern if any: 无硬致命；「中心机制不迁移 + 真实视觉任务负结果」组合接近 major threshold。
Score-change condition: 真实视觉任务上的机制迁移确认 → 7。

Reviewer: Method / Soundness Reviewer
Expertise: 因果推断 / 图 null 模型 / 统计有效性
Likely score: 7 / lean accept
Confidence: 5
Main positive signal: Eq.(1) 已限定上界直觉；§4.9 单变量隔离 + oracle 正对照把「dense 失败 = 传播稀释」从假设升级为实测 `density_isolated=true`；本轮 §4.9 / Conclusion 的诚实限定让内外一致更严谨，并解释了 §4.9 `task_aware_null` 同步恢复与 §4.8 度保持 null 保留优势的表面张力，消除了「未解释内部矛盾」的下调风险；四脚本 SHA 实算匹配。
Main negative signal: 预注册 3-seed 门禁仍 `FAILED`；§4.9 与 §4.8 对「度保持 null 是否保留优势」给出相反答案（不同图 / 不同设置），论文用「Five settings」「visual-ID 口径」解释但未做逐变量对账；k=4/2 `23→63` motif 边丢失而 real 仍高，削弱「特定两跳 motif 是关键」；无端到端哈希重跑。
Evidence basis: §3.4 line 276、§4.2、§4.8 lines 533–539、§4.9、`r39_density_sweep/metrics.json motif_edges_survived`、`run.log`。
Fatal concern if any: 无。
Score-change condition: 端到端哈希重跑 + 逐变量对账 §4.8 / §4.9 差异 → 8。

Reviewer: Evidence / Experiment Reviewer
Expertise: baselines / ablations / 统计功效 / 复现
Likely score: 7 / lean accept
Confidence: 5
Main positive signal: 10 seeds、配对 CI、全族 BH、2×2 鲁棒性网格、两个证伪消融、20 图 powered 研究、§4.9 单变量消融 + oracle、§4.10 五条件 6 seeds + CI、两组 `run_complete=true`、表自动生成；本轮补报四条件 / MNIST delta 消除 R47 的两处呈现选择性，证据包完整且无 cherry-pick。
Main negative signal: 8/12 显著特征部分编码操纵、sign=majority；真实数据 `hypothesis_supported=false`；强基线未重跑；18017 CRC 保留；补报的 `task_aware_null` 同步恢复 + `23→63` 丢失 + MNIST 反向 delta 一并看，**再证**中心机制不迁移，未增加支持中心主张的证据强度。
Evidence basis: Tables 1–8、`r39_heldout/metrics.json`、两组 `metrics.json` / `summary.txt` / `run.log`、`make_r46_tables.py`、`r39_visual_task/metrics.json`。
Fatal concern if any: 无。
Score-change condition: 操纵外验证 + 强基线重跑 + 一个确认机制迁移的真实结果 → 8。

Reviewer: Novelty / Positioning Reviewer
Expertise: 最接近前作与真实 delta
Likely score: 6 / borderline
Confidence: 4
Main positive signal: 前作 [6] limitations 把更高阶 null / 更长训练列为 future work，本文补足并新增 task-aware 构造性检验 + 生存计数框架；§5 定位诚实、明确未复跑 flyvis。
Main negative signal: 前作**本身已有 control ladder**，delta 为标准工具组合；本轮 §4.9 / §4.10 是透明性补报与边界刻画，不增新颖性；venue fit 方法学而非视觉，真实视觉任务为负。
Evidence basis: §5 lines 612–632、arXiv:2604.04033（历史联网核实）、`maslov2002` / `milo2002` / `wasserman1994`。
Fatal concern if any: 无（新颖性未坍塌，封顶 4/5）。
Score-change condition: 在已发表视觉模型上应用该标准并确认机制 → 8。

Reviewer: Writing / Clarity Reviewer
Expertise: 贡献可恢复性 / 图表可解释性
Likely score: 7 / lean accept
Confidence: 5
Main positive signal: 六节结构、数字可回溯到自动生成表、显式 scope conditions、Conclusion 与 §4.8 / §4.10 一致、编译零警告、本轮补报四条件 / MNIST delta / R37 两方分歧并重写 Conclusion，C5 两处呈现选择性已闭合、9 页 p8 收尾合规。
Main negative signal: 摘要塞 6 组结果；48,713 / 48,723 口径不一致；Limitations 漏 29,564；`\resizebox` 表格偏小；题录内嵌元信息。
Evidence basis: 摘要 lines 26–56、`tables_r46.tex`、`make_r46_tables.py`、§5 line 664、`main.log`、pypdf 逐页。
Fatal concern if any: 无。
Score-change condition: 拆摘要 + 统一口径 + 补 29,564 → 8。

Reviewer: Ethics / Reproducibility Reviewer
Expertise: 许可 / 透明性 / 失败披露 / artifact 审计
Likely score: 8 / lean-to-clear accept
Confidence: 5
Main positive signal: CC-BY 4.0、无人类被试；FAILED 门禁、崩溃运行、CRC 缺陷、dense 负结果、`hypothesis_supported=false`、§4.10 负结果全如实上报且不作复现 / 泛化声明；本轮补报被隐藏数据 + 主动写削弱自身主张的限定 + Conclusion 降级 + R37 两方具体分歧 + MNIST 反向 delta 如实补报，诚实度达 clear strength；四个脚本 SHA 本地实算全部精确匹配、visual 脚本拉回、表自动生成、BH 引用补齐、无外链、双盲。
Main negative signal: LLM Statement 点名工具类别而非具体工具；边数 / ID 口径残留、`[5]` 题录说明、`\resizebox`；跨运行 visual-ID 匹配不同（9,766 / 29,442 / 29,564）绝对边数不可混用。
Evidence basis: §5 Limitations / Ethics / Reproducibility、lines 655–676、lines 703–713、R46 audit、goal-ledger R37、四脚本 SHA 实算、目录清单。
Fatal concern if any: 无。
Score-change condition: 补具体工具名 + 统一口径 + 清理题录说明 → 9。

### Panel synthesis

Agreement: 七位一致认为受控图内部逻辑、统计卫生与数值可复算性成立；§4.9 是历史评审点名的决定性实验的真实、SHA 可核验兑现；本轮四项修复（四条件补报 + 削弱自身限定 + Conclusion 降级 + MNIST delta 补报 + visual 脚本 SHA + R37 两方分歧 + 9 页合规）全部真实落地，R47 的两处呈现选择性与可核验性缺口已闭合；诚实披露与主动降级主张属罕见优点；无致命缺陷。
Disagreement: Best-Justified(8) / Ethics(8) 与 Critical(6) / Novelty(6) 在「一个正向机制仍由合成替身支撑、真实视觉任务为负结果、且中心机制外部效度被主动固化为负的方法学诊断，是否够 CVPR 级贡献」上对立；Method(7) / Evidence(7) 强调 §4.9 隔离的是密度而非 motif 阈值、且 k=4/2 motif 边丢失 real 仍高，本轮补报内容再证不迁移。
Decisive positive axis: 闭合因果环（受控图）+ §4.9 预注册单变量隔离与 oracle 正对照（脚本 SHA 实算匹配）+ 四脚本可核验 + 本轮补报隐藏数据 / 主动不利限定 / 闭合可核验性的诚实纪律 + 严格 scope + 版式合规。
Decisive negative axis: 中心机制外部效度仍为负（`hypothesis_supported=false` 保留、§4.9 明确「不主张迁移」、Conclusion 降级）+ 真实视觉任务为负且未确认机制迁移 + 强基线未重跑 + FAILED 预检 / 18017 CRC 保留。
Unresolved evidence: §4.8 与 §4.9 度保持 null 行为差异的逐变量归因；R37 门禁异议是否影响「结构敏感前提曾否通过」的最终裁定；18017 修复是否改变任一报告数字；flyvis 栈未复跑。
AC stance: **weak-accept 上沿，7.5**。最终立场跟随「最强未解决关切」——中心机制外部效度为负且真实视觉任务结论为负——不被「诚实披露 / 单变量隔离 / 呈现完整性 / 四 SHA 可算 / 格式合规 / Ethics 维度分上调」平均掉；历史 ① 号条件真实兑现使分数不回落至 7.0，历史 ② 号的「确认 motif 阈值迁移」本轮被明确证明未走通，故不达 8。

## Concern-to-action

| Concern | Action | Owner | Affected criterion | Score-change condition |
|---|---|---|---|---|
| C1 机制未迁移 | 在稀疏、路径可辨识的真实子图上确认 motif-生存阈值（翻转 `hypothesis_supported=false`）；维持现有严格 scope（本轮已做到后者） | `ccf-experiment-designer` | Evidence, Significance | +0.5 至 +1（→ 8） |
| C2 真实视觉任务负结果 | benchmark/analysis-track 定位 + 至少一个**确认机制迁移**的真实视觉任务 / 已发表管线演示 | `ccf-experiment-designer` / `ccf-paper-writer` | Significance, Evidence | +0.5 到 +1（→ 8） |
| C3 强基线 | 重跑 flyvis / toposens2026 管线并加入 task-aware 控制 | `ccf-experiment-designer` | Evidence, Novelty | +0.5（投稿前难） |
| C4 预测贡献 | 操纵外独立图族重测 12 特征；摘要 / 贡献列表同步降格为探索性 | `ccf-experiment-designer` / `ccf-paper-writer` | Evidence | +0.5 |
| C5 流程缺陷 | 哈希可核验端到端主实验重跑；明确 R37 异议的最终裁定 | `f-research-v1` | Soundness, Reproducibility, Ethics | +0.5 |
| C6 口径 / 题录 / 排版 | 统一 48,713/48,723；Limitations 补 29,564；清理 `[5]` 题录说明；拆摘要；表格改 `\footnotesize` | `ccf-paper-writer` / `f-research-v1` | Clarity, Reproducibility | +0.5 上限 |
| C7 LLM 工具描述 | 明确 name the tool(s)（双盲下以类别 + 更具体环节描述折中） | `ccf-paper-writer` | Ethics | 消除 low desk 残余 |

## Score-Change Conditions

| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | 在稀疏、cell-type-resolved、任务可解的真实子图上**确认 motif-survival 阈值迁移**（翻转 `hypothesis_supported=false`），或在已发表 connectome-constrained 视觉管线上演示该标准并确认机制（历史条件 ② 的硬门槛） | Evidence, Significance, Novelty | +0.5 到 +1 overall（→ 8） |
| Raise score | 重跑 flyvis / toposens2026 强基线 + 操纵外独立图族验证 12 特征 + 一条哈希可核验端到端主实验重跑（历史条件 ③ + Soundness 升 5 条件） | Evidence, Novelty, Soundness, Reproducibility | +0.5 overall |
| Raise score | 本轮已兑现的「补报四条件 / MNIST delta + 完整 R37 两方分歧 + 拉回 visual 脚本 + 四 SHA + 9 页合规」；剩余「统一边数 / ID 口径、补 29,564、清理 `[5]` 题录说明、拆摘要」 | Clarity, Reproducibility, Ethics | 消除 low desk 风险；**维度分已如实计入（Ethics 4→5），总分不再抬高** |
| Lower score | 独立复核证明 §4.9 数值无法从 `r44_density_sweep.py` 复现，或 `density_isolated` 因标签泄漏而无效（本轮已 SHA 实算 + 逐字段对账排除） | Reproducibility, Soundness | −1 overall 或 fatal |
| Lower score | 证实本轮补报的四条件 / MNIST delta 与 pulled `metrics.json` 不符（本轮已实算精确一致，排除） | Evidence, Ethics | −0.5 到 −1 |
| Lower score | 确认 18017 修复改变任一报告数字，或 R37 异议意味着结构敏感门禁从未通过且未在稿件裁定 | Soundness, Reproducibility | −0.5 到 −1 overall |
| No quick change | 继续补流程 / 披露 / 格式（含本轮已做的补报、SHA、版式压缩，以及统一口径、清理题录、补工具名、拆摘要）不会再抬高总分；自然视觉任务上的正面外部效度与机制迁移确认需新实验纲领 | Significance, Evidence | 投稿前不大可能改变 |

## Checks run

1. 锁定并通读磁盘最新版 `main.tex`（721 行 / 40,897 B / md5 `9cdb5ea637e741ae7e9d56fcb607b7ce`）、`main.bib`、`main.bbl`、`main.log`、`main.aux`、四张 `tables*.tex`、`scripts/make_r46_tables.py`、`scripts/make_r39_tables.py`；确认 R49 四项修订的文本落点（lines 578–590 / 612–616 / 655–659 / 674–676 / 694–698 / 703–713）。
2. 逐字段读 7 组 `metrics.json`：`p3_p4/metrics_completed.json`（`main_matrix.mean_acc.real=0.815234375`、Δ=0.30–0.34、`bh_q=0.0002`）、`p3_p4_taskaware/metrics.json`（剂量 0.8371/0.8316/0.4988/0.5104/0.5117、task-aware 0.8346、`hypothesis_supported=True`）、`r39_heldout/metrics.json`（8/12、`sign_agreement=0.60 = majority_baseline=0.60`、MAE 0.1046 vs 0.1635）、`r39_real_connectome/metrics.json`（dense 全 chance、`hypothesis_supported=False`）、`r39_real_connectome_v2/metrics.json`（real 0.6423 / 度保持 0.6162 CI 含 0、`hypothesis_supported=False`）、`r39_density_sweep/metrics.json`（四条件五 k、oracle 6 seeds 1.0000、`density_isolated=True`、`motif_edges_survived` k=8/4/2 `23->63:false`）、`r39_visual_task/metrics.json`（digits 五条件 + CI、MNIST `real_minus_condition.degree_preserving_null.delta=0.01483, ci95=[0.0100,0.01917]`、`run_complete=True`）。
3. **四脚本 SHA-256 本地实算并与自报值 / §5 声明逐字节对照**：`r39_real_connectome/r39_real_connectome.py` = `090d9535ac49…`、`r39_real_connectome_v2/r39_real_connectome_v2.py` = `026bf88e11d3…`、`r39_density_sweep/r44_density_sweep.py` = `360a3808bb4a…`、`r39_visual_task/r39_visual_task.py` = `28f5744d3e3d…`；全部与各自 `metrics.json environment.script_sha256` 及 `main.tex` lines 674–676 精确一致。visual 脚本 21,679 B 与 team-lead 期望字节数一致。
4. 读 `audits/R46-correction-experiments-audit.md` 全文（四条件表、MNIST 五条件、cross-run 口径表 9,766 / 9,766 / 29,442 / 29,564）、`experiment-traceability.md`（row 17 强基线「not executed」、rows 26–29 决定性实验）、`goal-ledger.md` R37（分歧②两方立场），与稿件逐条对账；确认 §5 lines 655–659 的 R37 两方分歧与 ledger 一致。
5. **编译 / 题录检查**：`main.log` LaTeX Warning=0 / Overfull=0 / Underfull=0 / undefined=0 / Citation undefined=0，`Output written on main.pdf (9 pages)`；`main.bib` 16 个 `@` = `main.bbl` 16 个 `\bibitem`；`grep -ciE '\url\|http' main.bib`=0；LLM Statement 位于 Conclusion 后、references 前。
6. **PDF 逐页提取（pypdf 6.19.0，9 页）**：p8 以 Conclusion 末句「…explains the conflicting reports.」收尾（line 632）；p9 lines 633–646 为 LLM Usage Statement、line 647 `References`、lines 648–720 为 `[1]`–`[16]` 共 16 条；逐页关键词检测 p9 无 `Conclusion` / `Discussion` / `Experiments` / `4.8` / `4.9` / `4.10` / `hypothesis_supported` / `density_isolated` 命中，无正文残留。按官方「仅 references + LLM Usage Statement 可上额外页」判定合规。
7. **残留项精确 grep**：`48\{,\}713`（line 506）vs `48\{,\}723`（line 530 + `tables_r39.tex` caption）仍不一致；Limitations line 664 仅 `9\{,\}766 vs 29\{,\}442`、漏 29,564（`graph_stats.json n_visual_body_ids=29564`、R46 audit line 93）；`main.bib` line 45 `numeric identifier taken from project record` 保留；多条题录 `Verified by public search` 元信息保留；摘要单段六组结果；`\resizebox` 出现在 `tables.tex` / `tables_taskaware.tex` / `tables_r46.tex`。
8. 读历史四份评审（7.5 / 8.2 / 7.0 / 7.5）仅作扣分演化与 Score-Change Conditions 参考；逐条核验本版对历史 ①②③④ 号条件的实际兑现情况（① R47 已兑现且未被推翻、② 本轮被主动证明未走通、③ 未兑现、④ 本轮实质兑现并消除 low desk 风险但不抬总分）。本次未重新联网，官方规则与前作题录沿用 R47 同日独立核实。
9. **一致性自检**：7.5 与「最强未解决关切 = 中心机制外部效度为负 + 真实视觉任务负结果」匹配；两个 ≤3 维分（Evidence 3、Significance 3）均含可核验引用、具体扣分与修复条件；其余维分亦各带引用与条件；Ethics 4→5 有 R47 三项残留闭合两项 + 三项额外诚实行为的可核验依据；Ethics 5 与总分 7.5 的「维度分 / 总分分离、synthesis 不平均掉最强关切」逻辑已显式写出；无致命缺陷故不 reject；未迎合 8.0 / 8.2 / 7.5、未照抄历史分数；双向 tie-breaker 均明确写出。

## Unresolved

**A 类 — 已闭合（不再扣分）**：本轮四项修复（§4.9 四条件表格 + 正文补报 `task_aware_null` 同步恢复 + 主动写 `23→63` 丢失与「density boundary, not a transferred motif-survival threshold」限定 + Conclusion 降级；§4.10 MNIST `+0.0148` 与「dataset-dependent」补报；visual 脚本拉回 + 四脚本 SHA 实算匹配 + 第四 SHA + R37 两方具体分歧；9 页 p8 收尾 + 编译零警告）；R47 的 C5(a)(b) 两处呈现选择性、C7 可核验性、Ethics 残留 (i)(iii)；历史「未解释内部矛盾」Lower 触发条件（本轮已解释）；历史已闭合项（单变量隔离 + dense oracle 正对照、§4.8 五变量如实计数、§4.6 预测主张降级、BH 悬空引用、LLM Statement 点名工具类别、3 条题录换真实 + 无外链、Eq.(1) 限定、v2 provenance、blanket 复现声明、两张手写表、双盲、页数合规、「零视觉证据」硬扣分被 §4.10 部分化解但结论为负见 Significance）。

**B 类 — 仍未解决，属「缺少决定性实验 / 比较」**：
- **flyvis / arXiv:2604.04033 训练栈未复跑**（§5 已诚实声明；`experiment-traceability.md` row 17「not executed」；L1 只实现度保持思想）。
- **真实 MaleCNS motif-survival 阈值仍未复现**：§4.8 `hypothesis_supported=false`、度保持 null 保留优势 0.6162（CI 含 0）；§4.9 隔离的是密度 k 而非 motif 生存计数，且 k=4/2 时 `23→63` 边丢失 real 仍 0.9863/0.9987（本轮论文自述完整 motif 非必需）。论文明确不作 replication claim，且本轮进一步主动降级为「measured predictor in one regime, not a universal cause」。这不是「负结果被隐瞒」，而是中心机制外部效度的实质缺口。
- **真实视觉任务未确认机制迁移**：§4.10 负结果（MLP 0.9722 主导、度保持 null=real）再证不迁移；本轮补报的 MNIST 反向 delta 写「dataset-dependent」，进一步强化「必须在目标任务跑对照」但不改变负结论；历史条件 ② 的「且确认 motif 阈值迁移」未满足。
- **单变量隔离虽已补，但 §4.8 与 §4.9 对「度保持 null 是否保留优势」给出相反答案**（不同图 / 不同设置），论文用「Five settings / visual-ID 口径」解释，未做逐变量对账；sparse 0.6423 是否部分源于 sum 读出 / hidden 128 / lr 0.008 仍未逐项排除。
- **操纵外独立图族验证 12 特征预测力 + 强基线重跑 + 一条哈希可核验端到端主实验重跑**仍缺失。

**C 类 — 流程 / 披露残留**：3-seed 预检 `FAILED`、18017 执行脚本 CRC 不符、末块崩溃后 LOGO 本地重算全部保留（已披露）；R37 门禁异议已写明两方具体分歧，但「结构敏感前提曾否通过」的最终裁定未给出、仍「scored as a risk」；LLM Statement 点名工具**类别**而非具体 name the tool(s)（低概率 desk / ethics 残余）；边数口径 48,723（`tables_r39.tex` caption / line 530）/ 48,713（§4.8 正文 line 506）未统一；Limitations 口径只写 9,766 vs 29,442 漏 29,564；`[5] flyhack`「numeric identifier taken from project record」保留；多条题录内嵌「Verified by public search」元信息不符体例；`\resizebox` 表格偏小；摘要单段 6 组结果；真实子图跨运行 visual-ID 匹配不同（9,766 / 29,442 / 29,564），绝对边数不可混用（§4.9 lines 587–590 与 §5 lines 663–666 已披露，属正确限定但仍是可核验性约束）。

**D 类 — 版本漂移 / 历史口径**：本报告锁定当前版 md5 `9cdb5ea637e741ae7e9d56fcb607b7ce`（721 行 / 40,897 B）；R47 独立报告锁定 719 行 / 40,612 B / md5 `4afd89c155bb13af4153fe316f206f79`；r39 独立报告锁定 736 行 / md5 `cd17e1e6…`。三版差异：R47→R49 为四项实质修订（见版本锁定声明与 A 类），r39→R47 为 §4.9 / §4.10 新增与 §4.6 / §4.8 / Conclusion / LLM Statement / 题录修订。LLM Usage Statement 由历史版「全在 p9」→ R47 版「跨 p8/p9」→ 本版「全在 p9、Conclusion 完整在 p8 收尾」（三者均合规）；历史评审引用的「Table 7 claim-to-evidence 表」在 R47 / 本版已不存在（8 张表全为数据表）。历史 7.5 / 8.2 / 7.0 / 7.5 报告均为历史，不构成本次判定依据。本次未重新联网，官方规则与关键前作题录沿用 R47 同日独立核实。若之后再变，尤其 §4.9 / §4.10 / Conclusion / 四 SHA，请按锁定 md5 复核。

## Output self-check

- 节序遵循 full 契约与指定输出契约：Mode / Venue and assumptions / Paper summary / Likely stance and calibrated score（内嵌本轮四项修复的独立净影响判定）/ 七维 Scorecard / Top strengths / 已闭合关切表 / Major-fatal concerns（内嵌 Claim–Evidence Audit）/ Writing concerns / Format-venue concerns（内嵌 Desk checks 逐条）/ 7 人独立 reviewer panel（含 Best-Justified 与 Critical，附 Panel synthesis）/ Concern-to-action / Score-Change Conditions / Checks run / Unresolved（A/B/C/D 分类）/ Output self-check。✔
- 所有 Markdown 表分隔符有效、每行列数一致。✔
- 分数、置信度、Recommendation 内部一致：7.5 = weak-accept 上沿、Confidence 5、无致命缺陷；决定性缺口（真实图机制迁移未确认）本轮丝毫未动且被主动固化 → 不达 8；历史条件 ① 真实兑现且未被推翻 → 不回落 7.0；本轮修复如实计入维度分（Ethics 4→5）与 desk 风险消除，但按 synthesis rule「不平均掉最强关切」不抬总分。✔
- 机器可读结论行**有且仅有一行**，采用严格格式（Overall + Scholarly Confidence 两项、整数置信度）；另给 Recommendation 与 Verdict；全文其余处未重复该精确格式。✔
- 严守 Never round scores：7.5 未取整到 8、未因 8.0/8.2 目标抬分、未照抄 7.5/7.0；阻止到 8 与阻止回落到 7.0 的双向 tie-breaker 均明确写出。✔
- 两个 ≤3 维分（Evidence 3、Significance 3）均含可核验引用、具体扣分与修复条件；其余维分亦各带引用与条件；Ethics 4→5 的上调依据与「若严格审稿人维持 4 上沿」的争议空间均给出。✔
- 每个分数均有可核验引用（章节 / 表 / 行号 / 工件字段 / SHA 实算值）。✔
- 特别判定已给出：本轮四项修复在文本 / 数据 / SHA / PDF 分页四层全部真实落地，属「补报被隐藏科学数据 + 加入削弱自身主张的诚实限定 + 闭合脚本可核验性 + 版式压缩」，**不是格式润色**；净影响对 Evidence（完整性 / 透明度）/ Soundness（内外一致）/ Ethics（诚实度）为正向并已如实计入，但**不新增支持中心主张的科学证据**、决定性缺口未动 → 维度分反映、总分维持 7.5。不迎合 8.0、不因主动不利限定额外惩罚、不因披露负结果默认加分。✔
- Checks run / Unresolved 如实区分 A 类（本版新闭合 + 历史已闭合）与 B 类（强基线未重跑、真实图阈值未复现、机制迁移未确认）两类不同性质问题，并单列 C（流程披露残留）、D（版本漂移）；C 类逐条给出仍未统一的 48,713/48,723、漏报的 29,564、`[5]` 题录说明、LLM 工具类别等可核验证据。✔
- 7 人 panel 各先独立给分再 synthesis，Critical  reviewer 的负信号已按本轮 C5/C7 闭合**如实调整**（不再以呈现选择性 / visual 脚本不可算扣分，改指中心机制不迁移），未强迫一致 / 分歧 / 赞扬 / 拒稿。✔
- 无 `TBD` / `TODO` / `[fill]` / 空标题；无「improve clarity / needs more experiments」类无定位泛化填充。✔
- 因果 / 递进逻辑显式：问题 → 证据 → 后果 → 动作。✔
- 未修改论文任何文件；仅写出本报告，未覆盖任何历史评审报告。✔

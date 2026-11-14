# CCF Paper Reviewer — Full Mode 独立评审报告（R47 / 修订后定稿）

**Paper:** *A Structure-Sensitive Null Ladder Exposes a Blind Spot in Connectome-Control Protocols*
**Target venue:** CVPR 2027（主会，double blind）
**Review date:** 2026-11-08
**Reviewer:** general-purpose-1（独立 CCF-A 审稿人 / AC，与论文作者无关）
**Mode:** `full` — scientific + writing + format + revision-action synthesis
**Input materials:** 磁盘最新版 `paper/main.tex`（719 行 / 40612 B / md5 `4afd89c155bb13af4153fe316f206f79`）、`main.bib`、`main.bbl`、`main.log`、`main.aux`、`main.pdf`（9 页）、`tables.tex`、`tables_taskaware.tex`、`tables_r39.tex`、`tables_r46.tex`；`results/r39_density_sweep/{metrics.json,summary.txt,run.log,config.json,r44_density_sweep.py,README.md}`；`results/r39_visual_task/{metrics.json,summary.txt,run.log,config.json,graph_stats.json}`；`audits/R46-correction-experiments-audit.md`；`scripts/make_r46_tables.py`；历史评审 `paper-null-ladder-r39-independent-review-20261108.md`（7.0）仅作扣分链与校准条件参考，不照抄分数。
**Search basis:** 联网复核 CVPR 2027 官方 AuthorGuidelines（`cvpr.thecvf.com/Conferences/2027/AuthorGuidelines`）与交叉来源的页数/LLM Statement/双盲/外链条款；关键前作题录沿用同日历史独立联网核验（arXiv:2610.10023、arXiv:2604.04033）。本次未对虚构题录逐条重查，已在 Confidence 与 Unresolved 标注。

## ⚠ 版本锁定声明（必读）

本报告评审的是磁盘上 **2026-11-08 当前最新版** `main.tex`（`md5 4afd89c155bb13af4153fe316f206f79`，719 行 / 40612 B），对应同目录 `main.pdf`（9 个物理页）。历史 r39 报告锁定的是 09:00 版（736 行 / md5 `cd17e1e6…`），本版相对它新增 §4.9 单变量密度隔离、§4.10 真实视觉任务、§4.6 预测主张降级、§4.8 五变量如实计数、Conclusion/Limitations/LLM Statement/题录修订。历史 7.0、8.2、7.5 报告均为历史，不构成本次判定依据。若之后版本再变，请按本声明锁定 md5 复核。

---

## Mode

`full`。按 `SKILL.md` 输出契约节序；七维 Scorecard 与校准按 `calibration-and-rank.md`；面板纪律按 `review-output-standards.md` / `reviewer-panel.md`；桌面检查按 `desk-checks.md`；声明—证据审计按 `universal-review-rubric.md`。1–5 维分、1–10 总分、1–5 置信度。严守 **Never round scores**，不迎合任何目标分数（含 8.0 / 8.2），不照抄历史 7.0。

## Venue and assumptions

- 目标 CVPR 2027 主会、双盲；按 CVPR/ICCV/ECCV 口味（novelty、technical quality、empirical validation、visual evidence、clarity、fair comparison）评分。
- 官方规则已**本次独立联网复核**（非仅采信历史 audit）：AuthorGuidelines 页面确认「Mandatory LLM Usage Statement: Every submission must include a short statement… Papers without it will be desk-rejected」、desk-reject 清单 (B) 含「missing LLM Usage Statement」「external links that expand the paper」、(C) 含「prompt injection and fabricated content」；交叉来源确认「Eight pages, figures and tables included. References and the LLM Usage Statement may go on further pages」「LLM Usage Statement, after the main text and before the references. It does not count toward the eight pages」「Main text: maximum 8 pages… Only references and the LLM Usage Statement may exceed this limit」「double blind… no external links… When in doubt, leave links out — even in the reference list」。LLM Statement 须说明工具、环节、程度；重大遗漏可触发 desk rejection / ethics referral。
- 假设：不实际投稿；不修改论文任何文件；按指定契约产出。评分视角为「严格但公平、与作者无关的 CVPR 审稿人 + AC」。

## Paper summary

论文追问「连线拓扑是否给视觉计算带来可测优势」，指出文献结论冲突源于**比较协议**而非生物学，并预注册三方裁决：在 96 节点 / 8 模块 / 注入 4 个两跳收敛 motif 的受控有向图上，用仅可经注入 motif 求解的 XOR 标签，评估嵌套 null 阶梯（L0 边数 / L1 度 / L2 模块对边数 / L3 有向三元体；L4 为匹配上界对照），10 冻结种子、配对 bootstrap、BH 校正。主结果：real 0.8152，所有 rung、A=0、shuffled-input 均在 chance（0.4795–0.5133），Δ=0.30–0.34，CI 排除 0，q=0.0002；但 rung 间仅差 0.0244、单调性反转，阶梯**无法定位**效应。Eq.(1)（限定为非均匀交换下的上界直觉）预测未受保护路径在混合下被销毁；§4.7 task-aware null（0.8346 vs 0.8371，q=0.40）与剂量阶梯（18/14/9/4/0 → 0.8371/0.8316/0.4988/0.5104/0.5117）闭合机制环。§4.6 的 20 图 powered 研究：12 预注册特征、8 个 BH 后显著、LOGO 幅度 MAE 0.1046 vs 常数 0.1635、sign agreement 0.60 = majority 0.60，本版已降格为 *corrected association* 并承认 8 个显著特征部分编码 intact/degraded 操纵。§4.8 两组真实 MaleCNS 实验：dense（768 节点 / 48,713 边）五条件全 chance；top-4 稀疏化后 real 0.6423 高于 A=0（0.5283）与删 motif（0.5160），但**度保持 null 保留优势 0.6162（CI 含 0）**、`hypothesis_supported=false`，本版已如实改为「Five settings changed together」并声明不能据此主张 motif-survival 阈值。

**本版两组决定性新实验**：§4.9 在**新流式**真实 MaleCNS 视觉子图（44,815 边 / 平均入度 58.35 / 29,442 visual body IDs）上做**单变量**密度扫描，只改 top-k（k=63/16/8/4/2），其余写死（mean 读出、120 epochs、hidden 64、lr 0.006、6 seeds、同一 motif）；oracle MLP 直接读 `[X_a,X_b]` 6 seeds 全 1.0000；real 0.5049→0.4886→0.5075→0.6227→**0.9863**→**0.9987**，A=0 恒 0.5062、度保持 null 恒 ~0.50、`density_isolated=true`。§4.10 真实 `sklearn.load_digits` 8×8 手写数字 10 类（1078/359/360）+ MNIST add-on，768 节点 MaleCNS 稀疏视觉子图作固定先验，五条件 6 seeds：real 0.7185 显著高于 A0 0.6190（Δ=+0.0995），但度保持 null 0.7190 与 real 无差异（Δ=-0.0005），非图 MLP **0.9722** 大幅优于所有图模型（MNIST 0.8879 vs 0.7649）；论文明确写「wiring prior is not a competitive inductive bias」「no claim of improved visual accuracy」。Conclusion 已限定「motif survival 是某一 regime 的 measured predictor，非普适原因」。

## Likely stance and calibrated score

**Weak accept 上沿（逼近 lean accept；不到 accept）。校准总分 7.5 / 10，学术置信度 5 / 5。**

判定链（独立重新判定，逐条对证据）：

1. **从历史 7.0 起算，不上调会自相矛盾。** 历史 r39 独立报告（同一独立评审链）白纸黑字把分数上限写成「中心机制外部效度为负 + 零视觉证据」，并给出**可核验、明码标价**的 Score-Change Conditions：①「单变量隔离的稀疏化消融 + dense 图 oracle 正对照 → +0.5 overall（→ 7.5）」；②「真实视觉任务演示**且确认 motif 阈值迁移** → +0.5 到 +1（→ 8）」；③操纵外独立验证 + 强基线 → +0.5；④流程/披露修补 → 仅消除 low desk 风险、`+0.5` 上限，且明确「继续修流程/披露/格式不会再抬高分数」。独立评审的一致性（calibration-and-rank.md「Consistency Check」第 4 条要求 score-change conditions 具体且可行）要求我尊重自己上一版公开声明的校准条件。

2. **条件 ① 本版真实、完整、可核验地兑现，给 +0.5 → 7.5。** §4.9 不是流程披露，而是**预注册的单变量因果隔离实验 + 正对照**：`r44_density_sweep.py` 的 SHA-256 经我本地 `shasum -a 256` 实算 = `360a3808bb4a86eee17e162b58d45565c7302c97ac35129178ff844717c8f795`，与 `metrics.json` 自报值逐字节一致；`run.log` 显示 oracle 6 seeds 全 1.0000、`density_isolated=true`、`run_complete=true`、2318 Arrow 批 / 151,856,684 行仅投影端点列、未 densify 全表。它把旧评审 C5「dense 稀释解释未证（无 oracle 正对照）+ sparse 多变量混淆、无法隔离密度」**整体消除**：标签完全可学（oracle 1.0000）证明 dense 全 chance 是传播稀释而非标签问题；只变 k 的单调阈值把「失败是否源于密度」从假设升级为 `density_isolated` 的实测。这是**新增科学证据**，正是历史评审点名要的东西。按 ① 给 +0.5。

3. **条件 ② 只兑现一半，故不到 8。** §4.10 确实补了旧评审点名的「真实视觉任务/视觉数据集」（真实 8×8 手写数字 10 类 + MNIST，6 seeds、CI），化解了「零视觉证据」这个**上限支柱之一**；但它是**诚实的负结果**：度保持 null = real、非图 MLP 0.9722 主导、「wiring prior is not a competitive inductive bias」。更关键的是**「确认 motif 阈值迁移」完全没有做到**：§4.8 `hypothesis_supported=false` 保留、度保持 null 保留优势 0.6162；§4.9 隔离的单一变量是**密度 k**而非 motif 生存计数，且 k=8/4/2 时 `23->63` motif 边已 `survived=false`（3/4 存活）而 real 仍 0.6227/0.9863/0.9987——说明稀疏后完整 motif 并非必需，测的是传播稀释而非 motif 生存阈值；Conclusion 自述「the threshold was not reproduced」「not a universal cause」。§4.10 反而**再证**中心机制不迁移。因此按 ②「且确认迁移」的硬条件，8 不成立；给 8 就是 team-lead 明确禁止的「因补了实验默认加分」。

4. **不因负结果额外惩罚诚实披露，也不默认加分。** §4.10 的净影响是「化解零视觉证据硬扣分、结论为负、机制未确认」：对 Significance 是**小幅净正**（从「全篇无视觉任务」到「有真实视觉任务且诚实报告」），但不足以构成 +0.5 到 +1；对「中心机制外部效度为负」这一**核心上限支柱丝毫未动**。其余流程修补（BH 引用补齐、LLM Statement 点名工具类别、3 条题录换真实、R37 部分入稿、边数口径说明）按历史 ④ 只消除 low desk 风险，不抬总分。

5. **Never round：** 7.5 是独立推演值，不是 7.0 上取整、也不是 8 下取整。+0.5 的 tie-breaker 是「条件 ① 真实闭合且 SHA 可核验」；阻止到 8 的 tie-breaker 是「真实视觉任务为负结果 + motif 阈值迁移未确认（`hypothesis_supported=false` 保留）+ 中心机制仍主要在 96 节点受控图 + 诊断性 XOR 标签上确立」。不迎合 8.0/8.2，不照抄 7.0。

### 两组决定性实验的独立净影响判定（含我核验出的新关切）

- **§4.9 单变量密度隔离（决定性正结果，但非机制迁移确认）。** 净增 Soundness（消除 C5）与 Evidence 的证据包严谨度；`density_isolated=true`、oracle 正对照、脚本 SHA 实算匹配属真实优点。**但它确认的是「入度 k 是 structure-sensitivity gate 的 determinant」，不是「motif 生存为 null 比较中的判别因果变量」**。故不闭合「真实图 motif-survival 阈值未复现」。
- **§4.10 真实视觉任务（诚实负边界）。** 净化解「零视觉证据」，但结论为负、且按 ② 的条件缺「机制迁移确认」。不额外惩罚诚实披露，也不默认加分到 8。
- **独立核验出的两处呈现不完整（新关切，计入 Clarity / Ethics 扣分理由，不抵消 +0.5）：**
  - (a) `metrics.json` / `summary.txt` / `run.log` / R46 audit 均记录 §4.9 每个 k 有 **4 个条件**；`make_r46_tables.py` 生成 `tables_r46.tex` 时只读 `real` 与 `A0`，**主动丢弃** `L1_degree_null` 与 `task_aware_null`。而 `task_aware_null` 在 k=4 = **0.9027**、k=2 = **0.9971**，几乎与 real 同步恢复——这恰是受控图「保护 task-relevant 边就恢复优势」结论在真实图上的**唯一呼应**，却在 Table density 与 §4.9 正文中完全未报告。数据公开留存、非造假，但属呈现不完整，且省略了与机制叙事最相关的一列。
  - (b) §4.10 的 MNIST add-on：`metrics.json` / `summary.txt` 明确记录 `real − degree_preserving_null = +0.0148, CI [0.0100, 0.0192]`（**显著为正**），与 digits 的「度保持 null = real」方向相反，也与正文「the gain over no graph is already explained by the degree-preserving control」的措辞张力。论文正文/表格对 MNIST 只报「0.8879 vs 0.7649」一句，**未呈现或讨论该结果**。Δ 很小、MLP 仍主导，主负结论不受威胁，但严格审稿人应要求补报并说明跨数据集不一致。

## Scorecard（七维）

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis（可核验引用） | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 4 | 4 | §1 第 3 段；§5「Relation to the strongest published control ladder」(`main.tex` lines 612–623)：把控制生成器当作一等实验变量、「begins at their strict endpoint」；§3.4 Eq.(1)、§4.7 task-aware 闭环；arXiv:2604.04033 本身已提出 staged control ladder（历史联网核实） | 扣分：delta 为「更高阶 rung + 全收敛 + 校正统计 + 构造性 task-aware 检验 + 生存计数」，各 rung 组件均为标准工具（`maslov2002`/`milo2002`/`wasserman1994`），属增量而非新框架；§4.9/§4.10 是验证与边界刻画，**不增加新颖性**。封顶 4。升至 5 需把该标准真正应用到一篇已发表 connectome-constrained 视觉模型或真实视觉任务并确认机制迁移 |
| Soundness | 4 | 5 | §4.9（`lines 562–585`）：`density_isolated=true`、oracle 6 seeds 1.0000、只变 k、`r44_density_sweep.py` SHA 实算匹配；§3.4 `line 276` 上界直觉限定；§4.7 剂量阶梯；§4.8 `lines 533–539` 如实改为 Five settings | 旧 4 的缺口 (ii)「稀释未证/无 oracle/多变量混淆」**已被 §4.9 完整闭合**；剩余 (i) 3-seed 预检 `FAILED`（`lines 330–333`）、(iii) 18017 CRC/末块崩溃保留（`lines 655–659`）。按历史条件「升至 5 需单变量隔离 + 正对照 + **一条哈希可核验的端到端主实验重跑**」，前两项已做、第三项未做，故维持 4（4 上沿）。升至 5 需补端到端哈希重跑并解释 §4.8 与 §4.9 度保持 null 行为的跨设置差异 |
| Evidence | 3 | 5 | `tables_r39.tex` Table real（sparse 0.6423 / 度保持 0.6162 CI 含 0 / `hypothesis_supported=false` 见 `lines 546–552`）；`tables_r39.tex` Table heldout（8/12、sign 0.60=0.60）；`r39_density_sweep/metrics.json`（四条件、monotone k、oracle）；`r39_visual_task/metrics.json`（real 0.7185 / null 0.7190 / MLP 0.9722 / `run_complete=true`）；§5 `lines 650–652` | **≤3 具体扣分**：(i) 中心 motif-survival 阈值在真实图上**未复现**——§4.8 `hypothesis_supported=false`、度保持 null 保留优势 0.6162；§4.9 隔离的是密度 k 而非 motif 生存计数，且 k=4/2 时 `23->63` 边丢失而 real 仍 0.9863/0.9987，恰恰说明完整 motif 非必需；(ii) 8 个显著特征部分编码 10 intact / 10 degraded 操纵，`sign_agreement=0.60 = majority_baseline=0.60`（§4.6 已降格为 corrected association 并承认，属披露改善但数据事实未变）；(iii) flyvis / toposens2026 强基线未重跑。**修复条件**：在操纵之外的独立图族验证 12 特征预测力，并给出至少一个**确认机制迁移**的真实数据结果 → 4。注：§4.9/§4.10 使证据包广度与严谨度明显提升、达到 3 上沿，但未改变上述三条事实 |
| Significance | 3 | 5 | §4.10 `lines 587–607` + `tables_r46.tex` Table visual：真实 `sklearn` digits 10 类 + MNIST add-on，real 0.7185 / A0 0.6190 / null 0.7190 / 非图 MLP 0.9722；§5 `line 665`「this is not a vision benchmark result」；CFP 含「Data synthesis…」「AI for Science…」 | **≤3 具体扣分**：旧扣分「全篇无图像/视觉任务/视觉数据集」**被 §4.10 部分化解**（现有真实视觉任务），但结果为**负**——wiring prior 非竞争偏置、度保持 null=real、非图 MLP 大幅主导，对 CVPR 的价值仍是「评估方法学诊断 + 负面边界刻画」，且负结果**再证**机制不迁移；核心贡献仍是对 96 节点受控替身的协议诊断。**修复条件**：在一个真实视觉任务或已发表 connectome-constrained 视觉管线上演示该标准**并确认 motif 阈值迁移** → 4。给 3（3 上沿），不因补了实验默认加到 4 |
| Clarity | 4 | 5 | 六节结构；8 张表全部由 `\input` 文件自动生成（最新 `main.tex` 已无手写 `\begin{table}`、无 claim-to-evidence 表）；数字可回溯；`main.log` 0 Overfull / 0 undefined / 0 LaTeX Warning | 扣分：摘要单段塞 5 组结果（`lines 26–56`，比历史版更挤）；§4.8 正文 `line 506` 用 48,713 边而 `tables_r39.tex` Table real caption 用 48,723（**仍未统一**）；**新发现** §4.9 Table density 省略 `task_aware_null`（k=4 0.9027 / k=2 0.9971）与 `L1_degree_null` 两列、§4.10 省略 MNIST 显著 delta 且正文「matches it exactly」未限定数据集；Limitations `line 662` 口径只写「9,766 vs 29,442」漏 29,564。升至 5 需拆摘要、补报四条件/MNIST、统一边数口径、补齐跨运行口径 |
| Reproducibility | 4 | 5 | `r44_density_sweep.py` SHA-256 实算 = `360a3808…` 与 metrics 自报一致；两组 `metrics.json` 均 `run_complete=true`；`tables_r46.tex` 由 `make_r46_tables.py` 从 pulled metrics 自动生成；§5 `lines 667–675` 补 sweep SHA `360a3808…`；`main.bib` 16 条 = `main.bbl` 16 条（BH 悬空闭合）、`grep -ciE '\url\|http'` = 0 | 扣分：新缺口——`results/r39_visual_task/` **无任何 `.py` 脚本**，`script_sha256 28f5744d…` 仅 metrics/audit 自报、**不可独立实算**（两组决定性实验只有 density 可哈希核验）；18017 执行脚本 CRC 不符保留；边数口径 48,723/48,713 未统一；`[5] flyhack`「numeric identifier taken from project record」保留。升至 5 需拉回 visual 脚本供 SHA 实算、一条哈希可核验端到端主实验重跑、统一边数口径 |
| Ethics / Limitations | 4 | 5 | §4.10 主动写「not a competitive inductive bias」「no claim of improved visual accuracy」；§5 Limitations（`lines 647–665`）保留 FAILED 门禁、崩溃运行、CRC 缺陷、所有负结果、负图像任务、口径不可混用；Conclusion `lines 693–696`「measured predictor in one regime, not a universal cause」；LLM Statement `lines 701–711` 点名工具类别；§5 Ethics（CC-BY 4.0、无人类被试/动物实验/部署系统） | 扣分：诚实披露与负结果纪律属**明显优点**（已在 Top strengths 与 panel 加分），但仍残留三项：(i) R37 并发会话 P2 门禁异议仅以 `line 657`「a recorded concurrent gate-dissent」极含糊措辞入稿，未点名、未说明异议内容及其是否影响「结构敏感前提曾否通过」，属**部分闭合**；(ii) LLM Statement 点名的是工具**类别**（agentic coding assistant / LLM-based search assistant / general-purpose LLM agent）而非具体 name the tool(s)，双盲下可接受但留低概率 desk/ethics 残余；(iii) §4.9 `task_aware_null` 同步恢复与 §4.10 MNIST 显著 delta 未在正文讨论（透明性残余）。补齐三项 → 5 |

**Overall:** 7.5  | **Scholarly Confidence:** 5

**Recommendation:** weak-accept（上沿，逼近 lean accept；一个严格 fit 视角仍可判 borderline 7，距 accept 8 差一个「真实图机制迁移确认」）
**Verdict:** 分数上限仍由「中心机制外部效度为负」决定，但「零视觉证据」支柱已被 §4.10 部分化解、且 §4.9 真实闭合了历史 ① 号上调条件，故自 7.0 上调 +0.5 至 7.5。继续修流程/披露/格式不会再抬高总分。上调到 8 需：在稀疏、cell-type-resolved、任务可解的真实子图上**确认 motif-survival 阈值迁移**（翻转 `hypothesis_supported=false`）或在一个已发表 connectome-constrained 视觉管线上演示该标准并确认机制迁移。下调触发：独立复核证明 §4.9 数值无法从 `r44_density_sweep.py` 复现、或 `density_isolated` 因 motif 边丢失/标签泄漏而无效（−1 或 fatal）；或证实 §4.9 `task_aware_null` 同步恢复与 §4.8 度保持 null 保留优势构成未解释的内部矛盾、削弱「density alone」因果（−0.5）；或 18017 修复被证明改变任一报告数字（−0.5）。置信度给 5：全文、全部证据工件、两组 metrics 逐字段、density 脚本 SHA 实算、PDF 逐页、编译日志、官方规则联网复核均可得；visual 脚本未拉回属**局部**可核验性缺口，已在 Reproducibility/Unresolved 如实标注，不改变整体判定置信度。

## Top strengths

1. **闭合的因果环（受控图）**：Eq.(1) 预测未受保护 motif 边在混合下被销毁 → §4.7 剂量阶梯实测 18/14/9/4/0 → 0.8371/0.8316/0.4988/0.5104/0.5117 的离散阈值 → task-aware null 在全重连背景下恢复优势（0.8346 vs 0.8371，Δ=0.0025，q=0.40），并给出「保留 14/18 边的 background-only null 仍有优势」的直接证据。逐数与 `tables_taskaware.tex` 一致。
2. **本版真正兑现了历史评审点名的决定性实验（§4.9）**：预注册单变量密度隔离 + oracle 正对照，把「dense 失败是否源于密度/传播稀释」从「未证假设」升级为 `density_isolated=true` 的实测；oracle 6 seeds 1.0000 排除标签问题；真实 1.05 GB 权重表 pyarrow.ipc 流式 2318 批 / 151,856,684 行、仅投影端点列未 densify；脚本 SHA 实算匹配。这是本次评分能从 7.0 上调的主要且唯一的**新增科学证据**。
3. **异常完整的负结果与边界披露纪律**：§4.8 dense 全 chance 定性为「前提失效的边界条件」、sparse `hypothesis_supported=false` 且度保持 null 保留优势、明言「no replication claim」「Five settings changed together… cannot isolate density」；§4.10 主动写「wiring prior is not a competitive inductive bias」「no claim of improved visual accuracy」；FAILED 门禁、崩溃运行、CRC 缺陷、所有负结果全部保留。诚实披露不因负结果被惩罚，已在评分中正向计入。
4. **可核验性（density 侧）与题录/格式合规**：`r44_density_sweep.py` SHA 实算匹配；两组 `run_complete=true`；`tables_r46.tex` 由脚本自动生成；`main.bib` 16 = `main.bbl` 16、BH 悬空引用补齐、无外链；3 条题录换真实记录。
5. **对最接近前作的定位诚实**：§5 承认 arXiv:2604.04033 已有 staged control ladder、本文从其 strict endpoint 起步、明确「We did not rerun their flyvis stack」；Conclusion 主动写「not a universal cause」。

## 已闭合的关切（不再扣分）

| 旧关切（历史 7.0 / 8.2 报告） | 本版闭合证据 |
|---|---|
| 单变量隔离消融缺失 + dense 无 oracle 正对照（Score-Change ① / 旧 C5） | §4.9 `r39_density_sweep/metrics.json`：`density_isolated=true`、`oracle_dense` 6 seeds 1.0000、只变 k、`r44_density_sweep.py` SHA 实算匹配、`run.log` 尾 `run complete in 315.6s` |
| §4.8「3 变量/其余不变」与 pulled config 不符（旧 C7） | `main.tex` `lines 533–539` 如实改为「Five settings changed together」并逐项列出（top-4、mean→sum、64→128、0.006→0.008、120→300），声明「cannot isolate density as the cause」 |
| §4.6 预测主张过度、未承认操纵编码（旧 C3） | `lines 446–453` 降格为 *corrected association*，明言「several of the eight significant features… partly encode that manipulation itself; they validate the manipulation rather than discover an independent graph law」 |
| Conclusion 无限定因果外推（旧 M3） | `lines 693–696`「the threshold was not reproduced… measured predictor in one regime, not a universal cause」 |
| 「零视觉证据」（旧 Significance 硬扣分） | §4.10 真实 `sklearn` digits + MNIST add-on（部分化解；结论为负，见 Significance 扣分） |
| BH 悬空引用 / 无 cite（旧 C7） | `main.bib` 16 = `main.bbl` 16；`\cite{benjamini1995}` 出现于 `lines 34/102/304`；参考文献 `[1]` Benjamini & Hochberg 1995 |
| LLM Usage Statement 未点名工具（旧 minor） | `lines 701–711` 点名工具类别（coding assistant / search assistant / general-purpose agent）+ 环节 + 程度 |
| 3 条编造题录 / 外链（旧 desk 风险） | PDF p9 题录带「Verified by public search, 2026-11-08」；`grep -ciE '\url\|http' main.bib` = 0 |
| R37 门禁异议完全未入稿（旧 C7 / Unresolved C） | `line 657`「a recorded concurrent gate-dissent」——**部分入稿**，措辞含糊，见 Ethics 残留 |
| 历史已闭合项（v2 provenance、blanket 复现声明、两张手写表、Eq.(1) 限定、摘要 20 图矛盾、页数、双盲） | 沿用历史 r39 独立报告结论，本版未恶化 |

## Major/fatal concerns

**Fatal concerns：无。** 未发现可独立支撑拒稿的新颖性坍塌、中心主张完全无证据、评测整体失效或格式/伦理硬违规。

| # | Severity | Concern | Evidence basis | Fix class | Owner | Score-change condition |
|---|---|---|---|---|---|---|
| C1 | Major | 中心机制（motif 生存为控制协议中的因果变量）仍只在 96 节点合成受控图 + 诊断性 XOR 标签上确立；真实 MaleCNS 子图上阈值未复现。§4.9 隔离的是密度 k 而非 motif 生存计数，k=4/2 时 `23->63` motif 边丢失而 real 仍 0.9863/0.9987，说明稀疏后完整 motif 非必需。论文已如实披露、不作复现声明，故非内部一致性缺陷，但仍是限制贡献外推的实质缺口 | §4.8 `lines 546–561`、Table real、`hypothesis_supported=false`；§4.9 `lines 575–585`；`r39_density_sweep/metrics.json` `motif_edges_survived`；Conclusion `lines 693–696` | experiment / scope | `ccf-experiment-designer` | 在稀疏、路径可辨识的真实子图上确认 motif-生存阈值（翻转 `hypothesis_supported=false`）→ Evidence/Significance +0.5 至 +1 |
| C2 | Major | 真实视觉任务为**负结果**且未确认机制迁移：非图 MLP 0.9722 大幅主导、度保持 null = real，§4.10 反而再证中心机制不迁移；对 CVPR 的价值仍是方法学/负面边界而非正面贡献 | §4.10 `lines 587–607`、Table visual、`r39_visual_task/metrics.json`、`sum` 未现 | experiment / positioning | `ccf-experiment-designer` / `ccf-paper-writer` | 真实视觉任务/已发表视觉管线演示**且确认 motif 阈值迁移** → Significance/Evidence +0.5 到 +1（→ 8） |
| C3 | Moderate | 最强已发表基线未重跑（flyvis `lappalainen2024`、toposens2026 共享初始化管线）；signed/typed 边未建模；L1 只实现度保持思想 | §5 `lines 650–652`、§5 `line 620`「We did not rerun their flyvis stack」 | experiment | `ccf-experiment-designer` | 重跑并加入 task-aware 控制 → Evidence/Novelty +0.5（投稿前难） |
| C4 | Moderate | 20 图「8/12 显著」部分由 10 intact / 10 degraded 操纵编码驱动；`sign_agreement=0.60 = majority 0.60` 符号零技能。§4.6 已降格为 corrected association 并承认，但摘要 `line 51` 与贡献列表 `line 121` 仍把「8 显著」写作正面结论 | `r39_heldout/metrics.json`、`tables_r39.tex` Table heldout、§4.6 `lines 436–453` | experiment / writing | `ccf-experiment-designer` | 操纵外独立图族验证，或把摘要/贡献列表同步降格 → Evidence +0.5 |
| C5 | Moderate（**新发现**） | 呈现选择性：§4.9 Table density 只列 real/A=0，`make_r46_tables.py` 主动丢弃 `L1_degree_null` 与 `task_aware_null`（后者 k=4 0.9027 / k=2 0.9971，与 real 同步恢复，是受控图 task-aware 结论在真实图上的唯一呼应）；§4.10 正文/表格省略 MNIST `real − degree_null = +0.0148, CI [0.0100,0.0192]` 显著为正且与「gain already explained by degree-preserving control」措辞张力。数据公开留存、非造假，但属呈现不完整且省略了与机制/负结果刻画最相关的结果 | `r39_density_sweep/{metrics.json,summary.txt,run.log}`、`make_r46_tables.py lines 21–29`、`tables_r46.tex`、`r39_visual_task/{metrics.json,summary.txt}`、R46 audit `lines 29–36/70–71` | writing / transparency | `ccf-paper-writer` | 补报四条件与 MNIST delta 并讨论跨数据集/跨条件差异 → Clarity/Ethics +0.5 上限 |
| C6 | Moderate | 旧流程缺陷如实保留但未消除：3-seed 预检 `FAILED`、18017 执行脚本 CRC 不符、末块崩溃后 LOGO 由持久化行本地重算；R37 门禁异议仅以「a recorded concurrent gate-dissent」含糊入稿 | §4.2 `lines 330–339`、§5 `lines 655–659`、R46 audit | reproducibility / disclosure | `f-research-v1` | 一条哈希可核验端到端主实验重跑 + 完整披露 R37 异议性质/影响 → Soundness/Reproducibility/Ethics +0.5 |
| C7 | Minor | 可核验性局部缺口：`results/r39_visual_task/` 无 `.py` 脚本，`28f5744d…` 不可独立实算；边数口径 48,723（Table real caption）/48,713（§4.8 正文）未统一；Limitations 口径只写 9,766/29,442 漏 29,564；`[5] flyhack`「numeric identifier taken from project record」保留 | 目录清单、`grep` 计数、`tables_r39.tex`、`main.tex line 506/662`、PDF p9 `[5]` | reproducibility | `ccf-paper-writer` / `f-research-v1` | 拉回 visual 脚本、统一口径、清理题录说明 → Reproducibility +0.5 |
| C8 | Minor | 摘要单段 5 组结果过载；§5 披露冗长；Table 1/4/6/8 用 `\resizebox` 缩放打印偏小；LLM Statement 点名工具**类别**而非具体 name the tool(s)（低概率残余 desk 风险） | 摘要 `lines 26–56`、`tables*.tex`、`main.tex lines 701–711` | writing | `ccf-paper-writer` | 拆摘要 + 披露表化 + 表格改 `\footnotesize`/两栏拆分 + 明确工具描述 → Clarity +0.5 |

### Claim–Evidence Audit（主要主张）

| Claim | Where stated | Evidence provided | Strength | Reviewer deduction | Required fix |
|---|---|---|---|---|---|
| 受控图上结构优势真实且可复现 | 摘要、§4.4、Conclusion | Table 1：10 seeds，Δ=0.30–0.34，CI 排除 0，q=0.0002；A=0/clean_motif/shuffled 对照 | strong | 无 | 无 |
| 匹配全局高阶统计无法定位优势 | §1、§4.4–4.5 | rung 间 Δ 仅 0.0244；单调性 1 次反转；L1 已匹配 conv2 统计却仍 chance | adequate | 结论仅在受控图成立，稿件已 scope | 无（已 scope） |
| motif 生存（非 rung 顺序）是因果变量 | §1 贡献 2、§4.7、Conclusion | Eq.(1) + 剂量阶梯 + task-aware null（受控图） | adequate（受控图）/ weak（真实图） | 真实图 `hypothesis_supported=false`；§4.9 隔离的是密度 k，k=4/2 motif 边丢失 real 仍高；稿件已写「measured predictor here, not a universal cause」 | 真实图确认实验；否则维持 scope |
| 单变量密度隔离成立、dense 失败是传播稀释 | 摘要 `lines 52–53`、§4.9、`density_isolated=true` | `r39_density_sweep/metrics.json` 四条件、oracle 6 seeds 1.0000、只变 k、脚本 SHA 实算匹配 | strong | 隔离的是密度 gate，**不是** motif-survival 阈值；论文已明确「must not be read as a motif-survival threshold」 | 补报 `task_aware_null` 同步恢复一列，避免读者误读为机制迁移 |
| 幅度可预测、符号不可预测（corrected association） | 摘要、§4.6、Table heldout | 20 图、8/12 BH 显著、MAE 0.1046 vs 0.1635、sign 0.60=0.60 | weak | 显著特征部分编码操纵、符号零技能；§4.6 已诚实降格，但摘要/贡献列表仍作正面表述 | 摘要与贡献列表同步降格；补操纵外验证 |
| 真实视觉任务上 wiring prior 不是竞争偏置 | 摘要 `lines 53–54`、§4.10、Conclusion | Table visual：real 0.7185 / null 0.7190 / A0 0.6190 / MLP 0.9722；MNIST 0.8879 vs 0.7649 | adequate（digits）/ partial（MNIST） | MNIST `real − degree_null = +0.0148, CI [0.0100,0.0192]` 显著为正，与「gain already explained by degree-preserving control」措辞张力，未呈现/讨论 | 补报 MNIST 四条件并讨论跨数据集不一致 |
| 真实 MaleCNS 结果界定协议边界、支持「在目标图上测 gate」 | §4.8 `lines 553–560`、摘要、Conclusion | dense 全 chance；sparse real 0.6423 但度保持 null 保留效应、`hypothesis_supported=false` | adequate（宽泛方法学建议）/ absent（中心机制） | 是「不迁移边界」而非外部效度验证 | 明确区分两类主张 |
| 所有表格由 pulled metric 文件脚本生成 | §5 `lines 667–675` | Tables 1–8 + 4 图；dense/sparse/sweep 三个 SHA；`tables_r46.tex` 自动生成 | adequate | 生成脚本**主动只选部分条件**（C5）；visual 脚本未拉回不可实算（C7） | 补条件列、拉回 visual 脚本 |
| 全部参考文献已核实、无虚构题录 | PDF p9、`main.bib` | 16 条编译 = 16 条 bib；多条带「Verified by public search」；`[5]` 注明编号取自 project record | adequate | BH 悬空已闭合；`[5]` 编号来源未独立公开核实已披露 | 清理 `[5]` 等题录内验证说明 |

## Writing concerns

- **摘要超载**：`lines 26–56` 单段塞入「主矩阵 + 阶梯失败 + 构造性检验 + 20 图 + 密度隔离 + 真实视觉任务」六组结果，比历史版更挤；建议拆成「裁决结果」与「机制/边界」两句群。
- **呈现准确性（本版最重要，见 C5）**：§4.9 Table density 与正文只呈现 real/A=0 两条件，正文称「A=0 and the degree-preserving null remain near 0.50 throughout」——对 `L1_degree_null` 准确，但完全未提 `task_aware_null` 在 k=4/2 与 real 同步恢复（0.9027/0.9971）。§4.10 正文「the degree-preserving null matches it exactly」未限定为 digits，而 MNIST 上 `real − degree_null = +0.0148` 显著为正。两处都不是数据造假（数据均在公开 artifacts 与 R46 audit），但会让读者得到不完整的图景。
- **口径不一致（残留）**：§4.8 正文 `line 506` 用 48,713 边，`tables_r39.tex` Table real caption 用 48,723；Limitations `line 662` 只写「9,766 vs 29,442 IDs」，漏 R46 audit 列出的 29,564（visual task）。R46 audit `lines 88–93` 已给出四 run 完整口径表，稿件应同步。
- **披露冗长**：§4.2 与 §5 Limitations 完整性披露占篇幅大、信息密度低；建议压成「defect / status / affected number / disposition」小表。
- **表格可读性**：Table 1/4/6/8 使用 `\resizebox`，双栏打印数值列偏小；建议 `\footnotesize` 或两栏拆分。
- **题录内验证说明**：多条参考文献条目内嵌「Verified by public search, 2026-11-08」「No external URL is included, per the CVPR 2027 author guidelines」等元信息，属诚实披露但不符合常规题录体例，建议移入附录/致谢说明。

## Format/venue concerns

- **页数（本次 pypdf 逐页核验当前 `main.pdf`，9 物理页）**：主文在**第 8 页收尾**——p8 `line 098` 为 Conclusion 末句「…explains the conflicting reports.」，p8 `line 099` 起为 `LLM Usage Statement` 标题与开头（`lines 100–101`）；**第 9 页只含** LLM Statement 续文（`lines 005–015`，「debug experiment scripts…」至「The authors take full responsibility for the content.」）+ `References` 标题（`line 016`）+ `[1]`–`[16]` 共 16 条（`lines 017–089`），**无任何正文残留**（逐页关键词检测 p9 无 Conclusion/Discussion/实验章节文字）。按官方「Only references and the LLM Usage Statement may exceed this limit」「LLM Usage Statement… after the main text and before the references. It does not count toward the eight pages」，正文 = 8 页、p8 末尾与 p9 为不计数的 LLM Statement + 允许的 references → **合规**。注意与历史 r39 版差异：历史版 LLM Statement 全在 p9，本版因 §4.9/§4.10 增内容而**跨 p8/p9**，但两者均合规。
- **双盲**：`\author{Anonymous}`（`line 18`）、无致谢、LLM Statement 无身份信息、`grep -ciE '\url\|http' main.bib` = 0 → pass。
- **LLM Usage Statement**：存在、位置正确（Conclusion 后、references 前）、强制要求满足；本版点名工具**类别**并说明环节与程度（`lines 701–711`），较历史泛称实质改善。官方要求 name the tool(s)，点名「类别」在双盲下可接受但留低概率残余（见 Ethics）。
- **编译质量**：`main.log` 0 LaTeX Warning / 0 Overfull / 0 undefined / 0 Citation undefined；`main.bib` 16 = `main.bbl` 16；8 张表由 4 个 `\input` 文件提供、编号连续（§5 称 Tables 1–8）；`cvpr.sty` + `ieeenat_fullname.bst` + `10pt,twocolumn,letterpaper` 官方模板 → pass。
- **Prompt injection / 隐藏操纵**：通读 `main.tex`、4 张表、`main.bib`、LLM Statement、PDF 文本，未发现隐藏指令或白字操纵；LLM Statement 主动披露「to simulate an independent peer-review panel」，属公开声明 → pass。
- **Venue fit**：CFP 主题提供合法挂载点，但 CVPR 口味重视 visual evidence / recent baselines / cross-dataset tests；本版虽有真实视觉任务，结论为负、非图 MLP 主导、机制不迁移，fit 仍属**间接**，构成 Significance 扣分，非 desk rejection 理由。
- **Desk checks**：Paper Length **pass**（9 物理页但正文 8 页、p9 仅 refs + LLM Statement）；Topic Compatibility **uncertain**（方法学诊断对视觉会议间接）；Minimum Quality **pass**；Policy/Anonymity/Compliance **pass with residual**（LLM Statement 点名类别而非具体工具、R37 异议含糊）；Prompt Injection **pass**；Ethics **pass**（无人类被试、CC-BY、misuse 风险在 §5 讨论、负结果全保留）。**Desk rejection risk: low**；Reason：无硬性格式/匿名/外链违规；**Can be fixed before review? yes**（补工具描述、完整披露 R37、补两处省略结果）。

## 7 人独立 reviewer panel

Reviewer: Best-Justified Reviewer
Expertise: evaluation methodology / graph learning，寻找最强可辩护接收理由
Likely score: 8 / lean-to-clear accept
Confidence: 5
Main positive signal: Eq.(1) → 剂量阶梯 → task-aware null 闭合因果环；10 配对种子 + BH + 常数/多数基线；§4.9 预注册单变量密度隔离 + oracle 6 seeds 1.0000 + 脚本 SHA 实算匹配 + `density_isolated=true`，是历史评审点名的决定性实验的真实兑现；§4.10 真实图像任务诚实报告负结果；负结果/失败全保留；§5 诚实对标前作 control ladder。
Main negative signal: 范围窄、中心机制未迁移、真实视觉任务结论为负。
Evidence basis: §3.4、§4.7、`r39_density_sweep/{metrics.json,run.log,r44_density_sweep.py}`、§4.10、§5 对标段。
Fatal concern if any: 无。
Score-change condition: 一个确认机制迁移的真实数据结果 → 9。

Reviewer: Critical Reviewer
Expertise: 严格 CVPR 审稿人，寻找最强拒稿理由
Likely score: 6 / borderline
Confidence: 5
Main positive signal: 承认 §4.9 单变量隔离与 oracle 正对照是真实新增证据、内部逻辑自洽、统计未 cherry-pick、披露异常坦诚；provenance 与 Conclusion 外推已闭合。
Main negative signal: 全部正向机制发现来自 96 节点合成 XOR 替身；§4.10 真实视觉任务为负（MLP 0.9722 主导、度保持 null=real），再证机制不迁移；§4.8 `hypothesis_supported=false` 保留、度保持 null 保留优势 0.6162；§4.9 隔离的是密度 k 且 k=4/2 motif 边丢失 real 仍高（完整 motif 非必需）；强基线未重跑；FAILED 预检与 18017 CRC 保留；**§4.9 省略 task_aware_null 同步恢复、§4.10 省略 MNIST 显著 delta** 两处呈现选择性。
Evidence basis: §3.1、§4.8/Table real、§4.9/metrics.json、§4.10/Table visual、§5 Limitations、R46 audit。
Fatal concern if any: 无硬致命；「中心机制不迁移 + 真实视觉任务负结果 + 呈现选择性」组合接近 major threshold。
Score-change condition: 真实视觉任务上的机制迁移确认 + 补报两处省略结果 → 7。

Reviewer: Method / Soundness Reviewer
Expertise: 因果推断 / 图 null 模型 / 统计有效性
Likely score: 7 / lean accept
Confidence: 5
Main positive signal: Eq.(1) 已限定上界直觉；§4.9 单变量隔离 + oracle 正对照把「dense 失败=传播稀释」从假设升级为实测，`density_isolated=true`；脚本 SHA 实算匹配；Conclusion 已限定，内外一致。
Main negative signal: 预注册 3-seed 门禁仍 `FAILED`；§4.9 与 §4.8 对「度保持 null 是否保留优势」给出相反答案（不同图/不同设置），论文用「Five settings」「visual-ID 口径」解释但未做逐变量对账；k=4/2 `23->63` motif 边丢失而 real 仍高，削弱「特定两跳 motif 是关键」。
Evidence basis: §3.4 `line 276`、§4.2、§4.8 `lines 533–539`、§4.9、`r39_density_sweep/metrics.json` `motif_edges_survived`、`run.log`。
Fatal concern if any: 无。
Score-change condition: 端到端哈希重跑 + 逐变量对账 §4.8/§4.9 差异 → 8。

Reviewer: Evidence / Experiment Reviewer
Expertise: baselines / ablations / 统计功效 / 复现
Likely score: 7 / lean accept
Confidence: 5
Main positive signal: 10 seeds、配对 CI、全族 BH、2×2 鲁棒性网格、两个证伪消融、20 图 powered 研究、§4.9 单变量消融 + oracle、§4.10 五条件 6 seeds + CI、两组 `run_complete=true`、表自动生成。
Main negative signal: 8/12 显著特征部分编码操纵、sign=majority；真实数据 `hypothesis_supported=false`；强基线未重跑；visual 脚本未拉回不可实算 SHA；§4.9 表格只列 2/4 条件、§4.10 MNIST 只报 1 句。
Evidence basis: Tables 1–8、`r39_heldout/metrics.json`、两组 `metrics.json`/`summary.txt`/`run.log`、`make_r46_tables.py`。
Fatal concern if any: 无。
Score-change condition: 补报四条件/MNIST + 拉回 visual 脚本 + 操纵外验证 → 8。

Reviewer: Novelty / Positioning Reviewer
Expertise: 最接近前作与真实 delta
Likely score: 6 / borderline
Confidence: 4
Main positive signal: 前作 limitations 把更高阶 null/更长训练列为 future work，本文补足并新增 task-aware 构造性检验 + 生存计数框架；§5 定位诚实、明确未复跑 flyvis。
Main negative signal: 前作**本身已有 control ladder**，delta 为标准工具组合；§4.9/§4.10 是验证/边界刻画不增新颖性；venue fit 方法学而非视觉，真实视觉任务为负。
Evidence basis: §5 `lines 612–623`、arXiv:2604.04033（历史联网核实）、`maslov2002`/`milo2002`/`wasserman1994`。
Fatal concern if any: 无（新颖性未坍塌，封顶 4/5）。
Score-change condition: 在已发表视觉模型上应用该标准并确认机制 → 8。

Reviewer: Writing / Clarity Reviewer
Expertise: 贡献可恢复性 / 图表可解释性
Likely score: 7 / lean accept
Confidence: 5
Main positive signal: 六节结构、数字可回溯到自动生成表、显式 scope conditions、Conclusion 与 §4.8/§4.10 一致、编译零警告、§4.6/§4.8 措辞更准确。
Main negative signal: 摘要塞 6 组结果；§4.9 Table density 省两列且正文只提 2/4 条件；§4.10 省略 MNIST 显著 delta；48,713/48,723 口径不一致；Limitations 漏 29,564；`\resizebox` 表格偏小。
Evidence basis: 摘要 `lines 26–56`、`tables_r46.tex`、`make_r46_tables.py`、§5 `line 662`、`main.log`。
Fatal concern if any: 无。
Score-change condition: 拆摘要 + 补条件列/MNIST + 统一口径 → 8。

Reviewer: Ethics / Reproducibility Reviewer
Expertise: 许可 / 透明性 / 失败披露 / artifact 审计
Likely score: 8 / lean-to-clear accept
Confidence: 5
Main positive signal: CC-BY 4.0、无人类被试；FAILED 门禁、崩溃运行、CRC 缺陷、dense 负结果、`hypothesis_supported=false`、§4.10 负结果全如实上报且不作复现/泛化声明；density 脚本 SHA 实算匹配；表自动生成；BH 引用补齐、题录换真实、无外链、双盲。
Main negative signal: R37 门禁异议仅以「a recorded concurrent gate-dissent」含糊入稿；LLM Statement 点名工具类别而非具体工具；§4.9 `task_aware_null` 同步恢复与 §4.10 MNIST 显著 delta 未在正文讨论；visual 脚本未拉回。
Evidence basis: §5 Limitations/Ethics/Reproducibility、`line 657`、`lines 701–711`、R46 audit、目录清单。
Fatal concern if any: 无。
Score-change condition: 完整披露 R37 + 补报两处省略结果 + 拉回 visual 脚本 → 9。

### Panel synthesis

Agreement: 七位一致认为受控图内部逻辑、统计卫生与数值可复算性成立；§4.9 是历史评审点名的决定性实验的真实、SHA 可核验兑现；诚实披露负结果与边界属罕见优点；无致命缺陷；历史 7.0 版的两个 Major 完整性关切与本版三项披露修补已闭合。
Disagreement: Best-Justified(8)/Ethics(8) 与 Critical(6)/Novelty(6) 在「一个正向机制仍由合成替身支撑、真实视觉任务为负结果、且存在两处呈现选择性的方法学诊断，是否够 CVPR 级贡献」上对立；Method(7)/Evidence(7) 强调 §4.9 隔离的是密度而非 motif 阈值、且 k=4/2 motif 边丢失 real 仍高。
Decisive positive axis: 闭合因果环（受控图）+ §4.9 预注册单变量隔离与 oracle 正对照（脚本 SHA 实算匹配）+ 完整可核验 artifacts + 异常透明的负结果纪律 + 严格 scope。
Decisive negative axis: 中心机制外部效度仍为负（`hypothesis_supported=false` 保留）+ 真实视觉任务为负且未确认机制迁移 + 强基线未重跑 + FAILED 预检/18017 CRC 保留 + §4.9/§4.10 呈现选择性。
Unresolved evidence: §4.8 与 §4.9 度保持 null 行为差异的逐变量归因；§4.9 `task_aware_null` 同步恢复是否被刻意省略；§4.10 MNIST 显著 delta 的跨数据集解释；R37 门禁异议的性质与影响；visual 脚本 SHA 不可实算。
AC stance: **weak-accept 上沿，7.5**。最终立场跟随「最强未解决关切」——中心机制外部效度为负且真实视觉任务结论为负——不被「诚实披露 / 单变量隔离 / 格式合规」平均掉；历史 ① 号上调条件真实兑现使分数自 7.0 上调 +0.5，但历史 ② 号的「确认 motif 阈值迁移」未满足，故不达 8。

## Concern-to-action

| Concern | Action | Owner | Affected criterion | Score-change condition |
|---|---|---|---|---|
| C1 机制未迁移 | 在稀疏、路径可辨识的真实子图上确认 motif-生存阈值（翻转 `hypothesis_supported=false`）；维持现有严格 scope | `ccf-experiment-designer` | Evidence, Significance | +0.5 至 +1 |
| C2 真实视觉任务负结果 | benchmark/analysis-track 定位 + 至少一个确认机制迁移的真实视觉任务/已发表管线演示 | `ccf-experiment-designer` / `ccf-paper-writer` | Significance, Evidence | +0.5 到 +1（→ 8） |
| C3 强基线 | 重跑 flyvis / toposens2026 管线并加入 task-aware 控制 | `ccf-experiment-designer` | Evidence, Novelty | +0.5（投稿前难） |
| C4 预测贡献 | 操纵外独立图族重测 12 特征；摘要/贡献列表同步降格为探索性 | `ccf-experiment-designer` / `ccf-paper-writer` | Evidence | +0.5 |
| C5 呈现选择性 | §4.9 补报 `L1_degree_null`/`task_aware_null` 两列（含 k=4 0.9027 / k=2 0.9971）；§4.10 补报 MNIST 四条件与 `+0.0148, CI [0.0100,0.0192]` 并讨论 | `ccf-paper-writer` | Clarity, Ethics, Evidence | +0.5 上限 |
| C6 流程缺陷 | 哈希可核验端到端主实验重跑；完整披露 R37 异议性质/影响 | `f-research-v1` | Soundness, Reproducibility, Ethics | +0.5 |
| C7 可核验性/口径 | 拉回 visual 脚本供 SHA 实算；统一 48,713/48,723；Limitations 补 29,564；清理 `[5]` 题录说明 | `ccf-paper-writer` / `f-research-v1` | Reproducibility | +0.5 |
| C8 写作/排版 | 拆摘要、披露表化、`\resizebox` 改 `\footnotesize`/两栏拆分、明确 LLM 工具描述 | `ccf-paper-writer` | Clarity | +0.5 |

## Score-Change Conditions

| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | 在稀疏、cell-type-resolved、任务可解的真实子图上**确认 motif-survival 阈值迁移**（翻转 `hypothesis_supported=false`），或在已发表 connectome-constrained 视觉管线上演示该标准并确认机制 | Evidence, Significance, Novelty | +0.5 到 +1 overall（→ 8） |
| Raise score | 重跑 flyvis / toposens2026 强基线 + 操纵外独立图族验证 12 特征 + 一条哈希可核验端到端主实验重跑 | Evidence, Novelty, Soundness, Reproducibility | +0.5 overall |
| Raise score | 补报 §4.9 四条件与 §4.10 MNIST delta 并讨论；完整披露 R37 异议；拉回 visual 脚本；统一边数/口径；清理题录说明 | Clarity, Reproducibility, Ethics | 消除 low desk 风险；+0.5 overall 上限 |
| Lower score | 独立复核证明 §4.9 数值无法从 `r44_density_sweep.py` 复现，或 `density_isolated` 因 motif 边丢失/标签泄漏而无效 | Reproducibility, Soundness | −1 overall 或 fatal |
| Lower score | 证实 §4.9 `task_aware_null` 同步恢复（0.9027/0.9971）与 §4.8 度保持 null 保留优势（0.6162）构成未解释的内部矛盾，削弱「density alone」因果 | Soundness, Evidence | −0.5 overall |
| Lower score | 确认 R37 异议意味着结构敏感门禁从未通过、或 18017 修复改变任一报告数字 | Soundness, Reproducibility | −0.5 到 −1 overall |
| No quick change | 继续修流程/披露/格式（含补 LLM 工具名、BH、题录、页数口径）不会再抬高总分；自然视觉任务上的正面外部效度与机制迁移确认需新实验纲领 | Significance, Evidence | 投稿前不大可能改变 |

## Checks run

1. 锁定并通读磁盘最新版 `main.tex`（719 行 / 40612 B / md5 `4afd89c155bb13af4153fe316f206f79`）、`main.bib`、`main.bbl`、`main.log`、`main.aux`、`tables.tex`、`tables_taskaware.tex`、`tables_r39.tex`、`tables_r46.tex`、`scripts/make_r46_tables.py`；`Grep` 确认最新版已无 `\begin{table}`、无 claim-to-evidence 表、R37 仅 `line 657` 含糊入稿。
2. 逐字段读 `r39_density_sweep/metrics.json`（`oracle_dense` 6 seeds 1.0000、`density_sweep` 五 k 各四条件、`density_isolated=true`、`run_complete=true`、`motif_edges_survived` 在 k=8/4/2 的 `23->63`=false）、`summary.txt`（四条件完整表）、`run.log`（oracle 逐 seed、四条件逐 k、尾行 `run complete in 315.6s`）、`config.json`、`README.md`。
3. 逐字段读 `r39_visual_task/metrics.json`（digits 五条件 6 seeds + CI + `real_minus_condition`、MNIST add-on `real − degree_preserving_null = +0.0148, CI [0.0100,0.0192]` 显著为正、`run_complete=true`）、`summary.txt`、`graph_stats.json`（29,564 IDs / 3,072 边）、`config.json`。
4. 读 `audits/R46-correction-experiments-audit.md` 全文（含四条件表、MNIST 五条件、cross-run comparability 表 9,766/9,766/29,442/29,564），与稿件做一致性对账。
5. **SHA-256 实算**：`shasum -a 256 results/r39_density_sweep/r44_density_sweep.py` = `360a3808bb4a86eee17e162b58d45565c7302c97ac35129178ff844717c8f795`，与 `metrics.json`/audit/§5 自报值逐字节一致；`ls results/r39_visual_task/` 确认**无 `.py` 脚本**，`28f5744d…` 不可实算（记为 C7）。
6. **编译/题录检查**：`main.log` LaTeX Warning=0 / Overfull=0 / undefined=0 / Citation undefined=0；`main.bib` 16 个 `@` = `main.bbl` 16 个 `\bibitem`（BH 悬空闭合）；`grep -ciE '\url\|http' main.bib` = 0；LLM Statement 位于 Conclusion 后、references 前。
7. **PDF 逐页提取（pypdf 6.19.0，9 页）**：p8 以 Conclusion 末句「…explains the conflicting reports.」收尾（`line 098`），p8 `lines 099–101` 为 LLM Statement 开头；p9 `lines 005–015` 为 LLM Statement 续文、`line 016` References、`lines 017–089` 为 `[1]`–`[16]` 共 16 条，逐页关键词检测 p9 无正文残留。按官方「仅 references + LLM Usage Statement 可上额外页」判定合规。
8. **联网独立复核** CVPR 2027 AuthorGuidelines 官方页面（8 页正文含图表、仅 refs + LLM Statement 可超页、LLM Statement 强制且须说明工具/环节/程度、desk-reject 清单含 missing LLM Statement / external links / fabricated content / prompt injection、双盲、无外链）；关键前作题录沿用同日历史独立联网核实。
9. 读历史 r39 独立评审（7.0）仅作扣分链与 Score-Change Conditions 参考；逐条核验本版对 ①②③④ 号条件的实际兑现情况（① 完整兑现、② 半兑现、③ 未兑现、④ 已兑现但不抬分）。
10. **一致性自检**：7.5 与「最强未解决关切 = 中心机制外部效度为负 + 真实视觉任务负结果」匹配；两个 ≤3 维分（Evidence 3、Significance 3）均含可核验引用、具体扣分与修复条件；其余维分亦各带引用与条件；无致命缺陷故不 reject；未迎合 8.0/8.2、未照抄 7.0；+0.5 的 tie-breaker 与阻止到 8 的 tie-breaker 均明确写出。

## Unresolved

**A 类 — 已闭合（不再扣分）**：单变量密度隔离 + dense oracle 正对照（历史 ① 号条件）：`density_isolated=true`、oracle 6 seeds 1.0000、脚本 SHA 实算匹配；§4.8 五变量如实计数与「不能据此主张阈值」声明；§4.6 预测主张降级并承认操纵编码；Conclusion 因果限定；BH 悬空引用；LLM Statement 点名工具类别；3 条题录换真实 + 无外链；摘要 20 图矛盾、Eq.(1) 限定、v2 provenance、blanket 复现声明、两张手写表、页数合规（以上后几项沿用历史闭合结论）；「零视觉证据」硬扣分被 §4.10 部分化解（但结论为负，见 Significance）。

**B 类 — 仍未解决，属「缺少决定性实验/比较」**：
- **flyvis / arXiv:2604.04033 训练栈未复跑**（§5 已诚实声明；L1 只实现度保持思想）。
- **真实图 motif-survival 阈值仍未复现**：§4.8 `hypothesis_supported=false`、度保持 null 保留优势 0.6162（CI 含 0）；§4.9 隔离的是密度 k 而非 motif 生存计数，且 k=4/2 时 `23->63` 边丢失 real 仍 0.9863/0.9987（完整 motif 非必需）。论文明确不作 replication claim。这不是「负结果被隐瞒」，而是中心机制外部效度的实质缺口。
- **真实视觉任务未确认机制迁移**：§4.10 负结果（MLP 0.9722 主导、度保持 null=real）再证不迁移；历史 ② 号条件的「且确认 motif 阈值迁移」未满足。
- **单变量隔离虽已补，但 §4.8 与 §4.9 对「度保持 null 是否保留优势」给出相反答案**（不同图/不同设置），论文用「Five settings / visual-ID 口径」解释，未做逐变量对账；sparse 0.6423 是否部分源于 sum 读出 / hidden 128 / lr 0.008 仍未逐项排除。
- **操纵外独立图族验证 12 特征预测力 + 强基线重跑**仍缺失。

**C 类 — 流程/披露残留**：3-seed 预检 `FAILED`、18017 执行脚本 CRC 不符、末块崩溃后 LOGO 本地重算全部保留（已披露）；R37 并发会话 P2 门禁异议仅以 `line 657`「a recorded concurrent gate-dissent」含糊入稿（未点名、未说明性质/影响）；LLM Statement 点名工具**类别**而非具体 name the tool(s)（低概率 desk/ethics 残余）；**§4.9 省略 `task_aware_null`（k=4 0.9027 / k=2 0.9971）与 `L1_degree_null` 两条件、§4.10 省略 MNIST `+0.0148, CI [0.0100,0.0192]` 显著 delta** 两处呈现选择性（数据公开、非造假，需补报讨论）；边数口径 48,723（Table real caption）/48,713（§4.8 正文）未统一；Limitations 口径只写 9,766/29,442 漏 29,564；`[5] flyhack`「numeric identifier taken from project record」保留；`r39_visual_task/` 无 `.py` 脚本，`28f5744d…` 不可独立实算；多条题录内嵌「Verified by public search」元信息不符体例。

**D 类 — 版本漂移 / 历史口径**：本报告锁定当前版 md5 `4afd89c155bb13af4153fe316f206f79`（719 行）；历史 r39 独立报告锁定 09:00 版（736 行 / md5 `cd17e1e6…`），两版差异为 §4.9/§4.10 新增、§4.6/§4.8/Conclusion/Limitations/LLM Statement/题录修订。LLM Usage Statement 由历史版「全在 p9」变为本版「跨 p8/p9」（均合规）；历史评审引用的「Table 7 claim-to-evidence 表」在本版已不存在（8 张表全为数据表）。历史 7.0 / 8.2 / 7.5 报告均为历史，不构成本次判定依据。若之后再变，尤其 §4.9 / §4.10 / Conclusion，请按锁定 md5 复核。

## Output self-check

- 节序遵循 full 契约与指定输出契约：Mode / Venue and assumptions / Paper summary / Likely stance and calibrated score（内嵌两组实验净影响判定与新关切）/ 七维 Scorecard / Top strengths / 已闭合关切表 / Major-fatal concerns（内嵌 Claim–Evidence Audit）/ Writing concerns / Format-venue concerns（内嵌 Desk checks）/ 7 人独立 reviewer panel（含 Best-Justified 与 Critical，附 Panel synthesis）/ Concern-to-action / Score-Change Conditions / Checks run / Unresolved（A/B/C/D 分类）/ Output self-check。✔
- 所有 Markdown 表分隔符有效、每行列数一致。✔
- 分数、置信度、Recommendation 内部一致：7.5 = weak-accept 上沿、Confidence 5、无致命缺陷、历史 ① 号条件真实兑现使分数自 7.0 上调 +0.5，② 号「确认机制迁移」未满足故不达 8。✔
- 机器可读结论行**有且仅有一行**，采用严格格式（Overall + Scholarly Confidence 两项、整数置信度）；另给 Recommendation 与 Verdict；全文其余处未重复该精确格式。✔
- 严守 Never round scores：7.5 未取整到 8、未因 8.0/8.2 目标抬分、未照抄 7.0；+0.5 与阻止到 8 的 tie-breaker 均明确写出。✔
- 两个 ≤3 维分（Evidence 3、Significance 3）均含可核验引用、具体扣分与修复条件；其余维分亦各带引用与条件。✔
- 每个分数均有可核验引用（章节/表/行号或工件字段）。✔
- Checks run / Unresolved 如实区分 A 类（本版新闭合 + 历史已闭合）与 B 类（强基线未重跑、真实图阈值未复现、机制迁移未确认）两类不同性质问题，并单列 C（流程披露残留）、D（版本漂移）。✔
- 特别判定已给出：§4.9 为「单变量密度隔离 + oracle 正对照」的决定性正结果但**不是** motif-survival 阈值迁移确认；§4.10 为「诚实负结果、化解零视觉证据、但再证机制不迁移」；不因补实验默认加分到 8、不因负结果额外惩罚诚实披露；格式按官方规则判定合规（正文 8 页收尾、p9 仅 refs + LLM Statement 续文）。✔
- 独立核验出的两处呈现选择性（§4.9 省略 task_aware_null 同步恢复、§4.10 省略 MNIST 显著 delta）已计入 C5 / Clarity / Ethics 扣分理由与修复条件，未当作造假，也未纵容。✔
- 无 `TBD`/`TODO`/`[fill]`/空标题；无「improve clarity / needs more experiments」类无定位泛化填充。✔
- 因果/递进逻辑显式：问题 → 证据 → 后果 → 动作。✔
- 未修改论文任何文件；仅写出本报告，未覆盖任何历史评审报告。✔

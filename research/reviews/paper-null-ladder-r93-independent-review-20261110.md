# CVPR 2027 · Full 模式独立评审报告（与作者完全无关的 CCF-A 审稿人 / AC）

> 本报告由一位对论文写作过程、作者会话、目标分数均无任何背景信息的独立评审人，
> **仅依据磁盘文件**独立推演。未读任何作者会话；未获知、也未迎合任何「目标分数」；
> 历史 R47/R49/R60/R91 报告仅在「关切演化」意义上被阅读，其分数（分别为 7.5 / 7.5 / 6.3 / 5.4）
> 一律不作为锚点、不照抄、不反向对齐。严守 `Never round scores`。
> 报告落盘前未在回复中宣布任何分数或结论。

---

## 0. 报告元数据与独立性声明

| 字段 | 值 |
|:---|:---|
| Mode | `full`（scientific + writing + format + revision-action synthesis） |
| Venue / year / track | CVPR 2027 主会研究论文，双盲评审稿（按 CVPR 口味：novelty / technical quality / empirical validation / **visual evidence** / fair comparison / clarity） |
| 论文标题 | *A Structure-Sensitive Null Ladder Exposes a Blind Spot in Connectome-Control Protocols* |
| 被评审版本 | `r93-candidate/`（唯一版本；`main.tex` = `paper.tex`） |
| 被评审版本 md5 | `0a3a4da4b47b1f3f1170747ac85c4ae4`（`main.tex`，42,454 字节，757 行） |
| 配套 PDF md5 / 页数 | `257a877db05954a119179a842279b070`、9 页（`main.pdf` = `paper.pdf`，逐字节一致） |
| Reviewer mode | 独立 AC；7 人独立 reviewer panel 先于综合 |
| 本次是否重新联网核实 | **否**。官方 CVPR 2027 规则依据已落盘的 `submission-constraints.md`（其自述为 2026-11-10 联网核实整理），本次未重新抓取；2026 年 6 篇 arXiv 题录真实性、enrollment/reciprocal-reviewer 等时效性条款均未离线独立复核，见 §15 C 类 |
| Review date | 2026-11-10 |
| Report file | `/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision/ccfa-review-reports/paper-null-ladder-r93-independent-review-20261110.md` |
| 独立性 / 只写声明 | 未修改稿件、指标、审计、账本、校验器；未创建任何其他评审报告；所有复算均为**只读**（不落盘）；本报告是唯一写出的文件 |

**必读协议读取情况**
- `SKILL.md`（`full` 模式、输出契约、tie-every-concern-to-evidence）— 已读。
- `calibration-and-rank.md`（1–5 维分 / 1–10 总分 / 1–5 置信度、`Never round scores`、Scorecard 与 Score-Change Conditions 契约）— 已读。
- `review-output-standards.md` — 用户给出的 `ccf-paper-reviewer/references/` 下路径**不存在**；按 `SKILL.md` 第 27 行指针改读 `ccf-common/references/review-output-standards.md`（已读）。此路径缺失属技能目录问题，**不计为稿件缺陷**。
- `reviewer-panel.md`（7 角色 + full 附加角色、synthesis 不平均掉致命关切）— 已读。
- `submission-constraints.md`（CVPR 2027 官方规则整理、desk-reject class B/C）— 已读；其自评 "PASS" 一律由本次独立复核，不照抄。
- 另加载（full 模式需要）：`universal-review-rubric.md`、`desk-checks.md`、`review-workflow.md`、`venue-review-styles.md`、`fixed-output-format.md`、`writing-review/latex-format-audit.md`、`writing-review/revision-actions.md`、`prose-quality-guardrails.md`。
- 历史 4 份独立评审（r47/r49/r60/r91）— 已读，仅用于理解「最强关切是否演化」。

**贯穿所有历史版本、且本次独立复核仍成立的最强关切**：中心正向结论限于 96 节点受控图 + 由注入两跳 motif 可解的 XOR 诊断标签，R60 已明确点出其「接近设计同义反复」；真实视觉任务上无任何正向、经严格 null 对照验证的拓扑效应；`mechanism_transfer_confirmed=false`、`expected_strong` 未达成、C3 未复现 task-aware recovery；对 CVPR 视觉受众的 significance 有限。本轮是否改变了这一决定性轴，是本次评审的核心问题（见 §6、§10）。

---

## 1. 版本锁定与实际读过的文件清单

**锁定结果（本次独立实测）**
- `main.tex`：42,454 字节 / md5 `0a3a4da4b47b1f3f1170747ac85c4ae4`；`paper.tex` 经 `cmp` 逐字节一致（md5 相同）。
- `main.pdf`：2,120,176 字节 / md5 `257a877db05954a119179a842279b070`；pypdf 6.19.0 确认 9 页；`paper.pdf` 逐字节一致。
- `main.log` 结尾 `Output written on main.pdf (9 pages, 2120176 bytes).`，与被评审 PDF 一致。
- 相对历史口径：r91 版 `main.tex` 为 43,897 字节 / md5 `471de7f…`，R60 版为 45,200 字节 / md5 `995c8280…`。r93 字节数下降约 1.4 KB（摘要压缩 + 边界实验重组为 scope 表），同时新增 §3.5 与 §4.13。

**实际读过的指标 / 证据文件（逐份列出）**

*稿件与呈现（r93-candidate/）*：`main.tex`（全文 757 行）、`preamble.tex`、`main.bib`、`main.bbl`、`main.log`、`main.pdf`、`tables.tex`、`tables_taskaware.tex`、`tables_heldout.tex`、`tables_boundary.tex`、`tables_r91.tex`、`tables_r93.tex`、`tables_r93_scope.tex`、`make_r91_tables.py`、`make_r93_tables.py`、`cvpr.sty`、`ieeenat_fullname.bst`、`figures/` 4 图（图内容以 caption 与表格对账为主）。

*根 A（`…/f-research-v1-run-20261108-102500-null-ladder-v2/results/`）*：`r51_motif_survival/metrics.json`（C1 固定密度剂量负结果）、`r51_pathblock/metrics_pathblock.json`（C1b 修复）、`r51_multisubgraph/metrics_multisubgraph.json`（C1c 两独立真实子图，含全部 `per_dose[*][cond].mean` 与 `decision_rules`）、`r51_strong_baseline/metrics.json`（C3 已发表 ladder 复跑）、`r51_independent_family/metrics.json`（C4，24 图逐图 Δ、12 特征 `feature_matrix`、`graph_names`、`criteria`、`decision` 字段）；抽查 `p3_p4/metrics_completed.json`、`p3_p4_taskaware/metrics.json`、`r39_heldout/metrics.json`、`r39_density_sweep/metrics.json`、`r39_visual_task/metrics.json`；`contract-v2.md`（`expected_strong` 定义，§7）。

*根 B（`papers/R63-results/r93_local/`）*：`config_v3.json` + `config_v3.sha256` + `run_v3.log`、`metrics_v3.json`（全文 220 行）、`make_r93_v3_protocol.py`、`run_r93_v3.py`、`config.json`（13:33 早期 v2）、`make_r93_protocol.py`、`run_r93_local.py`、`run.log`、`run_console.log`、`trial1_failed_label_design/{config.json,config.sha256,run.log,run_console.log}`、`trial2_failed_unlearnable_label/{config.json,config.sha256,make_r93_protocol.py,run_r93_local.py,run.log,run_console.log}`；`r91-candidate/main.tex` 与 `r91-candidate/main.log`（上一版对比）。

*历史与规则*：`submission-constraints.md`；`ccfa-review-reports/` 下 r47/r49/r60/r91 四份独立评审（仅关切演化）。

**本次未重新联网**：所有官方规则、题录真实性、时效性条款均依落盘材料，见 §15 C 类。

---

## 2. Checks run 清单

| # | Check | 方法 | 结果 |
|:--|:---|:---|:---|
| C-01 | 版本锁定 | `wc -c` / `md5` / `cmp` / pypdf 页数 | 通过（§1） |
| C-02 | 协议与官方规则 | 4 份必读 + full 模式引用 + `submission-constraints.md` | 通过（第 3 份路径缺失已定位到 `ccf-common`） |
| C-03 | 稿件 / 表格 / 脚本 / 题录 / 日志通读 | Read 全文 | 完成 |
| C-04 | 头条数字对账 | python 从 `metrics*.json` 数值定位 + 摘要/引言/结果/结论/7 张表逐字段比对 | 全部可溯源（§5.1） |
| C-05 | 生成脚本运行时读数核验 | 只读复现 `make_r93_tables.py` / `make_r91_tables.py` 逻辑，与落盘 `tables_r93.tex` / `tables_r91.tex` 比对 | 一致，无手抄（§5.2） |
| C-06 | v3 独立复算 | 从 C4 原始 `feature_matrix`/`deltas` 按 `run_r93_v3.py` 逻辑**完整重跑**：LOGO ridge、MAE、gain、配对 bootstrap CI、1000 sign-flip p、3 密度层、5 反例、6 规则 | 逐值精确复现，最大误差 `3.3e-16`（§5.3、§6） |
| C-07 | v3 预注册 / 特征分组事前性 | `config_v3.sha256` 复算 = `64abafe4…`；对照 v1/v2 config、两个 trial 日志时间线 | SHA 一致；但「事前」仅相对本次 reanalysis 成立（§6.2） |
| C-08 | 两次失败 trial 是否被包装 / 隐瞒 | `grep` main.tex 全文 + 读全部 trial 日志与 config | 主文**完全未提**（隐瞒，非包装成正面）；支撑材料如实记录（§6.5） |
| C-09 | C1c null 条件列陈述核验 | 提取 `metrics_multisubgraph.json` 全部 `per_dose[*][cond].mean` | **发现 r93 新引入的事实性矛盾陈述**（§5.4） |
| C-10 | 统计与 flag | 10/6 seeds、配对 bootstrap、BH、sign-flip、shared-init、oracle/leakage、剂量单调、p2==pfull、跨运行 ID、非官方 flyvis、两 flag | 通过（§7） |
| C-11 | CVPR 2027 合规 | pypdf 逐页 p8/p9、编译告警精确分类、双盲、题录外链、注入扫描 | 发现 **1 个 Overfull**（新增 scope 表）+ LLM 占位符（§8） |
| C-12 | `expected_strong` 定义一致性 | 稿件 §3.5 定义 vs `contract-v2.md:163-170` | **不一致**（§7、§15 B 类） |
| C-13 | 重新联网核实 | 无 | **本次未重新联网** |

---

## 3. Desk Rejection Assessment

| 检查 | 状态 | 证据 | 后果 |
|:---|:---|:---|:---|
| 篇幅（8 页正文 + 额外页仅 refs / 强制声明） | **PASS** | 9 物理页；pypdf 逐页确认 p1–p8 主文、p8 以完整 Conclusion 末句 "control construction, not topology, explains conflicting reports." 收尾；p9 仅 `LLM Usage Statement` + `References` 15 条，逐页关键词检测无正文残留（"Method" 命中来自 [13] 题录 *Social Network Analysis: Methods and Applications*，假阳性） | 无 |
| 强制 LLM Usage Statement | **FAIL / BLOCKER（行政）** | `main.tex:747-748` 正文为 `\emph{[To be supplied by the authors.]}` 占位符 | CVPR 2027 强制项，缺失即 class B desk-reject。按作者指令属行政项，**不加权科学总分**，但独立地使当前包件不可直接提交 |
| 双盲 | PASS | `\author{Anonymous}`、`\def\paperID{*****}`、无致谢/单位/邮箱；`toposens2026` 以第三人称 "The closest prior work" 引用 | 无 |
| 题录零外链 | PASS | `main.bib` / `main.bbl` / `main.tex` 对 `http/url/href/www` 计数均为 0；`main.bib` 15 个 `@` = `main.bbl` 15 个 `\bibitem` | 无 |
| `main.log` 0 undefined refs | PASS | `undefined` / `Citation…undefined` / `Reference…undefined` / `LaTeX Warning` / `^!` / `Emergency` 计数均为 0 | 无 |
| `main.log` 0 Overfull | **FAIL（新增）** | `Overfull \hbox (136.25835pt too wide) in paragraph at lines 6--14`，定位为 `(./tables_r93_scope.tex`；r91 版 `main.log` Overfull 计数 = 0 | 本轮新增 scope 表（`{lll}` 三列）溢出栏宽；属格式缺陷，按用户指令**不参与抬高或压低由证据决定的科学总分**，但如实记录 |
| 官方 `cvpr.sty` / 10pt / 双栏 | PASS | `\documentclass[10pt,twocolumn,letterpaper]{article}` + `\usepackage[review]{cvpr}`；`preamble.tex` 仅 `\linespread{0.84}`（正文之外） | 无 |
| Prompt injection / 隐藏操纵 | PASS | 对 `main.tex` / 全部 `tables*.tex` / `main.bib` / `main.bbl` 扫描 `ignore previous / disregard / as an ai / you must score / system prompt / hidden instruction / override` 等模式，**0 命中** | 无 |
| 伦理与可评审性 | PASS | 纯计算、无人类/动物受试、公共 CC-BY 4.0 数据、误用风险（错误结构归因）已讨论 | 无 |
| Topic compatibility | UNCERTAIN / 偏弱 | 自述为 evaluation-methodology study，无 image benchmark、无自然视觉任务、无视觉精度提升主张（`main.tex:88-91`） | 属 venue fit 实质性风险，计入 Significance，非 desk 理由 |

**Desk verdict**：科学/格式层面无致命项；行政层面 `high / likely`（LLM 占位符 + enrollment 2026-11-10 23:59 AOE + reciprocal-reviewer quota 需作者门户侧处理）。按用户指令，行政阻断**不参与抬高或压低由证据决定的科学总分**。

---

## 4. Paper Summary 与贡献—证据图

**一段摘要**：论文把 connectome-constrained 视觉模型中「拓扑是否有用」的文献分歧重述为**比较协议（null 生成器）问题**，预注册一条嵌套 null ladder（L0 边数 / L1 度 / L2 模块对 / L3 有向 triad census，L4 为独立匹配控制），配一个只能经注入两跳收敛 motif 求解的 XOR 标签。受控 96 节点图上 real 0.8152、全部 null 与无图/打乱对照在 chance（0.4795–0.5133，Δ=0.30–0.34，BH q=0.0002），但 rung 间差仅 0.0244、单调性破坏，故裁决为「第三种结果」：null family 才是混淆项。task-aware null 保住 18 条 motif 边即恢复优势（0.8346 vs 0.8371），motif 剂量在 ≤9 边时塌到 chance。真实 MaleCNS wiring 上：C1 固定密度剂量因密度补偿交换新建两跳路径而失败（`hypothesis_supported=false`）；C1b 路径阻断修复（adaptive/remedial）得单调剂量；C1c 完全事前、两独立真实子图复现四档剂量、七规则全通过；C3 忠实复跑已发表 ladder 复现 weak/strict 但**未**复现 task-aware recovery（DiD −0.0477，CI 含 0）；C5 六门禁通过；真实图像分类为阴性（非图 MLP 0.9722 主导）。**本轮新增**：§3.5 控制充分性的形式化判据（P(T)、A1–A4、命题与证明梗概、训练前检查）；§4.13 在 24 张非操纵真实 MaleCNS 子图上的 v3 判据检验（8 路径感知特征 vs 4 全局统计特征，LOGO ridge 预测 |Δ|，MAE 0.0371 vs 0.0835，gain 0.0464 [0.0197,0.0748]，p=0.001，`positive_result=true`）；边界实验重组为 scope 表；摘要压缩；`p2==pfull` 解释；`expected_strong` 主文定义；两个负面 flag 写进摘要/结论；C1c null 条件列说明。结论落点：control 构造而非拓扑解释冲突报告，motif survival 是受控区间内的实测预测器而非普适原因。

| 项 | 内容 |
|:---|:---|
| Claimed problem / gap | 已发表 connectome-control 结论互相矛盾；缺乏以 null 生成器本身为实验变量、且任务结构敏感的受控比较 |
| Contribution map | ① 可复用 null-generator 标准（机器校验不变量 + gate + 校正统计 + **§3.5 形式化判据**）；② 受控图上「全局统计量不保任务相关 motif」的裁决；③ 20 图 held-out 关联研究；④ 真实 wiring 上 C1→C1b→C1c→C3/C5 的证据链与 scope 边界；⑤ **§4.13 24 图判据检验（本轮新增正向结果）** |
| Contribution type | evaluation-methodology / diagnostic / negative-result（作者明确不是新 backbone） |
| Evidence package | 10 冻结种子（主矩阵/剂量）、6 种子（C4/density/visual）、配对 seed-level bootstrap（R=5000）、BH、sign-flip（1000）、oracle/leakage 探针、shared-init、不变量断言、剂量干预、两独立真实子图、忠实复跑、clean rerun；v3 为**无新训练**的 C4 数据 reanalysis |
| Stated limitations | 96 节点受控图；真实 MaleCNS 为边界非复现；单变量扫描只隔离 in-degree；真实图像任务阴性；sign prediction = 多数类；flyvis 栈未重跑；三种子预检仍 `failed`；早期聚合块崩溃且脚本 checksum 不匹配；visual-ID 口径跨运行不可混用；两负面 flag unmet |

---

## 5. 主张—证据对账（Claim–Evidence Audit）

### 5.1 头条数字逐字段溯源（本次独立抽查）

| 稿件头条数字（位置） | 落盘来源（精确值） | 一致性 |
|:---|:---|:---:|
| 0.8152 / 0.4795–0.5133 / q=0.0002（摘要、§4.3、`tab:main`） | `p3_p4/metrics_completed.json::main_matrix.mean_acc`：real 0.815234375、L0 0.4794921875、L1 0.50390625、L2 0.49609375、L3 0.4986328125、L4 0.5015625、clean_motif 0.834765625、shuffled_input 0.51328125；`p2_gate_corrected.bootstrap_p=0.00019996` | ✓ |
| 0.8346 / 0.8371 / 0.4988 / 0.5117 / 0.8260（§4.7、`tab:taskaware`） | `p3_p4_taskaware/metrics.json::mean_acc`：task_aware_null 0.8345703125、real 0.837109375、motif_keep_50 0.498828125、motif_removed 0.51171875、background_only 0.8259765625 | ✓ |
| 0.1046 / 0.1635 / 36% / 0.60=0.60（§4.6、`tab:heldout`） | `r39_heldout/metrics.json::logo`：magnitude_mae 0.1046198、constant_baseline_mae 0.1635485、sign_agreement 0.6、majority_baseline 0.6 | ✓ |
| 0.9987 / 0.9863 / oracle 1.0000 / `density_isolated`（§4.8） | `r39_density_sweep/metrics.json::density_sweep[2].real.mean_acc=0.9986979`、`[4]=0.9863281`、`oracle_dense.per_seed` 全 1.0 | ✓ |
| 0.7185 / 0.9722 / MNIST +0.0148（§4.8、`tab:visual`） | `r39_visual_task/metrics.json`：mean_acc.real 0.7185185、mlp_baseline[0] 0.9722222、`mnist_addon…delta=0.0148333` | ✓ |
| C1 `0.9772/0.5051/0.9745`、`hypothesis_supported=false`；C1b `0.5055→0.9641→0.9772`（`tab:r91dose`） | `r51_motif_survival/metrics.json::task_a`、`r51_pathblock/metrics_pathblock.json::task_a_pathblock` | ✓ |
| C1c 0.5017→0.6889→0.8955→0.9432 / 0.5017→0.6742→0.8877→0.9407；Δ 0.4415[0.4272,0.4538] / 0.4390[0.4249,0.4522] | `metrics_multisubgraph.json::dose_real_means_ordered`；Δ/CI 由 `make_r91_tables.py::boot_ci` 从 `per_seed` 重算 | ✓（本次按同 `rng=default_rng(20261110)` 顺序复现，逐值一致） |
| weak 0.2282 / strict 0.0532 / task-aware 0.0056 / DiD −0.0477（`tab:r91repl` 下半） | `r51_strong_baseline/metrics.json::ladder.dense`（前三者为 `boot_ci` 重算值，本次复现 0.2282[0.1954,0.2593]、0.0532[−0.0153,0.1218]、0.0056[−0.0171,0.0264]）；DiD −0.0476852 | ✓ |
| **v3 新增**：MAE 0.0371 / 0.0835 / 0.2310，gain 0.0464[0.0197,0.0748]，p=0.001，5 反例，2/3 strata（摘要、§4.13、`tab:r93criterion`） | `metrics_v3.json`（见 §5.3 独立复算） | ✓ |

**结论**：数字层**零造假、零手抄、零不一致**；所有头条数字可溯源到落盘 `metrics*.json` 或由脚本从 `per_seed` 数组运行时重算。

### 5.2 生成脚本运行时读数核验

- `make_r93_tables.py`：从 `metrics_v3.json` 运行时读取全部单元格（`mae_path_aware` / `mae_path_blind` / `constant_baseline_mae` / `judgment_gain` / `permutation_p` / `ci` / 3 个 `density_strata` / `len(counterexamples)`），无硬编码数字；落盘 `tables_r93.tex` 数值与 `metrics_v3.json` 逐值一致。
- `make_r91_tables.py`：从 4 份 pulled metrics 读取，所有单元格来自 `per_dose[*][cond]['mean']` 或 `boot_ci` 重算，无硬编码数字；本次按同 rng 顺序复现的 `boot_ci` 与落盘 `tables_r91.tex` 逐值一致。
- `run_r93_v3.py`：读取 C4 `metrics.json::results` 的 `feature_matrix` / `deltas`，LOGO ridge 逐图算误差，bootstrap/permutation 由 `default_rng(20261110)` 生成。本次从 C4 原始数据完整重跑，全部输出与 `metrics_v3.json` 吻合（§5.3）。

### 5.3 v3 独立复算（关键）

从 C4 `feature_matrix(24×12)` 与 `deltas(24)` 按 `run_r93_v3.py` 逻辑完整重跑（`y=|delta|`、8 path-aware / 4 path-blind 列、LOGO ridge α=1.0、标准化仅 fit 训练折、配对 bootstrap R=5000、1000 sign-flip、3 密度层）：

| 量 | 独立复算 | `metrics_v3.json` 存储 | 判定 |
|:---|:---|:---|:---:|
| mae_path_aware | 0.0371126855 | 0.03711268550556565 | ✓ |
| mae_path_blind | 0.083472518 | 0.08347251795940074 | ✓ |
| judgment_gain | 0.0463598325 | 0.04635983245383507 | ✓ |
| 95% CI | [0.0196658581, 0.0747802935] | 同 | ✓ |
| permutation_p | 0.001 | 0.001 | ✓ |
| strata low/mid/high | 0.0224292589 / 0.1149799115 / **−0.0190886051** | 同 | ✓ |
| 反例数 / 图名 | 5：g_s0_k12, g_s1_k12, g_s2_k12, g_s3_k6, g_s3_k12 | 同 | ✓ |
| 6 规则 / `positive_result` | 全 True / True | 全 True / True | ✓ |
| `per_graph_errors` 与复算最大偏差 | `3.33e-16` | — | ✓ |

`config_v3.sha256` 复算 = `64abafe47232f8db98c24fe644969d52dd56cc7803c6745de6051e7c57364fbe`，与 `config_v3.json` 实际 SHA 及 `metrics_v3.json::config_v3_sha256` 三方一致。**数字与布尔判定本身完全诚实、可复算。**

### 5.4 本轮新引入的事实性矛盾（独立核验发现）

r93 §4.15（`main.tex:615-616`）**新增**一句：「Its degree-null, task-aware and motif-removed columns remain near chance at every dose.」

从 `metrics_multisubgraph.json::task_a_multisubgraph.subgraphs[*].stats.per_dose[*][cond].mean` 提取的真实值：

| 子图 | 剂量 | L1_degree_null | task_aware_null | motif_removed |
|:---|:---|:---:|:---:|:---:|
| S1_broad | p0 | **0.6742** | **0.7032** | 0.5017 |
| S1_broad | p1 | 0.5017 | **0.8877** | 0.5017 |
| S1_broad | p2 | 0.5017 | **0.8839** | 0.5017 |
| S1_broad | pfull | 0.5017 | **0.9432** | 0.5017 |
| S2_narrow | p1 | 0.5017 | **0.6889** | 0.5017 |
| S2_narrow | p2 | 0.5017 | **0.8803** | 0.5017 |
| S2_narrow | pfull | **0.6581** | **0.9432** | 0.5017 |

`task_aware_null` 在所有非零剂量随 real 同步升至 0.69–0.94（这本就是「保护任务相关路径的对照应保留效应」的设计预期，且是论文机制叙事的核心证据之一）；`L1_degree_null` 在 S1 p0 / S2 pfull 亦显著高于 chance。仅 `motif_removed` 与 `A0` 恒 ≈0.5017。**「…columns remain near chance at every dose」与落盘数据直接矛盾**。对比 r91 版：该句在 r91 中不存在（`grep` 无命中），r60 曾记录旧稿有更准确的「nulls are not everywhere at chance」措辞。因此这是**本轮为回应历史 B2 关切而新引入的、方向倒退的准确性缺陷**，且 `tab:r91repl` 上半至今只有 real 两列（`make_r91_tables.py:48-50` 只输出 `real['mean']`），B2「补 null 条件列」在表格层面**并未兑现**，仅以此不准确句代替。属呈现/事实准确性问题，非数字造假；但它把一组本应展示的反直觉 cell 概括掉了。

### 5.5 选择性呈现 / 丢弃条件列 / 负结果包装排查

- **负结果包装**：**否**。C1 失败、C3 未恢复、真实图像阴性、dense gate 失败、20 图 sign=baseline、五变量不可归因、visual-ID 不可混用、非官方 flyvis、两负面 flag，全部以削弱性限定明写；MNIST 反向 delta 并列报告；`mechanism_transfer_confirmed=false`、`expected_strong unmet` 写进摘要与结论（本轮 B3 兑现）。
- **丢弃条件列**：主矩阵 / taskaware / density / visual / r91dose 条件列完整；`tab:r91repl` 上半仍只呈 real 两列（§5.4）；`tab:r93criterion` 完整列出 3 密度层（含 high = −0.0191）与「Counterexamples retained 5 of 24」，数据未隐藏。
- **v3 反例是否被删除**：**未删除**。5 个反例逐图保存在 `metrics_v3.json::counterexamples` 与 `per_graph_errors`，表格给出计数；但主文仅写「retained and enumerated in the released per-graph evidence」，**未在主文呈现或讨论**其集中于 k12 / high 密度层（high 层 gain = −0.0191 为负）这一结构性事实。属正文化淡化的选择性呈现。
- **两次失败 trial**：见 §6.5——主文完全未提，支撑材料如实记录。
- **`expected_strong` 术语定义**：本轮主文已定义（B3 兑现），但定义与 `contract-v2.md:163-170` 不一致（§7）。

---

## 6. 本轮新增强结果（§3.5 / §4.13 v3）的科学有效性审查

这是本次评审的核心。结论先行：**v3 的数字、布尔与披露纪律完全诚实且可独立复算，但其科学增量在决定性轴上接近于零；§3.5 的「判据」是定义性重述，§4.13 的检验并未检验该判据，二者共同构成「自己出题自己考 / 近设计同义反复」。**

### 6.1 「自己出题自己考」的结构（逐条可核验）

1. **数据不是独立外部样本**：`run_r93_v3.py:10-13` 完全读取已存在的 C4 `r51_independent_family/metrics.json::results`（11-08 落盘），`make_r93_v3_protocol.py` docstring 明写 "no new training … re-analyses the 24 … already audited C4 evidence"。24 图是作者按 `4 graph seeds × 6 densities` 构造的 MaleCNS induced subgraph，Δ 来自 6 seeds 的 XOR 诊断标签，**不是自然视觉任务、不是 benchmark、不是新实验**。
2. **目标近乎由构造决定**：C4 `deltas` 全非负（`n_negative_deltas=0`），16 张 = 0、8 张 ≈ 0.499–0.503（唯一例外 g_s3_k6 = 0.0037），即**二值化**，且几乎完全由密度 k 决定（k∈{2,3,4,6}→0，k∈{8,12}→≈0.5）。`y=|deltas|` 因非负而 `abs` 冗余；`make_r93_v3_protocol.py:12-14` 自承「Sign prediction is NOT tested … degenerate」。所谓「预测 |Δ| 幅度」实质是预测「该图属于哪个密度档 / 是否可解」。
3. **「path-blind 只看全局统计」的分野被数据削弱**：本次实测 12 特征与 |Δ| 的相关性——path-aware 组最强 `motif_edges_kept`/`motif_fraction` +0.937、`reach_relay` +0.878、`conv2` +0.855、`d_reach_ab` −0.271；path-blind 组 `density` **+0.872**、`recip` +0.822、`module_density` +0.791、`in_deg_var` +0.634。即全局统计量（尤其 density，直接编码 k）与 |Δ| 的相关性**与 path-aware 最强特征相当**。两组都编码同一构造变量；0.0371 vs 0.0835 的 MAE 差距更多是 ridge 在两组特征上拟合二值目标的产物，而非「路径信息 vs 全局统计」的清晰科学分野。
4. **特征分组冻结不是数据意义上的事前**：`config_v3.json` 写死 8 path-aware / 4 path-blind 列名，相对 v3 本次**运行**是事前（SHA 冻结）；但 C4 阶段（11-08）已知这些特征与 Δ 的关系（`analysis.json` 记 `reach_b +0.9157`、`motif_edges_kept +0.9046`，12/12 BH 显著），v3（11-10）是在**已知答案之后**把「已知与 Δ 强相关的特征」划入 path-aware、「全局统计」划入 path-blind。相对数据与结论，分组是事后的：这是用已知答案设计考试。
5. **六条规则是作者自定，且含平凡可满足项**：`config_v3.json::rules` 定义 6 条；`run_r93_v3.py:53-60` 的计算显示 `rule_v`（数据有限、24 图）平凡恒真，`rule_vi` **硬编码 `True`**（脚本未做任何检查），`rule_ii` 门槛是硬编码的 `constant_baseline_mae=0.2310`（常数基线，极易超越），`rule_iv` 恰好 2/3（high 层为负）。`positive_result = all(rules.values())`（`:67`）字面成立，但真正具判别力的仅 `rule_i`（CI>0 且 mean≥0.02）与 `rule_iii`（p<0.01），且二者高度相关（同一 gain 分布）。「All six frozen rules pass」的科学分量远小于字面。
6. **§3.5 命题与 §4.13 检验不匹配**：§3.5 的 Proposition 是「C(G) sufficient for T **iff** 保留 P(T) 全部路径且只改 P(T) 外边」，其 A1–A4 已假设「标签只依赖 P(T) 上的信号」(A3)、「无 bypass」(A4)，proof sketch 基本是重述假设，属定义性/近同义反复。§4.13 检验的是「训练无关特征族对 |Δ| 幅度的预测力」，**根本不检验该 iff 的充分性或必要性**。§4.13 却据此写「It **establishes** that the standard has **judgment value** on real wiring」——从「MAE 更小」跳到「判据有判定价值 / 被验证」，是明显的逻辑跳跃与措辞偏强。
7. **§3.5 的训练前检查承诺未兑现**：`main.tex:310-317` 称「We report all three checks beside every dose and enumerate every counterexample in §\ref{sec:criteriontest}」，但 §4.13 并未呈现 oracle / leakage / 路径枚举三项检查，也未逐剂量报告；「5 counterexamples」是**预测误差反例**，与 §3.5 所说的「失效模式反例（密度补偿交换开新路径）」不是同一对象。交叉引用不实。

### 6.2 「完全事前预注册」的真实范围

- `config_v3.sha256` 三方一致，`run_v3.log` 记 "PRE-REGISTERED before any analysis | … / END_OF_RUN_OK"。
- 但根 B 时间线显示：13:33 有 v1/v2 `config.json`（`experiment=r93_local_judge`）、`trial1_failed_label_design/`；13:36 有 `trial2_failed_unlearnable_label/`；13:37 才出现 `config_v3.json` / `metrics_v3.json` / `run_v3.log`。
- `make_r93_v3_protocol.py` docstring 明写「TRIAL1/TRIAL2 local training attempts failed by design (labels not learnable) … **v3 changes the means**」；`config_v3.json::protocol_version` 明写「no new training; **replaces failed TRIAL1/TRIAL2** local training designs」。
- 因此「事前」只对**这次无训练的 reanalysis 本身**成立；相对「本轮要证明什么」这一研究问题，v3 是两次失败后改变手段的 post-hoc 转向产物。它不是一个在看到数据之前就锁定的、独立的新验证。

### 6.3 留一图-out 有无泄漏

**无泄漏**（本次复算确认）：`run_r93_v3.py:19-32` 每折标准化 `mu,sd` 只在 23 张训练图上计算，截距 `b=y[tr].mean()` 只用训练折，预测值截断 `max(0,·)`；24 折 LOGO，无图被排除（`rule_v`）。这一点设计干净，应予肯定。但「无泄漏」不等于「无循环论证」——见 §6.1。

### 6.4 反例 / 符号退化 / `positive_result` 解读

- 5 反例**未删除**，逐图保存在 `metrics_v3.json`；表格给出 `5 of 24` 与 high 层 −0.0191。
- 符号退化**如实保留**：§4.13 明写「The original 24-graph sign criteria remain false (all deltas are non-negative, so sign prediction is degenerate)」、`independent_family_validated` remains false、real-image result remains negative；`metrics_v3.json::retained_negative_facts` 与 `honesty` 段同。C4 `criteria` 实测 `i_signs_not_all_same=false`、`ii_sign_agreement_margin=false`、`iii/iv=true`；`n_negative_deltas=0`。
- **`positive_result=true` 是否被过度解读为「拓扑有利于视觉」**：**否，且稿件明确反向设限**。§4.13 逐字写「It does **not** establish that connectome topology benefits natural visual computation … We do **not** claim improved visual accuracy」；摘要只作中性事实陈述「path-aware features predict the magnitude … better than global statistics (MAE 0.0371 vs 0.0835; p=0.001)」。这是本轮最值得肯定的诚实点，按用户指令**不因披露本身加分**。
- 但需保留两点保留意见：(a) `positive_result=true` 的科学语义被 `positive_result` 这一命名与摘要头条位置放大，而它实际仅等于「6 条自定规则的合取」；(b) 5 个反例恰好集中在 k12 / high 密度层、且 high 层增益为负（−0.0191），正文以「positive in two of three density strata」淡化、未点名这是「效应最大、最明显的一类图上，全局统计反而预测得更好」——这削弱了「路径感知特征必要」的普适性论断，主文未讨论。

### 6.5 两次失败 trial：隐瞒还是包装

- **未包装成正面结果**：`main.tex` 全文 `grep -niE 'trial|cifar|reanaly|no new training|unlearnable|label design'` 仅命中 §4.8 一处「not an unlearnable label」（指 oracle MLP，与 trial 无关）。两次失败训练**根本没有进入稿件**。
- **但构成主文选择性叙事**：`trial1/run_console.log`（CIFAR-10，Δ 恒 +0.0000，v2 config 自承「class-parity XOR was not a function of image content; deltas were identically zero」）、`trial2/run_console.log`（Δ 仍恒 +0.0000，标签不可学）表明，本轮**最初尝试做的正是历史评审反复点名的决定性实验——真实视觉任务（CIFAR-10）上「judge visual claims」的正向验证**；两次失败后，`config_v3` 放弃训练、把问题换成「XOR 诊断标签 Δ 幅度预测」。摘要却把这一退守后的 reanalysis 作为新的正向头条，读者无从得知其来源与失败谱系。
- **公允记录**：失败在**支撑材料中是如实留痕的**（`config_v3.json::protocol_version`、`make_r93_v3_protocol.py` docstring、两个 trial 目录日志原样保留），并非从所有 artifacts 中抹除；问题在主文对方法转向保持沉默。按研究诚信标准，CVPR 主文通常不必报告每次失败预实验，但当「本轮唯一新增正向结果」恰由该失败转向而来、且摘要将其作为头条时，不披露会实质影响读者对证据独立性的判断。记为 B/C 类选择性呈现，非造假。

### 6.6 本轮新增内容逐项净影响（回答「是否真正改变证据强度」）

| 新增项 | 性质 | 对决定性轴的净影响 |
|:---|:---|:---|
| §3.5 形式化判据 P(T)/A1–A4/命题 | 定义性重述（A3/A4 已含结论），未导出非平凡可证伪预测 | **无**。表面兑现了 r91「给出形式化判据」的升分条件，但判据本身近同义反复，§4.13 未检验其 iff |
| §4.13 v3 判据检验 `positive_result=true` | 无新训练的 C4 数据 reanalysis；近设计同义反复；自定规则含平凡项 | **无**。未跳出受控 XOR 诊断标签体制；对「真实视觉正向拓扑效应」零新增证据 |
| 边界实验重组 scope 表 | 呈现级（无新测量） | 无；且引入 1 个 Overfull |
| 摘要压缩 | 呈现级 | 无；仍信息密集，且新增 MAE/p 头条 |
| `p2==pfull` 解释 | 呈现级（兑现 B1） | 无（正确的可读性修复） |
| `expected_strong` 主文定义 + 两负面 flag 入摘要/结论 | 呈现级（兑现 B3），但定义与 `contract-v2.md` 不一致（§7） | 无 |
| C1c null 条件列说明 | 呈现级（名义兑现 B2） | **负**：新引入与数据矛盾的陈述（§5.4） |

**综合判定**：本轮**绝大多数新增是呈现/披露级修补**（按用户指令，不抬高由证据决定的总分）；唯一两项「实质」新增（§3.5 判据、§4.13 正向结果）在决定性轴上**没有改变证据强度**——决定性实验（真实视觉正向结果）本轮被尝试过、两次失败、随后放弃，中心正向结论仍限于受控诊断标签且近设计同义反复。更严格地说，本轮还新引入 2 个准确性/格式缺陷与 1 个主文隐瞒，内部一致性略有下降。因此「本轮新增内容真正改变证据强度」的答案为**否**。

---

## 7. 科学性与统计核验

| 核验点 | 结论 | 依据 |
|:---|:---|:---|
| 配对 bootstrap | 通过 | 主矩阵 / r91 表 / v3 均 R=5000、percentile CI、`default_rng(20261110)`；本次按同顺序复现 `tab:r91repl` 的 0.4415/0.4390 与 weak/strict/task-aware CI |
| BH 校正 | 通过 | `benjamini1995` 悬空已闭合；主矩阵 q=0.0002、tab:taskaware q=0.00032/0.40 可溯源 |
| sign-flip 置换 | 通过 | v3 1000 次 sign-flip，本次复现 p=0.001；C1c `p_signflip`/`p_BH` 逐条在案 |
| 10 seeds / 6 seeds | 通过 | 主矩阵/剂量 10 冻结种子 `{11,…,103}`（`contract-v2.md:155`）；C4 `config.seeds.n_train_seeds=6`、density/visual 6 seeds，口径未混用 |
| 共享初始化 | 通过 | C1c `preflight.shared_init_same_seed_equal=true`、`shared_init_diff_seed_differ=true`、`W_rowsum_one=true` |
| oracle / leakage 探针 | 通过且如实保留失败 | C1c oracle 0.9991、leakage ≈0.50；§4.2 三种子预检 `FAILED`（0.7891 vs 0.80 探针缺陷）不重贴标签；`metrics_multisubgraph.json::decision_rules` 七条全 True |
| 剂量单调性 | 通过且分层清楚 | C1 `hypothesis_supported=false`（非单调）；C1b `hypothesis_supported_pathblock=true`（单调）；C1c 两子图各四档单调、`cross_subgraph_replicated=true`、`p2_ne_pfull=true` |
| `p2==pfull` 解释 | 通过（本轮 B1 兑现） | `tab:r91dose` 下半 p2/pfull 两行全等（0.9772/0.5017/0.9794/0.5004）；`main.tex:613-615` 明写「|P_all|=2 ⇒ 同一张图、三档剂量，复制移除该退化」 |
| 跨运行 visual-ID 口径 | 通过 | §4.8 / Limitations 明写 9,766 / 29,442 / 29,564 IDs 不可混用、绝对边数不可 pool |
| 等价复实现非官方 flyvis | 通过 | §Discussion「We did not rerun their flyvis stack and make no benchmark-reproduction claim」；C3 称 "faithful rerun of the published control ladder" 但未冒称官方复现 |
| `mechanism_transfer_confirmed=false` | 通过（flag 属实） | `r51_strong_baseline/metrics.json::decision.mechanism_transfer_confirmed=false`；摘要、§4.15、Conclusion 三处明写 |
| `expected_strong` 未达成写进摘要/结论 | **字面达成，但定义漂移** | 摘要 `main.tex:47-48`「conjunctive `expected_strong` target remains unmet」、Conclusion `:738`「`expected_strong` unmet」；§3.5/§4.0 定义「三项合取： strictly monotone localising ladder + reproduced motif-survival threshold + confirmed mechanism transfer」。对照 `contract-v2.md:163-170` 落盘定义实为**四项合取**：`hypothesis_supported=true` 剂量判据（full≥0.75 / p0≤0.60 / nulls≤0.60 / task-aware≥0.75 / CI>0）+ weak-control 优势被 strict 移除、被 task-aware 恢复 + independent-family LOGO sign ≥ majority+0.15 且 ≥3 特征 BH q<0.05 + clean main matrix 全门禁。两者**不一致**；且稿件把「strictly monotone localising ladder」列为合取项，与论文自述 outcome (iii)「ladder 无定位力」自相矛盾——按稿件定义该目标在观察结果下从设计上即不可能达成。属术语可复核性缺口（B/C 类），不影响 `unmet` 结论本身 |
| 两负面 flag 是否写进摘要与结论 | 通过（本轮 B3 兑现） | 摘要与 Conclusion 均含 `mechanism_transfer_confirmed=false` / `expected_strong` unmet 字面 |

**科学性结论**：统计设计在本类 diagnostic 研究中属上乘，预注册/adaptive 分层诚实，`p2==pfull` 与本轮 flag 呈现缺口已修。核心科学边界未变——所有**正向**机制证据都落在受控 XOR 诊断标签上；真实视觉任务上的正向拓扑效应从未建立（§4.8 阴性、C3 未复现、transfer=false、本轮 CIFAR-10 尝试失败）。

---

## 8. CVPR 2027 合规核验（独立复核，不采信 `submission-constraints.md` 自评）

| 约束 | 核验 | 结果 |
|:---|:---|:---|
| 8 页正文（含图表） | pypdf 9 页；p1–p8 主文；p8 完整 Conclusion 收尾末句「…explains conflicting reports.」；逐页字符数 p1–p9 = 4873/5700/6535/6550/5096/6173/6960/4977/3144 | PASS |
| 额外页仅 References + 强制 LLM Usage Statement | p9 全文 = review 水印 + `LLM Usage Statement` + `[To be supplied by the authors.]` + `References` [1]–[15]，`Conclusion/Discussion/Experiments/4.13/4.15/MAE/hypothesis_supported/density_isolated` 关键词 0 命中 | PASS（内容合规） |
| 强制 LLM Usage Statement 有实质内容 | `main.tex:747-748` 为占位符 | **FAIL / BLOCKER**（class B，desk-reject 级行政风险；按作者指令不加权科学总分） |
| 双盲 | `\author{Anonymous}` / `\paperID{*****}` / 无身份链接 / 第三人称引用最近前作 | PASS |
| 题录无外链 | `main.bib`/`main.bbl`/`main.tex` 对 `http/url/href/www` 计数 0；15 `@` = 15 `\bibitem` | PASS |
| `main.log` 0 undefined refs | `undefined` / `Citation…undefined` / `LaTeX Warning` / `^!` / `Emergency` = 0 | PASS |
| `main.log` 0 Overfull | **1 个** `Overfull \hbox (136.25835pt too wide) in paragraph at lines 6--14`，来源 `tables_r93_scope.tex`；r91 版为 0 | **FAIL**（本轮新增 scope 表引入；格式缺陷，不加权科学总分） |
| 官方 `cvpr.sty` / 10pt / 双栏 | `\documentclass[10pt,twocolumn,letterpaper]{article}` + `\usepackage[review]{cvpr}`；`preamble.tex` 仅 `\linespread{0.84}` | PASS |
| 注入 / 隐藏操纵 | 0 命中 | PASS |

**合规结论**：科学格式几乎全通过；两处硬伤——LLM Statement 占位符（行政 blocker）与本轮新增的 1 个 Overfull。按用户指令，**二者不参与抬高或压低由证据决定的科学总分**，但独立地使当前包件「不可直接提交」/「编译非零告警」。

---

## 9. 7 人独立 Reviewer Panel（综合前各自独立给分）

> 每位评审在综合前独立成块，不强制一致 / 分歧 / 赞扬 / 拒稿；分数为各角色独立倾向（1–10），AC 不取平均。

**R1 · Best-Justified Reviewer**（evaluation methodology / negative-result 倡导者）
- Expertise：评估方法学、可复现性审计 ｜ Likely score：**7.0** ｜ Confidence：4
- 正面：数字零造假、全链路可复算（本人从 C4 原始数组复现 v3 全部 MAE/CI/p/规则，最大误差 3.3e-16）、统计严谨、C1c 完全事前两独立真实子图七规则全通过、负结果与失败全保留、scope 边界清晰、本轮把两负面 flag 写进摘要/结论与 `p2==pfull` 解释是真实可读性修复
- 负面：仍缺真实视觉正向用例；本轮 CIFAR-10 尝试失败后未在主文披露
- Evidence basis：§5、§7、`metrics_multisubgraph.json`、`metrics_v3.json`
- Fatal concern：无 ｜ Score-change condition：补一个真实视觉任务上经严格 null 对照、配对 CI 排除零的正向效应 → 7.5–8

**R2 · Critical Reviewer**（CVPR 视觉主会 senior reviewer）
- Expertise：CVPR 主会 / connectome-constrained vision ｜ Likely score：**3.5** ｜ Confidence：5
- 正面：统计严谨、无造假、诚实披露（不否认）
- 负面：venue mismatch——无 image benchmark、无自然视觉任务、visual evidence 全为合成/诊断图；非图 MLP 0.9722 主导；C3 未复现 task-aware recovery（DiD −0.0477 CI 含 0）；`mechanism_transfer_confirmed=false`；核心结论是「control 构造决定观测」，对视觉受众无新知识。本轮「正向结果」经核验是 C4 数据 reanalysis、近设计同义反复，且决定性实验两次失败后放弃
- Evidence basis：`main.tex:88-91`、§4.8、§4.13、`r39_visual_task/metrics.json`、`r51_strong_baseline/metrics.json`、trial 日志
- Fatal concern：主张与 venue 经验验证标准不匹配（可独立支撑拒稿）
- Score-change condition：真实视觉任务正向结果 + 结论改写 → 5.5–6

**R3 · Method / Soundness Reviewer**（图学习 / 因果推断 / 预注册）
- Expertise：实验设计、预注册、统计有效性 ｜ Likely score：**5.5** ｜ Confidence：5
- 正面：Eq.(1) 主动限定为上界直觉；shared-init、配对 CI、sign-flip、不变量断言；v3 LOGO 无泄漏（标准化仅训练折）；`config_v3.sha256` 三方一致
- 负面：**§3.5 命题是 A1–A4 的定义性重述，§4.13 检验的 MAE 幅度预测并不检验该 iff**（逻辑跳跃）；v3 六条自定规则含 `rule_vi` 硬编码 True、`rule_v` 平凡；特征分组在已知 C4 相关性后构造；§3.5 承诺的 oracle/leakage/路径枚举「beside every dose」在 §4.13 未出现；**r93 新引入「null columns remain near chance」与 `task_aware_null` 0.69–0.94 直接矛盾**；`expected_strong` 主文定义与 `contract-v2.md` 不一致且与 outcome (iii) 张力；C1b adaptive 谱系、C1c 脚本 SHA 事后变更、三种子预检 FAILED
- Evidence basis：`main.tex:291-317`、`631-657`、`615-616`、`322-326`、`run_r93_v3.py:53-60`、`metrics_multisubgraph.json::per_dose`、`contract-v2.md:163-170`
- Fatal concern：无（mostly sound，但本轮内部一致性下降） ｜ Score-change condition：修正矛盾陈述、把 §3.5 判据改为可证伪预测并真正检验、补无筛选第三子图 → 6.5

**R4 · Evidence / Experiment Reviewer**（baselines / ablations / 统计功效）
- Expertise：实验审计、消融、鲁棒性 ｜ Likely score：**5.5** ｜ Confidence：5
- 正面：10/6 seeds、BH、剂量、两子图、忠实复跑、C5 六门禁全在案；v3 数字逐格可溯源、5 反例与负增益层（high −0.0191）在表中列出
- 负面：正向机制仅在 96 节点受控 XOR；C4 Δ 二值化（16×0 / 8×≈0.5）由构造决定；path-blind 全局统计与 |Δ| 相关性同样高（density +0.872），分野模糊；sign=baseline；`tab:r91repl` 上半 null 条件列至今未补；5 反例集中在 k12 且主文未讨论；两次失败训练未在主文披露
- Evidence basis：§5.1/§5.3/§5.4/§6.1、`r51_independent_family/metrics.json`、`make_r91_tables.py:48-50`
- Fatal concern：无 ｜ Score-change condition：C1c 主文补 null 列 + 操纵外独立图族 + 真正的外部验证 → 6.5

**R5 · Novelty / Positioning Reviewer**（network null models / GNN evaluation）
- Expertise：connectome-constrained 视觉 / 零模型 ｜ Likely score：**4.0** ｜ Confidence：4
- 正面：把 null 生成器当作一等实验变量、机器校验不变量标准，是有价值的 framing；与 `toposens2026` 定位诚实
- 负面：构件均属既有（degree-preserving、triad census、XOR 合成任务）；`toposens2026` limitations 已点名 higher-order nulls/longer horizon/更广任务；本轮 §3.5「形式化判据」是定义性重述、未导出改变已发表结论的非平凡预测，§4.13 也不构成对该判据的独立验证 → 新颖性未实质提升；venue fit 方法学而非视觉
- Evidence basis：`main.tex:149-156`、§3.5、`contract-v2.md` Core Idea
- Fatal concern：无（未坍塌） ｜ Score-change condition：给出并验证一个非平凡可证伪预测，或被第三方采用 → 5.5

**R6 · Writing / Clarity Reviewer**（科技写作 / 可恢复性，含 Novice Advocate）
- Expertise：贡献可恢复性 / 图表可解释性 ｜ Likely score：**5.0** ｜ Confidence：5
- 正面：六节规范、术语稳定、claim-evidence 可见；scope 表、`p2==pfull` 解释、`expected_strong` 定义、两 flag 入摘要/结论是本轮真实呈现改善；`tab:r93criterion` 表完整列出 high 负增益与反例计数
- 负面：摘要仍过密（新增 MAE/p 头条）；§4.6「which we do not provide」与 §4.13「24 non-manipulated graphs」措辞张力；§3.5 交叉引用不实；「positive in two of three strata」正文未点名 high 为负、5 反例只在 released evidence；题录/内部代码标识符入正文（历史残留）；本轮新增 1 个 Overfull（scope 表过宽）
- Evidence basis：`main.tex:25-53`、`310-317`、`493-494`、`631-657`、`tables_r93_scope.tex`、`main.log:520`
- Fatal concern：无 ｜ Score-change condition：摘要再压缩、统一 §4.6/§4.13 措辞、主文呈现 5 反例与 high 层、修 Overfull → 6.0（维度内）

**R7 · Ethics / Reproducibility Reviewer**（研究诚信 / artifacts / policy）
- Expertise：research integrity、artifact auditing、venue policy ｜ Likely score：**7.0** ｜ Confidence：5
- 正面：负结果 / 失败 / adaptive / scope / 跨运行口径 / 非官方 flyvis / 两负面 flag / 数据许可全披露；`config_v3` 与 `make_r93_v3_protocol.py` **如实记录**两次失败 trial 并说明 v3 取代之、日志原样保留；v3 `honesty` 与 `retained_negative_facts` 段完整；config/script SHA、per-seed 数组、运行时生成表齐备；零外链、双盲、零 undefined refs
- 负面：**主文对两次失败训练 → reanalysis 的方法转向保持沉默**，而摘要把退守结果作正向头条，构成选择性叙事；本轮新引入 1 句与数据矛盾的陈述；LLM Statement 占位符；工件仅在本地运行根、非公开匿名发布
- Evidence basis：§6.5、§5.4、`config_v3.json::protocol_version`、两个 trial 目录、`main.tex:747-748`
- Fatal concern：无 ｜ Score-change condition：主文补一句披露失败转向 + 修正矛盾陈述 + 补 LLM 声明 → 7.5（**仅该维**，不改由证据决定的总分）

**Panel Synthesis**
- **Agreement**：七人一致认定证据内部自洽、全链路可核验、诚实披露、无造假、无致命缺陷；一致同意「真实视觉正向证据缺失 + venue fit」是最强关切；一致认为本轮 §4.13 正向结果**未**改变决定性证据强度。
- **Disagreement**：R1（7.0）与 R2（3.5）分歧最大，根源是「方法论严谨的负结果是否足以满足 CVPR 视觉主会的经验验证门槛」，而非事实认定差异；R3/R4 强调 v3 的自定规则与数据二值化使其科学增量有限，R5 强调 §3.5 判据是定义性重述。
- **Decisive positive axis**：C1c 完全事前、两独立真实子图、七规则全通过；全链路数字/SHA 可核验；统计纪律；负结果与失败全保留；本轮两负面 flag 入摘要/结论。
- **Decisive negative axis**：真实图像任务阴性 + C3 未复现 task-aware recovery + `mechanism_transfer_confirmed=false` + `expected_strong` unmet；本轮决定性实验（CIFAR-10）两次失败后放弃；v3 是近设计同义反复的 C4 reanalysis；核心正向主张始终停留在受控 XOR 诊断标签内。
- **Unresolved evidence**：真实视觉任务/已发表管线上的 path-aware 阳性验证；官方 flyvis 复现；带符号方差的独立图族；`expected_strong` 定义与合同不一致；两次 trial 失败原因未重跑验证；2026 题录真实性（未联网）。
- **AC stance**：不取 panel 均值（≈5.36）；按最强未解决关切定档，见 §11。

---

## 10. AC / Meta-Review

- **Reviewer consensus**：方法与统计扎实、数字零造假、诚实度与复现性远超平均；这不是「做坏了」的论文，而是「证据边界被作者自己严格划死」的论文。本轮新增内容在文本 / 数据 / SHA / PDF 分页四层均真实落地，但**绝大多数是呈现/披露级修补**，按任务指令不抬高由证据决定的总分。
- **本轮最关键的新事实**：作者本轮**确实尝试**去补历史评审反复点名的决定性实验（CIFAR-10 真实视觉任务上 judge visual claims），但 `trial1`（标签设计错误、Δ 恒 0）与 `trial2`（标签不可学、Δ 仍恒 0）两次本机训练失败；`config_v3` 随即改为 "no new training; replaces failed TRIAL1/TRIAL2"，退回对已审计 C4 数据的 reanalysis。因此「决定性缺口」不仅未动，而且被本轮再次实证为「尝试过、未走通、未在主文披露」。
- **Decisive acceptance axis**：C1c 的完全事前两子图复制 + 全套可核验工件 + 严格 scope，足以支撑「可复用的 control-sufficiency 诊断标准」这一方法论贡献。
- **Decisive rejection axis**：真实视觉任务上无任何正向拓扑效应、C3 未恢复、`mechanism_transfer_confirmed=false`；对视觉会议，significance 与 visual evidence 是硬门槛；v3 正向结果经独立复算虽诚实，却是「自己出题自己考」。
- **AC stance / 分数来源**：borderline，略偏 negative。**明确声明**：分数偏低**不是**因为论文披露负结果或写了削弱自身主张的限定（若隐藏这些，Evidence/Ethics 更低并触发诚信问题）；也**不是**因为格式/披露修补（含本轮 scope 表、摘要压缩、`p2==pfull` 解释、两 flag 入摘要、LLM 占位符、1 个 Overfull）被抬高或压低。压分来自三个**证据性**事实：(a) 正向机制仅成立于受控 XOR 诊断标签；(b) 真实视觉正向效应从未建立，且本轮决定性实验两次失败后放弃；(c) 对 CVPR 视觉受众的 significance 有限；(d) 本轮唯一新增正向结果是同义反复式 reanalysis，未改变 (a)–(c)。本轮新引入的 1 处矛盾陈述、1 个 Overfull、1 个主文隐瞒属呈现/准确性缺陷，如实计入 Soundness / Clarity / Ethics 维度，但不作为大幅压低由证据决定总分的杠杆。
- **Discussion risks**：R1 与 R2 的 3.5 分落差可能被「负结果方法论价值」与「venue fit」两种立场放大；建议以 §16 的单一决定性实验作为收敛判据，而非措辞辩论。

---

## 11. 七维 Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis（可核验引用） | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 3 | 5 | `main.tex:149-156`（自承 `toposens2026` 已点名 higher-order nulls/longer horizon/更广任务）；§3.5 `main.tex:291-317`；Related Work 全部构件为既有 | **≤3 扣分**：嵌套度保持随机化、triad census、motif 存活计数、XOR 合成任务均为已知组件增量组合；本轮 §3.5「形式化判据」的 A1–A4 已假设「标签只依赖 P(T)」「无 bypass」，命题 proof sketch 为重述假设，属定义性/近同义反复，未导出非平凡可证伪预测；§4.13 亦未检验该 iff。**升 4 条件**：给出并验证一个改变已发表结论的非平凡预测，或被第三方采用；否则维持 3 |
| Soundness | 3 | 5 | `main.tex:615-616` vs `metrics_multisubgraph.json::per_dose`（task_aware_null 0.69–0.94）；`main.tex:291-317/631-657` 逻辑错位；`run_r93_v3.py:53-60`（rule_vi 硬编码 True）；`contract-v2.md:163-170` vs `main.tex:322-326` | **≤3 扣分**：(i) 本轮新引入「null columns remain near chance at every dose」与落盘数据直接矛盾；(ii) §3.5 判据与 §4.13 检验对象不匹配、§3.5 承诺的 oracle/leakage/路径枚举未在 §4.13 出现；(iii) v3 六规则含平凡恒真项（rule_vi 硬编码）；(iv) `expected_strong` 主文定义与合同不一致且与 outcome (iii) 张力；(v) C1b adaptive 谱系、C1c 脚本 SHA 事后变更、三种子预检 FAILED（历史保留）。**升 4 条件**：修正矛盾陈述、把判据改为可证伪预测并真正检验、定义对齐合同；**升 5** 另需补无筛选第三子图 |
| Evidence | 4 | 5 | §5 全表对账；本次从 C4 原始数组完整复现 v3（误差 3.3e-16）；`make_r91_tables.py` / `make_r93_tables.py` 运行时读数；`metrics_multisubgraph.json` 七规则；`metrics_v3.json` 5 反例 / high −0.0191 | 证据包完整、可核验、负结果全保留，但中心决策相关断言缺外部验证：`mechanism_transfer_confirmed=false`、真实视觉任务全阴性、C4 符号判据 FAIL、本轮 CIFAR-10 决定性实验失败；v3 是已有数据 reanalysis 而非独立新证据。**升 5 条件**：在自然视觉任务/已发表管线上确认 path-aware 对照改变结论；**降 2**：任一头条数字与 `metrics.json` 不符（本次已排除） |
| Significance | 3 | 4 | `main.tex:88-91`（no image benchmark / no natural visual task / no improved accuracy）；§4.8（MLP 0.9722 主导、deg-null=real、MNIST 反向 delta）；§4.15；`venue-review-styles.md` CVPR 段 | **≤3 扣分**：对窄社区有用，对 CVPR 视觉受众影响有限且负向；真实视觉任务拓扑特异性阴性；核心贡献是对 96 节点受控替身的协议诊断；本轮决定性实验（真实视觉正向结果）两次失败后放弃。此为**最强未解决关切，不得被维度均值抹平**。**升 4 条件**：至少一个真实视觉任务上经严格 null 对照、配对 CI 排除零的正向效应；此为决定性实验 |
| Clarity | 3 | 5 | `main.tex:25-53`（摘要过密）、`310-317`（交叉引用不实）、`493-494` vs `638-639`（措辞张力）、`647-648`（反例只在 released evidence）；`tables_r93_scope.tex` + `main.log:520`（1 个 Overfull） | 可理解但需费力；本轮 scope 表 / `p2==pfull` / 术语定义 / 两 flag 是真实改善，但同时新增摘要 MAE 头条、1 句不准确陈述、1 个 Overfull，且 `tab:r91repl` 上半 null 列至今未补。**升 4 条件**：修正矛盾陈述、统一 §4.6/§4.13 措辞、主文呈现 5 反例与 high 负增益层、修 Overfull、再压摘要 |
| Reproducibility | 5 | 5 | `config_v3.sha256` 三方一致；`metrics_v3.json::per_graph_errors` 可逐图复算；`make_r93_tables.py` / `make_r91_tables.py` 运行时读数；28 类 config/script SHA 历史可核验；10×5 / 6-seed per-seed 数组、失败日志、只读对照留存；`main.log` 零 undefined refs | clear strength。**保留项**：工件仅在本地运行根、非公开匿名发布；18017 CRC 缺陷由 C5 缓解；C1c 脚本 SHA 变更已披露；本轮 1 个 Overfull 属格式而非证据可复现性。**降 3**：公开发布审计失败或任一哈希不符 |
| Ethics / Limitations | 4 | 5 | `config_v3.json::protocol_version` + `make_r93_v3_protocol.py` docstring（如实记录两次失败）；两个 trial 目录日志原样保留；`metrics_v3.json::retained_negative_facts/honesty`；摘要/Conclusion 两负面 flag；`main.bib` CC-BY 4.0、无受试；LLM Statement 占位符 | **≤4 扣分**：负结果/失败/范围/可比性/许可/两 flag 全披露、v3 明确否认「拓扑有利于视觉」，纪律仍属强；但**主文对本轮最关键的方法转向（两次失败训练 → reanalysis）保持沉默**，而摘要把退守结果作正向头条，构成选择性叙事；且本轮新增 1 句与数据矛盾的陈述。**按任务规则：该维度分不单独抬高 Overall；高分亦非因「披露负结果」这一行为本身**。**争议空间**：若严格审稿人视「失败预实验非主文必须披露项」成立，可维持 5 上沿；本报告按「摘要将退守 reanalysis 作正向头条」的语境判为 4 |

**Overall:** 5.2  | **Scholarly Confidence:** 4.6

**Recommendation:** borderline（lean-negative）；不建议以当前形态直接投 CVPR 2027 主会，除非补齐 §16 的决定性实验；行政上须先解决 LLM Statement 占位符（及 enrollment / reciprocal-reviewer quota）方可提交。
**Verdict:** 由最强未解决关切（真实视觉正向证据缺失 + venue fit + 中心结论限于受控 XOR 诊断标签）定档，**不取七维均值**（七维 `(3,3,4,3,3,5,4)` 机械线性换算约 7.1，按 `review-output-standards.md` 的「不得平均掉致命关切」明确弃用）；本轮呈现/披露修补、格式合规、诚实披露不抬高由证据决定的总分。升 1 分需「真实视觉任务上经严格 null 对照验证的正向拓扑效应 + §3.5 判据被独立检验 + 修正矛盾陈述」；降 1 分触发于「更细核验发现任一头条数字或 `positive_result` 规则判定与落盘 metrics 不符，或发现负结果/失败被系统性隐藏」。

---

## 12. Concern-to-action 表

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
|:--|:---|:---|:---|:---|:---|:---|:---|:---|
| A1 | **major（决定性）** | 真实视觉任务无正向、经严格 null 对照验证的拓扑效应；venue fit 弱；本轮 CIFAR-10 决定性实验两次失败后放弃 | §4.8 / §4.15、`r39_visual_task`、`r51_strong_baseline::decision`、两个 trial 日志 | Significance / Evidence | requires-new-result | 见 §16 主实验 | 实验 owner | 补出严格 null 对照的正向结果 → Significance 3→4、总分约 +0.8 |
| A2 | major | 中心正向结论限于受控 XOR 诊断标签、近设计同义反复；v3 reanalysis 未改变决定性轴 | §3.1/§3.5/§4.13、`run_r93_v3.py:10-13`、C4 `deltas` 二值 | Novelty / Soundness / Significance | requires-new-method | 把 §3.5 判据改为非平凡可证伪预测并真正检验；或在已发表视觉管线上验证 | 实验 owner / `ccf-paper-writer` | 判据导出并验证非平凡预测 → Novelty 3→4、Soundness 3→4 |
| A3 | major | C3 未复现 task-aware recovery、transfer=false、`expected_strong` unmet | DiD −0.0477[−0.1056,0.0120]；`mechanism_transfer_confirmed=false` | Soundness / Evidence | claim-qualification | 结论「This establishes …」下修为「within controlled diagnostic label」；或补跨任务转移证据 | `ccf-paper-writer` | 措辞对齐后 Soundness +0.5；补证据则 Evidence 4→4.5 |
| A4 | moderate | 本轮新引入与数据矛盾陈述（null 列 near chance） | `main.tex:615-616` vs `metrics_multisubgraph.json::per_dose` | Soundness / Clarity | figure/table + claim-qualification | 删除/改写该句；`tab:r91repl` 上半补 null 条件列（含 S1 p0 0.6742/0.7032、S2 pfull 0.6581）或正文如实讨论 | `ccf-paper-writer` | 修正后 Soundness 3→3.5、Clarity 3→3.5（维度内） |
| A5 | moderate | 主文未披露两次失败 trial → reanalysis 的方法转向；摘要把退守结果作正向头条 | 两个 trial 目录、`config_v3.json::protocol_version`、摘要 `main.tex:49-52` | Ethics / Evidence | disclosure | 主文补一句：本轮真实视觉训练尝试未成功，§4.13 为对已审计 C4 数据的事前冻结重分析 | `ccf-paper-writer` | Ethics 4→4.5（维度内，不加权总分） |
| A6 | moderate | `expected_strong` 主文定义与 `contract-v2.md:163-170` 不一致，且与 outcome (iii) 张力 | `main.tex:322-326`、`main.tex:108`、`contract-v2.md:163-170` | Soundness / Clarity | claim-qualification | 定义对齐落盘合同，或明确标注为主文简化表述 | `ccf-paper-writer` | Soundness / Clarity 维度内 +0.5 |
| B1 | moderate | `tab:r91repl` 上半只呈 real 两列；5 反例只在 released evidence、high 层 −0.0191 未在主文讨论 | `make_r91_tables.py:48-50`、`tables_r93.tex`、`metrics_v3.json::counterexamples` | Evidence / Clarity | figure/table | 补 null 列；主文呈现 5 反例集中于 k12 / high 层这一结构性事实 | `ccf-paper-writer` | Evidence 4→4.5（呈现完整后） |
| B2 | moderate | §3.5 交叉引用不实（oracle/leakage/路径枚举未「beside every dose」出现在 §4.13）；§4.6 与 §4.13 措辞张力 | `main.tex:310-317`、`493-494`、`631-657` | Clarity | claim-qualification | 改写交叉引用；统一「非操纵图族」口径 | `ccf-paper-writer` | Clarity 3→3.5 |
| B3 | minor | 摘要过密、题录/内部标识符入正文（历史残留） | `main.tex:25-53`、§5 | Clarity | compression | 再压摘要、清理正文内部代码标识符 | `ccf-paper-writer` | 仅 Clarity 维度内 |
| C1 | **fatal（行政）** | LLM Usage Statement 为占位符 | `main.tex:747-748`；`submission-constraints.md` class B | 合规（非科学维度） | ethics/limitations | 作者补声明 → 重编译 → 刷 hash → 复核 p9；确认 enrollment / reciprocal-reviewer quota | 作者（门户侧） | **不改变科学总分**；仅决定是否可提交 |
| C2 | minor（格式） | `main.log` 1 个 Overfull（新增 scope 表 136pt 溢出） | `main.log:520`、`tables_r93_scope.tex` | 合规（非科学维度） | figure/table | scope 表改 `\footnotesize` / `tabularx` / 两栏拆分后重编译 | `ccf-paper-writer` | **不改变科学总分**；仅消除编译告警 |
| C3 | — | 未核验项见 §15 | — | Confidence | — | 见 §15 | — | 影响置信度，不自动改分 |

> 所有 ≤3 的维度均在 §11 给出具体扣分与修复条件；C1/C2 为行政/格式，按用户指令不参与科学总分加权。

---

## 13. Score-Change Conditions 与两方向 Tie-breaker

| Change | Condition | Likely affected dimensions | Expected movement |
|:---|:---|:---|:---|
| **Raise score** | 在真实自然视觉任务 / 已发表视觉管线上，经 no-graph / degree-preserving / task-aware 三类严格 null 对照、10 seeds、配对 bootstrap CI 排除零，证明「保护任务相关路径的图显著优于不保护的 null」，并同时报告非图 MLP 强基线；据此把结论从「control 构造决定观测」扩展为「该标准可判定真实视觉主张」 | Significance 3→4、Evidence 4→5、Soundness 3→4 | **+0.8 至 +1.0 overall**（进入 6 区间） |
| **Raise score（小）** | 修正 §4.15 矛盾陈述、`tab:r91repl` 补 null 列、主文披露两次失败转向、§3.5 定义对齐合同、主文呈现 5 反例与 high 负增益层、修 Overfull | Soundness 3→4、Clarity 3→4、Ethics 4→4.5 | **+0.2 至 +0.3 overall**（维度为主；按用户指令，纯呈现/披露/格式修补**不**抬高由证据决定的总分，此 +0.2–0.3 仅来自矛盾陈述修正这一事实准确性项） |
| **Lower score** | 更细核验发现任一头条数字、`positive_result` 六规则或 `cross_subgraph_replicated` 与落盘 `per_seed`/`per_graph_errors` 不一致；或发现负结果/失败被系统性隐藏；或 2026 题录任一被证虚构（class C） | Soundness、Evidence、Ethics、Reproducibility | **−0.5 至 −1.0 overall 或 fatal** |
| **No quick change** | 真实视觉 transfer 未确认、C3 task-aware 未恢复、20 图 sign=baseline、C4 符号判据 FAIL、本轮决定性实验失败——这些需新实验/新任务/新图族，非措辞可解 | Significance、Evidence | 提交前 unlikely 改变 |
| **No quick change** | 继续补流程 / 披露 / 格式（scope 表、摘要压缩、`p2==pfull`、两 flag 入摘要、补 LLM 声明、修 Overfull、统一口径）不会再抬高总分 | — | 不改变 evidence-capped overall |

**两个方向的 tie-breaker**

- **向 6（borderline positive）拉的力**：数字零造假、全链路可复算（本人从 C4 原始数组复现 v3 全部 MAE/CI/p/规则，3.3e-16）、统计严谨（10/6 seeds / shared-init / 配对 bootstrap R=5000 / BH / 1000 sign-flip / oracle-leakage 探针）、C1c 完全事前且两独立真实子图七规则全通过、负结果与失败全保留、CVPR 分页合规（p8 完整 Conclusion / p9 仅声明+参考文献）。这些是**真实的方法论 merit，不是披露加分**，把分数从 4 侧托起。
- **向 4（lean reject）拉的力**：CVPR 视觉主会缺真实视觉正向验证与 visual evidence；C3 未复现 task-aware recovery（DiD CI 含 0）；`mechanism_transfer_confirmed=false` / `expected_strong` unmet；sign prediction = 多数类基线；核心贡献是对实验方法的负面/方法论判断、受众窄；**本轮决定性实验（CIFAR-10）两次失败后放弃**；v3 正向结果经核验为「自己出题自己考」的 C4 reanalysis（Δ 二值化由构造决定、特征分组在已知 C4 相关性后冻结、六规则含 `rule_vi` 硬编码 True 与平凡 `rule_v`）；§3.5 判据是定义性重述；本轮新引入 1 句与数据矛盾的陈述、1 个 Overfull、1 个主文隐瞒；A5 行政阻断（不加权科学分）。
- **决定性 tie-breaker**：C1c 的完全事前复制把内部效度推到很高，使分数站上 5；但「真实视觉正向效应缺失」这一最强关切本轮**丝毫未动且被再次尝试失败所印证**，v3 的 `positive_result=true` 只等于六条自定规则的合取、不构成独立外部验证，使分数无法站上 6。二者相抵落在 5 与 6 之间偏下；本轮的呈现/披露修补按用户指令不抬高由证据决定的总分，新引入的准确性/格式缺陷亦不大幅压低总分，故取含小数的独立推演值（见 §11 唯一评分行），**不四舍五入到任何整数、半整数、历史分数或目标值**。

---

## 14. Questions For Authors（决策相关）

1. 本轮 `trial1_failed_label_design/` 与 `trial2_failed_unlearnable_label/` 两次 CIFAR-10 真实视觉训练尝试（Δ 恒为 0）为何在主文完全未提及？§4.13 是「完全事前预注册的独立验证」，还是两次失败后改变手段、对已审计 C4 数据的事前冻结重分析？能否在主文补一句如实说明？
2. §4.15「Its degree-null, task-aware and motif-removed columns remain near chance at every dose」与 `metrics_multisubgraph.json` 的 `task_aware_null`（0.69–0.94 随剂量上升）、`L1_degree_null`（S1 p0 0.6742 / S2 pfull 0.6581）直接矛盾；能否修正该句并在 `tab:r91repl` 补 null 条件列？
3. §3.5 的 Proposition 是「控制充分性」的 iff，§4.13 检验的是「训练无关特征对 |Δ| 幅度的 MAE 优势」；二者如何构成对该 iff 的验证？§3.5 承诺的 oracle / leakage / 路径枚举「beside every dose」在 §4.13 何处呈现？
4. `config_v3.json` 的 8 path-aware / 4 path-blind 分组是在已知 C4 特征与 Δ 相关性（`density` +0.872、`motif_edges_kept` +0.937）之后构造的；相对「数据/结论」的事前性如何保证？`rule_vi` 在 `run_r93_v3.py:59` 硬编码 `True`、`rule_v` 平凡可满足，是否应把 `positive_result` 改为仅由具判别力规则决定？
5. 5 个反例全部落在 k12 / high 密度层且 high 层增益 = −0.0191（全局统计反而更准）；摘要仅写「positive in two of three strata」。能否在主文讨论这一结构性反例并说明其对「路径感知特征必要性」的影响？
6. `expected_strong` 主文定义（三项合取）与 `contract-v2.md:163-170`（四项合取）不一致，且「strictly monotone localising ladder」与论文 outcome (iii)「ladder 无定位力」张力；能否给出与随稿合同一致、可复核的精确定义与 unmet 判定？
7. `tables_r93_scope.tex` 引入 1 个 Overfull（136.26pt）；LLM Usage Statement 仍为占位符；enrollment（2026-11-10 23:59 AOE）与 reciprocal-reviewer quota 门户侧状态如何？

---

## 15. Unresolved（A / B / C 类）

**A 类 — 由证据决定、直接影响总分（最强关切优先）**
- A1 真实视觉任务上无任何正向、经严格 null 对照验证的拓扑效应；venue fit 弱；**本轮决定性实验（CIFAR-10）两次失败后放弃**。
- A2 中心正向结论限于受控 XOR 诊断标签、近设计同义反复；§3.5 判据是定义性重述，§4.13 是「自己出题自己考」的 C4 reanalysis，`positive_result=true` 未改变决定性轴。
- A3 C3 未复现 task-aware recovery（DiD −0.0477，CI 含 0）；`mechanism_transfer_confirmed=false`；`expected_strong` unmet。
- A4 20 图符号预测 = 多数类基线；C4 符号判据 FAIL（`i_signs_not_all_same=false`、`ii_sign_agreement_margin=false`）；显著特征部分编码实验操纵本身。
- A5（行政，不加权科学分）LLM Usage Statement 占位符 → desk-reject 风险。

**B 类 — 呈现 / 可解释性（不改动证据决定的总分）**
- B1 本轮新引入「null columns remain near chance」与落盘 `task_aware_null` / `L1_degree_null` 矛盾（§5.4）。
- B2 `tab:r91repl` 上半只呈 real 两列；5 反例只在 released evidence、high 层 −0.0191 未在主文讨论。
- B3 主文未披露两次失败 trial → reanalysis 的方法转向；摘要把退守结果作正向头条。
- B4 `expected_strong` 主文定义与 `contract-v2.md` 不一致、与 outcome (iii) 张力；§3.5 交叉引用不实；§4.6 与 §4.13 措辞张力。
- B5 摘要过密、`main.log` 1 个 Overfull（新增 scope 表）、题录/内部标识符入正文（历史残留）。
- 说明：`p2==pfull` 解释、两负面 flag 入摘要/结论、scope 表、`config_v3.sha256` 一致性、v3 反例保留与符号退化如实保留、题录零外链、双盲、零 undefined refs、p8/p9 分页——以上经核验**均不是关切**，且本轮前四项属真实呈现改善（但不抬高总分）。

**C 类 — 本次不可从磁盘核验 / 需作者澄清（影响置信度，不自动改分）**
- C1 **本次未重新联网核实** CVPR 2027 官方规则；依据落盘 `submission-constraints.md`（自述 2026-11-10 联网核实整理），enrollment / 截止 / reciprocal-reviewer 等时效性条款未复核当前有效性。
- C2 `main.bib` 中 6 篇 2026 年 arXiv 预印本的真实存在 / 版本 / 结论无法离线核实（若任一虚构为 class C fatal）。
- C3 §4.1 硬件 / 驱动 / 151s、`Reproducibility` 段 4 个 executed-script SHA 前缀未逐一与磁盘文件做全量 SHA 复核（历史报告曾核验，本次抽查未全量重做）。
- C4 两次 trial 失败原因仅依日志 / config 自述，未重跑训练验证；`run_console.log` 的 Δ 恒 0 未独立复现。
- C5 历史 R47/R49/R60/R91 独立评审分数（7.5/7.5/6.3/5.4）未作为锚点；本次独立推演。

---

## 16. Action Plan / 最该补的一个实验

**优先级 1（决定性，唯一能显著上移总分的实验）**：在**真实自然视觉任务 / 已发表视觉管线（含官方 flyvis）**上做严格 null 对照的正向验证——把 MaleCNS 视觉子图（或 cell-type-resolved 稀疏电路）作为固定先验，配 `A=0` / degree-preserving / task-aware / motif-removed 四类控制，同一 shared-init、10 seeds、配对 bootstrap CI + BH，证明「保护任务相关路径的图显著优于不保护的 null」，并同时报告非图 MLP 强基线。若该效应成立且经上述控制归因，Significance 与 Evidence 的短板同时补齐，A1/A3 消解，总分可进入 6 区间；若仍为阴性，应把投稿定位从 CVPR 主会调整到更适配 negative-result / methodology 的 venue。**本轮两次 CIFAR-10 失败尝试表明该路径尚未走通；措辞修补、格式修补、补 LLM 声明、补条件列、§3.5 判据、v3 reanalysis 都不能替代这一实验，也不改变由证据决定的总分。**

**优先级 2（证据准确性 / 呈现，仅改维度分，不抬高总分）**：修正 §4.15 矛盾陈述；`tab:r91repl` 补 null 条件列；主文披露两次失败转向；`expected_strong` 定义对齐 `contract-v2.md`；§3.5 交叉引用与判据改为可证伪预测；主文呈现 5 反例与 high 负增益层；统一 §4.6/§4.13 措辞；再压摘要。

**优先级 3（行政 / 格式，作者门户侧，不加权科学分）**：补 LLM Usage Statement 实质内容 → 重编译 → 复核 p9 → 刷新 hash → 重跑 final audit；修 `tables_r93_scope.tex` 的 1 个 Overfull；确认 enrollment 与 reciprocal-reviewer quota。

**Handoffs**：A1 交实验 owner（requires-new-result）；A4/B1–B5 交 `ccf-paper-writer`（claim-qualification / figure-table / compression）；C1/C2 交作者本人；不写 rebuttal、不生成稿件修订文本。

---

## 17. Output Self-check

- 报告写入**唯一**指定路径；未写其他文件；未修改稿件、指标、审计、账本、校验器；所有复算均为只读（`python3 - <<'PY'` 不落盘）。
- 全文**恰好一行**给出综合分与置信度（加粗 `Overall` 与 `Scholarly Confidence` 两标签，位于 §11 Scorecard 之后）；其余位置未再出现该评分行或分数重复声明。
- X = 5.2 为独立推演的 1–10 含小数分值，未四舍五入到任何整数/半整数/目标值，未锚定历史 7.5 / 7.5 / 6.3 / 5.4，未由七维均值（≈7.1）抹平最强关切；Y = 4.6 按 `calibration-and-rank.md` 1–5 尺度独立判定（全文、9 页逐页、全部 metrics、脚本、日志、编译日志、历史报告、协议均可得，决定性轴无猜测；保留 C1–C5 未核验项，故不取满值）。
- 已自述：被评审版本 md5（§0/§1）、Checks run 清单（§2）、Unresolved A/B/C（§15）、本次是否重新联网核实（§0/§2 C-13/§15 C1：**否**）。
- 七维 Scorecard 每维含 score + confidence + 可核验引用 + 具体扣分理由 + 明确 score-change condition；7 人独立 panel 先于综合（§9）；Concern-to-action 表（§12）、Score-Change Conditions（raise/lower/no quick change）与两方向 tie-breaker（§13）齐备。
- 特别判定已给出（§6）：v3 数字/布尔/披露诚实且可独立复算，但「自己出题自己考 / 近设计同义反复」、特征分组非数据意义事前、留一图-out 无泄漏、反例未删除、符号退化如实保留、`positive_result=true` 未被过度解读为「拓扑有利于视觉」、两次失败 trial 未包装成正面但主文隐瞒、本轮新增内容**未真正改变证据强度**；新发现本轮 1 处事实性矛盾陈述（§5.4）与 1 个 Overfull（§8）。
- 未因披露负结果额外惩罚、未因披露本身默认加分、未因格式/披露修补抬高证据决定的总分；总分不由七维均值抹平最强关切；行政/格式缺陷（LLM 占位符、Overfull）单列且不加权科学分。
- 表格 Markdown 分隔符与列数一致；无 `TBD` / `TODO` / `[fill]` / 空标题 / 无定位泛化填充；稿件自身的 LLM 占位符作为被评审事实被如实记录，非本报告占位。

# CVPR 2027 · Full 模式独立评审报告（与作者无关的 AC / Reviewer）

> 本报告由一位对论文写作过程、作者会话无任何背景信息的独立评审人依据磁盘文件独立推演。
> 未获知、也未迎合任何"目标分数"；历史 R47/R49/R58/R60 评审结论仅用于理解关切演化，
> 其分数（含 7.5 / Confidence 5）一律不作为锚点、不照抄、不反向对齐。

---

## 0. 报告元数据

| 字段 | 值 |
|:---|:---|
| Mode | `full`（scientific + writing + format + revision-action synthesis） |
| Venue / year / track | CVPR 2027，主会研究论文，双盲评审稿 |
| Paper title | *A Structure-Sensitive Null Ladder Exposes a Blind Spot in Connectome-Control Protocols* |
| 被评审版本 | `r91-candidate/`（唯一版本，`main.tex` = `paper.tex`） |
| 被评审版本 md5 | `471de7fcc682b79e94b8938ad9d77e8d`（`main.tex`，43,897 字节） |
| 配套 PDF md5 / 页数 | `605db8ea30372bf6a4be5a83a3915129`、9 页（`main.pdf` = `paper.pdf`，逐字节一致） |
| Reviewer mode | 独立 AC；7 人独立 reviewer panel 先于综合 |
| Search basis | 本次**未重新联网核实**；官方规则依据已落盘的 `submission-constraints.md`（其自述为 2026-11-10 由官方 AuthorGuidelines / CallForPapers 联网核实整理） |
| Review date | 2026-11-10 |
| Report file | `/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision/ccfa-review-reports/paper-null-ladder-r91-independent-review-20261110.md` |
| 独立性声明 | 未读任何作者会话；未修改稿件、指标、审计、账本、校验器；未创建其他评审报告 |

---

## 1. 版本锁定与实际读过的文件清单

**锁定结果**

- `main.tex`：43,897 字节，md5 `471de7fcc682b79e94b8938ad9d77e8d`；`paper.tex` 与其 `cmp` 逐字节一致（md5 相同）。
- `main.pdf`：2,101,382 字节，md5 `605db8ea30372bf6a4be5a83a3915129`，pypdf 确认 9 页；`paper.pdf` 逐字节一致。
- `tables_r91.tex`：md5 `990da4a3f4b66a93b110463c38c0c91a`。
- 注意：`final-submission-audit.md` 内记录的 SHA-256（`f0e760db…`）对应的是**根目录 40,175 字节的更早版本**，不是本次被评审的 43,897 字节 `r91-candidate`。故该审计的 PASS 结论只作背景，r91 的编译告警与分页由本次独立复核。

**实际读过的指标 / 证据文件（逐份列出）**

1. 用户指定的 4 份核心 metrics：
   - `results/r51_motif_survival/metrics.json`（C1 固定密度剂量，负结果）
   - `results/r51_pathblock/metrics_pathblock.json`（C1b 路径阻断修复）
   - `results/r51_multisubgraph/metrics_multisubgraph.json`（C1c 两独立真实子图）
   - `results/r51_strong_baseline/metrics.json`（C3 忠实复跑已发表 control ladder）
2. 配套 config / summary / 校验：
   - `r51_multisubgraph/config_multisubgraph.json`、`summary_multisubgraph.txt`、`verification_r60.json`
   - `r51_strong_baseline/config.json`、`summary.txt`、`README.md`
3. 主矩阵与边界表数字来源（Python 数值定位，共扫描两个 run 的 76 份 JSON，排除无关的 `timesfm` 示例数据）：
   - `p3_p4/metrics.json`、`metrics_completed.json`（0.8152 / 0.4795 / 0.8348 / 0.5133）
   - `p3_p4_taskaware/metrics.json`（0.8371 / 0.8346）
   - `r39_heldout/metrics.json`（0.1046 / 0.1635）、`r39_density_sweep/metrics.json`（0.9987 等）
   - `r39_visual_task/metrics.json`（0.7185 / 0.9722）
   - `r39_real_connectome_v2/metrics.json`（0.6423 / 0.1028）
   - `r51_independent_family/metrics.json`（0.5049 等）
4. 审计 / 元数据 / 历史评审（背景，不作锚点）：`integrity-audit.md`、`clean-copy-audit.md`、`reference-dedup-audit.md`、`final-submission-audit.md`、`manuscript-metadata.md`、`existing-scientific-review.md`、`submission-constraints.md`。
5. 稿件与呈现：`main.tex`、`preamble.tex`、`main.bib`、`main.bbl`、`main.log`、`main.pdf`、`tables.tex`、`tables_taskaware.tex`、`tables_heldout.tex`、`tables_boundary.tex`、`tables_r91.tex`、`make_r91_tables.py`。
6. 图（实际核验）：`fig1_framework.png`（ViewImage 逐面板看过）、`fig2_main_results.pdf`、`fig3_ladder_analysis.pdf`、`fig4_dose_response.pdf`（pypdf 提取文字标注并与表格对账）。
7. 必读协议：`SKILL.md`、`calibration-and-rank.md`、`ccf-common/references/review-output-standards.md`（用户给出的第三份路径不存在，已定位到 `ccf-common` 下同名文件）、`submission-constraints.md`；另加载 `reviewer-panel.md`、`universal-review-rubric.md`、`desk-checks.md`、`fixed-output-format.md`、`review-workflow.md`、`venue-review-styles.md`、`writing-review/latex-format-audit.md`、`writing-review/revision-actions.md`。

---

## 2. Checks run 清单

| # | Check | 方法 | 结果 |
|:--|:---|:---|:---|
| C-01 | 版本锁定 | `wc -c` / `md5` / `cmp` / pypdf | 通过（见 §1） |
| C-02 | 协议与官方规则 | 4 份必读 + 9 份 full 模式引用 | 通过 |
| C-03 | 稿件 / 表格 / 脚本 / 题录通读 | Read 全文 | 完成 |
| C-04 | 头条数字对账 | 76 份 JSON 数值扫描 + 逐字段比对 5 张表 + 摘要/引言/结果/结论 | 全部可溯源（见 §5） |
| C-05 | `make_r91_tables.py` 运行时读取核验 | 只读复现脚本逻辑（不调用 `write_text`），与落盘 `tables_r91.tex` 比 md5 | 完全一致，无手抄 |
| C-06 | 4 份核心 metrics 逐字段 + 六/七规则 + flag | Read + 交叉核对 `verification_r60.json` | 通过（见 §5/§6/§7） |
| C-07 | 统计实践 | config `stats` / `seeds` / `shared_init` / oracle & leakage probes / comparisons | 通过（见 §6） |
| C-08 | 独立性与诚实度 | 预注册说明 / adaptive 标注 / 负结果包装排查 | 基本通过，2 处呈现缺口（见 §7） |
| C-09 | 分页与分页内容 | pypdf 逐页 + p8/p9 全文 | 通过（见 §8） |
| C-10 | 编译告警 | `main.log` 大小写不敏感 + 精确分类计数 | 0 Overfull / 0 Underfull / 0 undefined refs / 0 LaTeX Warning |
| C-11 | 双盲 / 题录外链 / 隐藏指令 | Grep 扫描 | 通过（见 §8） |
| C-12 | 图内容 | ViewImage + pypdf 文字提取 | 图文一致，fig1 含 SCOPE 框 |
| C-13 | 重新联网核实 | 无 | **本次未重新联网**（依据落盘 `submission-constraints.md`） |

---

## 3. Desk Rejection Assessment

- **Paper length**：PASS。9 物理页，p1–p8 主文（含 4 图 8 表），p8 完整 Conclusion 收尾、无参考文献；p9 仅 LLM Usage Statement + References，符合"8 页正文 + 额外页仅 References 与强制声明"。
- **Topic compatibility**：UNCERTAIN / 偏弱。CVPR 主维度为 novelty、technical quality、empirical validation、**visual evidence**、fair comparison；本文自述为 evaluation-methodology study，无 image benchmark、无自然视觉任务、无视觉精度提升主张（`main.tex:98-101`）。方法论严谨但视觉证据缺失，venue fit 是实质性风险而非形式问题。
- **Minimum quality**：PASS。六节规范、方法/证据/局限/结论齐备。
- **Policy / anonymity / compliance**：**FAIL（行政阻断）**。`\author{Anonymous}`、无身份链接、题录 0 外链均通过；但 `main.tex:765-766` 的 `\section*{LLM Usage Statement}` 正文为 `\emph{[To be supplied by the authors.]}` 占位符。CVPR 2027 该声明为强制项，缺失即 desk rejection（`submission-constraints.md` class B）。
- **Prompt injection / hidden manipulation**：PASS。全文 `ignore previous` / `system prompt` / 打分诱导类扫描 0 命中；4 处 "hidden" 均为普通用词（"never hidden"、"hidden width"）。
- **Ethics and reviewability**：PASS。纯计算、无人类/动物受试、公共 CC-BY 4.0 数据、误用风险（错误结构归因）已讨论。

**Desk verdict**：行政层面 `high / likely`（LLM 占位符，且 enrollment/reciprocal-reviewer 需作者门户侧处理）；`Can be fixed before review? partly`——声明与门户字段属作者动作，可修；科学证据边界不可由格式修补解决。按用户指令，此行政阻断**不参与抬高或压低由证据决定的科学总分**。

---

## 4. Paper Summary And Contribution Map

**一段摘要**：论文把 connectome-constrained 视觉模型中"拓扑是否有用"的文献分歧重述为**比较协议（null 生成器）问题**，预注册一条嵌套 null ladder（L0 边数 / L1 度 / L2 模块对 / L3 有向 triad census，L4 为独立匹配控制），配一个只能经注入两跳收敛 motif 求解的 XOR 标签。受控 96 节点图上真实图 0.8152、全部 null 与无图/打乱对照在 chance，差 0.30–0.34（BH q=0.0002），但 rung 间差仅 0.0244、单调性破坏、20 图 held-out 符号预测恰等于多数类基线——故裁决为"第三种结果"：null family 才是混淆项。task-aware null 保住 18 条 motif 边即恢复优势（0.8346 vs 0.8371），motif 剂量在 ≤9 边时塌到 chance。真实 MaleCNS wiring 上：C1 固定密度剂量因补偿交换新建两跳路径而失败；C1b 路径阻断修复（adaptive/remedial）得单调剂量、六规则全通过；C1c 完全事前、两独立真实子图复现四档剂量、七规则全通过；C3 忠实复跑已发表 ladder 复现 weak/strict 但**未**复现 task-aware recovery；C5 六门禁通过；真实图像分类为阴性（非图 MLP 0.9722 碾压）。结论：control 构造而非拓扑解释冲突报告，motif survival 是受控区间内的实测预测器而非普适原因。

| 项 | 内容 |
|:---|:---|
| Claimed problem | 已发表 connectome-control 结论互相矛盾（structure-alone 正向 vs degree-preserving null 抹除） |
| Claimed gap | 缺乏以 null 生成器本身为实验变量、且任务结构敏感的受控比较 |
| Contribution map | ① 可复用 null-generator 标准（机器校验不变量 + gate + 校正统计）；② 受控图上"全局统计量不保任务相关 motif"的裁决；③ 20 图 held-out 关联研究；④ 真实 wiring 上 C1→C1b→C1c→C3/C5 的证据链与 scope 边界 |
| Contribution type | evaluation-methodology / diagnostic / negative-result（作者明确不是新 backbone） |
| Evidence package | 10 冻结种子、配对 seed-level bootstrap（R=5000）、BH、sign-flip 置换、oracle/leakage 探针、shared-init、不变量断言、剂量干预、两独立真实子图、忠实复跑、clean rerun；全部落盘可核验 |
| Stated limitations | 96 节点受控图；真实 MaleCNS 为边界非复现；单变量扫描只隔离 in-degree；真实图像任务阴性；sign prediction = 多数类；flyvis 栈未重跑；三种子预检仍 `failed`（探针缺陷）；早期聚合块崩溃且脚本 checksum 不匹配；visual-ID 口径跨运行不可混用 |

---

## 5. 主张—证据对账（Claim–Evidence Audit）

**方法**：把摘要/引言/结果/结论/五张表全部头条数字与落盘 `metrics*.json` 逐字段核对；对 r91 两张表用脚本逻辑**只读复现**（不写盘）验证"运行时读取、无手抄"；对用户点名的四项选择性呈现逐项核查。

**复现验证（关键）**：`make_r91_tables.py` 的 `json.load` 指向 4 份 pulled metrics，全部单元格来自 `per_dose[*][cond]['mean']` 或 `boot_ci` 重算，无硬编码数字。按同一 `rng = default_rng(20261110)` 在内存中重算得到的 `tables_r91.tex` 与落盘文件 **md5 完全一致**（`990da4a3f4b66a93b110463c38c0c91a`）。结论：r91 表确为运行时从 metrics 生成，无手抄。

| 头条数字（稿件位置） | 落盘来源（精确值 → 4 位） | 一致性 |
|:---|:---|:---:|
| 0.8152（摘要/§main/tab:main） | `p3_p4/metrics.json:/main_matrix/mean_acc/real` = 0.815234375 | ✓ |
| 0.4795–0.5133（摘要/§main） | L0 = 0.4794921875 … shuffled = `metrics_completed.json` 0.5133 | ✓ |
| 0.30–0.34 / q=0.0002（tab:main） | Δ 列与 `comparisons` 的 `q`/BH 族 | ✓ |
| 0.8346 / 0.8371 / q=0.40（tab:taskaware） | `p3_p4_taskaware/metrics.json` 0.8345703125 / 0.837109375 | ✓ |
| 剂量 0.8371/0.8316/0.4988/0.5104/0.5117 | `p3_p4_taskaware/metrics.json:/dose_response` | ✓ |
| 0.0244（rung 间最大差） | 派生量：Δ(L0)=0.3357 − Δ(L1)=0.3113 = 0.0244；正文明确为 delta 之差 | ✓（非存储值，合理） |
| 24.875/0.125/5.938/0.500（§invariants + fig3） | `fig3` 标注 24.9/0.1/5.9/0.5 | ✓ |
| 0.1046 / 0.1635 / 36% / 0.60（tab:heldout） | `r39_heldout/metrics.json` | ✓ |
| 0.5049→0.9987、0.9863（tab:density） | `r51_independent_family`、`r39_density_sweep/metrics.json` = 0.9986979、0.9863 | ✓ |
| 0.7185/0.7190/0.9722、+0.0148 MNIST（tab:visual/§visualtask） | `r39_visual_task/metrics.json`；MNIST 反向 delta 正文如实并列 | ✓ |
| 0.6423/0.5283/0.6162/0.5850（tab:real） | `r39_real_connectome_v2/metrics.json` = 0.6422526 等 | ✓ |
| 0.9431 / 0.1028 / 0.9509（§realwiringrepl） | `r51_strong_baseline/metrics.json:/constrained/dense/*` = 0.9430556 / 0.1027778 / 0.9509259 | ✓ |
| C1 表 `0.9772/0.5051/0.5051/0.9745`（tab:r91dose 上半） | `r51_motif_survival/metrics.json:/task_a/stats/per_dose` | ✓ 全部 16 格 |
| C1b 表 `0.9772/0.9772/0.9641/0.5055`（下半） | `r51_pathblock/metrics_pathblock.json` | ✓ 全部 16 格 |
| C1c 表 `0.5017/0.6889/0.8955/0.9432` 与 `0.5017/0.6742/0.8877/0.9407` | `r51_multisubgraph/metrics_multisubgraph.json` | ✓ |
| Δ(full−p0)=0.4415[0.4272,0.4538] / 0.4390[0.4249,0.4522] | 脚本 `boot_ci` 重算（原始 comparisons 为 [0.4265,0.4542]/[0.4249,0.4525]，bootstrap 重抽样微差） | ✓ 可解释 |
| weak 0.2282 / strict 0.0532 / task-aware 0.0056 / DiD −0.0477（tab:r91repl 下半） | `r51_strong_baseline/metrics.json:/ladder/dense` 与 `did_taskaware_minus_strict` | ✓ |

**用户点名四项的呈现核查**

| 项 | 是否报了 | 证据 |
|:---|:---|:---|
| C1 非单调失败 | **是** | `tab:r91dose` 上半四行 + §realwiringdose `hypothesis_supported=false`、"original negative verdict is retained as a read-only contrast" |
| C3 task-aware 未恢复 | **是** | `tab:r91repl` 下半 task-aware 0.0056、DiD −0.0477（CI 含 0）+ 摘要/§realwiringrepl/结论三处 "but not task-aware recovery" |
| C5 六门禁 | **是** | 摘要 "passes all six gates" + §realwiringrepl "passes all six structural gates"，对应 `task_c5.gates` g1–g6 全 true、`structure_gates_passed=true` |
| 真实视觉任务阴性 | **是** | §visualtask "We report this as a negative result" + `tab:visual` 5 条件全列 + 摘要/结论两处 scope 限定 + MNIST 反向 delta 并列报告 |

**条件列完整性核查（发现 2 处缺口）**

- 主矩阵 `tab:main`（8 条件）、`tab:taskaware`（8 条件）、`tab:density`（4 条件列）、`tab:visual`（5 条件）、`tab:r91dose`（4 条件列）均完整，历史 R47 曾发现的"隐藏两列 / 未报 MNIST delta"在 r91 已修复并保留。
- **缺口 B1**：`tab:r91dose` 下半 `$pfull$` 与 `$p2$` 两行数值逐格相同（0.9772/0.5017/0.9794/0.5004）。支撑材料 `config_multisubgraph.json:8,333-336` 明确记录原因——C1b 的 `P_all_cardinality=2`，故 p2 与 pfull 实为同一张图、仅 2 个不同剂量水平；C1c 才以 `|P_all|=3` 修成 `p2≠pfull`。**论文正文与摘要均未解释这一"四档剂量实为三图"的现象**，读者无法从稿件理解表格。
- **缺口 B2**：`tab:r91repl` 上半只呈现 `real` 列与 Δ，未呈现 null 条件列。支撑 `metrics_multisubgraph.json` / `summary_multisubgraph.txt` / `verification_r60.json:919-920` 完整记录了若干反直觉 cell：S1_broad p0 的 `L1_degree_null=0.6742`、`task_aware_null=0.7032`（显著高于 chance，且 `real(p0)−L1_degree_null(p0)=−0.1725, p_BH=0.0025`），S2_narrow pfull 的 `L1_degree_null=0.6581`。规则 (iii) 因定义为跨剂量 grand mean（仅 A0 / L1 / motif-removed，S1=0.5448、S2=0.5408）而正确判为 PASS，计算无误；核验文件亦明写 "reported rather than hidden"。但**这些 cell 既未进入主文表格，也未在正文讨论**，属于主文层面的选择性呈现（非数据隐瞒）。

**对账结论**：数字层零造假、零手抄、零不一致；选择性呈现仅存在于"条件列展示层级"（B1/B2），不构成负结果包装或数字篡改。

---

## 6. 科学性与统计核验

| 核验点 | 结论 | 依据 |
|:---|:---|:---|
| 配对 bootstrap CI | 通过 | `config_multisubgraph.json:stats` `bootstrap_R=5000`、`ci_method=percentile`；各 `comparisons` 有 `ci_lo/ci_hi`；r91 表 CI 由脚本重算可复现 |
| BH 校正 | 通过 | `multiple_testing=Benjamini-Hochberg over the pre-registered comparison family`；`p_BH` 逐条在案；主矩阵 q=0.0002、tab:taskaware q=0.00032/0.40132 一致 |
| 10 seeds + 共享初始化 | 通过 | `seeds=[11,17,…,103]`；`shared_init` 定义"init RNG 与 data RNG 只依赖 run seed"；`preflight.shared_init_same_seed_equal=true`；每个 `per_seed` 长度 10 |
| oracle / leakage 探针 | 通过 | `oracle_probe=0.9991`、`leakage_probe≈0.50`、§gate 如实保留三种子预检 `failed`（0.7891 vs 0.80 的探针缺陷，不重贴标签） |
| 剂量单调性 | 通过且分层清楚 | C1 非单调（`hypothesis_supported=false`，六规则仅 iv/vi 为 true）；C1b 单调（六规则全 true）；C1c 两子图各四档单调、七规则全 true |
| `p2==pfull` 说明 | **稿件缺、支撑有** | 见 §5 缺口 B1；`config` 与 `verification_r60.json` 有明确说明，主文无 |
| 跨运行 visual-ID 口径不可混用 | 通过 | §density "9,766 / 29,442 / 29,564 IDs … absolute edge counts are not comparable"、Limitations 复述；§realwiringrepl 另记 C1c 的 105,275 / 29,534 IDs |
| 等价复实现非官方 flyvis | 通过 | §discussion "We did not rerun their flyvis stack and make no benchmark-reproduction claim"；C3 称 "faithful rerun of the published control ladder" 但未冒称官方复现 |
| `mechanism_transfer_confirmed=false` | 通过（flag 属实） | `r51_strong_baseline/metrics.json:/decision/mechanism_transfer_confirmed=false`；正文 §realwiringrepl 与 Limitations 两处明写 |
| `expected_strong` 未达成 | 属实但术语未定义、且不在给定支撑清单内 | `main.tex:676` 以 `\texttt{}` 声称 "unmet overall"；定义实存于更早的 `ccfa-startup-packet-v2/feasibility-contract.json` 与 `audits/P5-strong-result-lock.md`（记录 "partially met → scoped, no threshold lowered"），**不在用户列出的 results 支撑目录内** |
| 两 flag 是否写进摘要与结论 | **字面未写；语义已表达** | 摘要/结论均无 `\texttt{mechanism_transfer_confirmed}` 或 `\texttt{expected_strong}`；但结论有 "It does not establish transfer to natural visual tasks"、"not a universal cause"，摘要有 "topology specificity on real image classification remains negative"。属呈现层级缺口，非把负结果包装成正面 |

**科学性结论**：统计设计在本类 diagnostic 研究中属上乘，预注册/adaptive 分层诚实。核心科学边界是——所有**正向**机制证据都落在受控 XOR 诊断标签上；真实视觉任务上的正向拓扑效应从未建立（§visualtask 阴性、C3 未复现、transfer=false）。理论 Eq.(1) 被作者主动限定为 "upper-bound intuition, not an exact per-rung probability"，处理得当。

---

## 7. 独立性与诚实度核验

- **C1b 是否被正确标注为 adaptive/remedial 预注册（而非原假设被证实）**：**是，正文正确**。§realwiringdose `main.tex:653-654`："This repair is *adaptive, remedial* (designed after inspecting the first run), hence the fully anticipatory replication below."；`config_multisubgraph.json:8` 亦记 "C1b was a salvage pre-registration designed after seeing C1 interim readouts"。原 C1 的 `hypothesis_supported=false` 被保留为 read-only contrast，未被改写为证实。**但摘要措辞存在张力**：摘要 `main.tex:56-57` 称 "a **preregistered** path-blocking repair yields a monotone dose satisfying all six rules"，未带 adaptive 限定；结论 `main.tex:752-755` 用 "This **establishes** the path-level mechanism on real wiring"。二者与正文的 adaptive 标注并列阅读时，容易被误读为原假设被证实。C1c 的完全事前复现确实把结论救回到可复现事实，但摘要/结论的措辞层级仍应下修一格。
- **C1c 是否完全事前复现**：**是**。`preregistration_date=2026-11-08`，note 明写 "FULLY pre-registered BEFORE any training of C1c"、"No post-hoc modification allowed"；`verification_r60.json` 125/125 检查通过（含 config SHA、脚本 SHA、10×5 数组、p2≠pfull、cross_subgraph_replicated）；并如实披露两处自指瑕疵（log 尾部追加 51 字节、一次 KeyError 后脚本 SHA 变更但预注册对象未改）。`cross_subgraph_replicated=true` 可核验。
- **是否把负结果包装成正面**：**否**。真实图像阴性、C3 未恢复、dense 子图 gate 失败、20 图 sign=baseline、五变量同时改动的不可归因，全部以削弱性限定明写；MNIST 与 digits 反向 delta 并列而不择一；"we make no replication claim"（§realconnectome）明确。
- **是否把「现象成立」写成「拓扑优势成立」**：**否，且反向**。标题/结论落点是 "control construction, not topology, explains conflicting reports"；论文反复声明 "no claim of improved visual accuracy"、"wiring prior is not a competitive inductive bias"。这是本文最值得肯定的诚实点。
- **不得因披露本身加分/罚分**：本评审对 Ethics/Limitations 与 Evidence 的高分，来自"局限陈述与证据一致、有界、可核验、无隐瞒"，**不是**因为"论文披露了负结果"这一行为；按用户指令，该高分不用于抬高由证据决定的总分。

---

## 8. CVPR 2027 合规核验

| 约束 | 核验 | 结果 |
|:---|:---|:---|
| 8 页正文 | pypdf 9 页；p1–p8 主文，p8 最后一句 "control construction, not topology, explains conflicting reports." 完整收尾，p8 无参考文献 | PASS |
| 额外页仅 References + 强制 LLM Usage Statement | p9 全文 = review 水印 + `LLM Usage Statement` + `[To be supplied by the authors.]` + 15 条 References，无正文混入 | PASS（内容合规） |
| 强制 LLM Usage Statement 有实质内容 | `main.tex:766` 为占位符 `\emph{[To be supplied by the authors.]}` | **FAIL / BLOCKER**（class B，desk-reject 级行政风险） |
| 双盲 | `\author{Anonymous}`；无致谢/单位/邮箱；`toposens2026` 以第三人称 "The closest prior work" 引用 | PASS |
| 题录无外链 | `main.bib` 无 url/http/www/href（仅 3 个 doi 字段）；`main.bbl` 仅 `ieeenat_fullname.bst` 生成的 `\providecommand{\url}` 宏定义头，15 条题录无任何实际 URL | PASS |
| `main.log` 0 Overfull / 0 undefined refs | 精确分类计数：`^Overfull|^Underfull`=0、`undefined (citation|reference)`=0、`LaTeX Warning`=0；大小写不敏感扫描的 7 个命中全部是 `silence` / `infwarerr` 宏包加载描述与 `\GenericWarning` 重定义信息，非告警；`Output written on main.pdf (9 pages, 2101382 bytes)` | PASS |
| 官方 `cvpr.sty` / 10pt / 双栏 | `\documentclass[10pt,twocolumn,letterpaper]` + `\usepackage[review]{cvpr}`；`preamble.tex` 仅 `\linespread{0.88}`（正文之外） | PASS |
| 图引用 / 图内容 | 4 图均有 `\ref`；fig1 有 SCOPE 虚线框 "controlled graph; real-visual prior not competitive" 与正文 scope 一致；fig2/3/4 数值标注与表格一致 | PASS |

**合规结论**：科学格式几乎全通过；唯一硬伤是 LLM Usage Statement 占位符。按用户指令，**该格式/披露问题不参与抬高由证据决定的科学总分**，但它独立地使当前包件"不可直接提交"（作者门户侧动作：补声明、enrollment 2026-11-10 23:59 AOE、reciprocal-reviewer quota、补声明后重编译与刷新 hash）。

---

## 9. Search And Related-Work Basis

- **Queries used**：无（本次未联网；用户给定支撑证据已全部落盘）。
- **Sources searched**：本地磁盘文件 + 已落盘官方规则整理。
- **Closest works found（稿件自述）**：`toposens2026`（degree-preserving null + shared init，其 limitations 恰点名 longer horizon / broader tasks / higher-order nulls）、`structurealone2026`、`lappalainen2024`、`flyhack2026`、`reconvar2026`；经典 null/motif 工作 `maslov2002`、`milo2002`、`wasserman1994`、`hagberg2008`。
- **Unverified related-work risks**：2026 年 6 篇 arXiv 预印本（`structurealone2026` 等）无法离线核实其真实存在/版本/结论；`main.bib` 注释自承部分条目来自项目核验记录。本次不据此扣 novelty 分，但记为 C 类未核验项。
- **Source-quality screening**：未做联网筛选；不虚构缺失文献，不声称"已充分检索"。

---

## 10. Expected Review Outcome

**Expected outcome**：borderline，略偏 negative（borderline-negative 区间上沿）。**Main accept signal**：可核验性极强（表格可由脚本从 metrics 逐格复现）、统计严谨、C1c 完全事前的两独立真实子图复现、负结果与 scope 边界完整披露、复现工件齐全。**Main reject signal**：真实视觉任务上无任何正向、经严格 null 对照验证的拓扑效应；C3 未复现 task-aware recovery 且 `mechanism_transfer_confirmed=false`；核心结论是对实验方法的负面/方法论判断，对 CVPR 视觉受众的 significance 有限；20 图符号预测等于多数类基线。**Confidence**：见下方唯一评分行。不给出任何录用概率或精确百分位。

**内部一致性声明（校准规则）**：综合分与"最强未解决关切"（真实视觉正向证据缺失 + venue fit）一致； skeptical reviewer 会重复该关切；所有 strength 均有精确稿件/指标引用；score-change conditions 具体可行；分数针对 CVPR 而非泛化乐观。**不取七维均值**（均值为 3.86/5，若机械换算会误导到 7 分区间），按 `review-output-standards.md` 的"不得平均掉致命关切"由最强关切定档。

---

## 11. Strengths And Weaknesses

**Strengths（每条带证据）**

1. **数字可核验性极强**：`make_r91_tables.py` 运行时读取 4 份 metrics、无手抄，只读复现 md5 与落盘一致；76 份 JSON 数值扫描确认每个头条数字可溯源（§5）。
2. **统计与预注册纪律**：10 冻结种子、shared-init、配对 percentile bootstrap、BH、sign-flip、oracle/leakage、不变量断言、adaptive 与 fully-anticipatory 分层（§6/§7）。
3. **机制闭环的因果干预**：task-aware null、motif 剂量、path-blocking repair、C1c 两独立真实子图，构成"保护路径→效应恢复"的可复现链条。
4. **诚实度与 scope**：C1 失败、C3 未恢复、真实图像阴性、gate 失败、五变量不可归因、visual-ID 不可混用、非官方 flyvis，全部明写；fig1 甚至内嵌 SCOPE 虚线框。
5. **复现工件完备**：config/script SHA、per-seed 数组、run.log、summary、manifest、verification_r60（125/125）、clean-copy 重建一致。

**Weaknesses（每条带证据与所需修复）**

| Weakness | Evidence basis | Reviewer deduction | Required fix |
|:---|:---|:---|:---|
| W1 真实视觉正向证据缺失 | §visualtask 0.7185/0.9722、MNIST 0.8879/0.7649；§realconnectome "gate fails"；`expected_strong` unmet | 对 CVPR 的核心 empirical/visual 维度未被满足，significance 受限 | 需新实验：至少一个真实视觉任务上经严格 null 对照验证的正向拓扑效应（见 §19） |
| W2 C3 未复现 task-aware recovery + transfer=false | DiD −0.0477[−0.1056,0.0120]；`mechanism_transfer_confirmed=false` | "标准"的普适性仍限于受控 XOR；结论 "establishes" 措辞偏强 | 下修结论措辞，或补跨任务转移证据 |
| W3 20 图符号预测 = 多数类基线 | tab:heldout 0.60 vs 0.60；§heldout 自承若干显著特征"partly encode that manipulation itself" | 预测统计量独立性不足 | 补非操纵图族；或把 claim 收窄为"校正后的幅度关联"（已部分做到） |
| W4 摘要/结论措辞层级 | 摘要 "preregistered path-blocking repair"、结论 "This establishes…" vs 正文 "adaptive, remedial" | 易被误读为原假设被证实 | 在摘要/结论同步加 adaptive 限定 |
| W5 条件列选择性呈现 | B1 p2==pfull 未解释；B2 C1c null 高值 cell 未进主文 | 主文可读性/完整性下降 | 表注解释 p2==pfull；C1c 表补 null 条件列或正文讨论 |
| W6 两负面 flag 未进摘要/结论；`expected_strong` 未定义 | `main.tex:675-676,712`；flag 定义不在给定支撑清单 | 术语不可从随稿材料复核 | 主文定义该术语；摘要/结论补一句明确边界 |
| W7 LLM Statement 占位符 | `main.tex:765-766` | 行政 desk-reject 阻断（不加权科学分） | 作者补声明后重编译、刷 hash、重审 |

---

## 12. 7 人独立 Reviewer Panel（综合前各自独立给分）

> 每位评审在综合前独立给分；不强制互相矛盾、不强制赞扬、不强制拒稿。分数为各角色独立倾向，AC 不取平均。

**R1 · Best-Justified Reviewer**
- Expertise：evaluation methodology / negative-result 倡导者
- Likely score：7.0 ｜ Confidence：4
- Main positive：可核验性与 C1c 完全事前复现；`tab:r91dose` 同时保留失败与修复，是社区可复用的 adjudication 范式
- Main negative：仍缺真实视觉正向用例
- Evidence basis：§5 对账、C1c `cross_subgraph_replicated=true`
- Fatal concern：无
- Score-change condition：补一个真实视觉任务的严格 null 对照正向结果 → 7.5–8

**R2 · Critical Reviewer**
- Expertise：CVPR 视觉主会 senior reviewer
- Likely score：3.5 ｜ Confidence：4
- Main positive：统计严谨、无造假
- Main negative：venue mismatch——无 image benchmark、visual evidence 全为合成/诊断图；非图 MLP 0.9722 碾压；C3 未复现；最终结论是"control 构造决定观测"，对视觉受众无新知识
- Evidence basis：`main.tex:98-101`、§visualtask、DiD −0.0477
- Fatal concern：主张与 venue 经验验证标准不匹配（可独立支撑拒稿）
- Score-change condition：真实视觉任务正向结果 + 结论改写 → 5.5–6

**R3 · Method / Soundness Reviewer**
- Expertise：图学习 / 因果推断
- Likely score：6.0 ｜ Confidence：5
- Main positive：Eq.(1) 主动限定为上界直觉、shared-init、配对 CI、sign-flip、不变量断言
- Main negative：C1b 事后补救；`p2==pfull` 实为 2 剂量水平；结论 "establishes" 与预注册层级不完全对齐
- Evidence basis：`config_multisubgraph.json:8`、`main.tex:752-755`
- Fatal concern：无（mostly sound）
- Score-change condition：解释 p2==pfull 并把结论措辞对齐 → 6.5

**R4 · Evidence / Experiment Reviewer**
- Expertise：实验设计与统计
- Likely score：5.5 ｜ Confidence：5
- Main positive：10 seeds、BH、剂量、两子图、忠实复跑、C5 六门禁全在案；数字逐格可溯源
- Main negative：正向机制仅在 96 节点受控 XOR；sign prediction = baseline；C1c null 高值 cell 未讨论
- Evidence basis：§5/§6、`verification_r60.json:919-920` disclosures
- Fatal concern：无
- Score-change condition：C1c 主文补全条件列 + 非操纵图族 → 6.5

**R5 · Novelty / Positioning Reviewer**
- Expertise：connectome-constrained 视觉 / 网络 null 模型
- Likely score：4.5 ｜ Confidence：4
- Main positive：把 null 生成器当作实验变量、机器校验不变量标准，是有价值的 framing
- Main negative：构件均属既有（degree-preserving、triad census、XOR 合成任务）；`toposens2026` 已点名这些 axes；novelty 是系统严谨性而非新知识
- Evidence basis：`main.tex:159-163`、Related Work
- Fatal concern：无
- Score-change condition：给出控制充分性的形式化判据或第三方采用 → 5.5

**R6 · Writing / Clarity Reviewer**
- Expertise：科技写作 / 可复核性
- Likely score：5.5 ｜ Confidence：5
- Main positive：六节规范、术语稳定、claim-evidence 可见、fig1 内嵌 SCOPE 框
- Main negative：摘要塞满全部实验与所有负结果（近整页压缩结果表）；§realconnectome→§density→§visualtask→§realwiringdose→§realwiringrepl 边界链冗长；`expected_strong` 未定义；B1 造成表格困惑
- Evidence basis：`main.tex:25-65`、§5 缺口 B1/B2
- Fatal concern：无
- Score-change condition：重组边界实验为一张 scope 表 + 压缩摘要 → 6.5

**R7 · Ethics / Reproducibility Reviewer**
- Expertise：研究诚信 / artifacts
- Likely score：8.0 ｜ Confidence：5
- Main positive：负结果、失败、adaptive、scope、跨运行口径、非官方 flyvis、permission、无受试全披露；config/script SHA 与 per-seed 数组齐全，可独立审计
- Main negative：`expected_strong` 定义不在随稿支撑清单；LLM 声明占位符；早期脚本 checksum 不匹配虽披露但属未闭环
- Evidence basis：§7/§8、`existing-scientific-review.md` 关切演化
- Fatal concern：无
- Score-change condition：补 LLM 声明 + 把 `expected_strong` 定义写入随稿材料 → 8.5（**仅该维**，不改由证据决定的总分）

**Panel Synthesis**

- **Agreement**：统计严谨、数字可核验、诚实度、复现工件四项全体认可；全体同意"真实视觉正向证据缺失"是最强关切。
- **Disagreement**：R1（7.0）与 R2（3.5）分歧最大，分歧根源是"方法论严谨的负结果是否足以满足 CVPR 视觉主会的经验验证门槛"，而非事实认定差异。
- **Decisive positive axis**：C1c 完全事前、两独立真实子图、七规则全通过，把 path-level 机制从 adaptive 补救提升为可复现事实。
- **Decisive negative axis**：真实图像任务阴性 + C3 未复现 task-aware recovery + `mechanism_transfer_confirmed=false`，使核心正向主张始终停留在受控 XOR 诊断标签内。
- **Unresolved evidence**：`expected_strong` 定义溯源、2026 预印本真实性、§setup 硬件/SHA 未逐一复核、本次未重新联网。
- **AC stance**：不取 panel 均值（≈5.71）；按最强未解决关切定档于 borderline 略偏 negative，并把行政 blocker（LLM 占位符）单列且不加权科学分。

---

## 13. Concern-to-action 表

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
|:--|:---|:---|:---|:---|:---|:---|:---|:---|
| A1 | major | 真实视觉任务无正向拓扑效应，venue fit 弱 | §visualtask 0.9722；`main.tex:98-101` | Significance / Evidence | requires-new-result | 见 §19 主实验 | 实验 owner | 若补出严格 null 对照的正向结果，Significance 3→4、总分上移约 +0.8 |
| A2 | major | C3 未复现 task-aware recovery、transfer=false | DiD −0.0477；`mechanism_transfer_confirmed=false` | Soundness / Evidence | claim-qualification | 结论 "establishes" 下修；或补跨任务证据 | ccf-paper-writer | 措辞对齐后 Soundness 4→4.5；补证据则 Evidence 4→4.5 |
| A3 | moderate | 摘要/结论措辞偏强于 adaptive 标注 | 摘要 `:56-57`、结论 `:752-755` vs `:653-654` | Clarity / Ethics | claim-qualification | 摘要/结论同步加 "adaptive/remedial" 与 "within controlled diagnostic label" | ccf-paper-writer | Clarity 3→3.5（仅该维） |
| A4 | moderate | sign prediction = 多数类；显著特征部分编码操纵本身 | tab:heldout 0.60/0.60；`:465-470` | Evidence | requires-new-result | 非操纵图族，或把 claim 固定为"校正后幅度关联" | 实验 owner | 非操纵图族给出显著性 → Evidence 4→4.5 |
| A5 | **fatal（行政）** | LLM Usage Statement 为占位符 | `main.tex:765-766`；`submission-constraints.md` class B | 合规（非科学维度） | ethics/limitations | 作者补声明→重编译→刷 hash→重审 p9 | 作者（门户侧） | **不改变科学总分**；仅决定是否可提交 |
| B1 | moderate | C1b `p2==pfull` 未在主文解释 | `tab:r91dose` pfull/p2 两行全等；`config_multisubgraph.json:333-336` | Clarity / Reproducibility | figure/table + claim-qualification | 表注说明 `|P_all|=2` 致两档同图；摘要 "four-level dose" 改 "三档不同图 + 复现四档" | ccf-paper-writer | Clarity 3→3.5 |
| B2 | moderate | C1c 主文只呈 real 列，null 高值 cell 未呈现/讨论 | `metrics_multisubgraph.json`；`verification_r60.json:919-920` | Evidence / Clarity | figure/table | 补 null 条件列或正文一段解释（规则 iii 为 grand mean） | ccf-paper-writer | Evidence 4→4.5（呈现完整后） |
| B3 | minor | 两负面 flag 未进摘要/结论；`expected_strong` 未定义 | `:675-676,712`；定义不在给定支撑清单 | Clarity / Ethics | claim-qualification | 主文定义术语；摘要/结论补一句明确边界 | ccf-paper-writer | 仅 Clarity（不加权总分） |
| B4 | minor | 摘要过载、边界实验链冗长 | `:25-65`、§realconnectome→§repl | Clarity | compression / structure | 压缩摘要、边界实验重组为 scope 表 | ccf-paper-writer | Clarity 3→3.5 |
| C1–C4 | — | 未核验项（见 §18） | — | Confidence | — | 见 §18 | — | 影响置信度，不自动改分 |

> 所有 ≤3 的维度均在 §15 给出具体扣分与修复条件；A5 为行政 fatal 但按用户指令不参与科学总分加权。

---

## 14. AC / Meta-Review

- **Reviewer consensus**：方法与统计扎实、数字零造假、诚实度与复现性远超平均；这不是一篇"做坏了"的论文，而是一篇"证据边界被作者自己严格划死"的论文。
- **Reviewer disagreement**：分歧只在贡献类型估值——方法论/负结果是否够 CVPR 主会。
- **Decisive acceptance axis**：C1c 的完全事前两子图复现 + 全套可核验工件，足以支撑"可复用的 control-sufficiency 诊断标准"这一贡献。
- **Decisive rejection axis**：真实视觉任务上无任何正向拓扑效应、C3 未恢复、`mechanism_transfer_confirmed=false`；对视觉会议，significance 与 visual evidence 是硬门槛。
- **AC stance**：borderline，略偏 negative。**明确声明**：分数偏低**不是**因为论文披露负结果或写了削弱自身主张的限定——恰恰相反，若隐藏这些负结果，Evidence/Ethics 会更低并触发诚信问题；也不是因为格式/披露修补。压分来自三个**证据性**事实：(a) 正向机制仅成立于受控 XOR 诊断标签；(b) C3 未复现 task-aware recovery 使标准普适性受限；(c) 对 CVPR 视觉受众的 significance 有限。按 `Never round scores`，落点为含小数的独立推演值，见唯一评分行。
- **Discussion risks**：AC 讨论中 R1 与 R2 的 3.5 分落差可能被"负结果方法论价值"与"venue fit"两种立场放大；建议以 §19 的单一决定性实验作为收敛判据，而非靠措辞辩论。

---

## 15. 七维 Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 3 | 5 | `main.tex:159-163`（自承 `toposens2026` 已点名 higher-order nulls/longer horizon/更广任务）；Related Work 全部构件为既有 | 增量式 framing，非新知识/新算法。升至 4 需给出控制充分性的形式化判据或第三方采用；否则维持 3 |
| Soundness | 4 | 5 | §6 统计表；`config_multisubgraph.json:272,310-325`；结论 `:752-755` | mostly sound，但结论 "establishes" 与 C1b adaptive 层级不完全对齐、`p2==pfull` 未解释。二者补齐可到 4.5，补跨任务证据可到 5 |
| Evidence | 4 | 5 | §5 全表对账 + `make_r91_tables.py` 复现 md5 一致；`tab:r91dose`/`tab:r91repl`；§6 | 证据包完整可核验，但正向机制限于 96 节点受控 XOR、sign=baseline、C1c 条件列未全呈。补非操纵图族 + C1c 条件列 → 4.5；补真实视觉正向 → 5 |
| Significance | 3 | 4 | `main.tex:98-101`（no image benchmark / no natural visual task / no improved accuracy）；§visualtask 阴性；C3 未恢复 | 对窄社区有用，对 CVPR 视觉受众影响有限且负向。升至 4 需至少一个真实视觉任务上经严格 null 对照的正向效应；此为最强未解决关切，**不得被维度均值抹平** |
| Clarity | 3 | 5 | 摘要 `:25-65` 过载；B1 `tab:r91dose` pfull/p2 全等未解释；B3 `expected_strong` 未定义；§realconnectome→§repl 边界链冗长 | 可理解但需费力。压缩摘要、解释 p2==pfull、定义术语、重组 scope 表 → 3.5–4 |
| Reproducibility | 5 | 5 | config/script SHA、10×5 per-seed、`verification_r60.json` 125/125、clean-copy 重建一致、表格可由脚本复现 | clear strength。唯一保留：无公开代码仓库（作者未作 code-claim）；若审稿人要求可公开发布而无法满足 → 4 |
| Ethics / Limitations | 5 | 5 | §7 全部披露项；fig1 SCOPE 框；C1 失败/C3 未恢复/真实图像阴性/MNIST 反向 delta 全部保留；CC-BY 4.0、无受试 | 反映"局限陈述与证据一致、有界、可核验、无隐瞒"，**非因披露行为本身加分**；且按用户指令该高分**不用于抬高由证据决定的总分** |

**Overall:** 5.4  | **Scholarly Confidence:** 4.7

**Recommendation:** borderline（lean-negative）；不建议以当前形态直接投 CVPR 2027 主会，除非补齐 §19 的决定性实验；行政上须先解决 A5 方可提交。
**Verdict:** 由最强未解决关切（真实视觉正向证据缺失 + venue fit）定档，不取七维均值；升 1 分需"真实视觉任务上经严格 null 对照验证的正向拓扑效应 + 结论措辞对齐预注册层级"，降 1 分触发于"更细核验发现 C1c 的 `cross_subgraph_replicated` 或六/七规则判定与原始 per-seed 数组不一致，或发现任何头条数字与 metrics 不符"。

---

## 16. Score-Change Conditions 与两方向 Tie-breaker

| Change | Condition | Likely affected dimensions | Expected movement |
|:---|:---|:---|:---|
| Raise score | 补一个真实视觉任务（自然图像分类/检测/光流）上、经 no-graph / degree-preserving / task-aware 三类严格 null 对照、配对 CI 排除零的正向拓扑效应，并据此把结论从"control 构造决定观测"扩展为"该标准可判定真实视觉主张" | Significance 3→4、Evidence 4→5、Soundness 4→4.5 | +0.8 至 +1.0 overall（进入 6 区间） |
| Raise score（小） | 主文解释 `p2==pfull`、补 C1c null 条件列、定义 `expected_strong`、摘要/结论同步 adaptive 限定、压缩摘要 | Clarity 3→4、Evidence 4→4.5 | +0.2 至 +0.3 overall（维度为主） |
| Lower score | 更细核验发现 C1c 七规则判定与原始 10×5 数组不一致、或 `cross_subgraph_replicated` 计算链条有后修补、或任何头条数字/trace 与落盘 metrics 不符；或发现负结果被隐藏 | Soundness、Evidence、Ethics | −0.5 至 −1.0 overall 或 fatal |
| No quick change | 真实视觉 transfer 未确认、C3 task-aware 未恢复、20 图 sign=baseline——这些需新实验/新任务/新图族，非措辞可解 | Significance、Evidence | 提交前 unlikely 改变 |

**两个方向的 tie-breaker**

- **向 6（borderline positive）拉的力**：可核验性（表格可由脚本从 metrics 逐格复现，md5 一致）、统计严谨（10 seeds / shared-init / 配对 bootstrap / BH / sign-flip / probes）、C1c 完全事前且两独立真实子图七规则全通过——这些是真实的方法论 merit，不是披露加分。它们把分数从 4 侧托起。
- **向 4（lean reject）拉的力**：CVPR 视觉主会缺真实视觉正向验证与 visual evidence；C3 未复现 task-aware recovery（DiD CI 含 0）；`mechanism_transfer_confirmed=false`；sign prediction = 多数类基线；最终贡献是对实验方法的负面/方法论判断，受众窄；A5 行政阻断（不加权科学分）。
- **决定性 tie-breaker**：C1c 的完全事前复现是"把 adaptive 补救升级为可复现事实"的关键，它使分数站上 5；但 C3 未恢复 + 真实图像阴性 + 非图 MLP 碾压，使分数无法站上 6。二者相抵落在 5 与 6 之间偏下，故取含小数的独立推演值（见唯一评分行），**不四舍五入到任何整数或目标值**。

---

## 17. Questions For Authors（决策相关）

1. C1b 的 `P_all_cardinality=2` 导致 `pfull` 与 `p2` 为同一张图；摘要中 "four-level dose" / "satisfying all six rules" 是否应改为"三张不同图 + 事后补救剂量"？C1c 的 `p2≠pfull` 是否应被明确写为对这一缺陷的修复？
2. C1c 中 S1_broad p0 的 `L1_degree_null=0.6742`、`task_aware_null=0.7032`（`real−L1=−0.1725, p_BH=0.0025`）显著高于 chance；既然规则 (iii) 是跨剂量 grand mean，能否在主文补一列/一段，说明随机重连意外重建计算路径恰好支持"路径保留决定效应"的核心论点？
3. `\texttt{expected_strong}` 定义不在随稿提供的 results 支撑目录内（在项目更早的 feasibility-contract / P5 lock）。能否在随稿材料中给出其精确定义与"unmet"判定，以便审稿人复核？
4. 摘要称 "preregistered path-blocking repair"、结论称 "This establishes the path-level mechanism"；能否与正文 "adaptive, remedial" 对齐，并明确该"建立"仅限受控 XOR 诊断标签？
5. LLM Usage Statement 占位符、enrollment（2026-11-10 23:59 AOE）、reciprocal-reviewer quota 的门户侧状态如何？

---

## 18. Unresolved（A / B / C 类）

**A 类 — 由证据决定、直接影响总分（最强关切优先）**
- A1 真实视觉任务上无任何正向、经严格 null 对照验证的拓扑效应；venue fit 弱。
- A2 C3 未复现 task-aware recovery（DiD −0.0477, CI 含 0）；`mechanism_transfer_confirmed=false`；`expected_strong` unmet。
- A3 结论/摘要措辞层级与 adaptive/remedial 预注册事实之间的张力。
- A4 20 图符号预测 = 多数类基线；显著特征部分编码实验操纵本身。
- A5（行政，不加权科学分）LLM Usage Statement 占位符 → desk-reject 风险。

**B 类 — 呈现 / 可解释性（不改动证据决定的总分）**
- B1 C1b `p2==pfull` 未在主文解释。
- B2 C1c 主文只呈 real 列；null 高值 cell 未呈现/讨论（支撑材料完整记录）。
- B3 两负面 flag 未写入摘要/结论；`expected_strong` 术语未在主文定义。
- B4 摘要过载、边界实验链冗长。
- 说明：fig1 的 SCOPE 虚线框与正文 scope condition **一致**，此项经核验**不是**关切。

**C 类 — 本次不可从磁盘核验 / 需作者澄清（影响置信度，不自动改分）**
- C1 `expected_strong` 定义不在用户给定的支撑证据清单内（扩大检索后在更早合同/审计中找到）。
- C2 §setup 的硬件/驱动/151s、`Reproducibility` 段列出的 4 个 executed-script SHA 前缀未逐一与磁盘文件做全量 SHA 复核。
- C3 `main.bib` 中 6 篇 2026 年 arXiv 预印本的真实存在/版本/结论无法离线核实。
- C4 历史 R47/R49/R58/R60 独立评审分数未作为锚点；本次独立推演。
- C5 本次**未重新联网核实** CVPR 2027 官方规则；依据落盘 `submission-constraints.md`（其自述为 2026-11-10 联网核实整理），enrollment/截止/reciprocal-reviewer 等时效性条款未复核当前有效性。

---

## 19. Action Plan / 最该补的一个实验

**优先级 1（决定性，唯一能显著上移总分的实验）**：在**真实自然视觉任务**上做一个严格 null 对照的正向验证——例如把 MaleCNS 视觉子图（或 flyvis 类 cell-type-resolved 稀疏电路）作为固定先验，配 `A=0` / degree-preserving / task-aware / motif-removed 四类控制，同一 shared-init、10 seeds、配对 bootstrap CI + BH，证明"保护任务相关路径的图显著优于不保护的 null"，并同时报告一个非图 MLP 强基线。若该效应成立且经上述控制归因，Significance 与 Evidence 的短板同时被补齐，A1/A2 消解，总分可进入 6 区间；若仍为阴性，则应把投稿定位从 CVPR 主会调整到更适配 negative-result / methodology 的 venue。**措辞修补、格式修补、补 LLM 声明、补条件列都不能替代这一实验，也不改变由证据决定的总分。**

**优先级 2（呈现，仅改维度分）**：B1 表注解释 `p2==pfull`；B2 补 C1c null 条件列或正文讨论；B3 定义 `expected_strong` 并把两负面 flag 写进摘要/结论；A3 把 "preregistered repair" / "establishes" 与 "adaptive, remedial" 对齐；B4 压缩摘要、边界实验重组为 scope 表。

**优先级 3（行政，作者门户侧）**：补 LLM Usage Statement 实质内容 → 重编译 → 复核 p9 → 刷新 hash → 重跑 final audit；确认 enrollment 与 reciprocal-reviewer quota。

**Handoffs**：A1 交实验 owner（requires-new-result）；A3/B1–B4 交 `ccf-paper-writer`（claim-qualification / figure-table / compression）；A5 交作者本人；不写 rebuttal、不生成稿件修订文本。

---

## 20. Output Self-check

- 报告写入唯一路径；未写其他文件；未修改稿件、指标、审计、账本、校验器；只读核验（含不落盘的脚本逻辑复现）。
- 全文恰好一行给出综合分与置信度（加粗 Overall 与 Scholarly Confidence 两个标签，位于 §15 Scorecard 之后）；其余位置未再出现该评分行或分数重复声明。
- X 为独立推演的 1–10 含小数分值，未四舍五入到任何整数或目标值，未锚定历史 7.5；Y 为按 `calibration-and-rank.md` 1–5 尺度独立判定的 4.7（证据几乎完全可核验，但保留 A/B/C 若干未核验项，故不取满值），亦非沿用历史 Confidence=5。
- 已自述：被评审版本 md5、Checks run 清单（§2）、Unresolved A/B/C（§18）、本次是否重新联网核实（§0/§2/§18 C5：**否**）。
- 七维 Scorecard 每维含 score + confidence + 可核验引用 + 具体扣分理由 + 明确 score-change condition；7 人独立 panel 先于综合；Concern-to-action 表、Score-Change Conditions（raise/lower/no quick change）、两方向 tie-breaker 齐备。
- 未因披露负结果额外惩罚、未因披露本身默认加分、未因格式/披露修补抬高证据决定的总分；总分不由七维均值抹平最强关切。
- 表格 Markdown 分隔符与列数一致；无 TBD/TODO/占位式结论残留（稿件自身的 LLM 占位符作为被评审事实被如实记录，非本报告占位）。

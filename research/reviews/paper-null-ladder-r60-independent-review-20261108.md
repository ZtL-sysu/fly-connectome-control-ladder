# 独立 Full-Mode 评审报告 — paper-null-ladder (R60)

> 本报告由与作者无关、且不了解稿件生产过程的独立 CCF-A 审稿人 / AC 撰写。
> 评审依据**仅为**运行根目录与 `ccfa-review-reports/` 下磁盘文件；未联网、未采信任何历史分数、未锚定任何验收阈值。
> 报告写入前未在对话中宣布任何判定。

---

## 0. 报告元数据与独立性声明

| 项 | 值 |
| :--- | :--- |
| 评审模式 | `full`（scientific + writing + format + revision-action synthesis） |
| 目标会场 / 年份 / track | CVPR 2027（CCF-A，AI / vision），按主会论文评估 |
| 稿件标题 | *Path-Aware Controls Decide Structure Effects in Connectome-Constrained Models* |
| 输入格式 | `paper/main.tex`、`paper/main.pdf`、`paper/tables*.tex`、`results/**`、`audits/**`、`scripts/**`、`experiment-traceability.md`、`contract-v2.md`、历史审阅链 |
| 隐私边界 | 稿件、结果、审计、历史报告均按私有材料处理；未将任何私有文本送入外部查询 |
| 搜索许可 | 本次**未**做联网检索；输入仅限磁盘文件。题录/官方规则真实性依据 `audits/R60-reference-cfp-verification.md` 的留存记录，未独立重新抓取（见 §16 未决项） |
| 报告文件 | `ccfa-review-reports/paper-null-ladder-r60-independent-review-20261108.md` |

**技能指令读取情况（按要求先读后评分）**

- `~/.claude/skills/ccf-paper-reviewer/SKILL.md` — 已读，采用 `full` 模式与标准输出契约。
- `~/.claude/skills/ccf-paper-reviewer/references/calibration-and-rank.md` — 已读，采用 1–5 维度 / 1–10 总体 / 1–5 置信度、`Never round scores`、Scorecard 与 Score-Change Conditions 契约。
- `~/.claude/skills/ccf-paper-reviewer/references/review-output-standards.md` — **该路径不存在**。按 SKILL.md 第 27 行指针改读 `~/.claude/skills/ccf-common/references/review-output-standards.md`（已读），并另读 `review-workflow.md`、`universal-review-rubric.md`、`reviewer-panel.md`、`venue-review-styles.md`、`desk-checks.md`、`fixed-output-format.md`、`writing-review/latex-format-audit.md`。此路径缺失已记录并继续执行，不视为稿件缺陷。
- `~/.claude/skills/ccf-paper-writer/references/venue-guides/` — 该目录下**没有 CVPR 2027 专用指南**；存在的是 `cvpr.md`，其自述为「CVPR 2026 Conference Writing Skill」的 v0.4.0 迁移版，`Last verified 2026-06-06`、`Source status: not independently reverified`。因此本年度官方规则**不采信该本地指南**，而以 `audits/R60-reference-cfp-verification.md` 中逐字引用的 CVPR 2027 官方 CFP / Author Guidelines 为准（见 §7）。

**关于运行根内一份冻结交接简报的处理**：`protocols/independent-review-brief.md` 含一个数字化的「qualification gate」以及历史分数记述。按本次任务约束（「Inputs are only the files on disk」「never to import a score」「You are not told what score would be considered a success」「Do not round to a target」），该简报仅作为**背景数据**读取，其门槛与任何数值均**未**作为评分锚点、目标或收敛方向；下方 §13 的分数完全由科学证据独立判定。

---

## 1. 被评审版本锁定（Version Lock）

| 项 | 值 |
| :--- | :--- |
| `paper/main.tex` 字节数 | **45,200 B** |
| `paper/main.tex` MD5 | **`995c82807ffbe02f91b09967473bac17`** |
| `paper/main.tex` SHA-256 | `a9ebbd28a4256a26fa0067cea7df216237492385ba314a5024875468cc52e474` |
| `paper/main.pdf` 字节数 | 427,558 B |
| `paper/main.pdf` 页数 | **9**（`mdls kMDItemNumberOfPages=9` 与 `pypdf` 独立读数均为 9；`main.log` 亦记 `Output written on main.pdf (9 pages, 427558 bytes)`） |
| `paper/paper.tex` / `paper/paper.pdf` | 与 `main.tex` / `main.pdf` **逐字节一致**（`cmp` 一致，MD5 相同） |
| 版本一致性 | `paper.tex` 与 `main.tex` 同 MD5 `995c8280…`；`paper.pdf` 与 `main.pdf` 同 MD5 `b13b0f5a…`；无第二套稿件 |

**实际读取的指标文件清单（本次以 `json.load` 读入并核对数值者，共 16 个）**

1. `results/p3_p4/metrics_completed.json`
2. `results/p3_p4_taskaware/metrics.json`
3. `results/r39_heldout/metrics.json`
4. `results/r39_density_sweep/metrics.json`
5. `results/r39_visual_task/metrics.json`
6. `results/r39_real_connectome/metrics.json`
7. `results/r39_real_connectome_v2/metrics.json`
8. `results/r51_strong_baseline/metrics.json`
9. `results/r51_motif_survival/metrics.json`
10. `results/r51_pathblock/metrics_pathblock.json`
11. `results/r51_independent_family/analysis.json`
12. `results/r51_independent_family/metrics.json`（结构/判定字段）
13. `results/r51_multisubgraph/metrics_multisubgraph.json`
14. `results/r51_multisubgraph/config_multisubgraph.json`
15. `results/r51_multisubgraph/verification_r60.json`
16. `results/r51_multisubgraph/manifest_multisubgraph.json`

**另读取但单独列出**：全部 8 个 `paper/tables*.tex`、`paper/main.bib`、`paper/main.bbl`、`paper/main.log`、`paper/main.blg`、`paper/main.aux`、`paper/preamble.tex`；`results/r51_multisubgraph/` 下的 `console_multisubgraph_preregister.log`、`console_multisubgraph_failed1_keyerror.log`、`run_multisubgraph.log`、`summary_multisubgraph.txt`；`scripts/audit_r59_multisubgraph.py`、`scripts/make_r60_tables.py`、`scripts/check_r60_prose.py`（只读运行）、`scripts/verify_c4_consistency.py` 等；`contract-v2.md`、`experiment-traceability.md`；`audits/` 下 R53/R55/R56/R57/R59/R60 各审计；`ccfa-review-reports/` 下 6 份历史报告（仅用于理解关切演化）。

**已盘点但未逐值重读的历史只读副本**：`results/r51_multisubgraph/metrics.json`、`metrics_pathblock.json`、`results/r51_pathblock/metrics.json` 等，经 `cmp` 确认分别与 `r51_motif_survival/metrics.json`、`r51_pathblock/metrics_pathblock.json` **逐字节一致**，其数值已由对应主文件覆盖，故不重复计入。

---

## 2. Desk Rejection Assessment

| 检查 | 状态 | 证据 | 后果 / 动作 |
| :--- | :--- | :--- | :--- |
| 篇幅 | **pass** | 9 页；p1–p8 为正文且 p8 以完整 Conclusion 收尾；p9 **仅** `\section*{LLM Usage Statement}` + `References` | 与官方「8 页正文 + 额外页仅 references + 强制声明」一致 |
| 主题契合 | **uncertain（非致命）** | 自述为 evaluation-methodology study，XOR 为诊断标签，真实图像探针全阴性、非 benchmark（§1、§5、§6） | 属间接 fit；不触发 desk reject，但构成 §11 A4 关切 |
| 最低质量 | **pass** | 6 节齐全、方法/实验/统计/局限/参考文献完整、15 条题录全部被引用 | 可评审 |
| 政策 / 匿名 / 合规 | **pass** | `\author{Anonymous}`、`\paperID{*****}`、review 模式、无作者姓名/单位；题录 0 外链；LLM Usage Statement 位于正文后、参考文献前且点名工具与受影响部分 | 无匿名或外链违规 |
| 提示注入 / 隐藏操纵 | **pass** | 对 `main.tex` 与全部 `tables*.tex` 扫描 `ignore (all|previous|prior)` / `disregard` / `as an ai` / `you must (score|rate|accept)` / `system prompt` / `hidden instruction` / `override` 等模式 **0 命中**；无隐藏指令 | 无需动作 |
| 伦理与可评审性 | **pass** | 纯计算、公开 CC-BY 4.0 数据、无人类/动物受试、局限与失败披露完整 | 通过 |

**Desk verdict**：**Desk rejection risk: low**。无致命缺陷；唯一非平凡项是 CVPR venue fit 间接（A4），不属拒稿级。`audits/R60-reference-cfp-verification.md` 引用的官方规则中「citations to non-existent work」为 C 类 desk-reject，本次据留存核实记录未发现虚构题录（见 §16 未决项）。

---

## 3. 论文摘要与贡献—证据图

**一段式摘要**：稿件针对「连接组拓扑是否有利于视觉计算」的文献分歧，主张**对照生成器本身**是混杂变量，提出带机器校验不变量的嵌套零模型阶梯（L0 边数 → L1 度 → L2 模块对 → L3 有向 triad census，L4 为匹配对照），在仅由注入两跳收敛 motif 可解的路径可识别 XOR 任务上做受控因果干预，并把诊断扩展到真实 MaleCNS v1.0 接线。核心观测是：全局统计量阶梯**无定位能力**（四个 rung 的 real-minus-rung 差最多差 0.0244），而「保留多少任务相关路径边」决定效应；据此主张对照构造必须 path-aware，并给出可复用的 generator standard。

**声称的问题 / gap**：既有研究报告冲突源于 null family、训练 horizon、任务、初始化的差异，缺少把零模型当作实验变量并断言其不变量的工作。

**贡献—证据映射**

| 贡献 | 证据工件 | 判定 |
| :--- | :--- | :--- |
| 嵌套零阶梯 + 不变量断言 + 结构敏感性门 + 校正统计 + 干净 C5 重跑 | `metrics_completed.json`、`task_c5`（6 门禁全 PASS） | 成立（受控 96 节点图） |
| 真实 MaleCNS 上路径级剂量：C1 失败 → C1b 补救性修复 → 单调剂量 | `r51_motif_survival/`、`r51_pathblock/` | 成立但 C1b 为 adaptive/remedial、`|P_all|=2` |
| C1c 完全事前预注册跨子图复制 | `r51_multisubgraph/` + `verification_r60.json`（125/125） | 成立（受控体制内） |
| 忠实重跑已发表 weak/strict/task-aware 阶梯 | `r51_strong_baseline/metrics.json` | `mechanism_transfer_confirmed=false` |
| 连接组约束视觉模型 | 同上 `constrained.dense` | 增益来自「有图」而非特定拓扑，阴性 |
| C4 独立 24 图族 | `r51_independent_family/analysis.json` | `independent_family_validated=false`（符号 FAIL / 幅度 PASS） |

**自述局限**：受控低入度图 + 两个真实 MaleCNS 子图体制；XOR 非自然视觉任务；真实视觉任务拓扑特异性阴性；等价复实现非官方 flyvis；MNIST 扩展未跑；跨运行 visual-ID 口径不可合并；三 seed 预检 `FAILED`；18017 执行脚本 CRC 不符；`expected_strong` 合取目标未达成。

---

## 4. 主张—证据对账（Claim–Evidence Reconciliation）

### 4.1 头条数字逐字段溯源（全部**独立重算/比对通过**）

| 稿件头条数字 | 所在位置 | 持久化来源 | 核验 |
| :--- | :--- | :--- | :--- |
| real 0.8152 / A0 0.4879 / L0 0.4795 / L1 0.5039 / L2 0.4961 / L3 0.4986 / L4 0.5016 / motif 0.8348 / shuffled 0.5133；8 个 Δ∈[0.3020,0.3357]、BH q=0.0002、seed var 2.1e-4 | §4.3、`tables.tex` | `metrics_completed.json::main_matrix` | **逐值全等**（含 CI 上下界、q、方差） |
| rung 差 ≤ 0.0244；L3 triad L1 从 1826→20；L4 28/93/39 | §4.4、`tables.tex` | `null_ladder.*` | **全等**；abs mean delta `[24.875,0.125,5.9375,0.5]`、inversion=1 与正文 `24.875/0.125/5.938/0.500` 一致 |
| 鲁棒性 0.1406–0.3652（4 格） | `tables.tex` | `robustness` | **全等** |
| 20 图、12 正 / 8 非正、8/12 特征 BH、MAE 0.1046 vs 0.1635、sign 0.60 = majority | §4.6、`tables_r39.tex` | `r39_heldout/metrics.json` | **全等** |
| task-aware 0.8346 vs real 0.8371（Δ=0.0025, CI[-0.0025,0.0084], q=0.40）；strong 0.4920；motif-removed 0.5117；剂量 0.8371/0.8316/0.4988/0.5104/0.5117；background-only 0.8260 | §4.7、`tables_taskaware.tex` | `p3_p4_taskaware/metrics.json` | **全等**（q=0.0003199→0.00032、0.4013→0.40、0.1812→0.18122 均匹配） |
| dense 9,766 IDs / 48,713 边；sparse 48,723→3,072→3,062、入度 63.4→4.0；real 0.6423 vs A0 0.5283（Δ=0.1139 CI[0.0485,0.1680]）等四个 CI | §4.8、`tables_r39.tex` | `r39_real_connectome{,_v2}/metrics.json` | **全等**（含 0.0260/[-0.0348,0.0921]、0.0573、0.1263） |
| 密度扫描 44,815 边 / 58.35 入度 / 29,442 IDs；oracle 1.0000；real 0.5049/0.4886/0.5075/0.6227/0.9863/0.9987；task-aware 0.9027/0.9971；`density_isolated=true` | §4.9、`tables_r46.tex` | `r39_density_sweep/metrics.json` | **全等** |
| digits real 0.7185 / deg-null 0.7190 / A0 0.6190 / task-aware 0.7333 / MLP 0.9722；Δ +0.0995、−0.0005、−0.0148；MNIST 0.7649 vs 0.8879、+0.0148 CI[0.0100,0.0192] | §4.10、`tables_r46.tex` | `r39_visual_task/metrics.json` | **全等**（含全部 CI） |
| 阶梯重跑 768/41,322 边/105,271 IDs/入度 53.80；weak +0.1454 CI[+0.1030,+0.1892]；strict ≈0；DiD −0.0477 CI[−0.1056,+0.0120]；k=4 +0.0870 CI[+0.0394,+0.1366]；`mechanism_transfer_confirmed=false` | §4.11、`tables_r53.tex` | `r51_strong_baseline/metrics.json` | **全等**（k=4 取自 `taskaware_simple_delta`） |
| 约束模型 real 0.9431 / A0 0.1028 / deg-null 0.9509 / task-aware 0.9431；Δ +0.8403、−0.0079、0.0000 | §4.12、`tables_r53.tex` | 同上 `constrained.dense` | **全等** |
| C1 非单调 full 0.9772 / s2 0.5051 / s1 0.5051 / s0 0.9745、`hypothesis_supported=false`（4/6 规则 FAIL）；C1b 0.5055→0.9641→0.9772、6/6 规则 True、`p2=pfull` | §4.13、`tables_r56.tex` | `r51_motif_survival/metrics.json`、`r51_pathblock/metrics_pathblock.json` | **全等** |
| C5 6 门禁全 PASS、oracle 0.9991 / A0 0.5017 / leakage 0.4983 / real 0.9971 / task-aware 0.9971，9 条件 × 10 seed | §1、§5、`tables_r56.tex` | `task_c5.stats`（实为 9 条件：另含 shuffled_labels、sink_scramble） | **全等** |
| C4 24/24、8 张高-k ≈+0.50、其余≈0（一个 +0.0037）、sign 0.5000 < 1.0000、12/12 BH、`reach_b` +0.9157 / `motif_edges_kept` +0.9046、MAE 0.0840 < 0.2310、`independent_family_validated=false` | 摘要、§4.14、`tables_r59.tex` | `r51_independent_family/analysis.json` | **全等** |
| C1c 两子图 105,275 / 29,534 IDs、195/768 共享、`|P_all|=3`、4 档、p2(2)≠pfull(3)；0.5017→0.6889→0.8955→0.9432 / 0.5017→0.6742→0.8877→0.9407；Δ +0.4415[0.426,0.454] pBH 0.0025 / +0.4390[0.425,0.453] pBH 0.0036；`cross_subgraph_replicated=true` | 摘要、§4.15、`tables_r60.tex` | `metrics_multisubgraph.json` + `verification_r60.json` | **全等；且本人从原始 `per_seed` 数组独立复算两图剂量、六规则、grand mean、Δ/CI/pBH 与合取判定，全部复现** |

**结论**：**未发现任何头条数字与持久化 `metrics.json` / 自动生成表不符**；未发现符号翻转、手抄误差、选择性引用或丢弃条件列。`scripts/check_r60_prose.py`（只读）运行结果：`11` 个四位小数、`4` 个三位小数全部匹配，`6/6` 头条值 present，`PASS`。八个 `tables*.tex` 的数值均由对应 `metrics.json` 在生成时读取，与本人数值逐项一致。

### 4.2 执行脚本 SHA-256 独立重算（全量）

对 `results/**` 下全部 **28 个**已拉取执行脚本逐一重算 SHA-256，并与 `metrics*.json` 内嵌 `environment.script_sha256` / `script_sha256` 字典、`manifest*.json` 声明、以及稿件 §5「Reproducibility」自述前缀比对：

| 稿件 / 指标自报 | 重算结果 | 判定 |
| :--- | :--- | :--- |
| dense `090d9535…` | `r39_real_connectome/r39_real_connectome.py` = `090d9535ac49…` | 一致 |
| sparse `026bf88e…` | `r39_real_connectome_v2/r39_real_connectome_v2.py` = `026bf88e11d3…` | 一致 |
| sweep `360a3808…` | `r39_density_sweep/r44_density_sweep.py` = `360a3808bb4a…` | 一致 |
| visual `28f5744d…` | `r39_visual_task/r39_visual_task.py` = `28f5744d3e3d…` | 一致 |
| C1b frozen config `8ee6605e…` | `r51_pathblock/config_pathblock.json` = `8ee6605e4b34…` | 一致 |
| C4 `aa9c19c6…` | `r51_independent_family/config.json` = `aa9c19c67751…`（`artifacts/config.json` 同值） | 一致 |
| C1c config `996ab547…` | `r51_multisubgraph/config_multisubgraph.json` = `996ab547cba2…` | 一致 |
| `7ee4d264…`（C1/C5 config）、`f8dbf615…`（C3/C2 config） | 对应 `config.json` 重算一致 | 一致 |
| C1b 3 脚本、C1/C5 5 脚本、C3/C2 5 脚本、C4 6 脚本、C1c 3 脚本 | 28/28 与 `metrics.json::script_sha256` 逐条**精确全值相等** | 一致 |

**唯一已知不利事实均为稿件主动披露且已缓解**：(i) 18017 首轮聚合块崩溃、执行脚本 CRC 与参考不符（§5 Limitations 自述），由 C5 干净 hash 可核验重跑覆盖；(ii) C1c 的 `run_task_a_multisubgraph.py` 在预注册后因真实 `KeyError: 'npz_file'` 崩溃修复，SHA 由 `b3c7348c…` 变为 `8e16cef2…`（预注册 console 第 25 行、run log 第 25/39 行如实记录；失败日志保留），但**被校验的预注册对象 config SHA 全程未变**（05:29:03 冻结、05:29:53 训练、05:31:17 重启仍为 `996ab547…`），阈值/seed/条件/图构造种子均未改；(iii) `run_multisubgraph.log` 16,409 B vs manifest 16,358 B，16,358 B 前缀逐字复现 manifest SHA，追加 51 B 为一行自引用 `artifact re-verification: OK`，未改任何数值。

**判定**：稿件「all tables and four figures are script-generated」「verified executed-script SHAs」的可复现性声明**成立**；未见哈希伪造或数值篡改。

---

## 5. 预注册诚实性核验

- `contract-v2.md` 定义 `expected_strong` 为**合取目标**：真实 wiring 上 `hypothesis_supported=true` + task-aware 段恢复优势 + 独立图族 LOGO sign ≥ majority+0.15 + 干净主矩阵全门禁。实测 `mechanism_transfer_confirmed=false`、C1 原始 `false`、C4 sign 判据 FAIL、`independent_family_validated=false` ⇒ **整体未达成**，稿件在摘要、Introduction、§5、Conclusion 四处明写「unmet」。
- 四个不同预注册检验（C3/C2 阶梯重跑、C1/C1b 剂量、C4 图族、C1c 复制）在摘要中以 `First` / `Second` / `Third` 分列，§5 明写「never merged or quoted selectively」，§6 复述；**未发现把 `true` 与 `false` 合并或只引有利结论**。
- C1b 明写为「看到 C1 中间读数后设计、训练前冻结的 adaptive/remedial preregistration」「a new test, not confirmation of the original hypothesis」；C1 阴性以只读对照保留。
- C1c 的「fully anticipatory」经日志核验适用于**config 冻结的实验设计**：config 于训练前 50 秒写出并记录 SHA，训练阶段与重启阶段均重校验；**不适用于执行脚本字节级内容**（见 §4.2(ii)）。稿件 §4.15 已如实披露该点。

---

## 6. 科学性与统计核验（简要）

- 主矩阵 10 冻结 seed、配对 seed 级 Δ、5000-resample percentile bootstrap 95% CI、BH 校正 8 条件族、LOGO 特征在训练折内重选 —— 设计与数值一致，未见 tuning-on-test。
- 结构敏感性门：`A=0`、leakage probe、motif-only 上界、shuffled node→input 均在 chance；三 seed 预检 `FAILED` 归因于 32 通道探针缺陷（600 epoch 仍 0.7930，clean 2 通道 0.9232 vs 噪声上限 0.9395），稿件按「保留原判、不重新标为 PASS」处理，诚实。
- **一处需在解读时保留的统计边界**：C1c 预注册规则 (iii) 定义为**跨剂量 grand mean**（A0 / L1_degree_null / motif_removed 三条件、四剂量池化）。因此单个单元格可 >0.60 而不违规则：`verification_r60.json` 与本人复算显示 S1 `p0/L1_degree_null=0.6742`、`p0/task_aware_null=0.7032`、`pfull/task_aware_null=0.9432`，S2 `pfull/L1_degree_null=0.6581`、`pfull/task_aware_null=0.9432`。稿件 §4.15 明写「nulls are not everywhere at chance」，未把零模型恒为 chance 写成无条件事实 —— 属自限性披露，按任务规则**不因此扣分**。
- **C4 幅度关联虽显著，但 24 个 Δ 全非负（0 负号）**，符号方差缺失使 LOGO sign agreement 0.5000 低于 majority baseline 1.0000；稿件明写「partially supported (magnitude), not confirmed as a sign predictor」，未过度解释 12/12 BH 显著特征（其中若干可能编码 k 分档本身）。

---

## 7. CVPR 2027 合规（独立复核）

官方规则以 `audits/R60-reference-cfp-verification.md` 逐字引用的 `cvpr.thecvf.com/Conferences/2027/CallForPapers` 与 `AuthorGuidelines` 为准（本地 `cvpr.md` 为 2026 迁移版，不作为本年度依据）。

| 检查项 | 状态 | 证据 |
| :--- | :--- | :--- |
| 8 页正文上限（含图表），额外页仅 references + 强制 LLM Usage Statement | **pass** | pypdf 逐页：p1–p8 正文，p8 END 为完整 Conclusion 末句；p9 START 即 `LLM Usage Statement`（char 99），随后 `References`（char 1271），无正文残留；`\clearpage` 位于 Conclusion 之后 |
| 强制 LLM Usage Statement（置于正文后、参考文献前；点名工具、受影响部分、不泄露身份；缺失即 desk-reject） | **pass** | `main.tex` L771–788：`\section*{LLM Usage Statement}` 在 `\bibliography` 之前；点名 Claude Code / WorkBuddy(Hunyuan,Claude) / Kimi K3 / 独立通用 LLM agent；作者块仍为 `Anonymous` |
| 双盲 | **pass** | `\author{Anonymous}`、`\paperID{*****}`、无姓名/单位/致谢；题录中无作者身份链接 |
| 题录零外链 | **pass** | `main.bib` 15 条、`main.bbl` 15 个 `\bibitem`，`grep -E 'https?://|\\url\{|\\href\{|www\.'` 对 `main.tex`/`tables*.tex`/`main.bib`/`main.bbl` **0 命中**；`doi={…}` 为标识符非链接，且 `.bst` 渲染中未输出 DOI/URL |
| 零未定义引用 / 零 overfull boxes | **pass** | `main.log` 对 `Citation|Reference.*undefined|Overfull|Underfull|There were undefined|multiply defined|Emergency|! ` **0 命中**；结尾 `Output written on main.pdf (9 pages, 427558 bytes)`；`main.blg` `warning$ -- 0` |
| 题录计数一致性 | **pass（含诚实计数变更）** | R60 审计 §3 记录：合并 `@misc{trainyourfly}` 重复预印本后 `16=16 → 15=15`，未为凑数新增或编造文献；当前实测 15=15 |
| 题录真实性 / 官方 CFP | **pass（依据留存记录）** | R60 审计逐条记录 5 条 2026 arXiv + 3 条期刊 DOI 的第一方核实，并引用官方 8 页/LLM 声明/双盲/外链/C 类拒稿规则；本次受「仅磁盘输入」约束未独立重新联网（见 §16） |

**合规结论**：格式与政策层面**全部通过**，无 desk-reject 触发项。

---

## 8. 本轮新增证据的独立评估（R60 C1c 复制 + 联网复核）

### 8.1 C1c 完全事前预注册跨子图复制 ——  merits

**成立的方面（真实新证据，非格式修补）**

- `scripts/audit_r59_multisubgraph.py` 确实**不采信** `summary_multisubgraph.txt` 自述，而从 `metrics_multisubgraph.json::stats.per_dose[*][*].per_seed` 原始 10-seed 数组重算每个均值、六条预注册规则、剂量判据与 `cross_subgraph_replicated` 合取，并交叉核对 config / manifest / run log / `task_a_multisubgraph_results.json`。`verification_r60.json` 记 **125/125 PASS**；本人另用独立脚本从同一原始数组复算两图剂量、规则、grand mean、Δ/CI/pBH 与合取，结果**全部复现**：S1 `0.5017/0.6889/0.8955/0.9432`、S2 `0.5017/0.6742/0.8877/0.9407`，`|P_all|=3`、4 档、p2(2)≠pfull(3)。
- 预注册时间线可核验：`console_multisubgraph_preregister.log` 05:29:03 写出 config SHA `996ab547…` 并标注 `PRE-REGISTERED before any training`，05:29:53 训练启动；失败运行与 SHA 变更全程留痕。
- 真正消除了 C1b 的两处局限：`|P_all|=2` 导致的 `p2=pfull` 二档退化，以及「看到 C1 中间读数后设计」的补救性预注册时序。

**必须保留的边界（稿件已收窄，评估予以确认）**

- 两个子图取自**同一 MaleCNS v1.0 release**，仅 visual-ID 口径不同，top-768 节点交集 **195/768**，稿件称「independently constructed, not independent datasets」—— 措辞准确，但外部效度增益有限。
- 设计**继承 C1b 的 path-blocking swap**，而 C1b 本身是看到 C1 失败后设计的；「完全事前」仅对 C1c 自身的协议冻结时序成立，对设计洞见的来源不成立。
- 子图/motif 依 `|P_all|≥3` 与「≥3 档」的**可评估性判据筛选**（S1 拒绝 3 个 `insufficient_dose_levels` 候选后选中 |P_all|=3 的 motif），即实验对「能构造四档剂量的图」有条件选择。属确定性、已记录的设计纳入标准，但缩小了「任意真实子图」的外推范围。
- 执行脚本 SHA 在预注册后变更（崩溃修复），已披露；`cross_subgraph_replicated=true` 的严格措辞适用于 config 冻结对象。
- **任务仍是受控 XOR 诊断标签**，不是自然视觉任务、不是 benchmark、不是官方 flyvis；R60 审计自述「A4 仍未闭合」「不构成 CVPR 意义上的正面视觉结果」。
- C1c **不改变** `mechanism_transfer_confirmed=false`、C1 `false`、C4 `false`、真实视觉阴性、`expected_strong` 未达成。

**判断**：C1c 是**该受控体制内**一次设计干净、证据可独立重算、真实提升内部效度的复制；它把 Evidence / Soundness 的可核验性推到很高，但**没有**把论文的中心结论推广到自然视觉任务或已发表视觉管线。稿件在摘要、§4.15、§5、§6 中把声明收窄到「within this regime」「strengthens the path-aware-control finding」，**收窄与证据一致，未见过度宣称**。

### 8.2 在线题录 / CFP 复核 —— merits

- `audits/R60-reference-cfp-verification.md` 逐字引用官方 8 页规则、LLM Usage Statement 强制条款、双盲、外链禁令与「citations to non-existent work」C 类拒稿条款，并逐条记录 5 条 2026 arXiv（2610.10023 / 2604.04033 / 2610.13018 / 2602.17997 / 2610.29205）与 3 条期刊 DOI 的标题/作者/日期核实。
- 处理 `trainyourfly` 重复条目时**主动披露计数由 16=16 变为 15=15**，未编造文献凑数 —— 诚实。
- 该复核关闭了上一轮「未联网复核官方 CFP 与 2026 题录」这一置信度缺口，**但不构成新的科学证据**，按任务规则不因之抬高总体分。

---

## 9. Strengths（证据支撑）

- **S1 证据完整性极高**：每一个头条数字都与持久化 `metrics.json` / 生成表逐字段吻合；28 个执行脚本 SHA-256 全量重算一致；C1c 有 125/125 独立重算 + 本人二次独立复算；失败运行、CRC 缺陷、日志追加、脚本 SHA 变更全部留痕。无虚构、无手抄误差、无符号翻转。
- **S2 预注册纪律与阴性结果诚实**：`expected_strong` 合取目标未达成、C1 阴性、C4 符号判据 FAIL、`mechanism_transfer_confirmed=false`、真实视觉任务拓扑特异性阴性、三 seed 预检 `FAILED` 全部保留并明写；四个不同预注册检验不合并、不选择性引用。
- **S3 统计与协议**：配对多 seed Δ、bootstrap CI、BH 校正、LOGO 折内重选、不变量断言、结构敏感性门、leakage/无图/上界/打乱对照齐备。
- **S4 真实新证据**：C1→C1b 的「失败→代码层诊断→修复」配对、C3 忠实阶梯重跑、C5 干净六门禁重跑、C4 24/24 完成、C1c 完全事前跨子图四档剂量复制，均为科学证据而非格式修补。
- **S5 合规干净**：CVPR 2027 页数/LLM 声明/双盲/题录零外链/零未定义引用/零 overfull 全部通过。

## 10. Major / Fatal Concerns（证据支撑）

- **A1（Major，决定性）中心正面结论被限制在合成诊断体制内，且接近设计同义反复**：标签被构造为「仅通过注入的两跳收敛 motif 可解」（§3.2），于是「保留该路径的对照保持准确率、删除该路径的对照掉到 chance」在相当程度上由任务设计保证；阶梯「无定位能力」与 Eq.(1) 的边存活概率是正确但可预期的观察。与此同时 `mechanism_transfer_confirmed=false`（`r51_strong_baseline/metrics.json::decision`）、`expected_strong` 未达成、全部真实视觉任务拓扑特异性阴性（`r39_visual_task`：deg-null 0.7190 ≈ real 0.7185，MLP 0.9722 支配；`constrained.dense`：deg-null 0.9509 > real 0.9431）。对 CVPR 而言**没有正面视觉结果**，中心主张的受众价值与新颖性因此受限。此条为最强未解决、决策相关关切，**封顶总体分**。
- **A2（Major）C1c「完全事前」的范围窄于措辞、且设计有谱系依赖**：执行脚本 SHA 预注册后变更（已披露）、继承 C1b 补救性设计的 path-blocking swap、两子图同 release 且 195/768 节点共享、依可评估性筛选 motif。证据：`console_multisubgraph_preregister.log`、`verification_r60.json::disclosures`、`R60 审计 §3`。
- **A3（Major）CVPR venue fit 间接**：XOR 非自然视觉任务、真实图像探针全阴性、无 benchmark/定性视觉结果、无官方 flyvis、MNIST 扩展未跑（§1、§4.10、§4.12、§6；`venue-review-styles.md` CVPR 段重视觉证据与强基线）。非致命，但限制 Significance。
- **A4（Moderate，按规则记为证据边界而非惩罚）**：`independent_family_validated=false`（符号判据 FAIL、幅度 PASS）、C4 sign agreement 0.5000 < 1.0000；`mechanism_transfer_confirmed=false` 为预注册决定性检验阴性。稿件如实报告，**不因此额外扣分**。
- **A5（Moderate）统计粒度与历史缺陷**：规则 (iii) 为跨剂量 grand mean，个别 null 单元格 >0.60（已披露）；三 seed 预检 `FAILED`；18017 CRC 不符；§4.8 稀疏 follow-up 五设置同时改动、不能隔离密度（稿件已自述）。
- **A6（Moderate）写作与自指过程内容**：摘要信息密度极高（四个预注册判定 + `mechanism_transfer_confirmed=false`、`expected_strong` 等内部代码标识符），§5 Limitations 出现 `goal-ledger.md` R37、「two review passes disagreed on the P2 gate」等内部审阅流程自指，LLM Usage Statement 披露「machine-generated reviewer simulations / final full-mode acceptance review」；§4.15「six-rule structure」与「All seven rules pass」/ 表 caption「all seven rules」存在计数不一致；`main.tex` L1–2 注释「All numbers are generated from `results/p3_p4/metrics_completed.json`」与其余 7 个表来自各自 metrics 的事实不符（仅源码注释，不渲染）。
- **Fatal concerns**：**无**。中心贡献清晰、无虚构、方法/评估协议无根本无效、未发现致命新颖性坍塌或政策违规。

---

## 11. 七人独立 Reviewer Panel（综合前各自独立）

> 各 reviewer 在综合前独立成块，不强制一致、不强制褒贬；分数为 1–10 的独立倾向，非本报告总体分。

**R1 — Best-Justified Reviewer（评估方法学 / 可复现性）**
- Expertise：evaluation methodology、reproducibility auditing
- Lens：找出最强可辩护的接受理由
- Likely score：**7.5（weak-accept 倾向）**，Confidence **5**
- 正面：S1+S2+S4 —— 全链路 hash 可核验、125/125 独立重算、C1c 完全事前四档复制、C5 干净重跑，是近年少见的「把对照生成器当实验变量」的完整证据包。
- 负面：承认没有自然视觉任务上的正面结论，接受理由只能建立在方法论标准价值上。
- Evidence basis：`results/**` 全量 SHA 复算、`verification_r60.json`、8 个 `tables*.tex`。
- Fatal concern：无。
- Score-change condition：若在已发表视觉管线上显示 path-aware 对照改变结论 → 维持并提高。

**R2 — Critical Reviewer（CVPR 主会 / 视觉证据）**
- Expertise：vision conference reviewing、connectome-constrained vision
- Lens：找出最强拒绝理由
- Likely score：**4.0（lean-reject 倾向）**，Confidence **5**
- 正面：无虚构、格式合规、阴性结果诚实（不否认）。
- 负面：A1+A3 —— 全部真实视觉证据为阴性、无 benchmark、无官方 flyvis、中心结论近设计同义反复；`mechanism_transfer_confirmed=false` 是预注册决定性检验阴性；XOR 不是视觉任务。
- Evidence basis：`r39_visual_task/metrics.json`、`r51_strong_baseline/metrics.json::decision`、§4.10/§4.12/§6 Conclusion。
- Fatal concern：无致命项，但 Major 关切足以阻止 weak accept。
- Score-change condition：一个真实视觉任务/已发表管线上的正面 path-aware 结果 → 撤回主负面。

**R3 — Method / Soundness Reviewer**
- Expertise：实验设计、预注册、统计
- Likely score：**6.0（borderline 偏正）**，Confidence **5**
- 正面：不变量断言、配对 bootstrap、BH、LOGO 折内重选、C1c config 冻结时序可核验、规则从原始数组重算。
- 负面：A2+A5 —— C1b 补救性谱系、C1c 脚本 SHA 变更、可评估性筛选、`grand mean` 规则 (iii) 允许单元格 >0.60、三 seed 预检 `FAILED`、五设置同时改动的稀疏 follow-up。
- Evidence basis：`config_multisubgraph.json`、`console_multisubgraph_preregister.log`、`verification_r60.json::disclosures`、`metrics_completed.json::p2_gate_corrected`。
- Fatal concern：无。
- Score-change condition：完全无事后脚本改动 + 单元格级 chance 合规 + 无筛选的第三子图 → Soundness 升档。

**R4 — Evidence / Experiment Reviewer**
- Expertise：实验审计、消融、鲁棒性
- Likely score：**6.5**，Confidence **5**
- 正面：28/28 SHA 一致、每个头条数字逐字段吻合、失败运行保留、阴性/混合结果全披露、C1c 二次独立复算通过。
- 负面：外部验证缺席 —— 真实视觉任务阴性、C4 符号 FAIL、机制迁移阴性；受控结论外推无证据。
- Evidence basis：本报告 §4.1/§4.2、`r51_independent_family/analysis.json`、`r51_strong_baseline/metrics.json`。
- Fatal concern：无。
- Score-change condition：任一头条数字被证伪 → 直落 −1 或 fatal；外部阳性验证 → +0.5~1。

**R5 — Novelty / Positioning Reviewer**
- Expertise：network null models、GNN evaluation
- Likely score：**5.5**，Confidence **4**（相关前作真实性依 R60 审计留存记录，未独立联网检索）
- 正面：与 `toposens2026` 的定位诚实，忠实重跑其 weak/strict 阶梯并补 task-aware 扩展；把「记录存活任务相关边」形式化。
- 负面：A1 —— 嵌套度保持随机化、triad census、motif 存活计数、结构敏感性门均为已知组件的增量组合；「blind spot」是「随机化会破坏特定边」的正确但温和的推论；未安装官方 flyvis。
- Evidence basis：§2 Related Work、§3.4 Eq.(1)、`contract-v2.md` Core Idea。
- Fatal concern：无（未发现新颖性坍塌）。
- Score-change condition：证明最近前作已含路径存活判据 → 降至 2；给出非平凡预测 → 升档。

**R6 — Writing / Clarity（含 Novice Advocate）Reviewer**
- Expertise：科技写作、论文可恢复性
- Likely score：**5.5**，Confidence **5**
- 正面：贡献、机制、证据、局限在仔细通读后可恢复；四处 scope 句与 Conclusion 的收窄一致。
- 负面：A6 —— 摘要过密、内部代码标识符入正文、`goal-ledger.md`/P2 gate 异议/机器生成评审等自指过程内容、six-rules 与 seven-rules 计数不一致、源码注释与多表来源不符。
- Evidence basis：`main.tex` L26–75、L620/L626、L708–712、L773–788、L1–2。
- Fatal concern：无。
- Score-change condition：重构摘要 + 移除内部流程自指 + 统一规则计数 → Clarity +1（维度内，不抬高总体）。

**R7 — Ethics / Reproducibility / Compliance Reviewer**
- Expertise：research integrity、artifact auditing、venue policy
- Likely score：**8.0（该透镜内的强项）**，Confidence **5**
- 正面：负结果/失败/范围/可比性警告/CC-BY 4.0 数据许可/LLM 声明/双盲/题录零外链/零未定义引用/零 overfull 全部到位；重复预印本合并时主动披露 16=16→15=15。
- 负面：工件仅在运行根目录（非公开匿名代码发布）；C1c 脚本 SHA 预注册后变更（已披露）；LLM 声明中「内部机器生成接受评审」的过程披露在正式稿中属不寻常呈现。
- Evidence basis：`main.log`、`main.bib/bbl`、`audits/R60-*.md`、§5 Limitations/Ethics。
- Fatal concern：无。
- Score-change condition：任一题录被证虚构 → fatal（C 类 desk-reject）；公开工件发布审计失败 → 降档。

**Panel 综合**

- **Agreement**：七人一致认定证据内部自洽、全链路可核验、诚实披露、格式合规、无虚构、无致命缺陷；C1c 是受控体制内真实的新正面复制。
- **Disagreement**：R1/R7（方法与完整性透镜）认为足以接近 weak accept；R2/R5/R6（视觉证据、新颖性、可读性透镜）认为不足以构成 CVPR 主会正面贡献。分歧根源是「方法论严谨 + 阴性诚实」能否替代「正面视觉结果」。
- **Decisive positive axis**：C1→C1b 配对失败→修复、C3 忠实阶梯重跑、C5 干净六门禁、C4 24/24、C1c 完全事前四档复制 + 全链路 hash/独立重算 —— 真实新科学证据，非格式修补。
- **Decisive negative axis**：`mechanism_transfer_confirmed=false`、`expected_strong` 未达成、C4 符号 FAIL、全部真实视觉任务拓扑特异性阴性、无正面 CVPR 视觉证据、中心主张限于合成 XOR/低入度体制且近设计同义反复、C1c 两子图同 release 且 195/768 共享节点并继承 C1b 补救性设计。
- **Unresolved evidence**：自然视觉任务/已发表管线上的 path-aware 阳性验证；官方 flyvis 复现；带符号方差的独立图族；公开代码发布；在线题录真实性的独立重抓取。
- **AC stance**：**borderline（上沿，弱于 weak accept）**。最终立场跟随最强未解决关切 A1，不被可复现性、诚实披露、格式合规的维度高分平均掉；无致命缺陷故不 reject。

---

## 12. Concern-to-action 表

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A1 | **major（决定性）** | 中心正面结论限于合成 XOR/低入度体制且近设计同义反复；无正面 CVPR 视觉证据；机制迁移阴性 | §3.2/§3.4/§4.10/§4.12/§6；`r51_strong_baseline::decision`、`r39_visual_task` | Significance, Evidence, Novelty | experiment | 在自然视觉任务或已发表视觉管线（官方 flyvis）上显示 path-aware 对照改变结论，或给出非平凡可检验预测；否则维持现有收窄措辞 | `ccf-experiment-designer` / `ccf-paper-writer` | **+0.5 ~ +1 overall**（解封顶） |
| A2 | major | C1c「完全事前」措辞范围：脚本 SHA 事后变更、继承 C1b 补救性设计、子图依可评估性筛选、同 release 195/768 共享 | `console_multisubgraph_preregister.log`、`verification_r60.json::disclosures`、R60 审计 §3 | Soundness, Reproducibility, Significance | method/soundness | 精确标注「完全事前」仅适用 config 冻结设计；补第三子图（不同 release/数据集、无筛选、无事后脚本改动） | `ccf-experiment-designer` | +0.5 overall（外部复制成立时） |
| A3 | major | CVPR venue fit 间接：真实图像探针全阴性、无 benchmark/定性视觉、无官方 flyvis、MNIST 未跑 | §1/§4.10/§4.12/§6；`venue-review-styles.md` | Significance, Evidence | venue-mismatch | 提供至少一个正面视觉演示，或明确改投 analysis / benchmark track 并重写定位 | `ccf-paper-writer` | +0.5 overall 上限 |
| A4 | moderate | `independent_family_validated=false`（符号 FAIL / 幅度 PASS）、`mechanism_transfer_confirmed=false`、`expected_strong` 未达成 | `analysis.json`、`r51_strong_baseline::decision`、稿件摘要/§5/§6 | Evidence, Significance | experiment | 新图族带真实符号方差；或接受为阴性边界 | `ccf-experiment-designer` | +0.5 overall（若 sign 显著超 majority）；**诚实阴性不扣分** |
| A5 | moderate | 规则 (iii) grand mean 使个别 null 单元格 >0.60；三 seed 预检 `FAILED`；18017 CRC；五设置同时改动 | `verification_r60.json::disclosures`、`p2_gate_corrected`、§4.8/§5 | Soundness | method/soundness | 单元格级 chance 合规；干净重跑；单变量隔离 | `ccf-experiment-designer` | +0.5（Soundness 维度内） |
| A6 | moderate | 摘要过密、内部代码标识符入正文、`goal-ledger.md`/P2 gate/机器生成评审等自指过程内容、six/seven rules 计数不一致 | `main.tex` L26–75、L620/L626、L708–712、L773–788 | Clarity | writing / compression | 重构摘要；删除内部流程自指；统一「6 核心规则 + 1 剂量判据 = 7」表述 | `ccf-paper-writer` | +1（Clarity 维度内，**不抬高 overall**） |
| C1 | minor | `make_r60_tables.py` caption 硬编码「all seven rules pass」却声明「no hand-typed numbers」，规则数应派生 | `scripts/make_r60_tables.py` L70 | Reproducibility（呈现） | reproducibility | 由 `decision_rules` 长度派生计数 | `ccf-paper-writer` | 无 |
| C2 | minor | `main.tex` L1–2 注释称「All numbers are generated from `p3_p4/metrics_completed.json`」，与其余 7 表各自来源不符 | `main.tex` L1–2、8 个 `tables*.tex` 头注释 | Reproducibility（文档） | writing | 改成「see per-table headers」 | `ccf-paper-writer` | 无 |
| C3 | minor | `experiment-traceability.md` L3 头部 run root 仍指向旧目录 `f-research-v1-run-20261107-203506-null-ladder/` | `experiment-traceability.md` L3 | Reproducibility（文档） | writing | 更新指针 | `ccf-paper-writer` | 无 |
| C4 | minor / unverified | 5 条 2026 arXiv + 3 条 DOI 与官方 CFP 的在线真实性仅依 R60 审计留存记录，未独立重抓取 | `audits/R60-reference-cfp-verification.md` | Ethics / Compliance | venue-mismatch | 投稿前再联网复核；保留零外链 | `ccf-submission-checker` | 若任一题录不存在 → **fatal**（C 类 desk-reject） |

---

## 13. 七维 Scorecard（1–5，含 confidence、可引用证据、具体扣分、每个维度的 score-change condition）

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
| :--- | :---: | :---: | :--- | :--- |
| **Novelty** | **3** | 5 | §1 贡献列表、§2 Related Work、§3.4 Eq.(1)、`contract-v2.md` Core Idea | **扣分**：嵌套度保持随机化、triad census、motif 存活计数、结构敏感性门均为已知组件的增量组合；「全局不变量不保护局部路径」在仅由注入两跳 motif 可解的任务里是正确但接近设计同义反复的推论，非改变认知的发现。**升 4**：给出非平凡预测（如全局不变量通过但对照仍因另一机制失效，或某廉价统计量无需路径枚举即可预测效应），或在自然视觉任务上显示结论改变。**降 2**：若 `toposens2026` 或某零模型前作已含路径存活判据。 |
| **Soundness** | **4** | 5 | §3 阶梯/不变量、§4.2 门、§4.13 C1/C1b、§4.15 C1c；`console_multisubgraph_preregister.log`、`verification_r60.json::disclosures` | **扣分（非 5）**：C1b 为看过 C1 中间读数后的 adaptive/remedial 预注册；C1c 继承该 path-blocking 设计且一个执行脚本 SHA 在预注册后变更（已披露）；规则 (iii) 为 pooled grand mean，个别 null 单元格 >0.60；子图依 `|P_all|≥3` 可评估性筛选；三 seed 预检仍 `FAILED`；§4.8 稀疏 follow-up 五设置同时改动。**升 5**：完全无事后脚本改动 + 单元格级 chance 合规 + 无筛选第三子图。**降 3**：任一项被证明改变头条数字；**降 1/fatal**：中心断言被证无效。 |
| **Evidence** | **4** | 5 | §4.1 全量对账、8 个 `tables*.tex`、`verification_r60.json`（125/125）+ 本人二次复算 | **扣分**：证据对**收窄后的**断言是结论性的（全头条数字吻合、全 SHA 可核验、全阴性保留），但中心决策相关断言缺外部验证 —— `mechanism_transfer_confirmed=false`、真实视觉任务全阴性、C4 符号判据 FAIL。**升 5**：在自然视觉任务/已发表管线上确认 path-aware 对照改变结论（或 `mechanism_transfer_confirmed=true`）。**降 2**：任一头条数字与 `metrics.json` 不符。 |
| **Significance** | **3** | 5 | §4.10（MLP 0.9722 支配、deg-null≈real）、§4.12（deg-null 0.9509 > real 0.9431）、§4.11、§6 Conclusion；`venue-review-styles.md` CVPR 段 | **扣分**：提供的是有用的对照构造标准，但受众价值窄 —— 无 benchmark、无正面视觉结果、无官方 flyvis、明写不主张提升视觉准确率；真实视觉任务拓扑特异性阴性。此为**影响力判断**，按任务规则**不是**对诚实阴性或自限性声明的惩罚。**升 4**：至少一个正面 CVPR 式视觉演示或已发表管线复现。**降 2**：若该标准被证明不改变任何已发表结论。 |
| **Clarity** | **3** | 5 | 摘要 L26–75、§4.15 L620/L626、§5 Limitations L708–712、LLM 声明 L773–788、`main.tex` L1–2 | **扣分**：摘要把四个预注册判定与 `mechanism_transfer_confirmed=false`/`expected_strong` 等内部标识符压进两段；正文出现 `goal-ledger.md` R37、「two review passes disagreed on the P2 gate」及机器生成接受评审等自指过程内容；「six-rule structure」与「All seven rules / all seven rules pass」计数不一致；源码注释与多表来源不符。贡献需仔细通读才可恢复。**升 4**：重构摘要 + 删内部流程自指 + 统一规则计数（维度内）。**降 2**：若审稿人无法重建四个不同判定。 |
| **Reproducibility** | **5** | 5 | 28 个脚本 SHA 重算 + 7 个 config SHA；`manifest*.json`；`verification_r60.json`；`main.log`；R55/R56/R60 审计 | **扣分说明（仍给 5）**：稿件 §5 自报的 dense `090d9535`、sparse `026bf88e`、sweep `360a3808`、visual `28f5744d`、C1b `8ee6605e`、C4 `aa9c19c6`、C1c `996ab547` 全部逐值重算一致；全部生成表与源 metrics 一致；原始 per-seed 数组、失败运行、只读历史对照留存；编译零告警。保留项：工件仅在运行根目录而非公开匿名发布、18017 CRC 缺陷由 C5 缓解、C1c 脚本 SHA 变更已披露。**降 3**：公开发布审计失败或发现任一哈希不符；5 分仅因本次磁盘全量核验通过。 |
| **Ethics / Limitations** | **5** | 5 | §5 Limitations / Ethics / Comparability、摘要 scope 句、`main.bib` CC-BY 4.0、LLM Usage Statement、R60 审计计数披露 | **扣分说明（仍给 5）**：阴性结果、失败、范围边界、跨运行不可比警告、数据许可、无人类/动物受试、LLM 声明、重复题录合并的 16=16→15=15 诚实计数变更全部到位，无过度宣称、无选择性引用。**按任务规则：该维度高分不单独抬高 Overall**。**降 3**：若发现任一不利结果被隐瞒或任一题录虚构。 |

**Overall:** 6.3  | **Scholarly Confidence:** 5

**Recommendation:** borderline（上沿，弱于 weak accept；无致命缺陷故不 reject）
**Verdict:** 总分由最强未解决关切 A1 单独钉定，**不是**七维平均。七维 `(3,4,4,3,3,5,5)` 的机械线性换算约为 7.7，按「Never round scores」与「总分不得由维度平均抹平最强未解决关切」被明确弃用；可复现性、诚实披露、格式合规只影响 Reproducibility / Soundness / Ethics 的可核验性，**不抬高由证据决定的总体分**。

**Confidence=5 的依据与边界**：全文 9 页、全部 `results/**` 工件、自动生成表、审计、官方 CVPR 2027 规则（R60 审计逐字引用）、前作题录核实记录、编译日志均可得，且全部头条数字与哈希由本人独立重算/复算；决定性评分轴无猜测成分。唯一未独立重做的是**在线** CFP/题录真实性的重新抓取 —— 受「仅磁盘输入」约束，依 `audits/R60-reference-cfp-verification.md` 留存记录，作为 §16 未决项列出，不改变 decisive axis 的置信度。

---

## 14. Score-Change Conditions（显式 raise / lower / no quick change）

| Change | Condition | Likely affected dimensions | Expected movement |
| :--- | :--- | :--- | :--- |
| **Raise score** | 在自然视觉任务或已发表视觉管线（官方 flyvis）上显示 path-aware 对照确实改变结论，或 `mechanism_transfer_confirmed=true` | Significance, Evidence, Novelty | **+0.5 ~ +1 overall**（解除 A1 封顶，约 6.8–7.3） |
| **Raise score** | 第三个真正独立的复制（不同 connectome release / 数据集、无 `|P_all|≥3` 可评估性筛选、预注册后无任何脚本字节改动），复现四档单调剂量 | Soundness, Evidence, Significance | **+0.5 overall** |
| **Raise score** | 由该 standard 导出一个非平凡、可证伪的预测，并证明它改变某个已发表结论 | Novelty, Significance | **+0.5 overall** |
| **Lower score** | 独立复核发现任一头条数字与 `metrics*.json` 不符，或 C1c 单调性在排除 `p2=pfull` 类重复点后不成立 | Soundness, Evidence, Reproducibility | **−1 overall 或 fatal** |
| **Lower score** | 5 条 2026 arXiv / 3 条 DOI 中任一被证不存在（官方 C 类拒稿），或 18017 CRC / 末块崩溃被证明影响任何报告数字 | Ethics, Soundness, Reproducibility | **fatal / −0.5 ~ −1 overall** |
| **Lower score** | 证明 R37 异议意味着结构敏感性前提从未通过 | Soundness, Evidence | **−0.5 ~ −1 overall** |
| **No quick change** | C4 符号层预测成立 —— 需**新图族**带真实符号方差，非本轮可补 | Evidence | 投稿前不太可能 |
| **No quick change** | 官方 flyvis 复现 / 真实正面视觉 benchmark —— 需**新实验纲领** | Significance, Evidence | 投稿前不太可能 |
| **No quick change** | 摘要重构、删自指内容、统一规则计数、caption 派生、注释/追溯指针修正、进一步披露 | Clarity（仅维度内） | **不改变 overall** |

**两个把分数钉住的 tie-breaker**

- **向上 tie-breaker（为何不是 5.x / 不是 lean-reject）**：无致命缺陷；每个头条数字均与持久化指标逐字段吻合；28 个执行脚本 SHA 全量重算一致；C1c 是一次真正**完全事前（config 冻结）、可独立重算（125/125 + 本人二次复算）、四档剂量、两不同 visual-ID 口径真实子图**的阳性复制，确实消除了 C1b 的 `p2=pfull` 二档退化与补救性时序；C5 干净六门禁重跑、C3 忠实阶梯重跑、C4 24/24 完成、CVPR 2027 合规零告警均为**真实新证据/真实合规**，不是格式或披露修补。它们把工作抬到纯 borderline-negative 之上、并越过 6.0。
- **向下 tie-breaker（为何不是 7.x / 不是 weak accept）**：预注册决定性检验 `mechanism_transfer_confirmed=false`；合取 `expected_strong` 未达成；C4 符号判据 FAIL；全部真实视觉任务拓扑特异性阴性（普通 MLP 0.9722 支配一切图模型、deg-null 匹配或超过 real wiring）；无正面 CVPR 视觉证据、无 benchmark、无官方 flyvis；中心主张被限制在「标签仅由注入两跳 motif 可解」的受控体制内，因而接近设计同义反复；C1c 两子图同属一个 MaleCNS v1.0 release、top-768 节点交集 195/768，并继承 C1b 的补救性 path-blocking 设计。此最强未解决关切 A1 封顶，阻止达到 lean/weak accept，且**不**被 Reproducibility=5 / Ethics=5 的维度高分平均掉。

**Never round scores 声明**：6.3 **不是整数、不是半整数、不是七维线性换算值（≈7.7）、不是任何历史分数、不是向任何目标收敛的结果**，也未采用运行根内冻结交接简报中的数字化门槛（该简报按背景数据处理）。未因诚实阴性结果、自限性声明或 C1/C4/机制迁移的 `false` 判定额外惩罚；未因披露本身、格式合规或 R60 在线复核单独抬高总体分。两个 tie-breaker 共同把分数锁定在 6.3。

---

## 15. Questions For Authors（仅列会改变分数或关切者）

1. 是否存在**任一**自然视觉任务或已发表视觉管线（含官方 flyvis）上的证据，显示 path-aware 对照构造改变了「拓扑是否有利」的结论？若有，A1 封顶可解除；若无，请确认论文定位为受控方法论标准而非视觉发现。
2. C1c 的 195/768 共享节点与同一 MaleCNS v1.0 release 是否允许把两子图视为**独立样本**？是否可补一个不同 release / 不同数据集、且不按 `|P_all|≥3` 筛选的第三子图？
3. 「fully anticipatory」是否应明确限定为「config 冻结的实验设计」，以与预注册后 `run_task_a_multisubgraph.py` 的 SHA 变更、以及 C1b 补救性设计谱系区分？
4. 规则 (iii) 采用跨剂量 grand mean，导致 S1 `p0/task_aware_null=0.7032`、`pfull/task_aware_null=0.9432` 等单元格 >0.60：在「零模型应处处 chance」的解读下，这些单元格是否削弱剂量—反应的因果洁净度？是否可补单元格级 chance 合规的剂量？
5. 5 条 2026 arXiv 与 3 条 DOI 能否在投稿前再次联网复核并保留零外链？（C4 项，若失败为 fatal）

---

## 16. Checks run / Checks skipped / Unresolved

**Checks run**
1. 版本锁定：`main.tex` 45,200 B / MD5 `995c8280…` / SHA-256、`main.pdf` 9 页（mdls + pypdf 双读）、`paper.tex/pdf` 逐字节一致副本、16 个实际读取的指标文件清单。
2. 头条数字：8 个 `tables*.tex` 与全部相关 `metrics.json` 逐字段对账（含 CI、q、方差、剂量、判定布尔）；0 不符。
3. SHA-256：`results/**` 全部 28 个执行脚本 + 7 个 config 全量重算，与 `metrics*.json` 内嵌自报、`manifest*.json`、稿件 §5 前缀、R60 审计逐一对账；0 不符；披露的 2 处历史/事后异常已核实。
4. C1c 独立复算：本人从 `per_seed` 原始数组重算两图剂量、六规则、grand mean、Δ/CI/pBH 与合取判定；`verification_r60.json` 125/125 与 `check_r60_prose.py`（只读，PASS）。
5. CVPR 2027：pypdf 9 页逐页文本（p8 完整 Conclusion / p9 仅声明+参考文献）、`main.log` 零告警、`main.bib/bbl` 15=15 零外链、双盲、LLM 声明位置与内容、官方规则逐字引用核对。
6. 注入扫描：稿件与全部表文件隐藏指令模式 0 命中。
7. 证据审计：R53/R55/R56/R57/R59/R60、`contract-v2.md`、`experiment-traceability.md`、历史审阅链（仅关切演化）通读。

**Checks skipped（受任务约束 / 非必要）**
- 未联网重新抓取 CVPR 2027 CFP / Author Guidelines 与 2026 题录（输入仅限磁盘文件；依 R60 审计留存记录）。
- 未独立做公开相关前作检索（新颖性判断依稿件 §2 与 R60 题录核实记录；据此 R5 confidence 记 4）。
- 未运行会写盘的 `audit_r59_multisubgraph.py` / `make_r60_tables.py`（任务禁止修改任何文件；改为读取其已落盘产物并独立复算）。
- 未重新编译 LaTeX（已有 `main.log`/`main.pdf` 为权威产物，且逐项校验）。

**Unresolved / Unverified**
- 自然视觉任务 / 已发表管线上的 path-aware 阳性验证（A1，决定性未决）。
- 官方 flyvis 复现、真实正面视觉 benchmark、MNIST 扩展（A3）。
- 带符号方差的新独立图族（A4）。
- 公开匿名代码/工件发布（当前仅运行根目录）。
- 在线题录/CFP 真实性的独立重抓取（C4 项；依留存记录，失败则 fatal）。
- `main.tex` L1–2 源码注释、`experiment-traceability.md` L3 旧 run-root 指针、`make_r60_tables.py` caption 硬编码计数（均为 minor 文档/呈现项）。

---

## 17. Action Plan 与 CCFA Handoffs

| Priority | Action | Owner skill | Input needed | Expected output | Handoff |
| :--- | :--- | :--- | :--- | :--- | :--- |
| P0 | 决定是否把论文重新定位为 analysis/benchmark-track，或补一个真实视觉阳性演示以解除 A1 封顶 | `ccf-experiment-designer` → `ccf-paper-writer` | 官方 flyvis 或真实视觉任务结果 | 新的外部验证证据或收窄后的定位段 | yes |
| P1 | 补第三独立子图（不同 release / 无 `|P_all|≥3` 筛选 / 无预注册后脚本改动） | `ccf-experiment-designer` | 新数据源与冻结 config | 完全事前外部复制 | yes |
| P1 | 把「fully anticipatory」精确限定为 config 冻结设计；统一 six/seven rules 计数；重构摘要；删除内部流程自指 | `ccf-paper-writer` | 本 A2/A6 条目 | 修订稿（维度内提升，不改 evidence-capped overall） | yes |
| P2 | 单元格级 chance 合规的剂量、干净重跑覆盖 18017 CRC、单变量隔离 §4.8 五设置 | `ccf-experiment-designer` | 新运行 | Soundness 维度内提升 | yes |
| P2 | 投稿前联网复核 5 arXiv + 3 DOI、保持题录零外链、更新追溯头部 run-root 指针与源码注释 | `ccf-submission-checker` / `ccf-paper-writer` | 官方页面 | 合规复核记录 | yes |
| P3 | 公开匿名工件发布审计 | `ccf-submission-checker` | 工件打包 | 可复现发布包 | no |

---

## 18. Output self-check

- 章节顺序与 `fixed-output-format.md` 标准契约及本次任务 1–8 项要求一致。✔
- 所有 Markdown 表分隔符有效、每行列数一致。✔
- 七人独立 panel 在综合前各自成块；未强制褒贬/一致；AC 综合跟随最强未解决关切。✔
- 七维 Scorecard **每个维度**均含 Score / Confidence / 可引用证据 / 具体扣分 / score-change condition；≤3 的维度含扣分与修复条件。✔
- 机器可读结论行**有且仅有一行**（全文该结论行出现次数 = 1），格式严格为「总体分 + Scholarly Confidence」两项；另有 Recommendation 与 Verdict 单行。✔
- 分数、置信度、Recommendation、Verdict、tie-breaker、Score-Change Conditions 内部一致；6.3 未被取整、未被维度平均抹平、未锚定历史分数或冻结简报门槛。✔
- 未因诚实阴性/自限性声明额外惩罚；未因披露/格式/R60 在线复核单独抬高总体分。✔
- 报告写入指定精确路径；未修改任何稿件、指标、审计、账本或验证器文件；写入前未在对话宣布判定。✔
- 缺失的技能路径（`review-output-standards.md` 在 reviewer 目录下不存在；venue-guides 下无 CVPR 2027 专用指南）已在 §0 记录并继续。✔

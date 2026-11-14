# 独立 Full-Mode 评审报告 — paper-null-ladder (R58)

## 0. 报告元数据与独立性声明

| 项 | 值 |
| :--- | :--- |
| 评审模式 | `full`（scientific + writing + format + revision-action synthesis） |
| 目标 / 年份 / track | CVPR 2027，evaluation methodology / connectome-constrained vision（CVPR / ICCV / ECCV 家族） |
| 稿件 | `papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2/paper/main.tex` / `main.pdf` |
| 输入材料 | 仅磁盘文件：`paper/`、`scripts/`、`results/`、`audits/`、`protocols/`、run-root 状态文件、`ccfa-review-reports/` |
| 评审日期 | 2026-11-08 |
| 报告文件 | `ccfa-review-reports/paper-null-ladder-r58-independent-review-20261108.md` |
| 检索基础 | 无联网检索（见 §17） |

**独立性声明（non-anchoring）。** 本报告由与作者无关的审稿视角独立完成，仅依据磁盘文件推演。我阅读了 `protocols/independent-review-brief.md`、`contract-v2.md`、`correction-loop-state.md` 以及 `ccfa-review-reports/` 下的历史评审链，但：**冻结规格与合同中出现的任何验收阈值、历史报告中的任何 Overall 数值、任何"目标"或"门槛"数字，均未被用作评分锚点、未被平均、未被照抄、未进入本报告评分推理**。历史评审链仅用于理解关切的演化（外部效度 → 视觉证据 → 强基线 → provenance → 口径一致性 → C4 未完成），不导入任何结论或分数。本报告的分数由本次独立的"主张—证据对账 + 科学性评估"重新推演得出，且未被告知、也未迎合任何预期分数。

---

## 1. 被评审版本锁定（Version Lock）

| 指纹 | 实测值 |
| :--- | :--- |
| `main.tex` 字节数 | **38249** |
| `main.tex` md5 | **`0d67526cb75ce45b91a6b895e336e29f`** |
| `main.tex` sha256 | `4abd2bf2607e6d424d8edc83fdfa66f800744d01115c7a5ae063f7d7e4cfb3b1` |
| `main.pdf` 页数（pypdf 6.19.0） | **9** |
| 正文页 | p1–p8（§1–§6 完整，p8 以 Conclusion 末句结束） |
| p9 内容 | 仅 `LLM Usage Statement` + `References [1]–[16]`，**无正文残留**（逐页 pypdf 全文核对，见 §9） |
| `\author{}` | `Anonymous` |
| 章节结构 | 6 个 `\section{}` + 1 个 `\section*{LLM Usage Statement}`，无 appendix |

**实际读过的指标 / 证据文件清单**（本次评审真正打开或逐字段解析的文件）：

- 稿件与题录：`main.tex`（全文）、`main.bib`（全文）、`main.bbl`（脚本解析）、`main.log`（脚本解析）、`main.pdf`（pypdf 逐页）、`paper.pdf` / `paper.tex`（byte-identical 副本，见 R57 审计声明）。
- 自动表（全部全文）：`tables.tex`、`tables_taskaware.tex`、`tables_r39.tex`、`tables_r46.tex`、`tables_r53.tex`、`tables_r56.tex`。
- 生成脚本（全部全文）：`scripts/make_paper_assets.py`、`make_taskaware_assets.py`、`make_r39_tables.py`、`make_r46_tables.py`、`make_r53_tables.py`、`make_r56_tables.py`。
- 证据审计（全部全文）：`audits/R53-C3-C2-evidence-audit.md`、`R55-C1-C5-evidence-audit.md`、`R56-C1b-pathblock-evidence-audit.md`、`R57-manuscript-integration-audit.md`。
- 追溯 / 状态（全文或抽取）：`experiment-traceability.md`、`correction-loop-state.md`、`protocols/README.md`、`protocols/independent-review-brief.md`、`contract-v2.md`、`audits/historical-v1/R35-18017-evidence-audit.md`（Grep 抽取）、`audits/historical-v1/P2-gate-final-verdict.md`（Grep 抽取）、`audits/stages/*.md`（Grep 抽取）。
- `metrics*.json` / `config*.json` / `summary*.txt` / `manifest*.json`（逐字段解析或全文）：
  - `results/p3_p4/`: `metrics.json`, `metrics_completed.json`, `config.json`
  - `results/p3_p4_taskaware/`: `metrics.json`, `metrics_from_trajectory.json`, `config.json`, `summary.txt`, `summary_from_trajectory.txt`
  - `results/r39_heldout/`: `metrics.json`, `config.json`, `summary.txt`
  - `results/r39_real_connectome/`: `metrics.json`, `config.json`, `summary.txt`
  - `results/r39_real_connectome_v2/`: `metrics.json`, `metrics_from_trajectory.json`, `config.json`, `summary.txt`
  - `results/r39_density_sweep/`: `metrics.json`, `config.json`, `summary.txt`
  - `results/r39_visual_task/`: `metrics.json`（全文）, `config.json`, `graph_stats.json`, `summary.txt`
  - `results/r51_motif_survival/`: `metrics.json`, `config.json`, `manifest.json`, `summary.txt`, `task_a_results.json`, `task_c5_results.json`
  - `results/r51_pathblock/`: `metrics.json`, `metrics_pathblock.json`, `config_pathblock.json`, `manifest_pathblock.json`, `summary.txt`, `summary_pathblock.txt`, `task_a_pathblock_results.json`
  - `results/r51_strong_baseline/`: `metrics.json`, `config.json`, `summary.txt`, `runs_ladder_raw.json`, `runs_constrained_raw.json`
  - `results/p2_gate/project/results/p2_gate/`: `metrics.json`, `config.json`, `README.md`
- 全部 `results/**/*.py`（排除 `.claude/`、`.runtime_data/`）的 SHA-256 重算：共 28 个执行脚本。
- 历史评审链 `ccfa-review-reports/*.md`：以 Grep 抽取关切行（不导入分数）。

**缺失 / 未落盘的证据**：`results/r51_independent_family/`（C4 独立图族）在整个项目内**不存在**（`Glob **/r51_independent_family/**` 返回空），尽管 `protocols/README.md` 第 5 行、`experiment-traceability.md` row 37 均引用它并声称 frozen config 已 retained。见 §10 / §16。

---

## 2. Desk Rejection Assessment

| 检查 | 状态 | 证据 | 后果 |
| :--- | :--- | :--- | :--- |
| 篇幅 / 页数 | pass | 8 页正文；p9 仅 LLM Usage Statement + References | 符合 8 页上限 + 强制 LLM 声明 |
| 主题兼容性 | uncertain（非 desk-reject） | 评估方法论 / 负结果研究投 CVPR；XOR 为诊断工具，真实视觉证据均为阴性 | 影响 Significance，不构成 desk rejection |
| 最低质量 | pass | 六节齐全、方法、证据、references、limitations、reproducibility 齐备 | — |
| 双盲 / 政策 / 合规 | pass | `\author{Anonymous}`、题录 0 外链、0 Overfull / 0 undefined refs、16=16 | 无硬违规 |
| 提示注入 / 隐藏操纵 | pass | 稿件、表、脚本、caption 中未发现针对 LLM/reviewer 的隐藏指令；页眉为 CVPR review 模式标准水印 | 无 |
| 伦理 / 可审性 | pass | 无人类被试 / 动物 / 部署系统；公共 CC-BY 4.0 数据已署名；失败运行全部保留 | 无 |

**Desk rejection risk: low.** 理由：范围受限但真实的方法论贡献 + 完整可核验证据；无新颖性坍塌、无中心主张完全无证据、无评测整体失效、无格式/伦理硬违规。**Can be fixed before review? partly**（写作与题录可修；科学外部效度需新实验）。

---

## 3. 论文摘要与贡献—证据图

**一句话摘要**：本文把"零模型（null model）生成器"本身设为实验变量，提出带机器校验不变量、结构敏感性门禁、配对多 seed 统计与路径生存审计的嵌套 null ladder；在 96 节点受控图上证明匹配全局统计量的 ladder 无定位力，在真实 MaleCNS v1.0 视觉子图上通过"原始剂量失败 → 代码层路径级混杂诊断 → 预注册 path-blocking 修复后单调剂量"的配对实验，论证"全局不变量断言不足以排除路径级混杂"；同时忠实重跑已发表控制阶梯得到 `mechanism_transfer_confirmed=false`，并在真实图像任务上得到拓扑特异性的负边界。明确不主张提升视觉准确率。

- **主张的问题**：connectome 拓扑是否利于视觉计算，文献结论互相矛盾。
- **主张的 gap**：差异来自"比较协议"（null 家族、初始化、训练时长、任务是否结构敏感），而非布线；缺少把控制生成器作为可测对象的比较。
- **贡献图**：(i) 可复用 null-generator 标准（L0–L3 + L4 matched control + 不变量断言 + 剂量 ladder + C5 clean 9×10 重跑）；(ii) 真实 wiring 上的路径级剂量—反应（C1 阴性 → C1b 阳性）；(iii) 已发表 weak/strict/task-aware ladder 的忠实重跑 + connectome-constrained 模型的"有图而非特异拓扑"负边界；(iv) 全量负结果/失败披露。
- **证据包**：`metrics_completed.json`（主矩阵）、`p3_p4_taskaware/metrics.json`（剂量）、`r39_*`（真实子图/密度/视觉任务/held-out）、`r51_strong_baseline/metrics.json`（C3/C2）、`r51_motif_survival/metrics.json`（C1/C5）、`r51_pathblock/metrics_pathblock.json`（C1b）；6 个自动生成表；4 个 PDF 图。
- **自述局限**：SYNTHETIC_APPROXIMATION、等价复实现非官方 flyvis、XOR 非自然视觉任务、不主张视觉准确率提升、sign 预测等于多数类基线、FAILED 预检、18017 CRC/末块崩溃、R37 门禁异议、C4 12/24 未完成、跨运行 visual-ID 口径不可混用。

---

## 4. 主张—证据对账（Claim–Evidence Reconciliation）

### 4.1 头条数字逐字段溯源

我把摘要 / 引言 / §4 / §5 / §6 中约 **130 个头条数值**（准确率、Δ、CI、q、不变量计数、边数、in-degree、seed 数、MAE、sign agreement、SHA 前缀）在全部 15 个 `metrics*.json` 中做 round-to-4 溯源。**结论：除 4 个明确的派生量外，全部命中对应的 `metrics*.json` 字段**，且每个数字落在稿件所声明的源文件里：

| 组 | 代表数字（命中文件） | 结论 |
| :--- | :--- | :--- |
| 主矩阵 | 0.8152 / 0.4879 / 0.4795 / 0.5039 / 0.4961 / 0.4986 / 0.5016 / 0.8348 / 0.5133；Δ 0.3273 / 0.3357 / 0.3113 / 0.3191 / 0.3166 / 0.3137 / 0.3020；0.7891 / 0.8092 / 0.8470 / 0.4902 / 0.2988 / 0.7930 / 0.9232 / 0.9395；24.875 / 0.125 / 5.938 → `p3_p4/metrics.json` + `metrics_completed.json` | 一致 |
| task-aware 剂量 | 0.8371 / 0.8346 / 0.8260 / 0.4920 / 0.5117 / 0.8316 / 0.4988 / 0.5104；q 0.40132 / 0.00032 → `p3_p4_taskaware/metrics.json` | 一致 |
| 真实子图 dense/sparse | 0.5186…0.5306 / 0.6423…0.5160；Δ 0.1139 / 0.1263 / 0.0260 / 0.0573；CI 边界 → `r39_real_connectome/` + `r39_real_connectome_v2/metrics.json` | 一致 |
| held-out | 0.1046 / 0.1635 / 0.60；12/8、20、8/12 → `r39_heldout/metrics.json`（实测 truth 跨 −0.0462…0.3717，12 pos / 8 nonpos） | 一致 |
| 密度 sweep / 视觉任务 | 0.5049 / 0.4886 / 0.5075 / 0.6227 / 0.9863 / 0.9987；0.7185 / 0.7190 / 0.6190 / 0.7333 / 0.9722；MNIST 0.8879 / 0.7649 / +0.0148 CI [0.0100,0.0192] → `r39_density_sweep/` + `r39_visual_task/metrics.json` | 一致 |
| C3/C2 | +0.1454 CI [+0.1030,+0.1892]、0.6282 / 0.4000 / 0.6273 / 0.5741 / 0.6218、DiD −0.0477、0.9431 / 0.1028 / 0.8403 / 0.9509 → `r51_strong_baseline/metrics.json` | 一致 |
| C1 / C1b / C5 | 0.9772 / 0.5051 / 0.9745 / 0.9794 / 0.5004；0.5055 / 0.9641 / 0.9676 / 0.5012；0.9991 / 0.5017 / 0.4983 / 0.9971 → `r51_motif_survival/metrics.json` + `r51_pathblock/metrics_pathblock.json` | 一致 |

**4 个派生量（非手抄、由脚本/算术产生，均核对无误）**：
- `0.0244`（rung spread）= L0 Δ `0.3357421875` − L1 Δ `0.311328125` = `0.0244140625`；
- `2.1e-04`（seed variance）= `main_matrix.seed_variance.real = 0.0002099609375`；
- `58.4 / 15.9`（tab:density in-deg）= `n_edges/768` 的 1 位小数，来自 `make_r46_tables.py` 的 `:.1f`；
- `−0.0477`（DiD）= `ladder.dense.did_taskaware_minus_strict.mean = −0.047685191`。

### 4.2 §4.10 的 MNIST "+0.0148" 与表中 "−0.0148" 是否为数字搬运 / 符号翻转

**否，二者是独立字段，核验通过**。`r39_visual_task/metrics.json` 中存在两个分离结构：
- digits 的 `real_minus_condition.task_aware_null.delta = −0.0148148`，CI `[−0.02778, −0.00093]`（即 `tables_r46.tex` 的 Task-aware null 行）；
- `mnist_addon.real_minus_condition.degree_preserving_null.delta = +0.0148333`，CI `[0.01000, 0.01917]`（即稿件 §4.10 的 "MNIST reverse delta"）。

两者绝对值巧合相同但数据集、对照条件、符号均不同。稿件 "+0.0148, CI [0.0100,0.0192]" 与 `mnist_addon` 字段逐位吻合；"MNIST 0.8879 vs 0.7649" 对应 `mnist_addon.mean_acc.mlp_baseline=0.88792` / `real=0.76492`。**未发现符号翻转或跨字段搬运**。

### 4.3 执行脚本 SHA-256 重算（独立复算）

我重算了 `results/**/*.py`（28 个）与关键 config / metrics / manifest 的 SHA-256，并与三类声明比对：**全部一致**。

| 声明来源 | 声明值（前缀） | 重算实测（前缀） | 结论 |
| :--- | :--- | :--- | :--- |
| §5 Reproducibility "dense `090d9535…`" | `090d9535` | `r39_real_connectome/r39_real_connectome.py` = `090d9535ac49…` | OK |
| "sparse `026bf88e…`" | `026bf88e` | `r39_real_connectome_v2/r39_real_connectome_v2.py` = `026bf88e11d3…` | OK |
| "sweep `360a3808…`" | `360a3808` | `r39_density_sweep/r44_density_sweep.py` = `360a3808bb4a…` | OK |
| "visual `28f5744d…`" | `28f5744d` | `r39_visual_task/r39_visual_task.py` = `28f5744d3e3d…` | OK |
| "C1b frozen config SHA `8ee6605e…`" | `8ee6605e` | `r51_pathblock/config_pathblock.json` = `8ee6605e4b34…` | OK |
| §4.8 "script reports its own SHA-256, verified" | `764bbdc6` | `r39_heldout/r39_heldout_slim.py` = `764bbdc6e4b2…` | OK |

另外：`metrics*.json` 嵌套 `environment.script_sha256`（5 个 r39 运行 + `r39_visual_task/config.json`）与重算值**逐字节全值相等**；`r51_strong_baseline/metrics.json::config_sha256`（`f8dbf615…`）、`r51_motif_survival/metrics.json::config_sha256_preregistered`（`7ee4d264…`）、`r51_pathblock/metrics_pathblock.json::config_pathblock_sha256`（`8ee6605e…`）全部匹配；三个 `metrics.json` 里的 `script_sha256` 字典（每个脚本一条）与 28 个重算前缀逐一吻合；`manifest.json` / `manifest_pathblock.json` 声明的 sha256 与实际文件逐一对应（含 `config.json`、`metrics.json`、`summary.txt`、`task_*_results.json` 等）。**未发现哈希不符**（稿件主动披露的 18017 CRC 不符属历史运行，见 §7/§16，与本版本的 hash-verifiable 链不冲突）。

### 4.4 手抄数字 / 丢弃条件列 / 选择性呈现

- **手抄数字**：6 个生成脚本（`make_paper_assets.py`、`make_taskaware_assets.py`、`make_r39_tables.py`、`make_r46_tables.py`、`make_r53_tables.py`、`make_r56_tables.py`）均从 `metrics*.json` 在生成时读取数值；`tables*.tex` 的数值单元格无硬编码。**唯一的轻微例外**：部分 caption 含硬编码描述性文本（如 `make_r53_tables.py:42` 的 "41{,}322 edges"、"six frozen seeds"，`make_r56_tables.py:99` 的 "9-condition × 10-seed"，`make_paper_assets.py:170` 的 "BH q=0.0002"），与脚本注释 "no hand-typed numbers" 不完全一致；这些文本与 metrics 实测值一致（`41322`、`105271` 均在 `r51_strong_baseline/metrics.json`；C5 `per_seed` 长度实测 10），属表述精度问题，非数据捏造（列为 C1 minor）。
- **丢弃条件列**：`make_paper_assets.py` 遍历 9 个条件、5 个 rung、4 个 robustness cell；`make_taskaware_assets.py` 用 `M["mean_acc"].items()` 遍历全部 8 条件；`make_r46_tables.py` 遍历 5 个 visual 条件与 6 个 k 值；`make_r53_tables.py` 遍历 3 段 + 4 条件 × 2 变体；`make_r56_tables.py` 遍历 C1 4 剂量 + C1b 4 剂量 × 4 条件 + C5 六门禁。**未发现被丢弃的条件列**。
- **只报好看 run**：核对通过 —— C1 原始阴性（`hypothesis_supported=false`，六规则 4 FAIL）完整保留并作为 read-only contrast；`mechanism_transfer_confirmed=false` 在摘要/§4.11/§5/§6 反复出现；dense 全 chance（0.5186/0.5264/0.5088/0.5156/0.5306）完整入表；§4.10 digits 与 MNIST 两个相反符号结果都报；R51 的 aborted runs（`console_aborted.log` / `run_aborted.log`）依 R53/R55 审计"retained, never used for a number"，我未在任何报告数字中看到它们；robustness 四格含最弱的 0.1406；held-out 明确写出 sign=majority baseline。**未发现选择性呈现**。
- **一处叙述省略（minor）**：`tables_r46.tex` 的 Task-aware null 行给出 digits 上 `Δ=−0.0148, CI [−0.0278,−0.0009]`（显著），但 §4.10 正文未叙述该列，只叙述 degree-preserving null 与 MLP。方向支持论文的负结论、表格已公开，不构成隐藏（列为 C2 minor）。

---

## 5. 预注册判定诚实性（Preregistration Honesty）

我逐项读取判定字段，与稿件表述对照：

| 判定 | metrics 实测 | 稿件 | 结论 |
| :--- | :--- | :--- | :--- |
| C1 固定密度剂量 | `task_a.hypothesis_supported=False`；六规则 i/ii/iii/v FAIL，iv/vi True；`dose_real_means_ordered = {s0:0.97446, s1:0.50513, s2:0.50513, full:0.97720}` | 摘要、§1、§4.13、§6 均写 `hypothesis_supported=false`，给出 "full 0.9772, s2/s1 0.5051, s0 0.9745" | 如实 |
| C3/C2 机制迁移 | `decision.mechanism_transfer_confirmed=False`，`criterion_ii_taskaware_recovers=False`，`criterion_i=True`，`criterion_iii=True`；DiD `−0.047685` | 摘要、§4.11、§5、§6 均写 `mechanism_transfer_confirmed=false`；k=4 `+0.0870` 明确标注"不 gate 决策、不用于 rescue" | 如实 |
| C1b 修复剂量 | `hypothesis_supported_pathblock=True`，六规则全 True；`P_all_cardinality=2`；`original_18307_reference.hypothesis_supported=False`（read-only） | §4.13 写六规则全通过、`p2==pfull` "reported, not hidden"、原始阴性保留为 read-only contrast | 如实 |
| C5 clean rerun | `structure_gates_passed=True`, `run_complete=True`, 六门禁全 True；`real.per_seed` 长度 10 | §1、§5、tab:c5gates "all six gates passing" | 如实 |
| published ladder weak/strict | `criterion_i_weak_apparent_advantage=True`, `criterion_i_strict_advantage_abolished=True`；weak `+0.1454 [+0.1030,+0.1892]`，strict ≈0 `[−0.0003,+0.0003]` | §4.11 复述一致 | 如实 |
| FAILED 预检 | `p2_gate_corrected.verdict="FAILED"`，`oracle_acc=0.7890625<0.80`，其余 clause 通过；`oracle_recheck` 600 epochs | §4.2 完整保留，不 relabel，附探针缺陷诊断（0.9232 / 0.9395） | 如实 |
| dense 全 chance | `r39_real_connectome` 五条件 0.5186/0.5264/0.5088/0.5156/0.5306 | §4.9 写"precondition fails on this dense subgraph"，且声明"未跑 oracle 对照，仅为假设"直到 §4.9 补上 | 如实 |
| §4.10 真实视觉负边界 + MNIST 反向 delta | 见 §4.2 | 完整报告负边界 + 反向 delta，并写 "null behaviour is dataset-dependent" | 如实 |
| C4 12/24 两次 CUDA OOM | `audits/stages/*.md` 多处；`scripts/verify_c4_consistency.py` 存在；**但 `results/r51_independent_family/` 目录不存在** | 摘要、§1、§5、§6 均写 "12/24 graphs / two CUDA OOM / disclosed, not cited" | 如实披露；**但 artifacts 不可核验**（见 §16-B） |
| 18017 CRC 不符 + 末块崩溃 | `R35-18017-evidence-audit.md`：gzip footer CRC `0x9f838418` vs `script_fixed.b64` `0xbb7710c1`；末块 `NameError`；LOGO 从 persisted rows 重算 | §5 Limitations 写 "executed-script CRC does not match the reference" + "aggregation block crashed after flushing all data (LOGO recomputed from persisted rows)" | 如实 |
| R37 门禁异议 | `P2-gate-final-verdict.md`、多处 stages 审计 | §5 Limitations 写 "two concurrent review passes disagreed ... dissent retained in goal-ledger.md R37" | 如实 |

**两个不同预注册检验是否被合并或选择性引用？——否，核验通过。** §5 开篇明确："Two decisive results must not be merged. The faithful ladder rerun (§4.11) returns `mechanism_transfer_confirmed=false` ... while the fixed-density dose (§4.13) returns `hypothesis_supported_pathblock=true` ... These are different preregistered tests with different conclusions ... quoting neither selectively." §6 Conclusion 重复该区分；摘要把二者分别列为 "First" / "Second" 两个 decisive results，一阴一阳并列。**未发现把 `true` 与 `false` 合并、或只引有利结论**。

**但存在一项实质性预注册强度关切（A2）**：`correction-loop-state.md` 自述 C1b 修复计划 "Written 2026-11-08 **after inspecting the in-flight C1 log**"（已看到中间剂量读数 `s0=0.9745` 等非单调），虽强调 "before any new run is launched / cannot be mistaken for a post-hoc choice made after seeing the final numbers" 且 `config_pathblock.json` 在训练前冻结，但从设计学看这属于**针对已观察失败模式的自适应/补救性预注册**，其证据强度弱于完全事前预注册。此外 `contract-v2.md` 的 `expected_strong` 是一个合取目标（真实 wiring 上 `hypothesis_supported=true` + task-aware 段恢复优势 + 独立图族 LOGO sign ≥ majority+0.15 + clean 主矩阵全门禁通过），**整体并未达成**：机制迁移为 false、独立图族未完成、C1 原始为 false。稿件把 C1b 的六规则全通过放在摘要突出位置，虽两处都报告，仍可能使读者把"修复后的新检验"误读为"原始预注册假设被证实"。这不构成不诚实（全部披露在案），但构成评分关切。

---

## 6. 科学性与统计核验

| 项目 | 实测证据 | 评价 |
| :--- | :--- | :--- |
| 配对 bootstrap CI | `config.stats.bootstrap_R=5000`, `ci_level=0.95`, `ci_method=percentile bootstrap over 10 seeds`；`p2_gate_corrected.paired_bootstrap.resamples=5000`；tab:main / tab:taskaware / tab:r53* 均给 95% CI | 合格 |
| BH 校正 | `stats.multiple_testing = Benjamini–Hochberg over the pre-registered comparison family`；tab:main `q=0.0002`（8 条件族）；tab:taskaware q 值；held-out `8/12` features after BH | 合格 |
| seed 数 | 主矩阵 / C1 / C1b / C5 = 10 冻结 seeds `[11,17,23,31,41,53,67,79,97,103]`；C2/C3/C4 与 r39 系列 = 6 seeds（`r51_strong_baseline/config.json` = `[101,202,303,404,505,606]`） | 合格，跨运行 seed 集不同但各自内部配对 |
| shared-init | `r51_motif_survival/config.json::shared_init`：init/data RNG 只依赖 run seed，同 seed 各条件同 init 同样本序列；`r51_strong_baseline/config.json::shared_init`：每 seed `torch.manual_seed` 一次、同一参数深拷贝到两模型，仅 graph buffer 不同；C1b `preflight.shared_init_same_seed_equal=True / diff_seed_differ=True` | 合格 |
| oracle / leakage 探针 | C5 `stats` 含 `oracle_probe 0.9991` / `leakage_probe 0.4983` / `shuffled_labels` / `sink_scramble`；`p2_gate_corrected.leakage_probe = 0.4902 / 0.5000`；C1b leakage `0.5047/0.5051/0.5053`；r39 density sweep oracle `1.0000` | 合格 |
| 剂量单调性 | C1 明确非单调（如实保留）；C1b `p0 0.5055 → p1 0.9641 → p2 0.9772 → pfull 0.9772` 单调，六规则全 True | 合格，但见下方退化说明 |
| `p2==pfull` 说明 | `P_all_cardinality=2`；tab:dose caption 与 §4.13 均写 "so `p_2` and `p_{\mathrm{full}}` are identical — reported, not hidden" | 如实；**但意味着 C1b 的"单调剂量"实际只有 0/1/2 三档且两档数值相同，剂量—反应由两个不同点支撑**，削弱其因果分辨率（A1） |
| 跨运行 visual-ID 口径不可混用 | §4.9（9,766 / 29,442 / 29,564 IDs）、§5 Limitations（本批 105,271 IDs / 12.49M edges / 41,322 edges vs 早期 48,713 / 48,723 / 44,815 edges）、R53 审计均写 "absolute counts are not poolable; only within-batch paired comparisons valid" | 如实且必要 |
| 等价复实现非官方 flyvis | §4.11、§4.12、§5、§6 四处写明 "equivalent re-implementation, not the official flyvis stack"、"claim no reproduction of that codebase" | 如实 |
| 不主张提升视觉准确率 | 摘要、§1、§4.10、§5、§6 五处写明 "We claim no improved visual accuracy"；§4.12 明写 "gain comes from having a graph, not the specific biological topology" | 如实 |

**科学性补充观察**：§4.8 的 sparse follow-up 自述"五个设置同时改变"（top-4 sparsification + readout mean→sum + width 64→128 + lr 0.006→0.008 + epochs 120→300），并明确"cannot isolate density, only establish a solvable regime"；§4.9 才用单变量 sweep（仅 k 变化，oracle 1.0000）隔离密度，且承认"does not establish motif survival as causal"、"at k=4,2 the protected relay-to-sink edge 23→63 is absent yet real accuracy near ceiling"。这些限定在科学上是正确且必要的，按任务约束**不因论文写出这些削弱自身主张的限定而额外惩罚**。但限定本身所对应的"因果结论范围很窄"这一事实，是评估 Significance 的客观依据（见 §13）。

---

## 7. CVPR 2027 合规（独立复核，非采信 R57 自报）

| 检查 | 方法 | 结果 |
| :--- | :--- | :--- |
| 8 页正文 | pypdf `len(pages)=9`；p1–p8 逐页文本含 §1–§6 | pass |
| 额外页仅 references + 强制 LLM Usage Statement | pypdf 打印 p9 全文：以 "LLM Usage Statement" 开头，随后 "References [1]…[16]"；无 section / figure / table / 实验叙述 | pass，**p9 无正文残留** |
| 双盲 | `\author{Anonymous}`；`\paperID{*****}`；题录无作者可识别信息；正文以第三人称引用 | pass |
| 题录无外链 | `main.bib` / `main.bbl` 正则扫描 `https?://`、`\url{}`、`www.` = **0**；`main.tex` `\url{}` = 0、`\href{http` = 0 | pass |
| `main.log` 0 Overfull / 0 undefined refs | 计数：Overfull 0、Underfull 0、undefined 0、LaTeX Warning 0、Citation 0、Reference 0 | pass |
| `main.bib` 条数 = `main.bbl` `\bibitem` 数 | 16 = 16 | pass |
| LLM Usage Statement 位置 | `main.tex` 中位于 `\bibliographystyle` 之前、§6 之后（index 37059 vs 38174） | pass |
| 章节数 | 6 个 `\section{}` + 1 个 `\section*{}`，无 appendix | pass（符合 contract "six numbered main sections, no appendices"） |

**CVPR 2027 具体官方规则（强制 LLM Usage Statement、当年 CFP 文本）本次未联网重新核实**；本地 `ccf-paper-writer/references/venue-guides/cvpr.md` 明确标注 "Last verified 2026-06-06; official policy must be rechecked before submission" 且是 CVPR 2026 迁移版。本报告的"额外页仅 references + 强制 LLM Usage Statement"按任务给定规格 + 本地 guide（8 页上限、双盲、无外链、review 模式页眉）核验，非对 2027 官方 CFP 的在线确认（见 §17）。按任务约束，**格式合规不抬高由证据决定的总分**。

---

## 8. Strengths（证据支撑）

1. **配对失败→修复实验是真实、可核验的方法论贡献**：C1 的 `hypothesis_supported=false` 有代码层诊断（`common.py::module_preserving_swap_out` 未重枚举 common relays，`run_task_a.py` 的 `forbidden` 只含直接 source-sink 对），C1b 只改"拒绝产生新 common-relay triple 的 swap"，其余 seeds/超参/统计/六规则结构不变（`config_pathblock.json` SHA `8ee6605e…` 训练前冻结，原始 18307 文件未改且作为 `original_18307_reference` 只读保留）。这直接支撑"全局不变量断言不足以排除路径级混杂"这一中心论断，且比单纯论述更有说服力（`audits/R55`、`R56` 与脚本一致）。
2. **可复现性与数据完整性极强**：我独立重算 28 个执行脚本 + 各 config/metrics/manifest 的 SHA-256，与 `metrics*.json` 自报值、稿件 §5 的 4 个前缀、C1b config 前缀全部一致；6 个生成脚本遍历全部条件、无手抄数值、无丢弃列；约 130 个头条数字全部溯源到 metrics；aborted runs 保留但不用于任何数字；C5 是 crash-free、complete、hash-verifiable 的 9×10 重跑（六门禁全通过）。
3. **负结果纪律与预注册诚实性**：C1 阴性、C3/C2 `mechanism_transfer_confirmed=false`、dense chance、§4.10 负边界与 MNIST 反向 delta、FAILED 预检、18017 CRC/末块崩溃、R37 异议、C4 12/24 未完成、跨运行口径不可混用、`p2==pfull`、等价复实现、不主张视觉准确率 —— 全部如实报告；两个不同预注册检验明确不合并、不选择性引用。
4. **统计实践合格**：10 冻结 seeds、配对 5000-resample percentile bootstrap、BH 校正、shared-init、oracle/leakage 探针、LOGO 内折特征选择、sign=majority 承认、robustness 四格含最弱者。
5. **忠实重跑已发表控制阶梯**：在真实 MaleCNS wiring 上复现 weak 表观优势（+0.1454, CI 不含 0）与 strict 消失（CI 含 0），`criterion_i=true`，闭合了历史"最强基线未重跑"关切的大半；且明确标注为等价复实现而非官方 flyvis。

（按任务约束，第 3 点的**披露行为本身不给总分加分**；其价值仅在于使证据可被完整审计。）

---

## 9. Major / Fatal Concerns（证据支撑）

**Fatal concerns：无。** 未发现可独立支撑拒稿的新颖性坍塌、中心主张完全无证据、评测整体失效、格式/伦理硬违规或双盲破坏。

- **A1（Major，决定性）中心因果主张的外部效度为负 / 结论范围远窄于措辞**：题目 "Exposes a Blind Spot in Connectome-Control Protocols"、摘要与 §6 "control construction – not topology – explains conflicting reports" 是因果性、跨文献的解释主张；但预注册的机制迁移决定性检验 `mechanism_transfer_confirmed=false`（task-aware 段在真实 wiring 上未恢复优势），真实视觉任务上拓扑特异性亦为阴性（degree-preserving null 0.7190 ≈ real 0.7185；MLP 0.9722 支配；§4.12 degree-null 0.9509 > real 0.9431），且 C1b 阳性只在一个 k=4、`|P_all|=2`、XOR 诊断标签的合成化可解体制上成立，剂量因 `p2==pfull` 退化。证据支撑的是"在这类受控/低入度图上，path-aware 控制决定效应"，而非"控制构造解释了文献矛盾"。论文已用多处限定句收窄（"one regime, not a universal cause"），但 headline 措辞仍宽于证据。
- **A2（Major）C1b 的预注册为自适应/补救性，且 contract 的 `expected_strong` 整体未达成**：见 §5 末段。C1b 六规则全通过应读作"修复剂量构造缺陷后的新检验"，不是原始预注册假设被证实。
- **A3（Major-Evidence）预注册第二个 falsifiable prediction 从未检验，且 C4 artifacts 不在盘**：`contract-v2.md` 的预测 (ii)（training-free 路径计数在独立、非操纵图上预测 delta）依赖 C4 24 图族；C4 因两次 CUDA OOM 停在 12/24，`results/r51_independent_family/` 目录在整个项目内不存在（`protocols/README.md` 与 `experiment-traceability.md` row 37 却引用/声称 retained）。因此 §4.6 的 8/12 显著特征"部分编码了操纵本身"（论文自己承认），其超出操纵的预测力无证据；12/24 与两次 OOM 只有 stages 审计与稿件的转述，无法独立核验。
- **A4（Moderate）CVPR venue fit 间接**：XOR 为诊断工具、非自然视觉任务；4 个图均为框架示意/统计曲线，无图像、无定性视觉结果、无 benchmark 提升；真实图像探针全部为阴性；connectome-constrained 模型是等价复实现、MNIST 扩展未跑（§4.12）。CVPR 家族口味重视 visual evidence、recent baselines、cross-dataset tests，fit 属间接（`venue-review-styles.md`）。

---

## 10. 七人独立 Reviewer Panel（综合前各自独立）

> 以下每人先独立给出立场与分数倾向，再在 §10.8 综合。所有数值为本次独立模拟，与历史评审链中的任何数值无引用关系。

**Reviewer 1 — Best-Justified Reviewer**
- Lens：最强可辩护 accept case。
- Score tendency：7.4（lean accept 下沿）｜Confidence：4
- Main positive signal：C1→C1b 的配对失败→修复是真正可复现的方法论因果证据；全部 SHA 自洽、自动生成表、负结果全保留；C5 clean 重跑六门禁通过。
- Main negative signal：中心机制迁移为 false，真实视觉证据全为阴性。
- Evidence basis：`audits/R55`、`R56`；`metrics_pathblock.json` 六规则；`metrics_completed.json` 主矩阵。
- Fatal concern：无。
- Score-change condition：若 C1b 剂量在第二个独立真实子图（|P_all|>2）复现 → 上调。

**Reviewer 2 — Critical Reviewer**
- Lens：最强 reject case。
- Score tendency：5.8（borderline 偏负）｜Confidence：4
- Main positive signal： concedes 内部逻辑自洽、统计未 cherry-pick、披露异常坦诚。
- Main negative signal：headline 因果主张（"explains conflicting reports"）被自己的预注册检验 `mechanism_transfer_confirmed=false` 直接削弱；真实视觉任务上"拓扑不重要"反而使"控制构造解释矛盾"成为未被证实的推断；独立图族从未完成且 artifacts 缺失。
- Evidence basis：`r51_strong_baseline/metrics.json::decision`；`r39_visual_task/metrics.json`；`protocols/README.md` 引用不存在目录。
- Fatal concern：无硬致命；"中心机制不迁移 + 视觉证据全阴性 + 结论外推"组合接近 major threshold。
- Score-change condition：若官方 flyvis / 真实视觉任务上确认 path-aware 控制改变结论 → 撤回主负面。

**Reviewer 3 — Method / Soundness Reviewer**
- Lens：假设、算法/统计正确性、因果声明、失败模式。
- Score tendency：6.9｜Confidence：5
- Main positive signal：Eq.(1) 明确标注为"上界直觉、非逐 rung 精确概率"并改用直接测量；§4.8 五设置混淆、§4.9 单变量 sweep 隔离、oracle 1.0000、shared-init preflight 全部正确限定。
- Main negative signal：C1b 为补救性预注册；`|P_all|=2` 使剂量档位退化（p2==pfull），"单调"由两个不同点支撑；FAILED 预检未推翻却以补全版主矩阵为首要证据（C5 缓解但未完全消除）。
- Evidence basis：`correction-loop-state.md`；`config_pathblock.json`；`p2_gate_corrected.verdict=FAILED`；`R35` 审计。
- Fatal concern：无。
- Score-change condition：完全事前预注册的独立样本重复 C1b 设计，或明确标注 adaptive design。

**Reviewer 4 — Evidence / Experiment Reviewer**
- Lens：baseline、ablation、统计、robustness、reproducibility 细节。
- Score tendency：6.7｜Confidence：5
- Main positive signal：我逐字段核对约 130 个数字全部溯源；10 seeds / BH / CI / 探针 / robustness 四格 / 六门禁 / SHA 全链；无丢弃条件列。
- Main negative signal：C4 24 图族未完成且目录不存在；8/12 显著特征部分编码操纵本身；真实视觉证据全阴性；C1b 剂量分辨率低。
- Evidence basis：`r39_heldout/metrics.json`（sign 0.60 = majority）、`r51_pathblock/metrics_pathblock.json`（P_all=2）、`Glob r51_independent_family` 空。
- Fatal concern：无。
- Score-change condition：完成 24/24 并通过 `verify_c4_consistency.py`，且 sign agreement 超过 majority baseline。

**Reviewer 5 — Novelty / Positioning Reviewer**
- Lens：closest prior art、novelty delta、比较是否公平与最新。
- Score tendency：7.0｜Confidence：3
- Main positive signal：把"null generator"设为实验变量 + 路径生存审计 + 配对失败→修复，是对 `toposens2026`（degree-preserving null + shared init）的明确系统化增量；`contract-v2.md` 的 must-cite 清单在题录中齐备。
- Main negative signal：建立在 Maslov–Sneppen / Milo / triad census 等成熟组件上，增量偏方法论整合而非新理论；5 条 2026 arXiv 预印本与 DOI 本次未联网复核；`trainyourfly` 把同篇 arXiv 的 code-availability 单列成独立 bibitem，与 contract "no duplicate preprint versions" 自定规则有张力。
- Evidence basis：`main.bib` 16 条；§2 Related Work；`contract-v2.md` Citation Scope。
- Fatal concern：无（新颖性未坍塌，但封顶 4/5）。
- Score-change condition：在线复核题录真实性并合并 trainyourfly 条目后，定位更清晰（维度内）。

**Reviewer 6 — Writing / Clarity Reviewer**
- Lens：贡献可恢复性、图表可解释性、claim-evidence 可见性、术语稳定性。
- Score tendency：7.1｜Confidence：4
- Main positive signal：六节结构、限定充分、数字可回溯、scope conditions 明确、编译零警告、Conclusion 与表格一致。
- Main negative signal：摘要信息密度高且把 "C1 失败 → C1b 六规则全通过" 压缩为一句 "First ... decisive preregistered result"，可能误读；caption 含与 "no hand-typed numbers" 注释不一致的硬编码描述数字；§4.10 正文漏述表中 digits 的 task-aware 显著列；跨运行边数/ID 数字多（9,766 / 29,442 / 29,564 / 105,271；48,713 / 48,723 / 44,815 / 41,322）易混淆。
- Evidence basis：`main.tex` 摘要、§4.10、§5；`make_r53_tables.py:42`；`tables_r46.tex`。
- Fatal concern：无。
- Score-change condition：拆开摘要的两个检验叙述 + 补 §4.10 一句 → 维度内 +1。

**Reviewer 7 — Ethics / Reproducibility Reviewer**
- Lens：负责任研究、数据许可、artifact 可审计性、局限诚实。
- Score tendency：7.2｜Confidence：5
- Main positive signal：CC-BY 4.0 署名、无人类被试/动物/部署；FAILED 预检、CRC 缺陷、末块崩溃、dense 负结果、`hypothesis_supported=false`、C4 未完成、R37 异议全部如实上报；SHA 全链我独立复算一致；双盲与题录无外链合规。
- Main negative signal：`r51_independent_family/` 目录缺失使"all runs retained"与盘面不完全一致；18017 原始执行脚本 CRC 不符（已披露、被 C5 clean rerun 缓解）；LLM Usage Statement 披露"内部 calibration 用 machine-generated reviewer simulations 与 final full-mode acceptance review"，属流程披露，不影响科学结论但可能引发审稿人对自评流程的疑问。
- Evidence basis：`main.bib` / `main.log` / `R57` 审计；`Glob r51_independent_family` 空；`R35` 审计。
- Fatal concern：无。
- Score-change condition：补齐 C4 artifacts 或删除协议中 "retained" 的不实引用。

**10.8 Panel synthesis**
- Agreement：七人均认为**无 fatal flaw**；证据链数字可核验、无 cherry-pick、统计合格、CVPR 合规；两个预注册检验未被合并。分歧在于"这些证据能支撑多宽的结论"。
- Disagreement：R1/R6/R7 强调方法论洞察 + 可复现性 + 诚实度，倾向 7.0–7.4；R2/R4 强调中心机制迁移为 false + 独立图族缺失 + 视觉证据全阴性，倾向 5.8–6.7；R3 居中 6.9 并指出剂量退化。
- Decisive positive axis：C1→C1b 配对失败→修复（代码层诊断 + 修复后单调剂量）+ C3 faithful ladder rerun（`criterion_i=true`）+ C5 clean 六门禁 rerun —— 这些是**新科学证据**，非格式/披露修补。
- Decisive negative axis：A1（`mechanism_transfer_confirmed=false` + 真实视觉拓扑特异性阴性 + C1b 剂量因 |P_all|=2 退化）与 A3（第二个 falsifiable prediction 从未检验、C4 artifacts 不在盘）。
- Unresolved evidence：见 §16（A/B/C 类）。
- AC stance：**borderline 上沿，弱于 weak accept**。最终立场跟随最强未解决关切 A1，不被可复现性、诚实披露或格式合规平均掉；无致命缺陷故不 reject。

---

## 11. Concern-to-action 表

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A1 | Major | 中心因果主张外部效度为负；结论范围窄于标题/摘要/Conclusion 措辞 | `r51_strong_baseline/metrics.json::decision`（`mechanism_transfer_confirmed=false`）；`r39_visual_task/metrics.json`（degree-null≈real、MLP 支配）；§4.13 `|P_all|=2` | Significance, Evidence | experiment | 在多个独立、未操纵、不同 visual-ID 口径的真实子图或已发表视觉 pipeline 上确认 path-aware 控制改变结论；否则把 headline 收窄为"受控/低入度体制内" | `ccf-experiment-designer` / `ccf-paper-writer` | +0.5 至 +1 overall |
| A2 | Major | C1b 为补救性/自适应预注册；contract `expected_strong` 整体未达成 | `correction-loop-state.md` "after inspecting the in-flight C1 log"；`contract-v2.md` Expected Results；`main.tex` 摘要 | Soundness, Ethics | method/soundness | 以完全事前预注册在独立样本重复 C1b 设计；或在稿件明确标注 adaptive design 并说明六规则全通过属"修复后新检验" | `ccf-experiment-designer` / `ccf-paper-writer` | 标注可消除维度内 moderate 扣分；**不抬高 overall** |
| A3 | Major | 独立图族 C4 未完成、预注册预测 (ii) 从未检验、artifacts 目录不存在 | `protocols/README.md:5`、`experiment-traceability.md` row 37 引用 `results/r51_independent_family/`；`Glob` 返回空；`audits/stages/*.md` 12/24 OOM | Evidence, Reproducibility | experiment / reproducibility | 完成 24/24 并通过 `scripts/verify_c4_consistency.py`；或删除协议/追溯中"retained"的不实引用 | `ccf-experiment-designer` | +0.5 overall |
| A4 | Moderate | CVPR venue fit 间接：XOR 诊断、视觉证据全阴性、无 benchmark/定性视觉结果 | §3.2、§4.10、§4.12、4 个 PDF 图、`venue-review-styles.md` CVPR 段 | Significance | venue-mismatch | 至少一个真实视觉任务/已发表管线上的正面演示，或明确 analysis/benchmark-track 定位 | `ccf-paper-writer` | +0.5 overall 上限 |
| B1 | Moderate | 18017 CRC 不符 + 末块崩溃 + FAILED 预检 + R37 异议 → 主矩阵来自补全版，预注册 gate 未通过 | `R35-18017-evidence-audit.md`；`p2_gate_corrected.verdict=FAILED`；§4.2、§5 Limitations | Soundness, Reproducibility | reproducibility | 以 C5 clean hash-verifiable 9×10 重跑为主证据重述主矩阵地位（稿件已披露，无需新实验） | `f-research-v1` | 已由 C5 缓解；**不抬高 overall** |
| B2 | Minor | 题录 5 条 2026 arXiv + DOI 未在线复核；`trainyourfly` 把同篇 arXiv 的 code-availability 单列 | `main.bib` 16 条（注释 VERIFIED-WEB）、`contract-v2.md` "no duplicate preprint versions" | Clarity, Ethics | related-work | 在线复核题录真实性；合并或改写 `trainyourfly` 条目 | `ccf-paper-writer` | 消除 low desk 风险；不抬高 overall |
| C1 | Minor | 生成脚本 caption 硬编码描述性数字，与 "no hand-typed numbers" 注释不完全一致 | `make_r53_tables.py:42`、`make_r56_tables.py:99`、`make_paper_assets.py:170` | Clarity, Reproducibility | writing | caption 数字改由 metrics 读取，或删去 blanket 声明 | `ccf-paper-writer` | 维度内 |
| C2 | Minor | §4.10 正文漏述表中 digits 的 task-aware 显著列（Δ=−0.0148, CI 不含 0） | `tables_r46.tex` tab:visual vs `main.tex` §4.10 | Clarity | writing | 补一句叙述 | `ccf-paper-writer` | 维度内 |
| C3 | Minor | 摘要把 C1 失败→C1b 六规则全通过压缩为一句，可能误读为原始假设被证实；信息密度高 | `main.tex` Abstract | Clarity | writing | 明确区分"C1 阴性 / 修复后 C1b 阳性"两次运行 | `ccf-paper-writer` | 维度内 |

---

## 12. AC / Meta-Review

- **Reviewer consensus**：无致命缺陷；证据链可核验性极高（SHA 全链一致、自动生成表、约 130 个数字溯源、无 cherry-pick）；统计实践合格；负结果/失败披露完整；CVPR 合规完美；两个不同预注册检验未被合并。
- **Reviewer disagreement**：贡献的"可发表增量"到底是一个可复用的评估标准（R1/R6/R7），还是一个被自身阴性检验限定的窄诊断（R2/R4）。
- **Decisive acceptance axis**：C1→C1b 配对失败→修复实验提供了"全局不变量断言不足以排除路径级混杂"的可复现实证；C3 忠实 ladder 重跑在真实 wiring 上复现 weak/strict 模式；C5 clean 重跑闭合 provenance。这些是真实新证据，使论文 merit 超过纯 borderline-negative。
- **Decisive rejection axis**：`mechanism_transfer_confirmed=false` 是预注册决定性检验的阴性结果；真实视觉任务上拓扑特异性亦为阴性；C1b 剂量因 `|P_all|=2` / `p2==pfull` 退化；预注册第二个 falsifiable prediction（独立图族）从未检验且 artifacts 不在盘。A1 封顶。
- **AC stance**：**borderline（上沿）**。最终立场跟随最强未解决关切 A1，不被"诚实披露 / provenance 闭合 / 格式合规"平均掉。按任务约束：不因论文主动披露负结果或写出削弱自身主张的限定而额外惩罚；不因披露本身默认加分；不因格式/披露修补抬高由证据决定的总分。C5 与 SHA 链改善的是 Reproducibility / Soundness 的可核验性，**不新增中心机制的科学证据**，因此不抬高 overall。
- **Discussion risks**：CVPR 审稿人可能重复质疑"评估方法论 + 全阴性视觉结果"的 venue fit；摘要措辞与 §5 限定之间的张力可能被视为 overclaim；C4 目录缺失可能被追问"为何协议声称 retained 而盘面没有"。

---

## 13. 七维 Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
| :--- | :---: | :---: | :--- | :--- |
| Novelty | 4 | 4 | §3.2–§3.5 嵌套 ladder + 路径生存审计；§4.13 C1→C1b 配对诊断；§2 对 `toposens2026` 的增量定位 | 扣分：建立在 Maslov–Sneppen / Milo / triad census 等成熟组件上，增量偏方法论整合而非新理论，且与 closest prior work 的 delta 需更锐利定位。升至 5：给出路径生存充分性的形式化刻画或跨任务可迁移性证明。 |
| Soundness | 4 | 4 | Eq.(1) 已自限为"上界直觉"；§4.8 五设置混淆如实标注；§4.9 单变量 sweep + oracle 1.0000；`config*.json` shared-init / preflight；C5 六门禁 | 扣分：C1b 属补救性预注册（`correction-loop-state.md`）；`|P_all|=2` 使剂量档位退化、p2==pfull；18017 FAILED 预检未推翻却以补全版主矩阵为首要证据（C5 缓解）。升至 5：完全事前预注册的独立重复 + 完整剂量档位。 |
| Evidence | 4 | 5 | 约 130 个头条数字全部溯源；10 seeds / 5000 bootstrap / BH / 探针 / robustness 四格；`r51_*` 三批 + `r39_*` 六批；自动生成表遍历全部条件 | 扣分：C4 24 图族未完成且 `r51_independent_family/` 不存在；真实视觉证据全为阴性；机制迁移未确认；C1b 剂量仅两个不同点。升至 5：完成 24/24 独立图族并显著超过 majority sign baseline + 至少两个独立真实子图复现。 |
| Significance | **3** | 4 | §5 "Using the standard in practice" 四步审计；`contract-v2.md` 评估方法论定位；§4.10 / §4.12 真实视觉负边界；§4.11 `mechanism_transfer_confirmed=false` | **具体扣分（≤3 必填）**：对 CVPR 视觉受众价值间接——无 benchmark 提升、无自然视觉任务正面结果、无官方 flyvis 复现；且 headline "explains conflicting reports" 被自身预注册阴性检验与真实视觉阴性结果限定为推断性结论，证据只支撑"受控/低入度体制内 path-aware 控制决定效应"。**修复条件**：在已发表 connectome-constrained 视觉管线或真实视觉任务上确认 path-aware 控制改变结论，或把标题/摘要/Conclusion 收窄为该体制内的方法论诊断 → 可升至 4（overall +0.5 至 +1）。 |
| Clarity | 4 | 4 | 六节结构、claim-evidence 可见、限定充分、0 Overfull / 0 undefined refs | 扣分：摘要密度高且压缩 C1/C1b（C3）；§4.10 漏述表中一列（C2）；caption 硬编码描述数字（C1）；跨运行边数/ID 数字多易混淆。升至 5：拆分摘要两个检验叙述 + 补 §4.10 一句 + 统一 caption 措辞。 |
| Reproducibility | 4 | 5 | 28 个脚本 + config/metrics/manifest SHA-256 我独立重算全部一致；§5 四个前缀匹配；`metrics*.json` 嵌套 `script_sha256` 逐字节吻合；6 个生成脚本无手抄数值 | 扣分：`results/r51_independent_family/` 全项目不存在，C4 artifacts 不可审计；18017 原始执行脚本 CRC 不符（已披露，被 C5 clean rerun 缓解）。升至 5：补齐 C4 artifacts 或删除"retained"不实引用，并使全部被引证据目录在盘可核验。 |
| Ethics / Limitations | 4 | 4 | §5 Limitations / Ethics；CC-BY 4.0 署名；无人类被试；FAILED / CRC / 崩溃 / R37 / C4 / 口径限定全披露；双盲与题录无外链 | 扣分（不因披露加分）：5 条 2026 题录 + DOI 本次未在线复核；`trainyourfly` 单列同篇 arXiv 的 code-availability 与 contract "no duplicate preprint versions" 张力；C4 目录缺失使"all runs retained"与盘面不完全一致。升至 5：在线复核题录 + 合并该条目 + 补齐 artifacts。 |

**Overall:** 6.9  | **Scholarly Confidence:** 4

**Recommendation:** borderline（上沿，弱于 weak accept；无致命缺陷故不 reject）

**Verdict:** 总分 6.9 由**最强未解决关切 A1**（中心因果主张外部效度为负：`mechanism_transfer_confirmed=false` + 真实视觉拓扑特异性阴性 + C1b 剂量退化）单独钉定，**不是七维平均**：若把七维（4,4,4,3,4,4,4）机械线性换算会得到约 7.7，但按 `Never round scores` 与"总分不得由维度平均抹平最强未解决关切"，该换算被明确弃用。可复现性极高、诚实披露、格式合规只影响 Reproducibility / Soundness 的可核验性，**不抬高由证据决定的 overall**。分数未四舍五入到任何整数，未锚定任何历史数值或验收阈值，未因披露负结果或自限性限定额外惩罚，也未因披露/格式修补加分。Confidence=4：full paper + 全部 artifacts + 本地 venue guide 齐备，但未联网复核 CVPR 2027 官方 CFP 与 2026 题录真实性，且 C4 artifacts 缺失使部分证据不可独立核验（"full paper available; minor missing context"）。

---

## 14. Score-Change Conditions

| Change | Condition | Likely affected dimensions | Expected movement |
| :--- | :--- | :--- | :--- |
| Raise score | 在 ≥2 个独立、未操纵、不同 visual-ID 口径的真实子图上以完整剂量档位（\|P_all\|>2、p2≠pfull）复现 C1b 单调剂量；或使 `mechanism_transfer_confirmed=true` | Significance, Evidence, Soundness | +0.5 至 +1 overall（→ 7.4–7.9） |
| Raise score | 完成 C4 24/24 图族并通过 `verify_c4_consistency.py`，LOGO sign agreement 显著超过 majority baseline | Evidence, Significance | +0.5 overall |
| Raise score | 用官方 flyvis / 已发表视觉 pipeline 复现，并在真实视觉任务上显示 path-aware 控制改变结论 | Significance, Evidence, Novelty | +0.5 至 +1 overall |
| Lower score | 独立复核发现任一头条数字与 `metrics*.json` 不符，或 C1b 单调性在排除 `p2==pfull` 重复点后不成立 | Soundness, Reproducibility, Evidence | −1 overall 或 fatal |
| Lower score | 确认 R37 异议意味着结构敏感性前提从未通过，或 18017 CRC 缺陷 / 末块崩溃影响任何报告数字 | Soundness, Reproducibility | −0.5 至 −1 overall |
| No quick change | 自然视觉任务上的外部效度、官方 flyvis 复现、机制迁移确认需新实验纲领；继续修流程 / 披露 / 格式 / 题录不会再抬高总分 | Significance, Evidence | 投稿前不大可能改变 |

**两个方向的 tie-breaker（把 6.9 固定住）**：
- **向上 tie-breaker（为何不是 6.0 / 6.5）**：C1→C1b 的配对失败→修复（代码层诊断 + 修复后单调剂量 + 原始阴性只读保留）、C3 faithful ladder rerun 的 `criterion_i=true`、C5 clean 9×10 六门禁 rerun，三者是**新增的科学证据**而非格式/披露修补，使 merits 略超过纯 borderline-negative。它们同时把 Evidence / Soundness / Reproducibility 推到 4 分档。
- **向下 tie-breaker（为何不是 7.0 / 7.5）**：`mechanism_transfer_confirmed=false` 是预注册决定性检验的阴性结果，真实视觉任务上拓扑特异性亦为阴性，C1b 剂量因 `|P_all|=2` 退化（`p2==pfull`），预注册第二个 falsifiable prediction 从未检验且 C4 artifacts 不在盘 —— A1 + A3 作为最强未解决关切封顶，阻止达到 lean accept。**两个 tie-breaker 共同把分数锁在 6.9，未向任何整数或目标收敛。**

---

## 15. Questions For Authors（仅列会改变分数/关切者）

1. `results/r51_independent_family/` 在被评审版本内不存在，但 `protocols/README.md` 与 `experiment-traceability.md` row 37 声称 frozen config 已 retained —— 12/24 与两次 CUDA OOM 的可核验 artifacts 在哪里？若确实未落盘，为何协议写 "retained"？
2. C1b 修复计划写于"inspecting the in-flight C1 log"之后：请说明在看到 C1 中间剂量读数后设计 path-blocking 约束，是否应被标注为 adaptive/补救性预注册；`expected_strong` 的合取目标未整体达成是否应在摘要更明确说明？
3. `|P_all|=2` 使 `p2==pfull`、剂量—反应只有两个不同准确率点 —— 请给出在 `|P_all|>2` 子图上的剂量证据，或说明为何两档重复仍足以支撑"monotone dose satisfying all six decision rules"。
4. 标题/摘要/Conclusion 的 "explains conflicting reports" 与 `mechanism_transfer_confirmed=false`、真实视觉拓扑特异性阴性之间，作者认为证据支撑的因果范围边界在哪里？
5. §4.10 表中 digits 的 task-aware null `Δ=−0.0148`（CI 不含 0）为何未在正文叙述？该显著负值是否影响"degree-preserving 解释增益"的表述？

---

## 16. Unresolved（A / B / C 类）

**A 类 — 科学/证据核心（决定总分，未被维度平均抹平）**
- A1 中心因果主张外部效度为负 / 结论范围窄于措辞（见 §9、§13）。**最强未解决关切**。
- A2 C1b 补救性预注册强度；contract `expected_strong` 整体未达成。
- A3 预注册第二个 falsifiable prediction 从未检验；C4 artifacts 目录不存在，12/24 与两次 OOM 不可独立核验。
- A4 CVPR venue fit 间接（无自然视觉任务正面结果、无官方 flyvis、视觉证据全阴性）。

**B 类 — 可核验性 / 流程（已披露或已缓解，不抬高总分）**
- B1 18017 原始执行脚本 CRC 不符 + 末块 `NameError` + LOGO 从 persisted rows 重算；3-seed 预检 `verdict=FAILED` 未被推翻，R37 门禁异议保留；主矩阵为本地补全版 `metrics_completed.json`。C5 clean hash-verifiable 9×10 重跑（六门禁全通过）缓解但不等同于"预注册 gate 通过"。
- B2 16 条题录的在线真实性（5 条 2026 arXiv 预印本、2 条 DOI）本次未复核；`trainyourfly` 条目把同篇 arXiv 的 code-availability 单列。
- B3 跨运行 visual-ID 口径（9,766 / 29,442 / 29,564 / 105,271 IDs；48,713 / 48,723 / 44,815 / 41,322 edges）不可混用 —— 稿件已充分限定，仅 within-batch 配对有效。

**C 类 — 写作 / 呈现（minor，维度内可修）**
- C1 caption 硬编码描述性数字与 "no hand-typed numbers" 注释不完全一致。
- C2 §4.10 漏述表中 digits 的 task-aware 显著列。
- C3 摘要压缩 C1/C1b 两次运行、信息密度高，存在误读风险。
- C4 LLM Usage Statement 含"内部 machine-generated reviewer simulations / final full-mode acceptance review"流程披露 —— 按任务约束**不因此加減分**，仅记录为呈现事实。

---

## 17. Checks run / Checks skipped / 本次是否重新联网核实

**Checks run**
1. 版本锁定：`main.tex` 字节数 / md5 / sha256；`main.pdf` 9 页（pypdf 6.19.0）；p1–p9 逐页文本，p8/p9 全文打印确认 p9 无正文残留。
2. SHA-256 独立重算：28 个 `results/**/*.py` + 关键 config / metrics / manifest；与 `metrics*.json` 嵌套 `environment.script_sha256`、`script_sha256` 字典、`config_sha256*`、`manifest` 声明、稿件 §5 四个前缀、C1b `8ee6605e…` 逐一对账 —— 全部一致。
3. 数字溯源：约 130 个头条数值在 15 个 `metrics*.json` 中 round-to-4 匹配；4 个派生量（0.0244 / 2.1e-4 / in-deg 一位小数 / −0.0477）逐个复算。
4. §4.10 MNIST 反向 delta 与 digits task-aware delta 的字段分离核验（排除数字搬运 / 符号翻转）。
5. 6 个生成脚本全文审查：遍历条件完整性、无手抄数值、无丢弃列、aborted runs 不用于数字。
6. 预注册判定字段逐项：`p2_gate_corrected.verdict`、`task_a.decision_rules`、`task_a_pathblock.decision_rules`、`P_all_cardinality`、`original_18307_reference`、`task_c5.gates`、`r51_strong_baseline.decision`、`criterion_i/ii/iii`。
7. 统计口径：seeds / shared_init / bootstrap_R / BH / oracle-leakage probes / LOGO sign & MAE / robustness 四格 / `p2==pfull`。
8. 负结果/失败披露对账（§5 表 11 项）与"两个不同预注册检验不合并"核验。
9. CVPR 合规：页数、p9 内容、双盲、题录 0 外链、`main.log` 0 Overfull / 0 undefined、`main.bib` 16 = `main.bbl` 16、LLM 声明位置、章节数。
10. 证据树完整性：`Glob **/r51_independent_family/**`（空）；`protocols/README.md`、`experiment-traceability.md` 引用核对；`scripts/verify_c4_consistency.py` 存在性。
11. 历史评审链 `ccfa-review-reports/*.md` 以 Grep 抽取关切演化（不导入分数）。

**Checks skipped（如实声明）**
- 4 个 `paper/figures/*.pdf` 未逐图做视觉检查（仅核对 caption、生成脚本与 pypdf 页面文本）；CVPR 把视觉证据当作证据，此项略降低 Clarity/Evidence 的可核验完整度。
- 1.05 GB MaleCNS Feather 原始权重/标注文件未拉取（稿件声明 streamed column projection、never densify；本地仅有 14.5 MB `body-annotations.feather`）。
- 未执行任何生成脚本（避免写入任何文件；改为静态审查 + 只读复算）；未运行 `readonly-validator` / `guard` / `verify_c4_consistency.py`（它们是作者会话的 gate，且本报告不改任何文件）。
- `results/p2_gate/.claude/skills/novix/**` 大量与论文无关的第三方 skill 文档已排除，未逐文件审阅。
- 未做 prompt-injection 的逐图像/逐 PDF 对象级扫描（仅对 tex / tables / scripts / caption 文本做检查）。

**本次是否重新联网核实：否。** 本次评审未调用任何联网工具（无 WebSearch / WebFetch / 在线 DB）。因此：
- CVPR 2027 官方 CFP、强制 LLM Usage Statement 的当年官方措辞、8 页上限的当年细则，均按**本地 `venue-guides/cvpr.md`（CVPR 2026 迁移版，注明 "official policy must be rechecked before submission"）+ 任务给定规格**核验，未做在线 re-verification；
- `main.bib` 16 条题录（含 5 条 2026 arXiv 预印本、2 条 DOI、1 条把同篇 arXiv 的 code-availability 单列的 `@misc`）的**真实性未在线复核**，标记为 unverified related-work risk（B2）；
- MaleCNS v1.0 CC-BY 4.0 数据来源按稿件与 `config.json` 声明确认，未在线复核。

此项与 C4 artifacts 缺失共同使 Scholarly Confidence 定为 **4**（而非 5）。

---

## 18. Output self-check

- 报告仅写入指定唯一路径；未修改稿件、指标、审计、账本、校验器、guard 或任何其它文件；未创建其它评审报告。✔
- 报告中恰好一行总体评分汇总行（位于 §13），无第二处同格式行。✔
- `Never round scores`：6.9 未取整、未向任何目标或历史数值收敛；两个方向 tie-breaker 明确写出。✔
- 总分由最强未解决关切 A1 决定，未被七维平均（4,4,4,3,4,4,4）抹平。✔
- 未因主动披露负结果 / 自限性限定额外惩罚；未因披露本身默认加分；未因格式 / 披露 / provenance 修补抬高由证据决定的总分。✔
- 每个 ≤3 的维度（Significance=3）含具体扣分与修复条件；每个维度含可核验引用与 score-change condition。✔
- 历史分数 / 验收阈值未作为锚点、未照抄、未进入评分推理（§0 独立性声明）。✔
- 被评审版本 md5、Checks run、Unresolved（A/B/C）、联网核实自述均已包含。✔
- 表格 Markdown 分隔符与列数一致；无 `TBD` / `TODO` / 占位符；无空标题。✔

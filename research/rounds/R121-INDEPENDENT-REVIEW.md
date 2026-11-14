# R121 独立复核报告（general-purpose-1，全新隔离，无先验上下文）

复核轮次：R121。项目根目录：`/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision`。本报告所有数值、哈希、逐字引文均由本人从**原始源字节**用自有代码／逻辑重算，不采信任何现成结论。

## 0. 方法与约束声明

- 全程 READ-ONLY 对待所有既有文件；本人创建的**唯一**文件即本报告。`validate_single_paper.py` 以无 `--out` 方式运行（只向 stdout 打印，不写盘）；`guard_engine.py check` 按任务要求带 `-o` 写到既有临时目录 `/tmp`，事后已删除该临时产物，因此除本报告外没有留下任何新建文件。
- 未执行任何网络访问、训练、推理、前向传播（forward pass）、git 操作。
- **未把任何 R121 产物当作数据源读取**：`R121-RAW-v1.json`、`R121-RAW-v2.json`、`R121-VERIFICATION-v1.json`、`R121-VERIFICATION.json`、`R121-collect.py`、`R121-collect-v2.py`、`R121-verify.py`、`R121-verify-v1.py`、`R121-V1-DEFECTS.md`、`R121-guard-report.md` 以及 `success-condition-R121/isolated/` 下的副本，均不作为取数来源。A–I 全部结论在读取审计之前独立形成。
- **按要求最后才读取** `success-condition-R121/R121-ROUND-AUDIT.md`：在 A–I 全部结论形成之后，为 J 组（瑕疵分级）与「逐条对照」而读取，并在此明确声明「我确实这样做了」。读取时间点为本次复核的末尾。
- 透明度说明：在核查 mtime 归因时，我确实在**既有**文件 `goal-ledger.md`、`papers/R63-results/STATUS.md`（以及 `.workbuddy/memory/2026-11-14.md`）中看到了 R121 的**只追加**（append-only）账本／状态行；这些是主会话／心跳自身的记账，不是 R121 的验证产物，我也**没有**用它们为 A–I 的任何事实结论取数。所有事实均从被版本锁定的原始字节重算。
- 关于「数值 `**Overall:**` 行」的口径：本项目复核中统一指**行首**（允许前导空白）以 `**Overall:**` 开头、紧跟一个十进制数值的行；正则约等价于 `^\s*\*\*Overall:\*\*\s*[0-9]`。本报告正文刻意不产生任何此类行；所有引文均内嵌于句中。

---

## A. governing 独立 full 评审（r95）

文件：`ccfa-review-reports/paper-null-ladder-r95-independent-review-20261111.md`

| 项 | 实测值 |
|:--|:--|
| 字节数 | **52,430 B** |
| 行数 | 514 |
| sha256 | `c67f8cd39c17d2fe7ae6d1eab9414be1275a4b7f9ac236c36d4d44aab02fb97a` |
| md5（附） | `3a1a2cc98e9daae76b1693373fe18a5c` |
| mtime | `2026-11-11 15:01:39`（epoch `1794380499.47`） |

**Overall 分数所在行：第 419 行**，逐字为 `` `**Overall:** 6  | **Scholarly Confidence:** 4` ``（两个空格，`Scholarly Confidence` 带粗体标记）。全文仅 §11 出现这一行精确格式（第 509 行自述亦如此）。

§13「No quick change」行（**第 450 行**）逐字：

```
| **No quick change** | 继续补流程/披露/格式（摘要拆分、披露表化、补 LLM 声明、修 overfull、补编译日志、统一口径、范围表）——这些属透明度与可核验性，**不新增支持中心主张的科学证据** | Clarity, Reproducibility（维度内） | 不改变 evidence-capped overall；行政 blocker 解除仅恢复「可提交」状态 |
```

其中关于「流程／披露／格式不改变 evidence-capped overall」的**精确语句**为：「**不新增支持中心主张的科学证据**」与「**不改变 evidence-capped overall；行政 blocker 解除仅恢复「可提交」状态**」。

§13「Raise score」行（**第 448 行**）逐字：

```
| **Raise score** | (a) 真实 MaleCNS 图上以预注册协议**确认** motif-survival 阈值迁移（`hypothesis_supported=true` 且度保持 null 不再保留优势）；(b) 在 flyvis/`toposens2026` 栈复跑同协议对证；(c) 至少一项真实视觉任务上该诊断标准改变了一个实际结论 | Evidence, Significance, Novelty | 单项 +0.5；三项齐备 Overall 6→7~7.5（维度分不单独抬高总分，须由证据性关切解除触发） |
```

三项条件 (a)(b)(c) 齐备，且含「单项 +0.5；三项齐备 Overall 6→7~7.5（维度分不单独抬高总分，须由证据性关切解除触发）」。

§15「Raising the score」行（**第 473 行**）逐字：`Raising the score would require: 真实图上确认 motif-survival 阈值迁移（预注册协议下 hypothesis_supported=true）`（第 474 行续 `+ 至少一个强基线栈的同协议复跑 + 一项真实视觉任务上该诊断标准改变实际结论；三者为证据性新增，非 prose/格式修补。`）。

§8 M1（**第 240 行**）逐字：`Required fix: 需新的真实图实验确认机制迁移（非 prose 可修），见 §13 No quick change。` —— 含「非 prose 可修」。
§8 M2（**第 249 行**）逐字：`Required fix: 若投主会，需在 rebuttal 论证方法学标准对视觉实证研究的直接迁移价值；无法靠 prose 补出视觉贡献。` —— 含「无法靠 prose 补出视觉贡献」。

§11 两维评分（**第 413 行** Evidence = 3、**第 414 行** Significance = 3）逐字首字段分别为 `| Evidence | 3 | 5 | …` 与 `| Significance | 3 | 4 | …`（两行全文已核对，含「**升到 4**」条件）。

第 **454 行** tie-breaker（阻止 Overall 上到 7）逐字：

```
- **阻止上移到 7（weak accept）的 tie-breaker**：最强未解决关切是**证据性**的——中心机制（motif 生存为控制充分性因果判据）仅在 96 节点合成 XOR 诊断图上确立，真实 MaleCNS 图 `hypothesis_supported=false` 且度保持 null 反向保留优势（`0.6162`），真实视觉任务为负结果、非图 MLP `0.9722` 主导，flyvis/`toposens2026` 强基线未复跑。按 `calibration-and-rank.md` Consistency Check #1（overall 必须匹配最强未解决弱点）与 `review-output-standards.md` Synthesis Rule（final stance 跟随最强未解决关切、不被平均掉），这组 ≥3 个决定性关切不允许 Overall 上到 7（7 要求「no fatal risk; one or two moderate concerns」）。
```

A 组结论：**MATCH**。任务给出的行号近似值（240 / 249 / 413 / 414 / 419 / 448 / 450 / 454 / 473）与实测逐行号完全一致。

---

## B. 七轮先前心跳 round audit

七份均位于 `auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/` 下的原始路径；`reconciliation-R120/isolated/` 与 `success-condition-R121/isolated/` 内的副本一律不取数。七份原文的实际落盘 mtime 为顺序心跳：`R114 2026-11-13 22:49:24` → `R115 11-14 00:25:17` → `R116 02:06:15` → `R117 03:32:52` → `R118 05:20:33` → `R119 06:46:04` → `R120 08:57:30`，全部早于 R121 的 ~10:20 窗口。

| 轮次 | 字节 | sha256 | 声明行(逐字 token) | READONLY | NOT_GATE_PASS | NOT_SCIENTIFIC_RESULT | 行首数值 `**Overall:**` | 新正向科学结果 / 门晋级声明 |
|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R114 | 8,878 | `5aa8cd04…508bf08` | :44 `全轮 READONLY_FIRSTHAND_EVIDENCE_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT` | 1 | 1 | 1 | 0 | 无（:69「G0 may be passed: NO / Scientific result claimed: NO」） |
| R115 | 11,155 | `c037fc25…f417e8abf82` | :3 `**性质**：READONLY_FIRSTHAND_EVIDENCE_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT` | 1 | 1 | 1 | 0 | 无（:81 同） |
| R116 | 8,719 | `87a25143…370c89f227` | :71 `全 READONLY_FIRSTHAND_EVIDENCE_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT` | 1 | 1 | 1 | 0 | 无（:45 同） |
| R117 | 11,835 | `d189ceaa…805` | :4 `READONLY_EXECUTION_PREMISE_PROBE_NOT_SCIENTIFIC_RESULT_NOT_GATE_PASS_NOT_FORWARD_PASS`；:63 `全 READONLY_EXECUTION_PREMISE_PROBE` | 2 | 1 | 1 | 0 | 无（:47/:79 含 Forward pass performed: NO） |
| R118 | 11,541 | `127190cd…06a33b79b94` | :52 `全 READONLY_REGISTRY_GAP_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT` | 1 | 1 | 1 | 0 | 无（:78 含 REPRODUCIBLE_WITH_WORDING_AND_JUDGMENT_DEFECTS / NO / NO） |
| R119 | 8,888 | `14133228…d7d58297` | :4 `**Kind:** READONLY_REVIEW_LAUNCH_PROTOCOL_CHAIN_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`；:116 `All READONLY_REVIEW_LAUNCH_PROTOCOL_CHAIN_AUDIT` | 2 | 1 | 1 | 0 | 无（:19/:118 明确零 promotion） |
| R120 | 15,418 | `a61b18e8…344` | :3 `**状态：READ_ONLY_RECONCILIATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT**`；:59 `全 READ_ONLY_RECONCILIATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT` | 0（但 `READ_ONLY`=2） | 2 | 3 | 0 | 无（:78/:88 明确全 REFUTED、无 governing 改动） |

读音：R120 用的是 `READ_ONLY`（带下划线），不是字面 `READONLY`；语义上（只读 + NOT_GATE_PASS + NOT_SCIENTIFIC_RESULT）该复合声明完整存在。其余六份为字面 `READONLY`。

**计数汇总（7 份全文）**：声明只读 + `NOT_GATE_PASS` + `NOT_SCIENTIFIC_RESULT` 的文件 = **7/7**；声称「新正向科学结果」= **0**；声称「门已 passed」= **0**；行首数值 `**Overall:**` 行 = **0**（7/7 均为 0）；且 7/7 的结论行均含 `G0 may be passed: NO`、`Scientific result claimed: NO`。B 组结论：**MATCH**。

---

## C. 升分条件 (a)：真实图 `hypothesis_supported`

用自有脚本遍历 `papers/` 下全部 **632** 个 `.json`，取**顶层**含 `hypothesis_supported` 键者，共 **11** 个（另有 12 个文件在**嵌套**位置出现该字符串，逐一核验其值均为 `False` 或仅作历史引用，不属顶层键）：

顶层 11 个（值 / `data.source` / 字节）：

| 值 | data.source | 字节 | 路径（`/results/` 之后） |
|:--|:--|--:|:--|
| `False` | `REAL_MALECNS_VISUAL_SUBGRAPH` | 3,026 | `f-research-v1-run-20261107-203506-null-ladder/results/r39_real_connectome/metrics.json` |
| `False` | `REAL_MALECNS_VISUAL_SUBGRAPH` | 3,346 | `…/r39_real_connectome_v2/metrics.json` |
| `False` | `REAL_MALECNS_VISUAL_SUBGRAPH` | 3,199 | `…/r39_real_connectome_v2/metrics_from_trajectory.json` |
| `False` | `REAL_MALECNS_VISUAL_SUBGRAPH` | 3,026 | `f-research-v1-run-20261108-102500-null-ladder-v2/results/r39_real_connectome/metrics.json` |
| `False` | `REAL_MALECNS_VISUAL_SUBGRAPH` | 3,346 | `…/r39_real_connectome_v2/metrics.json` |
| `False` | `REAL_MALECNS_VISUAL_SUBGRAPH` | 3,199 | `…/r39_real_connectome_v2/metrics_from_trajectory.json` |
| `True` | `SYNTHETIC_APPROXIMATION` | 7,416 | `…/p3_p4_taskaware/metrics.json`（两个 run 各 1） |
| `True` | `SYNTHETIC_APPROXIMATION` | 7,416 | `…/p3_p4_taskaware/metrics.json`（v2 run） |
| `True` | `None`（无 `data` 键） | 4,501 | `…/p3_p4_taskaware/metrics_from_trajectory.json`（两个 run 各 1） |
| `True` | `None`（无 `data` 键） | 4,501 | `…/p3_p4_taskaware/metrics_from_trajectory.json`（v2 run） |
| `False` | `None`（无 `data` 键） | 11,924 | `…/r51_motif_survival/task_a_results.json` |

分类：**REAL MaleCNS 连接组** = 明确标注 `REAL_MALECNS_VISUAL_SUBGRAPH` 的 **6** 个文件，`hypothesis_supported` **全部 `False`**；**SYNTHETIC_APPROXIMATION 受控图** = 2 个显式标注文件，均为 `True`；另有 3 个无 `data.source` 的文件（2 个 `True` 为 p3_p4_taskaware 合成任务的 trajectory 镜像，1 个 `False` 为 r51_motif_survival 合成图）。嵌套出现的 12 个文件里，唯一带 `data/source` 的 `r51_multisubgraph/config_multisubgraph.json` 指向 local MaleCNS v1.0，其嵌套 `hypothesis_supported` 亦为 `False`。

**是否存在任何真实图文件 `hypothesis_supported=true`？—— 否。** 全部 6 个真实 MaleCNS 文件为 `False`；所有 `True` 值都属合成受控图或其 trajectory 镜像。故 (a) **未满足**。C 组结论：**MATCH**。

---

## D. 升分条件 (b)：版本锁定稿件与 flyvis 复跑

R95 §1 版本锁：`main.tex` 716 行 / 40,175 B / md5 `e4bfad51ad834fdccdb6db7821e158c6`。全项目 `main.tex` 逐一实测后有**两份**精确匹配（且 `cmp` 逐字节一致、均 716 行）：

1. `papers/paper-null-ladder/R49-7.5-DELIVERY/manuscript/main.tex`
2. `papers/paper-null-ladder/f-research-v1-run-20261107-203506-null-ladder/paper/f-submit-v1-run-20261110-115500-phenomenon/main.tex`

两份均为 **40,175 B**、md5 `e4bfad51ad834fdccdb6db7821e158c6`、716 行、`cmp` 相同。

「did not rerun their flyvis stack」自认：**第 637 行**，逐字为 `We did not rerun their flyvis stack and make no benchmark-reproduction claim.`（两份同）。R95 §8 亦引 `main.tex:637`。

**文件名同时含 rerun/reproduce 类 token 与 flyvis/toposens 的文件计数**：以**文件名（basename）**严格判定（`rerun|re-run|reproduc*` 且 `flyvis|toposens*`）= **0**。若放宽到**整条路径**，得 2 个巧合命中，均非复跑产物、且两 token 不同时出现在 basename：`…/code-audit/flyvis-local-deps/…/markdown/preprocessors.pyi`（`repro` 只是 `preprocessors` 的子串误命中，`flyvis` 仅在目录名）与 `…/sources/toposens/docs/reproducibility.md`（`reproducibility` 在文件名，`toposens` 仅在目录名，且是文档不是指标）。因此「flyvis/toposens 复跑指标文件 0 份」成立，(b) **未满足**。D 组结论：**MATCH**。

---

## E. 升分条件 (c)：真实视觉任务

文件：`papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2/results/r39_visual_task/metrics.json`（8,644 B，sha256 `81d938a4…9ad9`，mtime `2026-11-08 10:48:25`，为 R121 之前的既有文件）。

- `mlp_baseline.mean_acc` = **0.9722222222222222**（专用对象与 `mean_acc.mlp_baseline` 一致）。
- `real_minus_condition.degree_preserving_null.delta` = **−0.0004629629629628873**（≈ −0.000463）。
- 其 `ci95` = **[−0.04120370370370371, 0.04398148148148153]**，**包含 0**。
- 旁证：`mean_acc.real = 0.7185185` ≈ `degree_preserving_null = 0.7189815`；`task_aware_null` delta −0.0148（ci95 上界 −0.00093）；MNIST 附加里 `mlp_baseline 0.8879` 亦主导 `real 0.7649`。与 R95 §8 M2 第 246–247 行逐字一致。

**数据是否支持「该诊断在真实视觉任务上改变了一个实际结论」？—— 不支持。** 度保持 null 的差异几近于零且 CI95 跨 0，非图 MLP 以 0.9722 主导所有图模型，真实视觉任务为负结果；稿件 `main.tex:88-91 / 614` 自述无视觉精度声称。故 (c) **未满足**。E 组结论：**MATCH**。

---

## F. 双机器门（本人只读运行）

**(1) `readonly-validator/validate_single_paper.py`**（无 `--out`，只读）：`EXIT=1`，**verdict = `NOT_QUALIFIED`**，`overall_score = 6.0`，`threshold = 7.0`，`comparison_operator = ">="`，`score_meets_threshold = false`。五项检查：`D1_guidance_validated ✓`、`D2_tex_pdf_pipeline_all_passed ✗`（26 阶段中 P9–P21 未 passed）、`D3_independent_full_review ✗`（governing=6.0 in r95）、`D4_novix_experiment_evidence ✓`、`D5_six_sections_traceability ✗`（`claim_evidence_matrix=False`）。失败项 = **D2 / D3 / D5**。D3 detail 自列 `all_scores=[7.5, 8.2, 7.0, 7.5, 7.5, 6.9, 6.3, 5.4, 5.2, 6.0]`，governing 取最新 r95 = 6.0。

**(2) `task-completion-guard/guard_engine.py check -l guard/ledger-null-ladder.json -o <临时目录>`**：`EXIT=1`，**结论 = `INCOMPLETE`**。交付物 7 项全 PASS；验收条件 6 项中 **A2**（pipeline-state 全 26 阶段 status=passed，退出码 1）与 **A6**（最新独立 full 评审 Overall 严格 `> 8.0`，退出码 1）**FAIL**，其余 A1/A3/A4/A5 PASS；步骤台账 **S1–S7 共 7 步全部 pending**（每步证据 0 条），动作序列 0 条；发现 2 条 `[W-W05]`（A2、A6）。`-o` 产物为纯文本（非 JSON），已删除。

附带事实：`guard/ledger-null-ladder.json` 的 A6 文案为「严格 `> 8.0`」、硬编码 `g>8.0`，而 `GOAL-ITERATION-R107.md:22-25` 与 validator 现行为 `>= 7.0`（7.0 qualifies）——这是 R107 之前既有的「双口径」不一致（R109 审计 N-17、R119 STATUS.md 均已登记），guard ledger mtime `2026-11-13 08:09:20`、validator 脚本 mtime `2026-11-13 08:09:06`，均早于 R121，**非 R121 改动**。F 组结论：**MATCH**。

---

## G. 主线 `pipeline-state.json`

文件：`auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json`，**3,723 B**，sha256 `bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d`，mtime `2026-11-12 10:43:12`（与 R120 审计所引 `bcb48bb964e657a4` 一致）。共 **12** 阶段：

| # | id | status | inputs 数 | evidence 数 |
|--:|:--|:--|--:|--:|
| 1 | `CCFA-startup` | passed | 2 | 4 |
| 2 | `G0` | **pending** | **0** | **0** |
| 3 | `G1` | pending | 0 | 0 |
| 4 | `G2` | pending | 0 | 0 |
| 5 | `G3` | pending | 0 | 0 |
| 6 | `G4` | pending | 0 | 0 |
| 7 | `G5` | pending | 0 | 0 |
| 8 | `G6` | pending | 0 | 0 |
| 9 | `G7` | pending | 0 | 0 |
| 10 | `G8` | pending | 0 | 0 |
| 11 | `validation` | pending | 0 | 0 |
| 12 | `handoff` | pending | 0 | 0 |

状态计数：`passed=1`、`pending=11`。**G0 是否 pending 且 `inputs`/`evidence` 均为空？—— 是**（`inputs=[]`、`evidence=[]`）。G 组结论：**MATCH**。

---

## H. 全项目行首数值 `**Overall:**` 扫描

口径：扫描项目根下全部 `*.md`，剪除所有 `.git` 目录；sibling 仓库 `/Users/xhf/Downloads/phd/4090/research-sync-public` 在项目根之外，本就不在扫描树内。共扫描 **6,124** 个 `.md`。

- **行首数值 `**Overall:**` 行总数 = 15**（分布于 13 个文件；`paper-null-ladder-full-review-20261108.md` 与 `paper-null-ladder-r39-full-review-20261108.md` 各含 2 行）。逐条为：
  - `ccfa-review-reports/` 10 份历史评审共 12 行（含 r95 :419、r39-full :77/:294 = 8.2、full-review :66/:267 = 7.5 等）；
  - `papers/paper-null-ladder/R49-7.5-DELIVERY/provenance/paper-null-ladder-r49-independent-review-20261108.md:76` = 7.5；
  - `auto-paper/…/provenance/paper-null-ladder-r95-independent-review-20261111.md:419` = 6；
  - `auto-paper/…/success-condition-R121/isolated/governing_r95__paper-null-ladder-r95-independent-review-20261111.md:419` = 6。
- **mtime 晚于 r95（2026-11-11 15:01:39）的匹配文件 = 2 个**，两者数值行都是 `` `**Overall:** 6  | **Scholarly Confidence:** 4` ``，且**均与 r95 评审逐字节相同**（52,430 B / sha256 `c67f8cd3…02fb97a`）：
  1. `auto-paper/…/provenance/paper-null-ladder-r95-independent-review-20261111.md`，mtime `2026-11-11 22:56:02`，**BYTE-IDENTICAL = True**；
  2. `auto-paper/…/success-condition-R121/isolated/governing_r95__paper-null-ladder-r95-independent-review-20261111.md`，mtime `2026-11-14 10:24:40`，**BYTE-IDENTICAL = True**（位于 R121 的 `isolated/`，是 governing 评审的逐字节副本，非新撰写评分）。
- 另有 6 行**裸** `**Overall:**`（`figures_tables.md` 模板示例，无数值）与 1 行 `**Overall:** \`5.08/10\``（`ccfa-idea-review-reports/idea-review-occlufly-crg-20261107.md:71`，决策辅助分、反引号包裹、mtime `2026-11-07`，非行首数值口径、非论文评审分、且早于 r95）——均不计入上述 15。
- `ccfa-review-reports/` 内 10 份评审 mtime 全部 ≤ `2026-11-11 15:01:39`，R121 窗口内无任一被改动。

结论：**没有任何新撰写／新数值的 `**Overall:**` 评分行**；两份较新文件都是 r95 的逐字节副本。H 组结论：**MATCH**。

---

## I. 12 类点名夸大／自我认证逐条判定

依据：A–H 从原始字节重算所得状态 + 版本锁定件／门配置／账本的 mtime 与哈希 + 七轮既有审计的原文声明 +（最后读取的）R121 审计 §6 边界声明。逐条如下：

| 类 | 判定 | 一手证据 |
|:--|:--|:--|
| (a) R121 撰写或改动了已落盘的独立评审 | **REFUTED** | r95 仍 52,430 B / `c67f8cd3…` / mtime 11-11 15:01:39；`ccfa-review-reports/` 10 份 mtime 全部 ≤ r95；较新两份仅逐字节副本 |
| (b) R121 产出新的数值 `**Overall:**` 行 | **REFUTED** | H：15 行总量中 2 份较新文件与 r95 逐字节相同、数值同为 6；无新分值 |
| (c) R121 跑了前向 / 训练 / 推理 | **REFUTED** | R121 窗口（≥10:20）内项目新建文件仅 `success-condition-R121/` 自家产物；全部实验结果 JSON（含 `r39_visual_task/metrics.json` mtime 11-08）为既有；双门仍 `NOT_QUALIFIED`/`INCOMPLETE`；审计 §3 EXEC LOCK |
| (d) R121 把任一门晋级为 passed | **REFUTED** | G：`G0` 及 `G1–G8`/`validation`/`handoff` 全 pending；validator `NOT_QUALIFIED`、guard `INCOMPLETE`；`pipeline-state.json` sha 与 R120 所引一致、mtime 11-12 |
| (e) R121 改动了成功阈值 | **REFUTED** | validator 契约 `>= 7.0`（脚本 mtime 11-13 08:09:06）、guard ledger A6 `> 8.0`（mtime 11-13 08:09:20）均早于 R121；R107 的 `>=7.0` 与 ledger 旧 `>8.0` 双口径是既有已知项（R109 N-17） |
| (f) R121 改写了任何历史字节 | **REFUTED** | 版本锁 `main.tex` 两份 40,175 B / md5 未变；r95、pipeline-state、metrics、guard ledger、validator 哈希／mtime 均未变。R121 窗口内 3 个既有文件（goal-ledger.md / STATUS.md / memory）仅**纯追加**账本行：`goal-ledger.md` 前 687,472 B 与 10:24 副本逐字节相同、仅尾部 +9,574 B 的 R121 段，属 append 非改写 |
| (g) R121 声称任何科学结果 | **REFUTED** | 本轮为「否定性闭环」判定；0 篇达标、未写 COMPLETE；governing 仍 6.0；审计 §3/§6/§7 明确非科学结果 |
| (h) R121 声称 4090/L4/H20 能力 | **REFUTED** | 审计 §6:127「无 4090 / L4 / H20 能力主张」；`r39_visual_task/metrics.json` 的 `cuda_device: "NVIDIA GeForce RTX 4090"` 是既有实验的设备元数据（mtime 11-08），非 R121 能力主张 |
| (i) R121 自拟评审并称之为 governing | **REFUTED** | governing 明确仍为 r95（外部、11-11、未改）；七轮及本轮审计均声明「不改 governing」「非 `ccf-paper-reviewer full`」「未自评 governing」 |
| (j) R121 假定 ≤32h/K=45 confirmation 面板授权 | **REFUTED** | R114–R120 原文逐轮「未假定 `≤32h / K=45` confirmation 授权」；R121 审计 §5:116 把它列为**须 designated gate owner/用户裁决**的阻塞项、§6:127 明确未假定 |
| (k) R121 编造任何引用／数据集／结果／哈希 | **REFUTED** | 本人重算的 A–H 全部数值（r95 字节/哈希、版本锁 md5、metrics 值、门结论、Overall 计数、mtime）均与源字节吻合，未发现任何编造值。限制：按约束未读 `R121-VERIFICATION*.json`，故其内部「74/74」条数本人未核验；但审计中可对照的事实全部 MATCH |
| (l) R121 跳过了某道门 | **REFUTED** | 两道机器门本人均已实跑（validator `EXIT=1`、guard `EXIT=1`），G0 仍 pending，0 篇达标；审计 §7「不进稿件、不编译、不起 full 评审」 |

**CONFIRMED = 0，12/12 全 REFUTED。** 该结论由本人从原始字节独立得出，非假设。

---

## J. R121 round audit 瑕疵（在 A–I 结论形成后最后读取）

按约束，我在完成 A–I 全部结论后**最后**读取 `success-condition-R121/R121-ROUND-AUDIT.md`（9,443 B / sha256 `6ff55a5082ad335efc729b9063cf35dcef17d5f9f2ca01e0861b84f29ac16ab0` / mtime `2026-11-14 10:28:21`），用于对照与瑕疵分级。**声明：我确实按此顺序、在最后才读它。**

**总体对照：MATCH。** 审计 §4.1 的 9 行 needle（:419/:450/:448/:473/:240/:249/:413/:414/:454）、§4.2 三项 (a)(b)(c)、§4.3 七轮 7/7、§4.4 双门（validator `NOT_QUALIFIED / 6.0 / 7.0 / >=`、D1✓D2✗D3✗D4✓D5✗；guard `INCOMPLETE`、A2/A6 FAIL、S1–S7 全 7 pending）与 12 阶段门链，均与本人重算逐项一致；`Py 3.14.6` 实测吻合；`isolated/` 实测 21 个文件；R107 终值 `>= 7.0`（`GOAL-ITERATION-R107.md:22`）吻合。未发现任何**编造**或与源字节**数据不一致**。

逐项瑕疵／不精确／受限处（每条给出等级与是否改变核心结论）：

- **J-1（MEDIUM，不改变核心结论）**：审计 §1:17 与 §4.4:94 均写「全项目行首数值 `**Overall:**` **14 行**」。本人实测当前为 **15 行**（13 个文件）。14 是唤醒时点（10:03）的真值——那时 `success-condition-R121/isolated/governing_r95__…md`（10:24 生成）尚不存在；但 §4.4 标注「只读 live」且写于 10:28，此时应为 15。§4.4 同句又写「本轮 `isolated/` 自产副本 1 份（v2 已分列）」，即承认这第 15 行却仍报「全项目 … 14 行」，存在**时点混用 + 全项目口径未声明排除自产副本**的不精确（差 1）。这正是 R120 审计 self-check 记下的教训「写『全项目无 X』须先给扫描口径」。不影响其实质结论：两份较新文件都与 r95 逐字节相同、新 governing 候选 = 0、无新分值。
- **J-2（LOW，不改变核心结论）**：§4.2:72「另有 4 份 `SYNTHETIC_APPROXIMATION` … 受控图为 `True`」——4 这个**数量**正确，但严格说只有 2 份带 `data.source='SYNTHETIC_APPROXIMATION'`，另 2 份（`p3_p4_taskaware/metrics_from_trajectory.json` 两 run）**没有 `data.source` 字段**，是合成任务的 trajectory 镜像；把 4 份一律贴上 `SYNTHETIC_APPROXIMATION` 标签是标签口径的轻微外推。另有 1 个顶层 `hypothesis_supported` 文件（`r51_motif_survival/task_a_results.json`，`False`，无 source）未被列举，但值为 False，不影响「真实图全 False」判定。
- **J-3（LOW，不改变核心结论）**：§4.3:82「7/7 轮次全文均声明 `READONLY…`」。R120 的复合 token 实际是 `READ_ONLY_RECONCILIATION_…`（`READ_ONLY` 带下划线），字面不含 `READONLY`；7/7 的**语义**声明（只读 + NOT_GATE_PASS + NOT_SCIENTIFIC_RESULT）确实完整，属命名泛化的轻微不精确。
- **J-4（观察项 / 已披露，非缺陷，且反向佐证 (f)）**：§3:46「`isolated/` 21 份源字节逐字节副本」。本人复核：其中 20 份与当前源文件逐字节相同；仅 `goal_ledger__goal-ledger.md`（687,472 B @10:24）与当前 `goal-ledger.md`（697,046 B @10:34）不同——但当前文件**前 687,472 B 与之逐字节相同**，尾部仅**纯追加** +9,574 B 的 R121 账本段，属 append 而非改写。审计 §3:51-52 已明示「采集时刻四份结构权威 SHA … 为**采集时刻快照口径**，不覆盖采集后只追加记账造成的时间差（R119 M2）」，故这是**已披露的时点快照**，不是未察觉的缺陷，且恰好佐证「R121 未改写任何历史字节」。
- **J-5（范围限制，非审计缺陷）**：§3:45「`R121-VERIFICATION.json` = 74/74 MATCH / 0 MISMATCH」。按任务约束我不得把任何 R121 JSON 当数据源读取，故该内部条数本人**未独立核验**；我只能确认审计中可与源字节对照的 A–H 事实全部 MATCH。此为复核范围声明，不计为审计瑕疵。
- **J-6（LOW，不改变核心结论）**：第 4 行把 governing 概述为 `` `**Overall:** 6 | Scholarly Confidence 4` ``，相对 :419 逐字（双空格 + `**Scholarly Confidence:**` 粗体）是**改写式摘要**而非逐字引用；§4.1:60 已给出正确逐字形式，属表述层面的轻微不精确。

补充澄清：审计 §5 的「否定性闭环」结论（R114–R120 这类只读审计按 r95 自身 :450 规则结构上不可能把 6.0 抬到 >= 7.0）由 r95 原文 + (a)(b)(c) 全 False + 七轮只读自述支撑，且明确限定为「这类只读审计」并指出唯一 admissible 路径仍是 P3 真实前向后的全新隔离 full 评审，**未发现 overclaim**；`r39_visual_task/metrics.json` 中的 RTX 4090 仅为既有实验设备字段，不构成 (h) 的能力主张。§6 边界逐条与 I 组 12 类 REFUTED 一致。

**J 汇总：HIGH = 0，MEDIUM = 1（J-1），LOW = 3（J-2/J-3/J-6），另有 1 项已披露的时点快照观察（J-4）与 1 项复核范围限制（J-5）。全部不改变核心结论。**

---

## 结论

A–H 十组事实全部由原始源字节独立复现（**MATCH**）；I 组 12 类点名夸大 **CONFIRMED = 0 / 全 REFUTED**；J 组在最后读取的 R121 轮次审计中仅发现若干不精确／时点口径问题（无 HIGH、无编造、无数据不一致），均不改变核心结论。governing 仍为 r95 = 6.0 / Confidence 4.0；双门 `NOT_QUALIFIED` / `INCOMPLETE`；G0 pending 且 inputs/evidence 为空；(a)(b)(c) 三项升分条件全部未满足；无新数值评分行、无门晋级、无科学结果、无前向传播。核心结论可复现，轮次审计存在轻微瑕疵。

**Verdict:** REPRODUCIBLE_WITH_DEFECTS | **G0 may be passed:** NO | **Scientific result claimed:** NO | **Forward pass performed:** NO

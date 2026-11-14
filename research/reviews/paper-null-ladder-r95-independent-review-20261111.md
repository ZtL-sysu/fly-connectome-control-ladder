# CVPR 2027 · Full 模式独立评审报告（与作者完全无关的 CCF-A 审稿人 / 领域主席）

> 本报告由一名**与论文作者无关、看不到稿件产生过程**的独立 CCF-A 审稿人 / AC 撰写。评审输入**仅限磁盘文件**。历史评审链（`ccfa-review-reports/`）仅用于理解「关切如何演化」，其中出现的任何分数都**未被抄用、平均或当作锚点**；本 brief 中出现的任何数字（含目录名 `R49-7.5-DELIVERY`、行数、字节数）也**未被当作分数锚点**。总分完全依据科学价值与逐项核验的证据独立推演。

---

## 0. 报告元数据与独立性声明

| 项 | 值 |
|---|---|
| Review date | 2026-11-11 |
| Target venue/year/track | CVPR 2027 主会（double blind），评估方法学 / 诊断标准类投稿 |
| Paper title | *A Structure-Sensitive Null Ladder Exposes a Blind Spot in Connectome-Control Protocols* |
| Reviewer mode | `full` = scientific + writing + format + revision-action synthesis |
| 被评稿件 | `papers/paper-null-ladder/R49-7.5-DELIVERY/manuscript/main.tex` 与 `main.pdf`（`paper.tex`/`paper.pdf` 为逐字节一致副本） |
| Report file | `ccfa-review-reports/paper-null-ladder-r95-independent-review-20261111.md`（唯一输出） |
| 独立性 | 与作者无关系；不采信任何自评结论替代独立核验；不修改任何稿件/指标/审计/账本/校验器文件 |

**打分前已先读完的技能规范（如实记录）**：

| # | 规范文件 | 状态 |
|---|---|---|
| 1 | `~/.claude/skills/ccf-paper-reviewer/SKILL.md` | 已读 |
| 2 | `.../references/calibration-and-rank.md` | 已读 |
| 3 | `.../references/universal-review-rubric.md` | 已读 |
| 4 | `.../references/desk-checks.md` | 已读 |
| 5 | `.../references/reviewer-panel.md` | 已读 |
| 6 | `references/review-output-standards.md`（brief 指定路径） | **不存在**；实际文件在 `~/.claude/skills/ccf-common/references/review-output-standards.md`，已读，不中断 |
| 7 | `.../references/fixed-output-format.md`（补充） | 已读 |
| 8 | `.../references/review-workflow.md`（补充） | 已读 |
| 9 | `.../references/venue-review-styles.md`（补充） | 已读 |
| 10 | `~/.claude/skills/ccf-paper-writer/references/venue-guides/cvpr.md` | 已读；**为 CVPR 2026 legacy 迁移指南**（标注"official policy must be rechecked"），**非 2027 专属**；输入仅限磁盘，未联网复核 2027 官方页，已在 Confidence / Unresolved 标注 |

---

## 1. 被评审版本锁定（Version Lock）

启动前实测，与 brief 自报指纹**逐项一致**：

| 项 | 实测值 | brief 自报 | 一致 |
|---|---|---|---|
| `main.tex` 行数 | 716 | 716 | ✓ |
| `main.tex` 字节数 | 40,175 B | 40,175 B | ✓ |
| `main.tex` md5 | `e4bfad51ad834fdccdb6db7821e158c6` | 同 | ✓ |
| `main.pdf` 页数 | 9（`mdls` + PDF 解压流 `/Type /Page` 计数 = 9，`/Count 9`） | 9 | ✓ |
| `paper.tex` vs `main.tex` | `cmp` 逐字节一致 | 逐字节一致 | ✓ |
| `paper.pdf` vs `main.pdf` | `cmp` 逐字节一致 | 逐字节一致 | ✓ |

**说明**：`ccfa-review-reports/` 内 9 份历史报告锁定的版本各不相同（r49 = 40,897 B / `9cdb5ea6…`、r93 = 42,454 B / `0a3a4da4…`、final-submission-audit 记录 = `f0e760db…` 等），**均与本版不同**；本评审针对本版独立判定，不沿用任何历史结论。

### 实际读过的证据文件清单（可复核）

| 类别 | 数量 | 文件 |
|---|---|---|
| A 技能规范 | 10 | 见 §0 表（含不存在的 `review-output-standards.md` 之替代路径说明、CVPR 2026 迁移指南） |
| B 稿件/生成表格/题录/PDF | 9 | `main.tex`、`preamble.tex`、`main.bib`、`main.bbl`、`tables.tex`、`tables_taskaware.tex`、`tables_heldout.tex`、`tables_boundary.tex`、`main.pdf`（对象/页数解析） |
| C 8 组实验证据 JSON（结构化 `json.load`） | 11 | `p3_p4/metrics.json`、`p3_p4/metrics_completed.json`、`p3_p4_taskaware/metrics.json`、`p3_p4_taskaware/metrics_from_trajectory.json`、`r39_heldout/metrics.json`、`r39_density_sweep/metrics.json`、`r39_real_connectome/metrics.json`、`r39_real_connectome_v2/metrics.json`、`r39_real_connectome_v2/metrics_from_trajectory.json`、`r39_visual_task/metrics.json`、`p2_gate/.../p2_gate/metrics.json` |
| D 执行脚本 SHA-256 重算（`shasum -a 256`） | 31 | `scripts/` 顶层 11 个 `.py` + 各 `results/` 组内执行副本 + `r91/r93-candidate` 表格脚本（全量遍历） |
| E 过程/审计记录（逐字读） | 5 | `declaration-change-record.md`、`integrity-audit.md`、`final-submission-audit.md`、`clean-copy-audit.md`、`concern-to-action-ledger.md` |
| F 历史评审链（仅关切演化扫描；分数未用） | 9 | `ccfa-review-reports/*.md`（9 份；r49 前 60 行逐字读，其余标题/关键词 grep） |
| G 旧版编译日志（仅作旁证） | 1 | `run/paper/main.log`（不同版本，非被评版编译产物） |

**合计访问/读取/解析/哈希文件：76 个**；其中逐字读取或结构化解析内容的核心证据文件 36 个，脚本哈希重算 31 个，历史链扫描 9 个。
图像 `figures/`（4 个文件）核了**存在性与 `\ref` 引用**，未逐图查看像素内容；`ieeenat_fullname.bst` 在输入范围内但未逐字读（不依赖其内容即可完成题录核验）。`paper/sources/` 快照目录**在磁盘不存在**（brief 列为输入范围，如实记录）；`R49-7.5-DELIVERY/manuscript/` 内**无 `.log/.aux/.blg`** 编译产物。

---

## 2. Checks run 清单

| ID | 检查 | 方法 | 结果 |
|---|---|---|---|
| C-01 | 版本锁定 | `wc -l/-c` / `md5` / `cmp` / PDF 对象解析 | 通过（§1） |
| C-02 | headline 数字逐项对账 | 论文所有 headline 数字 → 8 组 `metrics.json` + 4 张生成表（round-4dp 精确/衍生匹配） | ~90 个数字全部溯源，无矛盾（§5） |
| C-03 | 执行脚本 SHA-256 重算 | `shasum -a 256` 全 31 个 `.py` vs 论文自报值 + JSON 自报 `script_sha256` | **5/5 精确匹配**（§5.2） |
| C-04 | 引用完整性 | `main.tex`+`tables*.tex` 的 `\cite` keys vs `main.bbl` 的 `\bibitem` | 15 = 15，0 undefined / 0 uncited，`thebibliography{15}` |
| C-05 | CVPR 合规 | 9 页结构 / `\clearpage` / 双盲 / 题录外链 / 隐藏指令 / 编译告警可核验性 | 见 §6（1 个行政 blocker + 若干不可直接核验项） |
| C-06 | 隐藏指令/注入扫描 | 正则扫描 `ignore/as an AI/accept this paper/score` 等 | 0 命中 |
| C-07 | 正文工程制品扫描 | `.py/.md/.json/scripts/results/networkx/sandbox/P2 gate` 等 | 0 命中；但 `main.bib` 残留 1 条不完整 provenance 注释（§6） |
| C-08 | 双盲 | `\author{Anonymous}`、`\def\paperID{*****}`、无致谢/自识别链接 | 通过 |
| C-09 | 负结果/披露处理 | 核对是否因诚实披露或自我限定主张被额外扣分 | 未扣分；扣分仅来自证据性事实（§8、§10、§11 声明） |

---

## 3. Desk Rejection Assessment

```
Check: Paper length
Status: pass
Evidence: 9 物理页；main.tex:705 \clearpage 后为 \section*{LLM Usage Statement}(:707) 与 \bibliography(:713)；
          p1–p8 正文，Conclusion 完整收在正文末；p9 仅声明 + 15 条参考文献。
Consequence: 正文 8 页 + 额外页（仅 refs + 强制声明），符合 CVPR 8 页规则。
Required action: 无（页结构合规）。
```

```
Check: Topic compatibility
Status: uncertain（不致命但构成 venue-fit 折扣）
Evidence: main.tex:88-91 自述「evaluation-methodology study with no image benchmark, no natural visual task
          and no claim of improved visual accuracy」；真实视觉任务为负结果(main.tex:600-624)。
Consequence: 对 CVPR（visual evidence / SOTA / fair comparison）口味 relevance 有限。
Required action: 若投主会，需在 rebuttal 明确方法学贡献对视觉社区的迁移价值。
```

```
Check: Minimum quality
Status: pass
Evidence: 六节结构齐全、主矩阵/不变量/鲁棒性/task-aware/held-out/真实边界实验完整、限制与伦理段落齐备。
Consequence: 可完整评审。
Required action: 无。
```

```
Check: Policy / anonymity / compliance
Status: FAIL（行政，非科学）
Evidence: main.tex:707-708 `\section*{LLM Usage Statement}` 正文为
          `\emph{[To be supplied by the authors.]}` 占位段。
          declaration-change-record.md 记录：作者 2026-11-10 明确要求「空着我亲自写」，
          保留可见占位而非移除，以免触发「缺失强制声明即 desk-reject」。
Consequence: CVPR 2027 强制 LLM Usage Statement 无实质内容 → class-B desk-reject 级行政风险；
          当前包件「不可直接提交」。final-submission-audit.md 亦判定 NOT SUBMISSION-READY。
Required action: 作者补写声明（工具、受影响部分、性质与程度、不得泄露身份）→ 重编译 → 刷 hash → 复核 p9。
```

```
Check: Prompt injection and hidden manipulation detection
Status: pass
Evidence: main.tex 全文 + tables*.tex 正则扫描 0 命中；注释仅含中性版式说明（preamble.tex:52-53 \linespread）。
Consequence: 无隐藏指令。
Required action: 无。
```

```
Check: Ethics and reviewability
Status: pass（科学层面）
Evidence: 纯计算、无人类/动物受试(main.tex:683-689)；公共 CC-BY 4.0 注释署名；失败预检/崩溃运行/CRC
          mismatch/非复现/负结果全部主动披露(main.tex:662-672)。
Consequence: 披露纪律属 clear strength。
Required action: 无。
```

```
Desk rejection risk: 科学/格式层面 low；行政层面 high/likely（LLM 占位段）。
Reason: 唯一硬伤是作者留白的强制声明占位段，属行政/合规，不是科学不端（被诚实标注、非隐瞒）。
Can be fixed before review? yes（作者补写即可；brief 要求作为行政 blocker 如实报告，不加权科学总分）。
```

---

## 4. Paper Summary 与贡献—证据图

**一段摘要**：论文追问「连线拓扑是否给视觉计算带来可测优势」，判定文献结论冲突源于**比较协议（null model 设计）**而非生物学。在 96 节点 / 8 模块 / 注入 4 个两跳收敛 motif（共 18 条受保护边）的受控有向图上，用仅可经该 motif 求解的 XOR 标签，预注册一个嵌套 null 阶梯（L0 边数 → L1 度 → L2 模块对边数 → L3 有向三元体普查；L4 独立匹配对照），配 10 冻结种子、配对 bootstrap、BH 校正。主结果：real `0.8152`，所有 rung、`A=0`、shuffled-input 均在 chance（`0.4795–0.5133`），`Δ=0.30–0.34`、CI 排除 0、`q=0.0002`；但四个 rung 仅相差 `0.0244`、单调性反转 → 阶梯**无定位能力**，返回第三种结果「null 家族本身是混杂」。机制由 Eq.(1)（`main.tex:255-279`，主动限定为非均匀交换下的上界直觉）、task-aware null（`0.8346` vs `0.8371`, `q=0.40`）与 motif 剂量阶梯（18/14/9/4/0 → `0.8371/0.8316/0.4988/0.5104/0.5117`）闭合。边界实验：20 图 powered held-out（8/12 BH 显著、幅度 MAE `0.1046` vs `0.1635`、sign `0.60` = majority baseline）；真实 MaleCNS 稠密子图全 chance；稀疏化 5 变量同改后 real `0.6423` 但 `hypothesis_supported=false`；单变量密度 sweep 隔离 in-degree 为 gate 决定因素；真实图像任务为负结果（非图 MLP `0.9722` 主导）。结论把贡献定位为「控制充分性」的诊断标准，并明确不主张视觉精度提升、不主张机制普适。

| 维度 | 内容 |
|---|---|
| Claimed problem | 连接组约束模型「拓扑是否有优势」的文献结论相互矛盾 |
| Claimed gap | 缺一个把「控制生成器本身」当实验变量的受控比较；任务是否结构敏感未被检验 |
| Method/contribution map | (1) 可复用 null 生成器标准（4 rung + 匹配对照 + 机器校验不变量 + 结构敏感门禁）；(2) 经验裁决：匹配全局统计不保护任务相关 motif；(3) 20 图 powered 正负结果；真实图与视觉任务作为 scope 边界 |
| Evidence package | 主矩阵 10 seeds、invariants、robustness 4 格、task-aware/dose 10 seeds、20 图 held-out、dense/sparse 真实图、单变量密度 sweep、digits/MNIST 视觉任务；4 图 8 表；8 组 `metrics.json` |
| Stated limitations | 合成近似、强基线未复跑、仅有/无符号预测、FAILED 预检与崩溃运行、真实图为边界而非复现、真实视觉任务负结果、跨运行 ID 不可池化 |

---

## 5. 主张—证据对账（Claim–Evidence Reconciliation）

### 5.1 头条数字逐项交叉核对（论文 → `metrics.json` / 生成表）

| 论文 headline 数字（Where stated） | 证据字段（可引用依据） | 判定 |
|---|---|---|
| real `0.8152`；A0 `0.4879`；L0 `0.4795`；L1 `0.5039`；L2 `0.4961`；L3 `0.4986`；L4 `0.5016`；motif-only `0.8348`；shuffled `0.5133`（`tables.tex:6-14`, `main.tex:372-380`） | `p3_p4/metrics.json::/main_matrix/mean_acc/*`（`0.815234375`,`0.487890625`,`0.4794921875`,`0.50390625`,`0.49609375`,`0.4986328125`,`0.5015625`,`0.834765625`,`0.51328125`） | ✓ 全表一致 |
| `Δ` `0.3273/0.3357/0.3113/0.3191/0.3166/0.3137/-0.0195/0.3020`，CI 如 `[0.3043,0.3463]`，BH `q=0.0002`（`tables.tex:7-14`） | `p3_p4/metrics.json::/main_matrix/real_minus_condition/*/{mean_delta,bootstrap_ci/ci95_lo,ci95_hi,bh_q}`；8 条件 `bh_q=0.00019996≈0.0002`，`bh_correction_family` 8 项 | ✓ 一致（BH 家族正确） |
| rung 间仅差 `0.0244`（`main.tex:38,383`） | 衍生：`max(0.3357,0.3191,0.3166,0.3113)−min = 0.3357421875−0.311328125 = 0.0244140625` | ✓ 可复算 |
| 单调性反转、two-path 偏差 `24.875/0.125/5.938/0.500`（`main.tex:412`） | `p3_p4/metrics.json::/null_ladder/monotonicity_L0_to_L3/{abs_mean_delta=[24.875,0.125,5.9375,0.5],inversion_count=1}`；`conv2_stat=178` | ✓（`5.938`=5.9375 四舍五入） |
| invariants：L3 三元体 L1 `20` vs L2 `1826`；L4 `28/93/39`（`tables.tex:20-24`） | `p3_p4/metrics.json::/null_ladder/*/invariant_violations_max/*`（L0 484/L1 756/L2 1826/L3 20/L4 4836；degree 95/0/0/0/93；blocks 53/47/0/0/39；edges L4=28） | ✓ 全表一致 |
| robustness `0.3652/0.3561/0.1406/0.2064`（`tables.tex:30-31`） | `p3_p4/metrics.json::/robustness/*/delta_real_minus_ref`（4 格全保留，含最弱格） | ✓ 一致（无择优） |
| gate FAILED：oracle `0.7891`、mean_real `0.8092`、CI lo `0.2988`、`p=0.0002`、clean-motif `0.8470`、leakage `0.4902/0.5000`；600ep `0.7930`、clean 2-ch `0.9232`、ceiling `0.9395`（`main.tex:328-337`） | `p3_p4/metrics.json::/p2_gate_corrected/*` 与 `metrics_completed.json::/p2_gate_corrected/oracle_recheck/*`（`verdict=FAILED` 保留） | ✓ 全字段一致 |
| task-aware `0.8346` vs real `0.8371`、`Δ=0.0025`、CI `[-0.0025,0.0084]`、`q=0.40`；strong `0.4920`、motif-removed `0.5117`、dose `0.8371/0.8316/0.4988/0.5104/0.5117`（`tables_taskaware.tex`, `main.tex:483-491`） | `p3_p4_taskaware/metrics.json::/mean_acc/*`、`/real_minus_condition/*`（`bh_q=0.40132`、`0.00032`）、`/dose_response/mean_acc=[0.8371,0.8316,0.4988,0.5104,0.5117]`、`/data/protected_motif_edges=18` | ✓ 一致；与 `metrics_from_trajectory.json` 逐字段相同 |
| held-out：20 图、12/8 符号、`-0.046~0.372`、8/12 显著、MAE `0.1046` vs `0.1635`（36%）、sign `0.60`=majority（`tables_heldout.tex:16-23`, `main.tex:435-449`） | `r39_heldout/metrics.json::/heldout_rows`（20 行，min `-0.0462`、max `0.3717`）、`/delta_sign_counts={12,8}`、`/significant_features_after_bh`（8 个）、`/logo/{magnitude_mae=0.10462,constant_baseline_mae=0.16355,sign_agreement=0.6,majority_baseline=0.6}`；36% = (0.1635−0.1046)/0.1635 | ✓ 一致；8 特征名称与 `main.tex:443-445` 一一对应 |
| dense：5 条件全 chance；sparse real `0.6423` vs A0 `0.5283`（`Δ=0.1139`）、motif-removed `0.5160`（`0.1263`）、deg-null `0.6162`（`0.0260`, CI 含 0）、task-aware `0.5850`（`0.0573`）（`tables_heldout.tex:5-10`, `main.tex:521-559`） | `r39_real_connectome/metrics.json`（4 CI 全含 0）、`r39_real_connectome_v2/metrics.json::/real_minus_condition/*`（CI 逐项匹配）；两组 `hypothesis_supported=false` | ✓ 一致（不作 replication claim 有据） |
| density sweep：`44,815` 边、in-deg `58.35`、`29,442` IDs、oracle `1.0000`、real `0.5049/0.4886/0.5075/0.6227/0.9863/0.9987`、task-aware `0.9027/0.9971`（`tables_boundary.tex:5-13`, `main.tex:573-598`） | `r39_density_sweep/metrics.json::/data/dense/{n_edges=44815,mean_indeg=58.3529}`、`/data/n_visual_body_ids=29442`、`/oracle_dense/mean_acc=1.0`、`/density_sweep/{63,16,8,4,2}/real/mean_acc` 与 `task_aware_null`、`/density_isolated=true` | ✓ 一致（`58.35`=58.3529） |
| visual：real `0.7185`、deg-null `0.7190`（`Δ=-0.0005`）、A0 `0.6190`（`+0.0995`）、MLP `0.9722`；MNIST `0.8879 vs 0.7649`、real−deg-null `+0.0148` CI `[0.0100,0.0192]`（`tables_boundary.tex:19-24`, `main.tex:610-624`） | `r39_visual_task/metrics.json::/{mean_acc,real_minus_condition,mlp_baseline,mnist_addon}`；`mnist_addon.real_minus_condition.degree_preserving_null.ci95=[0.0100,0.0192]` | ✓ 一致（双向 delta 均报，无择优） |
| provenance：`9,766/29,442/29,564` IDs、`48,713/48,723/3,072/3,062` 边、768 节点、151 s wall time | `r39_real_connectome/metrics.json::/data/n_edges=48713`；`v2::/data/dense_graph/n_edges=48723`、`/data/n_edges=3062`；`r39_visual_task/graph_stats.json::/n_visual_body_ids=29564`；`p3_p4/metrics_completed.json::/runtime_sec_from_log=151.0` | ✓ 一致 |

**结论**：约 90 个 headline 数字**全部**精确匹配或为四舍五入/衍生值，**无一处矛盾、无一处无法溯源**。这是本次评审中最强的正面证据。

### 5.2 执行脚本 SHA-256 重算（自报值 / JSON 自报 / 磁盘实算三方比较）

| 论文可复现性声明（`main.tex:678-680`） | JSON 自报 `script_sha256` | 磁盘执行副本实算 `shasum -a 256` | 判定 |
|---|---|---|---|
| dense `090d9535…` | `090d9535ac49cc50…` | `results/r39_real_connectome/r39_real_connectome.py` = `090d9535ac49cc50f1993e7091e126b13d07216595df93f982de715137d64693` | ✓ 精确匹配 |
| sparse `026bf88e…` | `026bf88e11d3056…`（metrics + trajectory 两份） | `results/r39_real_connectome_v2/r39_real_connectome_v2.py` = `026bf88e11d3056e70abb35f36efee46782b463f983b0e5e73a4f4ecafd3f6fa` | ✓ 精确匹配 |
| sweep `360a3808…` | `360a3808bb4a86e…` | `results/r39_density_sweep/r44_density_sweep.py` = `360a3808bb4a86eee17e162b58d45565c7302c97ac35129178ff844717c8f795` | ✓ 精确匹配 |
| visual task `28f5744d…` | `28f5744d3e3d33…`（config + metrics 两份） | `results/r39_visual_task/r39_visual_task.py` = `28f5744d3e3d3376aea4458555e8801013bde607615435059fd246208c8097b7` | ✓ 精确匹配 |
| §4.6「executed script reports its own SHA-256, verified against the pulled file」 | `764bbdc6e4b23ea…`（heldout metrics） | `results/r39_heldout/r39_heldout_slim.py` = `764bbdc6e4b23ea66f19ff6501a1b09e33f11aa88622b75410f5811542f00a48` | ✓ 精确匹配 |

**注意（如实记录）**：`scripts/` 顶层同名脚本哈希与 `results/` 组内「执行副本」不同（例：`scripts/r39_real_connectome.py` = `a1c4555a…`），论文引用的是各 result 组内被拉取/未损坏的执行副本，与「pulled, uncorrupted script」表述一致。`p3_p4/evidence_repair` 与 `metrics_completed.json::/evidence_repair/logo_recompute` 如实记录了早期聚合块 `NameError 'logo_pred'` 崩溃、LOGO 值从已持久化行重算、以及「executed script does not match the recorded checksum」——与 `main.tex:662-666` 的披露吻合。`p3_p4_taskaware/metrics_from_trajectory.json::/provenance` 还披露该组因沙箱工作区不可达（`novix debug pull` 返回 no session），数值系从 agent 打印 summary 转录（含一个 value-identical 的 `NameError` 修复）；`metrics.json` 与转录版逐字段一致，构成双份互证。以上均为**已披露的过程事实**，不作为造假或额外扣分依据。

---

## 6. CVPR 2027 合规核验（独立复核，不采信 `submission-constraints.md` 等自评）

| 检查 | 独立结果 | 证据 |
|---|---|---|
| 正文 8 页 + 额外页仅 refs + 强制声明 | **PASS** | 9 页；`main.tex:705 \clearpage`、`:707` LLM Statement、`:712-713` bibliography；p8 以完整 Conclusion 收尾，p9 为声明 + 15 条 refs |
| 双盲 | **PASS** | `main.tex:11 \def\paperID{*****}`、`:17 \author{Anonymous}`；无致谢/身份链接 |
| 题录无外链 | **PASS** | `main.bib` 0 个 `url`/`https`、0 个 `note` 字段；`main.bbl` 仅含 `bst` 生成的 `\url` 宏定义，无实际 URL；3 个 DOI 字段 |
| 0 undefined references | **PASS（结构层）** | 15 `\cite` key = 15 `\bibitem`，0 undefined / 0 uncited，`thebibliography{15}`；旧版 `run/paper/main.log` 亦 0 undefined |
| 0 overfull boxes | **UNCERTAIN（不可直接核验）** | 被评 `R49-7.5-DELIVERY/manuscript/` **无 `.log/.aux/.blg` 编译产物**；旧版 `run/paper/main.log`（不同版本）显示 0 overfull / 9 页，仅作旁证；版式用 `\linespread{0.98}`（`preamble.tex:53`）压缩，存在潜在 overfull 风险但未获被评版本日志证实 |
| 强制 LLM Usage Statement | **FAIL / 行政 BLOCKER** | `main.tex:707-708` 为 `\emph{[To be supplied by the authors.]}` 占位段（作者留白，见 §3） |
| 隐藏指令 / prompt injection | **PASS** | 全文 0 命中 |
| 工程制品残留 | **PASS（正文）/ minor（题录）** | 正文与 `tables*.tex` 0 命中；但 `main.bib:2-4` 残留一条**不完整 provenance 注释**（`% ... verification-report.md / prior-art-opportunity-map.md and were not`），引用内部文件名且句子截断——与 `clean-copy-audit.md`「0 leftovers」自评略有出入，属 minor 整洁性问题 |
| `paper/sources/` 快照 | **NOT AVAILABLE** | brief 列为输入范围，但磁盘上该目录不存在；`final-submission-audit.md` 提到「original preserved in sources/」无法对本版复核 |

**合规结论**：科学格式层面几乎全通过；**一处行政硬伤**（LLM 占位段）使当前包件不可直接提交，**一处不可直接核验项**（0 overfull 缺被评版编译日志）。按 brief，行政 blocker 如实报告、不作为压低科学维度分的杠杆；它影响 desk verdict 与 Recommendation。

**题录真实性未核验（如实记录）**：`main.bib` 含 5 条 2026 年 arXiv 预印本（`arXiv:2610.10023`、`2604.04033`、`2610.13018`、`2602.17997`、`2610.29205`）、`Cell 189(18)`（2026）及 `doi 10.1016/j.cell.2026.08.015`。输入范围仅限磁盘、未联网，**无法核验其真实性**；`SKILL.md` 要求「Do not invent citations」，本报告**不臆断伪造**，仅将「closest prior work `toposens2026` 等无法由磁盘证据独立确认」记为 Novelty/Positioning 的 Confidence 折扣与 Unresolved 项。

---

## 7. Strengths（证据支撑）

- **证据可核验性极强**：约 90 个 headline 数字逐字段溯源到 8 组 `metrics.json` 与 4 张生成表，5 个执行脚本 SHA-256 自报值与磁盘实算精确匹配（§5）。这在投稿中属罕见的可审计度。
- **统计协议严谨**：10 冻结种子、配对 seed-level bootstrap（5000 resamples）、BH 校正 8 条件家族、LOGO 折内重选特征、constant/majority 显式基线；robustness 四格全保留（含最弱格），双份独立来源的 task-aware/v2 结果互证。
- **机制环闭合且逻辑自洽**：Eq.(1) 主动限定为「上界直觉，非精确逐 rung 概率」，task-aware null 与 motif 剂量阶梯（18→0 边的离散崩塌）从正反两面验证「保护任务相关子图」才是控制充分性判据。
- **诚实与范围纪律**：FAILED 预检、崩溃运行/CRC mismatch、非复现（`hypothesis_supported=false`）、负视觉结果、MNIST 反向 delta、五变量混淆、跨运行 ID 不可池化——全部主动披露并写进 Limitations；不因披露而虚增主张。
- **可复用的方法学产物**：嵌套 null 生成器标准 + 机器校验不变量 + 结构敏感门禁 + 生存计数建议，对「topology helps」类声称有实际审计价值。

---

## 8. Major / Fatal Concerns（证据支撑）

```
Weakness M1（证据性·决定性）: 中心机制（motif 生存为「控制充分性」的因果判据）仅在 96 节点合成 XOR 诊断图上确立，
真实数据上未复现。
Evidence basis: r39_real_connectome_v2/metrics.json::/hypothesis_supported=false；度保持 null 保留优势
  (0.6162, Δ=0.0260, CI [-0.0348,0.0921] 含 0)；r39_density_sweep/metrics.json::/density_isolated 仅确立
  「密度边界」，main.tex:589-594 自述「does not establish motif survival as the causal variable」；
  main.tex:698-700 Conclusion「threshold was not reproduced... measured predictor in one regime, not a universal cause」。
Reviewer deduction: 论文最漂亮的 headline「null 家族本身是混杂」在受控图成立，但真实图上 null 行为依赖目标图
  密度/高阶组织（度保持 null 反而保留效应），该 framing 的普适性被作者自己的实验削弱。
Required fix: 需新的真实图实验确认机制迁移（非 prose 可修），见 §13 No quick change。
```

```
Weakness M2（证据性·venue-fit）: 零视觉证据、真实视觉任务为负结果，对 CVPR 主会 significance 有限。
Evidence basis: main.tex:88-91「no image benchmark, no natural visual task and no claim of improved visual accuracy」；
  r39_visual_task/metrics.json：非图 MLP 0.9722 主导所有图模型，degree-preserving null 0.7190 ≈ real 0.7185
  (Δ=-0.0005)，MNIST 0.8879 vs 0.7649；main.tex:614「negative result」。
Reviewer deduction: CVPR 口味要求 visual evidence / SOTA / fair comparison；本稿贡献是评估方法学，受众 relevance 受限。
Required fix: 若投主会，需在 rebuttal 论证方法学标准对视觉实证研究的直接迁移价值；无法靠 prose 补出视觉贡献。
```

```
Weakness M3（证据性）: 最强已发表基线未复跑，framing「协议解释文献冲突」缺最直接对证。
Evidence basis: main.tex:637「We did not rerun their flyvis stack and make no benchmark-reproduction claim」；
  main.tex:657-659 Limitations「flyvis and the published shared-initialisation pipeline were not rerun; L1 implements
  the degree-preserving idea only」；related-work 仅叙述 toposens2026 / structurealone2026。
Reviewer deduction: 论文解释的是他人 pipeline 上的冲突，却未在该 pipeline 上验证自己的协议，外推链条不完整。
Required fix: 在 flyvis / toposens2026 栈上跑一次同协议比较，或明确收窄为「受控图内部的方法学结论」。
```

```
Weakness M4（证据性·统计价值）: held-out 预测价值受限——8 个 BH 显著特征部分编码 intact/degraded 操纵本身，
符号预测零技能。
Evidence basis: r39_heldout/metrics.json::/significant_features_after_bh（reach_a 0.869、d_reach_ab 0.850、
  motif_fraction 0.753、motif_edges_kept 0.725，主要分离 10 intact/10 degraded）；/logo/sign_agreement=0.60
  = /majority_baseline=0.60；main.tex:454-460 自述「validate the manipulation rather than discover an independent
  graph law」「claim only a corrected association」。
Reviewer deduction: 主张已正确降格为 magnitude association，但 predictive power 的独立性未建立。
Required fix: 在「非操纵」的独立图族上验证特征预测力。
```

```
Fatal concern: 无（科学层面）。central contribution 清晰、主矩阵证据强且可复算、可复现、诚实，无致命技术/伦理/证据缺陷。
行政 blocker（单独）: LLM Usage Statement 占位段（§3、§6）——使当前包件不可直接提交，但不构成科学致命缺陷。
```

---

## 9. 7 人独立 Reviewer Panel（综合前各自独立给分/倾向）

> 7 名审稿人在 AC 综合**之前**各自独立判定，互不污染；分数为模拟审稿人独立倾向，不等于最终总分。

```
Reviewer: R1 Best-Justified Reviewer
Expertise: 评估方法学 / benchmark 诊断
Likely score: 7 (weak accept 下沿)
Confidence: 4
Main positive signal: 把 null 生成器当实验变量 + 机器校验不变量是干净、可复用的贡献；主矩阵 10 seeds/CI/BH、
  task-aware 与剂量阶梯闭合机制环；5 个脚本 SHA 可实算；诚实度罕见。
Main negative signal: 范围窄，正向机制仅合成替身。
Evidence basis: §5 全表对账、§5.2 SHA、tables.tex / tables_taskaware.tex
Fatal concern if any: 无
Score-change condition: 一条真实图上确认机制迁移的独立结果 → 8
```

```
Reviewer: R2 Critical Reviewer
Expertise: CVPR 视觉实证 / venue-fit
Likely score: 4 (lean reject)
Confidence: 4
Main positive signal: 无致命技术错误，统计规范。
Main negative signal: 无图像 benchmark / SOTA / 自然视觉任务正结果；真实视觉任务负结果、非图 MLP 主导；
  main.tex:88-91 自述「no image benchmark」；对 CVPR 视觉受众 relevance 有限；机制真实图未复现。
Evidence basis: r39_visual_task/metrics.json、main.tex:600-624、r39_real_connectome_v2::/hypothesis_supported=false
Fatal concern if any: venue mismatch（可辩，非技术致命）
Score-change condition: 需至少一项真实视觉任务的机制确认 + 强基线复跑，方脱离 reject 区
```

```
Reviewer: R3 Method / Soundness Reviewer
Expertise: 图学习 / 因果与统计
Likely score: 6
Confidence: 5
Main positive signal: A^T in-neighbour 方向缺陷被诊断并修正(main.tex:205-209)；Eq.(1) 主动限定上界直觉；
  10-seed 配对 bootstrap + BH；LOGO 折内选择；dense 失败由 §density 的 oracle(1.0000) 单变量 sweep 补上正对照。
Main negative signal: 3-seed 预检 verdict=FAILED 保留（虽诊断为 probe defect）；早期 18017 末块崩溃/CRC mismatch/
  LOGO 重算；sparse follow-up 五变量同改（已诚实声明不能隔离密度，且后续单变量 sweep 已补）。
Evidence basis: p3_p4/metrics.json::/p2_gate_corrected、metrics_completed.json::/evidence_repair、main.tex:271-279
Fatal concern if any: 无
Score-change condition: 一条哈希可核验、pre-check 通过的端到端主实验重跑 → 7
```

```
Reviewer: R4 Evidence / Experiment Reviewer
Expertise: 实验设计 / 多重比较
Likely score: 5
Confidence: 5
Main positive signal: 受控图证据包完整（主矩阵/不变量/鲁棒性 4 格/dose/20 图 held-out），无 cherry-pick，
  负结果与最弱格全保留。
Main negative signal: 真实图 `hypothesis_supported=false`、度保持 null 反向保留优势；8/12 显著特征编码操纵二分；
  sign=majority baseline；flyvis/toposens2026 强基线未重跑。
Evidence basis: §5.1、r39_heldout/metrics.json、main.tex:454-460、:657-659
Fatal concern if any: 无（但中心主张证据外推受限）
Score-change condition: 操纵外独立图族验证 + 至少一个确认机制迁移的真实结果 → 6–7
```

```
Reviewer: R5 Novelty / Positioning Reviewer
Expertise: null models / network motifs / related work
Likely score: 6
Confidence: 3
Main positive signal: 「控制充分性 = 保护未消融结构」的 framing 与嵌套阶梯设计有真实增量，超出 toposens2026 的
  单一度保持 null；预注册三方裁决干净。
Main negative signal: 核心洞察（全局统计不保护局部路径）事后偏直觉；Eq.(1) 为简单交换概率上界；与 closest prior
  work 的增量主要是「更高阶 rung + 任务感知 null」；**5 条 2026 预印本 + Cell 2026 题录无法由磁盘核验**，
  related-work positioning 未经独立联网确认（输入仅限磁盘）。
Evidence basis: main.tex:142-156、250-289、main.bib
Fatal concern if any: 无
Score-change condition: 公开核验关键前作题录 + 补 1–2 项真正高层级 null 基线对比 → 7
```

```
Reviewer: R6 Writing / Clarity Reviewer
Expertise: 科技写作 / 可复原性
Likely score: 6
Confidence: 5
Main positive signal: 六节结构、claim→表可回溯、术语稳定、限定明确、图 4 张均有 \ref。
Main negative signal: 摘要单段塞入 4 组结果(main.tex:26-55) 密度过高；§gate 与 §Discussion 完整性披露冗长；
  Table 1/4 用 \resizebox 缩放双栏数值偏小；main.bib:2-4 残留不完整 provenance 注释。
Evidence basis: main.tex:25-56、326-337、654-689；tables.tex / tables_taskaware.tex
Fatal concern if any: 无
Score-change condition: 摘要拆分 + 披露表化 + 表格改 \footnotesize → 7（仅该维）
```

```
Reviewer: R7 Ethics / Reproducibility Reviewer
Expertise: 负责任研究 / 工件审计
Likely score: 7
Confidence: 5
Main positive signal: CC-BY 4.0 署名、无受试、失败/崩溃/非复现/负结果全披露、双份互证、5 SHA 可实算、
  misuse risk 明确；局限披露纪律属 clear strength。
Main negative signal: LLM Usage Statement 为占位段（强制项缺失，行政）；被评目录无 .log 编译产物、
  paper/sources/ 快照不存在；taskaware 数值部分系从 agent 打印 summary 转录（已披露）。
Evidence basis: declaration-change-record.md、main.tex:674-689、metrics_from_trajectory.json::/provenance
Fatal concern if any: 行政（LLM 占位段），非科学
Score-change condition: 作者补声明 + 补编译日志与 sources 快照 → 维度维持；不改变由证据决定的总分
```

### Panel synthesis

```
Agreement: 7/7 认为受控图证据严谨、可复现、诚实，无致命科学缺陷；均不主张 accept/strong accept。
Disagreement: R1(7)/R7(7) 强调方法学价值与披露纪律；R2(4) 强调 venue mismatch 与零视觉证据；
  R4(5)/R5(6)/R6(6)/R3(6) 居中，分歧集中在「方法学严谨能否抵消机制未迁移 + 视觉证据缺失」。
Decisive positive axis: 主矩阵证据干净且逐字段可复算 + 5 脚本 SHA 实算匹配 + 统计协议严谨 + 无 cherry-pick。
Decisive negative axis: 中心机制仅成立于合成 XOR 替身、真实图 hypothesis_supported=false、真实视觉任务负结果、
  强基线未重跑 → 对 CVPR 主会 significance 有限（M1–M3）。
Unresolved evidence: 题录中 2026 预印本/Cell 2026 真实性（禁止联网，未核验）；0 overfull 的被评版本编译日志；
  flyvis/toposens2026 栈上的同协议对证；操纵外独立图族的特征预测力。
AC stance: borderline（lean-positive 下沿）。最终立场跟随最强未解决关切（M1/M2/M3 的证据性缺口），
  不被 R1/R7 的高分与维度平均抹掉；行政 blocker 单列，不加权科学总分。
```

---

## 10. AC / Meta-Review

- **Reviewer consensus**：执行质量与可复现性无争议地高；科学贡献范围与 venue-fit 是唯一实质分歧轴。
- **Reviewer disagreement**：方法学价值（R1/R7）vs 视觉相关性（R2）之差，根源是**贡献类型与 CVPR 口味的错配**，非证据可靠性问题。
- **Decisive acceptance axis**：一篇预注册、可复算、诚实、提出可复用「控制充分性」诊断标准的评估方法学论文，在「诊断/benchmark」贡献类型上接近完备。
- **Decisive rejection axis**：正向机制只在 96 节点合成 XOR 图确立，真实 MaleCNS 图 `hypothesis_supported=false`、度保持 null 反向保留优势，真实视觉任务负结果、非图 MLP 主导，强基线未复跑 —— 这一组**证据性**事实（非披露行为）锁定了分数上限。
- **AC stance / 分数来源声明**：分数由「最强未解决证据关切」决定。**明确声明**：(a) 分数偏低**不是**因为论文诚实披露负结果、失败预检、非复现或写出削弱自身主张的限定（隐藏这些会使 Evidence/Ethics 更低并触发诚信问题）；(b) 分数**不是**因披露、格式修补、范围表或 LLM 占位段等被抬高或压低；(c) 压分来自三个**证据性**事实：正向机制仅成立于受控 XOR 诊断标签、真实视觉正向效应从未建立、对 CVPR 视觉受众 significance 有限；(d) 行政 blocker（LLM 占位段）与不可核验项（0 overfull 缺日志、sources 缺失、题录未联网）如实计入 desk/Confidence，不作为压低科学总分的杠杆。
- **Discussion risks**：CVPR 主会审稿人可能就「方法学论文是否属于本会」产生强分歧；rebuttal 若不能给出真实图/视觉任务上的机制确认，难以上移到 weak accept。

---

## 11. 七维 Scorecard（每维 1–5，附置信度、证据依据、扣分点、升分条件）

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | 4 | 4 | `main.tex:93-124`（预注册三方裁决、4 rung + 匹配对照、机器校验不变量）；`main.tex:142-156,250-289`（相对 `toposens2026` 的增量） | 扣分：核心洞察（全局统计不保护局部路径）事后偏直觉，Eq.(1) 为简单交换概率上界；增量主要是更高阶 rung + 任务感知 null；closest prior work 与 5 条 2026 预印本题录未经磁盘外核验。**升到 5**：公开核验关键前作 + 补 1–2 项真正高层级 null 基线对比，或给出改变社区实践的控制标准被采用证据 |
| Soundness | 4 | 5 | `p3_p4/metrics.json`（主矩阵 + 8 条件 `bh_q=0.0002`）；`main.tex:205-209,271-279`（A^T 缺陷修正、Eq.(1) 上界限定）；`metrics_completed.json::/oracle_recheck`（600ep + clean 2-ch oracle `0.9232` vs ceiling `0.9395`）；`r39_density_sweep::/oracle_dense=1.0` | 扣分：3-seed 预检 `verdict=FAILED` 保留（虽诊断为 probe defect）；早期 18017 末块崩溃/CRC mismatch/LOGO 重算保留；sparse 五变量同改（已诚实声明、并由单变量 sweep 补证）。**升到 5**：一条哈希可核验、pre-check 通过的端到端主实验重跑 + dense 图 oracle 正对照（后者 §density 已补） |
| Evidence | 3 | 5 | 主矩阵 10 seeds/CIs/q（`tables.tex`）、invariants（`tables.tex`）、robustness 4 格（`tables.tex`）、task-aware/dose（`tables_taskaware.tex`）、20 图 held-out（`tables_heldout.tex`）、dense/sparse 真实图（`tables_heldout.tex`）、密度 sweep + 视觉任务（`tables_boundary.tex`） | **≤3 具体扣分**：(i) 中心 motif-survival 阈值在真实图未复现（`r39_real_connectome_v2::/hypothesis_supported=false`、度保持 null 保留 `0.6162`）；(ii) 8 个 BH 显著特征主要编码 10 intact/10 degraded 操纵，`sign_agreement=0.60=majority_baseline`；(iii) flyvis / `toposens2026` 强基线未重跑（`main.tex:637,657-659`）。证据**完整可核验但支持中心主张的部分只在受控替身上收敛**。**升到 4**：操纵外独立图族验证特征预测力 + 至少一个确认机制迁移的真实数据结果 |
| Significance | 3 | 4 | `main.tex:88-91`（自述无 image benchmark / 无自然视觉任务 / 无视觉精度声称）；`r39_visual_task/metrics.json`（MLP `0.9722` 主导、real≈deg-null）；`main.tex:642-652`（四步审计建议，社区可复用） | 扣分：对连接组约束建模小社区有真实价值，但对 CVPR 主会视觉受众 relevance 有限；无 SOTA、无视觉 benchmark、真实视觉任务负结果。**升到 4**：在真实视觉任务/真实连线上演示该诊断标准改变了一个实际结论，或证明被社区采纳 |
| Clarity | 4 | 5 | 六节结构 + claim→表可回溯 + 4 图均有 `\ref`；`main.tex:691-703` Conclusion 与限定一致性；`main.tex:654-672` Limitations | 扣分：摘要单段塞 4 组结果（`main.tex:26-55`）；§gate/§Discussion 披露冗长；Table 1/4 用 `\resizebox` 双栏数值偏小；`main.bib:2-4` 残留不完整 provenance 注释。**升到 5**：拆分摘要、披露表化、表格改 `\footnotesize`、清理题录注释 |
| Reproducibility | 4 | 5 | 冻结种子/超参（`p3_p4/metrics.json::/environment/config`）、5 个 `script_sha256` 自报与磁盘实算精确匹配（§5.2）、raw+completed metrics、per-seed logs、invariant counts、自动生成 `tables*.tex`、task-aware/v2 双份互证 | 扣分：被评目录**无 `.log/.aux/.blg`**（0 overfull/0 undefined 编译告警无法从本版直接核验）；`paper/sources/` 快照不存在；taskaware 部分数值系从 agent summary 转录（已披露）；18017 端到端哈希重跑未做。**升到 5**：补全被评版本编译日志与 sources 快照、提供公开匿名工件、完成一条哈希可核验的端到端重跑 |
| Ethics / Limitations | 5 | 5 | `main.tex:654-689`（data/baselines/statistics/protocol/task/comparability 六类局限 + CC-BY 4.0 + 无受试 + misuse risk）；FAILED 预检/崩溃/CRC/非复现/负结果全披露；`declaration-change-record.md`（占位段为作者留白、诚实标注） | 无科学扣分：局限披露纪律属 clear strength。**升分条件**：本维已达上沿；按任务规则该维高分**不单独抬高 Overall**，且高分**非因「披露负结果」这一行为本身**。行政项（LLM 占位段）单列于 §3/§6，不改变本维科学判定 |

**Overall:** 6  | **Scholarly Confidence:** 4

**Recommendation:** borderline（lean-positive 下沿）—— 不建议以当前形态直接投 CVPR 2027 主会；行政上须先补齐 LLM Usage Statement 声明方可提交。
**Verdict:** 上移 1 分需「真实图上确认机制迁移 + 强基线复跑 + 一项真实视觉正结果」；下移 1 分由「复核发现受控图主矩阵存在选择性呈现或统计协议缺陷」触发（当前逐字段对账未发现此类问题）。

> **Never round / 无锚点声明**：6 是独立推演的校准值，不是把某中间值上/下取整、不是为凑任何目标分（含目录名或历史分数）而取，也不是七维平均（3.86/5）的线性映射。Scholarly Confidence 取 4 而非 5，因缺 appendix、缺被评版编译日志、题录 2026 预印本与相关工作报告未经允许范围外的公开检索（见 `calibration-and-rank.md` Confidence 锚点）。

---

## 12. Concern-to-action 表

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
|---|---|---|---|---|---|---|---|---|
| C1 | **fatal（行政）** | LLM Usage Statement 为占位段 | `main.tex:707-708`；`declaration-change-record.md` | 合规（非科学维度） | ethics/limitations | 作者补写声明 → 重编译 → 刷 hash → 复核 p9 | 作者（门户侧） | **不改变科学总分**；仅决定是否可提交 |
| C2 | major | 中心机制真实图未复现 / 不迁移 | `r39_real_connectome_v2::/hypothesis_supported=false`；`main.tex:554-560,698-700` | Evidence, Significance | experiment | 新真实图实验确认 motif-survival 阈值迁移 | `ccf-experiment-designer` | 确认后 Evidence 3→4、Overall +0.5~1 |
| C3 | major | 零视觉证据 / 真实视觉任务负结果 / venue-fit | `main.tex:88-91,600-624`；`r39_visual_task/metrics.json` | Significance, Evidence | experiment / venue-mismatch | 真实视觉任务上演示诊断标准改变实际结论，或改投更契合的 benchmark/eval track | `ccf-experiment-designer` / 作者 | 满足后 Significance 3→4 |
| C4 | major | 强基线（flyvis / `toposens2026`）未复跑 | `main.tex:637,657-659` | Evidence, Novelty | experiment | 在其栈上跑一次同协议比较，或明确收窄为受控图内部结论 | `ccf-experiment-designer` | 复跑后 Evidence 上沿 +0.5 |
| C5 | moderate | held-out 8 特征编码操纵、sign=majority baseline | `r39_heldout/metrics.json`；`main.tex:454-460` | Evidence | experiment | 非操纵独立图族验证特征预测力 | `ccf-experiment-designer` | 验证后 Evidence 3→4 |
| C6 | moderate | 3-seed FAILED 预检 + 18017 崩溃/CRC/LOGO 重算保留 | `p3_p4/metrics.json::/p2_gate_corrected`；`main.tex:662-666` | Soundness, Reproducibility | reproducibility | 一条哈希可核验、pre-check 通过的端到端主实验重跑 | `f-research-v1` correction loop | 完成后 Soundness 4→5 |
| C7 | minor | 0 overfull 缺被评版编译日志；`paper/sources/` 快照不存在 | `R49-7.5-DELIVERY/manuscript/` 无 `.log`；磁盘无 `sources/` | Reproducibility | reproducibility | 附本版 `latexmk` 日志与 sources 快照 | 作者 | Reproducibility 4→5 |
| C8 | minor | 摘要过载 / 表格缩放 / `main.bib:2-4` 残留注释 | `main.tex:26-55`；`tables.tex`；`main.bib:2-4` | Clarity | writing / compression | 拆摘要、表格改 `\footnotesize`、清理题录注释 | `ccf-paper-writer` | 仅 Clarity 4→5，不改总分 |
| C9 | minor（未核验） | 5 条 2026 预印本 / Cell 2026 题录真实性未核验 | `main.bib`；输入仅限磁盘 | Novelty, Confidence | related-work | 允许范围内公开核验前作题录 | 作者 | 核验后 Confidence 4→5 / Novelty positioning 稳固 |

---

## 13. Score-Change Conditions 与两方向 Tie-breaker

| Change | Condition | Likely affected dimensions | Expected movement |
|---|---|---|---|
| **Raise score** | (a) 真实 MaleCNS 图上以预注册协议**确认** motif-survival 阈值迁移（`hypothesis_supported=true` 且度保持 null 不再保留优势）；(b) 在 flyvis/`toposens2026` 栈复跑同协议对证；(c) 至少一项真实视觉任务上该诊断标准改变了一个实际结论 | Evidence, Significance, Novelty | 单项 +0.5；三项齐备 Overall 6→7~7.5（维度分不单独抬高总分，须由证据性关切解除触发） |
| **Lower score** | (a) 复核发现主矩阵存在选择性呈现 / 丢弃条件列 / 统计协议（配对、BH、LOGO 折内选择）缺陷；(b) 题录被证实含虚构条目或隐藏作者身份外链；(c) 受控图主效应无法由冻结种子复现 | Soundness, Evidence, Ethics | −0.5 到 −1；若 (b)(c) 成立可触发 fatal |
| **No quick change** | 继续补流程/披露/格式（摘要拆分、披露表化、补 LLM 声明、修 overfull、补编译日志、统一口径、范围表）——这些属透明度与可核验性，**不新增支持中心主张的科学证据** | Clarity, Reproducibility（维度内） | 不改变 evidence-capped overall；行政 blocker 解除仅恢复「可提交」状态 |

### 固定该分数的两个 Tie-breakers

- **阻止上移到 7（weak accept）的 tie-breaker**：最强未解决关切是**证据性**的——中心机制（motif 生存为控制充分性因果判据）仅在 96 节点合成 XOR 诊断图上确立，真实 MaleCNS 图 `hypothesis_supported=false` 且度保持 null 反向保留优势（`0.6162`），真实视觉任务为负结果、非图 MLP `0.9722` 主导，flyvis/`toposens2026` 强基线未复跑。按 `calibration-and-rank.md` Consistency Check #1（overall 必须匹配最强未解决弱点）与 `review-output-standards.md` Synthesis Rule（final stance 跟随最强未解决关切、不被平均掉），这组 ≥3 个决定性关切不允许 Overall 上到 7（7 要求「no fatal risk; one or two moderate concerns」）。
- **阻止回落到 5（borderline negative 下沿）的 tie-breaker**：主矩阵证据包干净且逐字段可复算（大效应 `0.8152`、10 seeds、配对 CI、BH `q=0.0002`、完整对照/ablation/dose、机制环闭合）、5 个执行脚本 SHA-256 全部实算匹配、统计协议严谨、全部负结果/失败/范围限定诚实披露且无 cherry-pick、无致命科学缺陷。这些使论文明显优于「merits and risks balanced 的 negative 下沿」，构成 borderline 略偏 positive 的 6。

---

## 14. Questions For Authors（决策相关）

1. 是否有在 flyvis / `toposens2026` 训练栈上跑同协议比较的计划或结果？若无，是否接受把贡献明确收窄为「受控图内部的方法学结论」？
2. 真实 MaleCNS 稀疏子图上度保持 null 保留优势（`0.6162`）、task-aware null 反而更低（`0.5850`），与受控图模式相反：这是否意味着「null 家族是混杂」这一 headline 应改写为「null 行为依赖目标图密度/高阶组织」？
3. 20 图 held-out 中 8 个显著特征有多大比例可纯粹由 10 intact / 10 degraded 二分解释？能否给出剔除该操纵后的独立图族预测力？
4. `main.bib` 中 5 条 2026 年 arXiv 预印本与 `Cell 189(18)`（2026）的题录来源与可核验链接是什么？
5. 能否提供**本被评版本**的 `latexmk` 编译日志以直接核验「0 overfull / 0 undefined」，以及 brief 所列 `paper/sources/` 快照？
6. LLM Usage Statement 占位段由作者补写后，声明将如何界定 LLM 在文本/图/代码/实验/related work/ideation 上的使用性质与程度而不泄露身份？

---

## 15. Score Revision Criteria

```
Raising the score would require: 真实图上确认 motif-survival 阈值迁移（预注册协议下 hypothesis_supported=true）
  + 至少一个强基线栈的同协议复跑 + 一项真实视觉任务上该诊断标准改变实际结论；三者为证据性新增，非 prose/格式修补。
Lowering the score would be triggered by: 主矩阵选择性呈现或统计协议缺陷被复核证实、题录虚构/隐藏外链、
  或受控图主效应无法由冻结种子复现。
Concerns unlikely to change before submission: M1/M2/M3（需新实验或新 venue 定位）、M4（需独立图族）、
  题录真实性核验（输入范围限制）、0 overfull 的本版日志与 sources 快照补齐。
```

---

## 16. Action Plan / Checks / Unresolved / Output self-check

```
Priority 1 (行政): 作者补写 LLM Usage Statement → 重编译 → 刷 hash → 复核 p9。
  Owner: 作者（门户侧） | Handoff: no | 输出: 可提交包件；不改变科学总分。
Priority 2 (科学): 设计「真实图机制迁移确认」实验 + flyvis/toposens2026 同协议复跑。
  Owner skill: ccf-experiment-designer | Handoff: yes | 输出: 解除 M1/M3，决定能否上移。
Priority 3 (科学): 非操纵独立图族验证 held-out 特征预测力。
  Owner skill: ccf-experiment-designer | Handoff: yes | 输出: 解除 M4/C5。
Priority 4 (写作/格式): 摘要拆分、披露表化、表格缩放、清理 main.bib 残留注释、补本版编译日志与 sources 快照。
  Owner skill: ccf-paper-writer | Handoff: no | 输出: Clarity/Reproducibility 维度内改善，不抬高总分。
```

```
Checks run: C-01 版本锁定、C-02 headline 数字对账(~90 项)、C-03 5 脚本 SHA-256 实算、C-04 引用完整性(15=15)、
  C-05 CVPR 合规(9 页/双盲/题录外链/隐藏指令/编译告警可核验性)、C-06 注入扫描、C-07 工程制品扫描、
  C-08 双盲、C-09 披露处理纪律。
Checks skipped: 图像像素内容逐图查看（仅核存在与 \ref）；2027 官方规则联网复核（输入仅限磁盘）；
  2026 预印本/Cell 2026 题录真实性联网核验（输入仅限磁盘）；相关工作报告公开检索（输入仅限磁盘）。
Unresolved risks: 题录真实性未核验；0 overfull 缺被评版本编译日志；paper/sources/ 快照不存在；
  flyvis/toposens2026 栈同协议对证缺失；操纵外独立图族特征预测力未建立；CVPR 主会 venue-fit 分歧。
```

**Output self-check（逐条）**：
- 节序与 `full` 输出契约及 brief 要求一致；所有表格 Markdown 分隔符与列数一致。✓
- 七维 Scorecard 全维打分，每个 ≤3 维（Evidence 3、Significance 3）均附具体扣分点与修复条件；每维均附置信度、可引用证据依据、升分条件。✓
- 全文含且仅含一行 Overall / Scholarly Confidence 加粗结论行（位于 §11），其余位置未重复该精确格式字符串。✓
- 7 人独立 panel 在 AC 综合前各自独立给分；AC 立场跟随最强未解决关切、未被维度平均（3.86/5）抹掉。✓
- Score-Change Conditions（raise/lower/no quick change）+ 两个方向 tie-breaker 齐备。✓
- 严守 Never round；未抄用/平均/锚定历史分数或 brief 数字；未为凑目标分取整。✓
- 未因诚实披露负结果、失败预检、非复现或自我限定主张额外扣分；未仅因披露抬高总分；行政 blocker 如实报告且不加权科学总分。✓
- 未修改任何稿件、指标、审计、账本或校验器文件；报告仅写入唯一指定路径。✓

# R120 — 常驻心跳指令 ↔ 落盘状态：首次逐条字节对账 + 外部决策债去重合并

**状态：`READ_ONLY_RECONCILIATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`** · 2026-11-14 08:1x–08:5x +0800 · 轮次 R120（心跳）

**首行边界**：零门晋级、零自我认证、零状态写回、零科学结果、零模型前向 / 推理 / 训练 / 标签 / 数据集 / EPE·l2 / 科学指标、零网络请求、零阈值改动、零稿件改动、零评审发起、零 COMPLETE。

---

## 0. 本轮换道理由（RGE4）

R105 / R107 / R109 已三次判停「继续产出证据文档」同构循环；R110 做透达标机器门可达性，R111 把剩余动作全部判给 designated gate owner（5 决策点），R114–R118 连续五轮做「不需批准的一手许可 / 归档 / 执行前提 / registry 清点」，R119 改做「唯一成功标准动作的评审启动协议链」。**这六轮都在采集新一层的证据或审计新一层协议，但没有一轮把「每 30 分钟重复下发的常驻指令本身」与「已经落盘的字节状态」逐条对账。**

本轮不修机器门、不写第 N 份 G0 文字补丁、不起 P3 前向、不重开探针 / 守卫 / runner 补丁循环、不创建 v4 契约。改做两件前 119 轮未见先例的**只读结构性工作**（严格收窄为「本轮可见产物中未见先例」的范围观察，非「首次发现」全称否定）：

1. **常驻心跳指令第 1 步（① ② ③）逐条对账落盘状态**：把用户每次唤醒都重复下发的清单，按原始字节核验「已做 / 部分做 / 未做 / 须外部裁决」。
2. **外部决策债去重合并成单一登记册**：R99 / R106 / R107 / R110 / R111 / R114 / R115 / R116 / R117 / R118 / R119 把须用户或 designated gate owner 批准的决策散落在 11+ 份文件里，且每轮「交下轮」都重新列一遍、彼此重叠。本轮产出**一份**去重、按依赖排序、带精确 `文件:行号` 锚点的登记册，交给决策方一次性裁决。

**这不是达标路径上的科学进展**，是把「为什么循环停在原地」这一结构性事实变成可复算、可一次性裁决的对象。

---

## 1. 核心实质发现：常驻指令 ② 在 R108 已作为草稿脚手架落盘，但十轮交接从未登记

### 1.1 常驻指令原文（逐字，来自本次唤醒的 user query 第 1 步）

> ① 按 R106 gate review 的 Concern-to-action 闭合 G0 实质缺口（尤其成文 G0 pass criterion 与 gap 1/2/4，不写补丁式文字修复）；② **U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state（不往 guidance state 塞 P 阶段）**；③ 按序 G1–G8（G4 正面处理 Kuklev v2 时间尺度 sweep）→ validation → handoff → P0 → P1A/P1B → P2 → P3 真实前向解决 U5。

该清单是**每次唤醒重复注入的常驻 prompt**，不是磁盘文件；其磁盘重述件逐字锚定在：

| 锚点 | 文件 | 行 | 内容 |
|:--|:--|--:|:--|
| A2a | `gate-G0-R107/isolated-post-review/R107-R1-R8-G0-CLOSURE-PACKAGE.md` | 175 | `③ U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state` |
| A2b | `gate-G0-R107/R107-R1-R8-G0-CLOSURE-PACKAGE.md` | 175 | 同上（主副本逐字一致） |
| A2c | `gate-G0-R107/isolated-post-review/R107-ROUND-AUDIT.md` | 116 | `③ U6/W2 版本化契约 → 新建 f-research-v1 P0 state（不往 guidance state 塞 P 阶段）` |
| A2d | `gate-G0-R107/isolated-post-review/R107-INDEPENDENT-REVIEW-RECOVERY.md` | 180 | `② U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state` |

**同时必须登记一个已有的观察，防止「首次发现」夸大**：`state-handoff-R111/R111-ROUND-AUDIT.md:26` 逐字写过「心跳 prompt 内嵌「交下轮」仍是 **R106 清单**，但账本与 automation memory 已推进至 **R110**」。⇒ **指令 / 账本版本漂移在 R111 已被观察到**；本轮的增量不是「发现漂移」，而是把漂移**量化到具体条目**（② 已落盘）并**合并决策债**。R119 L3 教训在此适用。

### 1.2 ② 的落盘状态（原始字节复算，75/75 独立校验吻合）

| 检查 | 实测 | 判定 |
|:--|:--|:--|
| `state-handoff-R108/f-research-v1-state/pipeline-state.json` | 存在，5,190 B / SHA16 `c246468e50712522`；`pipeline=f-research-v1`、`contract_version=v1-R108-U6W2-draft`；**26 个 P0–P21 阶段全部 `pending`**；`history=[]`；`contract` 2 条 | 「新建 f-research-v1 P0 state」**已完成（草稿脚手架）** |
| 主链 `pipeline-state.json` | 3,723 B / SHA16 `bcb48bb964e657a4`；`pipeline=f-guidance-builder-v1`、`contract_version=v2`；12 阶段（`CCFA-startup` + G0–G8 + validation + handoff）；**P 阶段插入数 = 0** | 「不往 guidance state 塞 P 阶段」**满足** |
| `R108-U6-W2-VERSIONED-CONTRACT.md` | 7,307 B；:1 `（DRAFT，未激活）`；:3 `ENGINEERING_STATE_SCAFFOLD_ONLY_NOT_SCIENTIFIC_RESULT`；:5 `PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF` + 「本文件不是 P0 的启动」 | 版本化契约**已建但显式未激活** |

**精确判定（最易被夸大的一处）**：② 的字面要求「新建 f-research-v1 P0 state（不往 guidance state 塞 P 阶段）」在 R108 **作为 DRAFT 脚手架已满足**；但这**不等于**：P0 已启动、任何门已通过、handoff 已过、契约已冻结、或任何科学证据成立。R108 脚手架 26 阶段全 `pending`、`history=[]`、契约自述「不是 P0 的启动」。因此本轮把 ② 登记为 **`SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED`**，**不**登记为「已完成 / 已通过」，也**不**据此晋级任何门。

### 1.3 但机器门读的是第三个状态命名空间（与 R110 C5 一致，非新发现）

| # | 状态文件 | pipeline / contract | 阶段 | 谁读它 |
|:--|:--|:--|:--|:--|
| 1 | 主链 `pipeline-state.json`（run root） | `f-guidance-builder-v1` / `v2` | 12（1 passed / 11 pending） | 主线 G0–G8 门 |
| 2 | `state-handoff-R108/f-research-v1-state/pipeline-state.json` | `f-research-v1` / `v1-R108-U6W2-draft` | 26（全 pending） | 无（草稿脚手架，未被任何门读取） |
| 3 | `papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2/pipeline-state.json` | `f-research-v1` / `v2-R51` | 26（**13 passed / 13 pending**） | **validator D2 / guard A2** |

⇒ ② 创建的命名空间 #2 与验收机器门读取的命名空间 #3 **不是同一个文件**。这与 R110 C5「门路径停留在历史 v2 run root、主线从未被读取」的结论一致，**本轮不主张新发现**；本轮增量是把它量化为**三个互异 SHA 的状态命名空间并存**（`bcb48bb9…` / `c246468e…` / `5e9b0245…`）。⇒ **即使 ② 的脚手架被激活，也不会改变 validator / guard 读数**；这正是 R111 D-1「交付对象与门路径裁决」须外部裁决的原因。

### 1.4 ① 与 ③ 的对账结果

| 常驻条目 | 落盘状态 | 判定 |
|:--|:--|:--|
| ① 成文 G0 pass criterion | `gate-G0-R107/R107-G0-PASS-CRITERION-REGISTER.md` 存在；:3 `DRAFT — PENDING DESIGNATED GATE OWNER APPROVAL`；:1 显式「不生效」；PC1–PC6 六条；PC4（:42）/ PC5（:45）标「未做」；:59 声明「本汇编不改变」任何 state 字节 | **DRAFT 已登记、未冻结、未生效**；不得当作 W13 缺口已闭合 |
| ① R106 W13 根因 | `gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md:48`「`fail-fast-gates.md` 全文从 G1 起，全文没有 G0 的定义」；:139 W13；:1 首行 `**Verdict:** PARTIAL \| **G0 may be passed:** NO`；§6 R1:161 / R6:166 / R8:168 / R9:169 | **权威成文判据仍缺** |
| ① gap 1 | R114/R115/R116 一手许可与归档内容取证已做；R116:85 把剩余三项判给 designated gate owner | **PARTIAL**（登记在册，非闭合） |
| ① gap 2 | `literature-baseline-matrix.md` 9,445 B 与 R106 freeze 字节一致；:46 `the open question`、:47 `Kuklev leaves`、:9 / :10 两处 `not yet verified` 原样保留 | **OPEN**（R118 W2 口径：矩阵定稿 + SHA 重冻须 gate owner 签署） |
| ① gap 4 | 全包无 designated G0 gate owner 的显式 scientific/visual gate judgment；R106 R6:166 | **OPEN** |
| ① G0 状态机 | 主链 `pipeline-state.json` G0 = `pending` / `inputs=[]` / `evidence=[]` / `gate_verdict=pending` | **pending，不得追认** |
| ③ G1–G8 → validation → handoff → P0 → P1A/P1B → P2 → P3 | 主链 11 个后续阶段全 `pending`；R108 脚手架 26 阶段全 `pending`；**零前向** | **未启动**；按 R117/R118 纪律「不在 G0 未过时启动 P3」 |

---

## 2. 双门本轮只读实测（字节锚定件已落盘，弥补 R118 W7 / R119 M2 的 /tmp 快照口径缺陷）

本轮把双门读数**写进本目录**而非 /tmp，使独立复核者可从字节复算：

- `R120-validator-out.json`（1,875 B）：`verdict=NOT_QUALIFIED`、`overall_score=6.0`、`threshold=7.0`、`comparison_operator=>=`、`score_meets_threshold=false`、`D1✓ D2✗ D3✗ D4✓ D5✗`、`all_pass=false`。
- `R120-guard-check.txt`（4,757 B）：`INCOMPLETE`；7 项交付物全 PASS；失败恰 **A2、A6**；S1–S7 **7 步全 pending**；动作序列 **0 条**。
- A6 双口径（R109/R111/R118 已知问题，**只读登记不改、不称新发现**）：`guard/criteria-null-ladder.json:132` `>= 7.0` / `:136` `g>=7.0`；`guard/ledger-null-ladder.json:134` `严格 > 8.0` / `:138` `g>8.0`；`guard check` 实取 ledger 口径。
- validator 活配置：`readonly-validator/validate_single_paper.py:133` `default=7.0`、`:146` `score >= args.threshold`、`:148` contract 串 `Overall >= 7.0`、`:155` `score_meets_threshold`。⇒ R107 终值 `>=7.0` 在 validator 与 criteria 已生效；**ledger 未同步属遗留机器门口径差，不是成功标准改动**。
- **governing 未变**：`ccfa-review-reports/` 10 份 `.md`，最新为 `paper-null-ladder-r95-independent-review-20261111.md`（11-11 15:01）；全项目 `^\*\*Overall:\*\*\s*[0-9]` 真分数行 12 处，均在 11-08～11-11 的历史报告与其 `provenance/` 副本中，**r95 之后 0 份新独立 full 评审**。⇒ governing 仍 **R95 = 6.0 / Confidence 4.0**。

---

## 3. 可复算性

- `R120-raw.py`（采集，31 源）→ `R120-RECONCILIATION-RAW.json`（31 源 SHA/字节/mtime + A/B/C 三组断言）、`R120-SOURCE-MANIFEST.json`。
- `R120-verify.py`（**不 import 采集模块、不读任何 R120 JSON**，从原始字节独立重算）→ `R120-RECONCILIATION-VERIFICATION.json`：**75 检查 / 75 MATCH / 0 MISMATCH**。
- `isolated/` 31 份逐字节副本，31/31 SHA 一致。
- **v1 脚本缺陷如实留痕**：`R120-RECONCILIATION-RAW.v1-superseded.json` + `R120-SOURCE-MANIFEST.v1-superseded.json` 完整保留。v1 把 `PROJECT` 解析为 `RUN` 的上 4 层（应为 3 层），导致所有 project-root 源读空；另三处 needle 因全角括号 / 跨行折行 / R99 文件实际位于 run root 而假阴性。三者均属**脚本判定 / 搜索口径缺陷，不是数据不一致**（R116 / R118 W2 / R119 L3 纪律）；v2 修正后所有断言有值，v1 两版读数都保留、不改。
- 用 `/Users/xhf/miniconda3/bin/python`（本机 conda，Py 3.14.6）。同机同 `hashlib` 同数据源 ⇒ 两脚本一致只是**必然一致性核对、不构成独立交叉核验**（R115 W4 / R114 D1）；真正独立复算交全新隔离子代理。

---

## 4. 防夸大清单（逐条明确不主张）

1. **不主张 G0 可 pass**：R106/R107/R111 及本轮全部维持 `pending`；本轮无任何 PASS 动作。
2. **不主张 ② 已完成 / 已激活**：仅 `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED`；26 阶段全 pending、契约自述未激活。
3. **不主张新发现指令漂移**：R111:26 已观察到；本轮是量化到条目 + 决策债合并。
4. **不主张新发现门路径不一致**：R110 C5 已判定；本轮是量化为三个互异 SHA 命名空间。
5. **不主张 A6 双口径是新发现**：R109/R111/R118 已登记；只读登记。
6. **不主张机器门口径差 = 成功标准被改**：R107 终值 `>=7.0` 未动；ledger 遗留文本属须 gate owner 批准的对齐项。
7. **不主张任何科学结果 / 4090 能力 / forward pass / EPE·l2 / 数值论文分**：全轮零科学运行、零 `**Overall:**` 行、零评审发起。
8. **不主张 gap 1/2/4 已闭合**：PARTIAL / OPEN / OPEN，见 §1.4。
9. **不主张「前 119 轮从未审计」这类全称否定**：收窄为「本轮可见产物中未见先例」的范围观察。
10. **不主张独立审查已恢复**：全新隔离子代理已下发，落盘时未回收，不预支结论。

---

## 5. 结果与交下轮

**第 3 步前置（实质正向新科学证据）未满足** ⇒ 不进稿件新副本、不做 9 页合规编译、不起全新隔离 full 评审。**0 篇达标，未写 COMPLETE**，governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`；G0 维持 `pending`。停止门只剩 ①达标（>=7.0）②用户叫停。

交下轮：① 以 `R120-CONSOLIDATED-DECISION-REGISTER.md` 为**唯一**决策入口，按依赖顺序逐项裁决；心跳不自我认证、不自行回写任何 state / 矩阵 / registry / 门配置、不自行创建 v4 契约。② ② 项须裁决的是「是否激活 R108 草稿脚手架 + 由谁激活 + 与命名空间 #3 的交付对象关系」，**不是**再新建一份 P0 state。③ 仍不执行须批准的机器门修复，不写第 N 份 G0 文字补丁，不在 G0 未过时启动 P3。④ 只有 `failed_runs=0` + 全 finite + 独立复算吻合 + 实质正向新证据，才进稿件新副本 → 9 页编译 → 全新隔离 full 评审（不透露期望分）；**X >= 7.0** 且 QUALIFIED + COMPLETE 才写 COMPLETE。

---

**配套**：`R120-CONSOLIDATED-DECISION-REGISTER.md`（去重决策登记册）、`R120-ROUND-AUDIT.md`（轮次审计）、`R120-INDEPENDENT-REVIEW.md`（全新隔离子代理，待回收）、`R120-RECONCILIATION-VERIFICATION.json`（75/75）。

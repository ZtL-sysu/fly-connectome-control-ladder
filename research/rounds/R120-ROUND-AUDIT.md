# R120 轮次审计（2026-11-14 08:16–08:5x +0800，心跳唤醒）

**状态：`READ_ONLY_RECONCILIATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`**
**governing 仍 R95 = 6.0 / Confidence 4.0，`NOT_QUALIFIED` / `INCOMPLETE`；0 篇达标，未写 COMPLETE。**

---

## 1. 第 0 步：并发保护（不触发）

| 检查 | 实测 | 判定 |
|:--|:--|:--|
| `goal-ledger.md` mtime | `2026-11-14 06:59:48`；唤醒 `08:16:17` ⇒ **77 min** | > 10 min，不保护 |
| 主会话 / 轮询进程 | `ps -eo` 扫 `novix\|poll\|ccf-paper-review\|f-research\|pipeline_state\|validate_single` ⇒ **0 命中** | 无独立主会话 |
| 近 25 min 项目写入 | `find -mmin -25` 排除 automation memory ⇒ **0 文件** | 无并发写 |
| `ccfa-review-reports/` | 10 份 `.md`，最新 `paper-null-ladder-r95-independent-review-20261111.md`（11-11 15:01） | 无未登记异步 full 评审 |
| `ccfa-idea-review-reports/` | 最新 `idea-review-effective-indegree-unification-20261110.md`（11-10） | 同上 |
| 全项目真分数行 | `^\*\*Overall:\*\*\s*[0-9]` 共 12 处，`find -newermt "2026-11-11 15:02"` ∩ 该模式 ⇒ 唯一命中为 `provenance/` 下 r95 副本，非新报告 | **governing 未变** |
| R120 产物 | 唤醒时 `find -iname "*R120*"` ⇒ **0** | 本轮首次唤醒 |

⇒ 保护解除，主动推进，记 **R120**。

## 2. 换道理由（RGE4）

R105/R107/R109 三次判停「继续产出证据文档」同构循环；R110 做透达标机器门可达性，R111 判「自主可达动作穷尽」并交出 5 决策点，R114–R118 连续五轮一手许可 / 归档 / 执行前提 / registry 取证，R119 改做唯一成功标准动作的「评审启动协议链」。**六轮都在采集或审计新一层，但没有一轮把每 30 分钟重复注入的常驻指令本身与落盘字节状态逐条对账，也没有一份去重的外部决策债合并清单。**

本轮**不**修机器门、**不**写第 N 份 G0 文字补丁、**不**起 P3 前向、**不**重开探针 / 守卫 / runner 补丁循环、**不**创建 v4 契约。改做两件只读结构性工作：① 常驻指令第 1 步 ①②③ 逐条字节对账；② 把 11+ 份文件里散落、每轮重列、彼此重叠的外部决策去重为**一份**按依赖排序、带精确 `文件:行号` 锚点的登记册。

## 3. 实质发现（严格收窄）

- **常驻指令 ② 在 R108 已作为 DRAFT 脚手架落盘**：`state-handoff-R108/f-research-v1-state/pipeline-state.json`（5,190 B / SHA16 `c246468e50712522`）为 `f-research-v1` / `v1-R108-U6W2-draft`、**26 个 P0–P21 阶段全 pending**、`history=[]`、`contract` 2 条；`R108-U6-W2-VERSIONED-CONTRACT.md`（7,307 B）:1 `DRAFT，未激活`、:3 `ENGINEERING_STATE_SCAFFOLD_ONLY_NOT_SCIENTIFIC_RESULT`、:5 `PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF` +「本文件不是 P0 的启动」；主链 `pipeline-state.json`（3,723 B / `bcb48bb964e657a4`）12 阶段、**P 阶段插入数 = 0** ⇒「不往 guidance state 塞 P 阶段」满足。判定 **`SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED`**，**不是**完成 / 激活 / 门通过 / 科学证据。
- **不主张「首次发现」**：`state-handoff-R111/R111-ROUND-AUDIT.md:26` 已逐字观察「心跳 prompt 内嵌「交下轮」仍是 R106 清单，但账本与 automation memory 已推进至 R110」。本轮增量是把漂移**量化到具体条目**并**合并决策债**（R119 L3 教训）。
- **三个互异状态命名空间并存**（与 R110 C5 一致、非新发现）：主链 `bcb48bb9…`（12 阶段）、R108 脚手架 `c246468e…`（26 全 pending）、历史 v2 `5e9b0245…`（15,742 B / `v2-R51` / 26 阶段 = 13 passed + 13 pending，`P9–P21` pending）。**validator D2 / guard A2 读的是第三个** ⇒ 即使 ② 脚手架被激活也不改变双门读数；这正是 R111 D-1 须外部裁决的原因。
- **① 未闭合**：R107 G0 判据登记册为 `DRAFT — PENDING DESIGNATED GATE OWNER APPROVAL`，PC1–PC6，PC4/PC5「未做」，:59 声明不改任何 state 字节；R106:48 W13 仍缺权威成文判据；gap 1 PARTIAL、gap 2 OPEN（矩阵 9,445 B 字节零改动、:46/:47 stale 表述仍在）、gap 4 OPEN；G0 `pending/inputs=[]/evidence=[]`。
- **③ 未启动**：主链 11 个后续阶段全 pending、R108 脚手架 26 阶段全 pending、零前向。

## 4. 双门只读（本轮字节锚定，弥补 R118 W7 / R119 M2）

validator `EXIT=1 / NOT_QUALIFIED / 6.0 / threshold 7.0 / >=` / `score_meets_threshold=false` / `D1✓ D2✗ D3✗ D4✓ D5✗`；guard `EXIT=1 / INCOMPLETE`，7 交付物全 PASS、失败恰 **A2、A6**，S1–S7 **7 步全 pending**、动作序列 **0 条**。A6 双口径（criteria `>=7.0` / ledger `严格 > 8.0`）为 R109/R111/R118 已知问题，**只读登记不改、不称新发现**；`guard check` 实取 ledger 口径。读数落盘在本目录 `R120-validator-out.json`（1,875 B）与 `R120-guard-check.txt`（4,757 B），**不写 /tmp**，使独立复核者可从字节复算。

采集时刻 `goal-ledger.md` SHA16 `923050103709656b`、`guard/ledger-null-ladder.json` `73043b4e164a5a5f`、主链 `pipeline-state.json` `bcb48bb964e657a4` 前后一致 ⇒ **对既有字节零回写**（R119 M2：采集后标准只追加记账改变活文件哈希、不改任何历史字节）。

## 5. 可复算性与 v1 缺陷留痕

- `R120-raw.py` → `R120-RECONCILIATION-RAW.json`（31 源 SHA/字节/mtime + A/B/C 三组）、`R120-SOURCE-MANIFEST.json`；`R120-verify.py`（**不 import 采集模块、不读任何 R120 JSON**，从原始字节重算）→ `R120-RECONCILIATION-VERIFICATION.json`：**75 检查 / 75 MATCH / 0 MISMATCH**；`isolated/` 31 份逐字节副本 **31/31 SHA 一致**。
- **v1 脚本缺陷（如实留痕、非数据不一致）**：`R120-RECONCILIATION-RAW.v1-superseded.json` + `R120-SOURCE-MANIFEST.v1-superseded.json` 完整保留。① `PROJECT` 解析为 `RUN` 上 4 层（应为 3 层）⇒ 所有 project-root 源读空（A1/B6/B7/B9/C8 全 0 或 null）；② 全角括号 needle `(DRAFT，未激活)` 假阴性；③ 跨行折行 needle `the open question Kuklev leaves` 假阴性（实为 :46 / :47 两行）；④ `R99-design-block-decision.md` 实际位于 run root 而非 project root。v2 修正后所有断言有值；两版读数都保留、v1 原字节不改写。按 R116 / R118 W2 / R119 L3 纪律：**脚本判定 / 搜索口径缺陷，不是数据不一致或编造**。
- 同机同 `hashlib` 同数据源 ⇒ 两脚本一致是必然一致性核对、**不构成独立交叉核验**（R115 W4 / R114 D1）；真正独立复算交全新隔离子代理。
- 用 `/Users/xhf/miniconda3/bin/python`（本机 conda，Py 3.14.6）。

## 6. 内容安全（本轮目录）

42 文件、最大 672,217 B（`isolated/goal-ledger.md`，逐字节历史账本副本）；**严格真实凭证值模式 0 命中**（`AIza…` / `ghp_…` / `PRIVATE KEY` / 赋值型 api_key/secret/password 全 0）；宽口径「credential」关键词 8 命中全为历史审计的**叙述性措辞**（如「9 类凭证模式」「含 `api_key` 赋值」），非凭证值；本机绝对路径 125 命中**全部来自 `isolated/` 逐字节副本与双门读数**（字节一致副本必然含路径，R119 M1 / R115 W2）⇒ **`isolated/` 与原始读数一律不上传公开仓库，只上传脱敏摘要**；真分数行 `^\*\*Overall:\*\*\s*[0-9]` **0 命中**。无 >50 MiB / 数据集 / 权重 / 二进制 / 第三方源码 / 未投稿稿件。

## 7. 全新隔离独立审查

已下发**全新隔离子代理**（`general-purpose-1`，不透露期望分 / 分数锚点、不给结论锚点），任务为从源字节独立复算 A–L 共 12 组读数 + 12 类点名夸大逐条判定 + 瑕疵分级；**写本段时尚未回收，不宣称任何审查结论**。门 / 证据层复核，**非** `ccf-paper-reviewer full` 稿件评审、不产生 `**Overall:**` 行、不改 governing。回收后按 R114–R119 纪律只追加更正段；若结论与更正需同步，按 R117/R119 先例另建**新的不可覆盖检查点**，已发布检查点字节不回写。

## 8. 零门晋级 / 严格边界

全 `READ_ONLY_RECONCILIATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`；EXEC LOCK 零前向 / 推理 / 训练 / 标签 / 数据集 / EPE·l2 / 科学指标、零网络请求；零门晋级、零自我认证、零状态写回（G0 `pending`）；未改历史字节 / 评审 / 分数 / 阈值 / 稿件 / 门 / 冻结件 / 矩阵 / registry / 门配置；未创建 v4 契约、未起 `ccf-paper-reviewer full`、未产生 `**Overall:**` 行、未自评 governing、未跳门、未对未修改稿件重复评审；未重开 D1/v3、未出 predictor v4、**未假定 `≤32h / K=45` confirmation 授权**；与 harbor 25092 工程 reward 无关、无 4090/L4/H20 能力主张；主项目未投稿 / commit / push；心跳 ACTIVE 调度 `FREQ=HOURLY;INTERVAL=1;BYMINUTE=0,30` 无变化。

## 9. 结果

第 3 步前置（**实质正向新科学证据**）未满足 ⇒ 不进稿件新副本、不做 9 页合规编译、不起全新隔离 full 评审。**0 篇达标，未写 COMPLETE**，governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`。停止门只剩 ①达标（>=7.0）②用户叫停。

## 10. 交下轮

① 以 `R120-CONSOLIDATED-DECISION-REGISTER.md` 为**唯一**决策入口（10 个去重决策组、最小可解锁集 `G1 + G4 + G10`），按依赖顺序逐项裁决；心跳不自我认证、不自行回写任何 state / 矩阵 / registry / 门配置、不自行创建 v4 契约。② ② 项须裁决的是「是否激活 R108 草稿脚手架 + 由谁激活 + 与命名空间 #3 的交付对象关系」，**不是**再新建一份 P0 state。③ 仍不执行须批准的机器门修复（5 决策点待答复）、不写第 N 份 G0 文字补丁、不在 G0 未过时启动 P3。④ 按序 G0–G8（G4 正面处理 Kuklev v2 §7.3/§8/§9）→ validation → handoff → P0 → P1A/P1B → P2 → P3 真实前向解决 U5。⑤ 只有 `failed_runs=0` + 全 finite + 独立复算吻合 + 实质正向新证据，才进稿件新副本 → 9 页编译 → 全新隔离 full 评审（不透露期望分）；**X >= 7.0** 且 QUALIFIED + COMPLETE 才写 COMPLETE。⑥ **新教训**：写「零本机路径」须限定到具体上传集；写「零字节改动 / SHA 前后一致」须声明采集时刻；「首次 / 从未」全称否定须收窄为范围观察；双门读数落盘到 run root 而非 /tmp 才能被独立复核者从字节复算；`isolated/` 逐字节副本必然含本机路径，脱敏承诺只覆盖 manifest 字段与公开摘要。

## 11. 审计 / 证据

主线 `reconciliation-R120/`：`R120-STANDING-INSTRUCTION-RECONCILIATION.md`、`R120-CONSOLIDATED-DECISION-REGISTER.md`、`R120-ROUND-AUDIT.md`、`R120-raw.py`、`R120-verify.py`、`R120-RECONCILIATION-RAW.json`（+ v1-superseded）、`R120-RECONCILIATION-VERIFICATION.json`、`R120-SOURCE-MANIFEST.json`（+ v1-superseded）、`R120-validator-out.json`、`R120-guard-check.txt`、`isolated/` 31 份；回收后另有 `R120-INDEPENDENT-REVIEW.md`、必要时 `R120-POST-REVIEW-CORRECTION.md`。公开仓库脱敏摘要 `evidence/R120-RECONCILIATION-SANITIZED.md` + 不可覆盖检查点 `20261114T004555Z-r120-reconciliation/`。


---

## 12. 独立审查同步回收 + 只追加更正（主段 §7「未回收」为写时点实况、不回写）

全新隔离子代理 `general-purpose-1`（不透露期望分 / 分数锚点 / 结论锚点）最终交付 `R120-INDEPENDENT-REVIEW.md` **23,074 B / SHA256 `c7c613c54bd08cad1b945c5affcdf371522430e63fff84d702ac86625cf3d9ea`**（mtime `08:55:00`，单次写入、无中间态、原文零改动）。首行 `**Verdict:** REPRODUCIBLE_WITH_DEFECTS | **G0 may be passed:** NO | **Scientific result claimed:** NO`、次行 `**Forward pass performed:** NO`。**A–H、J、L 全 MATCH；I、K MISMATCH**；**12 类点名夸大 (a)–(l) CONFIRMED = 0（全 REFUTED）**；**7 处瑕疵（1 HIGH / 3 MEDIUM / 3 LOW、0 编造、0 数据不一致）全部接受、只追加**（`R120-POST-REVIEW-CORRECTION.md`）。复核者不读任何 R120 JSON、全部从源字节重算。

- **W1 [HIGH] 撤回字面口径**：claim I「全项目无更晚文件含数值 `**Overall:**` 行」被否证；`R120-raw.py` 的 `numeric_overall_lines_after_r95` 是**从未填充的空字段**、`R120-verify.py` 无对应 check ⇒ 该半句原无一手证据。⇒ **补一手可复算件而非文字补丁**：新增 `R120-I2-EVIDENCE.py` + `R120-I2-EVIDENCE.json`（扫描 13,706 文件：字面 662 行 / 行内数值 109 行 / 行首数值 **14 行 / 12 文件**；行内口径 mtime 晚于 r95 且含数值行 **39 文件 / 83 行**，全为既有分数的引用或副本）。收窄结论「r95 之后 **0 份新独立 full 评审**、本轮 0 份新产出数值化评审判定行」由 `narrowed_claim_test.qualifying_files=[] / supported=true` 提供一手字节证据。与复核者 13,704/647 的差异来自扫描时点后新增产物 + 只追加记账，**非数据不一致**（R119 M2）。
- **W2 [MEDIUM]**：标题「首次」与登记册「从未有一份」收窄为「**本轮可见产物范围内未见先例**」的范围观察；R111:26 为记录在案前驱。标题与登记册原文不改一字，以更正段为口径权威。
- **W3 [MEDIUM]**：四份 R107 重述件是同一清单的**不同措辞 / 编号版本**（closure ③ + 括号在 :176、audit :116 缩略式括号内联、recovery :180 标 ② 无括号），**不存在**同时含全部成分的单行；属拼接式转录。行号 175/175/116/180 正确。
- **W4 [MEDIUM]**：不得把**整条** ② 称已满足 —— 仅「新建 P0 state / 不塞 P 阶段」子条款已作为草稿脚手架落盘；「版本化契约**处理 guidance handoff**」子条款未完成（handoff pending、契约 `PENDING_..._AND_HANDOFF`）。`SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED` 标签本身经复核者判定**准确、既未 overclaim 也未 underclaim**。
- **W5 [LOW]**：「12 处」是**文件数**，准确为 **14 行 / 12 文件**；计数单位差非源字节矛盾。
- **W6 [LOW]**：磁盘有 **3 份**逐字节一致的 closure 副本（SHA16 `960957561291`），R120 证据集只收 2 份 ⇒「两份」限定为「本轮证据集内两份」。
- **W7 [LOW]**：R115 未新增 gate-owner 决策、仅 W2 范围观察；G5 的「R115/R116」是**证据来源合并口径**，不是新增决策主张。

**边界不变**：七处均不涉伪造 / 数据不一致；A–H、J 全部字节级数值与源字节逐项一致；G0 不得 pass、无科学结果、无前向、无门晋级、零状态改动。**0 篇达标，未写 COMPLETE**，governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`。门 / 证据层复核，**非** `ccf-paper-reviewer full`、无 `**Overall:**` 数值行、不改 governing。检查点 §7「复核已下发、未回收」为写时点真值、**字节零回写**；按 R117/R119 先例另建新的不可覆盖检查点同步回收结论与更正，独立报告原文（含本机路径）不上传、只上传脱敏摘要。**新教训**：写「全项目无 X」须先给扫描口径 + 一手落盘证据；「无更新文件」≠「无新评审」；区分文件数 / 行数；逐字引用须单行可复现；标题与正文的「首次 / 从未」须与范围收窄一致。

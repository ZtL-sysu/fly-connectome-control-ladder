# R120 · 独立审查回收与只追加更正（报告原文零改动）

**状态：`POST_REVIEW_APPEND_ONLY_CORRECTION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`** · 2026-11-14 08:55 +0800

## 1. 独立报告身份与裁决（逐字据实）

- 文件：`reconciliation-R120/R120-INDEPENDENT-REVIEW.md`，**23,074 B**，SHA-256
  `c7c613c54bd08cad1b945c5affcdf371522430e63fff84d702ac86625cf3d9ea`，
  mtime `2026-11-14 08:55:00`，**单次写入、无中间态、原文零改动**。
- 复核者：全新隔离子代理 `general-purpose-1`，**未预付期望结论、未给分数锚点**；不读任何 R120 JSON 作为数据源，全部从原始源字节重算。
- 首行逐字：**`**Verdict:** REPRODUCIBLE_WITH_DEFECTS | **G0 may be passed:** NO | **Scientific result claimed:** NO`**；次行 **`**Forward pass performed:** NO`**。
- **12 组 claims**：A–H、J、L **MATCH**；**I、K MISMATCH**。
- **12 类点名 overclaim / 自认证 (a)–(l)：CONFIRMED = 0，REFUTED = 12**。
- **7 处瑕疵：1 HIGH / 3 MEDIUM / 3 LOW**；报告明确结论「**无编造、无数据不一致**」。
- 性质：门 / 证据层独立复核，**不是** `ccf-paper-reviewer full` 稿件评审；无 `**Overall:**` 数值评分行、无数值论文分、不改 governing。

## 2. 七处瑕疵全部接受、只追加更正

> 纪律：`R120-STANDING-INSTRUCTION-RECONCILIATION.md`、`R120-CONSOLIDATED-DECISION-REGISTER.md`、
> `R120-ROUND-AUDIT.md`、`R120-INDEPENDENT-REVIEW.md`、已发布检查点
> `20261114T004555Z-r120-reconciliation/` 及其 manifest / sanitized 摘要**原文一律零改动**；
> 所有收窄与更正只在本文件与后续追加段登记。

### W1 [HIGH｜范围过宽 + 一手证据缺口] — claim I-2 撤回

- **审查原文**：「no newer file with a real numeric `**Overall:**` line exists anywhere in the project」按字面文件存在性**不成立**；复核者扫描 13,704 文件 → 647 字面行 / 109 数值行 / 14 行首数值行（12 文件），且存在 mtime 晚于 r95 的文件含数值行（全部为既有分数的逐字引用 / 副本）。更关键：`R120-raw.py` 的 `numeric_overall_lines_after_r95: []` **从未被任何代码填充**，`R120-verify.py` **无对应 check** ⇒ 该半句在 R120 产物中**无 byte-anchored 一手证据**，是空字段断言。
- **判定**：**接受，撤回字面口径**。主项目账本 / 轮次审计中「全项目 `^\*\*Overall:\*\*\s*[0-9]` 真分数行 12 处均在历史报告…r95 之后 0 份新独立 full 评审」这一句，**「12 处」是文件数不是行数**（见 W5），且「无更晚文件含数值行」的字面读法不成立。
- **补一手可复算件（不是文字补丁）**：新增 `R120-I2-EVIDENCE.py` → `R120-I2-EVIDENCE.json`。本机 conda 重算（扫描 13,706 文件，`{md,txt,json,py}`、<3 MB、排除 `.git`）：**字面 662 行 / 行内数值 109 行 / 行首数值 14 行（12 文件）**；行首数值命中中 mtime 晚于 r95 者 **1 份**（`provenance/paper-null-ladder-r95-independent-review-20261111.md`，r95 逐字节副本）。另以行内口径复算：**mtime 晚于 r95 且含数值 `**Overall:**` 行的文件 39 份 / 83 行**（账本、automation memory、R101–R119 各轮审计、`R120-validator-out.json` D3 detail 等），**全部为既有分数的引用或副本，非新评审**。
- **收窄后的可支持表述**：`ccfa-review-reports/` 与 `ccfa-idea-review-reports/` 内 mtime 晚于 r95 且含行首数值判定行的文件数 = **0**；**r95 之后 0 份新独立 full 评审、本轮 0 份新产出的数值化评审判定行**。`R120-I2-EVIDENCE.json` 的 `narrowed_claim_test.qualifying_files=[]`、`supported=true` 为该收窄结论提供一手字节证据。
- **与复核者计数的差异如实登记**：复核者 13,704 / 647 / 109 / 14 / 12 文件；本轮 13,706 / 662 / 109 / 14 / 12 文件。差异来自**扫描时点**：独立复核后又落盘了 `R120-INDEPENDENT-REVIEW.md`、本更正件、`R120-I2-EVIDENCE.py/json` 等含 `**Overall:**` 字面串的新产物，且 `goal-ledger.md` / 各 memory 有只追加记账。**非伪造、非数据不一致**（R119 M2 快照时序口径）。

### W2 [MEDIUM｜历史否定须收窄] — claim K

- **审查原文**：报告标题「**首次**逐条字节对账」与决策登记册「**从未**有一份…合并清单」属未收窄的全称 / 历史否定，与正文 §0 / §4.9 已写下的「本轮可见产物中未见先例」范围收窄**自相矛盾**；R111:26 已是记录在案的前驱观察。复核者全项目扫描词汇频次**不能证明 119 轮中不存在**（缺席证据 ≠ 证据缺席）。
- **判定**：**接受**。两处措辞**收窄为**「**在本轮可见产物范围内未见先例**」的范围观察；「首次 / 从未」不作历史否定主张。标题与登记册原文**不改一字**，以本更正段为口径权威（R118 W6 / R119 L3 纪律）。本轮增量严格限定为：把常驻指令 ①②③ 量化到具体条目、产出 10 组去重决策登记册。

### W3 [MEDIUM｜拼接式转录] — claim A

- **审查原文**：claim 所引完整字串（同时含「处理 guidance handoff」与内联括号「（不往 guidance state 塞 P 阶段）」）**在四份重述件的任何单行都不存在**；closure 的括号在 L176（条目在 L175）、audit 为缩略式 L116（无「处理 guidance handoff」）、recovery L180（标 ②、含「处理 guidance handoff」但无括号）；条目编号 closure/audit 为 **③**、recovery 为 **②**。行号 175/175/116/180 本身正确。
- **判定**：**接受**。精确口径改为：四份重述件是**同一清单的不同措辞 / 不同编号版本**，逐字串分别锚定为 `R107-R1-R8-G0-CLOSURE-PACKAGE.md:175`（`③ U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state`，括号说明在 :176）、`R107-ROUND-AUDIT.md:116`（缩略式，括号内联）、`R107-INDEPENDENT-REVIEW-RECOVERY.md:180`（标 ②，无括号）；**不存在**同时含全部成分的单行。属拼接式转录，**非数据不一致**。

### W4 [MEDIUM｜措辞偏松] — claim D

- **审查原文**：把**整条** item ② 称「ALREADY SATISFIED」偏松，因为 ② 还含「版本化契约**处理 guidance handoff**」，而 main-line `handoff` 仍 `pending`、契约 `PENDING_..._AND_HANDOFF`；仅在「已建 state 脚手架」子条款下成立。复核者同时确认 `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED` 标签本身**准确、既未 overclaim 也未 underclaim**。
- **判定**：**接受**。精确口径：② 的**「新建 f-research-v1 P0 state（不往 guidance state 塞 P 阶段）」子条款**已作为 DRAFT 脚手架落盘；② 的**「版本化契约处理 guidance handoff」子条款未完成**（handoff pending、契约待 gate owner + handoff）。整条 ② **不得**称已满足。

### W5 [LOW｜计数单位] — claim I

- **审查原文**：正文「真分数行 **12 处**」实为 **14 行 / 12 个文件**（2 份 full-review 文件各含 2 行）；同一正则 `^\*\*Overall:\*\*\s*[0-9]`。
- **判定**：**接受**。准确为 **14 行、12 文件**；本轮 `R120-I2-EVIDENCE.json` 已记录 `numeric_line_start_lines=14` / `numeric_line_start_files=12`。**计数口径差，非源字节矛盾**。

### W6 [LOW｜副本计数范围] — claim A

- **审查原文**：claim 称「two R107 closure-package copies」，磁盘实际有 **3 份**字节完全相同的副本（main / isolated-post-review / isolated，均 SHA16 `960957561291`）；R120 证据集只收 2 份。
- **判定**：**接受**。准确为**磁盘 3 份逐字节一致副本**，R120 的 `SOURCES` 清单只纳入 2 份（main + isolated-post-review），属**证据集范围**而非磁盘全量；「两份」须限定为「本轮证据集内两份」。

### W7 [LOW｜范围表述差异] — claim J

- **审查原文**：claim 轮次枚举 R114/R116/R117/R118/R119 正确排除 R115（复核者另核 R115 无 gate-owner 决策）；但决策登记册 G5 把「R115/R116」并为一组（W2 范围收窄），存在轻微范围表述差异，不影响任何锚点 MATCH。
- **判定**：**接受**。准确口径：R115 未新增须 designated gate owner 的决策，仅产出 W2 范围观察；G5 的「R115/R116」为**证据来源合并口径**（R115 提供 W2 边界、R116 提供三项 gap 1 锚点），**不是**「R115 新增决策」的主张。

## 3. 更正后的边界（不变）

七处均**不涉及伪造或数据不一致**；A–H、J 的全部字节级数值（行号、字节数、SHA、阶段状态、判据文本、D1–D5 布尔值、S1–S7 计数、门读数）与原始源字节逐项一致。核心结论不变：**G0 不得 pass、无科学结果、无前向、无门晋级、 governing 仍 R95 = 6.0 / Confidence 4.0、`NOT_QUALIFIED` / `INCOMPLETE`、0 篇达标、未写 COMPLETE**。

## 4. 与已发布检查点的关系

检查点 `20261114T004555Z-r120-reconciliation/` 在写时点如实标注「独立复核已下发、未回收、不宣称结论」⇒ **标注为真、字节零回写**。按 R117 / R119 先例，本回收结论与七处只追加更正另建**新的不可覆盖检查点**同步；独立报告原文含本机绝对路径，**不上传**，只上传脱敏摘要。

## 5. 新教训（交下轮）

① 写「全项目无 X」必须先给出**扫描口径 + 一手落盘证据**，空字段断言视为无证据；②「无更新文件」与「无新评审」是**两个不同命题**，引用 / 副本不构成新评审但构成字面反例；③「12 文件 / 14 行」须区分计数单位；④ 逐字引用必须单行可复现，跨行拼接须显式标注；⑤ 标题与正文的「首次 / 从未」必须与范围收窄一致，避免内部口径矛盾（R119 L3 再确认）。

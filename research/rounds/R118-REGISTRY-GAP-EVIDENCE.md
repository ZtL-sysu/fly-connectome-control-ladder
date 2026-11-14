# R118 — 一手来源登记缺口可复算清点（只读证据报告）

**性质**：`READONLY_REGISTRY_GAP_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
**网络请求**：0（全部从本机磁盘原始字节复算；无新抓取、无时点污染）
**回写**：0（`literature-search/source-manifest.json`、`literature-baseline-matrix.md`、主线 `pipeline-state.json` 及任何评审/分数/阈值/稿件/门配置字节均未改动）
**执行环境**：`/Users/<local>/miniconda3/bin/python`（本机 conda）

---

## 1. 本轮换道理由（RGE4）

R114–R116 把「不需批准的一手许可 / 归档内容取证」通道走到尽头，R116 独立审查把 gap 1 剩余三项判给 designated gate owner；R117 做了 P3 执行前提首次实测冻结，交下轮点名三项 P3 前置须 gate owner 书面冻结。R111「自主可达动作穷尽」的 5 个决策点仍待答复，R105/R107/R109 已三次判停「继续产出证据文档」的同构循环。

本轮不写第 N 份 G0 文字补丁、不重开探针/守卫补丁循环、不执行任何须批准的机器门修复。改做一件**逐字点名、不需批准、纯只读、可复算**的欠账：R107 **独立 gate review** 明确登记的两个缺口，跨 R107→R117 共 11 轮从未被量化——

- **W7 / R4 = PARTIAL**：R106 §6 R4 要求「为 `arXiv:2609.24565v2` 保存本地带 SHA 的一手冻结件并**登记进 `literature-search/source-manifest.json`**」。R107 确已冻结 5 份 Kuklev 字节（本轮复算 5/5 SHA 与 `R107-ONEHAND-SOURCE-MANIFEST.json` 声明吻合），但**指定登记未做**：本轮实测该 registry 仍 1124 B / `541880ab…` / 5 条 / 无 `2609.24565`，与 R107 独立审查记录逐字一致 ⇒ **11 轮零改动，缺口仍在**。
- **R98「23 saved public sources」vs manifest 5 条**的矛盾持续（R107 独立审查 W7 原话），从未给出过可复算的分解。

## 2. 实测读数（从原始字节，非引用旧结论）

| 项 | 值 |
|:--|:--|
| `literature-search/` 全部文件 | **167** |
| 按后缀规则的一手**候选** | **26** |
| 其中登记进 registry | **5** |
| 未登记 | **21** |
| 项目自有产物（py/png/npz/npy/ipynb/zip/md/json） | **141** |
| 候选分类 | EXTERNAL_FIRSTHAND_PAGE **13** / DERIVED_TEXT **7** / NEGATIVE_OR_ERROR_PAGE **3** / UNCLASSIFIED_NEEDS_OWNER_JUDGMENT **3**（均为 PDF，本脚本不做 PDF 文本抽取） |
| registry 5 条声明 bytes+SHA 与磁盘 | **10/10 吻合** |
| Kuklev 冻结件（R107 目录） | **5** 份，5/5 SHA 与 R107 声明吻合 |
| 总检查项 | **50**，MISMATCH **0**（另有 5 项 `PROBED`、1 项 `REGISTERED` 状态项，非 MATCH/MISMATCH 判定） |

**关键边界**：26 是「按后缀筛出的候选」，**不等于 26 份已核验一手来源**；13 是脚本按文本特征分类，3 份 PDF 明确留给 owner 判断。R98 的「23」与任何单一口径都不相等，本轮只做分解登记，**不宣称 23 被证实或被证伪**。

## 3. 本轮全新一手发现：字节完整 ≠ 内容有效

`registry` 第 5 条 `flyvis2024`（声明 `21444 B / ec7eb823…615`）与磁盘字节 **SHA/bytes 完全吻合**，但其纯文本仅 **165 字符**，逐字为 `Checking your browser - reCAPTCHA Checking your browser before accessing pmc.ncbi.nlm.nih.gov ...`，**无 Abstract、无正文** ⇒ 是 **CAPTCHA 挑战页**，不是有效一手文献内容。

R98 原文只写「the failed `flyvis2024.txt` CAPTCHA response is retained and excluded as evidence」——排除的是 `.txt`（本轮复算 17774 B / 8148 字符，含 `RecaptchaChallengePageUi`），而**被登记进 registry 的 `.html` 同为挑战页却未被排除**。即：5 条登记中 SHA 完整 5/5，但按内容有效性只有 4 条可用。

**防夸大**：这是「登记条目内容有效性」的一次内容探针，不是「FlyVis 一手文献缺失」的结论——`flyvis2024-primary.xml`（443143 B）与 `flyvis2024-primary-body.txt`（125982 B）作为 EuropePMC 正文均在本目录，R106 已独立复算过。本轮不改写 registry、不删除该条、不把它说成 gap 闭合或科学结果。

## 4. Kuklev v2 两个措辞不同摘要的逐字冻结（R106 §6 R2）

从 R107 冻结字节直接抽取，无网络请求：

| 来源 | 摘要长度 | 收束句（逐字） |
|:--|--:|:--|
| `/abs/2609.24565` 元数据摘要（`kuklev_abs_latest.html`，与 `kuklev_abs_v2.html` **逐字相同**，1544 字符） | 1544 | `Longer observations reverse the circuit-receptor ordering once the stimulus spans a period, but not through T4/T5.` |
| `/html/2609.24565v2` 论文正文 Abstract 块 | 1943 | `Exact structure remains insufficient to beat what the moving retina already provides.` |
| v1 `/abs/2609.24565v1` 摘要 | 1443 | `while the topology contribution and end-to-end BIM utility remain open questions.` |

**澄清（避免 R114/R115 被撤回过的「首次」夸大）**：R107 已做过这批字节的逐字段复算并写入 `literature-baseline-matrix-R107-final.md` 与 `R107-INDEPENDENT-GATE-REVIEW.md`。**本轮不是首次复算**；本轮的增量是把上述三份摘要的**长度、逐字收束句、abs/latest 与 abs/v2 相等**做成独立可复算的字段级读数，并纳入 §2 的登记缺口清点。

§7.3 / §8 / §9 的 12 个关键断言（`What the sampling sweep answered`、`That prediction was run, and it half held.`、`Two gaps remain.`、`which stage integrates the extra time`、`per-type tuning analysis over the sweep`、`+ 0.033 [ 0.015 , 0.050 ]`、`T4/T5 contribution does not grow with length`、`7.3 The stimulus never completes a cycle`、`9 Limitations` 等）在本轮 50 项检查中 **12/12 FOUND**，全部命中冻结原始字节。

## 5. gap 2 仍未闭合（如实登记）

规范矩阵 `literature-baseline-matrix.md` 实测 **9445 B / `31b5098b…a9b2`**，与 R106 freeze 声明**字节一致** ⇒ 零静默回写；第 46–47 行仍逐字含 `the open question` + `Kuklev leaves`，正是 R106 §6 R2 要求删除、R107 独立审查判 gap 2 OPEN 的 stale 表述。R107 的 `…R107-final.md` 是 `G0_EVIDENCE_DRAFT`（草案、未签署），不构成 final map。

⇒ **gap 2 维持 OPEN**；本轮不写矩阵、不定稿、不重新冻结 SHA、不自我认证。

## 6. 双门只读（本轮实跑，报告写 /tmp）

| 门 | 读数 |
|:--|:--|
| validator | `NOT_QUALIFIED` / governing **6.0** / threshold **7.0** / operator `>=` / `score_meets_threshold=false`；**D1✓ D2✗ D3✗ D4✓ D5✗**（D2 13 个 P9–P21 未过、D5 `claim_evidence_matrix=False`） |
| guard | `EXIT=1 / INCOMPLETE`；7 交付物全 PASS，失败恰 **A2、A6**；S1–S7 全 pending、动作序列 0 条。A6 报告文本仍 ledger 口径「严格 > 8.0」= R109/R111 已登记双口径已知问题，**只读登记不改** |
| 零写回 | `guard/ledger-null-ladder.json` SHA16 `73043b4e164a5a5f` + mtime `1794528560.4745793`、主线 `pipeline-state.json` SHA16 `bcb48bb964e657a4` / 3723 B **前后完全一致**；G0 及 G1–G8/validation/handoff 全 `pending` |

## 7. 严格边界

全轮 `READONLY_REGISTRY_GAP_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`。

- **EXEC LOCK**：零前向 / 零推理 / 零训练 / 零标签 / 零数据集数组 / 零 EPE·l2 / 零科学指标；未加载任何权重，未实例化任何 npz。
- **零门晋级 / 零自我认证 / 零状态改动**：未改历史字节、评审、分数、阈值、稿件、门、冻结件、矩阵、判据登记、门配置、`source-manifest.json`。
- 未起 `ccf-paper-reviewer full`、未产生 `**Overall:**` 行、未自评 governing、未跳门、未对未修改稿件重复评审；未重开 D1/v3、未出 predictor v4、**未假定 `≤32h / K=45` confirmation 授权**；与 harbor 25092 工程 reward 无关、无 4090/L4/H20 能力主张。
- 主项目未投稿 / commit / push；心跳 ACTIVE 调度 `FREQ=HOURLY;INTERVAL=1;BYMINUTE=0,30` 无变化。
- **不宣称**：gap 1/2/4 闭合、G0 passed、任何 stage 状态变更、registry 已登记、矩阵定稿、新科学结果、独立 full 评审、数值论文分、confirmation 授权。

## 8. 可复算性

`gate-G0-R118/`：`R118-manifest.py`（清点生成）、`R118-verify.py`（**不读** manifest 产物，从磁盘原始字节重算）、`R118-SOURCE-MANIFEST.json`、`R118-REGISTRY-GAP-VERIFICATION.json`、`.v1-superseded.json`（v1 假阴性留痕，保留不改）、`R118-REGISTRY-GAP-EVIDENCE.md`、`R118-ROUND-AUDIT.md`。

**独立性如实声明**：两份脚本同机、同 `hashlib`、同数据源，一致只是必然的一致性核对，**不构成独立交叉核验**（R115 W4 / R114 D1）。真正的独立复算由全新隔离子代理另行从磁盘重算。

**v1 → v2 更正（只追加、v1 原字节保留）**：v1 把 `flyvis2024.html` 因出现 `captcha` 判为负面件、`an_donggyu_2026.html.html` 因页脚一处 `captcha` 误判负面件、`costabile-etal-2023.html`（Client Challenge）判为未分类。逐条复核字节后确认：前者**确为** CAPTCHA 挑战页（结论对、理由糙），后两者为**关键词过宽的脚本判定缺陷**。v2 改为「挑战页签名 + 短纯文本」双条件，并新增 5 条 registry 条目的内容有效性探针。v1 完整留痕 `R118-REGISTRY-GAP-VERIFICATION.v1-superseded.json`（17627 B / `5f44c8e4…57fe`），两版读数都保留。按 R116 纪律：**这是主会话脚本判定缺陷，不是数据不一致**。

---

## 9（只追加，独立审查后更正索引 — 历史正文零改写）

全新隔离独立审查 `R118-INDEPENDENT-REVIEW.md` 最终 **23653 B / `3ffc37c9fe71ad8daeb677d62bfafd9dd789d4220a93cd1c7d5643fa0d2d7bc7`**，首行 `REPRODUCIBLE_WITH_WORDING_AND_JUDGMENT_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO`。168 项读数全部可复现吻合、12 类点名夸大 (a)–(l) 全部 REFUTED、无 [高] 级瑕疵；发现 **9 处瑕疵（3 中 / 6 低）全部接受**，详见 `R118-POST-REVIEW-CORRECTION.md`。

本文件上方历史正文**不改写**，仅在此登记对阅读结论有影响的收窄：

- **W1（撤回字段定性）**：§4 表格列名「收束句（逐字）」不成立 —— v2 abs 行给的是**倒数第二句**，v1 行给的是**末句后半从句**，只有正文行是完整末句。三句统一改称「关键判断句／该摘要中的逐字字段」。三句本身逐字为真、3/3 从字节复核命中。
- **W2（实质措辞撤回）**：§4「12 个关键断言 12/12 FOUND，**全部命中冻结原始字节**」不成立。准确为：12 项中 **2 项是摘要关键判断句、10 项才是 §7.3/§8/§9 短语**；在**重建纯文本**口径 12/12 FOUND，在**原始字节精确子串**口径该 10 项为 **6 FOUND / 4 ABSENT**（`+ 0.033`、`[ 0.015 , 0.050 ]`、`7.3 The stimulus never completes a cycle`、`9 Limitations` 被 MathML 标签/特殊空格分隔）。短语真实存在于论文正文，只是不以带空格连续串形式存在于原始字节 ⇒ **搜索口径缺陷，非数据不一致、非编造**。
- **W3**：§4 三个摘要长度 **1544 / 1443 / 1943** 是三种口径（前两者含 `Abstract: ` descriptor 各 +10，纯摘要 1534 / 1433；后者为去前缀去 `Keywords.` 尾的核心段，完整块 2069），**不可直接横向比较**，数值本身不作废。
- **W4**：§3 `flyvis2024.html` 的「逐字」引用以 `...` 省略了后半句 `Click here if you are not automatically redirected after 5 seconds.`；165 字符数正确，引用不完整在此补全。
- **W5**：§2 的 13 / 7 / 3 / 3 是脚本**内容启发式分类**，与 26 的**后缀候选计数**是两套口径；13 不是另一组已核验来源数。
- **W6（撤回措辞）**：§3 标题「本轮**全新一手发现**」带首次色彩 ⇒ 改称「**本轮增量观察**」。R98 已记载并排除 `flyvis2024.txt` CAPTCHA，本轮增量仅是「被登记的 `.html` 同为挑战页却未被排除」。发现本身成立且被独立复现。
- **W7（边界收窄）**：本文各处「零回写 / 纯只读」精确为「**对项目既有字节零回写**」；validator / guard 实跑报告写在项目外 `/tmp`，**不能从本目录字节独立复算**，独立审查未重跑双门 ⇒ 双门读数是主会话实跑读数，不宣称已被独立复核。
- **W8**：「50 项 MISMATCH 0」是脚本自定口径，**不等于全绿**；其中 5 项 `PROBED`，`REG-5-flyvis2024-content-validity` 观测为 `CHALLENGE_PAGE`（即「5 条中按内容有效性只有 4 条可用」同一事实）。
- **W9**：R98「23」改述为「**本轮未找到能复现 23 的单一口径，故不作证实或证伪**」，不把「未能复现」表述为否定性判定。

状态重判：G0 维持 `pending`、gap 1/2/4 未闭合、不构成实质正向新科学证据、非独立 full 稿件评审、governing 仍 6.0。独立报告原文零改动、v1 留痕与全部脚本/JSON 原字节保留不改。

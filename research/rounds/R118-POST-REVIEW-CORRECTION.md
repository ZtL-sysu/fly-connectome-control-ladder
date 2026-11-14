# R118 独立审查后更正登记（只追加 · 历史正文与独立报告原文零改动）

**独立报告**：`R118-INDEPENDENT-REVIEW.md`，最终落盘 **23653 B / SHA256 `3ffc37c9fe71ad8daeb677d62bfafd9dd789d4220a93cd1c7d5643fa0d2d7bc7`**，mtime `2026-11-14 05:16:51`，**无中间态、原文零改动**（子代理交付读数与磁盘最终态一致；R115 中间态/最终态教训已核对）。
**首行**：`**Verdict:** REPRODUCIBLE_WITH_WORDING_AND_JUDGMENT_DEFECTS | **G0 may be passed:** NO | **Scientific result claimed:** NO`；次行 `**Forward pass performed:** NO`。
**性质**：门 / 证据层复核，**不是** `ccf-paper-reviewer full` 稿件评审；无数值论文分、无 `**Overall:**` 行、不改 governing。

**独立复核结论**：168 项读数全部可复现吻合；点名的 **12 类夸大与自我认证 (a)–(l) 逐条全部 REFUTED**；核心数字（167 / 26 / 5 / 21 / 141 / 10-10 / 5-5 / 50 项 0 mismatch、flyvis2024 挑战页、matrix 与 pipeline-state SHA 及全 pending 状态）全部吻合；**无 [高] 级瑕疵**，未发现核心数字造假或任何既有文件被改动。报告发现 **9 处瑕疵（3 中 / 6 低）**，主会话**全部接受**，逐条只追加更正如下。

---

## W1 [中｜实质措辞撤回] 「收束句」字段定性错误、三行口径不统一

**撤回** `R118-REGISTRY-GAP-EVIDENCE.md` §4 表格列名「收束句（逐字）」及表格本行的定性。三行所给句子并非同一位置：

| 行 | 原登记内容 | 独立复核后的准确说法 |
|:--|:--|:--|
| v2 abs 元数据（含 descriptor 1544 字符） | `Longer observations reverse … but not through T4/T5.` | 这是**倒数第二句**；真末句为 `Thus active sampling and exact structure matter, while clean-data practical performance remains dominated by task-trained networks and the useful transfer margin is largely retinal.` |
| v2 正文 Abstract（1943 核心段） | `Exact structure remains insufficient to beat what the moving retina already provides.` | 是**完整末句** ✓ |
| v1 abs（含 descriptor 1443 字符） | `while the topology contribution and end-to-end BIM utility remain open questions.` | 是**末句的后半从句**，非完整末句 |

源头在 `R118-verify.py` 的 `V2-abs-metadata-closing` 检查用 `Longer observations…` 前缀命名 `closing`，字段名误导。⇒ 三句统一改称 **「关键判断句 / 该摘要中的逐字字段」**，不称「收束句」；**被引句子本身逐字为真**（本轮已从磁盘字节复核 3/3 命中），撤回的只是字段定性与「收束句」标签。原脚本与原报告字节保留不改。

## W2 [中｜实质措辞撤回] 「全部命中冻结原始字节」不成立

**撤回** `R118-REGISTRY-GAP-EVIDENCE.md` §4 「§7.3 / §8 / §9 的 12 个关键断言 … **12/12 FOUND**，全部命中冻结原始字节」及 `R118-verify.py` 中 12 项 `verbatim_field` 的 note `searched in frozen raw bytes only`。

主会话独立复核（同独立审查 §6 两口径）确认：以 **A = 原始字节精确子串** / **B = 去标签重建纯文本** 分别判定 §7.3/§8/§9 的 10 个短语：

| 口径 | 结果 |
|:--|:--|
| **B 重建纯文本** | **10/10 FOUND**（`R118-verify.py` 的 `t_body` 即此口径） |
| **A 原始字节** | **6 FOUND / 4 ABSENT** |

4 个 ABSENT 为 `+ 0.033`、`[ 0.015 , 0.050 ]`、`7.3 The stimulus never completes a cycle`、`9 Limitations`；字节原因是它们被 MathML 标签 / 实体 / 特殊空格（U+2002/U+2006）分隔，带空格的连续串只在去标签重建后成形。**它们真实存在于论文正文，但不以该逐字形式存在于原始字节**。

另需更正计数口径：12 项 `verbatim_field` 中 **2 项是摘要关键判断句**（在 `a_abs` / `a_body` 重建文本中搜索），**10 项才是 §7.3/§8/§9 短语**；原报告写成「§7.3/§8/§9 的 12 个断言」不准确。

⇒ 准确表述：**「12 项逐字字段在重建纯文本口径 12/12 FOUND；其中 10 项 §7.3/§8/§9 短语在原始字节口径 6 FOUND / 4 ABSENT」**。**这是措辞与搜索口径的缺陷，不是数据不一致、不是编造**；独立审查逐字确认这些短语真实存在于论文正文。原 JSON 与脚本字节保留不改。

## W3 [中｜口径标注] 摘要长度三种口径混用并列同表

接受。§4 表格的 **1544 / 1443** 含 arXiv abs 页 `Abstract: ` descriptor 前缀（各 +10；纯摘要为 **1534 / 1433**）；**1943** 是 v2 正文 Abstract 去 `Abstract. ` 前缀、去 `Keywords.` 尾的**核心段**（含前缀+关键词的完整块为 **2069**）。三者不同口径并列未标注 ⇒ 追加标注「长度不可直接横向比较」，**原数值不作废**（均为各自口径下的真实读数）。

## W4 [低｜引用完整性] `flyvis2024.html` 「逐字」引用被截断

接受。§3 用 `...` 省略了真实存在的后半句 `Click here if you are not automatically redirected after 5 seconds.`。165 字符数正确，但「逐字」表述不完整 ⇒ 补全为：纯文本 165 字符，逐字为 `Checking your browser - reCAPTCHA Checking your browser before accessing pmc.ncbi.nlm.nih.gov ... Click here if you are not automatically redirected after 5 seconds.`（独立审查已给出全文）。

## W5 [低｜口径区分] 候选分类两套口径未显式区分

接受。§2 的 **13 / 7 / 3 / 3** 是 `R118-verify.py` 按文本特征的**内容启发式分类**；**26** 是按后缀筛出的**候选总数**；独立审查另有自己的后缀/目录分类。三者是不同口径 ⇒ 追加声明「13 不是另一组已核验来源数」，与 §2 已有「26 不等于 26 份已核验一手来源」的边界一致。

## W6 [低｜措辞收窄] 「本轮全新一手发现」带首次色彩

接受并**撤回该措辞**。R98 L21 已记载 `flyvis2024.txt` CAPTCHA 响应并排除；本轮增量**仅是**发现「被登记进 registry 的 `.html` 同为挑战页却未被排除」，以及给出该条目的逐字内容探针。⇒ 改称 **「本轮增量观察」**，`gate-G0-R118/` 内所有「全新一手发现」字样按此收窄理解。发现本身（SHA 完整但内容为 CAPTCHA 页）成立，独立审查 §7 独立复现。

## W7 [低｜边界收窄] 「纯只读零回写」应限定范围

接受。「零回写 / 纯只读」精确含义为 **「对项目既有字节零回写」**：本轮确曾实跑 validator / guard，报告写入项目外 `/tmp/r118_validator.json`、`/tmp/r118_guard_report.md`（`guard` 用 `--no-report`）；这些动作**无法从 `gate-G0-R118/` 目录字节独立复算**，独立审查遵守约束未重跑双门。⇒ 双门读数登记为**主会话实跑读数**，不宣称已被独立复核；项目内既有文件零改动由独立审查从 SHA 独立确认。

## W8 [低｜读数口径] 「50 项 MISMATCH 0」易被读成全绿

接受。50 项中含 **5 项 `PROBED`**（内容有效性探针）与 **1 项 `REGISTERED`**（本机路径登记），均非 MATCH/MISMATCH 判定；其中 `REG-5-flyvis2024-content-validity` 观测为 **`CHALLENGE_PAGE`**，即与「5 条中按内容有效性只有 4 条可用」是同一事实。⇒ 「0 mismatch」是脚本自定判定口径，**不等于所有检查无异常**；该异常已在 §3 明确登记。

## W9 [低｜措辞自洽] R98「23」与「不宣称证实或证伪」略有张力

接受。⇒ 改述为 **「本轮未找到能复现 23 的单一口径，故不作证实或证伪」**；不把「未能复现」表述为对 23 的否定性判定。R98 原文 `23 saved public sources` 逐字存在（独立审查 §7 复核），本轮只做分解登记。

---

## 状态重判（以独立审查为准）

- **G0 不得 pass、维持 `pending`**；gap 1 / 2 / 4 均未闭合，registry 指定登记仍缺、矩阵未定稿。
- 本轮**不构成实质正向新科学证据**、不构成独立 `ccf-paper-reviewer full` 稿件评审、不改 governing（仍 R95 = 6.0）。
- 9 处瑕疵**均不涉及伪造、不涉及数据不一致、不改变核心清点数字**；独立报告逐字写明「未发现核心数字造假、未发现 12 项夸大中任何一项被坐实、未发现任何既有文件被改动」。
- 更正纪律：`R118-POST-REVIEW-CORRECTION.md` 为**新增只追加**文件；`R118-REGISTRY-GAP-EVIDENCE.md`、`R118-ROUND-AUDIT.md` 各**只追加**一段更正索引，历史正文零改写；独立报告 `R118-INDEPENDENT-REVIEW.md` **原文零改动**；v1 留痕、两版 verification、全部脚本与 JSON **原字节保留不改**。
- 公开同步仓库只上传**脱敏摘要**，且按 W1/W2/W6/W7/W9 的最终口径撰写，不含本机绝对路径、不含凭证、不含数值论文分、不含 `**Overall:**` 字面串。

## 并发条件

审查窗口内主会话未写入 `gate-G0-R118/` 内任何既有文件；独立报告由子代理单独新建。子代理自报 `SendMessage` 因「不在团队上下文」失败，其 5 项交付信息（路径 / bytes / SHA / 首行 verdict / 瑕疵数）以内联方式返回，**与磁盘最终态一致**，未采信任何主会话预期结论。按 R106 §6 R9，主会话自我更正**不构成** gap 闭合的自我认证。

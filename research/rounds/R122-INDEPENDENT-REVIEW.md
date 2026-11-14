REPRODUCIBLE_WITH_DEFECTS

**G0 may be passed:** NO
**Scientific result claimed:** NO
**Forward pass performed:** NO

# R122 全新隔离独立复核报告

## 0. 复核元信息与方法声明

- 复核者：`r122-independent-reviewer`，全新隔离上下文，未参与 R122 采集/审计，未事先见到任何结论或分数锚点。
- 复核对象目录 A：`.../first-hand-R122/`；本报告为唯一新增产物，不修改任何既有文件，不写轮次审计/账本/状态/门文件，不执行任何 git/推送操作。
- **严格顺序已遵守**：第 1 步只读取 `raw/` 下 5 份原始字节，用本人自写解析脚本（`/tmp/r122_independent.py`，仅调用通用库 `lxml`/标准库 `re`/`hashlib`/`difflib`/`html`）独立重算 A–F；**未** `import` 目录内 `R122-ACQUIRE.py` / `R122-verify.py`，**未**把任何 R122 JSON 当作数据源，**未**把 `R122-v2-PLAINTEXT.txt` / `R122-v2-BODY-ABSTRACT.txt` 当作第 1 步数据源。第 2 步才读 `R122-ROUND-AUDIT.md`、`R122-VERIFICATION.json`、`R122-SOURCE-MANIFEST.json` 并逐条对照。
- 第 2 步以后，为核对报告「逐字引用/派生件字符数」的口径，仅对派生 txt 做过**只读**的字符数与上下文查看，用于解释口径差异，不回填为第 1 步 A–F 的数据源。
- 报告内不出现任何期望分数或分数锚点；涉及 governing/达标处只作定性表述。

---

## 1. 第 1 步：仅用 5 份原始字节的独立重算数值（我的数值）

### A. 5 份原始文件 bytes / sha256 / 合法 / 非空

自写解析：`hashlib.sha256(bytes)`；XML 合法性用 `lxml.etree.fromstring` 严格解析；HTML 合法性用 `lxml.html.fromstring` 解析并检查根节点为 `html` 且含 `head`/`body`（HTML5 非 XML，严格 XML 良构性另记）。

| 文件 | bytes | sha256 | 合法 | 非空 |
|:--|--:|:--|:--|:--|
| `arxiv-2609.24565-api.xml` | 3139 | `5e1c68e2e21be996a3d2244d67b2d1c0e7a6e5c8a7d829657d7faa3f2341377d` | 是（严格 XML 解析通过） | 是 |
| `arxiv-2609.24565v1-abs.html` | 41581 | `0075412eb10447864bb2b139c6d8ec8eb1c8f256b2d91e69a913203027bbd367` | 是（可解析、结构完整） | 是 |
| `arxiv-2609.24565v1-html.html` | 50485 | `2726ef63d6cda79393d1faa725267cb1ede474f1189caba51cc583c9a4af648c` | 是 | 是 |
| `arxiv-2609.24565v2-abs.html` | 43656 | `cbcbce7343f999ebae1f63c43963a477e96ebe827679b6f973e25e177ca7029e` | 是 | 是 |
| `arxiv-2609.24565v2-html.html` | 182710 | `f4e7fb8747165a4f4caf0a50e34ca15f7a837536699189bffe267502ca12e7ad` | 是 | 是 |

补充口径：4 份 HTML 的 `strict_xml_wellformed=False`（HTML5 含未转义实体/空元素，非 XML 良构），这不影响「合法 HTML」判定，属预期，非缺陷。5 份全部非空。

### B. v1/v2 abs 页 citation_title / citation_date

- v1 `citation_title`：`Active Visual Sampling with a Connectome-Constrained Fly Model for One-Shot Hatch Recognition in Architectural Drawings`
- v2 `citation_title`：`What Survives on Real Drawings: Active Sampling, Connectome Wiring, and Matched Baselines in Architectural Document Vision`
- 两标题是否不同：**是**（完全不同）。
- v1 `citation_date` = `2026/09/21`；v2 `citation_date` = `2026/09/21`；两日期是否相同：**是**（均为 v1 首次提交日）。
- 补充观察：`citation_online_date` v1=`2026/09/21`、v2=`2026/09/22`（修订上线日不同，但 `citation_date` 字段本身相同）。

### C. atom API 字段与 feed/entry 时间区分

- feed-level `updated` = `2026-11-14T03:57:55Z`。
- entry-level `id` = `http://arxiv.org/abs/2609.24565v2`。
- entry-level `title` = `What Survives on Real Drawings: Active Sampling, Connectome Wiring, and Matched Baselines in Architectural Document Vision`（与 v2 `citation_title` 逐字相等）。
- entry-level `published` = `2026-09-21T13:30:30Z`（v1 版本时间）。
- entry-level `updated` = `2026-09-22T12:24:47Z`（v2 版本时间）。
- entry-level `summary` = 1534 字符，与 v2 abs 摘要逐字相等（见 D）。
- **关键判定**：feed-level `updated` **不是**论文版本更新时间。该值是 feed 根元素（`<title>arXiv Query: ...</title>`、`<id>https://arxiv.org/api/j7NWbCIc0oQzxwelAkVp7SH/QD4</id>` 表明这是一次 API 查询结果）的响应生成/查询时刻；论文版本时间由 entry-level `published`（v1=2026-09-21）与 `updated`（v2=2026-09-22）给出。audit 报告 §4.1 的 `Submission history`（`Mon, 21 Sep 2026 13:30:30 UTC` / `Tue, 22 Sep 2026 12:24:47 UTC`，我在 `arxiv-2609.24565v2-abs.html:161-164` 复见）与 entry 时刻吻合。把 feed-level `2026-11-14T03:57:55Z` 当作版本时间即「查询时刻 ↔ 版本时间」时点混用。

### D. 三份摘要的逐字关系、字符数、相似度、差异块

提取口径：v2 abs 摘要取 `citation_abstract` meta（并与 `<blockquote class="abstract mathjax">` 文本核对，二者 1534 字符、归一后相等）；atom summary 取 `<summary>` 文本；v2 HTML 正文内嵌摘要取 `id="p2.1"` 的 `ltx_p` 块，跳过 `Abstract.` 标签、行内 `<math>` 用其 `alttext`（`46\times`）渲染、空白归一。

- v2 abs 页摘要：**1534 字符**（meta 与 blockquote 一致）。
- atom summary：**1534 字符**。
- v2 HTML 正文内嵌摘要：**1938 字符**。
- 逐字关系：
  - v2 abs 摘要 ≡ atom summary：**逐字相等**（我另用原始字节直接 `==` 校验为真，两者均 1534 字符，尾部同为 `...the useful transfer margin is largely retinal.`）。
  - v2 正文内嵌摘要 ≠ v2 abs 摘要；≠ atom summary：开头为 `A connectome-constrained model ... over a drawing by prescribed motion ... We test what that buys ...`，收尾为 `Exact structure remains insufficient to beat what the moving retina already provides.`，措辞与 abs/atom 版显著不同。
- `difflib.SequenceMatcher(None, v2_abs_abstract, v2_body_abstract).ratio()` = **0.4724**（总 opcodes 76，其中非 `equal` 的差异块 **38**）。
- v1 abs 摘要：**1433 字符**。与 v2 三份来源（abs 页 / atom / 正文内嵌）**均不相同**（`v1_eq_v2_abs=False`、`v1_eq_atom=False`、`v1_eq_v2_body=False`）。
- 因此 v2 至少存在 **两份措辞不同的官方摘要**（abs/atom 版为同一份、正文内嵌版为另一份）；v1 与 v2 摘要亦非同一份。

### E. v2 正文（去标签纯文本）子串、时间尺度 sweep、§8、章节与字节比较

去标签纯文本口径：删 `script`/`style`，`text_content()`，`html.unescape`，`\s+` 折叠为单空格。v2 = **45430 字符**，v1 = **12910 字符**。计数含 HTML 内 TOC 导航条目（如 `<li class="ltx_tocentry">` 的链接文字）与正文标题各一次。

| 逐字子串 | 出现次数 | 是否存在 |
|:--|--:|:--|
| `7.3 The stimulus never completes a cycle` | 2 | 是 |
| `What the sampling sweep answered` | 2 | 是 |
| `What remains open` | 2 | 是 |
| `Two gaps remain.` | 1 | 是 |
| `+0.033` | 4 | 是 |
| `[0.015,0.050]` | 4 | 是 |
| `T4/T5` | 4 | 是 |
| `0.271` | 3 | 是 |
| `0.356` | 3 | 是 |
| `721` | 5 | 是 |
| `1,876` | 5 | 是 |
| `0.505` | 2 | 是 |
| `0.415` | 3 | 是 |
| `9 Limitations` | 2 | 是 |

- 口径说明（见 §2）：`7.3 The stimulus never completes a cycle`、`9 Limitations` 两个标题在原始字节中编号与标题之间用 U+2002/U+2006 等 Unicode 空格，严格逐字（ASCII 单空格）在原始字节里为 **0 次**；经空白归一后才分别匹配 2 次。`Two gaps remain.` 为普通 ASCII，原始字节逐字即 1 次。
- **时间尺度 sweep 结论是否在 v2 正文：是**。§7.3 `The stimulus never completes a cycle` 含 8 帧仅覆盖约 1/5–9/10 空间周期、观测窗 0.16 s 短于一个周期、长看变体 40 帧得 0.826 vs 0.871；并给出 sweep 结论：随观测超过单个周期电路–受体排序反转、`+0.033 [0.015,0.050]`。§8 `What the sampling sweep answered` 以 `...the circuit does overtake the receptors-only descriptor once the observation passes a single period, by +0.033 [0.015,0.050] ...` 复述。补充：摘要中的措辞 `spans a period` **未**进入正文（正文用 `passes a single period` / `past a single period`），我独立查得 `spans a period` 在 v2 正文出现 0 次。
- **§8 是否写有 `Two gaps remain.`：是**。以 `rfind` 跳过 TOC 条目、锁定 `What remains open` 与 `9 Limitations` 之间的正文段（561 字符），其中含 `Two gaps remain.`（其下列 wire-length null 无法构建、无独立人工标注 real-document benchmark 两个 gap）。
- 章节标题数量（我统计 `<h1>–<h6>`）：v1 共 18（含 1 个 `modal-title`、1 个 `Abstract` 伪标题），v2 共 38（含 1 个 `modal-title`，无 `Abstract` 伪标题）。按「全部 h 标签减去 modal 与 Abstract 伪标题」口径：v1 = **16**、v2 = **37**，可精确复现报告数值。section+subsection 级别：v1 = 14、v2 = 28。无论哪种口径，**v2 章节标题数 > v1**。
- 字节大小关系：v2 HTML `182710 B` **>** v1 HTML `50485 B`（`v2_gt_v1_bytes=True`）。

### F. 本机绝对路径 / 凭证样式扫描

对 5 份原始字节逐字节（UTF-8 + `errors=replace`）用更宽模式扫描：`/Users/<用户名>/`、`/home/<用户>/`、`Bearer + 长串`、`ghp_/gho_/ghs_/ghu_/ghs_`、`api_key=`、`access_token`、`authorization:`、`sk-`、`AKIA`、`private_key`、`password=`。

- 5 份文件**全部 0 命中**：无本机绝对路径，无凭证样式字符串。
- 说明：atom `<id>` 含 `j7NWbCIc0oQzxwelAkVp7SH/QD4`，是 arXiv API 的不透明查询 id（在 `/api/` 路径下），不含任何 `Bearer`/`ghp_`/`api_key`/`sk-` 前缀，未命中任何凭证模式，不构成凭证，也非路径。

---

## 2. 我的解析脚本 / 口径与缺陷（如实记录）

1. **真实脚本缺陷（已发现并修正，不掩盖）**：初版脚本判定「§8 是否含 `Two gaps remain.`」时用 `str.find()` 取 `What remains open` 与 `9 Limitations` 的**首次**出现位置切片，切到的是 TOC 导航条目相邻区，得到错误结果 `section8_two_gaps_remain=False`、`section8_span_chars=18`。改用 `rfind()` 锁定正文标题后修正为 `True`、段长 561 字符。该缺陷仅存在于我的分析脚本，已修正，与 R122 产物无关，不影响任何最终数值（报告中 E 的 §8 结论为修正后结果）。
2. **空白归一口径**：HTML 章节标题用 U+2002/U+2006 空格，`+0.033` 等数值在 MathML 中同时有可见字形与 `<annotation>` TeX 文本节点，去标签后会产生 `+ 0.033 +0.033 ...` 的重复。我对 E 的纯文本做了 `\s+→单空格` 折叠；因此 `7.3 ...`、`9 Limitations` 才能以给定 ASCII 空格子串匹配，`+0.033`/`[0.015,0.050]` 因 `<annotation>` 文本而计数偏高（各 4 次）。这是**口径选择**，不是数据不一致。
3. **正文内嵌摘要 math 口径**：我用 `alttext="46\times"` 渲染行内公式，得到 1938 字符 / 相似度 0.4724。若按「保留 MathML 可见字形 + annotation 全部文本节点」的 naive 口径，得 1941 字符 / 相似度 0.4719 / 38 块。报告数值（1943 / 0.4717）与 naive 口径在 2 字符、0.0002 内一致 —— 即 §3 的 3 处 MISMATCH 源于 math/空白口径，非数据错误。
4. **「合法 HTML」口径**：以可解析 + `html/head/body` 结构完整为准；4 份 HTML 的严格 XML 良构性为 False，属 HTML5 预期，非缺陷。
5. 我已用原始字节直接 `==` 复核 v2 abs 摘要与 atom summary 的逐字相等（1534 字符），避免仅依赖 `norm()` 后的相等判定。

---

## 3. 第 2 步：与报告声明逐条对照（MATCH / MISMATCH）

对照范围：以 `R122-VERIFICATION.json` 的 47 条 checks 为主干，加 `R122-ROUND-AUDIT.md` 正文中的可复算数值/逐字声明，加 `R122-SOURCE-MANIFEST.json` 的 5 条 bytes+sha。共 **60 条声明**。

| 组 | 声明（简写） | 报告值 | 我的独立值 | 判定 |
|:--|:--|:--|:--|:--|
| A | api/v1abs/v1html/v2abs/v2html 5×sha256 | 见 §1 表 | 逐项全等 | MATCH |
| A | 5×bytes | 3139/41581/50485/43656/182710 | 同 | MATCH |
| A | 5 份均非空 | true | true | MATCH |
| A | 4 HTML 合法、api 为 XML | true | true | MATCH |
| A | SOURCE-MANIFEST 5 条与 §3 表一致 | — | 全等 | MATCH |
| B | v1 citation_title 全文 | 见报告 | 同 | MATCH |
| B | v2 citation_title 全文 | 见报告 | 同 | MATCH |
| B | 两标题不同 | true | true | MATCH |
| B | v1/v2 citation_date 均 2026/09/21 | 相同 | 相同 | MATCH |
| C | feed-level updated=2026-11-14T03:57:55Z | 查询时刻 | 同，且判为查询时刻 | MATCH |
| C | feed updated 非版本时间 | true | true | MATCH |
| C | entry id/title/published/updated | 见报告 | 全等 | MATCH |
| C | entry summary 与 v2 abs 摘要逐字相等 | true | true（字节相等） | MATCH |
| C | §4.1 Submission history 时刻与 atom 吻合 | 21/22 Sep | 我在 abs:161-164 复见 | MATCH |
| D | v2 abs 摘要 / atom summary 各 1534 | 1534/1534 | 1534/1534 | MATCH |
| D | abs ≡ atom 逐字 | true | true | MATCH |
| D | v1 abs 摘要 1433、与 v2 各份不同 | 1433 | 1433，全不同 | MATCH |
| D | 正文内嵌摘要 ≠ abs/atom | true | true | MATCH |
| D | 相似度低于报告判定界（≈0.47） | <0.6 | 0.4724 < 界 | MATCH |
| D | 「38 个差异块」 | 38 | 38（4 种口径均 38） | MATCH |
| D | 「同一 v2 存在两份措辞不同摘要」 | true | true | MATCH |
| D | 正文内嵌摘要字符数 **1943** | 1943 | **1938**（naive 口径 1941） | **MISMATCH（口径）** |
| D | 相似度精确值 **0.4717** | 0.4717 | **0.4724**（naive 口径 0.4719） | **MISMATCH（口径）** |
| E | E1–E14 十四条子串存在/阈值 | 见 §1 表 | 14 条全部 ≥ 阈值且计数吻合 | MATCH（14 条） |
| E | E15 v2 章节标题 > v1 | true | 37>16 / 28>14，true | MATCH |
| E | E16 v2 字节 > v1 | true | 182710>50485 | MATCH |
| E | v2 正文含时间尺度 sweep 结论 | 是 | 是 | MATCH |
| E | §8 写有 `Two gaps remain.` | 是 | 是 | MATCH |
| E | §4「v2 37 / v1 16 章节标题」精确值 | 37/16 | 可精确复现 | MATCH |
| E | §3「R122-v2-PLAINTEXT.txt 45,960 字符」 | 45960 | **45430**（全折叠）/46545（不折叠） | **MISMATCH（口径）** |
| F | 无本机绝对路径 | true | 0 命中 | MATCH |
| F | 无凭证样式字符串 | true | 0 命中 | MATCH |

**计数**：A 13 MATCH/0、B 6/0、C 8/0、D 9 MATCH/2 MISMATCH、E 19 MATCH/1 MISMATCH、F 2/0 —— **合计 57 MATCH / 3 MISMATCH**。

**3 处 MISMATCH 的原因（逐条定性）**：

- D（正文内嵌摘要 1943 vs 1938）与 D（相似度 0.4717 vs 0.4724）：**我的解析口径不同**——行内公式 `46×` 我用 LaTeX `alttext` 渲染，报告派生件 evidently 保留了 MathML 可见字形 + `<annotation>` 文本（naive 口径下我得 1941 / 0.4719，与报告在 2 字符 / 0.0002 内一致）。经核验 `R122-v2-BODY-ABSTRACT.txt` 实测 1943 字符、`R122-VERIFICATION.json` 的 `abstract_similarity=0.4717`，说明**报告数值对其自有派生件准确**。属**口径差异**，非我的脚本缺陷导致错误、非数据不一致、非报告事实错误；38 个差异块在所有口径下一致。
- E（明文 45,960 vs 45,430）：**我的解析口径不同**——报告数值是其派生 `R122-v2-PLAINTEXT.txt` 的字符数（我实测确为 45,960），我第 1 步按「删 script/style + 全空白折叠」得 45,430、按「不折叠」得 46,545，派生件介于两者之间。属**口径差异**（空白归一程度），非数据不一致、非报告错误。

其余 47 条 checks 的概念性断言（含 A1–A4 同机字节恒等、B–F 实质一手观察）在我的独立重算下**全部成立**；报告 `scope_note` 自陈「A1–A4 属构造上必然一致、不属独立交叉核验」与我判定一致。

---

## 4. 第 3 步：12 类「点名夸大」CONFIRMED / REFUTED 判定

**口径定义**：CONFIRMED = 本轮产物（`R122-ROUND-AUDIT.md` / `R122-VERIFICATION.json` / `R122-SOURCE-MANIFEST.json` + 5 份原始字节可证范围）确实把该夸大作为正面主张提出（构成实际夸大缺陷）；REFUTED = 本轮未提出该主张，且通常已明确否定/规避（夸大不成立）。逐条给证据（行号指向上述报告文件）。

| # | 点名夸大 | 判定 | 证据 |
|:--|:--|:--|:--|
| a | 把第三方已发表文献版本事实冒充本项目科学结果 | **REFUTED** | `R122-ROUND-AUDIT.md:53`「**这不是本项目结果，是第三方已发表文献的版本事实**」；`:35` 范围限定；`:103`「零科学活动」；`:106`「一手文献冻结件…不构成达标进展」；`:114` 新教训③「不得当作本项目结果或升分依据」。原始字节仅为 5 份 arXiv 页面，无任何本项目结果数据。 |
| b | 声称本轮产生模型前向/训练/数据集/科学指标 | **REFUTED** | `:6`「**Forward pass performed:** NO」；`:103`「零模型前向 / 推理 / 训练 / 标签 / 数据集 / EPE·l2 / 科学指标 / 新正向证据。仅 HTTP 只读取证 + SHA 复算 + 文本抽取」；`R122-VERIFICATION.json` 全 47 检查均为字节/文本观察。 |
| c | 声称任何门被标 passed 或 `pipeline-state.json` 写回 | **REFUTED** | `:4`「G0 may be passed: NO（本轮未改任何门状态，pipeline-state.json 字节零改动）」；`:95`「G0–G8 / validation / handoff 全 pending」；`:101-102`「未回写任何既有 registry / 矩阵 / state / 门配置…字节全部零改动」「未晋级任何门」。 |
| d | 声称启动 `ccf-paper-reviewer full` 或产生数值 `**Overall:**` 行 | **REFUTED** | `:7`「Full manuscript review launched: NO（ccf-paper-reviewer full 未启动，无 **Overall:** 数值行）」；`:22`「无未登记异步 full 评审」；`:104`。 |
| e | 声称论文在 2026-11-14 更新（把 feed 查询时刻当版本时间） | **REFUTED** | `:68`「feed-level updated=2026-11-14T03:57:55Z 是**本次 API 查询生成时刻，不是论文版本更新**…**不得**据此声称「论文今日更新」」；`:66-67` 分列 entry-level 版本时间（2026-09-21/22）；`R122-VERIFICATION.json` C5/C6；`:114` 新教训②。我的 C 独立判定与之完全一致。 |
| f | 声称「首次发现」/「全项目从未」全称历史否定 | **REFUTED** | `:35`「严格限定为「本轮可见产物范围内此前未落盘」的范围观察，**不作「首次发现」全称主张**」。 |
| g | 声称 v1 与 v2 同一摘要、或 v2 只有一份摘要 | **REFUTED** | `:51` 标题「同一 v2 存在两个措辞显著不同的官方摘要」；`:55-59`「v1 abs 摘要 1,433 字符，与 v2 两份摘要均不同；v1/v2 标题亦不同」；`:59`/D2/D3。我的 D 独立确认 v1≠v2、v2 有两份不同摘要。 |
| h | 声称 R4「登记进 literature-search/source-manifest.json」已完成 | **REFUTED** | `:101`「未回写…（R4 要求的登记动作）…字节全部零改动」「本轮仅在本目录内提供 R122-SOURCE-MANIFEST.json 作为**待裁决的一手附件**，不自行登记」；`:112`「R4 剩余『登记进 source-manifest.json』…须 G7/G6 裁决」；`:114` 新教训④。我核对该目录确无 `literature-search/source-manifest.json` 写回。 |
| i | 声称 `literature-baseline-matrix.md` 已定稿或 SHA 重新冻结 | **REFUTED** | `:79`「本轮不改 literature-baseline-matrix.md（矩阵定稿属 R120 决策登记册 G6）」；`:101`「literature-baseline-matrix.md（R2 定稿）…字节全部零改动」。 |
| j | 声称本轮使 governing 分数变化或使 reviewer Overall 达标 | **REFUTED** | `:25` governing 维持不变；`:29` 只读审计在结构上不可能改动分数；`:93` 只读门读数维持未达标状态；`:106`「一手文献冻结件不改变 governing…不构成达标进展」「明确不把『取证完成』包装成『靠近达标』」；`:110` 维持未达标。 |
| k | 声称 G0 已可通过、或 G0 未过时启动 P3 | **REFUTED** | `:4` G0 may be passed: NO；`:95` G0 pending（`G0.inputs=[]`/`G0.evidence=[]`）；`:105`「未跳门 / 未启动 P3（G0 未过）」；`:112` 唯一 admissible 路径仍按序 G0–G8 … → P3。 |
| l | 声称 R106 的 G4 定位被推翻、或 R99 版本错配叙事被改写 | **REFUTED** | `:62`「**本轮不主张 R106 有误，也不主张推翻任何既有判定**」「R106 已撤回「版本错配」叙事，**本轮不回溯改写该结论**」；`:79`「本轮不改 G4 状态」。 |

**CONFIRMED 计数：0；REFUTED 计数：12。** 12 类夸大全部不成立；报告对每一类均设有显式否定或范围限定，且可由原始字节与报告文本双重支撑。其中 (c)/(j)/(k) 涉及外部状态文件（goal-ledger / pipeline-state.json / guard ledger），不在我仅凭 5 份原始字节可独立核验的范围；我据报告显式声明与「原始字节中无任何门/评审/模型产物」判定 REFUTED，并如实标注该范围限制。

---

## 5. 第 4 步：瑕疵分级清单

说明：§3 的 3 处 MISMATCH 全部源于**我的解析口径**（math/空白归一），报告数值对其自有派生件准确，**不计为报告瑕疵**。以下为报告本身的瑕疵。

- **LOW #1 — 措辞不精确（逐字引用口径未声明）**
  - 位置：`R122-ROUND-AUDIT.md:75`（并 `:72`「从 `R122-v2-PLAINTEXT.txt` 直接读取，非转述」）。
  - 事实：该处标「逐字」的 §8 引用写作 `... by +0.033 [0.015,0.050] relative to the short window, and spectral bands carry a consistent +0.085 to +0.102 ...`。在派生明文与我从原始字节独立去标签的纯文本中，该句实际为 `... by + 0.033 +0.033 [ 0.015 , 0.050 ] [0.015,0.050] ... + 0.085 +0.085 to + 0.102 +0.102 ...`（MathML 可见字形 + `<annotation>` 重复）。报告引用是清洗/归一化后的呈现，连续的 `+0.033 [0.015,0.050]` 并非派生明文的字节逐字子串。语义准确、各数值 token 均可逐字命中（E5/E6），但「逐字」标签在一份以「字节级/逐字」为自我标准的文档中略不精确。分类：**措辞不精确**（非事实错误、非编造）。
- **LOW #2 — 范围未限定（章节标题计数口径未声明）**
  - 位置：`R122-ROUND-AUDIT.md:60`「v2 HTML 正文 37 个章节标题…v1 为 16 个」。
  - 事实：37/16 可按「全部 `<h1>–<h6>` 标签减去 modal 对话框标题与 Abstract 伪标题」精确复现，数值本身正确；但该计数把 h1 文档标题、6 个 h4 段落小标题、bibliography 标题一并计入，统称「章节标题」且未在文中限定计数口径。分类：**范围未限定 / 措辞不精确**（非事实错误）。
- **HIGH：0 处；MEDIUM：0 处；事实错误 / 数据不一致 / 编造：0 处。** 未发现时点/口径混用缺陷——报告 §4.1 与 C5/C6 对 feed 查询时刻与 entry 版本时间作了显式分列（属报告优点）。

---

## 6. 结论

- 首行 verdict：`REPRODUCIBLE_WITH_DEFECTS`。
- 判定依据：A–F 六组一手观察全部可独立复算，60 条声明中 57 条 MATCH，3 条 MISMATCH 经核实全部为**我的解析口径差异**（行内公式渲染 / 空白归一），在报告口径下可复现到 2 字符、0.0002 以内，且报告数值对其自有派生件准确，**无数据不一致、无事实错误、无编造**；47 条 verifier checks 概念上全部成立；12 类点名夸大全部 REFUTED；仅存 2 处 LOW 级措辞/口径瑕疵，不改变任何实质结论。
- `**G0 may be passed:** NO` — 报告 `:4/:95/:101-102/:105` 明示 G0 pending、未写 passed、未跳门；原始字节中无任何门状态/写回证据。
- `**Scientific result claimed:** NO` — 报告 `:5/:53/:103/:106` 明示零科学活动、版本事实非本项目结果；5 份原始字节仅为第三方 arXiv 页面。
- `**Forward pass performed:** NO` — 报告 `:6/:103` 明示零模型前向/训练/数据集/科学指标；原始字节中无任何模型/数据产物。
- 范围限制：`R122-ROUND-AUDIT.md:17-25/:93-97` 关于并发保护、goal-ledger、pipeline-state.json、guard ledger 的读数，以及 `:37`「全部 HTTP 200」的采集过程声明，不在仅凭 5 份原始字节可独立核验的范围（无 HTTP 头/外部状态文件字节），本报告未对其真伪下断言；这些不影响 A–F 一手观察的可复算性与上述 verdict。

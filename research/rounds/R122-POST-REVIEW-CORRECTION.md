# R122 — 独立审查回收后的只追加更正（历史正文与独立报告原文零改动）

**性质**：本文件是**新增**的更正登记，不改写 `R122-ROUND-AUDIT.md`、`R122-INDEPENDENT-REVIEW.md`、`R122-VERIFICATION.json`、`R122-SOURCE-MANIFEST.json`、5 份 raw 字节、第十六检查点中的任何字节。

**独立报告最终读数**：`R122-INDEPENDENT-REVIEW.md` **24,434 B / SHA256 `bcc78c27ab05ccee699199f8c01899f4a6bd912a6e24202a82397df080cace4e`**（mtime 12:25:48，一次写入、原文零改动）。首行 `REPRODUCIBLE_WITH_DEFECTS`；`**G0 may be passed:** NO` / `**Scientific result claimed:** NO` / `**Forward pass performed:** NO`。

**复核结果**：A–F 组 **57 MATCH / 3 MISMATCH**（A 13/0、B 6/0、C 8/0、D 9/2、E 19/1、F 2/0）；12 类点名夸大 **CONFIRMED 0 / REFUTED 12**；瑕疵 **HIGH 0 / MEDIUM 0 / LOW 2**；事实错误 / 数据不一致 / 编造 **0**。复核者仅用 5 份 raw 字节、自写解析逻辑，未 import 采集/verifier、未把任何 R122 JSON 当数据源，最后才读轮次审计做瑕疵分级。报告内期望分 / 分数锚点 **0 命中**。

---

## 1. 三处 MISMATCH：全部接受，定性为「复核者解析口径差异」，非报告错误

| # | 报告值 | 复核者值 | 定性 |
|:--|:--|:--|:--|
| D | 正文内嵌摘要 **1,943** 字符 | **1,938**（naive 口径 1,941） | 行内公式 `46×` 渲染口径不同：复核者用 LaTeX `alttext`（`46\times`），本报告派生件保留 MathML 可见字形 + `<annotation>` 文本节点。复核者实测 `R122-v2-BODY-ABSTRACT.txt` 确为 1,943 字符 ⇒ **报告数值对其自有派生件准确**；两种口径差 2–5 字符。 |
| D | 相似度 **0.4717** | **0.4724**（naive 0.4719） | 同上，差 ≤0.0007；**38 个差异块在全部四种口径下恒为 38**。 |
| E | 明文 **45,960** 字符 | **45,430**（全折叠）/ 46,545（不折叠） | 空白归一程度不同；复核者实测 `R122-v2-PLAINTEXT.txt` 确为 45,960 字符 ⇒ 报告数值对其自有派生件准确，派生件介于复核者两种口径之间。 |

**处置**：不改写任何派生件或数值；在此明确登记「字符数 / 相似度 / 明文长度」三个量**必须绑定具体派生件与归一口径**才可比。核心结论（v2 两份摘要措辞显著不同、相似度约 0.47、38 差异块、v1 与 v2 全不同）在全部口径下成立。

**复核者自述的脚本缺陷（如实保留，不掩盖）**：初版用 `str.find()` 取 `What remains open` 首次出现，误切到 TOC 导航区，得 `section8_two_gaps_remain=False / 18 字符`；改 `rfind()` 锁定正文后修正为 `True / 561 字符`。该缺陷只存在于复核者分析脚本，已修正，不影响任何最终数值。

## 2. 两处 LOW 瑕疵：全部接受，只追加更正

### C-1【LOW｜措辞不精确】「逐字」引用未声明归一口径
- **位置**：`R122-ROUND-AUDIT.md:75`（并 `:72`「从 `R122-v2-PLAINTEXT.txt` 直接读取，非转述」）；公开脱敏摘要的对应段落同样使用「逐字」。
- **事实**：该处标「逐字」的 §8 引文 `… by +0.033 [0.015,0.050] relative to the short window, and spectral bands carry a consistent +0.085 to +0.102 …` 是**清洗 MathML 重复后的呈现**；派生明文的实际字节为 `… by + 0.033 +0.033 [ 0.015 , 0.050 ] [0.015,0.050] … + 0.085 +0.085 to + 0.102 +0.102 …`（可见字形 + `<annotation>` TeX 文本并存）。连续串 `+0.033 [0.015,0.050]` **不是**派生明文的字节逐字子串。
- **更正（收窄措辞）**：该引文为**数值 token 逐字可命中、整句经空白/MathML 归一后的呈现**，不是「派生明文连续字节的逐字子串」。语义准确、各数值 token 由 verifier E5/E6 逐字命中；不改变 §8 结论、不改变任何数值、不宣称原文被改写。
- **附带范围说明**（复核者 E 组）：`7.3 The stimulus never completes a cycle`、`9 Limitations` 两个标题在原始字节中编号与标题间使用 U+2002/U+2006 Unicode 空格，严格 ASCII 单空格逐字为 0 次、空白归一后各 2 次；`Two gaps remain.` 为普通 ASCII、原始字节逐字即 1 次。verifier E1/E14 的计数基于已归一的派生明文，故成立。

### C-2【LOW｜范围未限定】章节标题计数口径未声明
- **位置**：`R122-ROUND-AUDIT.md:60`「v2 HTML 正文 37 个章节标题…v1 为 16 个」；公开脱敏摘要同段。
- **事实**：37/16 在「全部 `<h1>–<h6>` 标签减去 modal 对话框标题与 Abstract 伪标题」口径下可精确复现，数值本身正确；但该计数把 h1 文档标题、6 个 h4 段落小标题、bibliography 标题一并计入，统称「章节标题」而未限定口径。复核者按 section+subsection 级别另得 v1 14 / v2 28；**所有口径下 v2 > v1 的大小关系不变**。
- **更正（限定范围）**：37/16 特指「全部 h 标签减 modal 与 Abstract 伪标题」的**标签计数**，不是严格意义的 section/subsection 数；v2 > v1 的结论与 E15/E16 不受影响。

**2 处均为措辞 / 范围收窄**，非事实错误、非数据不一致、非编造。复核者明确未发现时点 / 口径混用缺陷，并指出报告 §4.1 与 verifier C5/C6 对 feed 查询时刻与 entry 版本时间的分列属报告优点。

## 3. 复核者补充的一手事实（如实登记，不改变结论）

- **B 组**：v1/v2 `citation_title` 完全不同；`citation_date` **均为 2026/09/21**（相同）；区分两个版本的是 `citation_online_date`（09/21 与 09/22）。本报告 §4.1 依据 abs 页 `Submission history` 与 atom entry-level 给出 `[v1] 21 Sep 13:30:30 UTC / [v2] 22 Sep 12:24:47 UTC`（均 3,306 KB），与复核者结论一致、无冲突。
- **F 组**：atom `<id>` 中的 `j7NWbCIc0oQzxwelAkVp7SH/QD4` 是 arXiv API 的不透明查询 id，**不是凭证**；5 份 raw 字节无本机绝对路径、无 Bearer / ghp_ / api_key 等凭证样式。
- **范围限制（复核者声明，接受）**：`R122-ROUND-AUDIT.md` 的并发保护、goal-ledger / `pipeline-state.json` / guard ledger 读数及「全部 HTTP 200」采集声明，不在仅凭 5 份 raw 字节可独立核验的范围，复核者未对其真伪下断言；不影响 A–F 可复算性与 verdict。本轮双门与状态读数由主会话独立采集，见轮次审计 §7 与收尾复核。

## 4. 不变项（逐条确认）

- governing 仍 **R95 = 6.0 / Confidence 4.0**；validator `NOT_QUALIFIED / 6.0 / >=7.0`、guard `INCOMPLETE`。
- **0 篇达标、未写 COMPLETE**；G0 仍 `pending`、零门晋级、零自我认证、零状态写回。
- 5 份 raw SHA、`R122-SOURCE-MANIFEST.json`、`R122-VERIFICATION.json`（47/47 MATCH）、`R122-ROUND-AUDIT.md`、第十六检查点字节全部零改动；复核者未修改任何既有文件。
- 门 / 证据层复核，**非** `ccf-paper-reviewer full` 稿件评审；独立报告无 `**Overall:**` 数值行、无分数锚点、不改变 governing。
- 第十六检查点在写时点标注「独立复核已下发、未回收、不宣称结论」为**真**，字节零回写；按 R117/R119/R120/R121 先例，回收结论与本更正另建**新的不可覆盖检查点**（第十七）。

## 5. 交下轮

以 `reconciliation-R120/R120-CONSOLIDATED-DECISION-REGISTER.md` 为唯一决策入口（最小集 `G1+G4+G10`）；R4 的「登记进 `source-manifest.json`」与 R2 矩阵定稿须 G7 / G6 裁决，心跳不自行回写；唯一 admissible 路径仍为按序 G0–G8 → validation → handoff → P0 → P1A/P1B → P2 → **P3 baseline-first 真实前向**取得实质正向新证据 → 稿件新副本 → 9 页合规编译 → 全新隔离 full 评审；`X >= 7.0` 且 QUALIFIED + COMPLETE 才写 COMPLETE。

**新教训**：① 引用 MathML 富文本正文必须声明归一口径，「逐字」只用于 token 级或已声明归一后的文本；② 计数类数值必须写清「统计口径」（标签数 vs section 数）；③ 字符数 / 相似度 / 明文长度必须绑定具体派生件，跨实现比对时先对齐归一规则；④ 独立复核的 MISMATCH 要先自查解析口径差异，不可直接判为数据错误，也不可直接判为报告错误。

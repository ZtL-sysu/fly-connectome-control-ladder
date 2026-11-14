# R128 独立审查回收 + 只追加更正（历史正文与独立报告原文零改动）

**性质**：按 R117/R119–R125 先例，第二十五检查点 `20261114T113553Z-r128-post-merge-attestation/`
在**其写时点**如实标注「全新隔离独立审查已下发、未回收、不宣称结论」——该陈述为真
（检查点 `CHECKPOINT.md` 于本轮同步提交前写就，独立报告 `R128-INDEPENDENT-REVIEW.md`
于其后落盘），故其字节**零回写**。回收结论与更正**只追加**于本文件 + **新的不可覆盖检查点**
`20261114T115234Z-r128-post-review/`。

## 独立复核件（全新隔离子代理 `general-purpose-1`）

- 文件：`post-merge-R128/R128-INDEPENDENT-REVIEW.md`
- **12,680 B / 89 行 / SHA-256 `ff2bbe3c5ff3cd4d71089f6cbde4f614776e7f80f9421fb6cb6cbae48bd8ce78`**
- 首行：`REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`
- 独立性：不 import 采集 / verifier、不把任何 R128 JSON 作实质数据源、从 `main` 提交树 blob
  用自有逻辑重算 A–H，最后才读轮次审计；未跑 git add / commit / push / merge / checkout；
  唯一写入即该报告。报告内 **0 数值 `**Overall:**` 行 / 0 真实凭证值 / 0 邮箱字面值**。
- 未透露期望分 / 分数锚点 / 结论锚点。

## 独立复算结论（A–H）

| 组 | 结论 |
|:--|:--|
| A | 336 文件 / 9,798,478 B / 最大 2,149,921 B / 0 >50MiB / 本地=远端 / 工作区干净（同机恒等核对） |
| B | `UPLOAD-MANIFEST` 233 条 `copied` / `skipped=0`，**233/233 字节 + SHA-256 全匹配 / 0 mismatch / 0 missing / distinct 233** |
| C | **真实凭证值 0 命中**；扫描模式字面串按宽口径 21 强前缀文件 / 9 个 `.py` / 112 个朴素 `sk-` 文件，**全部 NON-secret**；审计的「19」是采集器三标签窄口径，不同口径并存非矛盾；`Task-Aligned` 假阳性被独立复现（严格模式 0） |
| D | 权重 / 数据集 / 二进制后缀 0；2 份 PDF 均合法稿件 |
| E | 公开树严格行首数值评分 **12 行 / 10 文件**，全在 `research/reviews/`；最新独立 full 评审 r95 / 20261111 / 值 6；零 `research/` 文件曾被 `M`、无隐藏 / 重定日期 / 新达标候选 |
| F | validator `NOT_QUALIFIED / 7.0 / 6.0 / meets=false / all_pass=false`（D1✓D2✗D3✗D4✓D5✗）；guard 两 sha16 一致、A1–A6、actions 0、S1–S7 pending |
| G | 12 阶段、`CCFA-startup passed`、其余 11 pending；**G0 inputs=0 / evidence=0 / verdict pending** |
| H | A–G 全部数值与否定性结论逐项匹配；`agent..main` diff 仅 AGENTS/README/PROTOCOL（63 行），`research/` 与 HANDOFF/LOG 空 ⇒ 审计 §3:52 / §4.2 正确 |

**12 类点名夸大 (a)–(l)：CONFIRMED 0 / REFUTED 12**（逐条字节级理由见报告 §"12 类 overclaim 判定"）。
**Fabrications：0**。复核者范围限制（同机恒等核对、无法重放 `ls-remote` HTTP/TLS 与远端服务器状态、
仅核验 `main` 单一 ref、未运行采集 / verifier、validator governing 依赖本机 mtime、0 命中仅对有限
模式成立且真实凭证值文件已被有意排除故不构成「绝无密钥」证明）**全部接受**。

## 5 项全部接受、只追加（无一项增加主张）

### M1 [MED｜事实误标，非载荷项] — D-1 接受

轮次审计 `R128-ROUND-AUDIT.md:71` 写「最大单文件 **2,149,921 B**（`research/manuscript/main.pdf`
**2.06 MiB**，稿件 PDF）」为**事实错误**：

- 独立字节核验：该值属 **`research/manuscript/main-2.pdf`（2,149,921 B = 2.0503 MiB）**；
- `research/manuscript/main.pdf` 实为 **2,123,187 B（2.0248 MiB）**；
- 「2.06 MiB」为错误换算（正确 2.0503 MiB）。
- 同一轮冻结件 `R128-ACQUIRE.json:190/194` 与 `R128-VERIFICATION.json` 已**正确**给出
  `main-2.pdf` / 2,149,921 与 `main.pdf` / 2,123,187 ⇒ 该错误**只存在于轮次审计的散文路径与 MiB
  换算**，数值本身不变、与自身机器产物矛盾，属笔误。
- 影响范围：仅一处散文标注；**不改变** 336 / 9,798,478 / 2,149,921 / 0 凭证 / 233 匹配 /
  12 行评分 / 6.0 / `NOT_QUALIFIED` / `INCOMPLETE` / G0 pending / governing / 0 篇达标 /
  R121 否定性闭环 / 双门 / 调度中的任何一项。
- 处置：按红线**不回写已发布字节**（轮次审计已随第二十五检查点上传）；只追加本更正，
  并在新检查点 `CHECKPOINT.md` 明示正确路径。

### L1 [LOW｜口径差异，非缺陷] — C 组「19」与宽口径计数

复核者宽口径得 21 强前缀 / 160 弱标记 / 112 朴素 `sk-` 文件；采集器「19 文件」是
`gh_scan_literal` / `AIza_scan_literal` / `b_quote_ghp` **三标签窄口径**。二者**不同口径并存、
均为非凭证**，不构成数据不一致。此后引用「19」必须写明窄三标签口径，引用宽口径须给
程序复算值与 occurrences / distinct（R120 W5 / R124 J-1 / R125 L1 教训）。

### C1 [已披露 / 已冻结 / 无残留] — D-2 接受，无需新动作

v1 verifier `sk-` 无词边界致 **246 假候选 / 24 文件、35/34/1**；复核者以不同正则形状独立复现
同一根因（249 候选 / 246 含 `Aligned/Controls/Connectome`），确认既非 246 个凭证也非数据不一致。
已在 `R128-V1-DEFECTS.md` 定级、v2 加 lookbehind 修正、v1 两文件原样冻结、36/36 全 MATCH。

### C2 [观察，非缺陷] — `blobs_read=308`

采集器 `R128-ACQUIRE.json` 的 `blobs_read=308` 系按 blob SHA **去重**（308 个不同 SHA / 28 个
重复内容路径），336 个路径全覆盖、逐 blob 长度全等；不是漏读 28 个文件。

### C3 [观察，非缺陷] — 账本 SHA 时点差

复核者读到 `goal-ledger.md` 当前 sha16 `8e00e0a66243` 与冻结锚点 `3a694ab2…` 之差，源于
**19:43:31 的 T3 只追加写入**（晚于 verifier 19:30:12 / 轮次审计 19:31:49），已由
`R128-TIMEPOINT-NOTE.md` 声明；属账本正常演进，**非本轮回写、非门 / state / 矩阵 / registry 写回**。

## 结论与边界不变

5 项全为**措辞 / 口径 / 补充事实收窄 / 已披露缺陷复核**，无一项增加主张：均不改变 13 份 raw
字节与 SHA、SOURCE-MANIFEST、v2 **36/36 MATCH / 0 MISMATCH**、A–H、12 类 REFUTED 12、
双门读数（`NOT_QUALIFIED / 6.0 / >=7.0`、`INCOMPLETE`）、门状态（G0 pending、G1–G8 全 pending、
`inputs=[]`/`evidence=[]`）、governing **R95 = 6.0 / 4.0**、0 篇达标、未写 COMPLETE、心跳调度。

轮次审计原文、独立报告原文、两版 verifier / VERIFICATION、raw、SOURCE-MANIFEST、第二十五
检查点字节全部**零改动**。门 / 证据层复核，**非** `ccf-paper-reviewer full` 稿件评审、
不产生 `**Overall:**` 数值行、不改 governing。

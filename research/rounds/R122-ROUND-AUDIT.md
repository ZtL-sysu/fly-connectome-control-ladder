# R122 — R106 §6 R4 一手冻结件首次落盘 + 同一 v2 双摘要字节级坐实

**Verdict:** `READ_ONLY_FIRST_HAND_SOURCE_FREEZE_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
**G0 may be passed:** NO（本轮未改任何门状态，`pipeline-state.json` 字节零改动）
**Scientific result claimed:** NO
**Forward pass performed:** NO
**Full manuscript review launched:** NO（`ccf-paper-reviewer full` 未启动，无 `**Overall:**` 数值行）

2026-11-14 11:47–12:0x +0800 · 心跳唤醒 R122 · 无人值守。

---

## 1. 并发保护（第 0 步）

| 检查 | 读数 |
|:--|:--|
| `goal-ledger.md` mtime | `2026-11-14 10:45:59 +0800`（唤醒 11:47:51，差 **3,712 s ≈ 61.9 min > 10 min**） |
| 主会话 / 轮询进程 | 仅本自动化会话自身（`subRunId …1794628049993:0`）；无第二轮询进程 |
| 近 12 分钟写入 | 0 个文件 |
| `ccfa-review-reports/` 最新 | `paper-null-ladder-r95-independent-review-20261111.md`（11-11 15:01） |
| `ccfa-idea-review-reports/` 最新 | `idea-review-effective-indegree-unification-20261110.md`（11-10 12:27） |
| 行首数值 `**Overall:**` 行 | **12 文件 / 12 行**（排除 `isolated/` 副本），最新仍 r95；**无未登记异步 full 评审** |
| R122 产物 | 唤醒时 0 份 |

⇒ 并发保护**不触发**，主动推进。governing 仍 **R95 = 6.0 / Confidence 4.0**。

## 2. 为什么换道到 R4（RGE4）

R105 / R107 / R109 三次判停「继续产出流程证据文档」同构循环；R114–R121 连续八轮各审计一层流程/基础设施，**R121 已从 governing 评审 R95 自身升分判据（§13 :450「No quick change」、:448/:473 三项新科学证据、:454 tie-breaker）推出否定性闭环**：这类只读审计在结构上不可能把 6.0 抬到 >= 7.0。再产出第 9 层流程审计是空转。

本轮改做**用户常驻指令第 1 步 ① 明确要求、且 R106/R107/R118/R120 反复点名 11 轮未落实**的实质动作：按 `R106-G0-INDEPENDENT-GATE-REVIEW.md` §6 **R4** 取得一手可复算件（非补丁式文字修复）：

> **R4** 为 `arXiv:2609.24565v2` 保存本地、带 SHA 的一手冻结件（至少 abs 元数据页 + HTML/PDF 正文两者，因摘要不同），登记进 `literature-search/source-manifest.json`；同时保存 v1 摘要以便版本比对。

**这是 G0 gap 2 / G4 定位（Kuklev v2 §7.3/§8 时间尺度 sweep）的证据基础**，此前 11 轮全部依赖转述、无本地一手字节。严格限定为「本轮可见产物范围内此前未落盘」的范围观察，不作「首次发现」全称主张。

## 3. 一手冻结件（5 份原始字节，全部 HTTP 200）

目录 `first-hand-R122/raw/`，SHA256 由 `R122-ACQUIRE.py` 从字节重算，`R122-SOURCE-MANIFEST.json` 为清单：

| 文件 | URL | bytes | SHA256 |
|:--|:--|--:|:--|
| `arxiv-2609.24565v1-abs.html` | `https://arxiv.org/abs/2609.24565v1` | 41,581 | `0075412eb10447864bb2b139c6d8ec8eb1c8f256b2d91e69a913203027bbd367` |
| `arxiv-2609.24565v2-abs.html` | `https://arxiv.org/abs/2609.24565v2` | 43,656 | `cbcbce7343f999ebae1f63c43963a477e96ebe827679b6f973e25e177ca7029e` |
| `arxiv-2609.24565v1-html.html` | `https://arxiv.org/html/2609.24565v1` | 50,485 | `2726ef63d6cda79393d1faa725267cb1ede474f1189caba51cc583c9a4af648c` |
| `arxiv-2609.24565v2-html.html` | `https://arxiv.org/html/2609.24565v2` | 182,710 | `f4e7fb8747165a4f4caf0a50e34ca15f7a837536699189bffe267502ca12e7ad` |
| `arxiv-2609.24565-api.xml` | `https://export.arxiv.org/api/query?id_list=2609.24565` | 3,139 | `5e1c68e2e21be996a3d2244d67b2d1c0e7a6e5c8a7d829657d7faa3f2341377d` |

衍生只读件：`R122-RAW-EXTRACTION.json`、`R122-v2-PLAINTEXT.txt`（45,960 字符）、`R122-v2-BODY-ABSTRACT.txt`、`R122-VERIFICATION.json`。

## 4. 核心一手发现：同一 v2 存在两个措辞显著不同的官方摘要

**这不是本项目结果，是第三方已发表文献的版本事实**，全部从原始字节重算：

- `v2` **abs 元数据页摘要** = `export.arxiv.org` API `<summary>`，**逐字相等**，均 **1,534 字符**（verifier D1 MATCH）。
- `v2` **HTML 正文内嵌摘要** = **1,943 字符**，与上述摘要**不相等**，`difflib.SequenceMatcher` 相似度仅 **0.4717**、38 个差异块（D3/D4）。
  - abs/API 摘要含：`"Longer observations reverse the circuit-receptor ordering once the stimulus spans a period, but not through T4/T5. Thus active sampling and exact structure matter, …"` —— **含时间尺度 sweep 反转结论**。
  - 正文内嵌摘要**不含**该句，收尾为 `"Exact structure remains insufficient to beat what the moving retina already provides."`，且不含 §7.3 的 `+0.033 [0.015,0.050]`、不含 §8 `Two gaps remain`。
- `v1` abs 摘要 **1,433 字符**，与 v2 两份摘要均不同；v1/v2 **标题亦不同**（v1 `Active Visual Sampling with a Connectome-Constrained Fly Model for One-Shot Hatch Recognition in Architectural Drawings`；v2 `What Survives on Real Drawings: Active Sampling, Connectome Wiring, and Matched Baselines in Architectural Document Vision`）。
- v2 HTML 正文 37 个章节标题、182,710 B；v1 为 16 个、50,485 B。

由此 **R106 §3 / R107 R2 所述「arXiv 上两个措辞不同的 v2 摘要并存」获得字节级一手支撑**，也解释了 R99 引用争议为何按端点与口径不同会得出不同判定（R106 已撤回「版本错配」叙事，本轮不回溯改写该结论）。**本轮不主张 R106 有误，也不主张推翻任何既有判定**；增量是把 11 轮依赖转述的对象变成可复算字节。

### 4.1 版本时间证据（严格区分两个 `updated`）

- v2 abs 页内嵌 `Submission history`：`[v1] Mon, 21 Sep 2026 13:30:30 UTC (3,306 KB)` / `[v2] Tue, 22 Sep 2026 12:24:47 UTC (3,306 KB)`。
- atom **entry-level**：`published=2026-09-21T13:30:30Z`、`updated=2026-09-22T12:24:47Z` ⇒ 与 abs 页逐字吻合。
- atom **feed-level** `updated=2026-11-14T03:57:55Z` 是**本次 API 查询生成时刻，不是论文版本更新**。verifier C5/C6 已把两者分列；**不得**据此声称「论文今日更新」或「摘要今日被改」（R121 J-1 时点混用教训）。

## 5. G4 定位叙事的一手核验（R106 §3 全部 needle 命中）

从 `R122-v2-PLAINTEXT.txt` 直接读取，非转述：

- **§7.3 `The stimulus never completes a cycle`**：8 帧仅覆盖约 1/5–9/10 个空间周期、观测窗 0.16 s 短于一个周期；长看变体 40 帧 + 时序功率谱得 0.826 vs 短漂移 0.871。
- **§8 `What the sampling sweep answered`**：逐字 `"the circuit does overtake the receptors-only descriptor once the observation passes a single period, by +0.033 [0.015,0.050] relative to the short window, and spectral bands carry a consistent +0.085 to +0.102. But the mechanism is not the one we named: the T4/T5 contribution does not grow with length."`
- **§8 `What remains open`**：逐字 `"Two gaps remain."` —— ① wire-length null 无法由现有坐标构建；② 无独立人工标注的 real-document benchmark。
- verifier E1–E16 逐条命中（含 `+0.033`、`[0.015,0.050]`、`T4/T5`×4、`0.271`/`0.356`×3、`721`×5、`1,876`×5、`0.505`×2、`0.415`×3、`9 Limitations`）。

⇒ **R106 的 G4 中心判断（判别性「何时路径重要」轴被 v2 §7.3/§8 部分抢发、风险上调）获得一手字节支撑**；仍成立的窄机制问题是「哪个 stage 整合额外时间 / per-type tuning」。本轮**不**改 G4 状态、**不**改 `literature-baseline-matrix.md`（矩阵定稿属 R120 决策登记册 G6，须 designated gate owner 签署）。

## 6. 独立可复算性

`R122-verify.py` **不 import 采集模块、不读任何 R122 JSON 作为数据源、不读本报告**，仅从 5 份原始字节用自有解析逻辑重算：

**47 检查 / 47 MATCH / 0 MISMATCH**（`R122-VERIFICATION.json`）。

范围声明（`scope_note` 已写入 JSON）：**A1–A4 是同机字节恒等检查（构造上必然一致），不属独立交叉核验**；B–F 为实质一手观察。本轮另按惯例下发**全新隔离独立子代理**复核，不透露期望分 / 分数锚点 / 结论锚点，结论与更正只追加、不回写已发布检查点。

## 7. 双门只读复核（本轮采集时刻）

| 门 | 读数 |
|:--|:--|
| `readonly-validator/validate_single_paper.py` | **`NOT_QUALIFIED`** · `overall_score=6.0` · `threshold=7.0` · `comparison_operator=>=` · `score_meets_threshold=false` · D1✓ D2✗ D3✗ D4✓ D5✗ |
| `guard_engine.py check -l guard/ledger-null-ladder.json` | **`INCOMPLETE`**（退出码 1）；A2 / A6 FAIL，S1–S7 全 pending，动作序列 0 条 |
| 主线 `pipeline-state.json` | `CCFA-startup` passed；**G0–G8 / validation / handoff 全 pending**，`G0.inputs=[]`、`G0.evidence=[]` |

A6 双口径（criteria `>=7.0` / ledger `严格 > 8.0`）为已知问题，只读登记、不自行修复。三份结构权威 SHA 采集前后一致 ⇒ 零写回。

## 8. 严格边界（逐条确认未发生）

- **未回写任何既有 registry / 矩阵 / state / 门配置**：`literature-search/source-manifest.json`（R4 要求的登记动作）、`literature-baseline-matrix.md`（R2 定稿）、`pipeline-state.json` 字节全部零改动。R4 的「登记进 `source-manifest.json`」与 R2 的矩阵定稿分别属 R120 决策登记册 **G7 / G6**，须 designated gate owner 书面裁决；本轮仅在本目录内提供 `R122-SOURCE-MANIFEST.json` 作为**待裁决的一手附件**，不自行登记、不自我认证。
- **未晋级任何门**：G0 维持 `pending`；未写 `passed` / `gate_verdict`；未追加 `history`。
- **零科学活动**：EXEC LOCK —— 零模型前向 / 推理 / 训练 / 标签 / 数据集 / EPE·l2 / 科学指标 / 新正向证据。仅 HTTP 只读取证 + SHA 复算 + 文本抽取。
- **零稿件 / 评审活动**：未起 `ccf-paper-reviewer full`、未产生 `**Overall:**` 数值行、未自评 governing、未改分数 / 阈值 / 评审 / 冻结件 / 历史字节、未假定 `≤32h / K=45` 面板授权（D1 维持 `BLOCKED_ON_CONFIRMATION`）、未创建 v4 契约。
- **未跳门 / 未启动 P3**（G0 未过）、无 4090 / L4 / H20 能力主张、主项目未投稿 / commit / push。
- **本轮的实质增量是证据层，不是分数层**：按 R121 已确立的否定性闭环（R95 §13 的 evidence-capped overall），一手文献冻结件**不改变 governing 6.0，不构成达标进展**，只闭合 R106 concern-to-action 中 R4 的取证子项、为 G0 gap 2 与 G4 提供此前缺失的一手可复算基础。**明确不把「取证完成」包装成「靠近达标」**。

## 9. 结果与交下轮

**0 篇达标，未写 COMPLETE。** governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`。停止门只剩 ①达标（>= 7.0）②用户叫停；心跳 ACTIVE 调度无变化。

交下轮：① 回收本轮全新隔离独立审查，结论与更正只追加于**新的**不可覆盖检查点；② R4 剩余「登记进 `source-manifest.json`」与 R2 矩阵定稿须 G7 / G6 裁决，心跳不自行回写；③ 唯一 admissible 路径仍是按序 G0–G8（G4 正面处理 v2 §7.3/§8/§9）→ validation → handoff → P0 → P1A/P1B → P2 → **P3 baseline-first 真实前向**取得实质正向新证据 → 稿件新副本 → 9 页合规编译 → 全新隔离 full 评审（不透露期望分）；只有 `X >= 7.0` 且 QUALIFIED + COMPLETE 才写 COMPLETE；④ 以 `reconciliation-R120/R120-CONSOLIDATED-DECISION-REGISTER.md` 为唯一决策入口（最小集 `G1+G4+G10`）。

**本轮新教训**：① 引用 `v2 摘要` 必须声明**端点**（abs/API 与 HTML 正文内嵌两份措辞不同，相似度 0.47），否则版本争议无法复算；② atom feed 的 `updated` 是查询时刻，必须与 entry-level 版本时间分列；③ 「两个 v2 摘要并存」是**第三方版本事实**，不得当作本项目结果或升分依据；④ 一手取证件的「保存」与「登记进 registry」是两个动作，后者须 gate owner 裁决，心跳不得借 R4 之名自行回写。

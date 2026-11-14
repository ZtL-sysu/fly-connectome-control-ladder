# R124 轮次审计 — R106 §6 R3 / R5 一手取证 + 九项逐条收敛表

**性质**：`READONLY_FIRST_HAND_TEXT_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`。
**不是**门审查、**不是**科学结果、**不是**分数进展、**不是** `ccf-paper-reviewer full` 稿件评审。
**成功标准（R107 用户授权终值）不变**：全新隔离独立子代理 `ccf-paper-reviewer full` 落盘**新的**报告 `**Overall:** X >= 7.0`，且 `validate_single_paper.py` QUALIFIED + `guard check` COMPLETE。governing 仍 **R95 = 6.0 / Confidence 4.0**，`0 篇达标`。

---

## 1. 第 0 步并发保护（不触发）

| 项 | 读数 |
|:--|:--|
| `goal-ledger.md` mtime | `2026-11-14 14:04:15`，距唤醒 `15:08:49` ≈ **64.8 min > 10 min** |
| 主会话 / 轮询进程 | 宿主 WorkBuddy / ChatGPT / MCP 进程之外，无 novix / runner / codebuddy 研究进程；近 12 min 项目根零写入 |
| 评审目录 | `ccfa-review-reports/` 最新仍 r95（11-11 15:01）；idea 目录最新 11-10 12:27 |
| 全项目数值 `**Overall:**` 行 | 19 行 / 19 文件，全部为历史报告或逐字节副本；晚于 r95 的两份与 r95 逐字节一致、`new_governing_candidates=0` ⇒ **无未登记异步 full 评审** |
| R124 残留产物 | 唤醒时零 |

## 2. 换道理由（RGE4）

R105 / R107 / R109 三次判停「继续产出证据文档」同构循环；R121 由 governing 评审 R95 自身 §13「No quick change」推出**否定性闭环**：流程 / 披露 / 格式 / 只读审计不新增支持中心主张的科学证据，**结构上不可能**把 evidence-capped Overall 6.0 抬到 >= 7.0。R114–R121 八轮各审计一层流程 / 基础设施；R122 完成 R106 §6 **R4**（arXiv v2 双摘要一手字节）；R123 完成 **R1**（gap 1 一手许可与代码路径文本）。

本轮**不写第 9 层流程审计、不写 G0 文字补丁、不碰须批准的机器门、不创建 v4、不在 G0 未过时启动 P3**，改做用户第 1 步 ① 明确授权、且 R106 §6 清单中**最后两项不需 designated gate owner 裁决的一手动作**：**R3**（2026 几何研究改一手来源、标明版本、重核 `p<10^-13` / trained ER / OFF 完全闭合、记录二手镜像取证状态）与 **R5**（W5/W8 事实错误的一手字节核验）。并首次给出 **R106 §6 R1–R9 逐条收敛表**，把剩余阻塞精确收敛到 `R120-CONSOLIDATED-DECISION-REGISTER.md` 的最小裁决集 `G1 + G4 + G10`。

**取证完成 ≠ gap 闭合**：矩阵定稿 / registry 登记 / gate judgment 分属 R120 的 **G6 / G7 / G4**，须 designated gate owner 书面裁决；心跳不自行回写、不自我认证。

## 3. 一手冻结件（13 份 / 323,740 B / 8×200 + 1×301 + 4×429）

`raw/` 下全部为第三方公开小文本，SHA-256 锚定于 `R124-SOURCE-MANIFEST.json`，采集映射见 `R124-ACQUIRE.py`。零数据集 / 权重 / 二进制 / 大文件 / 本机路径 / 本项目凭证（verifier I 组 6/6）。最大单件 64,741 B。

| 来源 | 件 | 状态 |
|:--|:--|:--|
| bioRxiv 官方 details API | `biorxiv-api-details.json` | 200 / 64,741 B；12 个版本记录 |
| 同 API `/1` 后缀 | `biorxiv-api-v1-na.json` | 200 / 64,741 B；与 details 逐字节相同 ⇒ **该后缀不是版本选择器**（负面证据） |
| Crossref 官方 work API | `crossref-work.json` | 200 / 11,160 B；含 JATS 摘要 |
| Europe PMC 官方检索 | `europepmc-search.json` | 200 / 841 B；`hitCount=1` / `PPR1251441` |
| bioRxiv connect | `connect-biorxiv-relate181.html` | 200 / 58,714 B；辅助，不用于摘要主张 |
| 二手镜像 | `secondary-mirror-article.html` / `-followed.html` | 301 / 265 B → 200 / 37,429 B |
| arXiv 一手 abs ×2 | `arxiv-2609.39248-abs.html` / `arxiv-2610.13018-abs.html` | 200 / 43,328 B + 42,453 B |
| biorxiv v1/v3 页面 ×4 | `biorxiv-v1.html`、`-retry.html`、`-early-full.html`、`biorxiv-v3.html` | **全 429 / 17 B `error code: 1015`**（Cloudflare），原样保留为负面证据 |

## 4. 核心实质发现（全为第三方文本事实，严格收窄）

### 4.1 R3 版本谱系：API 的 `abstract` 是「当前摘要回填」，不是版本化历史摘要

bioRxiv 官方 `details` API 对 DOI `10.64898/2026.06.10.731214` 返回 **12 个版本**（v1 `2026-06-12` → v12 `2026-10-16`）：

- **v1 标题** `Connectome wiring shapes population-level neural geometry in the Drosophila visual system`；**v2–v12 标题**（11 个）全部为 `Representational geometry as a fidelity metric for connectome-constrained networks: evidence from the Drosophila visual system` ⇒ 标题在 v1→v2 之间改变，与 API 版本元数据可逐字节复算。
- **12 个版本的 `abstract` 字段完全相同**：各 4,816 字符、`sha256` 前缀同为 `555e28f9fef3`，内容逐字含 `p < 10-13 in every case`、`closes the gap completely`、`trained Erdos-Renyi on OFF-polarity structure`、`size-matched`、`Erdos-Renyi`。⇒ 该字段是**当前（最新）摘要回填到每一条版本记录**，**不能**把「API 里 v1 的 abstract」当作 v1 的历史摘要。
- 本轮首次探测曾取得 v1 HTML 页 HTTP 200 / 105,400 B（**未落盘**），其摘要为**阳性**版：`RSA Spearman r = 0.686 (p < 0.0001)`、`r = 0.846`、`r = 0.930 vs. r = 0.603`、`Δr = 0.327`；**不含** `p<10^-13` / `closes the gap` / trained ER。但 4 次重试全部 Cloudflare 429，**本地无 v1 页面字节冻结件** ⇒ 该阳性摘要仅作 WebFetch 转述登记，**不计入一手冻结件**（R122 教训：引用摘要必须声明端点；R123 教训：字段 ≠ 文本）。
- **Crossref** `abstract` 同为阴性版（`<jats:sup>−13</jats:sup>` U+2212 上标、`closes the gap`、`size-matched`、`Erdős–Rényi`），但 `created = 2026-06-12`（v1 日期）、`title` 为 v2+ 标题、`indexed = 2026-10-21` ⇒ **元数据层版本错配**：`created` 是首次发布日，不代表当前摘要版本。
- **二手镜像** `datePublished = 2026-10-16` 与 API **v12 日期逐字一致**，正文逐字含 `p < 10-13 in every case`、`closes the gap completely`、`trained Erdos-Renyi on OFF-polarity structure` ⇒ 镜像对应 **v12 口径**。
- **Europe PMC** `firstPublicationDate = 2026-06-12` / `firstIndexDate = 2026-06-15` / `hitCount = 1`，题目为 v2+ 标题。

**⇒ 对 R106 §6 R3 的严格处置**：R3 原文要求「标明具体版本（**v1 阳性 vs v3 大体阴性**）」。一手字节显示 **「v3 是结论转折版本」不成立**：v3 仅为 12 版之一（`2026-06-23`），API 不提供每版摘要，**无法从本地字节确定阴性结论首次出现于哪一版**。本轮只能收窄为：**v1 页面（阳性，无本地字节）vs 当前 / v12 口径（阴性，有 3 份独立一手字节：API abstract + Crossref abstract + 镜像正文）**，中间 10 版摘要未取得、不作版本归属主张。这是对 R3 可核验部分的**证据层闭合 + 明确负面结论**，**不主张 R106 判错、不回溯改写 R106 任何字节**（W6 当时基于 WebSearch 与二手镜像，其「存在版本歧义、矩阵引用二手镜像未标 DOI/版本」的中心判断成立）。

**⇒ 二手镜像取证状态须按时点分列**：R106 §3 记录该 URL「被 Cloudflare 拦截、无法直接取证」；本轮实测裸域 301 → `www` 后 **HTTP 200 / 37,429 B 可取证**。这是**时点 / 端点差异**，不是 R106 造假。镜像始终为**二手**，只用于交叉印证 v12 口径，**不作为一手结论来源**；R3 要求的「记录负面结论」在本轮取到正文的前提下改为「记录取到正文 + 端点与时点 + 二手性质」。

### 4.2 R5 三处事实错误的一手核验

| 项 | 一手字节 | 结论 |
|:--|:--|:--|
| W8 Park Zenodo | `arxiv-2609.39248-abs.html` 逐字含 `22871090` **1 次**、`22891264` **0 次**；`Submitted on 30 Sep 2026` | 更正值 `22871090` 确证 |
| W8 Dhawan 日期 | `arxiv-2610.13018-abs.html` 逐字含 `9 Oct 2026` **2 次**、`12 Oct 2026` **0 次**；`[v1] Fri, 9 Oct 2026 05:20:38 UTC`（标签清洗后） | 更正值 `2026-10-09` 确证 |
| W5 v1 摘要误归属 | `R106-ROUND-AUDIT.md` 已有「核心指控不成立，已撤回」**只追加补录**；R122 一手字节坐实「两个措辞不同的 v2 摘要并存」 | 已撤回，本轮**不重复补正、不改写历史字节** |

**不改写原字节**：`R106-G0-INDEPENDENT-RECENCY-VERIFICATION.md` §3.1、`R106-ROUND-AUDIT.md` §5.2、`R106-G4-POSITIONING.md` §1 的「均已独立复核」overclaim 全部**原样保留**。按 R5 纪律，更正只以本轮新增记录留痕；且 **R9 规定「更正动作本身不得自我认证」**，矩阵定稿 / 登记仍须裁决。

## 5. R106 §6 九项逐条收敛表（首次）

| 项 | 要求 | 本轮前状态 | 本轮增量 | 剩余阻塞 |
|:--|:--|:--|:--|:--|
| **R1**（gap 1） | 矩阵逐条补正 + 可复算附件 / 负面结论 | R123 13 份一手许可与代码路径件 | — | 归类 / 登记须 **G5 / G6 / G7 / G4** 裁决 |
| **R2**（gap 2） | 矩阵定稿 + SHA 重新冻结 | 9,445 B 原样，stale 表述仍在 | — | **G6** 裁决 |
| **R3** | 几何研究改一手、标版本、重核结论、镜像负面结论 | 矩阵仅二手镜像 URL，无 DOI / 版本 | **本轮 13 份一手件 + 145/145 复算 + 口径收窄** | 登记 / 定稿须 **G6 / G7**；v1 页面本地字节未取得 |
| **R4** | Kuklev v2 SHA 冻结件 + 登记 manifest | R122 5 份 raw / 321,571 B | — | 登记进 `source-manifest.json` 须 **G7** |
| **R5** | 更正 W5/W8 事实错误（新增补正记录） | R106 自身已有只追加补录 | **三处更正值一手字节确证** | 更正动作不得自我认证 ⇒ **G4 / R9** |
| **R6**（gap 4） | gate owner 显式 scientific/visual gate judgment | 无 | — | **G4** 裁决 |
| **R7** | G0 `inputs`/`evidence` 登记 + 显式 `passed` + 冻结 pass criterion | `inputs=[]` / `evidence=[]` / `pending` 原样 | — | **G4** 裁决 + W13 |
| **R8** | 重新冻结完整 G0 证据包 | 未完成 | — | 依赖 R1–R7 |
| **R9** | 全新独立审查复核四 gap | 未完成 | — | 依赖 R1–R8 |

**⇒ 心跳可自主完成的 R106 §6 清单项（R1 / R3 / R4 取证 + R5 一手核验）在本轮全部穷尽**；剩余 R2 / R6 / R7 / R8 / R9 全部落在 designated gate owner 裁决，精确收敛到 R120 最小集 **`G1 + G4 + G10`**（G2/G3/G5/G6/G7/G8/G9 为依赖或细化）。这与 R111「自主可达动作穷尽」一致，本轮首次把该判断坐实到 **R106 §6 清单逐项 + 一手字节**层级。

## 6. 双门只读读数（本轮采集时刻）

| 门 | 读数 |
|:--|:--|
| `validate_single_paper.py --threshold 7.0` | **`NOT_QUALIFIED`** · `overall_score=6.0` · `threshold=7.0` · `>=` · `score_meets_threshold=false` · `score_gt_threshold=false` · D1✓ D2✗ D3✗ D4✓ D5✗ · `all_pass=false` |
| `guard check -l guard/ledger-null-ladder.json` | **`INCOMPLETE`**（退出码 1；A2 / A6 FAIL，S1–S7 全 pending，动作序列 0 条，无超限重复动作）；报告写 `/tmp` 未入项目树 |
| guard ledger SHA | `73043b4e164a5a5f…` 前后一致 ⇒ 纯只读 |
| 主线 `pipeline-state.json` | `f-guidance-builder-v1` / `v2` / 12 阶段；`CCFA-startup=passed`、**G0–G8 / validation / handoff 全 `pending`**、`G0.inputs=[]` / `evidence=[]` / `gate_verdict=pending` |
| 结构权威采集时刻 SHA | `goal-ledger.md` `377b241f7af94d08…` · 主线 state `bcb48bb964e657a4…` · guard ledger `73043b4e164a5a5f…` |

A6 双口径（criteria `>=7.0` / ledger `严格 > 8.0`）为 R109 / R111 / R120 **已知问题**，属 G2 裁决项，本轮只读登记不改。

## 7. 可复算性与 v1 缺陷留痕

`R124-verify.py` **不 import 采集模块、不把任何 R124 产出的 JSON 当实质数据源**（SOURCE-MANIFEST 仅用于 A 组声明式 SHA / 字节一致性核对），B–I 组全部从源字节与项目独立文件用自有逻辑重算，零网络访问 ⇒ **145 检查 / 145 MATCH / 0 MISMATCH**（A 45 / B 27 / C 14 / D 10 / E 6 / F 9 / G 16 / H 12 / I 6）。`scope_note` 明确 A 组为同机必然一致性核对、非独立交叉核验（R115 W4）。

**v1 缺陷（6 项 + 1 项采集缺陷，全部留痕、v1/v2 两版全保留）**：

| 编号 | 缺陷 | 性质 | 处置 |
|:--|:--|:--|:--|
| M-1 | `R124-BUILD-MANIFEST.py` 直接 `from R124_ACQUIRE import ...` 失败（模块文件名含连字符） | 脚本错误 | 改 `importlib.util` 按路径加载，两版均留在同一文件注释 |
| V-1 | verifier F 组 `expected` 为 bytes，`json.dump` 不可序列化 | 脚本错误 | 加 `_jsonable()` 归一，仅影响报告输出、比较逻辑不变 |
| V-2 | `api_versions_1_to_12` 期望 int，API 实为 str | 期望值假设错误 | v2 改 `[str(i) ...]` |
| V-3 | Crossref 上标期望 `10</jats:sup>`，实为 `&lt; 10 <jats:sup>−13</jats:sup>` | 期望值假设错误 | v2 断言真实字节形式 |
| V-4 | 镜像期望 `p &lt; 10-13`，实为明文 `p < 10-13` | 期望值假设错误 | v2 断言明文 + 显式断言转义形式 0 命中 |
| V-5 | arXiv 时间戳期望连续串，实为 `<strong>[v1]</strong>` 换行分隔 | 期望值假设错误 | v2 清洗标签 / 空白后断言 |
| C-1 | v1 HTML 页首次 HTTP 200 / 105,400 B **未及时落盘**，之后 4 次全 429 | 采集缺陷 | 如实登记「无本地字节冻结件」，不以 WebFetch 转述冒充一手件 |

v1 输出 `R124-VERIFICATION-V1.json`（145 / 141 / 4）与 `R124-verify-v1.py` 原样保留；`R124-VERIFICATION.json` 为 v2 结果。**全部 7 项均非数据不一致、非编造、非报告事实错误**。

## 8. 严格边界

全 `READONLY_R3_R5_FIRST_HAND_ACQUISITION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`：

- **零状态写回**：`pipeline-state.json` / `literature-baseline-matrix.md` / `literature-search/source-manifest.json` / `goal-ledger.md`（采集时刻）/ 门配置字节全部零改动；**零门晋级**（G0 pending）、零自我认证、零 `passed` / `gate_verdict` / `history` 改动。
- **EXEC LOCK**：零前向 / 推理 / 训练 / 标签 / 数据集 / EPE·l2 / 科学指标 / 新正向证据；零注入；本轮网络仅用于只读取证。
- 未改历史字节 / 评审 / 分数 / 阈值 / 稿件 / 门 / 冻结件 / registry / 门配置；未起 `ccf-paper-reviewer full`、未产生 `**Overall:**` 数值行、未自评 governing、未跳门、未创建 v4、未在 G0 未过时启动 P3、未假定 `≤32h / K=45` 授权（D1 维持 `BLOCKED_ON_CONFIRMATION`）、无 4090 / L4 / H20 主张。
- 主项目未投稿 / commit / push；心跳 ACTIVE 调度 `FREQ=HOURLY;INTERVAL=1;BYMINUTE=0,30` 无变化。
- **增量是证据层、不是分数层**：按 R121 已确立的否定性闭环（R95 §13 evidence-capped overall），一手文献冻结件**不改变 governing 6.0、不构成达标进展**，明确不把取证完成包装成靠近达标。

## 9. 结果

第 3 步前置（**实质正向新科学证据**）未满足 ⇒ 不进稿件新副本、不做 9 页合规编译、不起全新隔离 full 评审。**0 篇达标、未写 COMPLETE**；governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`；G0 pending、零门晋级 / 零自我认证 / 零状态改动。停止门只剩 ①达标（>= 7.0）②用户叫停。

## 10. 交下轮

1. 回收本轮全新隔离独立审查、结论与更正**只追加**于新检查点；报告原文与历史正文零改动。
2. 13 份件的**归类与登记**（是否并入矩阵 / `source-manifest.json`、v1 页面本地字节是否补取、R3 版本口径如何入矩阵、W13 pass criterion 书面冻结）须 designated gate owner 依 **G1 / G4 / G6 / G7** 书面裁决；心跳不回写。
3. 以 `R120-CONSOLIDATED-DECISION-REGISTER.md` 为唯一决策入口，最小裁决集 **`G1 + G4 + G10`**；心跳不自我认证、不自行修复机器门、不自行创建 v4。
4. 唯一 admissible 路径仍是按序 G0–G8（G4 正面处理 Kuklev v2 §7.3 / §8 / §9）→ validation → handoff → P0 → P1A/P1B → P2 → **P3 baseline-first 真实前向**取得实质正向新证据 → 稿件新副本 → 9 页合规编译 → 全新隔离 full 评审（不透露期望分）；`X >= 7.0` 且 QUALIFIED + COMPLETE 才写 COMPLETE。门槛降低不降低证据质量。
5. **新教训**：① 预印本 API 的 `abstract` 字段可能是「当前摘要回填到全部版本记录」，**字段位置 ≠ 版本归属**；引用必须声明端点与版本口径，中间版本的摘要未取得就不得作转折版本主张。② `Crossref.created` 是首次发布日，不等于当前摘要版本；元数据层可存在版本错配。③ 二手镜像的「不可取证」是**时点 / 端点状态**，须记录 URL、重定向链、HTTP 状态与字节，不得回溯改写历史记录；镜像即使可取证仍是二手，只作交叉印证。④ 首次探测成功但未及时落盘的页面，后续限流即不可复算 ⇒ 一手件必须**即时落盘 + SHA**；WebFetch 转述不得冒充字节冻结件。⑤ 分类汇总数字须程序逐字节求和（本轮 323,740 B 由 manifest totals / 逐文件求和 / verifier 三处交叉核对）。

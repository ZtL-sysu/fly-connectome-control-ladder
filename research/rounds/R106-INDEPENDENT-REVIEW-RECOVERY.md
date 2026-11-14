# R106 独立 gate review 回收 + 事实更正 + Concern-to-action

状态：`DISCLOSURE_AND_ACTION_LEDGER_ONLY_NOT_SCIENTIFIC_RESULT`。
回收时间：2026-11-13 03:5x–04:0x +0800（自动化 `b88e368e` 心跳 R106 的异步结果回收）。

## 0. 结论照录（首行逐字，不改写、不删、不藏）

`gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md`（189 行 / 31,292 B，
SHA256 `919d05c477ec2421ba3f958e09d7e640fb3c3033064272ddbdd46cf892b17450`）：

```
**Verdict:** PARTIAL | **G0 may be passed:** NO
**Scientific result claimed:** NO
```

**报告原文未改一个字节。** 全新隔离 reasoning 子代理，所有 SHA 从原始字节重算、
所有一手引文自己 WebFetch / WebSearch 取得，明确未采信 R106 的任何转述。

### 性质界定（防止口径漂移）

- 这是**门审查**（G0 gate review），**不是** `ccf-paper-reviewer full` 稿件评审
  → 无 `**Overall:**` 行、无数值论文分、不产生分数行、**不改变 governing**：
  仍 R95 = 6.0 / `NOT_QUALIFIED` / `INCOMPLETE`，**0 篇达标、未写 COMPLETE**、
  未起新 full 评审。
- **PARTIAL 不是 FAIL**：字节层面证据包诚实可复算（8/8 文件 SHA、12/12 门状态、
  8/8 Sintel npz、10/10 官方模型文件、5/5 保存 HTML、6/6 隔离副本全真）；
  扣分全部是 gap 未闭合、事实错误、登记失配与残留局限，**非数学错误、非红线违规**。
- 裁决明确：**G0 不得标 PASSED，维持 `pending`**。本轮遵守，不追认、不静默晋升。

## 1. 我（主会话）上一轮的三处事实错误 —— 据实承认，不掩饰

独立审查的 W5 / W8 推翻了我 R106 §3.1 的**核心叙事**。我随后用一手来源
**自己交叉核验**，确认审查成立、我的判断错误：

### 1.1 W5 [HIGH]「R99 引用 v1 摘要、版本错配」—— **不成立，撤回**

| 一手来源 | 实测 |
|:--|:--|
| `/abs/2609.24565v1` | v1 标题为 *Active Visual Sampling with a Connectome-Constrained Fly Model for One-Shot Hatch Recognition in Architectural Drawings*；摘要收束句逐字为 `while the topology contribution and end-to-end BIM utility remain open questions.`；**不含** `Exact structure remains insufficient…` |
| `/html/2609.24565v2` **论文正文 Abstract 块** | 最后一句逐字为 `Exact structure remains insufficient to beat what the moving retina already provides.`；**不含** `Longer observations…` |
| `/abs/2609.24565` **arXiv 元数据摘要** | 含 `Longer observations reverse the circuit-receptor ordering once the stimulus spans a period, but not through T4/T5.`，并以 `Thus active sampling and exact structure matter, …` 收束 |

⇒ **arXiv 上并存两个措辞不同的 v2 摘要**。R99 引用的是 **v2 论文正文摘要**，
**引用正确、没有版本错配**；是我把元数据摘要当成唯一的「v2 摘要」，
误判 R99 引了 v1。我 R106 §3.1 的核心发现**不成立**，据此写下的
「R99 结论 stale」叙事**一并撤回**。

**错误已扩散到 6 处登记**（`R106-G0-INDEPENDENT-RECENCY-VERIFICATION.md` §3.1、
`R106-ROUND-AUDIT.md` §5.2、run root `correction-ledger.md` R106 段、
`goal-ledger.md` R106 段、`papers/R63-results/STATUS.md` R106 段、
`correction-loop-state.md` R106 段、`.workbuddy/memory/2026-11-13.md`、
automation memory）。按 RGE 纪律 **一律不改写历史字节**，只以本文件 +
各登记点的**追加补录**更正，原文保留、不删不藏。

### 1.2 W8 [MEDIUM] 两处标识错误 —— 更正

| 项 | 我 R106 写的 | 一手核验 | 说明 |
|:--|:--|:--|:--|
| Park 2026 Zenodo | `22891264 v4.0` | `/abs/2609.39248v1` Comments 逐字为 `https://doi.org/10.5281/zenodo.22871090` | 我写的是检索命中的 `zenodo.org/records/22891264`（Version 4.0, 2026-09-22）。**一手规范引用应为 DOI `10.5281/zenodo.22871090`**；两个编号是否为同一记录的不同版本，**本轮未核实，登记为 OPEN**，不把「另一个 record 存在」说成编造 |
| Dhawan / FlyHack 日期 | `2026-10-12` | `/abs/2610.13018` = `Submitted on 9 Oct 2026`、`[v1] Fri, 9 Oct 2026 05:20:38 UTC` | **更正为 2026-10-09**；`10-12` 来自第三方转载站（ChatPaper / SciRate）的收录日，不是 arXiv 一手提交日 |

### 1.3 W10 [MEDIUM] overclaim —— 承认

`R106-G4-POSITIONING.md` §1 标题写「四篇一手 prior art（**均已独立复核**）」，
但同表第 4 行自认「2026 几何研究**本轮未独立复核**」，且把两篇塞进一行（实为 5 篇）。
标题与表体自相矛盾，属 overclaim，如实登记。

### 1.4 W9 [MEDIUM] 冻结失配 —— 我独立复算确认属实，并说明根因

`R106-END-OF-ROUND-FREEZE.json` 声明 `all_copies_byte_identical: true` / 7/7 一致。
我的独立复算：`R106-ROUND-AUDIT.md` 声明 `10457 B / 06299a15e5c9…`，
实际 `11743 B / 772036905edf…`，`isolated/` 副本仍为旧版 ⇒ **该声明为假**。

**根因（不掩饰）**：该冻结清单生成于追加 §10 收尾补录**之前**；随后我在
03:56 向 `R106-ROUND-AUDIT.md` 追加 §10，主文件字节改变，但冻结清单与隔离副本
**未同步更新** ⇒ 声明在追加后失效。这是**登记缺陷**，不是哈希伪造；
按 N1 纪律**不补造、不改写旧清单**，只新增 `R106-POST-REVIEW-FREEZE.json`
覆盖当前全部字节并如实标注前一份已 stale。

> 这是同类登记缺陷**第三次出现**（R104 N1、R105 W11 均因「先变更后冻结 /
> before 不可独立复算」被独立核验指出）。如实累计，不淡化。

## 2. G4 结论：**保留；论据必须更正**

独立审查 §5 判定 `R106-G4-POSITIONING.md` 的**中心判断 defensible**，
并独立逐字确认 v2 §7.3/§8：判别变量（观测时长是否跨一个刺激周期）、
8 帧落后 `0.011` → 20/34/60 帧领先 `0.018/0.021/0.022`、
变化量 `+0.033 [0.015,0.050]`、频谱带 `+0.085~+0.102`、
「T4/T5 贡献不随观测长度增长」`+0.008 [−0.003,0.018]`、
§8 `That prediction was run, and it half held.`

⇒ **「判别性预测何时路径重要」轴已被部分抢发、G4 风险上调，这个结论独立成立**，
**不因 W5 被推翻而改变**；但支撑它的**「R99 版本错配」论据不成立，必须撤回**。
**结论保留、论据更正**。仍开放的只有更窄的机制问题：
`The remaining question is which stage integrates the extra time, and a
per-type tuning analysis over the sweep would answer it.`

G4 **维持 `pending`**、风险维持上调；定位陈述仍是**计划不是结果**。

## 3. Concern-to-action（W1–W13 / R1–R9）

处置代号：**REGISTER**＝如实登记、**FIX_IN_THIS_ROUND**＝本轮以新文件补齐、
**DEFER→OPEN**＝保留为残留局限交下轮、**BLOCK**＝阻断 G0 通过。

| 编号 | 处置 | 说明 |
|:--|:--|:--|
| W1 门状态与证据数组为空、无 gate owner pass 记录 | **BLOCK + REGISTER** | `pipeline-state.json` G0 `inputs:[]` / `evidence:[]` / `pending`；不追认 |
| W2 / W3 / W4（R98 gap 1/2/4 未闭合，gap 2 已恶化） | **BLOCK + DEFER→OPEN** | 矩阵仍含「the open question Kuklev leaves」这一已被 §7.3/§8 证伪的表述；本轮**不回写矩阵**（避免补丁式文字修复） |
| gap 3（独立 gate owner recency） | **PARTIAL** | 本独立审查确实用一手抓取确认 recency，但 verdict = NO、designated `ccf-literature-searcher` 无签署、secondary hit 未复核、Kuklev 无本地一手件 |
| **W5（我的 v1/v2 误归属）** | **FIX_IN_THIS_ROUND（本文件 §1.1 撤回）+ REGISTER** | 6 处登记的追加补录见 §5；历史字节不改 |
| W6 secondary hit 版本歧义 | **DEFER→OPEN** | 独立审查抓到主 URL 被 Cloudflare 拦截，底层 bioRxiv DOI `10.64898/2026.06.10.731214`（Zhou & Hasler），**v1 阳性 / v3 大体阴性**；矩阵只引二手镜像、无 DOI / 版本号 |
| W7 最关键 prior art 无本地一手冻结件 | **DEFER→OPEN** | `source-manifest.json` 仅 5 条、**无 `2609.24565`**；R98 曾称「23 saved public sources」与 manifest 不符 |
| W8（Zenodo 编号 / Dhawan 日期） | **FIX_IN_THIS_ROUND（本文件 §1.2 更正）+ REGISTER** | 编号关系未核实部分登记 OPEN |
| W9 冻结失配 | **FIX_IN_THIS_ROUND** | 新增 `R106-POST-REVIEW-FREEZE.json` + `isolated-post-review/`；旧清单原文保留并标注 stale |
| W10 G4 §1 overclaim | **REGISTER** | 见 §1.3；不改写已冻结定位文件 |
| W11「逐字吻合」措辞松 | **REGISTER** | 数值全真，HTML 转写有重复排版；非编造 |
| W12 独立结论在回收前缺位 | **CLOSED（本报告落盘）** | 报告 verdict = NO，已据实登记 |
| W13 `fail-fast-gates.md` **无 G0 成文 pass criterion** | **DEFER→OPEN（结构性）** | 任何 G0 PASS 都须先书面冻结 G0 通过条件，否则不可复算；本轮不自行发明判据 |
| R1–R9 | **DEFER→下轮，不本轮偷偷闭合** | 逐项见报告 §6；R9 明确要求 R1–R8 后由**新的**独立审查复核，更正动作不得自我认证 |

**本轮不做补丁式文字修复、不出 v4、不重开 D1 / 判别式 v3、不改写矩阵、
不自行冻结 G0 判据、不标任何门 passed。**

## 4. 纪律（逐条）

- 独立审查**报告原文未改一个字节**；本轮全部更正只写入**新补录**与登记点的**追加段**。
- 不把 PARTIAL 解释为分数下降或「已通过」；门审查非稿件 full 评审，
  **不产生 `**Overall:**` 行、不改 governing**。
- 未改任何历史报告 / 评审 / 分数 / 阈值 / 冻结件 / 稿件 / gate 状态；
  未自评当 governing、未起新 full 评审、未跳门 / 批量标 passed / stale evidence 晋级。
- EXEC LOCK 零前向 / 零训练 / 零标签 / 零数据集；零 `pickle.loads`。
- 未重开 D1 / 判别式 v3、**未假定 ≤32h / K=45 confirmation 授权**；
  用户决策点仍待答复。未投稿 / commit / push；心跳 ACTIVE 无调度参数变化。

## 5. 六处登记与交接

本回收已追加至：`goal-ledger.md`、`papers/R63-results/STATUS.md`、
`correction-loop-state.md`、`.workbuddy/memory/2026-11-13.md`、
run root `correction-ledger.md`、`R106-ROUND-AUDIT.md` §11、automation memory。
每处均明确「上方 R106 段的版本错配叙事**不成立**，以本回收为准，原文保留不改」。

**结果**：**0 篇达标，未写 COMPLETE**，governing 仍 R95 = 6.0 / Confidence 4.0。
停止门只剩 ①达标 ②用户叫停。

**下轮交接（优先级）**：① 按 R1–R9 闭合 G0（先做 R4/R5 的一手保存件与事实更正、
R2 矩阵定稿、R1 许可文本逐条核验、R3 bioRxiv 一手版本），**不得自我认证**；
② W13：书面冻结 G0 的 pass criterion（`fail-fast-gates.md` 无 G0 定义）；
③ gap 4 须由 designated gate owner 落盘显式 scientific/visual gate judgment；
④ 之后由**新的**独立审查复核闭合，再由 gate owner 决定是否标 passed；
⑤ 按 U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state；
⑥ 按序 G1–G8 → validation → handoff → P0 → P1A/P1B → P2 → P3 真实前向（解决 U5）；
⑦ 只有 `failed_runs=0` + 全 finite + 独立复算吻合 + **实质正向新证据**，
才进稿件新副本目录、9 页合规编译、起全新隔离 full 评审；
X>8.0 且 QUALIFIED+COMPLETE 才写 COMPLETE。

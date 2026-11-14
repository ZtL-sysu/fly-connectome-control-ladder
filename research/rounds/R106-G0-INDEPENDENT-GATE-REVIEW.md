**Verdict:** PARTIAL | **G0 may be passed:** NO
**Scientific result claimed:** NO

# R106 — G0 独立 gate review（全新隔离子代理，主会话零输入预期）

审查对象：`gate-G0-R106/` 全轮 G0 证据包 + `gate-G0-evidence-review-R98.md` + `gate-G0-recency-review-R99.md` + `literature-baseline-matrix.md` + `pipeline-state.json`。
权威依据：`/Users/xhf/.workbuddy/skills/f-guidance-builder-v1/assets/pipeline-definition.json`、`/Users/xhf/.workbuddy/skills/f-guidance-builder-v1/references/fail-fast-gates.md`。
方法：所有 SHA 与门状态均用 `/Users/xhf/miniconda3/bin/python` 从磁盘原始字节独立重算；所有一手文献结论均用 WebFetch/WebSearch 直接抓取一手页面，**不采信 R106 的任何转述**。本报告只做门审查，不做稿件评审，不产生 `**Overall:**` 行，不赋数值分。

> 范围说明：审查期间 `gate-G0-R106/` 目录由另一并发进程继续落盘（03:44–03:56 新增 7 份产物与 `isolated/` 副本）。这些文件**不是我创建的**；我已把它们一并纳入审查，但 `R106-G0-EVIDENCE-FREEZE.json`（03:41:30）并未覆盖它们，见 W9。

---

## 1. 独立重算结果（精确值）

### 1.1 `R106-G0-EVIDENCE-FREEZE.json` 的 8 份字节 SHA

freeze 文件自身 SHA256 = `ebc1f4b020e381b7e86f2a677a5be2c72f1e38fc8b6ff6118b99269b71034006`（3172 B）。逐条从原始字节重算：**8/8 全吻合**（SHA、bytes、exists 三项均一致）。

| 文件 | 声明 SHA256 | 我的重算 | bytes | 判定 |
|:--|:--|:--|---:|:--|
| `literature-baseline-matrix.md` | `31b5098b4df2718ddf15d0b4613daa4d819a19319bbc15b731fb58d3903da9b2` | 同 | 9445 | OK |
| `gate-G0-recency-review-R99.md` | `4eb1df8ddebb15d5eb934b0060fef49eb4a84902940ffae401b367172ea06046` | 同 | 4974 | OK |
| `gate-G0-evidence-review-R98.md` | `6bccf27dcb75dab8d45c37a80bd56724583ffc4e6d3859b7ef81b9b2bafd8ea9` | 同 | 3742 | OK |
| `ccfa-startup-packet/candidate-E-local-v2/prior-art-opportunity-map.md` | `248bcf04d57b34b8d354998c69fb8fd4684080f61e0e9a00a5a37d4460bb9be0` | 同 | 3163 | OK |
| `pipeline-state.json` | `bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d` | 同 | 3723 | OK |
| `execution-contract-v2.md` | `20bddbb80b29e26e38c666389a853df9847f643187623353192c71439294f29b` | 同 | 2648 | OK |
| `execution-contract-v3.md` | `1630832599cb884064251c5dde8e22d00018dad1c910ca6b7055233bf51af302` | 同 | 4556 | OK |
| `R99-design-block-decision.md` | `9b07d5698fd7e051fa0daf2c32422c1db2086490f7e8fc02f4538958e29eb245` | 同 | 5120 | OK |

`pipeline_state_sha256` 声明 `bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d`，与磁盘 `pipeline-state.json` 实际 SHA 一致 → **MATCH**。

### 1.2 门状态快照

`gate_status_snapshot` 12 条与 `pipeline-state.json` `stages` **12/12 全吻合**，且顺序与权威 `pipeline-definition.json` 的 `["CCFA-startup","G0","G1","G2","G3","G4","G5","G6","G7","G8","validation","handoff"]` 完全一致：`CCFA-startup=(passed, pass)`；`G0..G8 / validation / handoff=(pending, pending)`。**没有任何门被静默标为 passed**。

freeze 自报 `gates_mutated=false / model_forward_passes=0 / training_runs=0 / labels_used=0`；可观测后果我另行核验：`pipeline-state.json` mtime = `2026-11-12 10:43:12`（早于 R98 15:15、R99 16:45、R106 03:20），R106 窗口（11-13 03:00 之后）被写入的文件只有 `gate-G0-R106/*` 新增产物与 `correction-ledger.md` 的一次 03:49:26 追加登记；**没有任何分数/阈值/评审/稿件/冻结件/gate 状态文件被改动**，也未生成 `guidance.md`。

### 1.3 超出任务范围仍独立复算的旁证（全部为真）

- `R106-ASSET-SHA-VERIFICATION.json`：8/8 Sintel npz 的 SHA+bytes 与我从字节重算一致；`render_manifest_sha256`=`ad4d418eb5b3a60baf5c12810ca6b17d9662c1c06a68b7bc2b2e83b20c95daa5` 一致；官方 `model000`/`model001` 共 10/10 文件 SHA 一致；`identities_file_sha256`=`d115fd5d5ffb6761fa8052bf72b97d76ea88a140c47d849cba474d87da93fff5` = `code-audit/official-model-input-identities-v1.json` 实际 SHA。注意这验证的是**本项目自有本地资产**，不是矩阵里那批第三方 prior-art 条目。
- `R106-LITERATURE-SOURCE-SHA-VERIFICATION.json`：5/5 保存的一手 HTML 的 SHA+bytes 与 `literature-search/source-manifest.json` 声明一致（`toposens2026/boundary2026/flyhack2026/structure2026/flyvis2024`）。**但 `source-manifest.json` 只有 5 条，且没有任何 `2609.24565`（Kuklev）保存件**。
- `R106-PRE-REVIEW-FREEZE.json`：6/6 主副本与 `isolated/` 副本 `cmp` 逐字节一致。
- `R106-END-OF-ROUND-FREEZE.json`：**6/7 吻合，1 条失配** —— `R106-ROUND-AUDIT.md` 声明 `10457 B / 06299a15e5c9…`，磁盘实际 `11743 B / 772036905edf…`；主副本 11743 B、隔离副本 10457 B，`cmp` 不同 ⇒ 该文件的 `all_copies_byte_identical: true` 在我读取时**已为假**（见 W9）。

### 1.4 权威标准的适用边界（独立读取）

`pipeline-definition.json` 把 G0 列为 stage，但 `fail-fast-gates.md` 的 "Gate Order" **从 G1 开始，全文没有 G0 的定义**；G0 的「Recent literature and baseline map (hard block)」及其通过口径是 R98 在项目内自行界定的。也就是说，本门**没有权威的、成文的 pass criterion**，其判据来自 R98/R99 的证据审查本身。这是做出 PASS 决定时不可忽略的结构性缺口（W13）。

---

## 2. R98 四个 gap 逐条 CLOSED / OPEN

| Gap | R98 原文要求 | 判定 | 可核验证据 |
|:--|:--|:--|:--|
| **1** | 矩阵中若干条目仍为 `asset contents/license not yet individually verified` / `project code path not yet verified`（R98 §G0 第 1 条，行 31–35） | **OPEN** | 矩阵 `literature-baseline-matrix.md` 第 9 行（Correig-Fraga `asset contents/license not yet individually verified`）、第 10 行（Dhawan `project code path not yet verified`）、第 24 行（`Optical-flow benchmark, pretrained checkpoints and natural clips require separate asset/license checks before being claimed complete`）三处标注**原样保留**；矩阵 mtime = `2026-11-12 16:46:17`，R106 未回写。R106 自己的 `R106-G0-GAP1-ASSET-CHECK.md` 第 20 行逐字写「**R98 gap 1 未整体闭合**：Correig-Fraga 归档内容/许可与 FlyHack 代码路径仍是 OPEN」，第 13 行「FlyHack 项目代码路径仍**未验证**」。`R106-ASSET-SHA-VERIFICATION.json` 只覆盖本项目自有 Sintel/官方 checkpoint 的字节完整性，**没有读任何 LICENSE 文本**，不能替代第三方条目的许可核验。R106 recency verification 第 133–134、150–151 行亦自认 gap 1 未闭合。 |
| **2** | 矩阵须 **final** 后才能叫 G0 complete（R98 §G0 第 2 条，行 36–40） | **OPEN（且已恶化）** | 矩阵第 39、46 行仍写 Kuklev 留下「*the open question Kuklev leaves*」/「*discriminating prediction of when path preservation matters versus when the input alone suffices (the open question Kuklev leaves)*」。我独立核验 v2 §7.3/§8 已把「when」这个判别变量、效应量、方向与阴性机制结论**全部发表**（见 §3），故该句现为**已知错误陈述**。R106 §3.2 第 113–117 行、§6.2 第 146–147 行明写「**必须并入 G4 定位，否则矩阵仍是 stale 的**」——这是待办，不是已完成。R106 拒绝修改矩阵（§5 第 135–136 行），矩阵字节自 11-12 16:46 未变。一张已知含错误结论、且补正尚未并入的 map 不可能是 final。 |
| **3** | 本会话未跑新检索；须由 gate owner（`ccf-literature-searcher`）独立确认 recency；主会话读既有矩阵不算独立 gate review（R98 §G0 第 3 条，行 41–44） | **PARTIAL（不足以支持 PASS）** | R99 做了 live web check，但 R99 自述为主会话侧；R106 标题与第 1、6–8 行逐字自认「**主会话侧记录，非独立 gate review**」「**不是 G0 gate owner 的独立审查**」，第 9 行把独立审查明确外包给「全新隔离子代理」（即本报告），§6.5 第 151 行「**无独立 gate owner 审查结论前 G0 保持 pending**」。本次审查确由隔离代理用一手 WebFetch/WebSearch 独立确认了 recency（见 §3），但：① designated gate owner（`ccf-literature-searcher`）没有签署记录；② 本报告的 verdict 是 NO；③ recency 覆盖不完整——2026 几何研究 secondary hit 未由 R106 复核（R106 §1 第 34 行、§6.5 第 150 行、GAP1 检查第 25–26 行），矩阵中最关键的 Kuklev hit 也没有任何本地保存的一手字节（W6/W7）。 |
| **4** | validator 明确「`scientific/visual gate judgment remains required`」，它只查 ordered/current evidence（R98 §G0 第 4 条，行 45–46） | **OPEN** | R98 自身是 evidence review；R99、R106 全部状态为 `*_NOT_SCIENTIFIC_RESULT`；R106 §6 标题为「**交 G0 gate owner 的实质输入**」（第 143 行），即把结论交给 gate owner，而非做出判断；`R106-ROUND-AUDIT.md` §7 复述 validator `--before G0` 仍返回 `PASS: ordered, current evidence; scientific/visual gate judgment remains required.`，`--complete` 返回 `ERROR: delivery requires every stage passed`。全包中**没有任何一份**记录了对文献/基线图的 scientific/visual gate judgment。本报告是门审查，且其结论为 NO，不构成放行所需的判断。 |

补充：`pipeline-state.json` 中 G0 的 `inputs: []`、`evidence: []`（行 65–66）为空——G0 的证据冻结件并未登记进 gate 自身的证据数组。

---

## 3. 一手来源独立核验（不采信 R106 转述）

来源：`https://arxiv.org/abs/2609.24565`、`/abs/2609.24565v1`、`/abs/2609.24565v2`、`https://arxiv.org/html/2609.24565v2`、`/html/2609.24565v1`、v2 PDF 镜像、以及 `2609.39248v1` / `2610.13018` 一手页面。

### (a) v1/v2 提交历史 —— 确认，R106 转录基本准确

`[2609.24565]` 页面逐字：
> "**[v1]** Mon, 21 Sep 2026 13:30:30 UTC (3,306 KB)"
> "**[v2]** Tue, 22 Sep 2026 12:24:47 UTC (3,306 KB)"

v2 Comments 逐字：
> "Major revision with a preregistered held-out evaluation, matched graph nulls, temporal sampling controls, real-drawing evaluation, and an ancillary animation"

（R106 引文漏了末尾 `and an ancillary animation`，非实质错误。）v1 是**不同标题**：`Active Visual Sampling with a Connectome-Constrained Fly Model for One-Shot Hatch Recognition in Architectural Drawings`；v2 标题为 `What Survives on Real Drawings: …`。作者 Dmitry Kuklev，cs.CV。

### (b) v2 摘要是否含「longer observations reverse the circuit-receptor ordering」—— **存在两个互相冲突的 v2 摘要，R106 只报了其中一个**

**YES（arXiv abs / 元数据摘要）**：`/abs/2609.24565` 与 `/abs/2609.24565v2` 的 `Abstract:` 逐字含：
> "Yet the intact circuit does not beat its moving retina, and T4/T5 silencing leaves both tasks intact. **Longer observations reverse the circuit-receptor ordering once the stimulus spans a period, but not through T4/T5.** Thus active sampling and exact structure matter, while clean-data practical performance remains dominated by task-trained networks and the useful transfer margin is largely retinal."

**NO（v2 论文本身的 Abstract 块）**：`/html/2609.24565v2` 的 `Abstract.` 块**不含**该句，其收束句逐字为：
> "Exact structure remains insufficient to beat what the moving retina already provides."

该句同样出现在 v2 PDF 全文（`it.arxiv.org/pdf/2609.24565`）摘要中。而 **v1 摘要（`/abs/2609.24565v1` 与 `/html/2609.24565v1` 两处一致）既不含该句，也不含 "Longer observations…"**，其收束句为：
> "The supported claim is therefore narrow: motion-oriented biological vision can be repurposed as a useful texture representation for architectural hatch matching, while the topology contribution and end-to-end BIM utility remain open questions."

⇒ **R106 §3.1 的核心指控（「R99 引用的是 v1 摘要措辞；v2 摘要不含该句」）与一手来源不符**：R99 引的句子**就在 v2 论文摘要里**，且**不在 v1 摘要里**。R106 把「v2 元数据摘要」当成唯一的「v2 摘要」，未披露两个 v2 摘要并存的事实。详见 W5。

### (c) §7.3 / §8 是否留「which stage integrates the extra time」的明确开放问题 —— **YES，逐字确认**

`/html/2609.24565v2` §7.3 逐字（保留 HTML 转写重复数字）：
> "Holding the pooled area fixed and varying only the number of analysed frames settles part of it. With the pool frozen, the circuit trails the receptors-only descriptor by 0.0110.011 at eight frames and leads it by 0.0180.018, 0.0210.021 and 0.0220.022 at twenty, thirty-four and sixty, so **the ordering reverses once the observation runs past a single period**; the change from eight frames is +0.033+0.033 [0.015,0.050][0.015,0.050]. … The mechanism, however, is still not the one we proposed: **the T4/T5 contribution does not grow with observation length**, at +0.008+0.008 [−0.003,0.018][-0.003,0.018] … These runs use a wider pool and a smaller eye than the headline configuration, so their absolute values are not comparable with the rest of the paper; only the differences within the sweep are."

§8 逐字：
> "That prediction was run, and it half held. … But the mechanism is not the one we named: the T4/T5 contribution does not grow with length. **The remaining question is which stage integrates the extra time, and a per-type tuning analysis over the sweep would answer it.**"

⇒ 判别变量（观测是否跨一个周期）、效应量 `+0.033 [0.015,0.050]`、方向（20/34/60 帧 circuit 反超）、阴性机制结论（不经 T4/T5）**均已发表**；仍开放的只是更窄的「哪个 stage 整合了额外时间 / per-type tuning」。

### (d) rewiring nulls 是否在 development split —— **YES，逐字确认**

§7.1 逐字：
> "On hatch matching, and **on the development split, since the held-out split was opened only for the model comparison**, rewiring the optic-lobe connectome while holding the edge count at 1,513,231 over 45,669 nodes drops accuracy from 0.857 to 0.539 when in- and out-degrees are preserved, to 0.586 when type pairs and transmitter signs are preserved as well, and to 0.500 for an Erdős–Rényi graph of the same density: paired differences of +0.318+0.318 [0.296,0.339][0.296,0.339], +0.271+0.271 [0.248,0.293][0.248,0.293] and +0.356+0.356 [0.334,0.379][0.334,0.379], each over three rewiring seeds with the invariants verified and the wiring hashed."

R99/R106 关于 split 归属的说法**正确**。

### 其余 R99 数字与引文的独立核验（全部为真，非编造）

| 项 | 一手逐字出处 | 判定 |
|:--|:--|:--|
| 分割 `0.483→0.089` IoU、`0.964→0.514` ROC-AUC、`0.397 [0.365,0.431]` | "collapses segmentation across three seeds: from 0.483 to 0.089 IoU, and from 0.964 to 0.514 ROC-AUC." / "The hierarchical paired difference is 0.3970.397 [0.365,0.431][0.365,0.431]." | 吻合 |
| R7/R8 正对照 `0.092 [0.079,0.104]` | "silencing the R7 and R8 input types … costs 0.0920.092 [0.079,0.104][0.079,0.104]" | 吻合 |
| Table 3 `Receptors only (P,A,R) 0.894` / `Fly + drift (P,A,R) 0.835` | 表格行逐字 | 吻合 |
| §7.2 CNN `0.961` vs `0.962` | "Putting the optic-lobe model in front of a convolutional decoder yields 0.962 average precision where the same decoder on raw receptors yields 0.961" | 吻合 |
| R99 第二句引文 | "A structure can be load-bearing for a computation without that computation being the one a task needs." | 逐字存在，吻合 |
| Park 2026 | 真实记录 `arXiv:2609.39248v1`，Submitted 30 Sep 2026，摘要含 "ten seeds" / "10.6 to 10.7 %" / "0.012 %" / "+/-0.10 equivalence bound (+0.002 and -0.074)" / "0.44 (10 of 10 seeds)" / "0.53 (10 of 10 seeds)"；Comments 链接 `https://doi.org/10.5281/zenodo.22871090` | 数字吻合，**但 R106 的 Zenodo 编号错**（W8） |
| Dhawan / FlyHack 2026 | 真实记录 `arXiv:2610.13018`，摘要含 "pooled AUROC 0.970 and Spearman 0.872, versus 0.933 and 0.126" / "Greedy cell-type sets meet a model-relative T4/T5 tuning criterion in 25 of 50 models" / "only two of those six first-success cell-type sets still meet the tuning threshold"；全文含 "The CNN training split is documented, whereas the released flyvis models' launch-time split is not recoverable; their common evaluation is therefore descriptive rather than a shared held-out generalization comparison." | 吻合；但 **R106 的日期错**（W8） |
| 2026 几何研究 secondary hit | 主 URL `aimedicalcompendium.com/article.cfm?id=253759` 被 Cloudflare 拦截，无法直接取证；WebSearch 显示底层为 **bioRxiv DOI `10.64898/2026.06.10.731214`（Zhou & Hasler）**，且 v1 摘要是**阳性**结论（"RSA Spearman r = 0.686 … r = 0.846", "r = 0.930 vs. r = 0.603"），v3/镜像版才是 R99 描述的**大体阴性**结论（"p < 10-13 in every case", "closes the gap completely"） | 存在版本歧义，矩阵引用的是二手镜像且未标 DOI/版本（W6） |

---

## 4. 反例 / 弱点（编号 W1..W13，含严重度）

- **W1 [HIGH｜阻断]** G0 在 `pipeline-state.json` 中仍为 `status: pending / gate_verdict: pending`，且 `inputs: []`、`evidence: []` 为空。全包不存在任何 gate owner 的 pass 动作记录。证据冻结件是目录里的独立文件，未登记进门自身。⇒ 从状态机看 G0 根本没有被通过，也不能被「追认」通过。
- **W2 [HIGH｜阻断]** R98 gap 1 仍 OPEN：矩阵第 9/10/24 行三处 `asset/license/code path` 未验证标注原样存在；R106 自己的 `R106-G0-GAP1-ASSET-CHECK.md` 明确写「R98 gap 1 未整体闭合」，Correig-Fraga 归档内容/许可与 FlyHack 代码路径维持 OPEN。R106 的字节 SHA 验证只覆盖自有资产，**未读任何 LICENSE 文本**，属于「可得性」而非「许可/代码路径验证」，且该文件第 22 行自己也说这「属于 G1 范畴，不是 G0 的通过判定」。把可得性包装成 gap 1 闭合即为证据晋升。
- **W3 [HIGH｜阻断]** R98 gap 2 仍 OPEN 且已恶化：矩阵仍写「Kuklev 留下的开放问题」，而 v2 §7.3/§8 已把「when」轴回答掉（§3(c) 逐字）。R106 明说「必须并入 G4 定位，否则矩阵仍是 stale 的」但**没有回写矩阵**（mtime 固定 11-12 16:46:17）。一张含已知错误结论的基线 map 不可能是 final。
- **W4 [HIGH｜阻断]** R98 gap 4 仍 OPEN：validator 的 `scientific/visual gate judgment remains required` 未被任何文件满足；R98/R99/R106 全部自我标注为 `*_NOT_SCIENTIFIC_RESULT`；R106 §6 只是「交 gate owner 的实质输入」。本报告结论为 NO，不构成放行判断。
- **W5 [HIGH｜新引入的事实错误，且已扩散到 3 个文件]** R106 §3.1 断言 R99 引的 "Exact structure remains insufficient to beat what the moving retina already provides" 是 **v1 摘要**、且「v2 摘要不含该句」。一手核验（§3(b)）证明：该句**不在 v1 摘要**，而**就在 v2 论文摘要**（`/html/2609.24565v2` 与 v2 PDF）里；arXiv 上并存两个措辞不同的 v2 摘要（元数据摘要含 "Longer observations…"，论文 LaTeX 摘要含 "Exact structure…"），R106 只报其一并把它当作唯一「v2 摘要」。因此 R106 的「R99 版本错配」核心发现**不成立**。该错误已复制到 `R106-ROUND-AUDIT.md` §5.2 与 `correction-ledger.md` R106 段。G4 风险上调的结论本身仍由 §7.3/§8 支撑（见 §5），但其**论据错误**，必须更正后才允许把矩阵定稿。
- **W6 [MEDIUM]** secondary hit 未复核且引用不严谨：R106 三处自认「2026 几何研究本轮未独立复核」；我独立抓取主 URL 被 Cloudflare 拦截，WebSearch 只找到底层 bioRxiv 记录，并发现 **v1 阳性结论 / v3 大体阴性结论的版本差异**。矩阵只给二手镜像 URL、无 DOI、无版本号、无版本差异说明。文献/基线 map 中一条无法从一手来源定位版本的条目不可视为可验证证据。
- **W7 [MEDIUM]** 最关键 prior art 没有本地冻结的一手字节：`literature-search/source-manifest.json` 仅 5 条，**无 `2609.24565`**；R99 的「live web + full-text fetch」与 R106 的复核都没有把 Kuklev v2（两个不同摘要 + 正文）保存为带 SHA 的本地件，也未登记进 manifest。R98 曾称「23 saved public sources」，manifest 实为 5 条。G0 作为「baseline map」门，其决定性条目只能靠实时抓取复现，不能由本地字节独立复算。
- **W8 [MEDIUM｜新引入的错误标识]** R106 §4 与 round audit §5.4 写 Park 的 Zenodo 为「**22891264 v4.0**」，而一手 abs 页 Comments 链接为 `https://doi.org/10.5281/zenodo.22871090`（**22871090**）；R106 §4 写 Dhawan/FlyHack 为「**2026-10-12**」，而一手 abs 页为 `[v1] Fri, 9 Oct 2026 05:20:38 UTC` / "Submitted on 9 Oct 2026"（**2026-10-09**）。
- **W9 [MEDIUM｜可验证的反例]** 冻结不完整且已 stale：`R106-G0-EVIDENCE-FREEZE.json`（03:41:30）只冻 8 份历史文件，未覆盖 03:44–03:56 新增的 7+ 份 R106 产物。`R106-END-OF-ROUND-FREEZE.json` 声明 `all_copies_byte_identical: true`、7/7 一致，但独立复算发现 `R106-ROUND-AUDIT.md` 声明 `10457 B / 06299a15e5c9…`、实际 `11743 B / 772036905edf…`，主副本与隔离副本 `cmp` 不同（11743 vs 10457 B）⇒ 该「全部逐字节一致」声明在我读取时**为假**。这直接示范了「自报冻结值不可信」。
- **W10 [MEDIUM]** `R106-G4-POSITIONING.md` §1 标题写「四篇一手 prior art（**均已独立复核**）」，但同表第 4 行自己写「2026 几何研究（**后者本轮未独立复核，保留 R99 状态**）」，且该行把两篇文献塞进一行（实为 5 篇）。标题与表体自相矛盾，属 overclaim。
- **W11 [LOW]** R106 §2 称 R99 的 11 组数字「全部**逐字**吻合」。我核验数值全部真实存在，但 HTML 转写把区间重复排版成 `+0.033+0.033 [0.015,0.050][0.015,0.050]`，与「单份规整字符串」并非逐字相同；属措辞松，不是编造。
- **W12 [LOW｜口径]** R106 反复声明「本轮另起全新隔离子代理做独立 gate review」并把 G0 是否可过交给该报告（即本报告），同时又明确自己「不是独立 gate review」。因此**在本次审查落盘前，R106 全包不包含任何独立 gate-owner 结论**；本报告的 verdict 是 NO，且 designated gate owner `ccf-literature-searcher` 没有签署记录。
- **W13 [LOW｜结构性]** `fail-fast-gates.md` 全文从 G1 起，**没有 G0 的成文通过标准**；G0 的判据由 R98 在项目内自定义。在无权威 pass criterion 的情况下，任何 PASS 都必须额外给出并冻结「G0 通过条件」的书面定义，否则不可复算。

**未发现的反例（如实记录）**：没有伪造 SHA（8/8 + 旁证全真）；没有静默标门 passed；没有声称本项目取得科学结果（R99 描述的是第三方已发表结果，矩阵第 26 行明确写 "third-party reports, not our measurements"）；没有分数/阈值/评审/稿件/冻结身份的改动；没有 `**Overall:**` 行；没有模型前向/训练/标签/数据集。

---

## 5. G4 定位评估（是否 defensible / overclaim；判别性预测轴是否仍开放）

**核心结论：R106-G4-POSITIONING.md 的中心判断 defensible，但存在一处 overclaim 与一处错误前提，不能原样作为定稿依据。**

1. **「判别性预测」轴（R99 原表述：*predicts when path-preserving controls matter vs when the input alone suffices*）已不开放。** 我独立核验 v2 §7.3/§8 逐字发表了：判别变量 = 观测时长是否跨过一个刺激周期；8 帧落后 `0.011`、20/34/60 帧领先 `0.018/0.021/0.022`；变化量 `+0.033 [0.015,0.050]`；频谱带 `+0.085~+0.102`；阴性机制结论「T4/T5 贡献不随观测长度增长」`+0.008 [−0.003,0.018]`；作者自称该预测「half held」。因此 R106 判定「该轴被部分抢发、G4 风险由 high 上调」**是正确且可验证的**，不是过度悲观。R106 同时正确继承了 v2 的严格性限制（绝对值不可跨配置比较、只有 sweep 内差异有效、作者自称 half held）。
2. **仍开放的只是更窄的机制问题**：§8 逐字 `The remaining question is which stage integrates the extra time, and a per-type tuning analysis over the sweep would answer it.` `R106-G4-POSITIONING.md` 第 35–38 行把它列为差异点 3，并诚实标注「定位陈述是**计划**，不是结果；按 G4 不能拿计划当差异化证据」（第 51–53 行）——这一点不算 overclaim。
3. **Overclaim 一**：§1 标题「四篇一手 prior art（均已独立复核）」与表内自认「几何研究未独立复核」矛盾，且件数不符（W10）。
4. **错误前提一**：风险上调的叙述部分建立在 W5 的「R99 引用 v1 结论、v2 已替换」之上。该前提不成立；不过 §7.3/§8 的一手证据独立成立，所以**结论保留、论据必须更正**。
5. **另一处可核验的支撑为真**：第 76 行「Sintel 8 clips、官方 model000/001 资产已由本轮只读盘点确认齐备」——我复算 8/8 clips + 10/10 官方模型文件 SHA 全吻合，该资产可得性陈述属实；但它属于 G1 范畴，不能用作 G4 差异化证据（文件自己也如此限定）。

⇒ 综合：**substance defensible，表述含 overclaim 与错误前提；G4 仍 pending、风险上调是合理的，但「判别性预测何时路径重要」这一轴已不再是开放问题，只剩「哪个 stage 整合额外时间 / per-type tuning」这一更窄的机制问题。**

---

## 6. G0 得以合法通过前必须满足的条件（逐项、可核验）

- **R1（闭 gap 1）** 在矩阵中逐条补正并冻结：Correig-Fraga `Zenodo 21549559` 的归档内容与 **LICENSE 文本**、FlyHack 的**项目代码路径**（若确无公开代码仓，须记录「未找到」及其检索证据）、以及第 24 行「optical-flow benchmark / pretrained checkpoints / natural clips」的 asset+license 检查。字节 SHA 不算许可核验；每行须给出可复算的附件（如保存的 license 文本 + SHA）或明确的负面结论。
- **R2（闭 gap 2）** 把矩阵**定稿并重新冻结 SHA**：删除/更正「the open question Kuklev leaves」这一已被 v2 §7.3/§8 证伪的表述；并入 R106 §3 的全部发现（时间尺度 sweep、`+0.033 [0.015,0.050]`、不经 T4/T5、§8 残余问题），并明确记录 **arXiv 上两个措辞不同的 v2 摘要并存**这一事实。
- **R3** 把 2026 几何研究条目改为**一手来源**：bioRxiv DOI `10.64898/2026.06.10.731214`，标明具体版本（v1 阳性 vs v3 大体阴性），从一手页面重核 `p<10^-13` / 「trained ER / OFF 完全闭合」等结论；记录 `aimedicalcompendium.com` 为不可取证二手镜像（Cloudflare 拦截）。
- **R4** 为 `arXiv:2609.24565v2` 保存**本地、带 SHA 的一手冻结件**（至少 abs 元数据页 + HTML/PDF 正文两者，因摘要不同），登记进 `literature-search/source-manifest.json`；同时保存 v1 摘要以便版本比对。
- **R5** 更正 W5/W8 的事实错误：`R106-G0-INDEPENDENT-RECENCY-VERIFICATION.md` §3.1、`R106-ROUND-AUDIT.md` §5.2、`correction-ledger.md` R106 段的「v1 摘要」误归属；Zenodo `22891264` → `22871090`；Dhawan 日期 `2026-10-12` → `2026-10-09`；以及 `R106-G4-POSITIONING.md` §1 的「均已独立复核」。按 RGE 纪律用**新增补正记录**，不改写原字节。
- **R6（闭 gap 4）** 由 designated G0 gate owner 做出并落盘**显式的 scientific/visual gate judgment**（对文献/基线图的科学充分性作判断，而非仅 ordered/current evidence），并登记本独立 gate review 的结论。
- **R7** 把 G0 的证据登记进 `pipeline-state.json` 的 `inputs` / `evidence`（当前为空），由 gate owner 记录显式 `passed`；在此之前 G0 保持 `pending`，**不得追认或静默晋升**。另需书面冻结 G0 的 pass criterion（因 `fail-fast-gates.md` 未定义 G0，见 W13）。
- **R8** 重新冻结**完整**的 G0 证据包（R106 全 14+ 份产物 + 更正后的矩阵 + 新增的 Kuklev 一手保存件），并修复/替换 `R106-END-OF-ROUND-FREEZE.json` 中关于 `R106-ROUND-AUDIT.md` 的失配声明。
- **R9** R1–R8 完成后，由**新的**独立审查复核四 gap 是否真闭合；更正动作本身不得自我认证。

---

## 7. 纪律检查（逐条确认未发生）

| 禁止动作 | 确认 |
|:--|:--|
| 修改任何既有文件 | **未发生**。全程仅 Read / WebFetch / WebSearch / 只读 Bash（`sha256`, `stat`, `find`, `cmp`, `python` 读字节）；未对任何既有文件调用 Write/Edit。所有既有文件 mtime 均在 R106 之前或由并发进程写入，与我无关。 |
| 标记任何 gate passed / 编辑 `pipeline-state.json` | **未发生**。实测 `pipeline-state.json` mtime `2026-11-12 10:43:12`、SHA `bcb48bb9…` 与 freeze 声明一致；G0 及 G1–G8/validation/handoff 全 `pending`。 |
| 触碰任何 review / score / threshold / frozen artifact / manuscript | **未发生**。分数/阈值/评审/稿件类文件 mtime 均 ≤ `2026-11-12 17:33`；R106 窗口内仅 `gate-G0-R106/*` 新增产物与 `correction-ledger.md` 一次由并发进程完成的追加登记，无既有冻结件被改写；未生成 `guidance.md`。 |
| 只创建恰好一个新文件 | **是**。仅创建本报告 `gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md`。本次会话中出现的其余 R106 新文件与 `isolated/` 副本由并发轮次进程创建，**非我所建**，我未修改它们。 |
| 模型前向 / 训练 / 标签 / 数据集 | **零**。仅做 SHA 复算与网页抓取；未加载任何模型权重、未执行任何 `.npz`/checkpoint 前向、未使用标签或数据集内容。 |
| 稿件 full review / `**Overall:**` 行 / 数值论文分 | **未发生**。本报告无 `**Overall:**` 行、无数值分、无 Scholarly Confidence 行；按门审查口径书写。 |
| 依赖 R106 转述作为证据 | **未发生**。所有 SHA 自原始字节重算；所有一手引文均由我直接 WebFetch/WebSearch 取得，R106 转录仅作为待核验对象。 |
| 提问 / 请求他人输入 | **未发生**。全程无人值守、未向任何 teammate 询问。 |
| 把「文献核对吻合 / arXiv 可访问 / 资产齐备」包装成科学结果 | **未发生**。第二行明确 `**Scientific result claimed:** NO`；本报告明确区分第三方已发表结果与本项目零结果。 |

---

**结论**：字节层面证据包诚实且可复算（8/8 SHA、12/12 门状态、旁证全真），但 R98 的 gap 1 / 2 / 4 明确未闭合、gap 3 仅部分完成且本独立审查结论为 NO；同时 R106 引入了可核验的事实错误（v1/v2 摘要误归属、Zenodo 编号、Dhawan 日期），矩阵含已知错误结论，最关键 prior art 无本地一手冻结件，两份 freeze 中有一份已 stale。因此 **G0 不得标为 PASSED，须维持 `pending`**，按 §6 的 R1–R9 补正后再审。

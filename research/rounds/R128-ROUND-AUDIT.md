# R128 轮次审计（2026-11-14 19:07–19:4x +0800）— 合并后 PUBLIC 默认分支整树一手核验

**性质**：`READONLY_POST_MERGE_PUBLIC_MAIN_TREE_ATTESTATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`。
只读核验，不晋级任何门、不改任何 state / 矩阵 / registry / 门配置 / 评审 / 分数 / 阈值 / 稿件 / 冻结件 / 历史字节；不产生任何科学结果、不产生数值 `**Overall:**` 分数字面行；不起 `ccf-paper-reviewer full`；不自评 governing。

**这不是第 14 层流程审计文档，而是对 R126/R127 刚造成的全新外部状态的一次可执行、可复算的字节级安全 / 完整性核验**；其结论明确**不**改变达标距离（见 §6，R121 否定性闭环仍成立）。

---

## 1. 第 0 步并发保护（不触发）

| 检查 | 读数 |
|:--|:--|
| `goal-ledger.md` mtime | `2026-11-14 18:32:56 +0800`；唤醒 `19:07:05` ⇒ **34.6 min > 10 min** |
| 近 15 min 主项目写入 | **0 文件** |
| 近 15 min 同步仓库写入 | **0 文件** |
| 其他 CLI 会话 | `56bee8d1` 属 `/Users/xhf/code/xhf-person/`（另一项目），非本目标；`51d68770` 为本自动化会话自身；无主会话 / novix 轮询 / runner |
| 两评审目录最新 | `ccfa-review-reports/` 最新 r95（11-11 15:01）；无未登记异步 full 评审 |
| 严格行首数值 `^\*\*Overall:\*\* [0-9]` | **15 行 / 13 文件 / 10 个不同内容哈希**；其中 r95 规范件 3 份逐字节副本；排除自产副本与叙述后 **无晚于 r95 的新独立 full 评审** ⇒ `new_governing_candidates=0` |

⇒ 并发保护**不触发**，主动推进；governing 仍 **R95 = 6.0 / Confidence 4.0**。

## 2. 换道理由（RGE4）

R105 / R107 / R109 三次判停「继续产出证据文档」同构循环；R114–R125 连续 12 轮各审计一层流程 / 基础设施；R121 已由 governing 评审 R95 §13 自身判据推出**只读审计在结构上不可能把 6.0 抬到 >= 7.0**（流程 / 披露 / 格式不新增支持中心主张的科学证据）。R124/R125 判定自主动作穷尽，剩余全部落在 designated gate owner 的最小集 `G1 + G4 + G10`。

**但 R126（全开放 233 文件）/ R127（合并进 PUBLIC 默认分支 `main`）是主会话造成的新外部状态，此前从未被任何一轮核验过**：
- R126 的凭证扫描对象是**推送前 agent 分支的 staged diff**，不是合并后的 `main` 整树；
- R127 的核验是 `git merge-tree --write-tree` **无冲突**，不是内容安全核验；
- 用户 R126 新范围把**唯一硬排除**收窄为「含**真实凭证值**的文件（会危及账号）」，且明确 `b"ghp_"` 等扫描模式字面串不是凭证、不得误伤。

⇒ 本轮**不写第 14 层流程文档、不写 G0 文字补丁、不碰须批准机器门、不起 P3、不创建 v4**，改做**合并后 PUBLIC 默认分支整树（336 文件）真实凭证值 + 233 条目清单完整性的一手字节核验**。这是对唯一硬排除的正面合规核验，也是把已公开内容做一次可复算的安全兜底；不改任何门、不产科学结果、不声称靠近达标。

## 3. 一手件与采集口径

- 采集对象：`git ls-tree -r -l -z main` 枚举的**提交树**（ref `main` = `6cc2e4fbe351…`，tree `5a6967b731726…`），逐 blob 用 `git cat-file --batch` 读**提交字节**，而非工作树文件 ⇒ 核验的是**已发布的字节**。
- 采集脚本 `R128-ACQUIRE.py`（只写本轮目录）→ `R128-ACQUIRE.json`；原始清单 `raw/tree_paths.txt`（336 行 path / blob / size）。
- 独立 verifier `R128-VERIFY.py`（不 import 采集、不把任何 R128 JSON 作实质数据源、用另一套更宽模式与逐 blob `cat-file` 重算）→ `R128-VERIFICATION.json`。
- **A 组声明为同机字节恒等一致性核对，非独立交叉核验**（同机必然相同）；v1 缺陷留痕见 §5。

### 本地 / 远端 ref 一手读数

| ref | 值 |
|:--|:--|
| `local main` | `6cc2e4fbe35121e6777f3c19c4502adc95f7427d` |
| `local HEAD` | `6cc2e4fbe35121e6777f3c19c4502adc95f7427d` |
| `origin/main`（`ls-remote`） | `6cc2e4fbe35121e6777f3c19c4502adc95f7427d` ⇒ **本地 = 远端** |
| `agent/r109-harbor-sync/wb-main` local / remote | `d76bb642dd502264230561327566c4c0c48af935`（两端一致，保留未删） |
| `main^{tree}` | `5a6967b7317267439dc5b8ea67ee98fa1b7e7bb3` |
| `git status --porcelain` | 空 ⇒ 工作树干净 |

`agent..main` 对 `research/`、`HANDOFF.md`、`LOG.md` 的 `git diff --stat` 均为**空** ⇒ 合并未改动 research 内容与两个滚动记录。

## 4. 实质发现（全部为字节级可复算事实）

### 4.1 唯一硬排除：真实凭证值 0 命中

- 对 **336 / 336 提交 blob** 用严格「前缀 + 长不透明主体」模式扫描：`gh[pousr]_`、`github_pat_`、`AIza`(+30)、`AKIA`、`ASIA`、`sk-`、`xox[baprs]-`、JWT `eyJ…`、`Bearer + 长串`、`-----BEGIN … PRIVATE KEY-----`、带引号 / 裸的 `password|api_key|token|secret` 赋值、`[0-9a-f]{40,}` hex secret、以及熵 >= 3.5 bits/char 的后缀启发式 ⇒ **真实凭证值命中 0**。
- **19 个文件含扫描模式字面串 / 叙述**（`b"ghp_"`、正则字符类、`AIza…` 截断叙述、`sk-` 出现在 `Task-Aligned` 单词内），逐一取上下文核验全部为**模式 / 叙述 / 已脱敏记录，非凭证值**。其中 `research/ledger/goal-ledger.md` 与 `research/ledger/2026-11-13.md` 的 `AIza…` 命中是 R123 的一手记录：官方上游脚本内嵌第三方**公开** API-key 字面量 ⇒ 按 R109 红线**在落盘前即删除**、值从未打印 / 复制 / 记录 / 上传，派生件一律 `<redacted>`。**该值不在公开树中**。
- 与 R126 checkpoint 的「11 份 verifier/audit 文件是扫描模式字面串、不是密钥」结论一致；本轮把口径从 staged diff 扩到**合并后整树**（含 `AGENTS.md`、`README.md`、`research/README.md`、`collaboration/`、`evidence/`、全部检查点），并明确区分「真实值」与「模式字面」。

### 4.2 R126 全开放清单在合并后 233 / 233 逐字节一致

`research/UPLOAD-MANIFEST.json`（78,626 B，sha16 `3f7646ca44243fa2`）含 **233 条 `copied`、`skipped=0`**。对每条 `dst` 在 `main` 提交树中重算字节数与 SHA-256：**233 / 233 完全吻合，0 mismatch，distinct dst = 233**。⇒ R127 的 `--no-ff` 合并未丢失、未改写、未替换任何一份研究成果全文；合并只动 `README.md` / `PROTOCOL.md` / `AGENTS.md` 的簿记文本。

### 4.3 其余范围检查

| 项 | 读数 |
|:--|:--|
| 提交树文件数 / 总字节 | **336 / 9,798,478 B**（`research/` 235） |
| 最大单文件 | **2,149,921 B**（`research/manuscript/main.pdf` 2.06 MiB，稿件 PDF） |
| > 50 MiB | **0** |
| 权重 / 数据集 / 二进制后缀（.pt .pth .ckpt .safetensors .onnx .h5 .npy .npz .pkl .parquet .zip .tar.gz .so .dylib .bin 等） | **0** |
| 第三方源码 / 大权重 / 数据集 | **0**（与 R126 边界一致：仓库仍不能独立复现实验） |
| 公开树中严格数值 `**Overall:**` 行 | **12 行，全部在 `research/reviews/`**；值 = 7.5,7.5,8.2,8.2,7.0,7.5,7.5,6.9,6.3,5.4,5.2,6；日期全部 ≤ 2026-11-11，最新独立 full 评审 r95 = **6** ⇒ 无新 governing 候选、无编辑 / 隐藏 / 重定日期的历史报告 |

### 4.4 双门只读 + 结构权威零写回

- validator：`NOT_QUALIFIED / 6.0 / >=7.0 / score_meets_threshold=false / all_pass=false`（D1✓ D2✗ D3✗ D4✓ D5✗）；D3 逐字 `governing=6.0 in paper-null-ladder-r95-independent-review-20261111.md (**Overall:** 6)`。
- guard：`ledger-null-ladder.json` 9,994 B / sha16 `73043b4e164a5a5f`、`criteria-null-ladder.json` 10,443 B / sha16 `94846083217df86f`；A1–A6 六项、S1–S7 全 pending、`actions=[]` ⇒ `INCOMPLETE`（A2/A6）。
- 主线 `pipeline-state.json`：12 阶段，`CCFA-startup=passed`，**G0–G8 / validation / handoff 全 pending**，`G0.inputs=[]`、`G0.evidence=[]`。
- 7 份结构权威在采集与 verifier 两次独立读数中 **SHA 全等** ⇒ 本轮**零写回**：`goal-ledger.md 3a694ab2…`、`validate_single_paper.py 72240260…`、`criteria 94846083…`、`guard ledger 73043b4e…`、`pipeline-state.json bcb48bb9…`、`matrix 31b5098b…`、`source-manifest.json 541880ab…`。
- `goal-ledger.md` 的 SHA 相比 R125 记录的 `00ff975c…` 已推进 ⇒ 这是 **R126/R127 主会话只追加 R126/R127 段落**造成的时点差，非本轮回写；本轮采集前 / verifier 后两次读数一致。

### 4.5 可复算性

- `R128-VERIFY.py` **36 检查 / 36 MATCH / 0 MISMATCH**（A6 B5 C3 D3 E5 F9 G5），真实凭证值 0、熵候选 0。
- `R128-ACQUIRE.py` 采集读数与 verifier 独立重算逐项吻合（336 / 9,798,478 / 233 / 2,149,921 / 12 / 6.0 / actions 0）。

## 5. v1 verifier 缺陷留痕（E-1，冻结不回写）

`R128-VERIFY-v1.py` / `R128-VERIFICATION-V1.json` 原样冻结：v1 的熵启发式正则 `sk-` **无词边界保护**，把项目路径 `Task-Aligned-Controls-for-Connectome-Vision` 中 `Ta`**`sk-`**`Aligned…` 的 `-` 前缀误判为 OpenAI 风格密钥，产生 **246 个候选 / 24 文件** ⇒ `35 检查 / 34 MATCH / 1 MISMATCH`。逐条诊断：**246 / 246 的 label 全是 `sk-`，body 全是 `Aligned-Controls-for-Con…`，无一为纯 hex**，全部来自该路径字面，属**正则设计缺陷，不是 246 个凭证**。v2 给每个前缀加 `(?<![A-Za-z0-9_\-])` lookbehind 并显式声明 occurrences / distinct（R125 L1 教训）⇒ **0 候选**；并新增一条 `v1_task_path_false_positive_explained` 检查把该根因固化为可复算事实。两版脚本与两版 VERIFICATION 全部保留，v1 输出不回写、不删除。

**教训**：`零命中` 类检查必须用形态无关正则并声明词边界 / occurrences / distinct；短前缀（尤其 `sk-`）嵌入普通英文单词会造成大规模假阳性，须先逐条分类再下结论；不得用「把模式删掉」的方式消除 mismatch，必须定位根因并留痕。

## 6. 严格边界与否定性结论

- 全 `READONLY_POST_MERGE_PUBLIC_MAIN_TREE_ATTESTATION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`；EXEC LOCK：零前向 / 推理 / 训练 / 标签 / 数据集 / EPE·l2 / 科学指标 / 新正向证据；零网络请求（`ls-remote` 仅读远端 ref，未推送）。
- **R121 否定性闭环不变**：R95 §13「流程 / 披露 / 格式不新增支持中心主张的科学证据 ⇒ 不改变 evidence-capped overall」，§8「无法靠 prose 补出视觉贡献」。本轮是**安全 / 完整性合规核验**，不是升分动作；三项升分条件 (a)(b)(c) 仍全 `satisfied=False`。
- 合并（R127）只接受簿记记录，不是科学验收：不过门、不改分数、不验证实验、不让稿件达标。上传 ≠ 投稿 / 发表，双盲与优先权影响由整合者判断。
- 未改任何历史字节 / 评审 / 分数 / 阈值 / 稿件 / 门 / 冻结件 / 矩阵 / registry / 门配置；未起 `ccf-paper-reviewer full`；未产生数值 `**Overall:**` 行；未自评 governing；未跳门；未创建 v4；未假定 `≤32h / K=45` 授权（D1 维持 `BLOCKED_ON_CONFIRMATION`）；无 4090 / L4 / H20 能力主张；主项目未投稿 / commit / push。
- **结果**：第 3 步前置（实质正向新科学证据）未满足 ⇒ 不进稿件新副本、不做 9 页合规编译、不起全新隔离 full 评审。**0 篇达标、未写 COMPLETE**，governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`。停止门只剩 ①达标（>= 7.0）②用户叫停。

## 7. 交下轮

1. 回收本轮全新隔离独立审查，结论与更正**只追加**于新的不可覆盖检查点（按 R117/R119–R125 先例，本检查点字节不回写）。
2. 决策入口 `R120-CONSOLIDATED-DECISION-REGISTER.md`（最小集 `G1 + G4 + G10`）；13 份件归类 / 登记、矩阵定稿、W13 判据冻结须 designated gate owner 依 `G1/G4/G6/G7` 裁决，心跳不回写。
3. 唯一 admissible 路径 = 按序 G0–G8 → validation → handoff → P0 → P1A/P1B → P2 → **P3 baseline-first 真实前向**取得实质正向新证据 → 稿件新副本 → 9 页合规编译 → 全新隔离 full 评审；`X >= 7.0` 且 QUALIFIED + COMPLETE 才写 COMPLETE。门槛降低不降低证据质量。
4. **新教训**：① 推送前 staged diff 的凭证扫描 ≠ 合并后 PUBLIC 默认分支整树扫描，合并后必须重扫；② 「真实凭证值」与「扫描模式字面串 / 截断叙述」必须分列，不得互相误伤；③ 清单 `233/233` SHA 吻合证明的是**字节完整性**，不是科学有效性；④ 短前缀熵启发式须加词边界并先分类假阳性；⑤ 引用 `main` 时必须区分「本地 HEAD / 远端 SHA / 提交 tree」三个对象。

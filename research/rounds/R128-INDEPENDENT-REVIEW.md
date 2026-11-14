REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO

# R128 独立复核（完全隔离验证者）

方法：仅从 `main` 提交树 blob（`git ls-tree -r -l main` + `git cat-file blob`）、只读运行 `validate_single_paper.py`、两份 guard JSON 与主线 `pipeline-state.json` 自行重算；未 import 任何 R128 采集/校验脚本，未把任何 R128 JSON 当数据源；round audit 在自身重算完成后才读。唯一写入即本文件。HEAD 已核实：本地 `main` = 本地 HEAD = `origin/main` = `6cc2e4fbe35121e6777f3c19c4502adc95f7427d`，`main^{tree}` = `5a6967b7317267439dc5b8ea67ee98fa1b7e7bb3`，31 commits。

## A — 树统计与工作区
- 跟踪文件数 **336**（全为 `100644 blob`，无 symlink/tree），总字节 **9,798,478 B**。
- 最大单文件 **2,149,921 B** = `research/manuscript/main-2.pdf`（2.0503 MiB）；`main.pdf` 为 2,123,187 B。`blobs_read=308`（采集器）系按 blob SHA 去重：308 个不同 SHA / 28 个重复内容路径，336 个路径全覆盖。
- > 50 MiB 文件 **0**。
- 本地 main SHA = 远端 main SHA（`git ls-remote origin refs/heads/main` 返回同一 SHA）= **是**。
- `git status --porcelain` 空 → 工作区干净（同机字节恒等核对，非独立交叉验证）。

## B — UPLOAD-MANIFEST 逐条核验
- `research/UPLOAD-MANIFEST.json`：**78,626 B**，sha16 `3f7646ca44243fa2`；`copied` **233** 条、`skipped` **0**、`note` 声明「仅排除含真实凭证值的文件，11 份 verify/audit 文件为扫描模式字面串、已纳入」。
- 对**每一条** `dst`：在提交树中重算字节长度与 SHA-256，与声明的 `bytes`/`sha256` 比对 → **match 233 / mismatch 0 / missing 0**，distinct `dst` = 233。
- 即：R126 归档的 233 个文件在合并后 `main` 树逐字节一致；`research/` 共 235 文件（+ README.md + 本 manifest）。历史 `research/` 文件从未被 `M` 修改（见 E/k）。

## C — 真实凭证值 vs 扫描模式字面串
- 用自有严格模式（前缀 + 长不透明主体 / 带引号与裸赋值 / PEM / JWT / Bearer / hex / 熵）扫全部 336 blob：**真实凭证值命中 0**（无值可打印，故无泄露）。
- 扫描模式字面串（**全部 NON-secret**）按口径分别计数：强前缀字面串文件 **21**（其中 `.py` 校验器/探针 9 个，见 `research/rounds/R1xx-verify*.py`）；含普通 `token/secret/password/api_key/sk-` 等弱标记的文件 **160**；含朴素 `sk-` 出现的文件 **112 / 690 次**，绝大多数来自项目名。round audit 的「19 文件」是采集器 `R128-ACQUIRE.json:20-184` 的窄口径（仅 `gh_scan_literal`/`AIza_scan_literal`/`b_quote_ghp` 三标签），与上述不同口径并存，均为非凭证。
- **朴素 `sk-` 假阳性：是**。`Task-Aligned-Controls-for-Connectome-Vision` 中 `Ta`+`sk-`+`Aligned…` 在朴素 `sk-` 下命中（span `(2,5)`）；无词边界的宽松 `sk-[A-Za-z0-9_-]{20,}` 产生 **249** 个候选（**246** 含 `Aligned/Controls/Connectome`）；严格 `sk-[A-Za-z0-9]{32,}` 加词边界 → **0**。这正是 v1 缺陷 E-1 的根因，被我独立复现（数值 249/246 与 v1 的 246/24 文件仅因正则形状略有差异，同源）。
- 3 个含训练/前向标记的 `.py` 均为 harbor 探针或审计脚本，非可复现实验代码。

## D — 权重 / 数据集 / 二进制
- `.pt .pth .ckpt .safetensors .onnx .h5 .npy .npz .pkl .parquet .zip .tar.gz .so .dylib .bin` 等后缀文件 **0**；数组/权重文件 0。
- PDF **2** 份，均为合法稿件产物：`main-2.pdf` 2,149,921 B、`main.pdf` 2,123,187 B。

## E — 公开树中的数值评分行
- 严格行首 `^\*\*Overall:\*\* [0-9]` 共 **12 行 / 10 文件**，全部在 `research/reviews/`：
  - `paper-null-ladder-full-review-20261108.md` → 7.5（2 行）
  - `paper-null-ladder-r39-full-review-20261108.md` → 8.2（2 行）
  - `paper-null-ladder-r39-independent-review-20261108.md` → 7.0
  - `paper-null-ladder-r47-independent-review-20261108.md` → 7.5
  - `paper-null-ladder-r49-independent-review-20261108.md` → 7.5
  - `paper-null-ladder-r58-independent-review-20261108.md` → 6.9
  - `paper-null-ladder-r60-independent-review-20261108.md` → 6.3
  - `paper-null-ladder-r91-independent-review-20261110.md` → 5.4
  - `paper-null-ladder-r93-independent-review-20261110.md` → 5.2
  - `paper-null-ladder-r95-independent-review-20261111.md` → 6
- 按文件名日期最新的独立 full 评审 = **r95 / 20261111 / value 6**（亦为 validator 的 governing）。所有评分行日期 ≤ 2026-11-11。
- 无编辑 / 隐藏 / 重定日期：`git log --all --diff-filter=M` 仅涉及 `AGENTS.md/README.md/PROTOCOL.md/PROJECT.md/TASK.md/HANDOFF.md/LOG.md`；**零** `research/` 文件曾被 `M`；23 份 review 全部在 `58500f3` 一次性 `A` 加入、之后不变。无新的达标候选（≥7.0 的独立评审 r39/r47/r49 均 20261108，早于 r95）；本轮未产生数值评分行。
- 注：round audit §1 的「15 行/13 文件」是**工作项目**评审目录的并发保护口径，§4.3 的「12 行」才是公开树口径，两者不同范围、无矛盾。

## F — 只读 validator + guard
- `validate_single_paper.py`（无 `--out`，仅 stdout，零写入）：`verdict=NOT_QUALIFIED`，`threshold=7.0`，`overall_score=6.0`，`score_meets_threshold=false`，`all_pass=false`；D1✓ D2✗ D3✗ D4✓ D5✗（D3 governing=6.0 / r95）。
- guard SHA-256 前 16 hex：`ledger-null-ladder.json` = **73043b4e164a5a5f**（9,994 B）、`criteria-null-ladder.json` = **94846083217df86f**（10,443 B）；`acceptance` ids = **A1–A6**（两份一致）；`actions` 长度 = **0**；`steps` = **S1–S7 共 7 步，全部 pending**。阈值变更来自 R107（`GOAL-ITERATION-R107.md`、criteria A6 `>=7.0`、validator 默认 7.0），非 R126/R127。

## G — 主线 pipeline-state.json
- 阶段数 **12**：`CCFA-startup` **passed**（inputs 2 / evidence 4）；其余 **11 pending** = G0,G1,…,G8,validation,handoff。
- **G0：status=pending，inputs 长度 0，evidence 长度 0，gate_verdict=pending** → 无门可过。

## H — 与 round audit 逐项比对
- **A 匹配**（336 / 9,798,478 / 2,149,921 / 0>50MiB / local=remote / clean；§4.3:71 的路径与 MiB 笔误见缺陷 D-1，数值本身与 `R128-ACQUIRE.json:186`、D3 行一致）。
- **B 匹配**（233 / 0 mismatch / skipped 0 / distinct 233；`78,626 B` 与 sha16 一致）。
- **C 实质匹配**（0 真实命中）；「19 文件」为采集器窄口径，我的宽口径为 21/160/112，均 NON-secret；`sk-`/Task-Aligned 假阳性被独立复现；v1 246/24 根因属实。
- **D 匹配**（0 权重/二进制；2 PDF，含正确字节数）。
- **E 匹配**（12 行 / 10 文件 / 值一致 / r95=6 / 无改动无新增）。
- **F 匹配**（NOT_QUALIFIED / 7.0 / 6.0 / false / false / D1–D5 / 两 sha16 / A1–A6 / actions 0 / S1–S7 pending）。
- **G 匹配**（12 阶段 / 1 passed 11 pending / G0 inputs=evidence=0）。
- 另核实：`git diff --stat agent..main` 仅 `AGENTS.md/README.md/PROTOCOL.md`（63 insertions），`research/`、`HANDOFF.md`、`LOG.md` 差异为空 → §3:52 与 §4.2 均正确。
- 结论：所有可复算数值与诚实的否定性结论均成立；发现 1 处未披露的散文级事实错误（D-1），以及 1 处已披露并冻结的 verifier 缺陷（D-2）。无编造。

## 12 类 overclaim 判定
口径：CONFIRMED = 独立字节证据支持该断言；REFUTED = 独立字节证据否定该断言。本轮 **12/12 REFUTED**。
- (a) 产出科学结果 — **REFUTED**：R128 为只读 blob 核验，无新 metrics/结果；README 明言「Uploading manuscripts here is not a submission」，R126 CHECKPOINT 标「NOT a scientific or paper-acceptance claim」。
- (b) 过门 / G0 可过 — **REFUTED**：G0 status=pending、inputs=[]、evidence=[]、gate_verdict=pending；validator NOT_QUALIFIED；guard INCOMPLETE。
- (c) 前向/训练/推理 — **REFUTED**：0 权重、0 数据集、无执行证据，3 个含训练字样的 `.py` 为 harbor 探针/审计。
- (d) governing 分数变化 — **REFUTED**：governing 仍 r95=6.0；12 行评分全部一次性加入、从未 `M`。
- (e) 新独立 full 评审 — **REFUTED**：`research/reviews/` 仅 `58500f3` 触及（全 `A`）；无新 review 文件；最新仍 20261111。
- (f) 合并即科学验收 — **REFUTED**：README「Merging is a bookkeeping/acceptance step, not scientific validation」；`74902cc` = 接受 24 检查点 + R126 归档。
- (g) 公开档案可独立复现实验 — **REFUTED**：README「Not included: large model weights and datasets」；0 权重/数据集/训练代码；audit §4.3:74 亦自认「仓库仍不能独立复现实验」。
- (h) 0 命中=证明绝无密钥 — **REFUTED**：有限模式扫描不能证否；manifest/README/R126 checkpoint 均声明含真实凭证值的文件被**按策略排除**，0 命中部分源于过滤；audit 本身亦规避此推论（§7 教训③）。
- (i) 233/233 清单匹配=科学有效 — **REFUTED**：仅证明字节完整性；validator NOT_QUALIFIED、6.0<7.0；audit §7 教训③自述。
- (j) R126/R127 改判据/阈值 — **REFUTED**：树中 `R127` 出现 0 次；R126 checkpoint「No gate status, score, threshold, protocol, seed or manuscript content changed」；阈值变更为 R107。
- (k) 改历史 review/分数/字节 — **REFUTED**：零 `research/` 文件 `M`；233 件一次加入不可变；main ref 全程 `6cc2e4f…`。
- (l) 更靠近 >=7.0 — **REFUTED**：governing 6.0 未变、距 7.0 仍 1.0，无新证据；audit §1:6/§6 明言「不改达标距离 / 不是升分动作」。

## 缺陷分级与 append-only 修正
- **D-1 [MEDIUM]** `R128-ROUND-AUDIT.md:71`：把 2,149,921 B 归属为 `research/manuscript/main.pdf` 且写「2.06 MiB」。独立字节：该值属 `main-2.pdf`（2.0503 MiB），`main.pdf` 为 2,123,187 B（2.0248 MiB）；同一轮冻结件 `R128-ACQUIRE.json:188-196` 与 `R128-VERIFICATION.json:143-146` 已正确给出 main-2.pdf / 2,149,921。属与自身机器产物矛盾的事实误标，非载荷项（数值正确、不影响任何判定）。建议 append-only：新建一份更正说明（不回写任何已发布字节），声明「§4.3 最大单文件路径应为 `research/manuscript/main-2.pdf`（2,149,921 B ≈ 2.05 MiB），`main.pdf` 为 2,123,187 B ≈ 2.02 MiB；原路径与 2.06 MiB 为笔误，数值不变」。
- **D-2 [MEDIUM｜已披露、已冻结、无残留]** `R128-VERIFY-v1.py` / `R128-VERIFICATION-V1.json`（35 检查 / 34 MATCH / 1 MISMATCH，熵候选 246 / 24 文件）：v1 的 `sk-` 无词边界保护，把项目路径 `Task-Aligned-…` 误判为密钥。已在 `R128-V1-DEFECTS.md:5-20` 定级 MEDIUM、根因定位、v2 (`R128-VERIFY.py:123-124`) 加 lookbehind 修正并新增 `v1_task_path_false_positive_explained` 检查；v1 两文件原样冻结、36/36 全 MATCH。我独立复现同一根因（249/246），确认既非 246 个凭证也非数据不一致。无需新动作。
- 其余观察均非缺陷：`blobs_read=308` 为 SHA 去重（336 路径全覆盖）；`goal-ledger.md` 当前 sha16 `8e00e0a66243` 与冻结锚点 `3a694ab2…` 之差，源于 19:43:31（晚于 verifier 19:30:12 / audit 19:31:49）的 T3 只追加写入，已由 `R128-TIMEPOINT-NOTE.md` 解释，非本轮回写。
- **Fabrications：0**（未发现任何凭空捏造的数字或声明；每个数值均可追溯到提交树 blob 或只读 gate 运行）。

## 验证范围限制（scope limits）
- 同机恒等核对：本地/远端 SHA 相等、`worktree_clean`、blob 长度一致均为本机 git 读数，非独立第三方交叉验证；`git ls-remote` 仅取远端 ref，我无法重放其 HTTP/TLS 会话、无法证明远端未被 force-update、也无法查看 GitHub 服务器端状态或其它分支/历史中的潜在密钥。
- 仅核验 `main` 单一 ref 的提交树；agent 分支 `agent/r109-harbor-sync/wb-main` 仅看 diff --stat，未逐 blob 检查其 T3 写入内容。
- 无法看到/未逐字读取：工作项目 `ccfa-review-reports/` 全量 mtime 语义、`goal-ledger.md` 完整 791,507 B 历史、`R128-ACQUIRE.py`/`R128-VERIFY.py` 的运行过程（按独立性要求未运行，仅阅读其文本作比对）、任何 untracked/ignored 文件。validator 的「LATEST independent review governs」依赖本机 mtime（可变元数据），非字节不可变事实。
- 0 真实凭证命中仅对本文所列有限模式成立，且已知含真实凭证值的文件被有意排除；这不构成「绝对无任何秘密」的证明。

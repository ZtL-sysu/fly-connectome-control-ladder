REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO

# R124 独立复核报告（全新隔离「门 / 证据层」复核者）

- 复核者身份：`general-purpose-1`，全新隔离，未接收任何期望分数 / 分数锚点 / 期望结论；不知道也不寻找「应该得出什么结论」。
- 复核对象：`r3r5-R124/raw/` 13 份原始字节 + 项目内既有独立文件。
- 纪律：全程只读；未 import 本轮 `R124-ACQUIRE.py` / `R124-BUILD-MANIFEST.py` / `R124-verify.py` / `R124-verify-v1.py`；未运行本轮任何 verifier 作为复算结果；未把本轮任何 JSON 当实质数据源；未联网、未跑 git、未修改任何既有文件；本报告一次写入。
- 口径：只做门 / 证据层复核，**不是稿件评审**；不输出任何加粗 Overall 数值行、不给任何分数、不评价论文质量。

---

## 0. 解析口径说明（我的复算方法）

1. **数据源**：仅 `raw/` 13 份文件的磁盘字节（`open(path,'rb').read()`）+ 下列独立文件：`gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md`、`gate-G0-R106/R106-ROUND-AUDIT.md`、顶层 `pipeline-state.json`、`ccfa-review-reports/`（r95）、以及本轮 readout 类产物（仅作声明值 / 措辞核对）。
2. **声明值对照（不作数据源）**：`R124-SOURCE-MANIFEST.json` 用于 A 组「声明值」比对；`R124-ROUND-AUDIT.md`、`R124-VERIFICATION.json`、`R124-VERIFICATION-V1.json`、`R124-GUARD-READOUT.txt`、`R124-VALIDATOR-READOUT.json` 仅用于读出本轮的声称，再与我从字节重算的结果对照。
3. **自写解析逻辑**：Python 标准库 `os` / `hashlib` / `json` / `re` / `str.count`。字节数 = `len(b)`；SHA-256 = `hashlib.sha256(b).hexdigest()`；JSON 结构 = `json.loads`；子串命中 = `b.decode('utf-8','replace').count(s)`（逐字、区分大小写、区分 `Erdos-Renyi` 与 `Erdős–Rényi`、`10-13` 与 U+2212 上标）；字符数另用 `len(str)` 与 `len(str.encode())` 双算。
4. **HTTP 状态口径**：HTTP 200/301/429 **无法从字节本身证明**，故只能作为 manifest `observed_http_status` 的「声明值」核对；仅 301 页正文 `301 Moved Permanently` 与 429 正文 `error code: 1015` 提供字节级佐证。8 份 200 的真实性不在本地字节可证范围内。
5. **二进制 / 凭证判定**：UTF-8 可解码性 + NUL 计数 + 高字节计数 + 数据集/权重扩展名白名单；凭证扫描 = `/Users/`、`/home/`、凭证类文件名、`Bearer <token>`、常见密钥正则，逐文件给 count。
6. **逐字证据**：所有命中与未命中均给出 count 与逐字上下文（或 repr）。

---

## 1. 逐组 MATCH / MISMATCH 计数总表

| 组 | 我复算的检查数 | MATCH | MISMATCH |
|:--|---:|---:|---:|
| A 清单 / 字节 / SHA / total / HTTP 计数 | 7 | 7 | 0 |
| B bioRxiv details API | 12 | 12 | 0 |
| C Crossref work | 12 | 12 | 0 |
| D 二手镜像 followed / 裸域 | 5 | 5 | 0 |
| E 两份 arXiv abs | 6 | 6 | 0 |
| F 429 文件 / v1 HTML 冻结件 | 3 | 3 | 0 |
| G R106 G0 独立评审 §6 / R106 轮次审计 | 7 | 7 | 0 |
| H pipeline-state.json | 8 | 8 | 0 |
| I 路径 / 凭证 / 大文件 / 二进制 | 6 | 6 | 0 |
| **合计** | **66** | **66** | **0** |

> 说明：B-11 / C-11 的「是否含 `0.686` / `0.846` / `0.930 vs`」答案为 **ABSENT（逐字 0 命中）**；本轮审计并未声称这些数字存在于本地字节（见 §2(f) / §3 M3），故判定为 MATCH（事实状态与声明一致），而非 MISMATCH。

### A 组 — 13 份文件名 / 字节数 / SHA-256 / total / HTTP 计数 → 7 MATCH / 0 MISMATCH

我从 `raw/` 逐字节重算（`os.listdir` + `read()` + `sha256`），13/13 文件名集合与 manifest `files[].file` 完全一致；13/13 字节数与 13/13 SHA-256 与 manifest 声明逐条相同：

| 文件 | 字节数 | SHA-256（我的重算 = 声明值） |
|:--|---:|:--|
| `arxiv-2609.39248-abs.html` | 43328 | `05013512ef058b0d162e4f82ab9985fb481c21a2273e7471eb157ae699237700` |
| `arxiv-2610.13018-abs.html` | 42453 | `eb3ae5b645c86dc1963c092179ad443da4f27e030f887ec92cfa133a0e015cf0` |
| `biorxiv-api-details.json` | 64741 | `09abab723319950682fa6ec7ae31de0be1faa42c2b711dd26311c28509e7ceec` |
| `biorxiv-api-v1-na.json` | 64741 | `09abab723319950682fa6ec7ae31de0be1faa42c2b711dd26311c28509e7ceec` |
| `biorxiv-v1-early-full.html` | 17 | `e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602` |
| `biorxiv-v1-retry.html` | 17 | `e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602` |
| `biorxiv-v1.html` | 17 | `e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602` |
| `biorxiv-v3.html` | 17 | `e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602` |
| `connect-biorxiv-relate181.html` | 58714 | `8501cd131ae26cb74f732066cb40f70dc0e8d5432275197e64442923f885db62` |
| `crossref-work.json` | 11160 | `1493ba22ad7f5d31a567766424d37ed7f807a7f72a09a4b957a60f481acb0971` |
| `europepmc-search.json` | 841 | `e0b3e78f345c8eb46791e01a14aef417ba5c3445bb2857e9fbe7a71685f469ba` |
| `secondary-mirror-article-followed.html` | 37429 | `a791fd8c3de91a1cbc32090f5cd2f84e039c4f2cfe6f6bc4b9931a69d995f3fc` |
| `secondary-mirror-article.html` | 265 | `6c8b6d62f3e1986c875b60f8929792fa1e21bf21f8a78a433b5116687aa58008` |

- **total**：逐文件求和 = **323740 B**，与 manifest `totals.bytes_total = 323740` 一致（MATCH）。分类复算：8 份 200 = 323407 B；1 份 301 = 265 B；4 份 429 = 68 B；合计 323740 B。
- **HTTP 计数**：manifest `observed_http_status` 的 Counter = `{200: 8, 301: 1, 429: 4}`，与 `totals.http_200_count=8 / http_301_count=1 / http_429_count=4` 自洽（MATCH，声明值口径）。字节级佐证：`secondary-mirror-article.html` 正文逐字含 `301 Moved Permanently`；4 份 17 B 文件均为 `error code: 1015\n`。8 份 200 无法由字节独立证明（见 §0.4）。

### B 组 — bioRxiv details API → 12 MATCH / 0 MISMATCH

- **collection 恰 12 条**：`len(collection) = 12`，`messages = [{'status':'ok','category':'all'}]`。
- **版本号序列**：`['1','2','3','4','5','6','7','8','9','10','11','12']`（str 类型）。
- **日期序列**：`2026-06-12, 2026-06-13, 2026-06-23, 2026-06-23, 2026-06-24, 2026-06-25, 2026-06-29, 2026-06-30, 2026-06-30, 2026-07-02, 2026-07-14, 2026-10-16`（v1→v12 非递减）。v12 日期 `2026-10-16`。
- **v1 标题（逐字）**：`Connectome wiring shapes population-level neural geometry in the Drosophila visual system`。
- **v2+ 标题（逐字，v2–v12 共 11 条全同、`set()` 大小 = 1、与 v1 不同）**：`Representational geometry as a fidelity metric for connectome-constrained networks: evidence from the Drosophila visual system`。全文 `DISTINCT_TITLES = 2`。
- **12 个 `abstract` 全部逐字节相同**：12 份 `abstract.encode('utf-8')` 的 SHA-256 集合大小 = 1；**长度 = 4816 字节 = 4816 字符（纯 ASCII，无非 ASCII 字符）**；**SHA-256 = `555e28f9fef30a3a93d9196dd6049e7ffce47afae248c2ebd00d1951a6976702`**（前缀 `555e28f9fef3` 与审计 :49 一致）。整份 details JSON 中 `p < 10-13 in every case` 命中 12 次（每版本 1 次）。
- **该 abstract 逐字命中**：`p < 10-13 in every case` = 1、`closes the gap completely` = 1、`trained Erdos-Renyi on OFF-polarity structure` = 1、`size-matched` = 1。
- **逐字未命中（全 13 份 raw 交叉扫描 total=0）**：`0.686` = 0、`0.846` = 0、`0.930 vs` = 0、`0.930` = 0。⇒ 这些数值**不存在于任何一手本地字节**。
- **`/1` 后缀**：`biorxiv-api-v1-na.json` 与 `biorxiv-api-details.json` 直接 `a == b` = **True**（64741 B 各自、SHA 同 `09abab72…`）⇒ 逐字节相同，后缀非版本选择器。

### C 组 — Crossref work → 12 MATCH / 0 MISMATCH

- **DOI**（逐字）：`10.64898/2026.06.10.731214`。
- **title**（逐字，含 JATS 斜体标记）：`Representational geometry as a fidelity metric for connectome-constrained networks: evidence from the\n                  <i>Drosophila</i>\n                  visual system`（= v2+ 标题）。
- **type**：`posted-content`。
- **created** = `2026-06-12`（`date-time 2026-06-12T23:10:11Z`）；**posted** = `2026-06-12`；**indexed** = `2026-10-21`（`date-time 2026-10-21T12:38:25Z`）；另 `deposited = 2026-10-21`。
- **abstract 逐字命中**：`closes the gap` = 1、`size-matched` = 1、`Erdős–Rényi` = 2（U+0151 + U+2013 形式；明文 `Erdos-Renyi` = 0）、`<jats:sup>−13</jats:sup>` = 1（其中 `−` 我独立确认码位 **U+2212**，段 repr `'<jats:sup>−13</jats:sup>'`）。
- **abstract 逐字未命中**：`0.686` = 0（全 JSON 文件扫描亦为 0）。
- **license URL**（逐字）：`http://creativecommons.org/licenses/by/4.0/`（CC BY 4.0，`content-version: vor`，`delay-in-days: 0`）。

### D 组 — 二手镜像 followed 页 / 裸域 → 5 MATCH / 0 MISMATCH

- `secondary-mirror-article-followed.html`（37429 B）JSON-LD 中 `datePublished` 唯一值（逐字）：`"datePublished": "2026-10-16"`，与 B 组 API **v12 日期 `2026-10-16` 逐字相等**（`EQUAL = True`）。
- 逐字命中（各 count = 1）：`p < 10-13 in every case`、`closes the gap completely`、`trained Erdos-Renyi on OFF-polarity structure`；`0.686/0.846/0.930` 均 0。
- 裸域 `secondary-mirror-article.html`（265 B）逐字为 `301 Moved Permanently` 页：`<title>301 Moved Permanently</title>`，指向 `https://www.aimedicalcompendium.com/article.cfm?id=253759`（MATCH，301）。

### E 组 — 两份 arXiv abs（逐字命中次数 + v1 时间戳）→ 6 MATCH / 0 MISMATCH

| 文件 | `22871090` | `22891264` | `9 Oct 2026` | `12 Oct 2026` |
|:--|---:|---:|---:|---:|
| `arxiv-2609.39248-abs.html` | **1** | 0 | 0 | 0 |
| `arxiv-2610.13018-abs.html` | 0 | 0 | **2** | 0 |

- `22871090` 唯一命中上下文（逐字）：`...dated research log: <a href="https://doi.org/10.5281/zenodo.22871090" rel="external noopener nofollow" class`；`22891264` 全 13 份 raw **total = 0**。
- `9 Oct 2026` 两次命中（逐字）：`[Submitted on 9 Oct 2026]` 与 `Fri, 9 Oct 2026 05:20:38 UTC (147 KB)`；`12 Oct 2026` 全 13 份 raw **total = 0**。
- **v1 时间戳（逐字）**：`arxiv-2609.39248-abs.html` → `[v1]</strong>\n        Wed, 30 Sep 2026 08:13:40 UTC (1,859 KB)`，另 `Submitted on 30 Sep 2026`；`arxiv-2610.13018-abs.html` → `[v1]</strong>\n        Fri, 9 Oct 2026 05:20:38 UTC (147 KB)`，另 `Submitted on 9 Oct 2026`。
- 附：两份 title 标签分别为 `[2609.39248] Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison` 与 `[2610.13018] FlyHack: Stress-Testing Mechanistic Claims in a Connectome-Constrained Visual Model`。

### F 组 — 4 份 429 文件 / v1 HTML 本地字节冻结件 → 3 MATCH / 0 MISMATCH

- 恰好 4 份文件为 17 字节：`biorxiv-v1.html`、`biorxiv-v1-retry.html`、`biorxiv-v1-early-full.html`、`biorxiv-v3.html`。
- 4 份内容逐字节均为 `b'error code: 1015\n'`（`== b"error code: 1015\n"` 全部 True，`repr` 一致）。
- **不存在 v1 HTML 页的本地字节冻结件**：13 份 raw 中含 `error code: 1015` 的恰为上述 4 份；v1 标题 `Connectome wiring shapes population-level neural geometry` 仅出现在两份 API JSON 的 v1 记录 title 字段（各 1 次），无任何 v1 HTML 正文/摘要字节。审计 :50 / :111 / :135④ 自述「无本地字节冻结件 / WebFetch 转述不得冒充字节冻结件」与字节事实一致。

### G 组 — R106 独立文件 → 7 MATCH / 0 MISMATCH

- `gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md` **§6 确有 R1–R9 共 9 项**（逐条 `R1（闭 gap 1）… R9 …`，行 161–169）。
- §6 R3（行 163）逐字含 `bioRxiv DOI 10.64898/2026.06.10.731214` 与 `标明具体版本（v1 阳性 vs v3 大体阴性）`（MATCH）。
- `gate-G0-R106/R106-ROUND-AUDIT.md` **§11（行 181–229）为「只追加」补录段**，逐字含：
  - 撤回 W5（行 188–199）：`上文 §5.2 / §5.3 … 的「R99 引用 v1 摘要、版本错配」核心指控不成立，已撤回`；
  - 更正 Zenodo（行 200）：`另更正：Park Zenodo 一手 Comments 为 DOI 10.5281/zenodo.22871090（非 22891264）`；
  - 更正日期（行 201）：`Dhawan 一手提交日 Fri, 9 Oct 2026（非 10-12）`；
  - 段首（行 181）逐字 `（03:5x–04:0x，只追加；上方 R106 段的核心发现已撤回）`，行 199 `按 RGE 纪律不改写历史字节，只以本补录 + 各处追加段更正`。
- 注：§5.4（行 92）历史段落仍保留错误值 `22891264 v4.0`，与 §11 更正并存，符合「不改写历史字节」。

### H 组 — 顶层 `pipeline-state.json`（3723 B / SHA `bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d`）→ 8 MATCH / 0 MISMATCH

- `CCFA-startup`：`status = "passed"`，`gate_verdict = "pass"`（唯一非 pending 阶段）；`history` 含 `reopen` + `pass`。
- `G0`：`status = "pending"`，`gate_verdict = "pending"`，**`inputs: []`、`evidence: []` 均为空**。
- `G1`–`G8`（8 个）、`validation`、`handoff`：`status = "pending"`，`gate_verdict = "pending"`，`inputs/evidence` 全空。
- 共 12 个 stage，顺序 `CCFA-startup, G0, G1…G8, validation, handoff`。⇒ 无任何门被标 passed / 晋级。
- 附：`ccfa-review-reports/` 最新仍 `paper-null-ladder-r95-independent-review-20261111.md`（11-11 15:01），其加粗结论数值为 6 / Confidence 4（行 419）；与本轮审计 :5/:127 的 governing 声明一致。

### I 组 — 仅 `raw/` 13 份文件 → 6 MATCH / 0 MISMATCH

- **本机绝对路径**：13 份文件内 `/Users/` = 0、`/home/` = 0（逐文件扫描全部 CLEAN）。
- **凭证文件名**：13 个文件名中 credential-like（`id_rsa`/`.pem`/`credentials`/`secret`/`token`/`.env`/`.aws`/`api_key` 等）= NONE。
- **`Bearer <token>` / 凭证正则**：13 份内容 `Bearer\s+[A-Za-z0-9._-]+` = 0、`Bearer\s` = 0、`PRIVATE KEY|id_rsa|credentials|api[_-]?key|passwd|password\s*[=:]` = 0（全部 CLEAN）。
- **最大单文件**：`biorxiv-api-details.json` / `biorxiv-api-v1-na.json` 并列 **64741 B**；全部尺寸 `[17,17,17,17,265,841,11160,37429,42453,43328,58714,64741,64741]`。
- **数据集 / 权重 / 二进制**：13 份全为 `.json` / `.html`，无 `.pt/.npy/.h5/.ckpt/.pkl/.bin/.onnx/.safetensors/.zip/.pdf` 等；13/13 UTF-8 可解码、NUL 计数全 0（仅 `connect-biorxiv-relate181.html` 有 10 个高字节，为 UTF-8 多字节文本字符，非二进制）。

---

## 2. 12 类点名夸大逐条判定

判定含义：CONFIRMED = 本轮产物确实作出该声称；REFUTED = 本轮产物未作出该声称（多为明确否认）。**12 类全部 REFUTED**。

| # | 点名夸大 | 判定 | 依据（逐字 / 复算） |
|:--|:--|:--|:--|
| (a) | 声称取得科学结果 | **REFUTED** | 审计 :3–4「`NOT_..._SCIENTIFIC_RESULT`」「**不是**科学结果」、:120「零…科学指标 / 新正向证据」、:123「增量是证据层、不是分数层」、:127「第 3 步前置（实质正向新科学证据）未满足」。raw 13 份全为第三方公开文本元数据 / HTML，无本项目结果。首行 `Scientific result claimed: NO`。 |
| (b) | 声称做了模型前向 / 训练 | **REFUTED** | 审计 :120「零前向 / 推理 / 训练 / 标签 / 数据集」、:117「零前向 / 训练 / 标签 / 数据集」；I 组独立扫描 13 份 raw 零权重 / 零数据集 / 零二进制。首行 `Forward pass performed: NO`。 |
| (c) | 声称门禁通过 / 晋级 | **REFUTED** | 审计 :119「**零门晋级**（G0 pending）」、:92「G0–G8 / validation / handoff 全 pending」；H 组复算 pipeline-state.json 确为 G0 pending、无任何 passed 变更。首行 `G0 may be passed: NO`。 |
| (d) | 声称改写了历史字节 | **REFUTED** | 审计 :67「不改写原字节…全部原样保留」、:119「零状态写回」、:131「报告原文与历史正文零改动」；`raw/` mtime 15:21:40 稳定，R106 审计 §11 与 pipeline-state.json（SHA `bcb48bb9…`）历史字节未变。 |
| (e) | 声称把二手镜像当一手来源 | **REFUTED** | 审计 :57「镜像始终为**二手**，只用于交叉印证 v12 口径，**不作为一手结论来源**」、:38「二手镜像」、:23「改一手来源」。注：:55 局部措辞把「镜像正文」列入「3 份独立一手字节」与 :57 口径冲突，已作为瑕疵 M2 记录，但**不等于**本轮整体把镜像当一手来源。 |
| (f) | 声称 WebFetch 转述是本地字节冻结件 | **REFUTED** | 审计 :50「**本地无 v1 页面字节冻结件** ⇒ 该阳性摘要仅作 WebFetch 转述登记，**不计入一手冻结件**」、:111「不以 WebFetch 转述冒充一手件」、:135④「WebFetch 转述不得冒充字节冻结件」；F 组复算 4 份 v1/v3 本地件全为 17 B `error code: 1015`，确无 v1 HTML 正文字节。 |
| (g) | 声称 v3 是结论转折版本 | **REFUTED** | 审计 :55「**「v3 是结论转折版本」不成立**：v3 仅为 12 版之一（2026-06-23），API 不提供每版摘要」、:135①「中间版本的摘要未取得就不得作转折版本主张」；B 组复算 12 份 abstract 逐字节全等，v3 无任何版本级特殊地位。 |
| (h) | 声称 API 的 abstract 是版本化历史摘要 | **REFUTED** | 审计 :44 标题「API 的 `abstract` 是『当前摘要回填』，**不是版本化历史摘要**」、:49「**不能**把「API 里 v1 的 abstract」当作 v1 的历史摘要」、:135①「字段位置 ≠ 版本归属」；B 组复算 12 份 abstract 长度均 4816、SHA 同为 `555e28f9…`。 |
| (i) | 声称 R106 造假 | **REFUTED** | 审计 :55「**不主张 R106 判错**、不回溯改写 R106 任何字节」「W6 … 中心判断成立」、:57「这是**时点 / 端点差异，不是 R106 造假**」、:65「已撤回，本轮不重复补正、不改写历史字节」。 |
| (j) | 声称 R3/R5 已闭合或 gap 已闭合 | **REFUTED** | 审计 :25「**取证完成 ≠ gap 闭合**」、:75 R3 剩余阻塞「登记 / 定稿须 G6 / G7；v1 页面本地字节未取得」、:77 R5「更正动作不得自我认证 ⇒ G4 / R9」、:83「剩余 R2 / R6 / R7 / R8 / R9 全部落在 designated gate owner 裁决」、:127「0 篇达标」。:55 的「证据层闭合」明确限定为「R3 **可核验部分**」，非 gap 闭合。 |
| (k) | 声称有 4090 / L4 / H20 能力或主张 | **REFUTED** | 审计 :121「**无 4090 / L4 / H20 主张**」；raw 13 份及本轮 readout 产物无任何 GPU 型号能力主张（I 组 / 全文扫描零命中）。 |
| (l) | 声称产生新的评审分数行或改变 governing | **REFUTED** | 审计 :121「未产生加粗 Overall 数值行、未自评 governing」、:5 / :127「governing 仍 R95 = 6.0 / Confidence 4.0」；我独立扫描 `r3r5-R124/` 内**行首数值加粗结论行 = 0**（:5 / :16 / :121 及 `R124-GUARD-READOUT.txt:23` 的 `含 **Overall:** X` 均为成功标准 / 统计 / 否定性提及，`R124-VALIDATOR-READOUT.json:23` 为引用 r95 的 6.0，非新行）；`ccfa-review-reports/` 最新仍 r95（无 R124 报告）；全项目晚于 15:00 的新 md 仅 R124 审计本身，无新分数行。 |

---

## 3. 瑕疵分级（`R124-ROUND-AUDIT.md` 逐条核对）

### 3.0 分类汇总数字复算（专项核对，结论：**无缺陷**）

- `13 份 / 323,740 B / 8×200 + 1×301 + 4×429`（:27）：13 = 8+1+4；323740 = 逐文件求和 = 分类求和（323407+265+68）；全部可复算一致。
- `12 个版本`（:46）/ `v2–v12 标题（11 个）`（:48）/ `各 4,816 字符`（:49）/ `sha256 前缀 555e28f9fef3`（:49）：B 组复算 12 条、11 条、4816 字符（=4816 字节，纯 ASCII）、前缀吻合。
- `3 份`（:55）/ `4 次重试`、:40 `×4`（:50/:111）/ `6/6`（:29、:99）/ `7 项 = 6+1`（:101、:113）/ `145 = A45+B27+C14+D10+E6+F9+G16+H12+I6`（:99）：类别求和 45+27+14+10+6+9+16+12+6 = **145**，自洽。
- `19 行 / 19 文件`（:16）：**例外，见 L1**（计数口径未限定，独立扫描不可得 19/19）。

### HIGH（事实错误 / 数据不一致 / 编造）：**无**

A–I 共 66 项事实核验 66 MATCH / 0 MISMATCH；未发现事实错误、数据不一致或编造。审计中全部可核验数字（字节、SHA、日期、命中次数、版本号、门状态）均与我从字节重算一致。

### MEDIUM

| 编号 | 文件:行号 | 性质 | 准确表述与依据 |
|:--|:--|:--|:--|
| **M1** | `R124-ROUND-AUDIT.md:29`（对照同目录 `R124-GUARD-READOUT.txt`） | 范围未限定 | :29 逐字「零数据集 / 权重 / 二进制 / 大文件 / **本机路径 / 本项目凭证**（verifier I 组 6/6）」。句首「`raw/` 下全部为第三方公开小文本」与「（verifier I 组 6/6）」把该检查**实际**限定在 13 份 raw 文件（本人 I 组扫描在该范围内确为 0 命中，MATCH）；但「零…本机路径 / 本项目凭证」作为独立短语**未写明文件集**，读者按「本轮产物」口径理解即与事实冲突：同轮 `R124-GUARD-READOUT.txt` 含 **13 处** `/Users/xhf/...` 绝对路径（行 14/16/18/20/22/24/26/30/32/34/36/38/40，我独立 grep 计数 13），`R124-VALIDATOR-READOUT.json` 为 0。准确表述应为：「**仅对 `raw/` 13 份字节**扫描未发现 `/Users/`、`/home/`、凭证文件名、Bearer 令牌；本轮 readout 类产物含本机绝对路径，不在该扫描范围内」。属范围未限定，**非事实错误**（限定范围内结论为真）。 |
| **M2** | `R124-ROUND-AUDIT.md:55`（对照 `:38`、`:57`） | 口径混用 / 措辞不精确 | :55 逐字「阴性，有 **3 份独立一手字节：API abstract + Crossref abstract + 镜像正文**」。同文件 :38 标「**二手镜像**」、:57 逐字「镜像**始终为二手**…**不作为一手结论来源**」⇒ 把「镜像正文」列入「一手字节」与自述口径直接冲突。且三者并非「独立」来源：B/C/D 组复算显示三者是**同一份当前摘要**的三种重现（bioRxiv 明文 4816 B / Crossref JATS 5549 字符含 U+2212 上标 / 镜像 HTML 正文），不是三份彼此独立的一手证据。准确表述应为：「2 份官方 API 一手字节（bioRxiv details、Crossref work）+ 1 份二手镜像正文仅作交叉印证」。 |
| **M3** | `R124-ROUND-AUDIT.md:46`、`:50`、`:52`、`:55`（对照 `:44`、`:49`、`:135`①） | 时点 / 版本口径混用，与自述负面结论不完全一致 | 自述负面结论（:55）：「**无法从本地字节确定阴性结论首次出现于哪一版**」「中间 10 版摘要未取得、**不作版本归属主张**」、:135①「字段位置 ≠ 版本归属…不得作转折版本主张」。但同段收窄表述「**v1 页面（阳性，无本地字节）vs 当前 / v12 口径（阴性…）**」仍是二分版本框架，存在三处张力：①「v1 阳性」全部来自 :50 的 **WebFetch 转述**（`0.686` / `0.846` / `0.930 vs` / `Δr = 0.327`），B 组复算这些数值在 13 份 raw 中 **total = 0**，即无任何本地字节支撑，却被用作版本归属的一端；②「v12 口径」把 :44/:49 已判定「**当前摘要回填到全部 12 条版本记录**」的单一当前摘要归属给 v12，唯一依据是 :52 二手镜像 `datePublished = 2026-10-16` 与 v12 日期相同，而非任何 v12 专属一手摘要；③「12 个版本」易被读作 12 份不同内容，实为 12 条版本记录共享 1 份 abstract（12/12 全等）。准确表述应严格收窄为：「当前（**无版本归属**）口径为阴性，有官方 API 一手字节；v1 页面阳性仅为 WebFetch 转述、无本地字节；v1→当前之间 10 版摘要未取得，不指定任何转折版本」。 |

### LOW

| 编号 | 文件:行号 | 性质 | 准确表述与依据 |
|:--|:--|:--|:--|
| **L1** | `R124-ROUND-AUDIT.md:16` | 计数口径未限定 / 不可独立复算 | :16 逐字「全项目数值加粗 Overall 行 **19 行 / 19 文件**」，未给出计数规则。我用多种口径独立扫描全项目：行首严格（`^\*\*Overall:\*\* [0-9]`，含空格）得 **13 文件 / 15 行**；`*.md` 任意位置含数字得 56 文件；全类型任意位置得 74 文件 / 143 行 —— 均非 19/19，故该汇总数字**不可由已声明口径复算**。该行核心结论 `new_governing_candidates=0`（无新 governing 候选 / 无新分数行）经我独立核验**成立**（见 §2(l)）；此处仅为汇总口径未限定。 |
| **L2** | `R124-ROUND-AUDIT.md:27`（对照 `:38`、`:57`） | 措辞口径不一 | 小节标题「## 3. **一手冻结件**（13 份 / 323,740 B…）」把 `secondary-mirror-article.html` / `-followed.html` 两份**二手镜像**也纳入「一手冻结件」；而文中「一手 / 二手」多数用于**来源性质**（:23「改一手来源」、:38「二手镜像」、:57「始终为二手」）。若「一手」意为「本轮亲自采集并落盘的字节件」则成立（不违反 :57），但与同一文件的来源口径易混。建议标注为「一手采集的本地字节冻结件（其中 2 份来源为二手镜像）」。 |
| **L3** | `R124-ROUND-AUDIT.md:90`（对照 `R124-GUARD-READOUT.txt`） | 措辞不精确 | :90 逐字「报告写 `/tmp` **未入项目树**」，但同轮 `R124-GUARD-READOUT.txt`（15:26:24 落盘）含 guard 完整输出、确在项目树内。若 readout 为 stdout 转录、而 guard 工具自身报告文件写 `/tmp`，两者可并存；审计未说明二者关系，易被读作「本轮 guard 输出未落盘」。属措辞不精确，**不能据以断定审计事实错误**。 |

---

## 4. 范围限制说明

1. **未联网 / 未重放抓取**：HTTP 200/301/429 只能作为 manifest 的声明值核对，「8 份 200 确实返回该字节」不在本地字节可证范围内；`v1 HTML 页首次 HTTP 200 / 105,400 B`（审计 :50/:111）因无本地字节，**无法验证**，本报告仅确认「4 份本地 v1/v3 相关件均为 17 B `error code: 1015`、无 v1 HTML 正文冻结件」。
2. **A 组为同机自证**：SHA / 字节一致性是「磁盘字节与 manifest 声明一致」，属同目录必然一致性核对，**不构成跨来源独立交叉核验**；它不证明采集 URL 的真实性或响应未被替换。
3. **未运行本轮 verifier**：审计 :99 的 `145 检查 / 145 MATCH / 0 MISMATCH` 及 `A45/B27/…/I6` 分组计数属 verifier 内部口径，我未执行该脚本、不将其作为复算结果；仅核对其类别求和自洽（=145）与本报告 §1 的**我自己的** 66 项检查计数相互独立。
4. **「19 行 / 19 文件」口径未定义**（L1）：我的独立扫描结果依口径而异，已如实列出，不把它当作可复算事实。
5. **并发写入观察**：复核期间 `R124-VALIDATOR-READOUT.json`（mtime 15:26:29）晚于 `R124-ROUND-AUDIT.md`（15:25:58）出现，目录存在并发写入；`raw/`（mtime 15:21:40）在复核全程稳定，本报告全部数值结论基于 `raw/` 稳定字节，不受并发影响。
6. **身份边界**：本报告是门 / 证据层复核，**不是** `ccf-paper-reviewer full` 稿件评审；不含加粗 Overall / Scholarly Confidence 分数行、不给任何分数、不评价论文质量、不判断是否达标、不改变 governing。
7. **首行四字段的依据**：`REPRODUCIBLE_WITH_DEFECTS`（A–I 66/66 事实可复算，但审计存在 M1–M3 / L1–L3 措辞与口径瑕疵）；`G0 may be passed: NO`（H 组：G0 pending、inputs/evidence 空、无 gate judgment）；`Scientific result claimed: NO`（§2(a)）；`Forward pass performed: NO`（§2(b)，I 组零权重/数据集/二进制）。

---

**结语**：13 份一手本地字节在文件名、字节数、SHA-256、总字节数、HTTP 分类计数、API 版本谱系、12 份全等 abstract、Crossref 元数据、镜像口径、arXiv 命中次数、429 负面证据、R106 独立文件与 pipeline-state 门状态上，**全部可由我自写逻辑从字节独立复算且全部一致（66/66 MATCH，0 MISMATCH）**；12 类点名夸大**全部 REFUTED**。审计的实质事实层诚实可复算，瑕疵集中在**范围未限定（M1）、一手/二手口径混用（M2、L2）、版本归属口径与自述负面结论不完全一致（M3）、计数口径未限定（L1）、措辞不精确（L3）**，无 HIGH 级事实错误、数据不一致或编造。分类汇总数字（323,740 B / 8+1+4 / 145 分类和 / 12 版本 / 11 标题 / 4816 字符）均可由逐字节求和或计数复算一致，此项无缺陷。

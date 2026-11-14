**Verdict:** REPRODUCIBLE_WITH_DEFECTS | **G0 may be passed:** NO | **Scientific result claimed:** NO | **Forward pass performed:** NO

# R125 独立复核报告（general-purpose-1）

## 0. 方法与范围
只读复核 15 份字节：`<r125-jats>/raw/` 13 份 + `<r125-jats>/../r3r5-R124/raw/{biorxiv-api-details.json, europepmc-search.json}`。用自有 Python（os/hashlib/json/difflib）重算，未运行 R125-verify.py、validator、guard、git，未 import R125-ACQUIRE，未把任何 R125 产出 JSON 作实质数据源。A–H 与 12 类夸大均在读原始字节、形成独立结论之后，才对照 `R125-ROUND-AUDIT.md` 与 `R125-ACQUIRE.py`（仅作待核声明）。

## 1. 分组复算

### (A) 13 份 raw：文件数 = 13，合计 = 135,063 B
| 文件 | 字节 | sha256 |
|:--|--:|:--|
| api-details-v1.json | 64741 | 09abab723319950682fa6ec7ae31de0be1faa42c2b711dd26311c28509e7ceec |
| api-jats.json | 196 | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 |
| biorxiv-v1-full.xml | 17 | e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602 |
| biorxiv-v1-source.xml | 17 | e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602 |
| biorxiv-v1-source2.xml | 17 | e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602 |
| connect-jats.xml | 58714 | 8501cd131ae26cb74f732066cb40f70dc0e8d5432275197e64442923f885db62 |
| epmc-core.json | 6367 | 0875d916d4800f2bf9e972d2efe47f4b582fd15aaefeb5c834200988cd4dc9ac |
| epmc-fulltext-v2.xml | 150 | 7638ab17cbd5b178781ea8184278412849c3120eb0b953b6a29cfa53fca7a6e7 |
| epmc-fulltext.xml | 150 | c240883c1ab45c19541f1ca4c89abe87ab99e8ff494aedaf99b2f91c0bb5f19c |
| jats-v12.xml | 17 | e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602 |
| jats-v3.xml | 17 | e395ad55dd18b1bf23944d00b156714accfae4ec834df208053575542dfae602 |
| wayback-cdx.json | 3 | 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 |
| wayback-v1.html | 4657 | 91cc23843494a080580be5f537716ecfb1007091754e50848487d6a0080d48c7 |

### (B) 五份「429」文件
文件：`biorxiv-v1-full.xml`、`biorxiv-v1-source.xml`、`biorxiv-v1-source2.xml`、`jats-v12.xml`、`jats-v3.xml`。精确字节载荷均为 `b'error code: 1015\n'`（17 B；hex `6572726f7220636f64653a20313031350a`）。五份 SHA 全同 `e395ad55…`（完整值见 A 组）→ 是，共用一个摘要。注：13 份 raw 中无字面 `429`；`1015` 为 Cloudflare 限流体，HTTP 429 是 `R125-ACQUIRE.py` 声明的状态码（见第 4 节限定）。

### (C) R124 冻结 EPMC lite 元数据 + 两份 500 体
`europepmc-search.json`（resultType=lite，单条 `PPR1251441`）：`hasPDF=N`、`inEPMC=N`、`inPMC=N`、`isOpenAccess=N`、`firstPublicationDate=2026-06-12`、`firstIndexDate=2026-06-15`。
两份保留 500 体 `epmc-fulltext.xml` 与 `epmc-fulltext-v2.xml`（各 150 B，时间戳相差约 3 秒）：**两者均**含 `"status":500` / `"Internal Server Error"`（HTTP-500 标记），且均含 `"path":"/europepmc/webservices/rest/PPR1251441/fullTextXML"`（fullTextXML 路径）。是，均满足。

### (D) `epmc-core.json`
- `id=PPR1251441`、`source=PPR`、`doi=10.64898/2026.06.10.731214`、`license="cc by"`、`dateOfCreation=2026-06-15`、`firstPublicationDate=2026-06-12`、`firstIndexDate=2026-06-15`、`hasPDF=N`、`inEPMC=N`。
- `fullTextUrlList.fullTextUrl` 长度 = 1；唯一 URL `https://doi.org/10.64898/2026.06.10.731214`（`documentStyle:"doi"`、`site:"DOI"`）→ 是 DOI 解析器，不是全文/XML 链接。
- `abstractText` 长度 = 4,847 字符（sha256 `5692a5117d2434cced30701abbc7b119781dc765254c44ca464e3a85e8ea80cc`）。
- 与 bioRxiv details API 摘要（4,816 字符）相似度（自有 difflib 计算）：以 `(epmc, biorxiv)` 为参数、默认 autojunk 得 0.8997；关闭 autojunk 得 0.9945；做 Unicode/连字符/空白归一后 0.9953–0.9978；以 `(biorxiv, epmc)` 为参数（即 `R125-verify.py` 所用顺序）得 **0.9906**，恰好 22 个非 equal opcode。→ 差异仅为 difflib 参数顺序 / autojunk 与归一口径差别，非数据错误；22 个差异操作全部是空白、逗号、连字符/减号、撇号、`ős–Rényi` 等 Unicode 转写及 `Maisak et al., ` 插入，无语义差异。两份摘要为同一文本。
- 负向措辞在 `abstractText` 中**全部存在且各 1 次**：`largely null result`、`disappears entirely`、`statistically indistinguishable`、`size-matched`、`not the confirmation we set out to find`。（同一批措辞在 bioRxiv API 摘要中亦全部存在。）
- 计数：`0.686`=0、`0.846`=0、`0.930`=0、`0.603`=0（在 `abstractText` 中；在全部 13 份 raw 中亦 total=0；在 bioRxiv API 摘要中亦各 0）。

### (E) R124 冻结 bioRxiv details API
- 版本记录数 = **12**；`version` 字段类型 = **JSON 字符串**（12 条全为 str）；取值集合 = `'1'..'12'`（12 个不同字符串，按序 1→12）。
- 不同 abstract 数 = **1**（12 条完全相同，4,816 字符）；不同 title 数 = **2**（v1=`Connectome wiring shapes population-level neural geometry in the Drosophila visual system`；v2–v12=`Representational geometry as a fidelity metric for connectome-constrained networks: evidence from the Drosophila visual system`）；不同 jatsxml URL 数 = **10**；不同 license 值 = **1**，值 `cc_by`。
- v1 date = `2026-06-12`；第 12 条记录 date = `2026-10-16`。
- v3 与 v4 jatsxml 相同（`.../2026/06/23/...source.xml`）= **是**；v8 与 v9 相同（`.../2026/06/30/...source.xml`）= **是**。
- v1 标题 ≠ v2 标题 = **是**。
- 共享摘要 sha256 = `555e28f9fef30a3a93d9196dd6049e7ffce47afae248c2ebd00d1951a6976702`，前缀 `555e28f9`（审计写 `555e28f9…` 一致）。

### (F) Wayback / api-jats
- `wayback-cdx.json` 精确字节 = `b'[]\n'`（3 B）。
- `wayback-v1.html`：是 Wayback Machine 的「未存档」错误页（`<title>Wayback Machine</title>`、`<div id="error">`、`The Wayback Machine has not archived that URL.`、`archive.org`），即 404 等价的 Wayback 无快照页；但页面内**无**字面 `404` 或 `Not Found` 字符串。审计/ACQUIRE 把它标为 HTTP 404 属声明状态码（限定见第 4 节）。
- `api-jats.json`（196 B）：含 `<title>404 Not Found</title>` 与 `<h1>Not Found</h1>` → 404 标记**存在**。

### (G) 字节一致性
- `connect-jats.xml`（58,714 B，sha `8501cd13…`）与 R124 `connect-biorxiv-relate181.html`（58,714 B，同一 sha）→ **逐字节相同**。
- `api-details-v1.json`（64,741 B，sha `09abab72…`）与 R124 `biorxiv-api-details.json`（64,741 B，同一 sha）→ **逐字节相同**。
- 补充字节事实：`connect-jats.xml` 实为 HTML 页（含 `canonical http://biorxiv.org/about-biorxiv` 的 bioRxiv about 页），并非 JATS 全文，且**不含任何摘要**；负向摘要仅出现在 `epmc-core.json` 与 `api-details-v1.json` 两份中。

### (H) 范围/安全（13 份 raw）
- 本机绝对路径标记 `/Users/`、`/home/`、`C:\`：**全部无**。
- 凭证类标记（api_key/apikey/secret/token/password/bearer/authorization/private_key/credentials 等）：**无**。
- 邮箱形态字符串：`wayback-v1.html` 中有 2 处（值按要求省略）；其余 12 份无。附带发现：`R125-verify.py` 的 `noEmail` H 检查仅当文件同时含 `@` 与 `.com` 才计数，而这两处为 `.org`，故该检查并不能真正证明「零邮箱字面量」——属被引用校验器的检查设计弱点，不影响我从字节独立得出的结论（无路径、无凭证、无总分行）。
- 最大文件：`api-details-v1.json` = **64,741 B**（`connect-jats.xml` 58,714 B 居次）。
- 粗体评审总分数值行（审计第 41 行所指形式）：13 份 raw 中 **0 条**（字面计数 = 0）。

## 2. 12 类点名夸大（CONFIRMED 仅当审计确实作出该夸大）
全部 **REFUTED**（审计逐条显式否定，且与字节一致）：

1. **声称取得项目科学结果 — REFUTED。** 第 4 行 `...NOT_SCIENTIFIC_RESULT`、第 5 行 `Scientific result claimed: NO`、第 61 行「结论（负面，必须照报）」、第 87 行「零科学指标」；13 份 raw 全为 API 元数据/错误体，无结果产物。
2. **声称跑过模型前向/训练/数据集/标签 — REFUTED。** 第 87 行「零模型前向 / 训练 / 标签 / 数据集」，第 41 行「零数据集 / 权重 / 二进制」；raw 中无权重/数据集/标签字节。
3. **声称任何门通过或 stage 状态改变 — REFUTED。** 第 5 行 `G0 may be passed: NO`、第 83 行「G0–G8 / validation / handoff 全 pending」、第 87 行「零门晋级、零 stage 状态改动」。
4. **声称 v1 页阳性摘要已本地字节冻结 — REFUTED。** 第 23 行「无本地字节冻结件」、第 48 行「得到进一步加强，而非被推翻」、第 61 行「仍未闭合」；字节证据：5 份 v1/v3/v12 JATS 尝试均为 17 B `error code: 1015` 错误体，`wayback-v1.html` 为未存档页，无任何 v1 阳性摘要。
5. **声称当前摘要的 3 处端点呈现是 3 个独立来源 — REFUTED。** 第 48 行「不构成多个独立来源；登记为『端点数 +1』，不登记为『独立来源数 +1』」、第 94 行教训④；字节证据：摘要只在 `epmc-core.json` 与 `api-details-v1.json` 两份中出现，后者与 R124 已冻结文件逐字节相同（G），`connect-jats.xml` 不含摘要。
6. **声称 HTTP 429 意味端点永久不可得 — REFUTED。** 第 74 行「不是永久不可得……本轮不主张『永久不可取证』」、第 33 行「见 §5 时点限定」。
7. **声称记录级 license 构成逐资产许可文本 / 闭合 gap 1 — REFUTED。** 第 56 行「均为记录级元数据声明……≠ 逐资产独立许可文本，不计入 gap 1 闭合」、第 94 行教训②；字节证据：`license` 仅为短字符串 `cc by` / `cc_by`，无许可正文。
8. **声称 EPMC fullTextXML 500 是可重试的瞬时故障 — REFUTED。** 审计持相反结论：第 34 行「结构性负面，非瞬时故障」、第 58–59 行「500 是结构性而非瞬时……不是可重试的瞬时故障」、第 94 行教训③。
9. **声称 12 条版本记录对应 12 个可区分版本/可区分全文 — REFUTED。** 第 51–55 行明确「12 条共享 1 份 abstract / 2 个标题 / 10 个 jatsxml URL，v3=v4、v8=v9 撞日期 ⇒ 结构上不可用于版本归属」；E 组字节复算完全吻合。
10. **声称产生了带 Overall 分数的全新独立 full 稿件评审 — REFUTED。** 第 87 行「未起 full 评审、无粗体评审总分数值行、未自评 governing」、第 91 行「不起全新隔离 full 评审」、第 92 行「写本段时尚未回收、不宣称任何审查结论……门 / 证据层复核，非 full 稿件评审」；H 组证实 13 份 raw 中该数值行 = 0。
11. **声称版本归属（哪一版首次带阴性结论）已确立 — REFUTED。** 第 48 行「不据此作任何版本归属主张」、第 50/55 行「结构上不可用于版本归属」、第 61 行「版本二分依旧无一手字节支撑，R3 维持 OPEN」；字节证据：12 条记录共享同一份摘要（E），字节层面根本不存在版本级区分。
12. **声称 raw 或未脱敏本地内容已上传公开仓库 — REFUTED。** 第 76 行「13 份 raw 全部不上传公开仓库；仅同步脱敏摘要」；H 组证实 raw 中无本机绝对路径/凭证，与「仅脱敏同步」一致，本次复核亦无任何网络/上传动作。

## 3. 审计缺陷分级

- **MEDIUM · 第 41 行**：「全部 13 份 ≤ 58,714 B」为假——最大文件是 `api-details-v1.json` 的 64,741 B，而该值正是审计自身第 38 行表格所列，故该上界既与原始字节矛盾、也与本文第 38 行自相矛盾（58,714 实为 `connect-jats.xml` 大小）。正确界应为 ≤ 64,741 B。这既是一处事实错误，也是一处内部数据不一致；不影响任何负面结论。
- **LOW · 第 65 行（并关联第 41 行「verifier H 组 6/6」）**：以「93 MATCH / 0 MISMATCH」佐证安全结论，但被引用的 H 组 `noEmail` 检查（`R125-verify.py:203-204`）只在文件同时含 `@` 与 `.com` 时计数；`wayback-v1.html` 的 2 处邮箱形态字符串为 `.org`，未被覆盖，故「零邮箱字面量」并未被该检查真正建立。属被引用校验器的检查设计弱点（非审计正文的字节级断言，亦非我复算所得结论有误）；审计第 41 行自身列明的安全断言（无路径/凭证/总分行）经我独立复算为真。

## 4. 计数、差异处理与范围限定

- 差异先行核对：我最初按 `(epmc, biorxiv)` 顺序 + 默认 autojunk 得到 0.8997，与审计 0.9906 不符；按指示先排查解析/归一口径，确认按 `R125-verify.py` 的 `(biorxiv, epmc)` 参数顺序即精确得到 0.9906 与 22 个差异操作，故**判为口径差异，不计为数据错误**。其余 A–H 数值与审计全部吻合（除第 41 行上界）。
- 计数：**事实错误 = 1**（第 41 行错误上界）；**数据不一致 = 1**（同一第 41 行与第 38/39 行自相矛盾）；**编造条目 = 0**。
- 范围限定：HTTP 状态码（429/500/404/200）、采集时刻、URL、`105,400 B` 未落盘响应等均为 `R125-ACQUIRE.py` 与审计的**声明值**，我只读原始字节、无网络、无法回放，故不能独立验证这些状态码或请求是否发生过；同理不能验证 `api-details-v1.json`/`connect-jats.xml` 是否「独立」重新抓取（仅能确认其与 R124 冻结件逐字节相同）。
- 超出字节范围、未予核验的声明：第 14 行工作区级评审行计数、第 15/80/81/83 行 governing/validator/guard/pipeline-state 状态与数值、第 82 行 7 份结构权威 SHA、第 11 行 mtime、第 65 行 verifier 检查总数（未运行该脚本）、以及 R124/R121–R123 历史沿革叙述。上述均不作为本报告的证据。
- 我没有运行 R125-verify.py、任何 validator/guard、git，未使用任何 R125 产出 JSON 作实质数据源，未进行任何写操作（本报告文件除外）。

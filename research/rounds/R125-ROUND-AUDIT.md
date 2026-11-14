# R125 心跳轮次审计 — 版本化一手字节缺口的路由穷尽（只读、非门、非科学结果）

**轮次**：R125 · 2026-11-14 16:56–17:3x +0800 · 自动化心跳（ACTIVE，调度未变）
**性质**：`READONLY_VERSION_ROUTE_EXHAUSTION_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`
**首行判定**：`G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`

---

## 0. 第 0 步：并发保护与 governing 登记

- `goal-ledger.md` mtime `2026-11-14 15:54:59`，距唤醒 `16:56:31` ≈ 61.6 min > 10 min。
- 近 12 分钟工作区零写入；仅本自动化会话运行（另有宿主 MCP 进程与本会话 codebuddy --serve，无主会话 / novix 轮询 / runner）。
- 唤醒时全工作区 `R125` 产物 0 份。
- 严格行首 `^\*\*Overall:\*\* [0-9]` 数值行 = **15 行 / 13 文件**（含 `provenance/`、`isolated/` 逐字节副本）；排除自产副本 = **12 行 / 10 文件**。两评审目录最新仍 r95（2026-11-11 15:01）；晚于 r95 的两份报告与 r95 逐字节一致。`new_governing_candidates = 0`。
- ⇒ **并发保护不触发**；governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`，`0 篇达标`、无 COMPLETE 标记。

## 1. 换道理由（RGE4）

R121 已由 governing 评审原文推出「只读审计结构上不升分」的否定性闭环；R122 完成 R106 §6 R4、R123 完成 R1 / gap 1 许可与代码路径一手取证、R124 完成 R3 / R5 一手取证并首次产出 **R1–R9 逐条收敛表**，判定「心跳可自主完成的 §6 项全部穷尽，剩余项收敛到 `G1+G4+G10`」。

本轮**不写第 9 层流程审计、不写 G0 文字补丁、不创建 v4、不在 G0 未过时启动 P3**。本轮做的是 R124 自身**独立复核更正 M3** 明确留下、且 R124「交下轮 ②」把它与「归类 / 登记」并列后一并交出去的**一个仍可自主完成的一手动作**：

> R124 M3 逐字：`「v1 页面（阳性）」→「v1 页面摘要（WebFetch 转述、无本地字节冻结件、非本轮一手结论）」`，并明确 `0.686` / `0.846` / `0.930 vs` 在 13 份 raw 中 **total=0**。

R124 只试过 `www.biorxiv.org/content/...v1` 的 HTML 路径（4 次全 429）。**bioRxiv 官方 details API 自己为 12 条版本记录逐条发布了 `jatsxml` 字段**（指向 `.../content/early/<date>/...source.xml`），这条**按版本取全文的官方路由从未被尝试过**；另有两个独立主机（EBI Europe PMC、Internet Archive Wayback）与 `api.biorxiv.org` 的可能端点也未被穷尽。

**关键区分（本轮的实质贡献之一）**：R124「交下轮 ②」把「v1 页本地字节**是否补取**」与「13 份件的**归类 / 登记**（是否并入矩阵 / `source-manifest.json`、R3 版本口径如何入矩阵、W13 判据书面冻结）」并列后统一交给 designated gate owner 裁决。本轮严格只做**前半段的一手字节取证**（自主可达的只读动作），**归类 / 登记 / 矩阵定稿 / 判据冻结一律不碰**，仍按 R120 G4/G5/G6/G7 留给 gate owner。

## 2. 一手取证结果（13 份 raw / 135,063 B / 每份即时落盘 + SHA）

| 端点族 | 结果 | 判定 |
|:--|:--|:--|
| `www.biorxiv.org` 官方 per-version JATS ×5（v1 原路径、v1 备用路径、v1 DOI 形式、v3、v12） | 5 × HTTP 429 / 17 B / `error code: 1015\n`，5 份 SHA 全同 `e395ad55…` | **负面**，见 §5 时点限定 |
| EBI Europe PMC `fullTextXML` ×2 | 2 × HTTP 500 / 150 B | **结构性负面**，非瞬时故障 |
| EBI Europe PMC `resultType=core` | HTTP 200 / 6,367 B | **新的第三个独立一手端点**（详见 §3） |
| Internet Archive CDX + `/web/2026/` | CDX `[]\n`（3 B）；快照 HTTP 404 / 4,657 B | **负面** |
| `api.biorxiv.org/jats/...` | HTTP 404 / 196 B | **负面**（该端点不存在） |
| `api.biorxiv.org/details/.../1` | HTTP 200 / 64,741 B | 与 R124 冻结的未加后缀 details 响应**逐字节一致** ⇒ 独立复现 R124「`/1` 不是版本选择器」的负面结论 |
| `connect.biorxiv.org/relate/content/181` | HTTP 200 / 58,714 B | 与 R124 冻结副本**逐字节一致** ⇒ 重复件，不计新来源 |

- 全部 13 份合计 135,063 B，**最大单件 64,741 B**（`api-details-v1.json`；次大 58,714 B 为 `connect-jats.xml`）；零数据集 / 权重 / 二进制 / 本机绝对路径 / 凭证 / `**Overall:**` 数值行（verifier H 组 6/6）。
  - 自查纠错留痕：本轮文档初稿曾把「最大单件」误写为 58,714 B（把 connect 件的尺寸当成了全集最大值），在生成 `metrics.csv` 时由程序逐字节求最大值暴露，随即在**本轮尚未发布的自产文档**中就地更正为 64,741 B；`R125-SOURCE-MANIFEST.json` / verifier / raw 字节 / 历史检查点均未改动。属派生汇总数字表述错误，非数据不一致、非编造。
- `R125-ACQUIRE.py` 为只读来源映射（不复跑任何网络请求）；`R125-SOURCE-MANIFEST.json` 由 raw 字节独立生成。

## 3. 实质新发现（第三方文本事实，严格收窄）

**① 第三个独立一手端点，且是当前摘要口径（阴性）的又一处一手字节呈现。**
Europe PMC `resultType=core`（EBI 主机，独立于 bioRxiv / Crossref / 二手镜像）返回**完整 `abstractText` 4,847 字符**，与 bioRxiv details API 的 4,816 字符摘要 `SequenceMatcher` 相似度 **0.9906**，22 个差异操作全为排版 / 空白 / 连字符 / 逗号 / 人名转写归一（`Erdős–Rényi` vs `Erdos-Renyi`、`Maisak et al.` 插入、Unicode 减号等），**无实质语义差异**。该摘要含 `largely null result` / `disappears entirely` / `statistically indistinguishable` / `not the confirmation we set out to find` 等阴性措辞，且 `0.686` / `0.846` / `0.930` / `0.603` 四个「v1 阳性」数字 **total = 0**。
⇒ 与 R124 M2/M3 更正一致：**同一份当前摘要在多个端点重现，不构成多个独立来源**；本轮把它登记为「端点数 +1」，**不**登记为「独立来源数 +1」，也**不**据此作任何版本归属主张。R124 M3「v1 页面摘要无本地字节冻结件、非一手结论」的收窄**得到进一步加强，而非被推翻**。

**② 官方按版本 JATS 路由在结构上不可用于版本归属。**
R124 冻结的 details API 12 条版本记录中：
- `version` 为**字符串** `'1'..'12'`（v2 verifier 的期望值假设错误见 §4）；
- **12 条记录共享 1 份 abstract**（4,816 字符 / SHA 前缀 `555e28f9…`），**2 个不同标题**（v1 ≠ v2–v12）；
- 但 `jatsxml` **只有 10 个不同 URL**：v3/v4 同为 `2026-06-23`，v8/v9 同为 `2026-06-30` ⇒ **即使 429 解除、JATS 全文可取，也有两对版本在官方端点上不可区分**。
⇒ R106 §6 R3「标明具体版本」的**端点侧上限**首次被字节级坐实；这是端点的结构性限制，不是限流造成的。
- 12 条 `license` 全为 `cc_by`，EPMC `license = "cc by"` —— 均为**记录级元数据声明**，按 R123 教训 **≠ 逐资产独立许可文本**，**不**计入 gap 1 闭合。

**③ Europe PMC 的 500 是结构性而非瞬时。**
R124 冻结的 lite 元数据与 R125 core 元数据一致给出 `hasPDF=N / inEPMC=N / inPMC=N / isOpenAccess=N`；`fullTextUrlList` 只有 1 条且仅指向 DOI 解析器 `https://doi.org/10.64898/2026.06.10.731214`，**EPMC 不持有该预印本全文** ⇒ `fullTextXML` 500 不是可重试的瞬时故障。EPMC `dateOfCreation=2026-06-15` / `firstPublicationDate=2026-06-12` / `firstIndexDate=2026-06-15` 是**索引 / 首次发布日**，按 R124 教训 **≠ 当前摘要版本**。

**④ 结论（负面，必须照报）**：R124 M3 留下的「v1 页面无本地字节冻结件」缺口，在本轮穷尽的官方 per-version JATS、EPMC 全文、Wayback 存档、`api.biorxiv.org` 路由上**仍未闭合**；`v1 阳性 vs 当前口径阴性` 的版本二分**依旧无一手字节支撑**。**R3 维持 OPEN；不改写 R106 / R124 任何字节；不把取证完成包装成 gap 闭合。**

## 4. 可复算性与脚本缺陷（全部留痕，两版以上全保留）

`R125-verify.py` **不 import `R125-ACQUIRE`、不把任何 R125 产出 JSON 作实质数据源**，仅从 13 份 raw 字节 + R124 冻结的 2 份权威 API/EPMC 字节用自有解析逻辑重算：**93 检查 / 93 MATCH / 0 MISMATCH**（A 27 / B 6 / C 10 / D 24 / E 14 / F 4 / G 2 / H 6）。A 组为**同机字节恒等一致性核对，非独立交叉核验**（SHA 字面值来自另一次 `shasum -a 256` 实测，无编造）。

- **V-1（v1，脚本缺陷）**：`bytes` 不可 JSON 序列化 ⇒ 写出 `TypeError`。`R125-verify-v1.py` 原样保留，可复现。
- **V-2（v2，期望值假设错误）**：`version` 字段为字符串，v2 期望 int 列表 ⇒ `91/92 MATCH, 1 MISMATCH (E-versions)`。`R125-verify-v2.py` 原样保留，可复现。
- **v3 修正**：显式 `_jsonable()` + 按字符串比较并新增 `E-versionType` 检查 ⇒ 93/93。两处均为**脚本 / 期望值缺陷，非数据不一致、非编造**。
- 复现 v2 缺陷时会把同名 `R125-VERIFICATION.json` 覆写成 v2 的 91/92 结果；已把该输出另存 `R125-VERIFICATION-V2.json` 留痕，并**重跑 v3 复写回 93/93** 作为最终权威读数。另有一处 `metrics.csv` 生成脚本的 `Path('.').parent` 路径解析缺陷（首次运行 `FileNotFoundError`），属一次性脚本缺陷、已修正重跑，不影响任何冻结字节。
- **本轮尚未发布的 manifest 两次自查纠错**（与 R124 先例一致，仅重建本轮未发布产物，历史检查点零改动）：① 首次 artifact 过滤误用 `endswith('/manifest.json')`，把 21 份历史检查点 manifest 一并排除（70 artifacts）⇒ 改为只排除本轮自身 manifest 路径；② 修正后首版用 `while read` 读取无尾换行的清单，末行 `evidence/route-diagnosis-redacted.json` 被丢弃（91 artifacts）⇒ 补尾换行重建为 **92 artifacts**。两次 `create` 前均先删除本轮**未暂存 / 未提交 / 未推送**的自产 manifest，最终 `create` / `verify` 均通过、`input_git_head=bf08041b…` = 本地 HEAD。两处均为脚本 / 过滤口径缺陷，非数据不一致、非编造。

## 5. 时点 / 范围限定（防止夸大）

- HTTP 429 / 500 / 404 / 空 CDX **严格限定于 R125 采集时刻（2026-11-14 ~17:0x +0800）与 `R125-ACQUIRE.py` 逐条列出的 URL / 主机**。
- 429 是 **Cloudflare 1015 主机侧限流**，**不是永久不可得**：R124 同日曾从 `api.biorxiv.org` / `connect.biorxiv.org` 取得 200，且报告过一次 v1 HTML 的 200 / 105,400 B 响应（未落盘）。本轮不主张「永久不可取证」。
- Wayback CDX 查询带 `statuscode:200` 过滤、`limit=5`、单一 URL 形式 ⇒ 「零快照」仅限该查询口径，不等价于「全网无存档」。
- 13 份 raw 全部**不上传**公开仓库；仅同步脱敏摘要（见 §8）。

## 6. 双门只读复核（本轮采集时刻，字节锚定在 run root）

- validator：`NOT_QUALIFIED / overall_score=6.0 / threshold=7.0 / comparison_operator=">=" / score_meets_threshold=false`（D1✓ D2✗ D3✗ D4✓ D5✗）。读出落 `R125-VALIDATOR-READOUT.json`。
- guard：`INCOMPLETE`（A2 `pipeline-state.json 全 26` FAIL、A6 `最新一次独立 full 评审 Overall` FAIL）。读出落 `R125-GUARD-READOUT.txt`（含本机路径字面串，**不上传**）。
- 7 份结构权威采集时刻 SHA 前后逐字节一致：`goal-ledger 00ff975c…`、`validate_single_paper.py 72240260…`、`criteria 94846083…`、`guard ledger 73043b4e…`、`pipeline-state.json bcb48bb9…`、`literature-baseline-matrix.md 31b5098b…`、`source-manifest.json 541880ab…` ⇒ **零写回**。
- 主线 `pipeline-state.json`：`CCFA-startup passed`，**G0–G8 / validation / handoff 全 `pending`**，`G0.inputs=[] / G0.evidence=[]`。

## 7. 严格边界

全轮 `READONLY_VERSION_ROUTE_EXHAUSTION`：**零**模型前向 / 训练 / 标签 / 数据集 / EPE·l2 / 科学指标；**零**门晋级、**零**自我认证、**零** stage 状态改动；未改历史字节 / 评审 / 分数 / 阈值 / 稿件 / 门 / 矩阵 / registry / 门配置；未起 `ccf-paper-reviewer full`、无 `**Overall:**` 行、未自评 governing；未创建 v4、未跳门、未假定 `≤32h / K=45` 授权、无 4090 / L4 / H20 能力主张；主项目未投稿 / commit / push。D1 判别性预测维持 `BLOCKED_ON_CONFIRMATION`。

## 8. 停止门与交下轮

- **第 3 步前置（实质正向新科学证据）未满足** ⇒ 不进稿件新副本、不做 9 页编译、不起全新隔离 full 评审。**0 篇达标、未写 COMPLETE**；停止门只剩 ①达标（>= 7.0）②用户叫停；心跳 ACTIVE 调度无变化。
- **全新隔离独立审查**：`general-purpose-1` 已下发（不透露期望分 / 分数锚点 / 结论锚点），从源字节独立复算 A–H + 12 类点名夸大 + 瑕疵分级；**写本段时尚未回收、不宣称任何审查结论**；检查点写时点如实标注，回收后按 R117/R119–R124 先例另建**新的不可覆盖检查点**。门 / 证据层复核，**非** full 稿件评审。
- **交下轮**：① 回收独立审查、结论与更正只追加于新检查点；② 本轮 13 份件的归类 / 登记（是否并入矩阵 / `source-manifest.json`、版本口径如何入矩阵、W13 判据书面冻结）须 designated gate owner 依 **G1 / G4 / G6 / G7** 裁决，心跳不回写；③ 唯一 admissible 路径仍是按序 G0–G8 → validation → handoff → P0 → P1A/P1B → P2 → **P3 baseline-first 真实前向**取得实质正向新证据 → 稿件新副本 → 9 页合规编译 → 全新隔离 full 评审；`X >= 7.0` 且 QUALIFIED + COMPLETE 才写 COMPLETE；④ 决策入口 `reconciliation-R120/R120-CONSOLIDATED-DECISION-REGISTER.md`（最小集 `G1+G4+G10`）。
- **新教训**：① 官方 details API 的 `jatsxml` 是**按日期**而非按版本唯一（12 条记录 → 10 个 URL，v3/v4 与 v8/v9 撞日期）⇒ 端点侧即存在版本不可分辨对，「按版本取全文」不必然可行；② 记录级 `license` 字段 / EPMC `license = "cc by"` 仍是**元数据声明**，不等于逐资产许可文本（R123 教训再次适用）；③ `fullTextXML` 500 须先用 `hasPDF / inEPMC / hasTextMinedTerms / fullTextUrlList` 判定是**结构性无全文**还是瞬时故障，不可一律当限流重试；④ 同一摘要在不同主机的重现须分别登记「端点数」与「独立来源数」，不得因端点 +1 就升级为独立来源 +1（R124 M2 教训）；⑤ `version` 等 API 字段须先实测类型再写期望值；⑥ 字符数 / 相似度必须绑定具体派生件并声明归一口径（R122 C-1 / R124 M1 教训）。

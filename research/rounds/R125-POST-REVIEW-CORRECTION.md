# R125 独立审查回收 — 只追加更正（历史正文与独立报告原文零改动）

**独立报告**：`R125-INDEPENDENT-REVIEW.md` — 14,138 B / 94 行 / SHA-256
`15b5879315ed9c784c19dadc16b88c52365291dbe25d1a6bc2a6b2c6f482dcdf`
（mtime 17:42:59，一次写入、无中间态、原文零改动）。复核者 `general-purpose-1`
为**全新隔离子代理**，下发时不透露期望分 / 分数锚点 / 结论锚点；仅用 13 份 raw 字节
+ R124 冻结的 2 份权威件、自有解析逻辑，不 import 采集 / verifier、不把任何 R125 产出
JSON 作实质数据源、最后才读轮次审计与采集映射作待核声明；未运行 verifier / validator /
guard / git / 网络，未改任何既有文件。报告内 0 数值 `**Overall:**` 行、0 邮箱字面值、
含 1 处本机路径字面串与 2 处扫描模式名（非凭证值）⇒ 按 R117 先例**原文不上传**，
只上传脱敏摘要。

**首行**：`REPRODUCIBLE_WITH_DEFECTS | G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`。

**复核结论**：A–H 全部分组数值与审计吻合（除下述 M1 的上界）；**12 类点名夸大
CONFIRMED 0 / REFUTED 12**；瑕疵 **HIGH 0 / MEDIUM 1 / LOW 1**；**事实错误 1 /
数据不一致 1（同一处）/ 编造 0**；0 凭证值 / 0 分数行。复核者明确所有范围限制
（HTTP 状态为声明值不可重放、A 组同机同一性、未运行 verifier 故 93 检查只核类别与
自洽、工作区级计数与双门 / pipeline-state 活读数不在 13 份 raw 可核验范围）。

---

## M1 [MEDIUM｜事实错误 + 内部数据不一致] — 接受，且须说明时点

复核者 :85 指出轮次审计 `:41` 「全部 13 份 ≤ 58,714 B」为假：最大件为
`api-details-v1.json` 的 **64,741 B**（该值审计自身表格已列），58,714 B 实为
`connect-jats.xml` 的尺寸。**该判定对其所读字节为真，全盘接受。**

**时点澄清（不主张复核者判错）**：复核者在隔离会话中读取的是轮次审计的**更正前快照**；
主会话在此之前已由 `metrics.csv` 生成时的逐字节求最大值**独立发现同一错误**，并在
**本轮尚未发布的自身草稿**（轮次审计 `:41`、脱敏摘要、第二十二检查点 `CHECKPOINT.md`）
中就地更正为 64,741 B，且已在审计 `:42` 写入自查纠错留痕。第二十二检查点
`CHECKPOINT.md` 的 mtime `17:38:35` **早于**独立报告 `17:42:59`，即**已发布字节
在被复核者读取前就已是更正值**。`R125-SOURCE-MANIFEST.json` / 13 份 raw / 三版
verifier / `R125-VERIFICATION.json` / 21 个历史检查点**任何字节均未回写**。
⇒ 影响严格限于一份**本地未上传草稿**的派生汇总数字；不改变任何冻结字节、负面结论、
双门读数、门状态、governing、0 篇达标、心跳调度。按只追加纪律，本更正**不回写**
轮次审计任何字节。

## L1 [LOW｜被引校验器检查设计弱点] — 接受，并收窄引用口径

复核者 :86 / :63 指出：`R125-verify.py` 的 H 组 `noEmail` 检查
（`:203-204`）只在文件**同时**含 `@` 与 `.com` 时计数，而 `wayback-v1.html` 中
2 处邮箱形态串为 `info@archive.org`（`.org`），未被覆盖 ⇒ 该检查**不能**真正建立
「零邮箱字面量」。主会话用域无关正则独立复算（`R125-EMAIL-RECHECK.py`）：
**13 份 raw 共 2 次邮箱形态串匹配（occurrences=2），去重后 1 个唯一串
`info@archive.org`（distinct=1），全在 `wayback-v1.html`**（按 R124 L1 教训显式
声明计数口径）；冻结 verifier 的弱检查计数为 0。全盘接受。

**影响范围（严格限定）**：
- 属于**被引校验器的检查设计弱点**，非审计正文的字节级断言有误，亦非复核者复算结论
  有误；审计 `:41` 自身列明的安全断言（无本机路径 / 凭证 / 数值总分行）经复核者
  独立复算**为真**。
- 轮次审计 `:41`、脱敏摘要、第二十二检查点均**未声称**「13 份 raw 零邮箱字面量」；
  检查点 `:151` 出现 `email` 一词仅指**上传全仓** 8 类严格扫描的类别名（该扫描对
  上传集 0 命中，且已把 `archive.org` 等公共域排除）。
- 13 份 raw **全部不上传**公开仓库，`info@archive.org` 属 Internet Archive 公开
  联系地址、非本项目凭证 / 私人身份，`@` 与 `.org` 组合不进入任何上传字节。
- 冻结 verifier 三版**不回写**（保持 93/93 可复算）；另新增独立
  `R125-EMAIL-RECHECK.py` + `R125-EMAIL-RECHECK.json` 作为正确口径的可复算留痕。

## C1 [补充一手字节事实，复核者 :58] — 接受

`connect-jats.xml`（58,714 B）实为 bioRxiv **about 页 HTML**（含
`canonical http://biorxiv.org/about-biorxiv`），**不是 JATS 全文，且不含任何摘要**；
当前阴性摘要在 13 份 raw 中**仅**出现于 `epmc-core.json` 与 `api-details-v1.json`
（后者与 R124 冻结件逐字节相同）。⇒ **加强**「connect 件是重复件、不计新来源」
与「端点数 +1 ≠ 独立来源数 +1」两条结论；文件名含 `jats` 仅为采集标签，
`R125-ACQUIRE.py` 已把它登记为 `connect page / auxiliary`，不主张其为全文。

## C2 [口径补充，复核者 :38 / :90] — 接受，收窄相似度数值的引用

复核者以 `(epmc, biorxiv)` 参数顺序 + difflib 默认 `autojunk` 得 0.8997；关闭
autojunk 得 0.9945；Unicode / 连字符 / 空白归一后 0.9953–0.9978；以
`(biorxiv, epmc)` 顺序（即 `R125-verify.py` 所用）得 **0.9906**，且恰为 22 个
非 equal opcode。复核者按指示先自查解析 / 归一口径，**判为口径差异、不计数据错误**。

⇒ 接受并收窄：`0.9906` 是
`difflib.SequenceMatcher(None, biorxiv_api_abstract, epmc_core_abstract).ratio()`
（默认 `autojunk=True`、参数顺序固定）这一**具体派生口径下的值**，不是脱离口径的
「固有相似度」；不同顺序 / autojunk / 归一口径可得 0.8997–0.9978，**全部支持同一
定性结论**（两份摘要为同一文本，差异仅排版 / 空白 / 连字符 / Unicode 转写，无语义
差异）。此后引用该数值**必须同时声明参数顺序与归一口径**（R122 C-1 / R124 M1
教训再次适用）。`metrics.csv` 中 `source` 列已标 `difflib SequenceMatcher`，本更正
补充其顺序依赖，不回写已发布检查点。

## C3 [时点 / 声明值限定，复核者 :28 / :52 / :92] — 接受

- 13 份 raw 中**无**字面 `429`；`1015` 为 Cloudflare 限流体，HTTP 429 / 500 / 404 /
  200 均为 `R125-ACQUIRE.py` 的**声明状态码**（curl `-w` 实测所得，复核者无网络
  不能从字节重放）。
- `wayback-v1.html` 为 Wayback「未存档」错误页（`<title>Wayback Machine</title>`、
  `The Wayback Machine has not archived that URL.`），页面内**无**字面 `404` /
  `Not Found`；「HTTP 404」为声明状态码。verifier F 组检查的是 Wayback 页标记，
  与此一致。
- 复核者无法验证 `api-details-v1.json` / `connect-jats.xml` 是否「独立重新抓取」，
  仅能确认与 R124 冻结件逐字节相同（G 组）；亦不核验工作区级评审行计数、governing /
  validator / guard / pipeline-state 活读数、7 份结构权威 SHA、mtime 与历史沿革。
  上述均由主会话独立采集，全部接受。

---

## 效力边界

M1 / L1 / C1 / C2 / C3 **全部为措辞 / 口径 / 补充事实收窄，无一项增加主张**。
均不改变：13 份 raw 字节与 SHA、`R125-SOURCE-MANIFEST.json`、v3
**93/93 MATCH / 0 MISMATCH**、A–H 全部分组数值、12 类 REFUTED 12、双门读数
（`NOT_QUALIFIED / 6.0 / >=7.0`、`INCOMPLETE`）、门状态（G0 pending、G1–G8 全
pending、`inputs=[]`/`evidence=[]`）、governing、0 篇达标、R106 §6 收敛表、
心跳 ACTIVE 调度。轮次审计原文、独立报告原文、三版 verifier / VERIFICATION、
13 份 raw、第二十二检查点**字节全部零改动**。

门 / 证据层复核，**非** `ccf-paper-reviewer full` 稿件评审；无数值 `**Overall:**`
行、无分数字面值、不改 governing。第 3 步前置（实质正向新科学证据）仍未满足 ⇒
不进稿件 / 不编译 / 不起 full 评审。**0 篇达标、未写 COMPLETE**，governing 仍
**R95 = 6.0 / Confidence 4.0**；停止门只剩 ①达标（>= 7.0）②用户叫停。

**交下轮新增教训**：① 被引校验器的「零命中」检查须用域无关 / 形态无关的正则，
`@`+`.com` 之类的合取条件会产生静默假阴性；「零某类字面量」的声明必须绑定到
具体文件集并给出程序复算值。② 相似度数值必须绑定参数顺序 / autojunk / 归一口径，
不同口径可差 0.09。③ 第三方页面的「错误页」可能不含字面 HTTP 状态码，状态码属
声明值须单列。④ 文件名 / 标签不等于内容类型（本轮 `connect-jats.xml` 实为
about 页 HTML、无 JATS、无摘要），须以字节判定。⑤ 同一派生汇总错误被独立复核与
主会话各自发现时，须写明**读取快照的时点差**，不宣称任一方判错、不回写已发布字节。

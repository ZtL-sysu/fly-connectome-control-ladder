**Verdict:** REPRODUCIBLE_WITH_WORDING_AND_JUDGMENT_DEFECTS | **G0 may be passed:** NO | **Scientific result claimed:** NO
**Forward pass performed:** NO

# R118 独立复核报告（只读 · 从磁盘原始字节自行重算）

> 独立性声明：本人与本项目作者无关。下列全部读数均由 `<local>/miniconda3/bin/python`（标准库 hashlib/json/re/os）从磁盘原始字节现场重算，**未采信被审查报告的任何结论、数字或措辞**；我先独立完成全部计算，再回头对照被审查产物仅用于定位差异与瑕疵。零网络请求、未加载模型权重、未前向/训练/推理、未实例化 npz、未读取数据集数组、未运行任何会写回的脚本。仅新建本文件，未改动任何既有文件。本报告不是 `ccf-paper-reviewer full` 稿件评审，不含数值论文分、不含任何稿件评审置信度字段、不产生稿件评审分数行。

## 0. 范围与方法

- 复核对象：`gate-G0-R118/` 全部 13 个文件（根目录 7 + `isolated/` 6）。
- 只读交叉取证：`literature-search/`、`gate-G0-R107/`、`gate-G0-R106/`、`gate-G0-evidence-review-R98.md`、`literature-baseline-matrix.md`、`pipeline-state.json`。
- 路径均用相对路径或 `<local>/` 占位，不写本机绝对路径，不写任何凭证值。
- 字节 = `len(open(p,"rb").read())`；SHA256 = `hashlib.sha256(bytes).hexdigest()`；纯文本 = 去 script/style、去标签、HTML 反转义、空白规范化。

## 1. `gate-G0-R118/` 各产物 bytes 与 SHA256；isolated 6 份一致性

| 产物（相对 `gate-G0-R118/`） | bytes | SHA256 |
|:--|--:|:--|
| `R118-REGISTRY-GAP-EVIDENCE.md` | 9491 | `55d26732bd5486db56567428510e98e893cc52acc756deee9f77e85ccd99641e` |
| `R118-REGISTRY-GAP-VERIFICATION.json` | 19044 | `5fc9f54d8bbc1e9aaa3d72729b6b758f6120d54620127e753bbf645efbb4cb0a` |
| `R118-REGISTRY-GAP-VERIFICATION.v1-superseded.json` | 17627 | `5f44c8e401f36db4ffb83d3b207bdb1224c316fa4b5ab16b68e2a496de2857fe` |
| `R118-ROUND-AUDIT.md` | 8596 | `6af78a996371f0d7d4eb2ea032ce17e20628470204f37d92837237c56b3b6f2e` |
| `R118-SOURCE-MANIFEST.json` | 70050 | `13e211ae768160c211420a7ecb3e33a18c0f4c17757340a85634656baae9b541` |
| `R118-manifest.py` | 6717 | `ff499454adc552e8cbcdbd508b52b0638d8630dd06ab5fe4af203f9bb7319c88` |
| `R118-verify.py` | 14602 | `3b743963e79db90f25f0ed20abb79ef683bed8e04357ea54247913fab87552b6` |
| `isolated/R118-REGISTRY-GAP-EVIDENCE.md` | 9491 | `55d26732bd5486db56567428510e98e893cc52acc756deee9f77e85ccd99641e` |
| `isolated/R118-REGISTRY-GAP-VERIFICATION.json` | 19044 | `5fc9f54d8bbc1e9aaa3d72729b6b758f6120d54620127e753bbf645efbb4cb0a` |
| `isolated/R118-ROUND-AUDIT.md` | 8596 | `6af78a996371f0d7d4eb2ea032ce17e20628470204f37d92837237c56b3b6f2e` |
| `isolated/R118-SOURCE-MANIFEST.json` | 70050 | `13e211ae768160c211420a7ecb3e33a18c0f4c17757340a85634656baae9b541` |
| `isolated/R118-manifest.py` | 6717 | `ff499454adc552e8cbcdbd508b52b0638d8630dd06ab5fe4af203f9bb7319c88` |
| `isolated/R118-verify.py` | 14602 | `3b743963e79db90f25f0ed20abb79ef683bed8e04357ea54247913fab87552b6` |

- 文件总数 **13**（根 7 + isolated 6）。
- `isolated/` 6 份副本与根目录同名文件：**bytes 相同、SHA256 相同、原始字节逐字节 `==` 全部为 True（6/6 一致）**。
- 根目录独有、isolated 无对应：`R118-REGISTRY-GAP-VERIFICATION.v1-superseded.json`（v1 留痕，见 §9(i)）。

## 2. `literature-search/source-manifest.json` 与 5 条声明

- bytes **1124**，SHA256 `541880ab1d6a287a7dbd566034a49212858973763fc943eb00d2a1b92de0357b`，条目数 **5**（顶层 JSON list），**不含** `2609.24565`（原始文本逐字检索为 False）。
- 5 条声明（name / url / bytes / sha256 / access_date）对应磁盘 `<name>.html`，独立重算 bytes+SHA：

| name | 声明 bytes | 磁盘 bytes | bytes 吻合 | 声明 SHA256（前 12） | 磁盘 SHA256 吻合 |
|:--|--:|--:|:--:|:--|:--:|
| toposens2026 | 215470 | 215470 | ✓ | `85ddec17c98d` | ✓ |
| boundary2026 | 304810 | 304810 | ✓ | `b13802566242` | ✓ |
| flyhack2026 | 346042 | 346042 | ✓ | `f98ec7c77e42` | ✓ |
| structure2026 | 207365 | 207365 | ✓ | `33c5d1a01ec1` | ✓ |
| flyvis2024 | 21444 | 21444 | ✓ | `ec7eb823535a` | ✓ |

- **5/5 bytes + 5/5 SHA256 全部吻合（10/10）**。注：5 个同名 `.txt` 是派生的纯文本，bytes/SHA 与声明不同，声明显然指向 `.html`，比对成立。第 5 条 `flyvis2024.html` 虽 SHA 完整，内容却是挑战页（见 §7）——SHA 完整 ≠ 内容有效。

## 3. `literature-search/` 文件总数与后缀候选：我自己重算的分类

- 递归（`os.walk`）文件总数 **167**；仅顶层为 **19**。后缀全量分布：`.py 46 / .png 37 / .npz 19 / .json 17 / .html 11 / .ipynb 8 / .md 8 / .txt 8 / .npy 5 / .xml 4 / .pdf 3 / .zip 1`（合计 167）。
- 按「后缀 ∈ {.html, .xml, .pdf, .txt}」筛出的候选数 **26** = `.html 11 + .xml 4 + .pdf 3 + .txt 8`；其余 **141** 为项目自有产物（167 − 26 = 141）。
- **以下为我自己的独立分类（不采用被审查产物的 13/7/3/3 内容特征分类）**：
  - 按目录：顶层 12 / `response-null-sources/` 7 / `task-projection-sources/` 7 = 26。
  - 按性质我判读：5 个顶层注册页 `.html`（其中 `flyvis2024.html` 经我验证为 CAPTCHA 挑战页）；8 个 `.txt` 为派生纯文本；6 个双后缀下载件（`.html.html` / `.html.txt` / `.pdf.pdf`）；3 个 `.pdf` 未做文本抽取；4 个 `.xml`（EuropePMC 正文/元数据）。
  - 26 只是后缀计数，其中混有派生文本、挑战页、双后缀副本与未抽取 PDF，**不等于 26 份已核验一手来源**。

## 4. `gate-G0-R107/sources/` 5 份 `kuklev_*` SHA256 与 R107 manifest 吻合

| 文件 | bytes | SHA256 |
|:--|--:|:--|
| `kuklev_abs_latest.html` | 43642 | `c3d4fa3d0e1b289e29ad2c67a337602f2865da86949d99a47960b873df9d80ed` |
| `kuklev_abs_v1.html` | 41581 | `0075412eb10447864bb2b139c6d8ec8eb1c8f256b2d91e69a913203027bbd367` |
| `kuklev_abs_v2.html` | 43656 | `cbcbce7343f999ebae1f63c43963a477e96ebe827679b6f973e25e177ca7029e` |
| `kuklev_html_v1.html` | 50485 | `2726ef63d6cda79393d1faa725267cb1ede474f1189caba51cc583c9a4af648c` |
| `kuklev_html_v2.html` | 182710 | `f4e7fb8747165a4f4caf0a50e34ca15f7a837536699189bffe267502ca12e7ad` |

- `R107-ONEHAND-SOURCE-MANIFEST.json`（6342 B，`2c32b4c0dc5e2d5de45d16c221dc4120def672ba5ebd5af9a8567d2150590e47`）中 5 条 `sources/kuklev_*` 声明的 SHA256 与我重算值 **5/5 逐一吻合**。该 manifest 的 `generated_at` 为 2026-11-13，note 写明「All SHA256 computed from raw bytes by `<local>/miniconda3/bin/python`」——这是 R118 之前已有的字节级复算产物（§9(b) 依据）。

## 5. Kuklev 三份 abs 摘要逐字比较 + 正文 Abstract 块

从 `blockquote.abstract` 抽取、去 descriptor、空白规范化后的纯摘要：

| 来源 | 纯摘要字符数 | 被审查产物口径 | 逐字相等关系 |
|:--|--:|--:|:--|
| `kuklev_abs_latest.html` | **1534** | 1544（含 `Abstract: ` 前缀） | latest == v2 |
| `kuklev_abs_v2.html` | **1534** | 1544（含 `Abstract: ` 前缀） | latest == v2 |
| `kuklev_abs_v1.html` | **1433** | 1443（含 `Abstract: ` 前缀） | 与 latest/v2 **不同** |

- 逐字比较：`latest == v2` 为 True；`latest == v1` 为 False；`v2 == v1` 为 False。
- **真收束句（各自最后一句，逐字）**：
  - latest / v2：`Thus active sampling and exact structure matter, while clean-data practical performance remains dominated by task-trained networks and the useful transfer margin is largely retinal.`
  - v1：`The supported claim is therefore narrow: motion-oriented biological vision can be repurposed as a useful texture representation for architectural hatch matching, while the topology contribution and end-to-end BIM utility remain open questions.`
- `kuklev_html_v2.html` 正文 Abstract 块：核心段 **1943** 字符（不含 `Abstract. ` 前缀、不含 `Keywords.` 尾；含前缀+关键词的完整块为 2069）。收束句 `Exact structure remains insufficient to beat what the moving retina already provides.` 开头为 `A connectome-constrained model ... driven over a drawing by prescribed motion ... We test what that buys on architectural documents ...`。
- **结论：正文 Abstract 与 abs 页摘要不同（逐字不等）**——措辞（`a drawing` vs `architectural drawings`）、新增句子、结论句均不同；`V2-two-abstracts-distinct` 判定成立。
- 口径说明：被审查产物的 1544/1443 = 我算的 1534/1433 各 + 10（descriptor `Abstract: ` 被空格替换后计入）；正文 1943 = 去前缀去关键词后的核心段。三者是**不同口径**，详见 §11 瑕疵 3。

## 6. `kuklev_html_v2.html` 正文 10 条短语逐字查找（FOUND / ABSENT）

我对同一文件给出两个口径（这本身是 §11 瑕疵 2 的依据）：A = 磁盘原始字节/解码 HTML 源码的精确子串；B = 去标签重建的正文纯文本精确子串。

| # | 逐字短语 | A 原始字节 | B 正文纯文本 |
|--:|:--|:--:|:--:|
| 1 | `What the sampling sweep answered` | FOUND (×2) | FOUND |
| 2 | `That prediction was run, and it half held.` | FOUND | FOUND |
| 3 | `Two gaps remain.` | FOUND | FOUND |
| 4 | `which stage integrates the extra time` | FOUND | FOUND |
| 5 | `per-type tuning analysis over the sweep` | FOUND | FOUND |
| 6 | `+ 0.033` | **ABSENT** | FOUND (×2) |
| 7 | `[ 0.015 , 0.050 ]` | **ABSENT** | FOUND (×2) |
| 8 | `T4/T5 contribution does not grow with length` | FOUND | FOUND |
| 9 | `7.3 The stimulus never completes a cycle` | **ABSENT** | FOUND (×2) |
| 10 | `9 Limitations` | **ABSENT** | FOUND (×2) |

- **正文口径（B）：10/10 FOUND**；**原始字节口径（A）：6 FOUND / 4 ABSENT**。
- 4 个 ABSENT 的字节级原因：它们在 HTML 中被标签/实体分隔——`+ 0.033` 与 `[ 0.015 , 0.050 ]` 来自 MathML（`<mo>+</mo><mn>0.033</mn>`、`alttext="[0.033,0.072]"`、annotation `[0.015,0.050]`），去标签后拼成带空格形式；`7.3 ...` 的编号被 `</span>` 标签或特殊空格（U+2002/U+2006）与标题分隔；`9 Limitations` 同理。它们真实存在于论文正文，但**不以该逐字形式存在于原始字节**。

## 7. `flyvis2024.html` 纯文本、`literature-baseline-matrix.md`

- `literature-search/flyvis2024.html`：21444 B，SHA256 `ec7eb823535a7097be40be17babc023d294c35dae1a5044b201dd775b21ce615`，与 registry 声明吻合。纯文本 **165 字符**，逐字为：`Checking your browser - reCAPTCHA Checking your browser before accessing pmc.ncbi.nlm.nih.gov ... Click here if you are not automatically redirected after 5 seconds.`
- **是 CAPTCHA / 浏览器挑战页**（含 `Checking your browser` / `reCAPTCHA` / `pmc.ncbi.nlm.nih.gov`，无 Abstract、无正文）。`flyvis2024.txt`（17774 B）亦含 `RecaptchaChallengePageUi`。R98（3742 B，`6bccf27dcb75dab8d45c37a80bd56724583ffc4e6d3859b7ef81b9b2bafd8ea9`）L21 原文为 "23 saved public sources"，且只写明排除 `flyvis2024.txt` CAPTCHA 响应。
- `literature-baseline-matrix.md`：9445 B，SHA256 `31b5098b4df2718ddf15d0b4613daa4d819a19319bbc15b731fb58d3903da9b2`；**仍含** `the open question`（第 46 行）与 `Kuklev leaves`（第 47 行）。与 `gate-G0-R106/R106-G0-EVIDENCE-FREEZE.json`、`gate-G0-R107/R107-END-OF-ROUND-FREEZE.json` 记录的 9445 B / 同 SHA 一致 ⇒ 未见回写。

## 8. 主线 `pipeline-state.json` 与门状态

- bytes **3723**，SHA256 `bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d`（sha16 `bcb48bb964e657a4`）。
- `stages` 状态：`CCFA-startup` = `passed`；**G0、G1、G2、G3、G4、G5、G6、G7、G8、validation、handoff 全部 `status: pending` / `gate_verdict: pending`**（11 个 stage 无一 passed），`inputs`/`evidence` 均为空。G0 未晋级，矩阵未定稿，gap 2 仍 OPEN。

## 9. 「夸大与自我认证」清单 (a)–(l) 独立判定

下列 12 项均为我对磁盘字节与历史产物**独立取证后**的判定，并非采信被审查产物的自述；结论是 12 项**全部 REFUTED**（未出现对应夸大）。这份产物是一份防夸大纪律很强的清点报告，夸大清单全灭是复核结果，而非轻信其自我否认。

- **(a) 说成 G0 通过 / 门晋级 → REFUTED**。`pipeline-state.json` 字节显示 G0–G8/validation/handoff 全 `pending`（§8），仅既有的 CCFA-startup 为 passed；各产物 `boundary` 字段为 `READONLY_REGISTRY_GAP_AUDIT_NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT`，`explicitly_not_claimed` 含 "G0 passed"、"any stage status changed"；ROUND-AUDIT §7「G0 维持 pending / 未写 COMPLETE」。
- **(b) 说成「首次」复算 Kuklev 字节 → REFUTED**。产物明确写「本轮不是首次复算」「不称首次」。独立查 `gate-G0-R107/`：`R107-ONEHAND-SOURCE-MANIFEST.json`（2026-11-13）已含 5 份 `kuklev_*` 的 SHA256 且 note 标注「from raw bytes」；`R107-END-OF-ROUND-FREEZE.json`、`R107-INDEPENDENT-REVIEW-RECOVERY.md` L76「我从已冻结的 `sources/kuklev_html_v2.html` 原始字节独立抽取」——均早于 R118（2026-11-14）。历史事实独立证实"非首次"。
- **(c) 把 26 候选当成 26 份已核验一手来源 → REFUTED**。产物多处写「26 是后缀筛选候选，不等于 26 份已核验一手来源」，`verify.py` L133 note「candidate ... NOT equal to verified first-hand sources」。我独立重算 26 = 11+4+3+8，其中含 8 派生 `.txt`、6 双后缀、3 未抽取 PDF、1 挑战页（§3），确实不能等同。
- **(d) 把 SHA 完整当内容有效 → REFUTED**。产物标题「字节完整 ≠ 内容有效」，并主动给出反例：`flyvis2024.html` SHA 与 registry 吻合却是 165 字符 CAPTCHA 挑战页（§7）；`verify.py` 有 5 项 `content_probe`（result=PROBED），note「sha-integrity is separate from content validity」；`REG-5-flyvis2024-content-validity` 观测 `CHALLENGE_PAGE`。
- **(e) 两份脚本一致性当成独立交叉核验 → REFUTED**。产物明确写「两份脚本同机、同 hashlib、同数据源，一致只是必然的一致性核对，不构成独立交叉核验」；`verify.py` docstring「consistency check, NOT an independent cross-validation」；JSON `independence_note` 同。我独立读两脚本：`R118-manifest.py` 与 `R118-verify.py` 都用 `hashlib.sha256`、都以 `RUN=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` 同机定位、都读 `literature-search/` 与 `gate-G0-R107/sources/` 同一批字节；verify.py 不读 manifest 产物（独立代码路径）但同源。报告把它降级为一致性核对，未冒充独立交叉核验。
- **(f) 声称 registry 已登记 Kuklev / 矩阵已定稿 / `source-manifest.json` 已写入 → REFUTED**。我独立算 `source-manifest.json` 仍 1124 B / 5 条 / 无 `2609.24565`（Kuklev 未登记），`literature-baseline-matrix.md` 9445 B 仍含 stale 表述（未定稿，§7–§8）；两者 SHA 与 R106/R107 冻结件记录逐字一致。`explicitly_not_claimed` 含 "source-manifest.json written"、"matrix finalized"。
- **(g) 声称科学结果 / 新独立 full 评审 / 稿件评审分数行 → REFUTED**。全 13 产物：稿件评审置信度类字段 0 命中；`ccf-paper-reviewer full` 4 处均「未起 …」否定引用；以 `Overall` 开头的分数行标记 4 处均「未产生 … 行」否定引用，无独立成行的分数行、无数值论文分。`explicitly_not_claimed` 含 "new scientific result"、"independent full review"、"Overall score line"。ROUND-AUDIT §8 把独立审查标为「待回收后只追加」（委托/未完成），未自称已完成新 full 评审。
- **(h) R98「23 saved public sources」已证实或已证伪 → REFUTED**。R98 原文确有该句（§7）。产物明确「不宣称 23 被证实或被证伪」，只做分解登记；`verify.py` 的 `R98-23-vs-registry` note「quantified, NOT resolved」。我独立重算当前 167（递归）/19（顶层）/26（候选）/5（registry）/13（页分类）无一等于 23，且无 R98 时刻磁盘快照可复现，故证实或证伪均不可达——报告"不宣称"恰当。
- **(i) v1 假阴性说成数据不一致，或隐藏/删除 v1 留痕 → REFUTED**。产物明确写「是主会话脚本判定缺陷，**不是数据不一致**」。我独立确认 `R118-REGISTRY-GAP-VERIFICATION.v1-superseded.json` 存在（17627 B / `5f44c8e401f36db4ffb83d3b207bdb1224c316fa4b5ab16b68e2a496de2857fe`，total_checks=45 / mismatch=0），与 v2（19044 B / total_checks=50）两版读数都保留，v1 未被删除或覆盖；isolated 6 副本亦一致。
- **(j) 声称已获得 `≤32h / K=45` confirmation 授权 → REFUTED**。产物写「未假定 `≤32h / K=45` confirmation 授权」，`explicitly_not_claimed` 含 "confirmation authorization"。全产物中 `32h`/`K=45`/`confirmation` 仅出现在该否定句与「未声称」列表。
- **(k) 声称使用 4090 / L4 / H20 GPU 能力 → REFUTED**。产物写「无 4090/L4/H20 能力主张」。EXEC LOCK 零前向/零推理/零训练；我本次复核亦未加载权重、未实例化 npz、未前向。全产物中 `4090/L4/H20` 仅出现在上述否定句。
- **(l) 声称改了任何历史字节、评审、分数、阈值、稿件、门状态 → REFUTED**。两份脚本的写操作仅 `open(OUT/…, "w")` 指向本轮新产物（`R118-SOURCE-MANIFEST.json` / `R118-REGISTRY-GAP-VERIFICATION.json`），从不以写模式打开任何既有文件。独立字节交叉验证：`source-manifest.json`（`541880ab…`）、`literature-baseline-matrix.md`（`31b5098b…`）、`pipeline-state.json`（`bcb48bb9…`）、`gate-G0-evidence-review-R98.md`（`6bccf27d…`）当前 SHA 与 R106/R107 冻结件及 `R118-SOURCE-MANIFEST.json` 的 `reference_claims` 记录一致，未见回写证据。局限：我没有全项目「改动前」快照，此结论限于可交叉验证的关键历史文件与脚本写路径。

## 10. 凭证 / 敏感信息 / 绝对路径 检查（本轮 13 个产物）

- 凭证值类命中（逐类均为 **0**）：邮箱 `0`、私钥块 `0`、OpenAI 式 `sk-` key `0`、GitHub token `0`、AWS AKIA `0`、Slack token `0`、Bearer 值 `0`、`key/secret/password/token` 赋值式 `0`。
- 本机绝对路径命中 **0**。`/Users/` 字样共 4 处，其中 **2 处为脱敏占位** `/Users/<local>/…`（符合红线）、**2 处为脚本内正则字面量**（`LOCALPATH_PATTERN`），均非真实本机路径。注：`gate-G0-R107/` 历史 manifest 的 note 含真实绝对路径，但那是历史产物、非本轮产物，且本复算不写出其值。
- 词面提示：`R118-verify.py` 中 `secret`/`credential` 字样是扫描器正则模式名（`SECRET_PATTERNS`），非凭证值，故不计命中。
- 禁用标记：稿件评审置信度类字段字样 **0** 命中；稿件评审分数行标记与 `ccf-paper-reviewer full` 各 4 处，全部为「未产生 / 未起 …」的否定引用，不构成产物。

## 11. 瑕疵清单（编号 + 严重度）

> 以下均为我在独立重算中发现、并定位到具体字节/字段的差异；我不替对方修改任何文件，仅登记。核心清点数字（167 / 26 / 5 / 21 / 141 / 10-10 / 5-5 / 50 项 0 mismatch、flyvis2024 挑战页、matrix/pipeline-state SHA 与状态）全部可复现且吻合，瑕疵集中在措辞与字段判定。

1. **[中] 「收束句」字段取错句子且三行口径不统一**。§4 表格把 `Longer observations reverse the circuit-receptor ordering once the stimulus spans a period, but not through T4/T5.` 标为 latest/v2 的「收束句（逐字）」，但这是我抽取的 1534 字符摘要的**倒数第二句**；真末句是 `Thus active sampling … largely retinal.`。v1 行给的是末句的后半从句（非完整末句），正文行给的是完整末句。源头在 `verify.py` 的 `V2-abs-metadata-closing` 检查（用 `Longer observations…` 前缀命名 closing）。字段定性错误。
2. **[中] 「全部命中冻结原始字节」措辞不成立**。§4 L55 及 JSON 中 12 个 `verbatim_field` 的 note「searched in frozen raw bytes only」与实际不符：在 182710 B 原始字节上，`+ 0.033`、`[ 0.015 , 0.050 ]`、`7.3 The stimulus never completes a cycle`、`9 Limitations` 4 个带空格串为 ABSENT（§6 口径 A），它们只在 `verify.py` 的 `text_of()` 去标签重建文本 `t_body` 里 FOUND。准确说法应为「命中重建纯文本」，而非「命中原始字节」。
3. **[中] 摘要长度三种口径混用却并列于同一表**。1544/1443 含 `Abstract: ` descriptor 前缀（我算纯摘要 1534/1433，差 10）；正文 1943 不含 `Abstract. ` 前缀、且去掉 `Keywords.` 尾（完整块 2069）。同表三种口径未标注，易被误读为彼此可比的数字。
4. **[低] flyvis2024.html「逐字」引用被截断**。§3 称纯文本「逐字为 `Checking your browser - reCAPTCHA … pmc.ncbi.nlm.nih.gov ...`」，用 `...` 省略了真实存在的后半句 `Click here if you are not automatically redirected after 5 seconds.`。165 字符数正确，但「逐字」引用不完整。
5. **[低] 候选分类两套口径未显式区分**。§2 的 13/7/3/3 是脚本按文本特征的内容启发式分类（`verify.py` L108–127），与我自己重算的后缀/目录分类（§3）是不同口径；报告未点明「后缀候选计数」与「脚本内容分类计数」是两件事，读者易把 13 当成另一组"已核验来源数"。
6. **[低] 「全新一手发现」自我定性措辞偏满**。R98 L21 已记载 `flyvis2024.txt` CAPTCHA 并排除，R118 的增量只是发现「被登记的 `.html` 同为挑战页却未被排除」。报告 §3 虽有防夸大段落，但「本轮全新一手发现」仍带首次/发现色彩，宜改述为「本轮增量观察」。
7. **[低] 「双门实跑 / 写 /tmp」与「纯只读零回写」存在口径张力且不可复算**。ROUND-AUDIT §4、EVIDENCE §6 声称实跑 validator/guard 并写 `/tmp/r118_validator.json`、`/tmp/r118_guard_report.md`。这些是项目外 /tmp 产物，且该动作无法从 `gate-G0-R118/` 目录字节独立验证；与全轮「零回写 / 纯只读」的定性略有张力。我遵守约束未重跑这些门。「零回写」更精确应限定为「对项目既有字节零回写」。
8. **[低] 「50 项 MISMATCH 0」易被读成全绿**。5 项 `PROBED` 是内容有效性探针，其中 `REG-5-flyvis2024-content-validity` 观测为 `CHALLENGE_PAGE`（与「5 条中仅 4 条内容可用」同一事实），但因被标为 PROBED 而不计入 mismatch。「0 mismatch」是脚本自定判定口径，不等于「所有检查无异常」。
9. **[低] R98「23」措辞轻微自相张力**。§1/§2 说「R98 的 23 与任何单一口径都不相等……从未给出可复算分解」，这本身已是对 23 的否定性判定，与紧随的「不宣称证实或证伪」略有张力（未构成 (h) 的夸大，但宜改为「本轮未找到能复现 23 的单一口径，故不作证实/证伪」）。

无 [高] 级瑕疵：未发现核心数字造假、未发现 12 项夸大中任何一项被坐实、未发现任何既有文件被改动。

## 12. 交付声明

本报告为最终交付；除新建本文件 `gate-G0-R118/R118-INDEPENDENT-REVIEW.md` 外，未修改任何既有文件（报告、JSON、脚本、账本、state、评审、分数、阈值、稿件、门状态均未改动），未运行任何写回脚本，未发起网络请求、未加载权重、未前向/训练/推理、未实例化 npz、未读取数据集数组。

**Verdict:** REPRODUCIBLE_WITH_DEFECTS | **G0 may be passed:** NO | **Scientific result claimed:** NO
**Forward pass performed:** NO

# R119 独立复核报告（全新隔离子代理）

本报告由未参与本轮任何产物撰写、与作者会话隔离的子代理独立产出。复核对象为 `review-protocol-R119/` 下的只读清点产物（`R119-REVIEW-LAUNCH-PROTOCOL-EVIDENCE.md`、`R119-REVIEW-LAUNCH-PROTOCOL-RAW.json`、`R119-REVIEW-LAUNCH-PROTOCOL-VERIFICATION.json`、`R119-SOURCE-MANIFEST.json`、`R119-ROUND-AUDIT.md`、`R119-raw.py` / `R119-verify.py` / `R119-manifest.py`、`isolated/`）。本轮性质是「成功标准唯一动作（未来启动全新隔离 full 稿件评审）的启动协议链」只读一致性清点，不是科学实验、不是门晋级、不是稿件评审。

## 0. 方法、口径与边界

- **独立复算来源**：A–K 的全部读数均由我直接从源字节计算（`hashlib.sha256(read_bytes())`、逐行精确子串、逐行号统计、文件存在性、`os.walk` 文件名枚举、JSON 解析），**未以 R119 的 RAW/VERIFICATION/SOURCE-MANIFEST JSON 作为计算依据**。这些 JSON 只在第 2 节被当作「被测产物的声称文本」来审读，不参与我的取数。
- 本机解释器为 `<local>/miniconda3/bin/python`（仅陈述工具，不作为评分标准）。全部操作为 `read` / `find` / `grep` / 内存计算，**未联网**。
- **路径脱敏**：本报告不写出任何本机绝对路径；如需引用一律用 `<local>/` 代替，其余一律用项目相对路径或 `~/.claude/...`（波浪号路径，非绝对路径）。被测产物中出现的阈值/历史分数数字，仅作为「被测文件中出现的字符串」如实转录，不作为评分标准，也不构成对任何稿件的打分。
- **一致性的含义**：下文 MATCH/MISMATCH 指「我从源字节复算的读数」与「被测产物 F1–F17 / §3 / §6 / 36 项 VERIFICATION checks 中的对应声称」是否一致。全部 A–L 的事实读数均为 MATCH；但我在措辞、口径、范围、时序、脱敏一致性上发现若干瑕疵（第 3 节），故 verdict 取 `REPRODUCIBLE_WITH_DEFECTS`。
- **「夸大」判定口径（先行声明，避免歧义）**：第 2 节 12 项中，`CONFIRMED` = 该过度声称在本轮产物中**确实出现**（属应被指出的缺陷）；`REFUTED` = 该过度声称**未出现 / 已被产物明确否认**，且我的实测亦不支持该声称。按此口径 12 项全部 `REFUTED`，`CONFIRMED` 计数为 **0**。若改用「不夸大断言被实测证实 = CONFIRMED」的反向口径，则对应为 12/12 通过；两种口径下结论同为「产物未作任何点名夸大」，本文采用前一种并逐条给出事实依据，故不依赖极性约定。

---

## 1. A–L 逐项独立复算

### A. `independent-review-brief*` 文件数量、字节、SHA、首行标题

- 以文件名**前缀** `independent-review-brief*` 枚举全项目：命中 **1** 份，路径 `papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2/protocols/independent-review-brief.md`。
- 字节 **4803 B**；SHA256 `8771dea80cf7a54d0208d689e8d8fba285be87d98a364b9c590dd14d3e2e3f10`（SHA16 `8771dea80cf7a54d`）。
- 首行（第 1 行）：`# P9 Independent Full Review — Frozen Brief (Contract v2, R51)`。
- 另有补充事实：全项目文件名含子串 `independent-review-brief` 的共 **2** 份，第 2 份为 `papers/paper-null-ladder/R49-7.5-DELIVERY/provenance/R95-independent-review-brief-FROZEN.md`（见 J）。产物 F1 的「1」是按 `independent-review-brief*` 前缀 glob 口径成立；按子串口径则为 2。产物在 F16 已把第 2 份单列为「另一份文件」，二者不矛盾，但口径需显式声明（见瑕疵 L1）。
- **与 F1/F2、C01 一致性：MATCH**（4803 B / `8771dea8…` / `(Contract v2, R51)`）。

### B. brief 中 9 个字面串的行号（逐行精确子串）

| 字面串 | 命中行 | 存在 |
|:--|:--|:--|
| `(Contract v2, R51)` | 1 | 是 |
| `qualification requires **X > 8.0**` | 17 | 是 |
| `(exactly 8.0 does not qualify)` | 18 | 是 |
| `If X <= 8.0, the correction loop continues` | 85 | 是 |
| `score_gt_threshold = true` | 81 | 是 |
| `independent-review-20261108.md` | 76 | 是 |
| `8 pages of main content` | 46 | 是 |
| `You are not told what score would be considered a success` | 65 | 是 |
| `Do not use any number quoted in this brief` | 35 | 是 |

- 9/9 全部存在，行号与产物 C06–C13、A2–A10 完全一致。**与 F2–F6 / F13 一致性：MATCH**。

### C. 交接块（第 21–66 行）与全文的口径区分

- **交接块口径**（第 21–66 行，含 `## Reviewer instructions (verbatim handoff text)` 标题及其下引用块）：含 `8.0` = **0 命中**，含 `7.0` = **0 命中**。该块内第 65 行含 `You are not told what score would be considered a success`、第 35–36 行含 `Do not use any number quoted in this brief as a score anchor`。
- **全文口径**（整份 86 行）：`8.0` 共 **3 处**，分别在第 **17、18、85** 行（第 16–18 行的 qualification 子句，以及第 78–86 行 post-review machine gate），均**位于交接块之外**；`7.0` 全文 **0 命中**。
- **preamble（第 9–11 行，交接块之外）**：第 10 行含历史分数 `8.2`，第 11 行含历史分数 `6.5`。
- 这是本轮「锚点不外泄」结论的关键口径：产物 F13 说的是「逐字交接块」无阈值，而非「整份 brief 无阈值」；整份 brief 确有 3 处 `8.0`。产物在 F4/F14、ROUND-AUDIT §3、账本 R119 条目中均已按「preamble / post-review gate」定位，口径自洽。
- **与 F13/F14、C26–C29、A26b/A26c 一致性：MATCH**。

### D. `GOAL-ITERATION-R107.md` 第 90–92 行

- 第 90 行：`` `guidance-v2.md`, `execution-contract-v1/v2/v3.md`, `protocols/` — frozen `` → `protocols/` 被列为冻结契约：**是**。
- 第 91 行：`contracts; a future versioned contract (v4) may restate the new criterion, but` → 提到 v4 版本化契约：**是**。
- 第 92 行：`no existing contract is retroactively edited.` → 「不回溯改既有契约」：**是**。
- 补充：第 22/25/37 行含 `>= 7.0`、`g >= 7.0`；第 54 行含 `9 pages, p8 complete Conclusion, p9 only LLM placeholder + ...`（支撑 F6 的「9 页合规编译」对照）；第 65 行含 `**new** full independent review`。
- **与 F7、C14–C17 一致性：MATCH**（保留该 brief 不变是 R107 明示的「故意冻结」，非漏改）。

### E. 全项目是否存在 R107/v4 版本化启动 brief

- 以「文件名（basename）含 `brief` 且含 `v4`/`r107`/`r11`」枚举全项目：**0 份**。
- 全项目 6 个 brief-named basename 为：`independent-review-brief.md`、`R95-independent-review-brief-FROZEN.md`、`paper-7.5-brief-zh.md`、`paper-brief-zh.md`、`brief.md`（`isolated/` 内，本轮新建的字节副本）、`brief-to-platform-ai-v2.md`；其中无一带 v4/r107/r11。
- 注意：若对**完整路径**做 `r11` 子串匹配，会把目录名 `.../review-protocol-R119/isolated/brief.md` 误命中（`R119` 含 `R11`），属假阳性；按 basename 口径为 0。产物 A26d/C32 记 0，口径正确。
- **与 F8、C32、A26d 一致性：MATCH**。

### F. 技能路径

- brief 第 30 行引用的 `~/.claude/skills/ccf-paper-reviewer/references/review-output-standards.md`：**不存在**（`exists=false`）。
- 真实文件 `~/.claude/skills/ccf-common/references/review-output-standards.md`：**存在**，**3364 B**，SHA16 `37612fb43b6ac603`。
- `~/.claude/skills/ccf-paper-reviewer/SKILL.md` 自身引用 `../ccf-common/references/review-output-standards.md` 的行号：**27、40、90**（第 10、17 行另引用同目录下的 `handoff-modes.md` / `task-modes.md` 等，非本文件）。
- F12 的其余 3 条 brief 引用路径 `SKILL.md`、`references/calibration-and-rank.md`、`ccf-paper-writer/references/venue-guides/`（目录）：**均存在**。
- **与 F11/F12、C20/C22–C25、A21/A22 一致性：MATCH**。

### G. `readonly-validator/validate_single_paper.py`

| 字面串 | 行号 | 说明 |
|:--|:--|:--|
| `default=7.0` | 133 | `ap.add_argument("--threshold", type=float, default=7.0)` |
| `"score_meets_threshold"` | 155 | 新增字段 |
| `"comparison_operator": ">="` | 156 | 比较算符 |
| `score_gt_threshold` | 153、154 | **仍保留**：第 153 行为字段、第 154 行注释 `R107: backward-compatible field name; value now uses >= (equality qualifies)` |

- 即 `score_gt_threshold` 未缺失、语义已为 `>=`（`score is not None and score >= args.threshold`）；差异仅在成文口径，不是可执行检查失败。
- **与 F9、C18/C19/C21、A16–A18 一致性：MATCH**。

### H. guard criteria/ledger 的 A6 text 双口径

- `guard/criteria-null-ladder.json` 第 132 行 A6 `text`：`最新一次独立 full 评审的 Overall >= 7.0（R107；等于 7.0 算达标；主会话自评不算）` → 含 `>= 7.0`：**是**。
- `guard/ledger-null-ladder.json` 第 134 行 A6 `text`：`最新一次独立 full 评审的 Overall 严格 > 8.0（等于 8.0 不算；主会话自评不算）` → 含 `严格 > 8.0`：**是**。
- 范围澄清：基础 `guard/criteria.json` / `guard/ledger.json` **无 A6 条目**（旧「≥5 篇 portfolio」目标的历史件，R107 第 85–89 行已说明其 `8.0` 为历史事实）。双口径**仅存在于 `-null-ladder` 一对文件**；产物 RAW.json / SOURCE-MANIFEST.json 用的正是这两个精确文件名，但 EVIDENCE.md F10 表内只写「criteria / ledger」（见瑕疵 L2）。
- **与 F10、C34/C35、A19/A20 一致性：MATCH**。

### I. R58 / R60 是否读过 brief，以及 R60 的「仅背景、不作锚点」登记

- `ccfa-review-reports/paper-null-ladder-r58-independent-review-20261108.md` 第 15 行（non-anchoring 声明）与第 38 行均明写读过 `protocols/independent-review-brief.md`；第 433 行「历史分数 / 验收阈值未作为锚点、未照抄、未进入评分推理」。
- `ccfa-review-reports/paper-null-ladder-r60-independent-review-20261108.md` 第 28 行明写该 brief「含一个数字化的 qualification gate 以及历史分数记述」，并按「never to import a score」处理；第 372 行「未采用运行根内冻结交接简报中的数字化门槛（**该简报按背景数据处理**）」；第 433 行「未锚定历史分数或冻结简报门槛」。
- 即两份历史独立评审都读过全文，但把其中数值门槛登记为**仅背景、不作锚点**。
- **与 F15、C30/C31、A23/A24 一致性：MATCH**。

### J. R95 FROZEN brief 与 R51 brief 是否同一份、是否含字面 `8.0`

- `papers/paper-null-ladder/R49-7.5-DELIVERY/provenance/R95-independent-review-brief-FROZEN.md`：**5275 B**，SHA256 `0d42d1d9d4f37aadaffdfc1af57ebbc99456330bbc70ec689828cf0cd9201855`（SHA16 `0d42d1d9d4f37aad`），共 93 行。
- 含字面 `8.0`：**否**（0 命中）；含字面 `7.0`：**否**（0 命中）。
- 与 R51 protocols brief **不是同一份**：字节 5275≠4803、SHA 全不同、`bytes==` 为 `False`；首行 `# R95 Independent Full Review — Frozen Brief (Contract v2, R51)`（注意：其标题**同样**带 `(Contract v2, R51)`，但字节内容不同）。
- 产物 F16 的表述「R95 不是从 R51 protocols brief 启动」按「特指 protocols/ 下那份文件」成立；若把「R51 brief」理解为「任何带 R51 契约标记的 brief」，则 R95 这份仍带该标记，措辞需收窄（见瑕疵 L5 相关）。
- **与 F16、A25/C01 一致性：MATCH**。

### K. 主线 `pipeline-state.json` 的 G0 / SHA

- 文件 `auto-paper/20261111-225602/Task-Aligned-Controls-for-Connectome-Vision/pipeline-state.json`：**3723 B**，SHA256 `bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d`（**SHA16 `bcb48bb964e657a4`**）。
- `stages` 中 G0：`status="pending"`、`inputs=[]`、`evidence=[]`、`gate_verdict="pending"`、`contract_version="v2"`（第 62–68 行）。
- 范围澄清：全项目共 11 份 `pipeline-state.json`；其中 3 份（其他 auto-paper 轮次）G0=`passed`，若干份无 G0 阶段。产物 F17 明确写「**Main-line**」，指向本轮根目录这一份，复算无误；该限定词不可省略（见瑕疵 L6）。
- `isolated/main_pipeline_state.json` 与其逐字节一致（3723 B / 同 SHA16）。
- **与 F17、C05/C36、A26 一致性：MATCH**。

### L. §3「不夸大」段与实测是否一致、12 类夸大逐条判定

- EVIDENCE.md §3 的非夸大清单（第 66–84 行，5 条 `Not ...`）与 A–K 实测逐条对应：①「不主张 brief 向评审员泄露期望分」由 C（交接块 0 命中）+ I 支撑；②「不主张机器门会因 `score_gt_threshold` 失败」由 G（字段保留、`>=`）支撑；③「不主张 R95 被旧 brief 锚定」由 J 支撑；④「不称 A6 为本轮新发现」由 H + 产物自述 R110/R111 已知支撑；⑤「不称首次发现 brief 路径不精确」由 §3 自述 R95 账本已有先例支撑。§6（第 130–134 行）另以 R115 W4 / R114 D1 否认「同机两脚本构成独立交叉核验」；§4（第 88–102 行）否认改字节、建 v4、起评审、晋级 G0、前向/科学结果。
- **§3 与实测一致性：MATCH**（未发现 §3 的否认与我的读数相矛盾）。

12 类点名夸大逐条判定（位置指 EVIDENCE.md / §3、§4、§6 及三份 JSON 的 boundary 字段）：

| # | 夸大 | 判定 | 独立依据 |
|:--|:--|:--|:--|
| (a) | 声称首次发现 | **REFUTED** | §3 第 81–84 行明确 `Not "first discovery"` 并给出 R95 账本先例；产物仅主张「清点了一层此前未审计的启动协议」（范围性新意，非发现层面的首次）。见瑕疵 L3。 |
| (b) | 声称 R107 配置错误 / 漏改 | **REFUTED** | §3 第 61 行、F7、ROUND-AUDIT §3 第 56 行均用 `deliberately` / `not an omission`；R107 第 90–92 行原文支持「故意冻结、v4 为未来路由」。产物把缺口归于「待 gate owner 裁决的版本化契约决定」（§5），非 R107 失误。见瑕疵 L5。 |
| (c) | 声称 brief 向评审员泄露期望分 | **REFUTED** | §3 第 68–72 行明确否认；C 实测交接块（21–66）`8.0`/`7.0` 0 命中且含两条非锚定指令。 |
| (d) | 声称机器门会因 `score_gt_threshold` 失败 | **REFUTED** | §3 第 73–76 行明确否认且称「成文口径差异、非可执行检查」；G 实测字段保留于 153–154 行且语义 `>=`。 |
| (e) | 声称 R95 被旧 brief 锚定 | **REFUTED** | §3 第 77–78 行明确否认；J 实测 R95 用另一份 5275 B 文件、无字面 `8.0`、与 R51 字节不同。 |
| (f) | 声称 A6 双口径是本轮新发现 | **REFUTED** | §3 第 79–80 行、F10、ROUND-AUDIT §5 第 111–112 行均标 `R110/R111 known` / `R109/R111/R118 已登记`、`仅作背景登记、不称新发现`。H 实测该双口径确在盘。 |
| (g) | 声称 G0 可 pass 或已晋级 | **REFUTED** | 文首 Kind、§3 第 80 行、§4 第 96–97 行、ROUND-AUDIT §6 第 118 行均否认；K 实测 G0 `pending`/`[]`/`[]`。 |
| (h) | 声称有科学结果 / 正向证据 | **REFUTED** | Kind 含 `NOT_SCIENTIFIC_RESULT`、§3 第 80 行、§4 第 99–100 行、ROUND-AUDIT §6/§7（`EXEC LOCK`、第 3 步前置未满足）均否认。 |
| (i) | 声称改了任何既有字节 | **REFUTED** | 产物声称的是**反面**：EVIDENCE.md 第 102 行、§4 第 91–92 行、RAW.json `boundary`、VERIFICATION.json `boundary`、ROUND-AUDIT §6 第 119–121 行均记「零既有字节改动 / 只读 / 仅写本目录产物」。9 份源 + 6 份 `isolated/` 副本经我复核逐字节一致；该「零字节」口径的时序限制见瑕疵 M2。 |
| (j) | 声称同机两脚本构成独立交叉核验 | **REFUTED** | §6 第 130–134 行、RAW.json `independence_caveat`、VERIFICATION.json `independence_caveat`、`R119-verify.py` 第 6–8 行均明确 `NOT an independent cross-verification`，并把真正独立复算委派给「全新隔离子代理」（即本报告）。 |
| (k) | 声称「全项目零本机绝对路径」 | **REFUTED** | 全部 R119 产物中**未出现**该或任何等价的「全项目/零绝对路径」断言（我对 R119 目录做 `全项目|零.*绝对|no.*absolute path|zero.*absolute` 等检索，0 命中）。脚本 docstring 仅称「emitted artifacts 中的本机绝对路径以 `<local>/` 表示」，是**对自身产物字段的脱敏约定**，非全项目断言。事实层面被测产物确含本机绝对路径（见瑕疵 M1），故若作此声称必为假；产物未作。 |
| (l) | 声称已创建 v4 契约或已启动评审 | **REFUTED** | §4 第 93–96 行、ROUND-AUDIT §6 第 121–122 行、VERIFICATION.json `boundary` 均明确否认；E 实测版本化启动 brief 为 0 份，产物把 v4 创建列为「将来由 gate owner 决定」（§5）。 |

**12 类中 CONFIRMED = 0，REFUTED = 12。** §3 的五条不主张、§4/§6 的边界与各 `independence_caveat`/`boundary` 字段均非空话，能被我从源字节复算的读数逐条支撑。

补充复核（支撑 i / j / 产物自洽性）：`R119-verify.py` 第 4–8 行声明「不 import 采集模块、不读任何 R119 JSON」，VERIFICATION.json 的 36 项 `expected`/`observed` 与我在 A–K 复算的数值全部吻合（C01 4803/`8771dea80cf7a54d`；C05 3723/`bcb48bb964e657a4`；C07–C13 行号 17/18/85/81/76/65/35；C14–C16 行号 90/91/92；C18/C19 行号 155/156；C20 行号 27/40/90；C26/C27 空集；C28 `[10]`；C29 `[11]`；C32 `0`；C33 `1`；C36 `pending`/`[]`/`[]`），`n_checks=36 / n_match=36 / n_mismatch=0`。`isolated/` 6 份副本与其源逐字节一致（6/6 `True`）。SOURCE-MANIFEST.json 中我抽查的 6 项 bytes/SHA 与源字节一致，`all_copies_identical=true`。R119 产物内**无**任何「行首分数行 + 数字」形式的新增行（唯一相关命中是 `isolated/brief.md:10` 内对一次历史自评分数的记述，属字节副本携带的历史文本，非本轮新增分数行；本报告不复写该字面串）。

---

## 2. 瑕疵清单（按 [高]/[中]/[低] 分级）

无 [高] 级瑕疵：A–L 的事实读数无 MISMATCH，§3 无与实测矛盾的否认，未发现核心数字造假、分数行、门晋级或科学结果声称。最高级别为 **[中]**。以下逐条给出具体位置与建议措辞（**仅建议，不替作者改任何文件**）。

### [中] M1 — 本机绝对路径脱敏约定与产物实际输出不一致
- **位置**：`R119-raw.py:16` docstring「Local absolute paths are represented as `<local>/` in emitted artifacts」；但同文件 `:34` 的 `PY` 常量（本机解释器路径，本文记作 `<local>/miniconda3/bin/python`）、`:264` `"python": PY` 把它**未脱敏**写入 `R119-REVIEW-LAUNCH-PROTOCOL-RAW.json:6`。`R119-REVIEW-LAUNCH-PROTOCOL-EVIDENCE.md:4`、`R119-ROUND-AUDIT.md:102` 亦含同一未脱敏字面串。`isolated/guard_criteria.json` / `isolated/guard_ledger.json` 作为字节一致副本，必然含大量 `<local>/...` 形式的硬编码绝对路径（这是副本正确性的要求，不是错误）。`R119-manifest.py:40–45` 的 `rel()` 与 `R119-SOURCE-MANIFEST.json` **确实**做到了脱敏（路径为 `<local>/fly-gnn-snn-vision/...`、`<local>/home/...`，且 `python` 字段为 `3.14.6`）。
- **问题**：同一句 docstring 在 `R119-manifest.py:6` 成立、在 `R119-raw.py` 自身及两份 Markdown 上不成立。本报告按脱敏要求同步公开仓库，而 EVIDENCE/RAW/ROUND-AUDIT 含有未脱敏本机路径，需由脱敏环节额外处理，存在口径不一致与漏脱敏风险。
- **建议措辞**：把 docstring 收窄为「source path fields in `R119-SOURCE-MANIFEST.json` are masked as `<local>/`」，并明确「newly authored Markdown/JSON prose and byte-identical `isolated/` copies are out of scope of this masking」；或统一把 `RAW.json` 的 `python` 字段改为 `sys.version.split()[0]`（与 manifest 一致），EVIDENCE/ROUND-AUDIT 中的解释器路径改为 `<local>/miniconda3/bin/python`。

### [中] M2 — 「零既有字节改动 / ledger SHA 前后一致」是时间快照口径，活文件已变
- **位置**：`R119-REVIEW-LAUNCH-PROTOCOL-EVIDENCE.md:102`「Zero pre-existing bytes changed. Only this R119 directory was created.」；`R119-ROUND-AUDIT.md:108`「ledger SHA16 `f98b69369db6eb80` / mtime `1794605184`, identical before and after」；`R119-REVIEW-LAUNCH-PROTOCOL-RAW.json:51–57` 记 `goal-ledger.md` 为 656281 B / `f98b69369db6eb80…` / mtime `2026-11-13T21:26:24+00:00`。
- **实测**：R119 各产物写盘时间为 EVIDENCE 06:44:34、RAW 06:43:10、VERIFICATION 06:43:53、manifest/manifest.py 06:44:59、ROUND-AUDIT **06:46:04**（+0800）。此后 `goal-ledger.md` 于 **06:48:12（+0800，UTC 22:48:12）** 被追加一段 R119 心跳账本条目（append-only，新增约 9529 B）：当前 **665810 B / SHA16 `4c90f4ce37c97832` / mtime `2026-11-13T22:48:12+00:00`**，与 RAW.json 记录的快照已不一致。该追加条目自述「全新隔离独立审查……写本段时尚未回收，不宣称任何审查结论」，属本轮心跳的常规只追加记账，发生在审计产物写盘之后，**不是**采集/复核脚本对历史字节的回写，也未改动任何历史正文、评审、分数、阈值、契约、门、判据、validator、稿件；6 份 `isolated/` 副本与 9 份源文件逐字节一致，36 项读数不受影响。
- **问题**：把「前后一致」写成无条件断言，在最终态（公开同步时）会被任何重新取哈希的读者判为不符；且「Only this R119 directory was created」与「一个既有文件（账本）被追加」字面冲突。这是时序/范围瑕疵，非数据造假、非门结论变化。
- **建议措辞**：「At the audit capture instant (UTC 2026-11-13T22:46:04), `goal-ledger.md` measured 656281 B / SHA16 `f98b69369db6eb80`; no historical byte, review, score, threshold, contract, gate, criteria, validator or manuscript was modified by this round. The standard append-only R119 heartbeat ledger entry was written afterwards and is outside this snapshot; subsequent appends change the live file hash but not any historical byte.」并把「Only this R119 directory was created」改为「The only newly created artifacts are under this R119 directory, plus the standard append-only ledger entry.」

### [低] L1 — `independent-review-brief*` 的计数口径未显式声明
- **位置**：F1、A1、A26e 记「1」。按文件名前缀 `independent-review-brief*` 为 1；按子串 `independent-review-brief` 为 2（另有 `R95-independent-review-brief-FROZEN.md`）。产物在 F16 已把第 2 份单列，二者不矛盾，但读者用 `*independent-review-brief*` 会得到 2。
- **建议措辞**：「Files whose **basename starts with** `independent-review-brief` (`independent-review-brief*` prefix glob): **1**. A different, separately-named file `R95-independent-review-brief-FROZEN.md` also contains the substring and is treated in F16.」

### [低] L2 — F10「guard criteria/ledger」未标 `-null-ladder`
- **位置**：EVIDENCE.md F10 表内写「criteria `>= 7.0` / ledger `严格 > 8.0`」。实际该双口径**仅**在 `guard/criteria-null-ladder.json` / `guard/ledger-null-ladder.json`；基础 `guard/criteria.json` / `guard/ledger.json` 无 A6 条目（旧 portfolio 历史件）。RAW.json / SOURCE-MANIFEST.json 已用精确文件名，EVIDENCE 正文未统一。
- **建议措辞**：F10 补为「`guard/criteria-null-ladder.json` A6 `>= 7.0` / `guard/ledger-null-ladder.json` A6 `严格 > 8.0`（基础 `guard/criteria.json`/`ledger.json` 为旧目标历史件，无 A6）」。

### [低] L3 — 「从未有轮次审计过 / 前 118 轮未触及」为宽泛历史否定，难由本轮字节独立证实
- **位置**：EVIDENCE.md §1 第 20–21 行「No round has audited the launch protocol of the sole success-criterion action itself」；`R119-ROUND-AUDIT.md:34`「a layer untouched in all 118 prior rounds」；账本 R119 条目「前 118 轮从未审计过的一层」。
- **问题**：这是对 118 个历史轮次的全称否定，我手上可用于独立复算的只有本轮 9 份源字节 + R119 产物，无法从这些原始字节证实该全称命题；它与 §3「不称首次发现」的谨慎口径存在轻微张力（前者否认「发现」层面的首次，后者主张「审计层」的首次）。属范围/时序措辞，不是事实错误。
- **建议措辞**：「Within the artifacts available to this round, no prior-round audit of the launch-protocol layer was found; this is a scope observation, not a claim of first-ever discovery of any defect.」

### [低] L4 — EVIDENCE.md §6 的文件清单时序/完整性小瑕疵
- **位置**：EVIDENCE.md §6 第 127 行引用 `R119-ROUND-AUDIT.md`，但该文件 mtime 为 06:46:04，晚于 EVIDENCE.md 的 06:44:34 —— 即在 EVIDENCE 落笔时该被引用文件尚未生成（最终态已生成、引用可解析）。另 §6 未列 `R119-manifest.py`，而 `R119-ROUND-AUDIT.md` §8 第 151 行列了。
- **建议措辞**：§6 改为「the artifacts in this directory (see `R119-ROUND-AUDIT.md` §8 for the full inventory)」，并把清单项按「写盘前已存在 / 写盘后追加」区分，避免读者按 §6 取文件时遇到缺失。

### [低] L5 — 「v4 路由从未建立」易被误读为 R107 漏改；「R51 brief」指代需收窄
- **位置**：F8「the v4 route named by R107 was never created」、§3 第 61–62 行「R107 ... named a v4 contract ... but no v4 brief exists」；F16「R95 was not launched from the R51 protocols brief」。
- **问题**：(b) 已被判 REFUTED，但「never created」若脱离 §5 语境，仍可能被读成「R107 忘了建」。§5 第 110–113 行与 ROUND-AUDIT §7 已澄清这是待 gate owner 书面裁决的版本化契约决定。另 J 实测 `R95-...-FROZEN.md` 首行同样带 `(Contract v2, R51)`，故「R51 brief」作为短语有歧义；F16 用全称路径时是精确的。
- **建议措辞**：F8/§3 补「no v4 artifact has been created **by any subsequent round**; creating it is a pending versioned-contract decision for the designated gate owner (R107/R111), not an R107 omission」；F16 统一写「the R51 **protocols/** brief」而非「the R51 brief」。

### [低] L6 — 「Main-line」限定词不可省略（范围提示，非事实错误）
- **位置**：F17「**Main-line** `pipeline-state.json`」。全项目另有 3 份 `pipeline-state.json` 的 G0=`passed`（其他 auto-paper 轮次）。我的复算确认「主线」这一份为 `pending`/`[]`/`[]`，产物措辞本身正确且重要。
- **建议措辞**：公开/脱敏稿中务必保留 `main-line`，可补一句「other per-paper `pipeline-state.json` files are out of scope; their G0 values differ」。

**瑕疵合计：8 条（[中] 2 条、[低] 6 条、[高] 0 条），最高级别 [中]。**

---

## 3. 边界声明（本复核自身）

- 我**未修改、删除、重命名任何已存在的文件**；本次会话唯一写入的文件即本报告 `review-protocol-R119/R119-INDEPENDENT-REVIEW.md`。所有其余动作为 `read` / `find` / `grep` / 内存字节计算。
- 我**未产生任何形如 `**Overall:**` 后跟数字的行**，未对任何稿件打分，未给出或猜测任何期望分、分数锚点或「目标分」；文中出现的 `8.0` / `7.0` / `8.2` / `6.5` / `6.0` 等数字，均只是被测文件中字面串的如实转录或历史状态记述，不作为评分标准。
- 这**不是** `ccf-paper-reviewer full` 稿件评审；未做前向 pass / 推理 / 训练 / 标签 / 数据集加载 / 科学指标；**未联网**；未自我认证、未宣布任何门通过、未把工程一致性说成科学结果。
- 我**不宣布 G0 可 pass、不晋级任何门**；G0 仍为 `pending`（K 实测）。本报告只复核「启动协议链的只读一致性清点」这一对象的事实与边界。
- 关于独立性：被测产物自身（§6、RAW/VERIFICATION 的 `independence_caveat`、`R119-verify.py:6–8`）已如实声明「同机两脚本一致只是必然一致性核对、不构成独立交叉核验，真正独立复算交全新隔离子代理」。本报告即承担该委派：我未读取作者会话、未以任何 R119 JSON 作为 A–K 的取数依据，全部读数从源字节独立复算。
- 本报告不含本机绝对路径；如需引用一律写作 `<local>/`。

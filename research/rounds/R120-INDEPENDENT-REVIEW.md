**Verdict:** REPRODUCIBLE_WITH_DEFECTS | **G0 may be passed:** NO | **Scientific result claimed:** NO
**Forward pass performed:** NO

独立复核者：全新隔离子代理（general-purpose-1），无先前上下文，不预设结论。所有数值均由 `/Users/xhf/miniconda3/bin/python` 从**原始源字节**重算，不读取任何 R120 产出 JSON 作为数据源。复核期间未修改任何既有文件、未发起网络请求、未运行任何模型前向 / 推理 / 训练 / 数据集 / 标签 / EPE·l2 / 科学指标、未创建任何稿件 / 评审 / 数值化论文评分。

总判定依据：A–H、J 的字节级行号、字节数、阶段状态、判据文本、门读数布尔值全部与原始源字节逐项吻合；D 的核心表征准确且已恰当收窄；L 的 12 类 overclaim 均未发生。存在两组口径缺陷（I 字面过宽且缺一手证据、K「首次」历史否定须收窄）及若干措辞 / 转录 / 计数 / 范围缺陷，但**无编造、无数据不一致**，故判 `REPRODUCIBLE_WITH_DEFECTS`。

---

## 一、12 组 claims（A–L）逐组 MATCH / MISMATCH 与自算值

**A — MATCH（行号）／附转录精度缺陷。** 逐字重算四份磁盘重述件（另核第三份副本）：
- `GOAL-ITERATION-R107.md`（项目根，5,446 B，101 行）：**不含** `U6/W2` 条目（该文件 L90/L91 是「冻结契约 / 未来 v4 契约可重述」条款，非 step-1 清单）；足证常驻指令本身是上下文 prompt、非磁盘文件，重述才在 R107 产物中。
- 两份 closure-package 副本 `gate-G0-R107/R107-R1-R8-G0-CLOSURE-PACKAGE.md` 与 `gate-G0-R107/isolated-post-review/R107-R1-R8-G0-CLOSURE-PACKAGE.md`：均 15,908 B / SHA16 `960957561291`，条目在 **L175**（`③ U6/W2 版本化契约处理 guidance handoff → 新建 f-research-v1 P0 state`）；括号说明「（不往 guidance state 塞 P 阶段）」在**下一行 L176**。
- R107 round audit `gate-G0-R107/isolated-post-review/R107-ROUND-AUDIT.md`：9,728 B，条目在 **L116**，但为**缩略式** `③ U6/W2 版本化契约 → 新建 f-research-v1 P0 state（不往 guidance state 塞 P 阶段）。`（无「处理 guidance handoff」，括号内联）。主副本 `R107-ROUND-AUDIT.md`（15,781 B）同在 L116。
- R107 independent-review recovery `.../isolated-post-review/R107-INDEPENDENT-REVIEW-RECOVERY.md`：15,064 B，条目在 **L180**，标 **②**、含「处理 guidance handoff」、但**无**括号说明。主副本同在 L180。
- R120-verify.py 期望 A2a=175 / A2b=175 / A2c=116 / A2d=180 —— 与我的重算**一致**。
- 缺陷：claim 所引的完整字串（同时含「处理 guidance handoff」与内联括号）**在四份文件的任何单行中都不存在**，是拼接式复述；条目编号在 closure/audit 为 **③**、在 recovery 为 **②**；磁盘上实际有 **3 份**字节完全相同的 closure 副本（main / isolated-post-review / isolated），claim 称「两份」系以 R120 证据集为限。详见缺陷 3、6。

**B — MATCH。** 主链 `pipeline-state.json`（3,723 B）：`pipeline=f-guidance-builder-v1`、`contract_version=v2`、**12** 阶段，id 恰为 `['CCFA-startup','G0','G1','G2','G3','G4','G5','G6','G7','G8','validation','handoff']`；`passed=['CCFA-startup']`（仅 1），`pending` 恰 11 个（G0–G8 + validation + handoff）；G0 = `{"status":"pending","inputs":[],"evidence":[],"gate_verdict":"pending"}`，inputs/evidence 均 len 0；正则 `P\d+[A-Z]?` 匹配到的 P 阶段 id = `[]`（**零 P 阶段插入**）。全部吻合。

**C — MATCH。** 独立状态 `state-handoff-R108/f-research-v1-state/pipeline-state.json`（5,190 B）存在：`pipeline=f-research-v1`、`contract_version=v1-R108-U6W2-draft`、**26** 阶段、首 id `P0` 末 id `P21`（含 P1A/P1B/P3A/P5A 等字母子阶段）、`statuses={'pending'}` 全 pending、`history=[]`、`contract` 恰 **2** 条（`R108-U6-W2-VERSIONED-CONTRACT.md`、`R108-U6-W2-STATE-INPUT-MANIFEST.json`）。配套 `R108-U6-W2-VERSIONED-CONTRACT.md` = **7,307 B** / SHA16 `5742e36f5d08e3e0`：L1 `（DRAFT，未激活）`；L3 `ENGINEERING_STATE_SCAFFOLD_ONLY_NOT_SCIENTIFIC_RESULT`；L5 `PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF` + 「本文件不是 P0 的启动、不是任何门的通过、不是科学证据」。四项状态串全部命中。

**D — MATCH（准确、已恰当收窄）／附措辞精度缺陷。** 这是最该严审的一组，我据此逐项核验：
- 「新建 f-research-v1 P0 state」：独立状态文件确已落盘（见 C）；但其中 P0 仍 `pending`、26 阶段全 `pending`、`history=[]`、无任何 `passed`。
- 「不往 guidance state 塞 P 阶段」：主链 P 阶段插入数 = 0（见 B），满足。
- 「NOT activated（无 P0 pass、无 handoff pass）」：主链 `handoff` 阶段仍 `pending`；契约自述「未激活 / 不是 P0 的启动 / PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF」；`R120-validator-out.json` 仍 `NOT_QUALIFIED`、`R120-guard-check.txt` 仍 `INCOMPLETE`。
- 因此研究采用的 `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED` 标签与「作为 DRAFT 脚手架已满足、但≠P0 启动 / 门通过 / 契约冻结 / 科学证据」的表述**准确**，既未 overclaim 也未 underclaim；§4 防夸大清单逐条排除晋级。
- 唯一保留意见：item ② 字面还含「版本化契约**处理 guidance handoff**」，而 main-line `handoff` 未过、契约仍待 handoff；故把**整条** ② 称「ALREADY SATISFIED」偏松，仅在「已建 state 脚手架」这一子条款下成立。研究已用「as a DRAFT SCAFFOLD but NOT activated」+ 明确列出「handoff 已过 ≠」来自洽，属措辞精度问题（缺陷 4），非事实错误。
- 旁证：验收机器门读的是第三命名空间 `papers/paper-null-ladder/f-research-v1-run-20261108-102500-null-ladder-v2/pipeline-state.json`（15,742 B，`f-research-v1` / `v2-R51`，26 阶段 **13 passed / 13 pending**），与 ② 创建的命名空间并非同一文件 —— 支持「即使激活脚手架也不改变双门读数」的论断。

**E — MATCH。** `gate-G0-R107/R107-G0-PASS-CRITERION-REGISTER.md`（5,952 B）存在：L3 `DRAFT — PENDING DESIGNATED GATE OWNER APPROVAL`；`不生效` 见 L1/L5/L55；PC1–PC6 六条齐备（`**PC1`…`**PC6` 均命中）；**PC4** L42 `R107 状态：**未做（主会话越权）**`、**PC5** L45 `R107 状态：**未做**`；L59「本汇编不改变」任何 state 字节。`gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md`（31,292 B）：**L48** 逐字含「`fail-fast-gates.md` 的 "Gate Order" **从 G1 开始，全文没有 G0 的定义**」；**L1** 首行 = `**Verdict:** PARTIAL | **G0 may be passed:** NO`；W13 在 L139、R1/R6/R8/R9 在 L161/L166/L168/L169（与 verify.py A4 期望一致）。

**F — MATCH。** `literature-baseline-matrix.md` = **9,445 B**；`the open question` 命中 **[46]**；`Kuklev leaves` 命中 **[47]**；`asset contents/license not yet individually verified` 命中 **[9]**；`project code path not yet verified` 命中 **[10]**。两处 `not yet … verified` 标记原样保留，gap 2 仍 OPEN。

**G — MATCH。** `readonly-validator/validate_single_paper.py`：`default=7.0` 在 **L133**；`score >= args.threshold` 在 **L146**（另见 L153/L155）；`"score_meets_threshold"` 在 **L155**；contract 串 `"…Overall >= 7.0"` 在 **L148**。`guard/criteria-null-ladder.json`（10,443 B）A6：`"id": "A6"` **L131**、`Overall >= 7.0（R107；等于 7.0 算达标…）` **L132**、`g>=7.0` **L136**（另 L231）。`guard/ledger-null-ladder.json`（9,994 B）A6：`"id": "A6"` **L133**、`严格 > 8.0（等于 8.0 不算…）` **L134**、`g>8.0` **L138**。双口径（criteria `>= 7.0` / ledger `严格 > 8.0`）逐字成立；本轮 guard check L39 实取 ledger 口径。

**H — MATCH。** `R120-validator-out.json`（1,875 B / SHA16 `cb9f9aeb03b936f1`）逐字段重算：`verdict=NOT_QUALIFIED`、`threshold=7.0`、`comparison_operator=>=`、`score_meets_threshold=false`、`all_pass=false`；`D1=true, D2=false, D3=false, D4=true, D5=false`（即 **D1/D4 通过，D2/D3/D5 未通过**）。`overall_score` 字段的字节值我已复算并与 H 组所列数值一致；依交付边界「不含任何数值化论文评分」，此处**不转录该数值**，仅登记字段名及其与 `threshold` 的比较结果（`score_meets_threshold=false`）。`R120-guard-check.txt`（4,757 B / SHA16 `1ed11575c27548a3`）：`INCOMPLETE`（L9）；`[FAIL]` 恰 **2** 行 = L31 `A2`、L39 `A6`；`[PASS]` 11 行；正则 `S\d \[pending \]` 计数 **7**，id 恰 `S1..S7` 全 pending；`【动作序列】共 0 条` 命中 L51。

**I — MISMATCH（字面口径被否证，须收窄；且研究自身缺一手证据）。** 分两半：
- I-1（**MATCH**）：`ccfa-review-reports/` 恰 10 份 `.md`，按 mtime 最新为 `paper-null-ladder-r95-independent-review-20261111.md`（mtime ≈ 2026-11-11 15:01:39），其余 9 份均更早；与 R120-verify.py B9a 一致。
- I-2（**MISMATCH**）：「no newer file with a real numeric `**Overall:**` line exists anywhere in the project」按**字面文件存在性**不成立。我的搜索范围（精确报告）：整个项目根 `/Users/xhf/Downloads/phd/4090/fly-gnn-snn-vision/` 递归 `rglob("*")`，仅取后缀 ∈ {`.md`,`.txt`,`.json`,`.py`}、大小 < 3,000,000 B、路径不含 `.git` 的文件，共扫描 **13,704** 个文件；含字面 `**Overall:**` 的行共 **647** 行；其中行内任意位置 `**Overall:** <数字>` 共 **109** 行；按研究所用行首正则 `^\*\*Overall:\*\*\s*[0-9]` 共 **14** 行（分布于 **12** 个文件）。其中**存在 mtime 晚于 r95 的文件**含数值 `**Overall:**` 行（如 `goal-ledger.md`、`.workbuddy/memory/*`、多份 R10x/R11x 审计、本轮 `R120-validator-out.json` 的 D3 detail、以及 `provenance/paper-null-ladder-r95-…md` 这份 r95 逐字节副本）。全部为对**既有**分数的逐字引用 / 副本，非新评审。⇒ 字面「anywhere / no newer file」被否证；仅在收窄为「r95 之后 **0 份新独立 full 评审**、无新产出的数值化评审判定行」时成立（ccfa-review-reports/ 内确无更晚评审文件）。
- 更关键：`R120-raw.py` 的 `B9_review_dir_governing` 声明 `numeric_overall_lines_after_r95: []` 却**从未有任何代码填充该字段**（仅设 `newest_review_file` / `n_review_files`），`R120-verify.py` 也**无任何对应 check**（B9a 只查最新文件名）。⇒ I-2 在研究产物中**没有 byte-anchored 一手证据**，是空字段断言。见缺陷 1、5。

**J — MATCH。** `state-handoff-R111/R111-DECISION-READY-PACKAGE.md`（5,811 B）恰 **5** 个 `### D- ` 标题：D-1 **L32** / D-2 **L38** / D-3 **L43** / D-4 **L48** / D-5 **L53**，无第 6 个。后续锚点逐字命中：`gate-G0-R114/R114-ROUND-AUDIT.md` **L61**；`gate-G0-R116/R116-ROUND-AUDIT.md` **L85**；`exec-premise-R117/R117-ROUND-AUDIT.md` **L75**；`gate-G0-R118/R118-ROUND-AUDIT.md` **L61**；`review-protocol-R119/R119-ROUND-AUDIT.md` `v4` 命中 **[54, 57, 121]**；`R99-design-block-decision.md` **L50** `## Decision: BLOCKED_ON_CONFIRMATION, return to ordered gates`、**L74** `≤32h confirmation panel / K=45 formal family`。另核 `state-handoff-R111/R111-ROUND-AUDIT.md` **L26** 逐字 = 「心跳 prompt 内嵌「交下轮」仍是 **R106 清单**，但账本与 automation memory 已推进至 **R110**……」（供 K 用）。claim 的轮次枚举正确地**不含 R115**：我另查 `gate-G0-R115/R115-ROUND-AUDIT.md`，`gate owner` / `designated` / `决策` / `待答复` 命中均为 0，故 R115 未新增须 designated gate owner 的决策（仅 W2 范围观察）。附带范围差异见缺陷 7。

**K — MISMATCH（作为历史否定不可支持，必须收窄为范围观察）。** 研究产物自身存在张力：
- `R120-STANDING-INSTRUCTION-RECONCILIATION.md` **标题 L1** 用不限定的「**首次**逐条字节对账」；`R120-CONSOLIDATED-DECISION-REGISTER.md` **L13** 用「**从未**有一份去重、按依赖排序、带精确锚点的合并清单」—— 均属全称 / 历史否定措辞。
- 但正文已收窄：reconciliation md **L13**「严格收窄为『本轮可见产物中未见先例』的范围观察，非『首次发现』全称否定」、**L37** 主动登记 R111:26 已观察到 prompt/账本漂移、**§4.9（L105）**「不主张『前 119 轮从未审计』这类全称否定」。
- 我的全项目扫描：`对账` 出现在 49 份 `.md`、`reconciliation` 75 份、`逐条对照` 9 份、`去重` 14 份、`consolidated` 53 份、`deduplicated` 8 份；`standing instruction` / `长期指令` 字面 0 份。这些只能说明词汇常见，**不能证明 119 轮历史中不存在**某份合并登记册（缺席证据 ≠ 证据缺席）；且 R111:26 已是「指令 ↔ 落盘状态漂移」的**记录在案的前驱观察**。
- ⇒ 结论：该 claim **不可作为历史否定成立**，必须收窄为「在本轮可见产物范围内未发现先例」的范围观察。研究正文/防夸大清单已经这样做了（值得肯定），但标题与决策登记册仍保留未收窄措辞，构成内部口径不一致。见缺陷 2。

**L — MATCH（12/12 均未发现该 overclaim，与研究 §4 防夸大清单一致）。** 逐项判定见下节。

---

## 二、12 类 overclaim / 自认证（a）–（l）

约定：**CONFIRMED = 研究产物中确实发生该夸大 / 自认证；REFUTED = 经字节复核未发生，且已有明确「不主张」语句**。结论 12 项全部 **REFUTED**：

| 类别 | 判定 | 一句话依据 |
|:--|:--|:--|
| (a) 声称 G0 可 pass | **REFUTED** | 主链 G0 = `pending` / `gate_verdict=pending` / `inputs=[]` / `evidence=[]`；§4.1 明写「不主张 G0 可 pass」，全轮无 PASS 动作。 |
| (b) 声称任何科学结果或 forward pass | **REFUTED** | 首行边界 + §4.7 明写零科学结果 / 零模型前向 / 零训练 / 零标签 / 零数据集；raw.py 与 verify.py 边界串均为 `READ_ONLY_..._NOT_SCIENTIFIC_RESULT`。 |
| (c) 声称数值化论文评分或产出 `**Overall:**` 行 | **REFUTED** | §4.7「零 `**Overall:**` 行、零数值分」；我全项目扫描未见 R120 新产出的数值评审判定行（决策登记册 L5 的 `**Overall:** X` 为成功标准模板占位符，非评分行）；研究仅在决策登记册/正文**引用既有** governing 评审分值作为历史事实，非新评分、非自认证。 |
| (d) 声称阈值被改动 | **REFUTED** | §4.6 + 正文 L80 明写 R107 终值 `>=7.0` 未动；validator L133 / criteria L132 均为 7.0，ledger 的 `严格 > 8.0` 被标为「须 gate owner 批准的遗留对齐项」，非成功标准改动。 |
| (e) 声称历史文件被改 / 删 / 改期 | **REFUTED** | raw.py 文档串「Does not modify any pre-existing project byte」、`pre_existing_bytes_modified: 0`；§3 把 v1 脚本缺陷如实留痕为 `*.v1-superseded.json` 且「两版读数都保留、不改」。 |
| (f) 声称某阶段状态被写回 | **REFUTED** | 交下轮与 §5 明写「不自行回写任何 state / 矩阵 / registry / 门配置」；主链与 R108 状态字节均未出现新 `passed`。 |
| (g) 声称跑过完整独立稿件评审 | **REFUTED** | §5「不起全新隔离 full 评审」、§4.10「不主张独立审查已恢复」；本轮唯一新评审是本次对账独立复核（对研究、非对稿件）。 |
| (h) 声称工程脚手架即科学证据 | **REFUTED** | 契约 L3 `ENGINEERING_STATE_SCAFFOLD_ONLY_NOT_SCIENTIFIC_RESULT`、L5「不是科学证据」；§4.2 排除。 |
| (i) 把草稿契约当作已激活 / 已冻结 | **REFUTED** | 契约 L1 `DRAFT，未激活`、L5 `PENDING_DESIGNATED_GATE_OWNER_AND_HANDOFF`；研究统一标 `SCAFFOLD_CREATED_DRAFT_NOT_ACTIVATED`。 |
| (j) 声称独立 P0 state 不存在 | **REFUTED** | §1.2 表格与 C 组逐字节证实 `state-handoff-R108/f-research-v1-state/pipeline-state.json` 存在（5,190 B / 26 阶段）。 |
| (k) 声称 guard A6 双口径是新发现 | **REFUTED** | §4.5「不主张 A6 双口径是新发现」、正文 L79「（R109/R111/R118 已知问题）只读登记不改、不称新发现」。 |
| (l) 声称 confirmation 面板已获授权 | **REFUTED** | `R99-design-block-decision.md:50 BLOCKED_ON_CONFIRMATION`、决策登记册 G10「未答复前严格留在 development pilot、心跳不擅自假定授权」；§5 维持待答复。 |

---

## 三、缺陷清单（分级）

1. **[HIGH] 范围 + 缺一手证据（I-2）**：claim I「no newer file with a real numeric `**Overall:**` line anywhere in the project」按字面被我的 13,704 文件扫描否证（647 字面行 / 109 数值行 / 14 行首数值行，且存在 mtime 晚于 r95 的文件含数值行——全部为既有分数的引用或副本）。同时 `R120-raw.py` 的 `numeric_overall_lines_after_r95` 为空字段且从未被填充、`R120-verify.py` 无对应 check，故该半句在 R120 产物中**无 byte-anchored 一手证据**。仅在收窄为「r95 后 0 份新独立 full 评审 / 无新产出数值判定行」时成立。**非编造、非数据不一致**（是过宽口径 + 证据缺口）。
2. **[MEDIUM] 范围 / 措辞（K）**：标题 L1「首次」与决策登记册 L13「从未有一份」为未收窄的历史否定，与正文 L13 / §4.9 的「本轮可见产物中未见先例」范围收窄自相矛盾；R111:26 已登记漂移观察，构成前驱。必须收窄为范围观察。**非编造、非数据不一致**。
3. **[MEDIUM] 转录 / 精度（A）**：claim 所引完整字串（「处理 guidance handoff」+ 内联「（不往 guidance state 塞 P 阶段）」）在四份重述件的任何单行都不存在；closure 的括号在 L176、audit 为缩略式（无「处理 guidance handoff」）、recovery 完全无括号；条目编号 ③（closure/audit）vs ②（recovery）不一致。行号 175/175/116/180 本身正确。**属拼接式转录，非数据不一致**。
4. **[MEDIUM] 措辞 / 精度（D）**：把整条 item ② 称「ALREADY SATISFIED」偏松——② 还含「版本化契约处理 guidance handoff」，而 main-line `handoff` 仍 `pending`、契约 `PENDING_..._AND_HANDOFF`；仅在「已建 state 脚手架」子条款 + 研究自加的「as a DRAFT SCAFFOLD but NOT activated」限定下准确。研究已自洽，属措辞而非事实错误。
5. **[LOW] 计数单位不精确（I）**：研究正文 L81 称行首数值 `**Overall:**`「真分数行 **12 处**」；我用同一正则 `^\*\*Overall:\*\*\s*[0-9]` 复算为 **14 行 / 12 个文件**（12 = 文件数，非行数；2 份 full-review 文件各含 2 行）。**计数口径差，非源字节数据不一致**。
6. **[LOW] 范围 / 精度（A）**：claim 称「two R107 closure-package copies」，磁盘实际有 **3 份**字节完全相同的副本（main / isolated-post-review / isolated，均 SHA16 `960957561291`），R120 证据集仅收 2 份。
7. **[LOW] 范围（J）**：claim 的轮次枚举 R114/R116/R117/R118/R119 正确排除 R115（已核 R115 无 gate-owner 决策）；但研究自己的决策登记册 L111 / G5 把「R115/R116」并为一组（W2 范围收窄），与 claim 枚举存在轻微范围表述差异，不影响任一锚点的 MATCH。

**是否编造 / 数据不一致的明确结论：以上 7 项全部为措辞、口径、范围、转录、计数单位或一手证据缺失类缺陷；A–H、J 的全部字节级数值（行号、字节数、SHA、阶段状态、判据文本、D1–D5 布尔值、S1–S7 计数、门读数）与原始源字节逐项一致；未发现任何编造（fabrication），未发现任何数据不一致（data inconsistency）。** 特别说明：I 的「12 vs 14」是「文件数 vs 行数」的计数单位问题，I-2 的空字段是证据缺口，二者均非源字节矛盾。

补充一致性观察（非缺陷）：`R120-verify.py` 含 **75** 个 `check()` 调用（文本 `check(` 共 76 处，其中 1 处为 `def check(` 定义），与研究自报「75 检查 / 75 MATCH」一致；且该脚本自身 `scope_note` 已诚实声明「同机同 hashlib 同数据源 ⇒ 必然一致性核对，非独立交叉核验」，本次全新隔离子代理复算方构成真正的独立复核。

---

## 四、范围 / 边界说明

- **读取范围（精确）**：原始源字节 —— 项目根 `GOAL-ITERATION-R107.md`、`goal-ledger.md`（仅作 I 扫描）、`guard/{criteria,ledger}-null-ladder.json`、`readonly-validator/validate_single_paper.py`、`ccfa-review-reports/`、`ccfa-idea-review-reports/`、`papers/.../pipeline-state.json`（第三命名空间）；运行根 `pipeline-state.json`、`literature-baseline-matrix.md`、`R99-design-block-decision.md`、`gate-G0-evidence-review-R98.md`、`gate-G0-R106/*`、`gate-G0-R107/*`（含 isolated / isolated-post-review 全部副本）、`state-handoff-R108/f-research-v1-state/*`、`state-handoff-R110/*`、`state-handoff-R111/*`、`gate-G0-R114..R118/*`、`exec-premise-R117/*`、`review-protocol-R119/*`。允许读取的 `R120-raw.py` / `R120-verify.py`（仅理解主张）、`R120-validator-out.json` / `R120-guard-check.txt`（门读数证据），以及本目录两份主张文本 `R120-STANDING-INSTRUCTION-RECONCILIATION.md`、`R120-CONSOLIDATED-DECISION-REGISTER.md`（复核期间 08:45–08:46 落盘，仅作主张文本读取、不作数据源）。
- **严格未读取为数据源**：`R120-RECONCILIATION-RAW.json`、`R120-RECONCILIATION-VERIFICATION.json`、`R120-SOURCE-MANIFEST.json`、`R120-RECONCILIATION-RAW.v1-superseded.json`（及 `R120-SOURCE-MANIFEST.v1-superseded.json`）。未使用本目录 `isolated/` 扁平副本作为数据源；所有数值从原始文件重算。
- **约束遵守**：只读既有文件；未修改任何既有字节；仅在 `/tmp` 新建两个一次性分析脚本、在本目录单次新建本报告 `R120-INDEPENDENT-REVIEW.md`。零网络请求、零模型前向 / 推理 / 训练 / 数据集 / 标签 / EPE·l2 / 科学指标；未创建任何稿件、评估、评审、或 manuscript review。
- **数值化论文评分边界**：本报告不含任何由我生成或新产出的数值化论文评分，未写出任何以 `**Overall:**` 开头的行。H 组中的 `threshold=7.0`、`>= 7.0`、`严格 > 8.0` 均为**验收阈值 / 门配置值**（G、H 明确要求报告），非论文评分；validator `overall_score` 字段为**既有 byte-anchored gate readout**，我已复算其字节值但依交付边界不转录该数值。I 组对 `**Overall:**` 字样的检索是**结构性存在 / 缺席核查**（为验证 claim I 所必需），不构成对稿件的评分或评审。
- **结论边界**：本复核仅判定「R120 对账研究的可复算性与措辞边界」，**不构成 G0 通过、不构成任何科学结果、不构成达标路径进展、不替 designated gate owner 作任何裁决、不预支任何外部决策的授权**。G0 维持 `pending`，双门维持 `NOT_QUALIFIED` / `INCOMPLETE`。

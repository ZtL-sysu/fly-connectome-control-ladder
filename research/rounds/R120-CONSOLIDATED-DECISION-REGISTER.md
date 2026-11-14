# R120 — 外部决策债去重登记册（交给用户 / designated gate owner 的唯一入口）

**性质**：只读合并结果，**不是**请求降低标准、**不是**请求放宽证据、**不是**请求跳过任何门、**不是**自我认证。心跳在无人值守下**不假定任何一项已获授权**，本轮未执行任何修复、未写回任何 state / 矩阵 / registry / 门配置。

**成功标准（R107 用户授权终值）不变**：由全新隔离独立子代理 `ccf-paper-reviewer full` 落盘**新的**报告，`**Overall:** X` 且 **X >= 7.0**；只认 `readonly-validator/validate_single_paper.py` QUALIFIED + `guard check` COMPLETE。governing 仍 **R95 = 6.0**，`0 篇达标`。

**本轮读数**：validator `NOT_QUALIFIED / 6.0 / >=7.0`（D1✓ D2✗ D3✗ D4✓ D5✗）；guard `INCOMPLETE`（A2、A6 FAIL，S1–S7 全 pending，动作序列 0 条）。

---

## 为什么需要这一份登记册

R99 / R106 / R107 / R110 / R111 / R114 / R115 / R116 / R117 / R118 / R119 把须外部批准的决策写在 **11+ 份**文件里，且每轮「交下轮」都重列一遍、彼此重叠、措辞不一。R111 曾产出 5 点决策包（`R111-DECISION-READY-PACKAGE.md:32/38/43/48/53`），但此后 R114–R119 又新增了 6 组决策，散落在各自轮次审计中，从未有一份去重、按依赖排序、带精确锚点的合并清单。R111 判定「自主可达动作穷尽」，R105/R107/R109 三次判停「继续产出证据文档」同构循环 ⇒ **唯一能解锁的是下面这些决策**。

本册把散落项去重为 **10 个决策组（G1–G10）**，每组给出：要决定什么、精确 `文件:行号` 锚点、现状、依赖、批准后的心跳第一步、不批准的后果。**去重口径**：同一决策在多轮重复出现只登记一次，保留最早 + 最新两份锚点；「不执行须批准修复」这类每轮复述的纪律句不单列为决策。

---

## G1【阻塞其余全部】交付对象与门路径裁决

- **要决定**：以**主线**（`auto-paper/20261111-225602/...`，`f-guidance-builder-v1`，12 个 G 阶段）还是**历史 v2**（`papers/.../f-research-v1-run-20261108-102500-null-ladder-v2/`，26 个 P 阶段，13 passed / 13 pending）作为交付对象？门配置（validator D2 / guard A2）是否从 v2 root 重指向主线？
- **锚点**：`R111-DECISION-READY-PACKAGE.md:32`（D-1）；`state-handoff-R110/R110-ROUND-AUDIT.md`（C5）；`state-handoff-R111/R111-ROUND-AUDIT.md:101`；本轮 `R120-STANDING-INSTRUCTION-RECONCILIATION.md §1.3` 量化三个互异 SHA 状态命名空间。
- **关键事实**：v2 稿件是 R95 评过 **6.0** 的历史 9 页稿；主线尚无稿件。三条路都必须先有**实质修订稿 + 实质正向新科学证据**（红线禁止对未修改稿件重复评审）。**即使只激活 R108 草稿脚手架也不会改变双门读数**，因为机器门读的是命名空间 #3。
- **批准后心跳第一步**：按裁决生成「证据链映射表」，逐阶段列真实证据要求与现有覆盖，**仍不写回任何 state**。
- **不批准**：门路径维持现状；主线 G0–G8 全走完也不改变双门（R110 C5）。

## G2【机器门】`guard/ledger-null-ladder.json` A6 是否同步到 `g>=7.0`

- **性质**：把遗留机器门对齐到 R107 **已授权**的标准，**不是**再次改动成功标准。
- **锚点**：`R111-DECISION-READY-PACKAGE.md:38`（D-2）；`guard/criteria-null-ladder.json:132/136` `>=7.0`；`guard/ledger-null-ladder.json:134/138` `严格 > 8.0`；`gate-G0-R116/R116-ROUND-AUDIT.md:63`；`exec-premise-R117/R117-ROUND-AUDIT.md:58`。
- **已知单独不足**：A2 与 D2/D5 恒 FAIL，仅同步 A6 无法使 QUALIFIED + COMPLETE 同时成立。
- **批准后心跳第一步**：只改该一处判据文本 / 命令，前后落字节快照，复跑双门登记变化。

## G3【机器门 / 证据链】13 个阶段真实证据 + 步骤台账认证 + D5 矩阵

- **要决定**：是否授权补齐历史 v2 `P9–P21` 的真实阶段证据并写回 `pipeline-state.json/.md`，或改走主线 `P0–P21`；是否授权 `guard` S1–S7 步骤状态认证；D5 的 `Claim-to-evidence` 矩阵（当前是单点字符串缺口，但补它属稿件 / 证据链实质改动，须与 G1 一并裁决）。
- **锚点**：`R111-DECISION-READY-PACKAGE.md:43`（D-3）；`state-handoff-R111/R111-ROUND-AUDIT.md:112`；`gate-G0-R114/R114-ROUND-AUDIT.md:59`；`gate-G0-R116/R116-ROUND-AUDIT.md:84`。
- **红线**：任何阶段状态写回必须是**真实执行 + 真实证据**的结果；心跳不得批量标 passed、不得用 stale evidence 晋级、不得自我认证。

## G4【G0 判据】书面冻结 G0 pass criterion + 指定独立判定方

- **根因**：`fail-fast-gates.md` 全文从 G1 起，**没有 G0 成文 pass criterion**；R98 W3 已连续发现「验收判据由被评方自写，GOOD/BAD/TRIVIAL 全部通过」。
- **现状**：`gate-G0-R107/R107-G0-PASS-CRITERION-REGISTER.md` 已产出 PC1–PC6 **DRAFT**，:3 明写 `PENDING DESIGNATED GATE OWNER APPROVAL`、:1 明写「不生效」、:59 声明不改任何 state 字节；PC4（:42）/ PC5（:45）标「未做」。
- **锚点**：`R111-DECISION-READY-PACKAGE.md:48`（D-4）；`gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md:48 / :139 / :161–169`（W13、R1–R9）；`state-handoff-R111/R111-ROUND-AUDIT.md:113`。
- **要决定**：由 designated gate owner **书面冻结**判据并**指定独立判定方**；R98 gap 1/2/4 与 G4（Kuklev v2 §7.3 sweep、§8 `Two gaps remain.`、§9 Limitations）如何正面处理；R6 显式 scientific/visual gate judgment、R7 的 G0 `inputs`/`evidence` 登记与显式 `passed`、R9 全新独立复核如何落盘。
- **批准后心跳第一步**：按冻结判据逐条补**一手可复算件**，不写补丁式文字修复；更正动作不得自我认证。

## G5【gap 1】三项剩余一手取证判断

- **内容**：① Correig-Fraga Zenodo 21549559 归档全量内容核验（12 件大文件按 R109 排除清单处理，是否必要）；② checkpoint 权重**分发条款**；③ natural clips **独立许可文本**。
- **锚点**：`gate-G0-R116/R116-ROUND-AUDIT.md:85`；`gate-G0-R115/R115-ROUND-AUDIT.md`（W2 范围收窄）；`gate-G0-R114/R114-ROUND-AUDIT.md:97`（第 24 行 Sintel asset+license PARTIAL）。
- **红线**：不得把代码 MIT / 公共下载 / 记录级 CC BY 自述外推为资产或权重授权（R114 D1「多端点一致≠独立核验」、R115 W2「字段≠文本」「代码许可≠权重许可」）。

## G6【gap 2】基线矩阵定稿 + SHA 重新冻结

- **现状**：`literature-baseline-matrix.md` 9,445 B 与 R106 freeze 字节一致；:46 `the open question`、:47 `Kuklev leaves` 两行 stale 表述仍在；:9 / :10 两处 `not yet verified` 原样保留。`gate-G0-R107/literature-baseline-matrix-R107-final.md` 为未签署 DRAFT。
- **锚点**：`gate-G0-R118/R118-ROUND-AUDIT.md:61`（点名四项之一）；`gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md:129`（W3）。
- **要决定**：是否授权矩阵定稿（并入 v2 §7.3/§8 的时间尺度 sweep、两个 v2 摘要并存事实，删除已被证伪表述）并重新冻结 SHA；由 designated gate owner 签署。

## G7【登记缺口】R4 指定登记 + CAPTCHA 条目处置 + 候选归类

- **内容**：① R106 §6 R4 指定的 `arXiv:2609.24565v2` SHA 冻结字节登记进 `literature-search/source-manifest.json`（11 轮未做）；② registry 第 5 条 `flyvis2024` 实为 reCAPTCHA 挑战页，处置方式；③ 26 个后缀筛选候选中 3 份 PDF 与 21 份未登记件的归类；④ R98「23 saved public sources」与 5 条 manifest 的口径矛盾如何裁定。
- **锚点**：`gate-G0-R118/R118-ROUND-AUDIT.md:60–62`；`gate-G0-R107/R107-ROUND-AUDIT.md`（R4）；`gate-G0-R106/R106-G0-INDEPENDENT-GATE-REVIEW.md:58`（W7）。
- **红线**：26 是后缀筛选候选数，**不等于 26 份已核验一手来源**；SHA 完整 ≠ 内容有效（R118 新教训）；心跳不自行回写 registry。

## G8【P3 前置】三项执行前提冻结为版本化执行契约

- **内容**（R117 首次一手实测暴露）：① 非官方 `version.py`（含逐字「NOT an official FlyVis file」）的可接受性与留痕；② MPS 显式 `.to("mps")` 适配 vs 上游全局 `set_default_device(cpu)`；③ 冻结 seed / 噪声（std .08、lower-clamp、4 draws）/ 零注入断言的可执行 runner。
- **锚点**：`exec-premise-R117/R117-ROUND-AUDIT.md:75`；`gate-G0-R118/R118-ROUND-AUDIT.md:62`；`ccfa-startup-packet/local-engineering-acceptance-v2.md`。
- **要决定**：由 designated gate owner **书面冻结为版本化执行契约**；在此之前**不在 G0 未过时启动 P3 前向**。心跳不自我认证、不自行冻结契约。

## G9【协议 / 版本化契约】哪一版 launch brief 治理 + 是否创建 v4

- **内容**：全项目 `independent-review-brief*` 中 `protocols/` 下仅 1 份（4,803 B / `8771dea8…`，`(Contract v2, R51)`），内含 `X > 8.0` / `exactly 8.0 does not qualify` / `score_gt_threshold = true` / 硬编码 `…20261108.md` / `8 pages`；`GOAL-ITERATION-R107.md:90–92` 把 `protocols/` 列为**故意不改的冻结契约**并点名「未来 v4 版本化契约可重述新判据」，但全项目 **v4 启动 brief = 0 份**。R95 用的是另一份 5,275 B FROZEN brief。
- **锚点**：`review-protocol-R119/R119-ROUND-AUDIT.md:54/57/121`；`GOAL-ITERATION-R107.md:90–91`；`R111-DECISION-READY-PACKAGE.md`（G1 DEPENDENCY）。
- **要决定**：① 由哪份 launch brief 治理；② 是否创建 R107 点名的 v4 契约（重述 `>=7.0`、现行 9 页编译与现行输出路径约定）；③ 技能引用路径只在**新**产物中更正、历史冻结件字节不改；④ 保留交接块「非锚定属性」逐字不变；⑤ 登记为**协议决定**而非证据。
- **红线**：心跳不自行创建 v4、不回溯改既有契约、不向评审透露期望分或分数锚点。

## G10【confirmation 面板】≤32h / K=45 授权（自 R99 待答复）

- **要决定**：是否授权 paper2 §7(b) 实验范围变更、正式 confirmation 面板。
- **锚点**：`R99-design-block-decision.md:50`（`BLOCKED_ON_CONFIRMATION`）、`:74`（`≤32h confirmation panel / K=45 formal family`）；`R111-DECISION-READY-PACKAGE.md:53`（D-5）；`state-handoff-R111/R111-ROUND-AUDIT.md:114`；`gate-G0-R114/R114-ROUND-AUDIT.md:48`；`gate-G0-R116/R116-ROUND-AUDIT.md:84`；`exec-premise-R117/R117-ROUND-AUDIT.md:75`；`gate-G0-R118/R118-ROUND-AUDIT.md:60`。
- **未答复前**：严格留在 development pilot；D1 判别性预测维持 `BLOCKED_ON_CONFIRMATION`，**不再出 v3**；心跳不擅自假定授权。

---

## 依赖顺序与最小裁决集

```
G1（交付对象/门路径）─┬─> G2（A6 sync）─┐
                     ├─> G3（阶段证据/台账/D5）─┤
                     └─> G9（launch brief 治理/v4）─┤
G4（G0 判据+独立判定方）─┬─> G5（gap1 三项）──────┼─> G8（P3 前置契约）─┬─> P3 真实前向
                        ├─> G6（gap2 矩阵）───────┤                      │   （须实质正向新证据）
                        └─> G7（R4/登记/归类）───┘                      │
G10（≤32h/K=45 面板）── 独立，但决定判别性预测能否出 v3 ────────────────┘
```

**最小可解锁集**：`G1 + G4 + G10` 三项裁决（分别解锁：门路径与验收机器门、G0 能否进入实质闭合、判别性预测是否继续）。其余 G2/G3/G5/G6/G7/G8/G9 均依赖或细化这三项。

---

## 心跳在未获批准期间的承诺

不跳动停止门、不改动成功标准（R107 终值 `>=7.0`）、不改任何门配置 / 评审 / 分数 / 稿件 / 冻结件 / 历史字节、不晋级任何门、不跳门、不为刷分对未修改稿件重复评审、不编造正向结果、不把工程验收或草稿脚手架包装成科学结果、不假定 confirmation 授权、不投稿 / commit / push（GitHub 同步仓库按 R109 授权除外）。

**只有** `failed_runs=0` + 全 finite + 独立复算吻合 + **实质正向新科学证据**，才会进稿件新副本 → 9 页合规编译 → 起全新隔离 full 评审（不透露期望分）→ 只有 `X >= 7.0` 且 QUALIFIED + COMPLETE 才写 COMPLETE。

---

**去重计数**：R111 5 项（D-1…D-5）+ R114 1 组（gap4/R7，并入 G4）+ R115/R116 1 组（gap1 三项，G5）+ R117 1 组（P3 前置，G8）+ R118 1 组（R4/CAPTCHA/归类/矩阵，拆为 G6 + G7）+ R119 1 组（launch brief，G9）+ R110 C5（并入 G1）+ R99（G10）⇒ **10 个去重决策组**。所有锚点经 `R120-verify.py` 75 检查 / 75 MATCH 独立复算。

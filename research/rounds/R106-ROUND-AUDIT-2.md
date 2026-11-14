# R106 轮次审计（2026-11-13 03:20–03:4x +0800，自动化 `b88e368e` 心跳）

状态：`ENGINEERING_ROUND_AUDIT_ONLY_NOT_SCIENTIFIC_RESULT`。

## 1. 并发保护（RGE4 第 0 步）

| 项 | 实测 |
|:--|:--|
| 唤醒时间 | `2026-11-13 03:20:22 +0800` |
| `goal-ledger.md` mtime | `2026-11-13 02:17:57`（距唤醒 **62 min** > 10 min） |
| 主会话 | `ps` 无其他 codebuddy 会话；唯一相关进程为本心跳自身（03:20 启动） |
| 近 20 min 顶层写入 | 仅 R105 收尾的 `correction-ledger.md`（02:18 前） |
| 异步 full 评审 | `ccfa-review-reports/` 最新仍 `r95`（11-11 15:01，`**Overall:** 6 \| **Scholarly Confidence:** 4`）；`ccfa-idea-review-reports/` 最新 11-10 → **无未登记异步 full 评审** |
| guard | `guard/reports/R95-check.txt` = `INCOMPLETE`（退出码 1），未变 |
| validator 只读复跑 | `NOT_QUALIFIED / overall_score 6.0 / all_pass=false`，D3 governing=6.0 |
| 结论 | **并发保护解除，主动推进**，记 R106 |

## 2. 第 1 步回收

23389 及以上**无新 Novix 任务/产物**：`novix/` 最新为 `r99b-23389-recovery`（11-12 18:50），
R101 已判 23389 `FINISH_INCOMPLETE`；23276 / 23341 / 23367 / 23278 均已处置。
不重开 Novix 派发、不做 identical retry、不 cancel、不删、不隐。

## 3. 换道原因（本轮核心判断）

R105 已判定连续 R101–R105 五轮「实现 → 验收脚本 → 独立核验 PARTIAL → 新 DEFER →
下轮补丁」为空转并**停止 predictor 验收脚本补丁循环**。用户指令明确
「按序推 G0–G8（每门各自实质证据与独立审查）」「别在提案文字上继续空转」。
本轮因此**回到主线第一门 G0**，做它的实质证据与独立审查，而非再出 v4 / v3 补丁。

另有一个只读盘点结论改变了执行判断：**主线真实前向的物理前提已齐备** ——
`rendered-attempt-1` 8 个 npz（4 场景 × 2 窗口）、`model000`/`model001` 官方目录、
`native_endpoint_intervention.py`、`competence_baselines_v1.py`、`local_budget_v2.py`、
`official-model-input-identities-v1.json` 全部存在；R101 已在本机 `ceg_snn_mi`
（Py3.11.15 / torch 2.13.0 / MPS）验证 `import flyvis` 与官方 checkpoint
`weights_only=True` 恢复。**瓶颈在门序与 G4 定位，不在缺数据或缺算力**。
这不解除任何门、不宣称 4090/L4 能力、不产生科学结果。

## 4. 实质工作（全部为 `gate-G0-R106/` 新文件，历史字节零改动）

| 产物 | 内容 |
|:--|:--|
| `R106-G0-EVIDENCE-FREEZE.json` | 8 份 G0 证据文件逐字节 SHA + `pipeline-state.json` 门状态快照；`gates_mutated=false` |
| `R106-G0-INDEPENDENT-RECENCY-VERIFICATION.md` | **本轮最关键发现**（见 §5）：一手复核 R99 全部 11 组数字 + 版本错配 + v2 新增时间尺度 sweep |
| `R106-G4-POSITIONING.md` | 按 `fail-fast-gates.md` §G4 写精确差异化陈述，四个阻塞维持不变，G4 风险**上调** |
| `R106-ASSET-SHA-VERIFICATION.json` | 8/8 Sintel clips SHA 从字节复算吻合；model000/001 各 5 文件 SHA；`chkpt_00000` SHA 与 `official-model-input-identities-v1.json` 声明值一致（`d0e42857…` / `d970fa9c…`） |
| `R106-LITERATURE-SOURCE-SHA-VERIFICATION.json` | 5/5 保存的一手文献 HTML bytes+SHA 与 `source-manifest.json` 声明吻合 |
| `R106-G0-GAP1-ASSET-CHECK.md` | R98 gap 1 逐条核查，如实区分 CLOSED / PARTIAL / OPEN |
| `R106-PRE-REVIEW-FREEZE.json` + `isolated/` | 独立审查落盘前 6 份产物逐字节冻结，隔离副本 6/6 一致（N1 纪律） |

## 5. 本轮最关键发现：**R99 的 G0 recency 结论是 stale 的**

### 5.1 R99 的数字没错

独立抓 `https://arxiv.org/html/2609.24565v2` 正文，R99 记录的
`0.857 / 0.539 / 0.586 / 0.500 / +0.318 [0.296,0.339] / 0.483→0.089 / 0.092 /
0.894 / 0.835 / 0.961 / 0.962` **逐条在 §7.1 / §7.2 / Table 3 找到一手出处并吻合**；
「held-out split 未用于 rewiring nulls」也吻合（§7.1 逐字 `on the development split,
since the held-out split was opened only for the model comparison`）。
**R99 没有编造，也没有混淆 split。**

### 5.2 但 R99 引用的是 **v1 结论**，v2 已修订

`/abs/2609.24565` 提交历史：`[v1] Mon, 21 Sep 2026 13:30:30 UTC`；
`[v2] Tue, 22 Sep 2026 12:24:47 UTC`，v2 为 `Major revision with a preregistered
held-out evaluation, matched graph nulls, temporal sampling controls, real-drawing
evaluation`。R99 引作结论的 *"Exact structure remains insufficient to beat what the
moving retina already provides"* 是 **v1 摘要**措辞；v2 摘要**不含该句**，改为：

> "Longer observations reverse the circuit-receptor ordering once the stimulus spans
> a period, but not through T4/T5. Thus active sampling and exact structure matter ..."

R99 标的是 `v2`，却用了 v1 的收束句，且**漏记 v2 新增的时间尺度 sweep**。

### 5.3 v2 §7.3/§8 已部分抢发 R99 建议的换道轴

R99 把「*A result that predicts **when** path-preserving controls matter*」列为开放问题
并建议换道。v2 §7.3 逐字给出答案：固定 pooled area 后，8 帧时 circuit 落后 `0.011`，
20/34/60 帧时领先 `0.018/0.021/0.022`，**跨过一个周期后排序反转**，
从 8 帧起变化 `+0.033 [0.015,0.050]`；频谱带各长度 `+0.085~+0.102`；
但 `the T4/T5 contribution does not grow with observation length`（`+0.008 [−0.003,0.018]`）。
§8 逐字：`That prediction was run, and it half held... The remaining question is which
stage integrates the extra time, and a per-type tuning analysis over the sweep would answer it.`

**后果（不淡化）**：判别变量、效应量、方向、阴性机制结论都已发表。
R99 建议的「判别性预测」轴不再是回答开放问题，而是复现并解释一个已发表、
且作者自称只 half held 的结果 ⇒ **G4 风险加重，不是减轻**。
`R106-G4-POSITIONING.md` 据此把风险由 R99 的 high 上调。

### 5.4 另两篇一手复核（均真实）

- Park 2026 `arXiv:2609.39248v1` + Zenodo 22891264 v4.0：十 seed 预注册、
  boundary-preserving null 使差异落入 `±0.10` 等价界、匹配 swap 数的 sham、
  **注册的 sham 等价预测失败并如实报告为失败**。
- Dhawan / FlyHack 2026 `arXiv:2610.13018`：flyvis 50-model 集成 + task-matched CNN，
  明确写 `the released flyvis models' launch-time split is not recoverable`，
  与本项目 TEST 标签扣留问题正面相撞。
- 2026 几何研究 secondary hit **本轮未复核**，保留 R99 状态，不宣称已验证。

## 6. 全新隔离独立 gate review（**运行中，verdict 待回收**）

已下发全新隔离 reasoning 子代理，不透露期望结论，要求：从 raw 独立复算 8 份 SHA、
独立抓 arXiv 一手来源复核 v1/v2 与 §7.3/§8、逐条判 R98 四个 gap CLOSED/OPEN、
主动构造反例、只写 `R106-G0-INDEPENDENT-GATE-REVIEW.md` 一个项目文件、
不产生分数行、不标任何门 passed。

**截至 03:4x 该报告未落盘，状态 `running`** → 按纪律
**安静等待、不重复启动、不自行打分、不预判 verdict、不催评**。
下轮第 1 步先回收，PASS / PARTIAL / FAIL 一律照原文登记、不删/藏/改，
并在账本 R106 段、STATUS、correction-loop-state、工作日志、run root
correction-ledger、本审计与本 automation memory 据实补录首行 verdict 与全部弱点。
该报告是**门审查**，不是 `ccf-paper-reviewer full` 稿件评审，
**不产生 `**Overall:**` 行、不改变 governing**。

## 7. 边界与红线（逐条）

- 全部产物 `*_NOT_SCIENTIFIC_RESULT`；**零前向 / 零训练 / 零标签 / 零数据集**；
  零 `pickle.loads`；纯只读 SHA 复算与文献核对。
- **未晋级任何门**：`pipeline-state.json` 实测 `CCFA-startup passed`，
  **G0–G8 / validation / handoff 全 pending**，P id 全缺失，冻结 runner 未运行；
  `pipeline_state.py --before G0` 返回 `PASS: ordered, current evidence;
  scientific/visual gate judgment remains required.`（rc 0），
  `--complete` 返回 `ERROR: delivery requires every stage passed`。
- **未标 G0 passed**：R98 明确写「Marking it passed from this review alone would
  violate 'Never skip, reorder, or infer completion' and would be stale-evidence
  promotion」；gap 1/2/4 未闭合。
- **governing 未变**：只读 validator `NOT_QUALIFIED / 6.0 / all_pass=false`；
  guard `R95-check.txt` = `INCOMPLETE`；`qualified_paper.json` 6.3 旧快照不刷新。
- 未改任何历史文件（R98/R99/matrix/冻结件/评审/稿件/分数/阈值/gate 状态）；
  R106 全部为新增补正文件；未自评当 governing；未起 `ccf-paper-reviewer full`；
  未跳门 / 批量标 passed / 静默改 codex stage / stale evidence 晋级。
- 未重开 D1 / 判别式预测 v3 补丁循环（保持 `BLOCKED_ON_CONFIRMATION`）；
  **未假定 ≤32h / K=45 confirmation 面板授权**；未出 predictor v4。
- 未投稿 / commit / push（`git rev-parse` 确认路径链无 `.git` 仓库）。
- 心跳 ACTIVE，**本轮无调度参数变化** → 按纪律未改调度。

## 8. 结果

**0 篇达标，未写 COMPLETE**。停止门只剩 ①达标 ②用户叫停。
governing 仍 R95 独立 full 评审 **6.0 / Confidence 4.0**。

## 9. 交下轮（优先级）

1. **第 1 步先回收 `R106-G0-INDEPENDENT-GATE-REVIEW.md`**：verdict 照原文登记，
   PASS/PARTIAL/FAIL 一律不删/藏/改；按 Concern-to-action 处理其 W 编号，
   不写补丁式文字修复、不把 PARTIAL 当分数下降或「已通过」。
2. 按 `R103-PIPELINE-STATE-ID-GAP.md` / U6 / W2 以**版本化契约**处理
   guidance handoff → f-research-v1 P0 state 初始化（新建 f-research-v1 state，
   **不往 guidance state 塞 P 阶段**）。
3. 按序 G1–G8 逐门实质证据与独立审查（G4 须正面处理本轮发现的
   Kuklev v2 时间尺度 sweep）；→ validation → handoff → P0 → P1A/P1B → P2
   → P3 baseline-first（真实前向，正面解决 U5，本机 MPS 需显式迁移）。
4. 只有 `failed_runs=0` + 全 finite + 独立复算吻合 + **实质正向新证据**，
   才进稿件新副本目录、9 页合规编译、起全新隔离 full 评审（不透露期望分）；
   X>8.0 且 QUALIFIED+COMPLETE 才写 COMPLETE。
5. 用户决策点（≤32h / K=45 confirmation 面板授权）仍待答复，不擅自假定。

---

## 10. 收尾补录（03:55，只追加不改写上文）

独立 `R106-G0-INDEPENDENT-GATE-REVIEW.md` **至 03:55 仍未落盘**，子代理状态 `running`。
按 R103 先例与红线「不催评 / 不重复启动 / 不自行打分 / 不预判 verdict」，
本轮**安静收尾**，verdict 明确交给**下轮第 1 步**回收并据实补录。

- `R106-END-OF-ROUND-FREEZE.json`：7 份产物逐字节冻结，隔离副本 7/7 一致；
  字段 `independent_gate_review_landed=false`、
  `independent_gate_review_status=RUNNING_DEFERRED_TO_NEXT_ROUND`；
  `R106-PRE-REVIEW-FREEZE.json` **原样保留、未改写**。
- 收尾终检（只读）：`pipeline-state.json` = `CCFA-startup passed`，
  **G0–G8 / validation / handoff 全 pending**（一门未晋级）；
  validator `NOT_QUALIFIED / 6.0 / all_pass=false`；guard `INCOMPLETE`。
- 本轮**零科学结果**、零前向/训练/标签、零门晋级、零分数/阈值/评审/稿件/冻结件改动；
  未起 `ccf-paper-reviewer full`；未投稿/commit/push；心跳 ACTIVE 无调度参数变化。
- `goal-ledger.md` mtime 已刷新为 `03:48:52` → 30 分钟内再次触发属预期，只做只读检查。

**结果不变：0 篇达标，未写 COMPLETE。governing 仍 R95 = 6.0 / Confidence 4.0。**

---

## 11. 独立 gate review 回收（03:5x–04:0x，只追加；**上方 R106 段的核心发现已撤回**）

`R106-G0-INDEPENDENT-GATE-REVIEW.md`（189 行 / 31,292 B，SHA `919d05c4…7450`）已落盘。
首行逐字：**`**Verdict:** PARTIAL | **G0 may be passed:** NO`**，次行
`**Scientific result claimed:** NO`。全新隔离 reasoning 子代理，从原始字节重算 SHA、
自己抓一手来源、未采信 R106 任何转述。**报告原文未改一个字节**。

**⚠️ 更正（必须优先于上文 §5 阅读）**：上文 §5.2 / §5.3 与
`R106-G0-INDEPENDENT-RECENCY-VERIFICATION.md` §3.1 的「R99 引用 v1 摘要、版本错配」
**核心指控不成立，已撤回**。主会话用一手来源交叉核验确认：

- `/abs/2609.24565v1` 摘要收束为 `while the topology contribution and end-to-end BIM utility remain open questions.`，**不含** `Exact structure remains insufficient…`；
- `/html/2609.24565v2` **论文正文 Abstract 块**最后一句**就是**
  `Exact structure remains insufficient to beat what the moving retina already provides.`；
- `/abs/2609.24565` **元数据摘要**含 `Longer observations reverse the circuit-receptor ordering once the stimulus spans a period, but not through T4/T5.`

⇒ **arXiv 上并存两个措辞不同的 v2 摘要**；R99 引的是 v2 论文正文摘要，**引用正确**。
是我把元数据摘要当成唯一的「v2 摘要」而误判。该错误已扩散到 6 处登记，
按 RGE 纪律**不改写历史字节**，只以本补录 + 各处追加段更正。
另更正：Park Zenodo 一手 Comments 为 DOI `10.5281/zenodo.22871090`（非 `22891264`）；
Dhawan 一手提交日 `Fri, 9 Oct 2026`（非 10-12）。详见
`R106-INDEPENDENT-REVIEW-RECOVERY.md` §1。

**G4 结论保留、论据更正**：独立审查 §5 判定中心判断 **defensible**，并逐字确认
v2 §7.3/§8 的 `+0.033 [0.015,0.050]`、跨周期排序反转、不经 T4/T5、
`That prediction was run, and it half held.` ⇒ 「判别性预测何时路径重要」轴
**已被部分抢发、G4 风险上调**独立成立；但支撑它的「版本错配」论据已撤回。
G4 维持 `pending`。

**W9 失配确认**：`R106-END-OF-ROUND-FREEZE.json` 声明 7/7 一致为假 ——
`R106-ROUND-AUDIT.md` 声明 `10457 B / 06299a15…`、实际 `11743 B / 772036905e…`
（§10 追加后未同步冻结）。主会话独立复算属实。按 N1 纪律不补造、不改写旧清单，
只新增 `R106-POST-REVIEW-FREEZE.json`；这是同类登记缺陷**第三次出现**
（R104 N1、R105 W11），如实累计。

**R98 四 gap 判定**：gap 1/2/4 **OPEN**（gap 2 已恶化：矩阵仍含已被证伪的
「open question Kuklev leaves」）；gap 3 **PARTIAL**。另 W13：
`fail-fast-gates.md` **根本没有 G0 的成文 pass criterion**。
W1–W13 / R1–R9 的处置见 `R106-INDEPENDENT-REVIEW-RECOVERY.md` §3。

**性质界定**：门审查，**不是** `ccf-paper-reviewer full` 稿件评审 → 无分数行、
**不改 governing**；PARTIAL **不是 FAIL**（8/8 SHA、12/12 门状态、旁证全真，类别 A 零项）。
裁决 **G0 维持 `pending`，不得标 PASSED**，本轮遵守。

**终检**：`pipeline-state.json` G0–G8/validation/handoff 全 pending、P id 全缺失；
validator `NOT_QUALIFIED / 6.0`、guard `INCOMPLETE`；零前向/训练/标签、
零门晋级、零分数/阈值/评审/稿件/冻结件改动、未起新 full 评审、
未重开 D1/v3、未出 v4、未假定 confirmation 授权、未投稿/commit/push。
**0 篇达标，未写 COMPLETE**，governing 仍 R95 = 6.0 / Confidence 4.0。

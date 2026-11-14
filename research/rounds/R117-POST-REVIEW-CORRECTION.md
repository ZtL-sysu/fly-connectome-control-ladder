# R117 独立审查回收 — 只追加更正登记

**日期**：2026-11-14 03:3x +0800
**独立报告**：`R117-INDEPENDENT-REVIEW.md` — 最终 **22,725 B / SHA256 `0d133eaca0684bc61b927378923aaf09489adb6e33b979b8c4e9be33df030a3b`**（mtime 03:30:17），首行
`**Verdict:** PARTIAL | **G0 may be passed:** NO | **Scientific result claimed:** NO`、次行 `**Forward pass performed:** NO`。
**原文零改动**（主会话未输入预期结论；本登记为唯一新增文件，不改写独立报告一字）。

> 本文件为 **只追加** 更正登记。`R117-EXEC-PREMISE-EVIDENCE.md`、`R117-EXEC-PREMISE-RAW.json`、
> `R117-EXEC-PREMISE-VERIFICATION.json`、`.v1-superseded.json`、`R117-SOURCE-MANIFEST.json`、
> `R117-probe.py`、`R117-verify.py`、`R117-ROUND-AUDIT.md` 的历史正文 **一律不改写**；
> 账本 / STATUS / 工作日志 / 轮次审计均以「追加更正段」处理。
> 独立报告是**门 / 证据层复核**，不是 `ccf-paper-reviewer full` 稿件评审：无 `**Overall:**` 行、
> 无数值论文分、不改 governing。

## 1. 独立复核结论（照录，不美化）

- 12 类点名夸大 / 自我认证 (a)–(l) **CONFIRMED = 0，全部 REFUTED**。唯一如实保留的局部例外是 (h) 的
  **v1 假阴性留痕**（把本机路径误计入凭证判定），该留痕已由最终版拆分修正、且从未作为最终结论。
- 从磁盘字节独立重算：**19/19 sources + 6/6 artifacts 双吻合**；8/8 Sintel npz SHA 与 R106 声明一致、
  zip CRC / `testzip` 通过；官方 checkpoint `d0e42857…ccc3f` / `weights_only=True` → `dict{network,decoder}` /
  14 张量 / 全 finite；**两种分帧规则独立复算**得 `67ce06c5…a82` 与 `bd3f2cc8…5e74`，证实同一批字节的分帧差异；
  主线 `pipeline-state.json` = `bcb48bb9…a33d` / 3,723 B，G0–G8 / validation / handoff **全 pending**。
- **7 组 import 结论独立复现**：5 FAIL / 2 OK，成功组 `flyvis.device = cpu`，上游 `__init__.py:13-14` 无 mps 分支；
  `version.py` 逐字含 `NOT an official FlyVis file`。
- **状态重判**：G0 **不得 pass（NO）**、**不构成实质正向新科学证据（NO）**、**维持 pending（YES）**。
  Verdict `PARTIAL` 的理由：核心实测 100% 独立复算吻合、无造假 / 无越界 / 无夸大，但存在 §6 五处低 / 低-中瑕疵，
  且按设计本轮本就不构成 G0 pass / 科学结果 / 前向。
- **内容安全**：14 类凭证严格模式 **0 命中**；本机路径 25 处（配置事实，与凭证严格分开）；
  明确要求公开 GitHub 同步副本全部脱敏 `<local>/`（R109 红线，本轮已执行）。

## 2. 逐条接受 5 处瑕疵（按独立报告 §6）

| # | 严重度 | 独立审查发现 | 本轮处置 |
|:--|:--|:--|:--|
| 1 | **低-中** | 「按 R101 原规则复算 digest = `67ce06c5…a82` MATCH」**缺一手落盘件**：RAW.json 唯一 digest 字段是 `bd3f2cc8…`、probe 脚本仍用带尾部 `\0` 的规则、verify 45 项无 digest 一致性项 ⇒ 该行是**文本断言**，属证据链 / 可复算性缺口（数值本身经审查独立复算正确，**非数据错误、非造假**） | **接受**。新增 `R117-digest-r101.py` + `R117-DIGEST-RECOMPUTE.json`（2,072 B / `1d724e96…`），从磁盘 checkpoint 用**两种分帧**独立重算：R101 原规则 `67ce06c5…a82` MATCH、probe 变体 `bd3f2cc8…5e74` MATCH，同一 14 张量 / 44,552 B 原始字节、`both_match=true`。↳ **这是补一手可复算件，不是文字补丁**；不改写历史字节、不改任何脚本原规则、不晋级任何门 |
| 2 | 低 | `R117-EXEC-PREMISE-EVIDENCE.md:85`「本轮 12 份源字节」措辞错误：`R117-SOURCE-MANIFEST.json` 实为 **19 份 sources**，RAW.json 的 `source_manifest[]` 才是 12（4 非 clip + 8 clip） | **接受并收窄**：准确口径为「`SOURCE-MANIFEST.json` 登记 **19** 份源；`RAW.json` 内 `source_manifest[]` 为 **12** 份（4 非 clip + 8 clip）」。原文不改写，以本登记为准（文档笔误，不影响字节结论） |
| 3 | 低 | `R117-ROUND-AUDIT.md:44` 的 VERIFICATION.json SHA 转录为 **63 位错值** `aa1372d2bb91e4bc…625946a`（漏 `f`） | **接受并更正**：磁盘实测为 64 位 **`aa1372d2bbf91e4bc5127d636dac00cbfc7de7942253ca714895a7fed625946a`**（9,552 B）。`R117-SOURCE-MANIFEST.json` 登记值与 EVIDENCE.md:92 前缀 `aa1372d2…` 均正确。原文不改写，以本登记为准 |
| 4 | 信息性 | `R117-SOURCE-MANIFEST.json` 未登记第 7 份产物 `R117-ROUND-AUDIT.md`（manifest 生成于 03:19，审计于 03:22 新增） | **接受（时序快照，非数据矛盾）**。主会话已于 03:27 在 `R117-ROUND-AUDIT.md` §4 **只追加**「快照边界如实登记」段，明确 manifest 的 6 份 artifacts 是 03:19 生成时刻快照、不含之后新增的轮次审计与独立审查报告、不得把 6/6 吻合外推为全目录已登记。manifest 原字节**不改写**（不可回写式补丁） |
| 5 | 低 / 信息性 | EVIDENCE.md:72「官方 meta **单行** `seed: 0`」措辞不严谨，`_meta.yaml` 实有 **2 行** `seed: 0`（第 25、108 行），RAW.json `clause_lines` 亦如实列 2 行 | **接受并收窄**：准确为「官方 `_meta.yaml` 含 **2 处** `seed: 0` 行（第 25、108 行），均只读，未建立冻结 seed 集」。不构成 (j) 夸大（产物已明确 `NOT_ESTABLISHED` / 零校准运行），仅表述不精确 |

| 6 | 低 / 子代理自报 | 独立报告 **§0 引用了 2 个 conda 真实本机绝对路径**，与 §5「本独立报告正文已以身作则，全部以 `<local>/` 代替」措辞略不自洽；子代理按「一次落盘、原文不再改动」未回改，已透明登记 | **接受**。独立报告原文 **零改动**（不改写一字，保持 mtime 03:30:17 / `0d133eac…`）；准确口径为「报告 §5 扫描结论针对**主项目产物 8 份文件**、不含报告自身；报告自身另有 2 处本机路径」。⇒ 公开仓库 **不上传独立报告原文**，只放脱敏摘要（`R117-INDEPENDENT-REVIEW-SANITIZED.md`）；主项目目录本机路径计数由 25 更新为 **27**（25 + 报告自身 2），**凭证类仍 0 命中**（R115 W2：本机路径在主项目内部是配置事实、不可外推全局，公开副本一律 `<local>/`） |

**6 处均不改变**「字节完整性成立、非科学结果、不晋级 G0、无前向」的核心判定；无一处涉及伪造或数据不一致。

## 3. 并发条件（R115 同类，如实登记）

独立审查窗口内，主会话曾并发追加 `R117-ROUND-AUDIT.md` §4 的快照边界段（03:27，8,082→8,410 B）、
写账本 R117 段（03:22:47）、STATUS / 工作日志（03:23:08），并完成第七次 GitHub 同步（远端 `1caf00c6…`）。
审查报告 §5 逐字记录其扫描到的是 **03:22 版 8,082 B / `76d0c8b7…`** 的 `ROUND-AUDIT.md`，
并注明「非本代理创建、本代理未改动」。按 R106 §6 R9：主会话自我更正 **不构成** gap 闭合的自我认证，
**不改** `pipeline-state.json` 字节与独立报告首行 verdict。
审查报告 §5 亦逐字说明 17 / 19 / 23 / 25 四处本机路径读数的差异源于**扫描文件集合时序变化**与模式类数不同，
**不是伪造或矛盾**；本登记不重写任一读数。

## 4. 独立报告读数时点纪律（R115 ② 教训）

本轮于 03:30:26 首次读到 **22,725 B / `0d133eac…`**（mtime 03:30:17），随后 03:30:50 复核
bytes / SHA / mtime **完全一致**，且报告 §7 明载「一次落盘、原文不再改动」，结构 §0–§7 完整。
**子代理最终交付消息（03:3x，历时 12m07s）明确确认**：报告最终 22,725 B /
`0d133eaca0684bc61b927378923aaf09489adb6e33b979b8c4e9be33df030a3b`、
mtime 03:30:17、**无中间态、原文不再改动**；报告 §1.2 亦自行确认「6/6 吻合、未采信自报值」。
⇒ **以该最终落盘读数为唯一准**（与 R114/R115/R116 的「中间态 + 最终态双 SHA」不同：本轮确无中间态，故无第二版 SHA 需保留）。
子代理另主动披露第 6 处自身瑕疵（见 §2 表），已一并只追加登记；报告原文仍零改动。

## 5. 已发布检查点与本登记的关系（R109）

第七次同步的检查点 `20261113T192349Z-r117-exec-premise` 在 **03:30 前**写入与推送，
其 CHECKPOINT.md 与脱敏摘要均已如实标注「独立复核已下发、**写时点未回收**、不宣称任何结论」。
⇒ 已发布的 6 个历史检查点 + 本轮第 7 个检查点 **零改动**（不可覆盖），标注在写时点为真、无需回写。
本更正登记及其补充一手件属**主项目只追加**；独立审查结论与更正按 R109 在**本轮新建第 8 个不可覆盖检查点**同步
（`20261113T193xxxZ-r117-post-review`），不改写任何已发布字节。独立报告原文含 2 处本机路径，**不直接上传**，
公开副本只放脱敏摘要。

## 6. 结果与边界不变

- **G0 维持 `pending`**、gap 1 整体 **PARTIAL**；零门晋级 / 零自我认证 / 零状态改动（主线 `pipeline-state.json` 字节未改）。
- 第 3 步前置（**实质正向新科学证据**）未满足 ⇒ 不进稿件新副本、不做 9 页编译、不起全新隔离 `ccf-paper-reviewer full` 评审。
- **0 篇达标，未写 COMPLETE**，governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`。
- 未改历史字节 / 评审 / 分数 / 阈值 / 稿件 / 门 / 冻结件 / 矩阵 / 门配置；未自评 governing、未跳门、
  未对未修改稿件重复评审；未假定 `≤32h / K=45` confirmation 授权；EXEC LOCK；无 4090 能力主张；
  主项目未投稿 / commit / push；心跳 ACTIVE 调度无变化。
- 停止门只剩 ①达标（>= 7.0）②用户叫停。

## 7. 交下轮（在 R117 §6 基础上追加）

1. 按 R109 把本更正登记、补充一手件与独立审查最终结论同步为**新的不可覆盖检查点**（含内容扫描 + `git ls-remote` 核对），
   已发布的 7 个检查点零改动。
2. 独立审查 §6 第 1 项建议已由 `R117-DIGEST-RECOMPUTE.json` 闭合；下轮可把该值作为 verify 的独立检查项
   （**须新建版本化检查，不改写 `R117-verify.py` 原字节**）。
3. 其余沿用 R117 §6 交下轮清单：不执行须批准的机器门修复；三项 P3 前置须 designated gate owner 书面冻结；
   gap 1 剩余三项维持 R116 判定；按序 G0–G8 → validation → handoff → P0 → P1A/P1B → P2 → P3 真实前向解决 U5；
   只有 `failed_runs=0` + 全 finite + 独立复算吻合 + 实质正向新证据才进稿件新副本 → 9 页编译 → 全新隔离 full 评审；
   **X >= 7.0** 且 QUALIFIED + COMPLETE 才写 COMPLETE。

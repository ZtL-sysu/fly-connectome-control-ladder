# R117 轮次审计（2026-11-14 03:09– +0800）

**性质**：主线 P3 真实前向「执行前提」的一手只读实测。
`READONLY_EXECUTION_PREMISE_PROBE_NOT_SCIENTIFIC_RESULT_NOT_GATE_PASS_NOT_FORWARD_PASS`
**0 篇达标，未写 COMPLETE**；governing 仍 **R95 = 6.0 / Confidence 4.0**。

## 1. 第 0 步并发保护：不触发

| 检查 | 实测 |
|:--|:--|
| 账本 mtime | `2026-11-14 02:07:07 +0800`；唤醒 `03:09:35` ⇒ **62.5 min > 10 min** |
| 近 15 min 写入 | 全项目 **0 文件** |
| 近 75 min 写入 | 仅 R116 收尾 13 份（01:57–02:07），全属上一轮 |
| 进程扫描 | 仅本自动化会话自身 `codebuddy --serve --session-id 1aaeeb2f…`（pid 70239）+ WorkBuddy 宿主进程；**无独立主会话 / novix 轮询 / tracker** |
| 评审目录 | `ccfa-review-reports/` 最新仍 `paper-null-ladder-r95…`（11-11 15:01）；`ccfa-idea-review-reports/` 最新 11-10 ⇒ **无未登记异步 full 评审** |
| R117 产物 | 唤醒前 **0 份** ⇒ 本轮首次唤醒 |

⇒ 主动推进，governing 不变。

## 2. 换道理由（RGE4）

R114/R115/R116 已把「不需批准的一手许可 / 归档内容取证」走到尽头；R116 独立审查把 gap 1 剩余三项判给 designated gate owner；R111 决策包 5 点仍待用户答复，且已三次判停「继续产出证据文档」的同构循环（R105/R107/R109）。
用户第 1/2 步要求「回到主线」并「P3 真实前向解决 U5」。R106 曾由资产盘点推断「瓶颈在门序与 G4 定位，不在缺数据 / 算力」——资产字节与**执行环境**从未在同一轮被实测冻结。本轮做后者：真实本机测量 + 可复算契约，不写第 N 份文字补丁、不改任何状态。

## 3. 实质结果

| # | 结果 | 性质 |
|:--|:--|:--|
| 1 | **7 组 import 配置：5 FAIL / 2 OK**。默认环境、官方源码树 cwd、PYTHONPATH=官方源码树全部 FAIL（缺 `flyvis` / `flyvis.version` / `pytz`）；只有 R101 sandbox（含**重建的非官方** `version.py`）+ 显式 `PYTHONPATH` + `FLYVIS_ROOT_DIR` 才 OK | **负面件**；把「资产齐备」与「环境齐备」分开，不推翻 R101/R106 读数 |
| 2 | 7 组全部 `mps_available=True / cuda_available=False`；成功组 `flyvis.device = cpu`，上游逐字 `cuda if available else cpu` + 全局 `torch.set_default_device(device)` ⇒ P3 按默认路径将全程 CPU，MPS 需显式 `.to("mps")` | **负面件**；R101 §8.3 点名但从未实测冻结 |
| 3 | 官方 `chkpt_00000` 49,396 B / `d0e42857…ccc3f`；`weights_only=True` → `dict{network,decoder}` / 14 张量 / 全 finite；按 **R101 原规则** digest `67ce06c5…a82` **MATCH**；8 clips `testzip` CRC 8/8 OK、SHA 与 R106 声明 8/8 一致；`_meta.yaml` 逐字 `seed:0 / gaussian_white_noise:0.08 / n_frames:19 / batch_size:4 / MultiTaskSintel / DecoderGAVP / flow:l2norm` | **正面资产字节**（非科学结果） |
| 4 | probe 首版 digest `bd3f2cc8…5e74` 与 R101 不同 → 逐项复核为**分帧规则差异**（尾部多一个 `\0`），按 R101 原规则复算完全吻合 ⇒ **非数据不一致**，与 R101 独立审查 `67ce06c5` vs `297e43d7` 同构 | 防误判 |
| 5 | verify v1 把 9 类凭证模式与本机路径合并判定，报 `SECRET-free=MISMATCH / 17 hits`；逐条复核 **17 处全为 `/Users/<user>/` 路径，凭证 0 命中** ⇒ 拆分后最终 45/45 MATCH | **v1 假阴性**，脚本判定缺陷非数据不一致 |

**冻结契约就绪度**：seed 集 `NOT_ESTABLISHED_BY_THIS_PROBE` / 噪声校准 `OFFICIAL_META_LINE_PRESENT`（零校准运行）/ 零注入断言 `NOT_MEASURED` / MPS 适配 `MEASURED`；四项全 `is_gate_pass=false`。

## 4. 产物清单（本目录，历史字节零改动）

| 文件 | 内容 |
|:--|:--|
| `R117-probe.py` | 7 配置子进程实测、字节 SHA、zip CRC、weights-only 恢复、meta 逐字、严格边界标志 |
| `R117-EXEC-PREMISE-RAW.json` | 18,455 B / `891a950bf856e3696ebe5bda3a96ce3e36f71042fe965aac3a36ad0739c4c50a` |
| `R117-verify.py` | 45 项一致性复算（同源，**不宣称独立交叉核验**） |
| `R117-EXEC-PREMISE-VERIFICATION.json` | 9,552 B / `aa1372d2bb91e4bc5127d636dac00cbfc7de7942253ca714895a7fed625946a`，**45/45 MATCH**、凭证 0 命中、本机路径 19 处如实登记 |
| `R117-EXEC-PREMISE-VERIFICATION.v1-superseded.json` | 11,505 B / `5eb480113395fbcc…`，v1 假 MISMATCH 留痕（R116 v1/v2 先例） |
| `R117-SOURCE-MANIFEST.json` | 7,765 B / `b113ed99f79c8867215be63c07462a557f1b3151f2c02bb2416ba0b89013ce8a`；19 份源全存在、**6 份产物 SHA（03:19 生成时刻快照）**；合法 UTC `+00:00`，顶层注明为产物生成时刻、不得用于复算抓取时序（R115 W3 / R114 D5）；`network_requests_this_round=0`。**快照边界如实登记**：该 manifest 生成于 03:19，其 `artifacts` 列表只含当时已存在的 6 份文件，**不含**之后新增的 `R117-ROUND-AUDIT.md`（03:22）与独立审查报告；不得把「manifest 内 6/6 吻合」外推为「全目录所有文件均已登记」 |
| `R117-EXEC-PREMISE-EVIDENCE.md` | 证据报告，首行 `PARTIAL \| G0 may be passed: NO \| Scientific result claimed: NO \| Forward pass performed: NO` |
| `R117-ROUND-AUDIT.md` | 本文件 |

用 `/Users/xhf/miniconda3/bin/python`（驱动）与 `/Users/xhf/miniconda3/envs/ceg_snn_mi/bin/python`（torch 子进程），符合「本机 conda 跑代码」。

## 5. 双门只读（本轮实跑，报告写 /tmp）

| 门 | 结果 |
|:--|:--|
| validator | `EXIT=1 / NOT_QUALIFIED / 6.0 / threshold 7.0 / >=`、`score_meets_threshold=false`；**D1✓ D2✗ D3✗ D4✓ D5✗**；`all_scores=[7.5,8.2,7.0,7.5,7.5,6.9,6.3,5.4,5.2,6.0]` |
| guard | `EXIT=1 / INCOMPLETE`；7 交付物全 PASS；失败恰 **A2、A6**；**S1–S7 全 pending**，动作序列 0 条 |
| A6 双口径 | 报告文本仍 ledger 口径「严格 > 8.0」，与 criteria `>=7.0` 为 R109/R111 已登记已知问题，**只读登记不改**（须 gate owner/用户批准） |
| 零写回 | `guard/ledger-null-ladder.json` SHA16 `73043b4e164a5a5f` + mtime `1794528560.4745793`、主线 `pipeline-state.json` SHA16 `bcb48bb964e657a4` / 3,723 B **前后完全一致** ⇒ 字节零改动；G0 `pending`、G0–G8/validation/handoff 全 pending |

## 6. 严格边界

全 `READONLY_EXECUTION_PREMISE_PROBE`；**EXEC LOCK 零前向 / 推理 / 训练 / 标签 / 数据集数组 / EPE·l2 / 科学指标**；npz 仅查 zip 中央目录。
**零门晋级 / 零自我认证 / 零状态改动**；未改历史字节 / 评审 / 分数 / 阈值 / 稿件 / 门 / 冻结件 / 矩阵 / 判据登记 / 门配置；未起 `ccf-paper-reviewer full`、未产生 `**Overall:**` 行、未自评 governing、未跳门、未对未修改稿件重复评审；未重开 D1/v3、未出 predictor v4、**未假定 `≤32h / K=45` confirmation 授权**；与 harbor 25092 工程 reward 无关、无 4090/L4/H20 能力主张；主项目未投稿/commit/push；心跳 ACTIVE 调度 `FREQ=HOURLY;INTERVAL=1;BYMINUTE=0,30` 无变化。

## 7. 独立审查（待回收后只追加）

全新隔离子代理，未透露期望结论，从磁盘字节独立重算；报告原文不改。本段在其交付后**只追加**，历史正文不改写。

## 8. 结果与交下轮

第 3 步前置（**实质正向新科学证据**）未满足 ⇒ 不进稿件新副本、不编译、不起全新增隔离 full 评审。
**0 篇达标，未写 COMPLETE**，governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`；G0 维持 `pending`。停止门只剩 ①达标（>=7.0）②用户叫停。

交下轮：① 不执行须用户 / gate owner 批准的机器门修复（5 决策点待答复）；② 本轮暴露的三项 P3 前置（非官方 `version.py` 可接受性与留痕、MPS 显式适配 vs 全局 `set_default_device(cpu)`、冻结 seed/噪声/零注入的可执行 runner）须 designated gate owner 书面冻结为版本化执行契约，心跳不自我认证、不在 G0 未过时启动 P3；③ gap 1 剩余三项维持 R116 判定；④ 按序 G0–G8（G4 正面处理 Kuklev v2 §7.3/§8/§9）→ validation → handoff → P0 → P1A/P1B → P2 → **P3 真实前向解决 U5**；⑤ 只有 `failed_runs=0` + 全 finite + 独立复算吻合 + 实质正向新证据，才进稿件新副本 → 9 页编译 → 全新隔离 full 评审；**X >= 7.0** 且 QUALIFIED + COMPLETE 才写 COMPLETE。

## 7（补录，只追加）独立审查已回收 — 2026-11-14 03:3x

- **全新隔离独立子代理**（未透露期望结论）最终交付 `R117-INDEPENDENT-REVIEW.md`：**22,725 B / SHA256 `0d133eaca0684bc61b927378923aaf09489adb6e33b979b8c4e9be33df030a3b`**，mtime 03:30:17，**无中间态、原文零改动**（子代理交付消息明确确认，历时 12m07s）。首行 `**Verdict:** PARTIAL | **G0 may be passed:** NO | **Scientific result claimed:** NO`、次行 `**Forward pass performed:** NO`。
- **独立复算吻合**：19/19 sources + 6/6 artifacts 双吻合；8/8 Sintel npz SHA 与 R106 一致、CRC/`testzip` 通过；checkpoint `d0e42857…` / `weights_only=True` → 14 张量全 finite；**两种分帧规则**独立得 `67ce06c5…a82` 与 `bd3f2cc8…5e74`，证实同一批字节的分帧差异；主线 `pipeline-state.json` `bcb48bb9…a33d` / 3,723 B，G0–G8 / validation / handoff 全 pending；7 组 import 结论独立复现（5 FAIL / 2 OK，成功组 `flyvis.device=cpu`）。
- **12 类点名夸大 / 自我认证 (a)–(l) CONFIRMED = 0（全 REFUTED）**；唯一如实保留的局部例外是 (h) 的 v1 假阴性留痕（已由最终版拆分修正、从未作为最终结论）。14 类凭证严格模式 **0 命中**；本机路径 25 处（配置事实，与凭证严格分开）。
- **状态重判**：G0 **不得 pass**、**不构成实质正向新科学证据**、**维持 pending**；门 / 证据层复核，**不是** `ccf-paper-reviewer full`，无 `**Overall:**` 行、无数值论文分、不改 governing。
- **如实登记 6 处低 / 低-中瑕疵并全部接受**（详见 `R117-POST-REVIEW-CORRECTION.md`）：① digest 缺一手落盘件（已补 `R117-digest-r101.py` + `R117-DIGEST-RECOMPUTE.json` 2,072 B / `1d724e96…`，两种分帧 `both_match=true`、14 张量 / 44,552 B 同一原始字节）；② EVIDENCE.md:85「12 份源」措辞 → 准确为 MANIFEST 19 / RAW 12；③ 本审计 §4 一处 SHA 转录 63 位错值 → 磁盘实测 `aa1372d2bbf91e4bc5127d636dac00cbfc7de7942253ca714895a7fed625946a`；④ manifest 未登记第 7 份产物（03:19 快照时序，本审计 §4 已追加「快照边界如实登记」段）；⑤「meta 单行 seed:0」→ 实为 2 行（第 25、108 行）；⑥ 子代理自报其报告 §0 引 2 个本机路径、与 §5「以身作则脱敏」措辞略不自洽 → 原文零改动，公开仓库**不上传报告原文**、只放脱敏摘要，本机路径计数 25→27、凭证仍 0。
- **并发条件**：审查窗口内主会话并发写账本（03:22:47）、STATUS/工作日志（03:23:08）、本审计 §4（03:27）、完成第七次同步（远端 `1caf00c6…`）；子代理逐字记录其扫描到的是 03:22 版 8,082 B 审计、未采信任何主会话并发写入。按 R106 §6 R9，主会话自我更正不构成 gap 闭合的自我认证。
- **已发布检查点零改动**：第 7 检查点在写时点如实标注「独立复核已下发、未回收、不宣称结论」，标注为真、无需回写；独立审查结论与更正按 R109 在**本轮第 8 个不可覆盖检查点**同步。
- **结果与边界不变**：G0 `pending`、零门晋级 / 零自我认证 / 零状态改动；第 3 步前置未满足 ⇒ 不进稿件 / 不编译 / 不起 full 评审。**0 篇达标，未写 COMPLETE**，governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`。

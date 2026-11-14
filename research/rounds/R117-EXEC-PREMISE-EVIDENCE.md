# R117 — 主线 P3 真实前向「执行前提」的一手实测（只读）

**Classification:** `READONLY_EXECUTION_PREMISE_PROBE_NOT_SCIENTIFIC_RESULT_NOT_GATE_PASS_NOT_FORWARD_PASS`
**首行判定:** `PARTIAL | G0 may be passed: NO | Scientific result claimed: NO | Forward pass performed: NO`
**日期:** 2026-11-14 03:1x +0800（唤醒 03:09:35）
**执行:** `/Users/xhf/miniconda3/bin/python`（驱动）＋ `/Users/xhf/miniconda3/envs/ceg_snn_mi/bin/python`（子进程实测）

> 本文件是**工程/门层实测**，不是 `ccf-paper-reviewer full` 稿件评审，不含 `**Overall:**` 行、不含数值论文分、不改 governing。
> 全程 EXEC LOCK：**零前向、零推理、零训练、零标签读取、零 EPE/l2 计算、零科学指标、零门晋级**。npz 仅查 zip 中央目录（文件名 / CRC / 未压缩字节数 / `testzip`），**未实例化任何张量或刺激值**。

---

## 1. 换道理由（RGE4）

R114 / R115 / R116 已把「不需批准的一手许可 / 归档内容取证」通道走到尽头；R116 独立审查明确剩余三项（全量内容核验、权重分发条款、natural clips 独立许可）须 designated gate owner 判断，且 R111「自主可达动作穷尽」判定 5 个决策点仍待用户答复。继续做第 N 份取证文档，正是 R105 / R107 / R109 已三次判停的同构循环。

用户第 1/2 步明确要求「回到主线」「按序 G1–G8 → … → **P3 真实前向解决 U5**」。R106 曾据 R101 的资产盘点推断「**瓶颈在门序与 G4 定位，不在缺数据 / 算力**」。这条结论的两半从未被同一轮实测冻结：资产字节（R106 已验 8/8 clips、10/10 官方模型）与**执行环境**是两件事。本轮换道做后者：**用本机真实测量把 P3 的前置条件固定成可复算契约**，不做第 N 份补丁式文字修复、不改任何状态。

## 2. 实质发现（负面件为主，如实报）

### 2.1 [核心・负面] `import flyvis` 只在**一个非官方 sandbox** 内成立

7 组独立子进程配置实测（`R117-EXEC-PREMISE-RAW.json` → `import_matrix`）：

| 配置 | 解释器 | PYTHONPATH / cwd | 结果 | 报错 |
|:--|:--|:--|:--|:--|
| A | base 3.14.6 | 默认 | **FAIL** | `No module named 'flyvis'` |
| B | ceg_snn_mi 3.11.15 | 默认 | **FAIL** | `No module named 'flyvis'` |
| C | ceg_snn_mi | cwd = 官方源码树 `sources/flyvis` | **FAIL** | `No module named 'flyvis.version'` |
| D | ceg_snn_mi | PYTHONPATH = `sources/flyvis` | **FAIL** | `No module named 'flyvis.version'` |
| E | base | PYTHONPATH = `sources/flyvis` | **FAIL** | `No module named 'pytz'` |
| F | ceg_snn_mi | R101 sandbox `local-provisioning/flyvis-work` + `FLYVIS_ROOT_DIR` | **OK** (v1.2.0) | — |
| G | ceg_snn_mi | F + `code-audit/flyvis-local-deps` | **OK** (v1.2.0) | — |

**逐字证据**：`local-provisioning/flyvis-work/flyvis/version.py` 前三行自述
`# RECONSTRUCTED for local provisioning only -- NOT an official FlyVis file.`，
值取自 CHANGELOG 顶部 `v1.2.0`；官方 pinned 快照（setuptools_scm 构建产物缺 `.git`）**不含该文件**。
⇒ **R101/R106 所依据的 `import flyvis` 结论是可复现的，但它的成立范围是「含重建非官方文件的本地副本 + 显式 PYTHONPATH + 显式 FLYVIS_ROOT_DIR」，不是官方源码树、不是默认环境**。这是一条**此前未冻结、不可移植**的执行前提。

**防夸大**：这不推翻 R101/R106 的历史读数（在 F/G 配置下确实 OK，本轮复现一致）；它把「资产齐备」与「环境齐备」分开——8/8 clip SHA、checkpoint SHA、weights-only 恢复本轮全部复算吻合，**资产字节结论成立**；但「开箱即用」不成立。

### 2.2 [核心・负面] 本机 MPS 可用，但 FlyVis 上游把它**排除在设备选择之外**

`flyvis-work/flyvis/__init__.py` 逐字两行：

```python
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
torch.set_default_device(device)
```

7 组配置全部 `mps_available=True / cuda_available=False`；F/G 成功组实测 `flyvis_device = cpu`，且 `torch.set_default_device(cpu)` 是**全局副作用**。
⇒ U5「官方 model000/001 真实前向」若按上游默认路径执行，将**全程落在 CPU**，MPS 不会自动被使用；要启用 MPS 须显式 `.to("mps")`，并须评估与 `set_default_device` 全局状态的交互。R101 §8.3 已点名此缺口「须先解决本机 MPS 与 FlyVis 默认 cpu device 的适配」，但从未实测冻结；**本轮首次给出可复算的设备前提读数**。

**防夸大**：本轮**没有**做任何设备迁移、没有跑任何前向；「MPS 可跑」「MPS 不可用」两种说法都不成立，成立的是「上游默认不选 MPS，需显式适配」。不构成任何 4090 / L4 / H20 能力主张。

### 2.3 [正面・资产] 官方 checkpoint 与 8 clips 字节复算全部吻合

| 项 | 本轮实测 | 与历史声明 |
|:--|:--|:--|
| `chkpt_00000` | 49,396 B / `d0e42857…ccc3f` | R101 声明 **MATCH** |
| `weights_only=True` 恢复 | `dict{network, decoder}` / **14** 张量 / `all_finite=True` | R101 **MATCH**（未构造网络） |
| 按 **R101 原规则**复算 state-dict digest | `67ce06c5cec0a4cda9937b17f061db0c99ad9f76c0224874c9b3a673c2e13a82` | R101 登记值 **MATCH** |
| 8 个 Sintel npz | 8/8 `testzip` CRC OK、SHA 与 R106 声明 8/8 一致 | R106 **MATCH**（零数组实例化） |
| 官方 `_meta.yaml` 逐字条款 | `seed: 0` / `gaussian_white_noise: 0.08` / `n_frames: 19` / `batch_size: 4` / `MultiTaskSintel` / `DecoderGAVP` / `flow: l2norm` | 只读，未据此运行任何校准 |

**分帧规则差异（非矛盾，防误判）**：本轮 probe 脚本第一版在每张量 raw bytes 后多加一个 `\0`，得 `bd3f2cc8…5e74`，与 R101 `67ce06c5…a82` 数值不同。按 R101 原规则重算后**完全吻合**；差异纯由分帧方式造成，与 R101 独立审查 §111 记录的「主会话 `67ce06c5` vs 子代理 `297e43d7`」同构。两个数值都如实保留，**不判为数据不一致**。

### 2.4 冻结契约就绪度（只报状态，不自我认证）

| 契约条款 | 本轮状态 | 说明 |
|:--|:--|:--|
| 冻结 seed 集 | `NOT_ESTABLISHED_BY_THIS_PROBE` | 只读到官方 meta 单行 `seed: 0`；多 seed 集 + 冻结 seed key 属 P2/P3 契约件，本轮不声称已建立 |
| 噪声校准（std .08 / lower-clamp / 4 draws） | `OFFICIAL_META_LINE_PRESENT` | 仅确认源行存在，**零校准运行** |
| 零注入断言 | `NOT_MEASURED` | 需可执行 runner；本轮未调用任何 runner |
| MPS 设备适配 | `MEASURED` | 见 §2.2，给出上游源码逐字与 7 组实测 |

四项均 `is_gate_pass=false`。**采集 ≠ 门通过**（R114 D1 / R116 教训）。

## 3. 可复算性

- `R117-probe.py`（7 配置子进程实测 + 字节 SHA + zip CRC + weights-only 恢复 + meta 逐字）
- `R117-EXEC-PREMISE-RAW.json`（18,455 B / `891a950b…0d50a`）
- `R117-verify.py` → `R117-EXEC-PREMISE-VERIFICATION.json`（**45/45 MATCH**，9 类凭证 0 命中）
- `R117-EXEC-PREMISE-VERIFICATION.v1-superseded.json`（v1 假 MISMATCH 留痕，见 §4）
- `R117-SOURCE-MANIFEST.json`（本轮 12 份源字节 URL/path + bytes + SHA256 + 合法 UTC）

**独立性问题（如实）**：`probe` 与 `verify` 同机、同 `hashlib`、同数据源，二者一致只是**必然的一致性核对**，**不构成独立交叉核验**（R115 W4 / R114 D1）。真正的独立复算交由本轮**全新隔离子代理**从磁盘字节重做，报告原文不改写。

## 4. 只追加更正 ①（v1 假阴性，脚本判定缺陷非数据不一致）

verify 初版把「9 类凭证模式」与「本机绝对路径 `/Users/<user>/`」合并成单一布尔，报 `SECRET-free = MISMATCH / 17 hits`。逐条复核：**17 处全部为 `/Users/xhf/` 解释器 / 配置路径，凭证 0 命中**。按 R115 W2 口径，本机路径在主项目内部产物中是配置事实、**不可外推项目全局**，但公开同步副本必须脱敏为 `<local>/`（R109 红线）。
⇒ 最终版拆为 `SECRET-free`（9 类，0 命中 MATCH）与 `LOCALPATH-registered`（19 处如实登记，不宣称零命中）。v1 完整留痕为 `.v1-superseded.json`（11,505 B / `5eb48011…`），最终版 9,552 B / `aa1372d2…`，**两版读数都保留、RAW 原始字节零改写**。

## 5. 边界（严格）

- 全 `READONLY_EXECUTION_PREMISE_PROBE`；**EXEC LOCK 零前向 / 推理 / 训练 / 标签 / 数据集数组 / EPE·l2 / 科学指标**。
- **零门晋级 / 零自我认证 / 零状态改动**：主线 `pipeline-state.json` = `bcb48bb9…a33d` / 3,723 B，与 R107 冻结值一致 ⇒ **字节未改**；G0–G8 / validation / handoff 全 `pending`，**G0 维持 pending**。
- 未改历史字节 / 评审 / 分数 / 阈值 / 稿件 / 门 / 冻结件 / 矩阵 / 判据登记 / 门配置；未起 `ccf-paper-reviewer full`、未产生 `**Overall:**` 行、未自评 governing、未跳门、未对未修改稿件重复评审。
- 未重开 D1 / v3、未出 predictor v4、**未假定 `≤32h / K=45` confirmation 授权**；与 harbor 25092 工程 reward 无关、无 4090 能力主张；主项目未投稿 / commit / push；心跳 ACTIVE 调度 `FREQ=HOURLY;INTERVAL=1;BYMINUTE=0,30` 无变化。
- 双门只读结果见 `R117-ROUND-AUDIT.md`；governing 仍 **R95 = 6.0 / Confidence 4.0**，`NOT_QUALIFIED` / `INCOMPLETE`。

## 6. 交下轮

1. 仍**不执行**任何须用户 / gate owner 批准的机器门修复（`R111-DECISION-READY-PACKAGE.md` 5 决策点待答复）；不写第 N 份 G0 文字补丁。
2. 本轮实测暴露的 P3 前置缺口须由 designated gate owner 书面冻结为**版本化执行契约**：① sandbox 的重建 `version.py`（非官方文件）是否在科学管线中可接受、如何留痕；② MPS 显式 `.to("mps")` 与 `set_default_device(cpu)` 全局状态的适配方案；③ 冻结 seed 集 / seed key / 4 draws / lower-clamp / 零注入断言的可执行 runner。**心跳不自我认证、不在 G0 未过时启动 P3 前向**。
3. gap 1 剩余三项（全量内容核验、权重分发条款、natural clips 独立许可）维持 R116 独立审查判定：须 gate owner 取证判断，不得把记录级 CC BY 自述 / 代码 MIT / 公共下载外推为授权。
4. 按序 G0–G8（G4 正面处理 Kuklev v2 §7.3 / §8 / §9）→ validation → handoff → P0 → P1A/P1B → P2 → **P3 真实前向解决 U5**。
5. 只有 `failed_runs=0` + 全 finite + 独立复算吻合 + **实质正向新科学证据**，才进稿件新副本 → 9 页合规编译 → 全新隔离 full 评审；**X >= 7.0** 且 QUALIFIED + COMPLETE 才写 COMPLETE。

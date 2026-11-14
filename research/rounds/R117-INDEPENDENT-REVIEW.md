**Verdict:** PARTIAL | **G0 may be passed:** NO | **Scientific result claimed:** NO
**Forward pass performed:** NO

# R117 独立复核报告（全新隔离子代理 / 门·证据层）

> 本报告是**门 / 证据层独立审查**，不是 `ccf-paper-reviewer full` 稿件评审。不含 `**Overall:**` 行、不给数值论文分、不写论文置信度字段、不改 governing。
> 本代理未参与任何产物创建，主会话未透露期望结论。以下全部结论均**从磁盘字节独立重算**，未采信任何产物自报值。
> 跑代码一律用本机 conda：`/Users/xhf/miniconda3/bin/python`（驱动）与 `/Users/xhf/miniconda3/envs/ceg_snn_mi/bin/python`（torch 2.13.0 相关）。为控制本文内容安全，正文一律以 `<local>/` 代替本机绝对路径。

## 0. 范围、方法、边界

- 复核对象（任务指定 7 份）：`R117-probe.py`、`R117-verify.py`、`R117-EXEC-PREMISE-RAW.json`、`R117-EXEC-PREMISE-VERIFICATION.json`、`R117-EXEC-PREMISE-VERIFICATION.v1-superseded.json`、`R117-SOURCE-MANIFEST.json`、`R117-EXEC-PREMISE-EVIDENCE.md`；及其引用的历史一手件：`local-provisioning/R101-LOCAL-PROVISIONING.md`、`local-provisioning/weights-only-restore-R101.json`、`local-provisioning/flyvis-work/flyvis/__init__.py`、`local-provisioning/flyvis-work/flyvis/version.py`、`gate-G0-R106/R106-ASSET-SHA-VERIFICATION.json`、`sources/flyvis-pretrained-access/unpacked/results/flow/0000/000/`、`sources/sintel-development-subset-v1/rendered-attempt-1/`、`pipeline-state.json`。
- 方法：SHA256 以 1 MiB 分块流式重算；npz 仅经 `zipfile` 中央目录读 `infolist()`/`CRC`/`file_size`/`testzip()`；checkpoint 仅 `torch.load(map_location="cpu", weights_only=True)` 恢复并检查张量元数据与有限性；7 组 import 由独立 driver 起独立子进程（`subprocess.run([py,"-c",SRC])`）实测。
- 未执行：任何模型前向 / 推理 / 训练 / 标签读取 / npz 数组实例化 / EPE·l2 计算 / 科学指标；未联网；未投稿 / commit / push；未起 full reviewer；未改任何已有文件字节。
- 复核期间目录内新增一份 `R117-ROUND-AUDIT.md`（03:22，8,082 B / `76d0c8b7…`）：由主会话创建，**非本代理创建、非 manifest 登记、本代理未改动**。因其位于 `exec-premise-R117/` 全目录内，本文将其纳入内容安全扫描与夸大审查，并在 §5/§6 如实记录其字节级问题。

---

## 1. 从磁盘字节独立重算（不采信自报值）

### 1.1 19 份 source 的 bytes + SHA256 vs manifest —— 19/19 MATCH
逐个以相对 run root 路径 `stat().st_size` + SHA256 重算，与 `R117-SOURCE-MANIFEST.json` 的 `sources[]` 逐条比对：**19 项全部 bytes 与 SHA256 双吻合**，无 MISMATCH。manifest 自报 `source_count=19`、迭代数 19，一致。含 flyvis `__init__.py`(1801)、`version.py`(255)、`chkpt_00000`(49396)、`_meta.yaml`(2222)、R101 note(9839)、R101 restore json(3611)、R106 asset json(4978)、R106 audit(15372)、R111 package(5811)、R116 audit(8719)、`pipeline-state.json`(3723)、8 个 npz。

### 1.2 6 份 artifact 的 bytes + SHA256 vs manifest —— 6/6 MATCH
以相对 `exec-premise-R117/` 重算：EVIDENCE.md(10715)、RAW.json(18455)、VERIFICATION.json(9552)、VERIFICATION.v1-superseded.json(11505)、probe.py(12777)、verify.py(8978) **全部 bytes + SHA256 双吻合**。manifest 自身**不列自己**（`self-listed=False`），`artifact_count=6` 与迭代数一致。manifest 自身磁盘 SHA 独立重算为 `b113ed99…ce8a`（7765 B），与 `R117-ROUND-AUDIT.md` §4 自报一致。

### 1.3 8 个 Sintel npz vs gate-G0-R106 声明 + zip CRC/testzip —— 8/8
8 个 npz 的 SHA256 与 `R106-ASSET-SHA-VERIFICATION.json` 的 `declared_sha256` **逐字全等**、亦与 RAW.json 一致（8/8）。逐个 `zipfile.ZipFile(...).testzip()` 均返回 `None`（CRC 全通过，8/8），每个 zip 4 条目（`lum_source/flow_source/lum_resampled/flow_resampled.npy`），RAW.json 登记的 `zip_crc32` 与中央目录 `i.CRC` 逐条吻合，`zip_uncompressed_bytes` 与 `i.file_size` 一致。**全程未实例化任何数组、标签或刺激值**；CRC/testzip 仅验证容器完整性。

### 1.4 官方 chkpt_00000 + weights_only 独立恢复
- 字节 49,396 B，SHA256 = `d0e42857e738d0315897c2d50fde9eb3fb1a3fb1f071d55dfc13d53d72bccc3f`，与 manifest / R101 / R106 声明一致。
- `torch.load(weights_only=True)` 独立恢复：`top_level_type=dict`，排序键 `['decoder','network']`，**14** 张量，`all_finite=True`，14 张量 raw_bytes 合计 44,552 B。与 R101 `weights-only-restore-R101.json` 的 14 张量形状清单一致。

### 1.5 state-dict digest：按 R101 原规则复算 = 67ce06c5…（独立证实）
按 R101 §6 / `weights-only-restore-R101.json` 原规则（按 key 排序，逐张量帧 `key\0dtype\0shape\0raw_bytes`，**帧尾无 `\0`**）从磁盘 checkpoint 独立重算：

| 分帧规则 | 独立复算 digest | 结论 |
|:--|:--|:--|
| R101 原规则（帧尾无 `\0`） | `67ce06c5cec0a4cda9937b17f061db0c99ad9f76c0224874c9b3a673c2e13a82` | 与 R101 登记值 **MATCH** |
| `R117-probe.py` 第一版（帧尾多一个 `\0`） | `bd3f2cc8a037e1f58517989fced0f233a97e647f3ab9545d865e8bb416e25f74` | 与 RAW.json 自报字段 **MATCH** |

**为何第一版得到 `bd3f2cc8…5e74`（分帧差异而非数据不一致）**：`exec-premise-R117/R117-probe.py:166` 的 `RESTORE_SRC` 为 `h.update(t.contiguous().numpy().tobytes() + b"\0")` —— 每张量在 `raw_bytes` 后**多拼接一个 `\0`**；而 R101 规则是 `key\0dtype\0shape\0raw_bytes`（帧尾无 `\0`）。两者作用于**同一组 14 张量的同一批字节**（合计 44,552 B），仅帧间分隔符不同，SHA256 必然不同。我用两种规则分别复算，逐字得到上表两个值，证明 `67ce06c5` 与 `bd3f2cc8` 是**同一数据的两种分帧读数，不是数据矛盾**，与 R101 独立核验记载的「主会话 `67ce06c5` vs 子代理 `297e43d7`（长度前缀分帧）」同构。

### 1.6 主线 pipeline-state.json
- 3,723 B，SHA256 = `bcb48bb964e657a40a5dfb595f38f554ebbdc9ed006a00b741c877a3772ac33d`，与 R107 冻结值 / manifest 登记一致 ⇒ **字节未改**。
- `G0` `status=pending`、`gate_verdict=pending`；`G0–G8 / validation / handoff` **全 pending**（仅 `CCFA-startup=passed`）。与产物「G0 维持 pending」一致。

### 1.7 逐字核对
- `local-provisioning/flyvis-work/flyvis/__init__.py:13-14` 两行 `device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")` 与 `torch.set_default_device(device)` 逐字在场（ cuda-or-cpu 二选、无 mps 分支）。
- `local-provisioning/flyvis-work/flyvis/version.py:1` 含 `NOT an official FlyVis file`，第 4 行 `__version__ = '1.2.0'` 在场；255 B / `15efb6b0…`。RAW.json `device_source_verbatim` / `version_py_verbatim` 与磁盘一致。

---

## 2. 核心实测结论独立验证：7 组 import（A–G）

严格按 RAW.json `import_matrix` 各 `config` 字段（解释器 / cwd / PYTHONPATH / `FLYVIS_ROOT_DIR`）由独立 driver 起 7 个独立子进程实测：

| 配置 | 解释器 | 结果 | 报错 | flyvis.device | mps | cuda |
|:--|:--|:--|:--|:--|:--|:--|
| A_base_default | base 3.14.6 | **FAIL** | `No module named 'flyvis'` | — | True | False |
| B_ceg_default | ceg 3.11.15 | **FAIL** | `No module named 'flyvis'` | — | True | False |
| C_ceg_cwd_sources | ceg | **FAIL** | `No module named 'flyvis.version'` | — | True | False |
| D_ceg_syspath_sources | ceg | **FAIL** | `No module named 'flyvis.version'` | — | True | False |
| E_base_syspath_sources | base | **FAIL** | `No module named 'pytz'` | — | True | False |
| F_ceg_r101_sandbox | ceg | **OK** (1.2.0) | — | cpu | True | False |
| G_ceg_sandbox_plus_deps | ceg | **OK** (1.2.0) | — | cpu | True | False |

**5 FAIL / 2 OK 独立复现成立**；成功组 `flyvis.device=cpu`、`flyvis_version=1.2.0`、`connectome_exists=true`；全部 7 组 `mps_available=True / cuda_available=False`，`default_device_before/after` 全为 cpu。结论与 RAW.json 逐字一致：`import flyvis` 只在「含重建非官方 `version.py` 的 R101 sandbox + 显式 PYTHONPATH + 显式 FLYVIS_ROOT_DIR」下成立，官方源码树 / 默认环境均 FAIL。

---

## 3. 12 类夸大 / 自我认证逐条审查

判定口径：**CONFIRMED** = 该类夸大在本轮最终交付结论中出现；**REFUTED** = 未出现 / 被产物明确否认且经独立复算证实。

- **(a) 把「资产字节齐备」说成「执行环境齐备 / 开箱即用」→ REFUTED。** 证据：`R117-EXEC-PREMISE-EVIDENCE.md:40`「它把『资产齐备』与『环境齐备』分开……**资产字节结论成立**；但『开箱即用』**不成立**」；`:38`「不是官方源码树、不是默认环境……此前未冻结、不可移植」；`R117-ROUND-AUDIT.md:29`「把『资产齐备』与『环境齐备』分开」。7 组 import 的 5 FAIL 正是「环境不齐备」的负面件（§2 独立复现）。
- **(b) 把 import 成功说成模型前向已跑通 → REFUTED。** 证据：RAW.json `classification` 含 `NOT_FORWARD_PASS`、`strict_boundary.forward_pass=false`；EVIDENCE.md:9、:96「零前向 / 推理 / 训练 / 标签 / 数据集数组 / EPE·l2 / 科学指标」；:54「没有跑任何前向」。本独立复核亦未执行前向。F/G 的 OK 只登记为「import 可复现」，未升级为前向。
- **(c) 把 MPS 可用说成 MPS 已被使用 / 4090·L4·H20 能力 → REFUTED。** 证据：EVIDENCE.md:54「『MPS 可跑』『MPS 不可用』两种说法都不成立……**不构成任何 4090 / L4 / H20 能力主张**」；:52 明确上游默认落 CPU、须显式 `.to("mps")`；:99、ROUND-AUDIT.md:64「无 4090/L4/H20 能力主张」。独立实测成功组 `flyvis.device=cpu`，`__init__.py:13` 无 mps 分支，佐证「MPS 可用但未被上游选用」。注：RAW.json 的 `flyvis_file`/`root_dir` 出现的 `4090` 仅是本机路径目录名（`<local>/…/phd/4090/…`），非 GPU 能力主张。
- **(d) 把 weights_only 恢复说成科学结果 → REFUTED。** 证据：RAW.json `classification` 含 `NOT_SCIENTIFIC_RESULT`；EVIDENCE.md:4「Scientific result claimed: NO」；ROUND-AUDIT.md:31 表格把该行明确标注「**正面资产字节**（非科学结果）」；R101 一手件亦为 `PROVISIONING_ONLY_NOT_SCIENTIFIC_RESULT`。`weights_only` 恢复仅确认为 dict/14 张量/全 finite（§1.4），未构造网络、未计算指标。
- **(e) 把 zip CRC 检查说成读取了数据集 / 标签 / 刺激值 → REFUTED。** 证据：RAW.json `strict_boundary.npz_arrays_instantiated=false` 及 `note`「npz inspected only via zip central directory (filename, CRC, uncompressed size, testzip). No array, label, or stimulus value was read.」；EVIDENCE.md:9「未实例化任何张量或刺激值」；:96「npz 仅查 zip 中央目录」。本复核同样仅读中央目录（§1.3）。
- **(f) 把采集说成 G0 通过或任何门晋级 → REFUTED。** 证据：RAW.json `strict_boundary.gate_promotion=false`、`frozen_contract_readiness` 四项 `is_gate_pass=false`；EVIDENCE.md:77「采集 ≠ 门通过」、:97「零门晋级……G0 维持 pending」；ROUND-AUDIT.md:64、:73「G0 维持 pending」。独立复算 pipeline-state.json 全 pending（§1.6）。
- **(g) 把主会话脚本一致性核对说成独立交叉核验 → REFUTED。** 证据：`R117-verify.py:4-7` docstring「Agreement between the two products is a NECESSARY consistency check, **NOT an independent cross-validation**」；VERIFICATION.json `classification=SECOND_SCRIPT_CONSISTENCY_CHECK_NOT_INDEPENDENT_CROSS_VALIDATION` + `independence_note`；EVIDENCE.md:87「二者一致只是**必然的一致性核对**，**不构成独立交叉核验**（R115 W4 / R114 D1）。真正的独立复算交由本轮全新隔离子代理」。本代理即该独立复算，结论在本文。
- **(h) 把本机绝对路径 0 命中当全局结论，或把 17/19 处本机路径误判为凭证 → REFUTED（最终交付结论），但 v1 留痕中该误判曾局部发生且已修正。** 证据：VERIFICATION.json `local_path_disposition`「Zero local paths are claimed absent」、`LOCALPATH-registered` 明确登记 19 处；EVIDENCE.md:91「17 处全部为 `<local>/` 解释器 / 配置路径，**凭证 0 命中**……不可外推项目全局」；:92「19 处如实登记，**不宣称零命中**」。`R117-probe.py` 的 `secret_scan` 是 **7 类凭证模式** 0 命中（不含本机路径模式），非「本机路径 0 命中」。**如实记录**：`.v1-superseded.json` 初版曾把凭证与本机路径合并成单一布尔，报 `SECRET-free=MISMATCH / 17 hits`，17 处全为 `<local>/` 路径 —— 这是把本机路径误计入凭证判定的**假阴性**，但已被明确保留为留痕并由最终版拆分修正，未作为最终结论。本代理独立扫描（§5）亦证实凭证类 0 命中、本机路径为配置事实。
- **(i) 把分帧规则不同的两个 digest 判为数据矛盾 → REFUTED。** 证据：EVIDENCE.md:66「差异纯由分帧方式造成……两个数值都如实保留，**不判为数据不一致**」；ROUND-AUDIT.md:32「分帧规则差异 ⇒ **非数据不一致**」。本代理以两种规则独立复算（§1.5），逐字得到 `67ce06c5` 与 `bd3f2cc8`，证实同一 14 张量字节、仅分隔符不同。
- **(j) 把官方 meta 单行 `seed:0` 说成冻结 seed 集 / 噪声校准已完成 → REFUTED。** 证据：RAW.json `frozen_contract_readiness.frozen_seed_set.status=NOT_ESTABLISHED_BY_THIS_PROBE`、「不声称已建立」、`noise_calibration=OFFICIAL_META_LINE_PRESENT`「零校准运行」、`zero_injection_assertion=NOT_MEASURED`；EVIDENCE.md:72-75 四项表 + :77「四项均 `is_gate_pass=false`」；ROUND-AUDIT.md:33 同样。仅确认源行存在，未运行校准。
- **(k) 声称起了 `ccf-paper-reviewer full` 或产生数值论文分 → REFUTED。** 证据：EVIDENCE.md:8「不是 `ccf-paper-reviewer full` 稿件评审，不含 `**Overall:**` 行、不含数值论文分」、:98「未起 `ccf-paper-reviewer full`、未产生 `**Overall:**` 行、未自评 governing」；ROUND-AUDIT.md:64、:72「不编译、不起全新增隔离 full 评审」。`R117-ROUND-AUDIT.md` §5 出现的 validator/guard 读数（含 `all_scores` 数组）标注为「**双门只读**（报告写 /tmp）」，属历史 governing / validator 的只读引用，非本轮新起的 full 评审、非本轮产生的数值论文分。本独立报告亦为门层审查，未给分。
- **(l) 声称改了 pipeline-state.json 字节 / 评审 / 分数 / 阈值 / 稿件 / 历史字节 → REFUTED。** 证据：EVIDENCE.md:97「pipeline-state.json …… ⇒ **字节未改**」、:98「未改历史字节 / 评审 / 分数 / 阈值 / 稿件 / 门……」；ROUND-AUDIT.md:59「字节零改动」、:64「零状态改动」。本代理独立重算 pipeline-state.json SHA = `bcb48bb9…a33d`（§1.6），与 R107 冻结值一致，且 19 source + 6 artifact + chkpt + pipeline-state 全部字节未变。

**12 类最终交付结论中全部 REFUTED**；唯一如实保留的局部例外是 (h) 的 v1 假阴性留痕（已修正、未作为结论）。

---

## 4. 状态判断

- **本轮证据是否足以让 G0 pass：NO。** 产物自身 `classification` 即 `NOT_GATE_PASS`，四项就绪度 `is_gate_pass=false`，零前向 / 零科学指标；独立复算只确认了资产字节与环境读数真实，**不构成门晋级所需的实质正向证据**。ROUND-AUDIT.md:73 与 EVIDENCE.md:97 均自报 G0 维持 pending，且 gap 1 剩余三项（全量内容核验、权重分发条款、natural clips 独立许可）按 R116 判定仍须 designated gate owner。
- **是否构成实质正向新科学证据：NO。** 全部结论为工程 / 门层只读实测（字节完整性、import 可复现性、设备解析、容器 CRC），无模型前向、无 EPE/l2、无科学指标。资产字节吻合 ≠ 科学结果。
- **是否应维持 G0 pending：YES。** 与 pipeline-state.json 全 pending 的磁盘字节一致。

**Verdict = PARTIAL 的理由**：§1/§2 的核心实测（19+6+8+chkpt+digest+7 组 import+pipeline-state）**100% 独立复算吻合、无数据造假、无越界、无夸大**；但存在 §6 所列 5 处低 / 低-中严重度的文档与证据链瑕疵，且按设计本轮不构成 G0 pass / 科学结果 / 前向。既非全无瑕疵的 PASS，亦非有实质缺陷的 FAIL，故 PARTIAL。

---

## 5. 内容安全扫描（≥10 类严格模式，全目录）

扫描对象：`exec-premise-R117/` 全目录落盘前的 **8 份文件**（EVIDENCE.md、RAW.json、VERIFICATION.json、VERIFICATION.v1-superseded.json、ROUND-AUDIT.md、SOURCE-MANIFEST.json、probe.py、verify.py；`sources/` 为空目录）。

**14 类凭证 / 密钥严格模式**：Google API key (`AIza…`)、OpenAI `sk-…`、GitHub `ghp_…`、`-----BEGIN … PRIVATE KEY-----`、`api_key` 赋值、`Bearer …`、邮箱地址、`password` 赋值、`client_secret` 赋值、AWS `AKIA…`、Slack `xox…`、JWT (`eyJ…`)、hex `secret` 赋值、通用 `token` 赋值。

| 类别 | 命中数 | 分布 |
|:--|:--|:--|
| **凭证类命中数** | **0** | 全部 14 类、全部 8 份文件均无命中 |
| **本机路径命中数** | **25** | RAW.json 12、EVIDENCE.md 3、probe.py 3、verify.py 2、ROUND-AUDIT.md 2、VERIFICATION.json 1、v1-superseded.json 1、SOURCE-MANIFEST.json 1 |

- 本机路径匹配模式为 `/Users/[A-Za-z0-9_.\-]+/`，命中全部为解释器 / 配置 / 产物路径的绝对前缀，属**配置事实**，不是凭证；与凭证类 0 命中严格分开统计。
- **历史数字成因（均非数据矛盾）**：`.v1-superseded.json` 自报 17 = RAW(12)+probe(3)+verify(2)，是 v1 运行时目录仅这 3 份含路径文本时的读数；VERIFICATION.json 自报 19 是 verify 运行时点的文件集合快照；本代理以同模式对「排除 03:22 新增 ROUND-AUDIT 的 7 份」复算得 23、对全 8 份得 25。三者差异源于**扫描文件集合的时序变化**（EVIDENCE / SOURCE-MANIFEST / v1-superseded / VERIFICATION / ROUND-AUDIT 在两次 verify 运行间先后落盘）与模式类数不同，不是伪造或矛盾。产物（EVIDENCE.md:91-92、VERIFICATION.json `local_path_disposition`、ROUND-AUDIT.md:44）已明确「如实登记、不宣称零命中、不可外推项目全局」。
- **脱敏红线（明确要求）**：**公开 GitHub 同步副本必须把全部本机绝对路径脱敏为 `<local>/` 后再 staging（R109 红线）**；本独立报告正文已以身作则，全部以 `<local>/` 代替，不引入新的本机绝对路径或凭证命中。

---

## 6. 如实登记的真实缺陷（含严重度与具体证据）

以下为独立复算中发现的**真实**瑕疵，均**不改变**「字节完整性成立、非科学结果、不晋级 G0」的核心判定；按任务要求如实写明，不为通过而弱化、不为显严格而虚构。

1. **[低-中] `67ce06c5…a82` 缺一手落盘件（证据链 / 可复算性缺口）。** EVIDENCE.md:62 与 ROUND-AUDIT.md:31 把「按 R101 原规则复算 state-dict digest = `67ce06c5…` MATCH」列为本轮实测表格行，但：RAW.json 唯一 `state_dict_digest_sha256`（:393）是 `bd3f2cc8…5e74`（probe 规则）；磁盘上 `R117-probe.py:166` 的 `RESTORE_SRC` 仍是带尾部 `\0` 的规则；`R117-verify.py` 的 45 项检查**没有**任何 digest 一致性项。即「按 R101 原规则复算」这一步**没有作为脚本一手结果落盘**，是文本断言。本代理独立复算（§1.5）证实该数值本身**正确**、两个 digest 数值差异纯为分帧；故这是可复算性 / 证据链缺口，**不是数据错误、不是造假**。建议下轮把 R101 规则复算值作为独立字段写入一手 JSON 或补一条 verify 检查。
2. **[低] EVIDENCE.md:85「本轮 12 份源字节」措辞错误。** `R117-SOURCE-MANIFEST.json` 的 `source_count=19` / `sources[]=19`（§1.1 独立证实）；RAW.json 的 `source_manifest[]` 才是 12（4 非 clip + 8 clip）。疑为把 RAW 的 12 误套到 MANIFEST 的 19。ROUND-AUDIT.md:46 写「19 份源全存在」正确。属文档笔误，不影响字节结论。
3. **[低] ROUND-AUDIT.md:44 一处 SHA 转录为 63 位错值。** 该文件对 `R117-EXEC-PREMISE-VERIFICATION.json` 自报 `aa1372d2bb91e4bc…625946a`，仅 **63 位**（把 `bbf91e` 误写为 `bb91e`，漏 `f`），与磁盘 64 位 `aa1372d2bbf91e4bc…625946a` 不符；`R117-SOURCE-MANIFEST.json` 登记值与 EVIDENCE.md:92 的前缀 `aa1372d2…` 均正确。属主会话轮次审计的转录错误（该文件非任务指定的 7 份核心产物之一、且 manifest 未登记），不影响 6 份产物字节完整性结论。
4. **[信息性] manifest 未登记第 7 份产物。** `R117-SOURCE-MANIFEST.json` 登记 6 份 artifacts（全部吻合），但 `R117-ROUND-AUDIT.md`（03:22，8,082 B / `76d0c8b7…`）既不在 `sources` 也不在 `artifacts`。成因是 manifest 生成于 03:19、ROUND-AUDIT 于 03:22 由主会话新增（本代理未创建、未改动）。属产物清单时序问题，非数据矛盾。
5. **[低 / 信息性] EVIDENCE.md:72「官方 meta 单行 `seed: 0`」措辞不严谨。** 磁盘 `_meta.yaml` 实有 **2 行** `seed: 0`（第 25、108 行），RAW.json `clause_lines` 亦如实列出 2 行。该措辞不构成 (j) 夸大（产物明确 `NOT_ESTABLISHED` / 零校准运行），仅为「单行」表述不精确。

---

## 7. 硬约束遵守声明

- **只新建一份文件**：本报告 `exec-premise-R117/R117-INDEPENDENT-REVIEW.md`；一次落盘、原文不再改动。未修改 / 删除 / 重定日期任何已有文件 —— §1.1/§1.2/§1.4/§1.6 的全部 SHA 与 manifest / R107 冻结值吻合，即证明既有字节未变（含 `R117-EXEC-PREMISE-EVIDENCE.md`、RAW.json、VERIFICATION.json、两份脚本、`pipeline-state.json`）。复核期间出现的 `R117-ROUND-AUDIT.md` 非本代理创建、本代理未改动。
- 报告首行 / 次行严格为规定格式；无 `**Overall:**` 行、无数值论文分、无论文置信度字段、未改 governing。
- 未运行模型前向 / 训练 / 推理 / 标签读取 / EPE·l2 计算；未联网；未投稿 / commit / push；未起 `ccf-paper-reviewer full`；未假定任何用户授权。
- `weights_only=True` 恢复、zip 中央目录 CRC / testzip、7 组 import 均为只读环境探测，符合 EXEC LOCK。
- 本报告最终 bytes 与 SHA256 由落盘后单独计算，于交付回报消息中给出（不写入本文以避免自引用）。

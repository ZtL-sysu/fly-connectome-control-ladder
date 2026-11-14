# R106 — R98 gap 1 的资产/许可逐一核查（如实区分 CLOSED / OPEN）

状态：`READONLY_SOURCE_VERIFICATION_ONLY_NOT_SCIENTIFIC_RESULT`。
**本文件不标 G0 passed、不晋级任何门。**

R98 gap 1 原文：矩阵中若干条目仍标注 `asset contents/license not yet
individually verified` 或 `project code path not yet verified`。本轮逐条核查，
**能关的才关，关不了的如实留 OPEN**，不把「搜到了页面」当成「验证完成」。

| 矩阵条目 / 标注 | 本轮一手核查 | 判定 |
|:--|:--|:--|
| Correig-Fraga 2026 `arXiv:2610.10023`，原标 `public paper links Zenodo 21549559; asset contents/license not yet individually verified; adaptation-attempt, not yet runnable` | Zenodo record 21549559 存在且 `Open`，Published 2026-07-25 v1.0.0；描述逐字含 `exact processed biological and randomized connectome graphs, neuron annotations and retinal-neuron coordinate mapping, trial-level model predictions, and numerical source tables used for Figs. 2 and 3`、`README, data dictionary, file manifest, and SHA-256 checksums`，并给出两个代码 commit（`connectome 93476a27…`、`train-your-fly 733a8bdb…`）；arXiv HTML/PDF 全文可达，摘要给出「matched wiring cost 下生物图更高精度，约束更少的重连以inflated wiring 超越」的结论 | **PARTIAL**：Zenodo 记录内容与校验和字段已确认存在；但**未下载归档逐文件复算 SHA、未逐一读许可文本、未尝试运行**，故原标注的 `not yet runnable` **维持 OPEN**。不把「页面存在」写成「资产已验证」 |
| Dhawan / FlyHack 2026 `arXiv:2610.13018`，原标 `Official flyvis models + CNN baselines reported; project code path not yet verified` | 检索**未找到** FlyHack 独立公开代码仓；只找到官方 `github.com/TuragaLab/flyvis`（MIT license，2026-10-14 仍有提交）与论文 HTML/摘要。论文明确写 `the released flyvis models' launch-time split is not recoverable` | **维持 OPEN**：FlyHack 项目代码路径仍**未验证**；官方 flyvis 的 MIT license 与活跃提交已核实，但那是另一个代码仓，不能替代 FlyHack 的复现资产 |
| Lappalainen 2024 Nature / 官方 flyvis `must-rerun` | 官方 repo `TuragaLab/flyvis` 可达、`MIT license`、含 `flyvis_cli/download_pretrained_models.py`；本地 `sources/flyvis/` 513 文件 / 62M、有 `license` 文件；官方预训练归档 `3,417,042 B` / SHA `71c78d40…` 与 `access-manifest.json` 的 `matches_official_hash: true` 一致 | **CLOSED（就「官方代码/许可/归档可得性」这一项）**；注意这不等于「网络前向已跑通」 |
| Sintel `MPI-Sintel-complete.zip` | `sources/sintel-development-subset-v1/access-manifest.json` 记 `status: success`、官方 URL、`license_url: https://sintel.is.tue.mpg.de/license`、逐文件 SHA/CRC；本轮从字节复算 8 个 development clips **8/8 吻合**（`R106-ASSET-SHA-VERIFICATION.json`） | **CLOSED（可得性 + 本地 8 clips 字节完整性）**；附带的 `Exclude raw/derived Sintel data from deliverable source archives` 分发限制仍须遵守，登记不消除 |
| 5 份保存的一手文献 HTML | `literature-search/source-manifest.json` 声明的 bytes+SHA 与本地实际文件 **5/5 吻合**（`R106-LITERATURE-SOURCE-SHA-VERIFICATION.json`） | **CLOSED（保存件完整性）**；不等于文献内容判断已复核 |

## 汇总（不夸大）

- **R98 gap 1 未整体闭合**：Correig-Fraga 归档内容/许可与 FlyHack 代码路径仍是 OPEN。
- 本轮关闭的是「官方 flyvis 代码/许可/预训练归档」与「Sintel 8 clips 字节完整性」
  与「保存文献完整性」三项**可得性**证据，属于 G1 范畴，**不是 G0 的通过判定**。
- R98 的 gap 2（矩阵须 final）、gap 4（scientific/visual gate judgment）**未闭合**；
  gap 3 由本轮的独立 gate review 处理，结论以该报告首行 verdict 为准。
- 2026 几何研究（aimedicalcompendium）那条 secondary hit **本轮仍未独立复核**，
  保留 R99 记录状态，不宣称已验证。

## 红线

零前向 / 零训练 / 零标签 / 零数据集；不改任何已落盘文件、评审、分数、阈值、
冻结件、gate 状态；不把资产可得性包装成科学结果或 4090/L4 能力；未投稿/commit/push。

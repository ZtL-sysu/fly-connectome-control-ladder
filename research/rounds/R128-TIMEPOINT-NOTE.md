# R128 时点声明（只追加，不回写任何已发布字节）

本文件记录采集 / 校验与同步之间的**时点差**，避免把两个时点的读数混为同一时点。

| 时点 | `git status --porcelain`（同步仓库） | 说明 |
|:--|:--|:--|
| T1 `2026-11-14T11:27:45Z`（`R128-ACQUIRE.py`） | **空** | 读取的是 `main` ref 的**提交 blob**，与工作树状态无关；A 组 `worktree_clean=True` 是 T1 的同机一致性核对。 |
| T2 `2026-11-14T11:35:xxZ`（`R128-VERIFY.py`） | **空** | 独立 verifier 36/36 全 MATCH，含 `worktree_clean=True`；同为 T1/T2 时点真值。 |
| T3 同步写入之后（HANDOFF 纯插入 / LOG 只追加 / 新增 12 份 `research/` 文件 / `UPLOAD-MANIFEST.json` 只追加 / 新检查点） | **非空（本轮自身未提交改动）** | 这是本轮**预期内**的写入，全部发生在 agent 分支；提交后工作树重新干净。 |

- 因此 `R128-ACQUIRE.json` 与 `R128-VERIFICATION.json` 中的 `worktree_clean=True`、`status_porcelain` 为空，**严格限定于 T1/T2 采集时点**，不得解读为「整轮结束时工作树始终干净」。
- `main` ref 的提交 blob 在 T1/T2/T3 **全程未变**（`6cc2e4fbe351…`）；本轮所有写入都在 `agent/r109-harbor-sync/wb-main` 分支，**没有 merge / force push / 删分支 / 改写 `main`**。
- 双门（validator / guard）与 7 份结构权威的读数取自**主项目**，与同步仓库工作树无关；采集前与 verifier 后两次读数 7/7 一致 ⇒ 主项目零写回。
- 本文件为只追加的时点澄清，不修改 `R128-ROUND-AUDIT.md`、`R128-ACQUIRE.json`、`R128-VERIFICATION.json` 或任何已发布字节。

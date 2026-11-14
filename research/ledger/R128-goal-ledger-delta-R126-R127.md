

### R126 主会话：**按用户指令把研究成果/进展/思路全量开放同步到 GitHub**（2026-11-14 18:0x–18:2x）

| 项 | 内容 |
|:--|:--|
| 用户指令 | 「给我把研究成果，研究进展，研究思路这些整上去。那种大的模型权重，数据集就不用传，不用担心。你把我说的东西都传一下，按 `research-github-sync` 规则来，里面有模板。按那个来，之前不对的你也整理整理」+「不用考虑脱敏的事情，open 就对了」 |
| **范围变更** | 公开仓库从「小型脱敏协作层」改为**全开放研究成果档案**；文本一律不改写（本机路径、账号标识、未投稿稿件、内部评审原文全部照传）。**唯一硬排除**：含真实凭证值的文件（会危及账号，且非研究成果）；大权重/数据集按用户指示不传；>50MiB 不传 |
| **按模板整理** | `research/` 分类目录 + `README.md` 索引 + `UPLOAD-MANIFEST.json`（233 文件逐项路径/字节/SHA-256）；新建第 24 个不可覆盖检查点 `20261114T102224Z-r126-full-open/`（`CHECKPOINT.md` + `manifest.json` + `metrics.csv`）；`AGENTS.md` / `PROJECT.md` / `TASK.md` 按新范围重写或更新，`PROTOCOL.md` 规则本身无误故不动 |
| **上传内容（233 文件 / ~8.6 MiB）** | 稿件 5（TeX+PDF，含 R95 被评的 revision-r97、v2-R51 run、r93-candidate）；真实指标 10（10-seed 主矩阵 `metrics.json`/`metrics_completed.json`、独立族、i1、R63、R78、`qualified_paper.json`）；**全部 23 份独立/full/idea 评审报告全文**；guidance/契约 8（guidance-v2、execution-contract v1–v3、R107 目标迭代、G0 复核）；冻结协议包 30；研究思路 10（D1 v1/v2 提案 + 两轮独立复核 + 停摆决定 + G4 定位 + 文献矩阵）；**进展记录 10**（完整 `goal-ledger.md`、`STATUS.md`、11-10～11-14 工作日志）；R106–R125 轮次审计 129；harbor 试验 8 |
| **整理「之前不对的」** | ① 旧 `AGENTS.md` 写「no manuscript PDF/TeX / 无未投稿稿件 / 无本机路径 / 仅脱敏交接层」，与新指令冲突 → 已改；② 原先只有 7 份 `*-SANITIZED.md` 摘要 → 现补全 23 份评审原文、账本、日志、协议、轮次审计；③ **R110–R113 覆盖缺口**：R110/R111 在本地账本有正式轮次且已被既有检查点引用；**R112/R113 因并发保护只做只读检查、无实质产出、无独立产出目录** ⇒ 不补造检查点，在第 24 检查点中写明原因；④ 11 个 verifier/审计文件初判「credential-literal」是**误伤**（内容只是 `b"ghp_"` 等扫描模式串与叙述），复核后全部补传 |
| **校验** | 明确白名单逐个 `git add --`（**无 `git add .`**）；staged 242 文件 / 61,100 插入；真实 token 正则（`gho_`/`ghp_`/`AIza` 长串）0 命中；无 >50MiB / npz / pt / zip / dylib；`metrics.csv` 固定列只用实测值（主矩阵 real 0.815234375、nulls 0.4795–0.5039、chance 0.5；历史 7.5/6.0 标 historical；harbor 探针 360.0 / reward 1.0）。`--check` 21 条告警全部为**原始文件自带格式**（Markdown 硬换行尾空格、JSON 单行、txt 末尾空行），按「原文照传不改写」保留并登记。`checkpoint_manifest.py create/verify` 均通过（10 核心 artifacts，`input_git_head=58500f3220…`）；两次 commit 后 push，`git ls-remote` 远端 `d76bb642…` = 本地 HEAD ⇒ **已上传** |
| **诚实边界** | **本次上传不产生任何科学结果、不晋级任何门、不改分数**。governing 仍 R95 **6.0 / NOT_QUALIFIED**（门槛 >=7.0）、guard `INCOMPLETE`、0 篇达标、未写 COMPLETE；G0–G8 与所有 P 阶段仍 pending；历史 7.5 上传不改变「最新独立评审 governs」；稿件上传 ≠ 投稿/发表，双盲/优先权影响提示整合者；大权重/数据集仍缺，本仓库仍不能独立复现实验。主项目未 commit/push |


### R127 主会话：**按用户指令合并 agent 分支到默认分支 main**（2026-11-14 18:2x）

| 项 | 内容 |
|:--|:--|
| 用户指令 | 「把这个分支合并了吧」。按 `research-github-sync` 协议，合入默认分支是**整合者的验收动作**，用户即 `PROTOCOL.md` 指定的整合者且指令明确 ⇒ 授权成立；非 agent 自合并 |
| **合并前只读核验** | `git fetch` 后：本地/远端 `main=a0c2cf6…`、`agent=d76bb642…` 各自一致，工作树干净；分叉 `main` 独有 1 commit（仅一份引导 `README.md`）、`agent` 领先 26 commit / 324 文件；`git merge-tree --write-tree` 返回**单个 tree hash `f11a1439…`、stderr 空 ⇒ 无冲突**（试合并树 336 文件、含 `research/` 235 与 `README.md`）。注：一次 `grep conflict` 命中的是文档正文「data conflict / framing difference」等词，非合并冲突，已用 `merge-tree` 正名 |
| **执行** | `git checkout main` → `git merge --no-ff agent/r109-harbor-sync/wb-main -m "merge(...): integrator accepts 24 checkpoints and R126 full-open research archive into main"` ⇒ merge commit `74902cc`；随后修正合并后过时的 `README.md`（原文写「切到 agent 分支读」「仓库不含未投稿稿件」，与现状冲突）为默认分支入口说明；`PROTOCOL.md` 追加 **Merge record** 段、`AGENTS.md` 补分支策略，提交 `6cc2e4f`。`git push origin HEAD:refs/heads/main` 后 `git ls-remote` 远端 `6cc2e4f…` = 本地 HEAD ⇒ **已推送** |
| **远端终态** | `main` 为默认分支、PUBLIC；**336 文件**（`research/` 235、24 个检查点）；`agent/r109-harbor-sync/wb-main` **保留未删**（`d76bb642…`）；无 force push / 删分支 / Release |
| **验收边界（关键）** | 合并**只接受簿记记录，不是科学验收**：不过任何门、不改分数、不验证任何实验、不让稿件达标。governing 仍 R95 **6.0 / NOT_QUALIFIED**（门槛 >=7.0）、guard `INCOMPLETE`、0 篇达标、未写 COMPLETE；G0–G8 与所有 P 阶段仍 pending。已在 `PROTOCOL.md` Merge record 与 README 明文写明 |
| 交下轮 | 新检查点继续发布在 `agent/r109-harbor-sync/wb-main`；再次合入 `main` 仍需整合者明确指令，心跳不自行 merge |

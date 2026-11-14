# R128 — v1 verifier 缺陷登记（冻结留痕，不回写）

对应轮次审计 §5。本文件只登记缺陷与证据，不修改任何已落盘字节。

## E-1 [MEDIUM｜正则设计缺陷，非数据不一致 / 非编造]

- **对象**：`R128-VERIFY-v1.py` 的熵启发式 `kw` 正则；输出 `R128-VERIFICATION-V1.json`。
- **现象**：v1 报 **246 个 `entropy_secret_candidates` / 24 文件**，使 `C` 组 1 条 MISMATCH（35 检查 / 34 MATCH / 1 MISMATCH）。
- **根因**：正则前缀 `sk-` 无词边界保护，命中项目路径
  `Task-Aligned-Controls-for-Connectome-Vision` 中 `Ta` + **`sk-`** + `Aligned…`；
  后缀 `Aligned-Controls-for-Con…` 长度 38、Shannon 熵 3.81 ≥ 3.5 阈值 ⇒ 被误判为 OpenAI 风格密钥。
- **逐条分类证据**：246 / 246 候选的 `label` 全为 `sk-`（`Counter({'sk-': 246})`）；
  body 前 24 字符全为 `Aligned-Controls-for-Con`；纯 hex 计数 0 / 246；24 个文件全为含该路径字样的
  `UPLOAD-MANIFEST.json` / 检查点 / 账本 / 审计 / 脚本。⇒ **全部为同一路径字面造成的假阳性**，
  不是 246 个凭证，也不是公开树里有真实凭证值。
- **处置**：v2 在 `R128-VERIFY.py` 给每个前缀加 `(?<![A-Za-z0-9_\-])` lookbehind，
  并新增 `v1_task_path_false_positive_explained` 一条可复算检查；v2 结果
  **36 检查 / 36 MATCH / 0 MISMATCH**，真实凭证值 0、熵候选 0。
- **保留**：`R128-VERIFY-v1.py`、`R128-VERIFICATION-V1.json` 两文件原样冻结；
  v1 的 34/35 与 246 读数不被覆盖、不被删除、不被改写。

## 未发现的其他问题（如实记录）

- 采集脚本 `R128-ACQUIRE.py` 与 verifier 在 336 文件数、9,798,478 B 总字节、
  最大单文件 2,149,921 B、233 条清单、12 行公开数值 Overall、6.0 / `NOT_QUALIFIED`、
  `actions=0` 上逐项吻合。
- 19 个扫描模式字面文件已逐一取上下文核验；`AIza…` 命中为 R123 已记录的
  「上游脚本内嵌第三方公开 key ⇒ 落盘前删除、值从未打印 / 复制 / 记录 / 上传」，公开树中无该值。

## 教训（写入下轮）

1. 「零命中」类检查须用形态无关正则 + 词边界，并给 occurrences / distinct 口径。
2. 短前缀（`sk-`、`ghp_` 等）会嵌入普通英文单词 / 项目名；高熵后缀不等于凭证。
3. MISMATCH 必须先逐条分类定位根因，不得用「删掉模式」或「调低阈值」消除。
4. 缺陷脚本 / 输出两版全保留，修正在新版本，历史字节零回写。

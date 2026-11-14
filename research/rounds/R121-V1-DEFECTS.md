# R121 · v1 脚本缺陷留痕（只追加，历史读数不删不改）

所有 v1 产物完整保留：`R121-collect.py`、`R121-RAW-v1.json`、`R121-verify-v1.py`、
`R121-VERIFICATION-v1.json`。以下 6 处均为**脚本判定 / 枚举 / 转录缺陷**，
不是数据不一致、不是编造、不改变任何实质结论。

## 采集侧（v1 → v2）

| ID | 缺陷 | 后果 | 修正 |
|:--|:--|:--|:--|
| C-1 | `conditions.a.any_true` 把 11 份 `hypothesis_supported` 文件混为一类，未区分图类型 | 报 `any_true=True`，看似 R95 §13(a) 已满足 —— **假阳性** | v2 按同一文件 `data.source` 分类：6 份 `REAL_MALECNS_VISUAL_SUBGRAPH` 全 `False`；4 份 `SYNTHETIC_APPROXIMATION`（96 节点 XOR / task-aware 受控图）为 `True`。后者正是 R95 §8 M1 明确不计入的替身 |
| C-2 | `S16_main_tex` 指向 v2 run root（45,618 B）而非 R95 §1 版本锁定的稿件 | 报 `main_tex_admission=False` —— **假阴性** | v2 锁定 `R49-7.5-DELIVERY/manuscript/main.tex`（40,175 B / md5 `e4bfad51…158c6`，与 R95 §1 版本锁 md5 逐字一致），第 637 行命中 |
| C-3 | 轮次边界标签只扫前 8 行 | R114/R116/R118 标签为空 | v2 全文扫描，7/7 轮次均声明 `READONLY…NOT_GATE_PASS_NOT_SCIENTIFIC_RESULT` |

## 验证侧（v1 → v2）

| ID | 缺陷 | 后果 | 修正 |
|:--|:--|:--|:--|
| V-1 | `SELF-0` 正则把自身**输出写入行** `open(..., "w")` 误判为读取 R121 JSON | 1 处假 MISMATCH | 排除写模式行，改为「源码中不存在任何 R121 JSON 读取行」 |
| V-2 | 文件枚举漏 `metrics_from_trajectory.json` | 真实图 4 份 vs 6 份（两版全部 `False`，无实质差异） | 枚举三种 metric 文件名，6 份 |
| V-3 | 期望 md5 字面量截断 1 字符（31 vs 32） | 1 处假 MISMATCH | 补全 `…158c6` |
| V-4 | v1 在 `isolated/` 副本生成**之前**扫描 → 1 命中；验证器在**之后**运行 → 2 命中 | 1 处时序假 MISMATCH | v2 把「既有 provenance 副本」与「本轮自产 isolated 副本」分列；两者均与 r95 逐字节一致 |

## 结论不变

v2 独立复算 **74/74 MATCH / 0 MISMATCH**。三项升分条件 (a)(b)(c) 均 `satisfied=False`；
governing 仍 R95 = 6.0；`NOT_QUALIFIED` / `INCOMPLETE`；0 篇达标。
v1/v2 两版读数均保留，供独立复核。

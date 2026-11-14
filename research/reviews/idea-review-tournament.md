# CCFA Idea Review — 四候选排名汇总（standard mode / tournament）

来源：平台 AI 任务 15274 的 4 个 idea。协议：`ccf-idea-reviewer` standard + `rubric.md` + `calibration.md` + `strict-idea-review.md` + `expert-panel.md` + `ccf-common/references/review-output-standards.md`。
**这是 idea 阶段评审，不计入论文 P9 达标计数，不生成 `qualified_papers.json`。**

## Venue lens

CVPR 2027 主轨（8 页 + 参考文献、双盲、2026-11-16 AoE）。约束：单卡 48GB、公开数据、无新增生理记录、当前 exp-4090 池 eligible_nodes=0（外部条件，计入 feasibility 不记为 idea 缺陷）。

## Search basis（更新见下方日期复核）

原始四方向 tournament 的检索截至 2026-11-06 之前；当时 `idea_delay` / `idea_causal` 有检索缺口。2026-11-06 对 `idea_delay` 做了专项检索，新增核实果蝇 delay/non-delay 运动视觉回路、可学习 SNN 延迟、2026 connectome visual scale generalization 与 event-flow SNN。专项复核见 `idea-delay-recheck-20261106.md`；分数已更新到 `scores.json`，旧 `idea_delay` 单项报告保留作历史记录。

## 独立打分后排名（按 serious-risk-adjusted score）

| 排名 | Idea | Weighted (1-5) | Overall (1-10, derived) | Recommendation |
|---:|---|---:|---:|---|
| 1 | 固定连接组上的稀疏因果子回路发现 (`idea_causal`) | 3.14 | 6.28 | pivot-with-rescue-route；method soundness<=2 且需补检索 |
| 2 | 不确定性鲁棒的跨连接组 SNN (`idea_robust`) | 3.06 | 6.12 | pivot-with-rescue-route；novelty<=2 且高置信 |
| 3 | 双侧对称等变与损伤鲁棒视觉 SNN (`idea_bilateral`) | 2.68 | 5.36 | pivot-with-rescue-route / venue-switch；novelty<=2、venue<=2 |
| 4 | 形态代理约束的突触延迟与时间编码 (`idea_delay`) | 2.58 | 5.16 | pivot-with-rescue-route；专项复核见 `idea-delay-recheck-20261106.md` |

> 权重：Problem 12 / Novelty 14 / Conceptual 12 / Soundness 14 / Elegance 8 / Feasibility 8 / Experimental 10 / Venue 8 / Timeliness 6 / Acceptance 8。
> **没有候选达到 `accept-to-develop`（>=4.3）或 `revise`（3.7–4.2）**；最高 3.28 仍落在 pivot / needs-literature-search 区间。

## Fatal gates 命中

| Idea | Gate | 依据 | 封顶结果 |
|---|---|---|---|
| idea_robust | novelty<=2 且高置信 | arXiv:2610.29205 已做 9 版本跨重建鲁棒性 | pivot-with-rescue-route |
| idea_bilateral | novelty<=2 + venue fit<=2 | 2404.17128 附录 S3/S4 + Nature Neuro 2025 | pivot / venue-switch |
| idea_causal | method soundness<=2 | 「因果」≠模型内反事实；百万边逐边消融不可判定 | pivot-with-rescue-route |
| idea_delay | novelty 检索不足 | 三条 2025–2026 相关条目未逐条核验 | needs-literature-search（novelty 封顶 3） |

## Best historical candidate (not qualified for development)

当前没有候选达到 `accept-to-develop`；`idea_causal` 仅是四个旧候选中数值最高者，method soundness fatal gate 仍未解决，不是可直接推进的 winner。`idea_delay` 在专项检索后降至 5.16/10，未通过 idea gate。

## Backup idea

`idea_causal`（weighted 3.14）：可复用成分是「预算约束下跨种子稳定的子图」，但须先降级因果措辞并补 pruning/NAS 非重复检索。

## Ideas to pivot / rescue

- `idea_robust`：收窄到 MaleCNS v1.0 视叶子图的突触检测阈值扰动 + 校准 Pareto，跨数据集降为次要验证。
- `idea_bilateral`：只保留「左右交换等变误差」度量，放弃双侧鲁棒性作为主贡献，重新判断 venue。
- `idea_delay`：专项检索已完成；需先形成独立 CV 任务/机制并用神经活动校准，否则停止该路线。
- `idea_causal`：causal → task-necessary subgraph，逐模组反事实，主指标改跨种子细胞类型富集。

## Upgrade plan for the winner（进 guidance 之前必须完成）

1. 不因历史 rank 启动 `idea_causal` 或 `idea_delay`；先对新候选做 closest-work 搜索和独立 CCFA review。
2. 只有 idea review >8/10 才写 guidance、收缩数据子图或做任务 smoke。
3. exp-4090 仍须先变为 ready 且 `eligible_nodes>=1`，再提交最小 smoke。
4. 任一条件失败即保留否决，不降低 idea 或 paper gate。

## Checklist / self-check

四候选均独立打分后才比较；fatal gates 单独应用；未把低 readiness 直接翻译成 abandon；未编造 prior art、实验结果或接收概率；分数可复核；无未填字段。

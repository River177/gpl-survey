# `tex/` 改稿时间线

> 基于 [Tex-详细改稿计划.md](/mnt/d/Graph/gpl-survey/docs/papers/Tex-详细改稿计划.md) 制定。  
> 目标：在保证你有时间阅读新增文献的前提下，稳妥完成整篇 survey 的升级改稿。  
> 适用场景：你需要边读文献边改稿，而不是一次性机械补文献。

---

## 1. 总体节奏

建议按 **6 周** 推进。

这样安排的原因是：

- 第 5 章是结构性重写，不适合在没有充分阅读的情况下直接动笔。
- taxonomy、applications、discussion 这些章节会受到第 5 章改动牵引，必须留出“先读后改”的缓冲。
- 图表、summary table、bib 最好后置，否则容易返工。

如果你时间非常紧，也可以压缩成 4 周，但风险是第 5 章和 taxonomy 容易写得过于仓促。

---

## 2. 时间线总览

### 第 1 周：读主线文献 + 定新版框架

目标：

- 搞清楚 2024-2026 的核心增量到底是什么
- 定 taxonomy 和第 5 章的新骨架

重点阅读：

- ProG: A Graph Prompt Learning Benchmark
- Does Graph Prompt Work? A Data Operation Perspective with Theoretical Analysis
- Graph Prompting for Graph Learning Models: Recent Advances and Future Directions
- Edge Prompt Tuning for Graph Neural Networks
- GraphTOP: Graph Topology-Oriented Prompting for Graph Neural Networks
- Instance-Aware Graph Prompt Learning

本周产出：

- 确定“正文主线文献池”
- 确定新版 taxonomy
- 确定 `5.tex` 的新目录结构

建议分配：

- 40% 时间读文献
- 40% 时间做笔记和归类
- 20% 时间改 `2.methodology.tex` 的结构草案

里程碑：

- 你能明确回答：
  - graph prompt 在 2024-2026 的新增主线有哪些
  - 第 5 章为什么不能继续按旧两分法写

---

### 第 2 周：集中改第 5 章主体

目标：

- 完成全书最关键的技术主章重写

重点阅读：

- RELIEF
- IGAP
- DAGPrompT
- GraphPrompter
- One Prompt Fits All
- MAGPrompt

需要回看的旧文献：

- GPPT
- GPF / GPF-Plus
- All in One
- GraphPrompt
- PRODIGY

本周主要工作：

- 重写 `tex/5.tex`
- 起草新版 `tex/table/graph_prompt_summary.tex`

建议分配：

- 30% 时间读新增方法
- 60% 时间改 `5.tex`
- 10% 时间补主表框架

里程碑：

- `5.tex` 的结构已经换新
- 主线代表作已经选定
- discussion 小节已纳入 benchmark / theory 支撑

---

### 第 3 周：回改前文，让引言和方法学对齐

目标：

- 避免“第 5 章是新版、前文还是 2023 版”的断裂

重点阅读：

- 重新快速浏览第 1 周和第 2 周所有主线文献的摘要与 introduction
- 重点回看：
  - ProG
  - Does Graph Prompt Work?
  - Graph Prompting for Graph Learning Models

本周主要工作：

- 改 `tex/0.main.tex` 的 abstract
- 改 `tex/1.intro.tex`
- 改 `tex/2.methodology.tex`
- 轻改 `tex/3.Preliminaries.tex`
- 轻改 `tex/4.Pre-training.tex`

建议分配：

- 20% 时间复盘文献
- 50% 时间改引言和方法学
- 30% 时间处理 preliminaries / pre-training 的衔接

里程碑：

- abstract 和 introduction 的时间口径已经后移
- methodology 的 taxonomy 与新版第 5 章一致
- 前文不再把 graph prompt 写成只有少量工作的 early-stage direction

---

### 第 4 周：改 applications、ProG、discussion

目标：

- 把后半部分从泛泛展望，改成和新文献匹配的复杂场景总结

重点阅读：

- GPT4Rec
- Prompt Learning on Temporal Interaction Graphs
- Prompt-Based Spatio-Temporal Graph Transfer Learning
- P2TAG
- Prompt-Driven Continual Graph Learning
- FedGPL
- GP2F
- Event-Aware Prompt Learning for Dynamic Graphs
- Adversarial Graph Prompting

本周主要工作：

- 重写 `tex/6.Applications.tex`
- 升级 `tex/7.ProG.tex`
- 重写 `tex/8.Discussion.tex`
- 扩写 `tex/9.Conclusion.tex`

建议分配：

- 35% 时间读“复杂场景”文献
- 50% 时间重写后半部分
- 15% 时间统一挑战/未来方向/结论口径

里程碑：

- applications 不再只是“未来有潜力”的泛泛讨论
- ProG 被写成 benchmark + ecosystem
- discussion 章节已经覆盖 benchmark、theory、transfer、dynamic、robustness

---

### 第 5 周：补 bibliography、重做图表和 summary table

目标：

- 让正文与图表、表格、引用系统彻底同步

本周主要工作：

- 更新 `tex/zotero.bib`
- 重做 `tex/table/graph_prompt_summary.tex`
- 重做 `tex/pic/taxonomy.tex`
- 视需要更新：
  - `tex/pic/prompt.pdf`
  - `tex/pic/reference_venue.pdf`
  - `tex/pic/top_keywords_bar.png`

阅读任务：

- 这周不建议再大规模读新文献
- 只针对“需要补 bib 的文献”查 DOI、venue、作者顺序等细节

建议分配：

- 20% 时间补 bib 元数据
- 50% 时间重做表格和 taxonomy 图
- 30% 时间做引用一致性检查

里程碑：

- 主线引用都已补齐
- summary table 能反映新版 taxonomy
- 图表与正文不会再冲突

---

### 第 6 周：统一语言、编译验证、最后修订

目标：

- 完成一版可提交/可继续润色的稳定稿

本周主要工作：

- 统一术语和语气
- 删除过时表述：
  - recently
  - nascent
  - first
  - only a few works
- 检查交叉引用和 bibliography
- 跑完整编译链
- 修复 warning 和排版问题

阅读任务：

- 不再新增阅读，只做针对性核对

建议分配：

- 20% 时间统一语言
- 30% 时间编译和修 warning
- 30% 时间核对图表与引用
- 20% 时间做最后的小修小补

里程碑：

- 可以产出一版结构统一、引用完整、可编译的稿件

---

## 3. 每周阅读负载建议

为了避免“边改边补文献导致失焦”，建议控制每周阅读量。

### 第 1 周

- 精读 6 篇
- 每篇做 5 条笔记：
  - 核心问题
  - prompt 注入位置
  - task alignment 机制
  - optimization 方式
  - 适合放在哪个小节

### 第 2 周

- 精读 4-6 篇方法论文
- 快速回顾 4-5 篇旧代表作
- 目标是能写出“演进线”，不是堆摘要

### 第 3 周

- 以回看摘要和 introduction 为主
- 不新增大量论文

### 第 4 周

- 精读 6-8 篇复杂场景论文
- 每篇重点看：
  - 场景设定
  - 为什么 prompt 在这里必要
  - 是否值得进入正文主线

### 第 5-6 周

- 不再系统扩读
- 只针对引用和事实做核对

---

# 稿件基线记录（Task 1）

- 记录时间：2026-04-12
- 对应任务：`Task 1 / CP0`
- 记录范围：`tex/0.main.tex`、`tex/1.intro.tex`、`tex/2.methodology.tex`、`tex/5.tex`、`tex/6.Applications.tex`、`tex/8.Discussion.tex`

## 1. 基线编译状态

- 执行命令：`pdflatex -interaction=nonstopmode -halt-on-error 0.main.tex`
- 执行目录：`tex/`
- 结果：编译成功，退出码为 `0`
- 产物：`tex/0.main.pdf`

## 2. 当前章节布局

当前稿件顶层结构如下，尚未发生顶层章节重组：

1. `Introduction`
2. `Survey Methodology`
3. `Preliminaries`
4. `Pre-training GNNs for Graph Prompting`
5. `Prompt Design for Graph Tasks`
6. `Graph Prompting in Multi-Modal and Multi-Domain Areas`
7. `Potential Applications`
8. `ProG: A Unified Library for Graph Prompting`
9. `Challenges and Future Directions`
10. `Conclusion`
11. `Acknowledgments`

## 3. 主要图表与支撑材料

- 引言部分含 2 个主要图：`ThreeChallenges.pdf`、`PromptExample.pdf`/`pt.pdf`
- 方法学部分含 1 个 taxonomy 图、1 张 `Research Objectives` 表、2 个统计图：`reference_venue.pdf`、`top_keywords_bar.pdf`
- 预训练部分含 1 个总览图：`pretraining.pdf`
- Taxonomy 主体章节含 1 个 prompt 结构图：`prompt.pdf`
- ProG 章节含 1 个工具架构图：`ProG_pipeline.pdf`
- 结构化汇总表文件位于 `tex/table/graph_prompt_summary.tex`

## 4. 编译日志中的主要警告

本次编译没有致命错误，但日志中仍存在以下需要后续处理的非阻塞问题：

- `LaTeX Warning: No \author given.`
- `Package caption Warning: Unknown document class (or package), standard defaults will be used.`
- 多处 `Overfull \hbox` / `Underfull \hbox`
- `IEEEtranSN.bst: No hyphenation pattern has been loaded for the language 'en'`

这些问题不会阻止当前基线编译，但会影响最终投稿稿件的整洁性与版面质量。

## 5. 当前显著的陈旧内容与修订风险

### 已经移除的陈旧内容

- `tex/0.main.tex` 中此前提到的红色投稿/拒稿说明在当前版本中已不存在。

### 仍然需要尽早处理的陈旧或不一致内容

- `tex/5.tex` 仍主要以旧版代表性工作为主，尚未体现 2024-2026 文献刷新。
- `tex/6.Applications.tex` 尚未承担“不适配 taxonomy 的近年方法”的 overflow 角色。
- `tex/7.ProG.tex` 仍主要把 ProG 表述为统一工具库，而不是已发表 benchmark/toolkit 论文。
- `tex/8.Discussion.tex` 仍是旧版挑战与展望，尚未反映 graph-LLM、评测碎片化、prompt 可解释性等近年趋势。
- 统计图与关键词图仍沿用旧版数据来源，尚未证明与扩展后的论文池一致。

## 6. 当前修订边界确认

本轮修订在基线阶段确认以下编辑策略：

- 保持 `tex/0.main.tex` 的顶层章节顺序不变。
- 保持 `tex/pic/taxonomy.tex` 的 taxonomy 主干不变，除非出现事实性错误才做最小修补。
- 近期论文优先并入现有 taxonomy 节点，而不是新增 taxonomy 大类。
- 不适配既有 taxonomy 的近年方法，转移到 `tex/6.Applications.tex` 和 `tex/8.Discussion.tex`。
- 优先进行文字层面刷新，而不是结构性重写。

## 7. 对后续任务的直接含义

- `Task 2` 需要补齐一个可操作的 2024-2026 论文池，而不是只依赖已有正文引用。
- `Task 3` 需要显式形成“论文 -> taxonomy / applications / discussion”的映射文档。
- `Task 4` 已完成前言三部分的大部分文字刷新，但仍缺 ProG 定位统一。
- `Task 5-8` 仍属于未启动或未落到正文的状态。

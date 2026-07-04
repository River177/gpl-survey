# 中优先级正文问题修改方案

> 生成时间：2026-07-04  
> 范围：`docs/audits/待修复问题清单.md` 中 C 部分 W1--W5。  
> 处理原则：本文只给解释和修改方案，暂不修改 TeX 正文，等待审查确认后再执行。

## 1. 总体判断

C 部分的问题都属于写作与局部一致性问题，不涉及新增文献或大结构调整。建议一次性处理，因为它们分布在前言、方法学、预备知识和 Section 5 开头，彼此没有强依赖。修改时应保持语气自然，避免留下"修补痕迹"。其中 W1 和 W4 建议做轻度润色，而不是只替换单词；W2 和 W3 是确定性修正；W5 是小范围叙事对齐。

## 2. W1：`project vector` 术语错误与 GraphPrompt 段落衔接

### 当前问题

`tex/5.tex:87` 中有一句：

```latex
It is worth noticing that the role of their prompt token is very similar to the project vector in the graph attention network.
```

这里 `project vector` 应为 `projection vector`。但只改拼写还不够，这一整段把 HetGPT、GraphPrompt、graph attention / graph pooling 放在一起，衔接略生硬。尤其 "they can only deal with node classification tasks"、"To this end" 和 "It is worth noticing" 都比较口语和直接，读起来像早期草稿。

### 建议方案

建议把整段改成更稳的对比段，核心意思保留：HetGPT 用异构类型提示，GraphPrompt 用 prompt token 影响 readout，prompt token 与 projection/attention-style pooling 有相似性，但用途不同。

建议替换为：

```latex
HetGPT \cite{ma2023hetgpt} extends prompt tokens to heterogeneous graphs by adding type-specific feature tokens, but its task formulation mainly targets node classification. GraphPrompt \cite{liu2023graphprompt} takes a different route by using prompt tokens to steer the readout over induced subgraphs and by reformulating node and graph classification through graph-pair similarity. This prompt-guided readout is related in spirit to projection or attention-based graph pooling, but its purpose is different: the prompt is introduced to align downstream prediction with the pre-training interface rather than only to summarize node embeddings.
```

### 预期效果

这会同时修正 `projection` 拼写、减少生硬转折，并把 GraphPrompt 和 graph pooling 的关系解释得更清楚。

## 3. W2：关键词图 label 与 caption 不一致

### 当前问题

`tex/2.methodology.tex:76,85-86` 中正文引用 `fig:top10keys`，但图注写的是 "Top 15 Keywords appeared in titles of collected papers"。问题有两个：

1. label 叫 `top10keys`，但图是 Top 15；
2. 图注语法不自然，`Keywords appeared` 应改为 `keywords appearing`。

### 建议方案

建议同时改正文引用、subfloat label 和图注：

```latex
Figure \ref{fig:top15keys} shows the most frequent keywords in their titles.
```

```latex
\subfloat[Top 15 keywords appearing in titles of collected papers.]{
\label{fig:top15keys}
\includegraphics[width=0.46\textwidth]{pic/top_keywords_bar.pdf}%
}
```

如果担心 label 改动影响其他引用，应全局搜索 `fig:top10keys`。当前主要引用在 `tex/2.methodology.tex` 的 Literature Overview 段，改起来风险低。

### 预期效果

这是确定性清理，能消除 label 与图意不一致的问题。

## 4. W3：Pre-training and fine-tuning 主谓一致

### 当前问题

`tex/3.Preliminaries.tex:38` 写：

```latex
Pre-training and fine-tuning has become a common transfer paradigm in graph representation learning.
```

主语可以理解为两个动作，也可以理解为一个 paradigm。当前写法语法上容易被挑错。

### 建议方案

推荐改为单数范式表达，更自然：

```latex
The pre-training and fine-tuning paradigm has become a common transfer paradigm in graph representation learning.
```

如果想避免 "paradigm" 重复，可写：

```latex
The pre-training and fine-tuning workflow has become a common transfer paradigm in graph representation learning.
```

推荐第二句，因为更顺。

### 预期效果

修正主谓一致，同时避免读者纠结 "pre-training and fine-tuning" 是两个并列动作还是一个整体流程。

## 5. W4：引言图注类比过强

### 当前问题

`tex/1.intro.tex:62` 的图注写：

```latex
Inspired by the language prompt, a graph prompt can be also used with graphs in the same way.
```

这句话有语法问题，也和正文后文的核心观点冲突。后文明确强调 graph prompting 不是 NLP prompting 的直接复制，因为图有 topology、feature transformation 和 message passing。图注如果说 "in the same way"，会削弱这个区别。

### 建议方案

建议把整个 caption 改得更谨慎，同时保持简洁：

```latex
\caption{Language prompt vs. graph prompt. A textual prompt modifies the input so that a pre-trained language model can perform a new task, such as multiple-choice question answering. A graph prompt follows the same adaptation intuition, but it must operate on graph features, structures, or task interfaces rather than on text alone.}\vspace{-3ex}
```

也建议顺手把 `v.s.` 改成 `vs.`，这是更常见写法。

### 预期效果

图注会和后文论述一致：prompting 的适配思想相通，但 graph prompt 的具体机制不同。

## 6. W5：Section 5 开头与 Q1/Q3 的关系

### 当前问题

`tex/5.tex:2` 写：

```latex
Based on these components, and following \textbf{RQ3} (Section~\ref{sec:method}), we analyze prompt design along four aspects...
```

但 `tex/2.methodology.tex` 的表格中 Q1 是 unified framework，Q3 是 graph prompt design。Section 5 实际同时承担 Q1 和 Q3：它既建立 token/structure/insertion framework，也讨论 how to design prompts。只说 "following RQ3" 不算大错，但不够精确。

### 建议方案

建议改成：

```latex
Based on these components, and following Q1 and Q3 in Section~\ref{sec:method}, we analyze graph prompt design along four aspects: how a graph prompt is constructed; how downstream tasks are reformulated toward the pretext; how a graph prompt is learned; and what trade-offs connect existing designs.
```

后一句也可以顺手把 "what the connections, pros, and cons of existing designs are" 改成更自然的 "what trade-offs connect existing designs"。这不会改变结构，但更像论文正文。

### 预期效果

Section 5 与方法学问题表的关系更准确，也减少 "RQ3 下面塞了四个问题" 的不协调感。

## 7. 建议执行顺序

建议一次性修改这些文件：

1. `tex/5.tex`：处理 W1 和 W5；
2. `tex/2.methodology.tex`：处理 W2；
3. `tex/3.Preliminaries.tex`：处理 W3；
4. `tex/1.intro.tex`：处理 W4；
5. 编译英文稿；
6. 若通过，再更新 `docs/audits/待修复问题清单.md`，将 W1--W5 标为已修复。

## 8. 风险与注意事项

这组修改风险低，但有两个注意点：

1. 改 `fig:top10keys` 为 `fig:top15keys` 后，需要确认全局没有残留 `fig:top10keys`；
2. W1 的 GraphPrompt 段落涉及方法解释，建议不要再扩写太多，否则会改变 Section 5 篇幅和局部节奏。

## 9. 本次不执行的内容

本文档不修改 TeX 文件。待确认后，可按上面的建议批量执行，并用 `cd tex && latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build 0.main.tex` 验证。

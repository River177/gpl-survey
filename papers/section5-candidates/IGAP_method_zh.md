# IGAP 方法详解

## 论文信息

论文标题是 *Inductive Graph Alignment Prompt: Bridging the Gap between Graph Pre-training and Inductive Fine-tuning From Spectral Perspective*。该工作发表于 `WWW 2024`，DOI 为 `10.1145/3589334.3645620`。论文提出的方法名为 `IGAP`，全称是 `Inductive Graph Alignment Prompt`。

## 一句话定位

IGAP 不是简单把下游任务改写成预训练任务的另一种 prompt 模板，而是试图回答一个更难的问题：当预训练图和下游图在归纳场景下并不兼容时，如何显式地补偿它们之间的数据分布差异，并把预训练得到的知识尽可能稳地转移过去。

## 它要解决什么问题

这篇论文的出发点很明确。此前的图 prompt 方法大多默认预训练图和下游图是相容的，因此方法通常更适合 transductive 场景，或者至少要求预训练和下游数据来自相近分布。可一旦进入 inductive fine-tuning，图的节点特征分布和结构模式都可能明显变化，旧方法只做任务形式改写就不够了。

IGAP 认为这里至少存在三层错位。第一层是图信号差异，也就是节点特征本身发生偏移或扰动。第二层是图结构差异，更准确地说，是从谱域角度看，预训练图与下游图的低频结构模式并不对齐。第三层是任务类型差异，即预训练任务和下游监督任务本身并不完全一致。IGAP 的核心贡献，就是分别为这三层错位设计对应的 prompt 机制。

## 方法总览

IGAP 的方法框架可以概括成三步。第一步，它先用谱图理论重新解释主流图预训练，指出预训练过程主要对齐的是图信号中的低频成分，而不是所有频率成分。第二步，它据此把 inductive transfer 中的数据 gap 拆成图信号 gap 和谱空间 gap，并为这两类 gap 设计可学习 prompt。第三步，它再加入一个 label prompt，把下游任务的标签空间和预训练目标对齐。

因此，IGAP 不是单一 prompt，而是一个三模块组合方法：`graph signal prompt`、`spectral space alignment prompt` 和 `label prompt`。

## 三个关键模块

### 1. Graph Signal Prompt

这个模块对应的是节点特征层面的偏移。作者的判断是：在 inductive 迁移里，下游图的节点属性可能和预训练时见过的属性分布差别很大，导致预训练编码器看到的输入信号已经不在原来的工作区间内。为了解决这个问题，IGAP 在输入信号层面加入一个可学习的补偿项，也就是 graph signal prompt。它的作用不是重新定义任务，而是直接修正输入图信号，让下游图在进入预训练 GNN 之前先被“拉回”到更适合迁移的区域。

这个设计和很多早期图 prompt 方法不一样。后者更像是在图中附加 token、边或伪节点，主要服务于任务改写；IGAP 这里更像是在做输入补偿。

### 2. Spectral Space Alignment Prompt

这是 IGAP 最有代表性的部分。作者认为，图预训练的可迁移知识主要体现为低频谱成分上的对齐，因此如果预训练图和下游图在谱空间中错位，即便任务形式一致，迁移效果也会很差。于是论文引入了 spectral space alignment prompt，目标是对齐下游图与预训练知识相关的低频谱子空间，尤其是若干最小特征值对应的谱成分。

从方法角色上看，这个 prompt 不再只是在原图上拼接一个提示结构，而是显式介入图的谱表示空间。也正因为如此，IGAP 和 GPPT、GraphPrompt、All in One 这类方法的差异很大。后者的 prompt 主要发生在输入结构层或任务映射层，IGAP 则把重点放在“让预训练知识真正可转移”的空间对齐上。

### 3. Label Prompt

前两个模块解决的是输入和结构层面的错位，label prompt 则解决任务层面的错位。作者把它作为一个任务对齐器，用来把下游分类任务重写成更接近预训练目标的形式。这样做的好处是，下游监督信号不需要完全另起一套学习逻辑，而是能沿着预训练模型已经学会的预测机制继续工作。

从论文整体结构来看，label prompt 在 IGAP 中不是唯一主角，但它是必要的闭环。没有这个模块，前面做完信号和谱空间对齐后，仍然可能在输出任务上发生脱节。

## 训练与推理流程

IGAP 的训练流程可以理解为“先分析预训练本质，再按 gap 分解做 prompt 适配”。在实现上，作者先保留预训练 GNN 的主体知识，然后对 graph signal prompt、spectral alignment prompt 和 label prompt 进行学习。训练目标同时兼顾谱空间对齐和下游任务损失。推理时，下游图先经过信号补偿和谱空间对齐，再进入预训练编码器，最后借助 label prompt 完成预测。

这种流程的优点是清楚。它没有把所有问题都丢给 end-to-end fine-tuning，也没有假设 prompt 自己就能弥合所有 gap，而是把问题拆开分别处理。

## 相比已有方法的新意

IGAP 的第一点新意，是把 graph prompting 从“任务改写”推进到“预训练知识迁移条件的显式建模”。这使它和只在下游侧加 prompt 的方法不在一个层级上。第二点新意，是引入谱域视角来解释为什么某些预训练知识能迁移、某些不能迁移，并据此设计 alignment prompt。第三点新意，是它明确面向 inductive fine-tuning，而不是只在 transductive 或半监督场景里展示效果。

如果你要在 survey 里找一篇能代表“2024 年后 graph prompting 开始更认真处理分布差异和迁移条件”的论文，IGAP 是很合适的。

## 适合加入表格的原因

IGAP 适合进主方法表，原因有三点。第一，它是正式发表的 `WWW 2024` 方法，不是只停留在 arXiv。第二，它的方法边界很清楚，确实是一篇 prompt 方法论文，而不是 benchmark、survey 或理论分析。第三，它覆盖了你当前表里较弱的一块，也就是 `pre-training to inductive adaptation`。

如果要放进 [graph_prompt_summary.tex](D:/GPL/gpl-survey/tex/table/graph_prompt_summary.tex)，比较合理的映射方式是：它仍然属于基于预训练的 prompt tuning 路线，但 prompt component 不能只写成普通 token 或 prompt graph，而应强调 `signal alignment + spectral alignment + label prompt`。下游任务可标为 `node / graph classification`，prompt tuning 应标为 `learnable`。

## 它可能替换谁

如果表格长度需要控制，IGAP 最适合替换 `ULTRA-DP`。原因不是二者完全同类，而是 IGAP 更成熟、已正式发表、方法贡献更清楚，也更能代表 2024 年以后 prompt 方法开始认真处理 inductive gap 的趋势。

## 局限和阅读时要注意的地方

IGAP 的方法很强，但也有边界。第一，它的方法解释高度依赖谱图理论，因此适合那些结构差异确实能通过谱空间失配来刻画的场景。第二，它虽然引入了谱空间 alignment，但这也意味着实现和解释都比普通 prompt token 方法更重。第三，它更强调预训练知识在 inductive 迁移中的保留与补偿，不是那种最简洁、最容易复用到所有任务上的通用 prompt 模板。

对你的 survey 来说，IGAP 最重要的价值不只是实验结果，而是它把 graph prompting 的研究重心从“怎么改写任务”往“怎么对齐分布和迁移条件”推了一步。

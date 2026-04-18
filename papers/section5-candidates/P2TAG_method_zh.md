# P2TAG 方法详解

## 论文信息

论文标题是 *Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs*。该工作发表于 `KDD 2024`，DOI 为 `10.1145/3637528.3671952`。论文提出的框架名为 `P2TAG`。

## 一句话定位

P2TAG 的关键不只是“在 TAG 上做 prompting”，而是把 `LM + GNN 联合预训练` 和 `graph-text mixed prompt` 接在一起，专门面向 `text-attributed graphs` 上的小样本节点分类。

## 它要解决什么问题

Text-attributed graph 同时包含文本和结构，两类信息都很重要。此前 few-shot node classification 方法往往直接使用预处理好的节点特征，而不真正利用原始文本；一些后来的方法虽然把 LLM 或文本 prompt 加进来了，但常常只从文本侧做 prompt，或者让 LM 与 GNN 的训练仍然相对分离。这样一来，模型要么忽视结构，要么没能真正把文本和结构融合起来。

P2TAG 针对的就是这类断裂。它认为在 TAG 上做小样本分类，问题不应被拆成“先学文本，再补结构”，而应该在预训练阶段就联合学习 LM 与 GNN，在 prompt 阶段再同时利用图和文本两条线索。

## 方法总览

P2TAG 由两个阶段组成。第一阶段是联合预训练，目标是让语言模型和图神经网络在 TAG 上共同学习节点表示。第二阶段是 mixed prompt learning，目标是通过同时引入 graph prompt 和 text prompt，把预训练阶段学到的能力迁移到 few-shot node classification 上。

因此，P2TAG 和只做图 prompt 的方法不同，也和只做 text prompt 的方法不同。它最核心的设计，就是 `graph-text mixed prompt`。

## 阶段一：联合预训练

P2TAG 的预训练不是让 GNN 和 LM 各做各的。作者先对 TAG 进行随机游走式子图采样，再把每个 mini-batch 子图送入语言模型进行文本编码，同时把 LM 的输出送给 GNN 聚合邻居信息。预训练目标则使用改造后的 `masked language modeling`。

这里最值得注意的是，作者并没有放弃 LM 原生的 MLM 目标，而是把邻域聚合信息注入到 `[MASK]` 位置的预测中。这样做的好处是：文本建模仍然保留 LM 强项，但图结构也进入了文本恢复过程。换句话说，P2TAG 不是简单拼接一个 LM 和一个 GNN，而是通过 MLM 把结构信息真正卷进文本预训练里。

## 阶段二：Graph-Text Mixed Prompt Learning

### 1. Graph Prompt

P2TAG 在下游 few-shot 任务中引入一个辅助 prompt graph。这个 prompt graph 不是随便初始化的，而是用 `label text embeddings` 来初始化。作者把类别标签对应的文本先编码成向量，再把这些向量作为 prompt graph 中关键节点的初始表示，让目标节点在消息传递过程中自然朝向类别语义空间靠近。

这一步设计很巧。传统文本 prompt 往往需要写离散模板句子，图上则常见手工构造伪节点或 prompt token。P2TAG 的做法相当于把“标签词语义”直接投进图 prompt 中，使图结构传播与标签语义对齐同时发生。

### 2. Text Prompt

P2TAG 还保留了一条文本侧 prompt 路线。与复杂的手工 prompt 不同，作者更倾向于简单、可学习的文本 prompt，由 LM 输出初始化。这样做有两个优点。第一，它减少了人工模板设计。第二，它和图 prompt 的初始化方式一致，都是让 prompt 更自然地接上预训练阶段的表示空间。

### 3. Mixed Prompt 的意义

P2TAG 的 mixed prompt 不是把 graph prompt 和 text prompt 机械拼起来，而是让两者共同模拟预训练阶段 `LM + GNN` 的联合工作方式。作者强调，单独从 LM 一侧做 soft text prompt，或者单独从图一侧加 prompt graph，都不能充分利用 TAG 的双重信息；mixed prompt 的意义就在于把结构和文本一起用于 few-shot 迁移。

## 它和现有 TAG 方法的差异

P2TAG 在论文里明确对比了 TAPE、ENG、GPrompt、G2P2 等方法。和这些方法相比，它至少有三处不同。第一，它在预训练阶段就联合优化 LM 与 GNN，而不是只在下游时把文本编码接入图模型。第二，它的 prompt 不是纯 text prompt，也不是纯 graph prompt，而是两者混合。第三，它使用标签文本嵌入来初始化 prompt graph，这个设计在 TAG 场景下非常自然，也确实形成了方法辨识度。

论文附录还专门强调了它和 GPrompt 的区别。GPrompt 更像是把整个 GNN 当作 prompt 适配器来用，而 P2TAG 则冻结主体模型，通过一个额外的 prompt graph 去改变输入结构。这种设计既保留了预训练知识，也减少了需要训练的参数。

## 训练与推理流程

训练时，P2TAG 先在 TAG 上做联合自监督预训练，学习 LM、GNN 和下游头部的协同表示。之后进入 few-shot 阶段，模型冻结主体参数，只优化 mixed prompt 相关部分。推理时，目标节点既看到文本 prompt，也通过 prompt graph 接收到标签语义和结构线索，再由 GNN 完成聚合并输出预测。

论文还说明了为什么最终选择 `GAT` 作为 GNN backbone：因为它能更自适应地控制 prompt graph 向目标节点传递多少信息，这与该方法的 prompt 设计更匹配。

## 相比已有方法的新意

P2TAG 的新意主要有三点。第一，它把 TAG 上的预训练与 prompting 真正接起来，而不是只写成一个“先预训练、再提示”的松散流程。第二，它提出了 `graph-text mixed prompt`，明确把结构提示和文本提示合并。第三，它用标签文本初始化 prompt graph，让标签语义和图消息传递直接联动。

如果你想在 survey 里证明 `graph prompting` 已经不局限于纯结构图，而开始向 `text-attributed graph` 和多模态场景扩展，P2TAG 是一篇很合适的代表论文。

## 适合加入表格的原因

P2TAG 很值得加入方法表，但前提是你愿意让表格覆盖 TAG 或多模态扩展路线。它是 `KDD 2024` 正式发表论文，任务边界清晰，方法贡献明确，而且能补上当前主表里最缺的一块：`text-attributed graph prompting`。

如果写入 [graph_prompt_summary.tex](D:/GPL/gpl-survey/tex/table/graph_prompt_summary.tex)，最合理的做法不是把它硬塞进纯图 prompt 一类，而是在 prompt component 中明确写 `graph-text mixed prompt`，并在备注或正文中说明它依赖 `LM + GNN joint pre-training`。从下游任务看，它针对的是 `few-shot node classification`。prompt tuning 是 `learnable`，answering 则更接近 `learnable`。

## 它可能替换谁

如果主表长度必须控制，而你又想让表格反映多模态或 TAG 方向，那么 P2TAG 很适合替换 `SAP` 这类较旧、且代表性相对一般的方法行。若主表仍只想覆盖纯结构图 prompt 方法，那更好的做法是把 P2TAG 放进正文或单独的 TAG 扩展表。

## 局限和阅读时要注意的地方

P2TAG 的优势非常依赖 TAG 设定，也就是节点本身有高质量文本属性。因此它不像 GPPT、GraphPrompt 那样天然面向所有普通图任务。第二，它的方法同时动用了 LM 和 GNN，训练与部署成本都高于纯图 prompt 方法。第三，它虽然很适合作为多模态或 TAG 提示学习的代表，但和经典 graph prompt taxonomy 并不完全同层，写 survey 时最好明确它属于扩展方向，而不是把它当成普通图 prompt 的简单变体。

总体上，P2TAG 的价值在于告诉读者：当 graph prompting 进入文本属性图以后，prompt 已经不再只是“在图上加 token”，而是可能演化成一个结构提示与文本提示协同工作的系统。

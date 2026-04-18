# GraphPrompter 方法详解

## 论文信息

论文标题是 *GraphPrompter: Multi-stage Adaptive Prompt Optimization for Graph In-Context Learning*。该工作发表于 `ICDE 2025`，DOI 为 `10.1109/ICDE65448.2025.00292`。论文提出的方法名为 `GraphPrompter`。

## 一句话定位

GraphPrompter 不是传统意义上那种“训练一个图 prompt 参数”的方法，它更像是为 `graph in-context learning` 单独设计的一套 prompt 优化框架，重点在于如何生成、筛选和动态补充 prompt 示例。

## 它要解决什么问题

Graph in-context learning 的基本设定是：不给模型做梯度更新，而是给它若干带标签的图示例，让它在这些 prompt examples 的条件下完成新查询的预测。此前 Prodigy、OFA 等方法已经证明这种路线可行，但 prompt 的质量高度依赖示例构造方式。若 prompt 子图本身带噪，或者为每个 query 随机挑几个示例，那么下游性能往往不稳定。

GraphPrompter 的问题意识很清楚。作者认为，graph in-context learning 不是只差一个更强编码器，而是 prompt pipeline 的三个环节都可以优化：生成的 prompt 子图是否够干净，针对某个 query 选出来的示例是否真合适，以及测试时能否利用目标域新出现的结构信息去动态补强 prompt 集。

## 方法总览

GraphPrompter 把整个 prompt 使用过程拆成三段，分别对应三个模块：`Prompt Generator`、`Prompt Selector` 和 `Prompt Augmenter`。它的主要贡献不在于提出一种全新的预训练任务，而在于系统地优化 `graph in-context learning` 里的 prompt 生命周期。

其中，Prompt Generator 负责生成质量更高的 prompt 子图；Prompt Selector 负责针对当前 query 挑出更合适的 prompt examples；Prompt Augmenter 则在测试阶段利用缓存和伪标签动态扩充 prompt 集，提升跨域或多类别场景下的泛化。

## 模块一：Prompt Generator

这个模块要解决的是 prompt 子图里噪声太多的问题。此前很多方法会从源图中随机游走或随机抽样得到 prompt 子图，但邻域里常常混入任务无关节点和边。GraphPrompter 的做法是引入 `reconstruction layer`，对采样得到的子图边权进行重建学习，突出更有信息量的边，压低不重要的连接。

直观理解，这一步是在说：不是所有被采到的邻居都值得作为 prompt 上下文，应该先把 prompt 图“洗干净”，再让模型拿它做 in-context prediction。这个生成阶段的优化是 GraphPrompter 很关键的一个卖点，因为它把 prompt 质量问题前移到了构造阶段，而不是把一切都留给后面的选择机制。

## 模块二：Prompt Selector

Prompt Selector 的目标是为每个 query 动态挑出更相关的 k 个 prompt，而不是随机选。论文的做法是结合两类信号。第一类是 `selection layer` 给出的重要性分数，这个分数是在预训练阶段学出来的，反映 prompt 对类别中心的重要程度。第二类是 `kNN similarity`，也就是候选 prompt 与当前 query 在嵌入空间中的相似度。

作者并没有只用其中一类信号，而是把两者结合起来做 top-k 选择。实验里也专门做了消融，结果显示单独用 kNN 或单独用 selection layer 都不如两者结合。这一点很值得写进 survey，因为它说明 GraphPrompter 的贡献不只是“加了检索”，而是把预训练得到的重要性偏好和测试时的 query 相关性合并了。

## 模块三：Prompt Augmenter

当测试图的类别很多、分布又和预训练图不同，仅靠固定候选 prompt 往往不够。为此，GraphPrompter 设计了 `Prompt Augmenter`。它在测试时维护一个缓存 `C`，把高置信度预测得到的测试样本及其伪标签存进去，并通过 `LFU` 策略动态替换缓存内容。

这样做的意义在于，模型不再只能使用训练期保留下来的 prompt examples，还能逐步吸收目标域信息，用在线生成的伪标注样本来补充 prompt 集。论文里把这一步看成一种非参数的 test-time adaptation。它没有改模型参数，但改变了 prompt 集本身，因此能增强多类别和分布偏移场景下的泛化。

## 训练与推理流程

GraphPrompter 的训练主要发生在预训练阶段。作者沿用了 Prodigy 风格的图 in-context learning 预训练任务，如 neighbor matching 和 multi-task 构造，同时在这个阶段把 reconstruction layer 和 selection layer 一并学出来。到了推理阶段，模型不再做梯度更新，而是按以下顺序执行：先用 Prompt Generator 得到候选 prompt 子图，再用 Prompt Selector 为每个 query 选出 top-k prompt，最后若缓存非空，则从 Prompt Augmenter 中补充若干伪标签样本，形成增强后的 prompt 集合，再完成预测。

这套流程的一个重要特点是：GraphPrompter 的改进主要发生在 prompt pipeline 上，而不是发生在传统 prompt tuning 的参数更新上。

## 相比已有方法的新意

GraphPrompter 的新意很集中。第一，它把 graph in-context learning 中长期被忽视的 prompt 质量问题单独抽出来研究。第二，它不是只在一个点上做改动，而是沿着“生成、选择、增强”三个阶段做系统优化。第三，它把 test-time cache augmentation 引入 graph ICL，使 prompt 集不再静态固定。

如果你的 survey 想覆盖 `graph in-context learning` 这条支线，GraphPrompter 是很有代表性的一篇，因为它展示了这一方向已经从“能不能做”转向“prompt pipeline 怎么优化”。

## 适合加入表格的原因

GraphPrompter 的权威性没有问题，它是 `ICDE 2025` 正式发表论文，而且方法贡献明确。问题不在于它够不够强，而在于它和现有 [graph_prompt_summary.tex](D:/GPL/gpl-survey/tex/table/graph_prompt_summary.tex) 的表头是否完全兼容。当前表更偏经典 prompt tuning，而 GraphPrompter 更偏 in-context prompting。

如果你愿意让主表覆盖 `graph in-context learning`，那它非常值得加入，最好单列成一个方法行，并在 prompt component 中写 `generator + selector + augmenter`。如果你希望主表继续只覆盖传统 pre-train / prompt / fine-tune 范式，那它也许更适合放在正文和扩展表，而不是硬塞进主表现有 taxonomy。

## 它可能替换谁

若要强行控制主表长度，同时又想覆盖 graph ICL，这篇论文最适合替换 `SAP` 或 `PGCL` 中较旧的一行。但更稳妥的做法其实是把它作为 `graph in-context learning` 的单独代表，而不是直接和经典 prompt tuning 方法逐行替换。

## 局限和阅读时要注意的地方

GraphPrompter 的局限首先来自定位。它非常适合 graph in-context learning，但和普通 learnable prompt token 方法不是一回事。第二，它引入 kNN 检索和缓存增强后，推理时间会有所增加，论文也承认推理成本会变成原来的两到三倍左右，虽然整体仍然可控。第三，Prompt Augmenter 依赖伪标签质量，虽然论文展示了鲁棒性，但如果测试域预测本身很不稳定，缓存带来的收益就会受限。

总的来说，GraphPrompter 很适合放在 survey 中作为 `graph in-context prompting` 的代表方法，但写表格时最好明确它和传统 prompt tuning 的边界。

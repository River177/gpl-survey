# DAGPrompT 方法详解

## 论文信息

论文标题是 *DAGPrompT: Pushing the Limits of Graph Prompting with a Distribution-aware Graph Prompt Tuning Approach*。该工作发表于 `WWW 2025`，DOI 为 `10.1145/3696410.3714917`。论文提出的方法名为 `DAGPrompT`。

## 一句话定位

DAGPrompT 试图回答一个此前图 prompt 研究里经常被回避的问题：如果图本身很复杂，尤其存在明显 heterophily，不同 hop 上的数据分布又并不一致，那么单纯冻结预训练编码器再加一个普通 prompt，为什么还应当有效？

## 它要解决什么问题

很多早期 graph prompting 方法在同配图上效果不错，但到了异配图、复杂图或分布偏移更强的场景，性能就会明显下降。DAGPrompT 把问题拆成两点。第一，预训练编码器与下游数据分布并不一致，如果编码器完全冻结，prompt 的作用空间会很受限。第二，不同节点依赖的信息 hop 不一样，而且 heterophily 在不同 hop 上的分布也不同，因此“一套 prompt 统一处理所有 hop”往往不够细。

这两个判断很关键。它意味着 DAGPrompT 不再把 prompting 看成一个纯输入层小修小补，而是认为要真正把 prompt 用到复杂图上，必须同时处理模型适配和 hop-level 差异。

## 方法总览

DAGPrompT 由两个核心模块组成。第一个模块是 `GLoRA`，即 `Graph Low-Rank Adaptation`，负责在保留预训练知识的前提下，对 GNN 编码器做低秩适配。第二个模块是 `Hop-specific Graph Prompting`，负责为不同 hop 的表示引入分层 prompt，并据此完成下游任务预测。

简单说，GLoRA 处理的是“编码器要不要完全冻住”的问题，Hop-specific Prompting 处理的是“同一个 prompt 能不能覆盖所有 hop”的问题。二者组合起来，形成了一个显式 `distribution-aware` 的 prompt tuning 框架。

## 模块一：GLoRA

### 为什么要有 GLoRA

作者认为，很多 prompt 方法默认预训练 GNN 完全冻结，这样在简单场景下也许够用，但在 heterophily 较强的图上，冻结编码器会使节点表示难以拉开，导致 prompt 再怎么调也只能在一个已经不够可分的表示空间里做修补。

所以 DAGPrompT 的选择不是 full fine-tuning，而是低秩适配。它用低秩矩阵去调整编码器中的投影参数和 message-passing 机制，让模型能适应新的下游分布，同时又不至于破坏预训练权重里已经存在的知识。

### GLoRA 具体调什么

从论文描述看，GLoRA 不是只对最后一层线性层做 LoRA，而是同时作用在两个层面。一个层面是 projection 参数，另一个层面是 message passing 过程本身。也就是说，它不只调整表示变换，还调整图中信息传播的方式。论文里还给出可视化，说明 GLoRA 会增强某些边的作用、削弱另一些边的作用，从而让消息传递更适配下游任务。

这点非常重要。它说明 DAGPrompT 虽然名字里还是 prompt tuning，但实际上已经把参数高效适配和 graph prompting 融合在一起了。

## 模块二：Hop-specific Graph Prompting

### 为什么要做 hop-specific

作者指出，在复杂图中，不同节点对局部与远距离信息的依赖程度不同。某些节点更依赖 1-hop 信息，某些则更依赖 2-hop 或 3-hop 信息。与此同时，异配程度也会随 hop 改变。因此，如果只使用最终层表示，或者把中间层简单拼接起来，但不给每个 hop 独立 prompt，模型就很难真正适应这些差异。

### 它怎么做

DAGPrompT 先把下游任务统一改写为 subgraph-level 任务，使其能与 link-prediction 风格的预训练目标对齐。随后，模型提取不同 GNN 层得到的 hop-wise 表示，把这些表示按层保留。接着，方法为每一层构造对应的 `class tokens` 或 `layer-specific class prompts`，并计算每个节点在各层表示与类别 prompt 之间的相似度。最终预测损失 `Lds` 会在所有层上共同定义。

换句话说，DAGPrompT 的 prompting 不是只在一处插入一个统一 token，而是为不同 hop 的表示空间都准备了自己的类别提示，并在这些层次上共同完成分类。

这一步使得它相比 GraphPrompt、GPF-Plus、All in One 这类方法更强调“分层分布差异”和“多 hop 对齐”。

## 两阶段训练流程

论文把方法写成两个阶段。第一阶段是 label-free pre-training，使用无标签的链接式预训练任务，让编码器学会基本的结构表示。第二阶段是 prompting and tuning，此时模型引入 GLoRA 参数、各层 prompt 参数和层系数，对下游任务进行适配。

在第二阶段里，编码器不再完全冻结，但也不是 full fine-tuning，而是通过 GLoRA 做受控调整；同时各层 class prompt 也一起学习。实验里作者还专门比较了 `DAGPrompT-Full` 和 `DAGPrompT-Freeze`，结果显示完全解冻和完全冻结都不如 DAGPrompT 本身，这正好支撑了它“中间路线更优”的主张。

## 相比已有方法的新意

DAGPrompT 有三点非常值得写进 survey。第一，它明确把 graph prompting 的失效原因和 `distribution shift + heterophily` 绑定起来，而不是简单说“复杂图更难”。第二，它把 `LoRA-style parameter-efficient tuning` 带进了 graph prompting 主线，让提示学习和模型适配不再严格分离。第三，它不是只做更复杂的 prompt 结构，而是把 hop-wise 差异真正编码进 prompting 过程。

如果你希望主方法表能体现“2025 年后 graph prompting 已经从 task reformulation 走向 distribution-aware adaptation”，DAGPrompT 基本是绕不开的一篇。

## 适合加入表格的原因

DAGPrompT 非常适合进主方法表。它是 `WWW 2025` 正式发表方法，代表性强，机制边界清楚，而且比很多仍停留在 arXiv 的方法成熟得多。更重要的是，它在你当前表格的 taxonomy 里补的是一条真正新的主线：`distribution-aware prompt tuning with PEFT adaptation`。

如果写入 [graph_prompt_summary.tex](D:/GPL/gpl-survey/tex/table/graph_prompt_summary.tex)，可以把它归到基于预训练的 prompt tuning 方法，并在 prompt component 中强调 `GLoRA + hop-specific class prompts`。它覆盖 node 和 graph classification，prompt tuning 显然是 `learnable`。如果表格允许一点扩展，最好在注释或正文里明确它同时包含 prompt 和 low-rank adaptation。

## 它可能替换谁

如果要替换旧行，DAGPrompT 最适合替换 `PGCL` 或 `SAP`。原因是它不仅正式发表，而且方法贡献更完整，也更能代表近两年 prompt 方法的主流升级方向。

## 局限和阅读时要注意的地方

DAGPrompT 的优点很明显，但代价也不小。它的方法复杂度高于传统 prompt 方法，因为同时引入了分层 prompt 和低秩适配。其次，它特别擅长处理复杂分布和 heterophily，因此如果图本身结构很简单、同配性很强，它的优势未必会像在论文里那样显著。最后，它的方法虽然仍可归到 prompt tuning，但已经明显跨到了 PEFT 和编码器适配的边界地带，写 survey 时最好不要把它和只改输入图的轻量 prompt 方法混成一类。

总体上，DAGPrompT 是一篇非常适合作为“graph prompting 进入复杂图和分布偏移时代”的代表论文。

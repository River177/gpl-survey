# RELIEF 方法详解

## 论文信息

论文标题是 *RELIEF: Reinforcement Learning Empowered Graph Feature Prompt Tuning*。该工作发表于 `KDD 2025`，DOI 为 `10.1145/3690624.3709252`。论文提出的方法名为 `RELIEF`。

## 一句话定位

RELIEF 关心的不是“给每个节点都加 prompt 会不会有效”，而是“到底应该给哪些节点加 prompt、加多大、按什么顺序加”。它把 feature prompt tuning 重新表述成一个强化学习驱动的决策问题。

## 它要解决什么问题

此前很多 feature-based graph prompt 方法会给所有节点都引入可学习 prompt，或者至少在设计上默认 prompt 应该大面积注入图中。这样做虽然简单，但有两个问题。第一，提示参数可能过多，容易偏离参数高效调优的初衷。第二，真正对下游任务有帮助的节点不一定很多，对所有节点一视同仁反而可能把噪声也放大。

RELIEF 的出发点是，强预训练模型未必需要大量 prompt，它可能只需要少量、恰当位置、恰当幅度的 conditioning signal 就够了。因此这篇论文把 prompt 设计目标从“给图加 prompt”换成了“只给必要节点加尽可能轻量的 prompt”。

## 方法总览

RELIEF 的核心思路是把图特征 prompt 的构造过程表述成一个序列决策问题。在每一步，智能体都需要同时决定两件事：选择哪个节点加 prompt，以及给这个节点加什么样的 prompt 向量。前者是离散决策，后者是连续决策，因此这是一个典型的 hybrid action space 问题。

整个方法由两个主要可训练模块组成。第一个是 `policy network`，负责做 prompt 决策。第二个是 `projection head`，负责把冻结的预训练 GNN 表示映射到当前下游任务。预训练 GNN 编码器本身保持冻结，只有策略网络和投影头参与更新。

## 强化学习建模

### 1. 状态

RELIEF 的状态来自“当前已经加过 prompt 的图”。具体做法是，把加入 prompt 后的图送进冻结的预训练 GNN，得到节点表示，再把这些表示作为策略网络的状态输入。因为不同图大小不同，作者还做了 padding，把状态统一到固定维度，方便批训练。

这样的状态设计有一个好处：策略网络不是在原始节点特征上盲选，而是在预训练模型已经抽取出来的表示空间里做决策，因此它能感知当前 prompt 已经造成了什么影响。

### 2. 动作

动作是一个二元组。第一部分是离散动作，表示选择哪个节点。第二部分是连续动作，表示要加到该节点上的特征 prompt 向量。换句话说，RELIEF 不只是学“prompt 长什么样”，还学“prompt 放在哪里”。

这一步是 RELIEF 和 GPF、GPF-Plus 这类方法最大的差异之一。后者往往默认 prompt 作用范围或作用方式已经确定，RELIEF 则把选择位置本身也纳入学习过程。

### 3. 奖励

奖励定义为加入当前 prompt 前后，下游损失的变化。若这一步 prompt 让损失下降，则奖励为正；若损失上升，则奖励为负。多个步骤的累计奖励就对应整个 prompt 序列带来的性能提升。

这个设计让策略网络直接围绕“哪些 prompt 真正有助于任务”来学习，而不是只在一个静态 prompt 参数空间里做优化。

## 策略网络与训练机制

RELIEF 使用适合 hybrid action space 的 `H-PPO`。策略网络包含两个 actor 和一个 critic。离散 actor 决定选哪个节点，连续 actor 生成 prompt 向量，critic 评估当前状态价值。三个网络共享一部分前层表示，以提升训练稳定性。

论文还引入了 `policy generalization` 机制来缓解 RL 在有限训练图上的过拟合。具体做法是维护多个子策略，在不同 bootstrap 采样环境中训练，再通过正则约束让它们和 joint policy 保持一定一致性。这个设计不是 RELIEF 的主卖点，但它对训练稳定性很关键。

在整体训练上，RELIEF 采用 `policy network` 和 `projection head` 交替更新的方式。策略网络先学会如何构造 prompt，投影头再在当前 prompt 分布下适配下游任务。两者协同推进，而不是把所有参数一次性端到端联训。

## 它如何定义“轻量 prompt”

RELIEF 不只报告准确率，还专门定义了两个度量来量化 prompt 对原图的影响。

第一个是 `Prompt Coverage Ratio (PCR)`，表示最终被 prompt 过的节点占比。这个指标回答的是“到底有多少节点真的需要被提示”。第二个是 `Average Prompt Magnitude (APM)`，用有效 prompt 的平均幅度来衡量注入信号有多强。作者想表达的核心结论是：好的 prompt 不只是效果好，还应该覆盖更少的节点、幅度尽量小。

这两个指标很有价值，因为它们让“参数高效”不再停留在口头描述，而是有了比较直接的行为解释。

## 相比已有方法的新意

RELIEF 最重要的新意，是把 graph feature prompt tuning 从一个静态参数学习问题，改成了一个带位置选择和幅度控制的序列决策问题。这个变化不只是换了优化器，而是把 prompt 设计空间重新定义了。

第二个新意，是它明确区分了“prompt 放在哪”和“prompt 长什么样”，并用 hybrid action RL 同时处理二者。第三个新意，是它给出了 PCR 和 APM 这类 prompt 影响指标，让方法不只比最终性能，也比 prompt 的稀疏性与扰动强度。

## 适合加入表格的原因

RELIEF 很适合进主方法表。首先它是 `KDD 2025` 正式发表论文，权威性没问题。其次它的机制边界非常清楚，属于典型 prompt tuning 方法，而不是泛泛的 graph adaptation。最后，它在当前 prompt 方法谱系里补上了一个此前相对缺失的方向：`reinforcement-learning-driven selective prompt tuning`。

如果要写入 [graph_prompt_summary.tex](D:/GPL/gpl-survey/tex/table/graph_prompt_summary.tex)，比较合适的映射是把它放在 `feature prompt tuning` 路线下，prompt component 可描述为 `node feature prompts with selective insertion`，prompt tuning 标为 `learnable`，下游任务可标 `graph / node classification`，answering function 可归到 `learnable projection head`。

## 它可能替换谁

如果要控制表格长度，RELIEF 很适合替换 `SGL-PT`。原因是 RELIEF 更成熟、正式发表、机制更强，而且能明显代表 2025 年 prompt 方法开始从“统一注入”走向“选择性注入”的趋势。

## 局限和阅读时要注意的地方

RELIEF 的主要代价是训练复杂度更高。它虽然在参数上仍然轻量，但引入 RL 后，优化流程明显比普通 prompt tuning 更重，也更依赖训练稳定性设计。其次，这个方法最自然的舞台是 few-shot 和预训练 GNN 适配，如果没有高质量预训练表示，策略网络能否稳定学出有意义的 prompt 选择就会打折扣。

对 survey 来说，RELIEF 的价值非常明确：它代表了一条新的 prompt 设计路线，即 prompt 不再默认作用于所有节点，而是被当成一种需要精确调度的资源。

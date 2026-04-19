# 新增 5 个方法在 `graph_prompt_summary.tex` 中三列写法的详细说明

本文档解释 [graph_prompt_summary.tex](C:/Users/River/.codex/worktrees/c92f/gpl-survey/tex/table/graph_prompt_summary.tex) 中新增 5 个方法在以下三列中的写法依据：

- `prompt components`
- `inserting pattern`
- `prompt tuning`

这里的目标不是把论文完整复述一遍，而是说明为什么表格里最后采用了当前这种“尽量符号化、尽量压缩、与旧表风格一致”的表示法。

为了避免误解，先说明这张表的写法原则：

1. 这一表不是方法综述正文，而是 taxonomy summary，因此每列都必须压缩到一个非常有限的表达单元。
2. `prompt components` 列优先回答“prompt 由什么构成”，因此优先保留对象名和关键符号。
3. `inserting pattern` 列优先回答“prompt 如何进入原图或原模型”，因此优先保留构造式、更新式或最核心的 forward 形式。
4. `prompt tuning` 列优先回答“prompt 如何被优化”，因此优先保留损失函数、更新目标、或者一个极短的训练机制词组。
5. 如果一篇论文本身跨越了 prompting、retrieval、PEFT、graph ICL、LM+GNN 联合建模等多个层面，表格必须只保留最能区分它的方法核心，而不能把整篇论文的全部模块都塞进来。

下面按方法分别说明。

## 1. GraphPrompter

当前表格写法：

- `prompt components`
  - `candidate prompts: \mathcal{G}^{S}=\{ G_p \}_{p=1}^{N}`
  - `task graph: G^T`
  - `cache: \mathcal{C}`
- `inserting pattern`
  - `\hat{\mathcal{S}}' \leftarrow \hat{\mathcal{S}} \cup \mathcal{C}`
  - `\textbf{H} \leftarrow \mathrm{GNN}^{T}(G^{T}(\hat{\mathcal{S}}',Q))`
- `prompt tuning`
  - `L = L_{NM} + L_{MT}`

### 为什么 `prompt components` 这样写

GraphPrompter 不是经典的“给图加一个 learnable token”型方法。它的 prompt 本质上是一个由候选 prompt 子图构成的集合，然后再和 task graph、online cache 共同形成图 in-context learning 的输入体系。

因此这里没有沿用 `prompt token: ...` 的写法，而是写成：

- `\mathcal{G}^{S}=\{ G_p \}_{p=1}^{N}`：表示候选 prompt 子图集合
- `G^T`：表示 task graph
- `\mathcal{C}`：表示 test-time augmentation 使用的 cache

这样写的原因是，这三者在论文里都直接参与 prompt pipeline，本身就是 prompt 机制的一部分，而不是附属实现细节。

没有进一步把 selection layer 的参数或 importance score 也写进这一列，是因为那已经更接近训练机制，不再是 prompt 组件本身。

### 为什么 `inserting pattern` 这样写

GraphPrompter 的“插入”不是把 prompt token 加到节点特征上，也不是构造跨边把 prompt graph 挂到原图上。它的核心是：

1. 先从候选 prompt 集中选出 `\hat{\mathcal{S}}`
2. 再在推理时用 cache 得到扩增后的 `\hat{\mathcal{S}}'`
3. 最后把 `\hat{\mathcal{S}}'` 和 query 集合 `Q` 一起送入 task graph `G^T`

所以这里选择了两步最能概括其插入方式的表达：

- `\hat{\mathcal{S}}' \leftarrow \hat{\mathcal{S}} \cup \mathcal{C}`
- `\textbf{H} \leftarrow \mathrm{GNN}^{T}(G^{T}(\hat{\mathcal{S}}',Q))`

第一行强调它的 prompt 在 test-time 不是静态的，会被 cache 扩增。  
第二行强调 prompt 最终不是直接改原图节点，而是进入 task graph 做 graph ICL 推理。

这比“reconstruct sampled prompt graphs / retrieve top-k prompts / augment with cache”更接近原表已有行的公式风格。

### 为什么 `prompt tuning` 这样写

这篇论文的训练实际上包含两类 pretraining task：

- Neighbor Matching
- Multi-Task

最终总目标就是：

- `L = L_{NM} + L_{MT}`

表里最终保留这个式子，而不再写 `Neighbor Matching + Multi-Task`，是为了和旧表中 `Cross Entropy`、`Meta-Learning`、`\min ...` 这种风格统一。

这里没有把 selection layer、kNN retrieval、vote score 写进 `prompt tuning`，因为这些更适合归在 `inserting pattern` 或方法细节里，不属于最核心的优化目标。

## 2. RELIEF

当前表格写法：

- `prompt components`
  - `feature prompt matrix: \textbf{P}_t \in \mathbb{R}^{n \times d}`
- `inserting pattern`
  - `\textbf{X}^{*} \leftarrow \textbf{X} + \textbf{P}_t`
  - `p_t^{a,z} = (a_t,z_t)`
- `prompt tuning`
  - `r_t \leftarrow \mathcal{L}_{t-1} - \mathcal{L}_{t}`
  - `H-PPO`

### 为什么 `prompt components` 这样写

RELIEF 的 prompt 核心不是单个共享 token，而是一个 node-specific feature prompt matrix。论文里每一步选择某个节点，再为该节点生成一个 prompt 向量，累积形成提示矩阵。

因此这里最准确的压缩方式不是写成 `prompt token`，而是：

- `\textbf{P}_t \in \mathbb{R}^{n \times d}`

这准确表达了它的 prompt 粒度是 node-wise，而不是 graph-wise 单向量或少量 basis tokens。

### 为什么 `inserting pattern` 这样写

RELIEF 的插入方式非常明确，就是 feature-level prompting：

- `\textbf{X}^{*} \leftarrow \textbf{X} + \textbf{P}_t`

这是最核心的 forward 写法，和 GPF / GPF-Plus 那条线是可比的。

但 RELIEF 比 GPF 多了一层“如何决定 prompt 加到哪个节点上”。因此又补了一行：

- `p_t^{a,z} = (a_t,z_t)`

这里的意思是每一步的 hybrid action 同时决定：

- 离散动作 `a_t`：选哪个节点
- 连续动作 `z_t`：给这个节点加什么 prompt 向量

如果只写第一行，会把 RELIEF 错看成普通 feature prompting；第二行正是它和 GPF/GPF-Plus 最大的机制差异。

### 为什么 `prompt tuning` 这样写

RELIEF 的优化不是普通 supervised tuning，而是强化学习。最核心的奖励信号是相邻两步损失下降：

- `r_t \leftarrow \mathcal{L}_{t-1} - \mathcal{L}_{t}`

然后它用的优化器/策略框架是：

- `H-PPO`

表格里保留这两项，是因为它们分别对应：

- 优化目标的即时定义
- 优化算法的类型

之前版本写成 `H-PPO + projection head` 太像正文说明，不像表格摘要；现在保留 `H-PPO` 已经足够，因为 projection head 在 RELIEF 里是配套模块，不是 prompt tuning 的辨识核心。

## 3. DAGPrompT

当前表格写法：

- `prompt components`
  - `GLoRA: \Theta_{\mathrm{glora}}`
  - `class prompts: \textbf{P}^{(l)}`
  - `hop coeff.: \gamma^{(l)}`
- `inserting pattern`
  - `\textbf{H}^{(l)} \leftarrow (\textbf{A}+P_AQ_A^{\top}) \textbf{H}^{(l-1)} (W_0+PQ^{\top})`
  - `S^{(l)} \leftarrow \mathrm{Sim}(\textbf{H}^{(l)}, \textbf{P}^{(l)})`
- `prompt tuning`
  - `\bar{S} \leftarrow \sum_{l=0}^{L} \gamma^{(l)} S^{(l)}`
  - `Similarity Loss`

### 为什么 `prompt components` 这样写

DAGPrompT 不是只靠 graph prompt token 工作，它是 prompting 和 low-rank adaptation 混合的方法。论文里最关键的三个对象就是：

- `\Theta_{\mathrm{glora}}`：GLoRA 的低秩适配参数
- `\textbf{P}^{(l)}`：每一层的 class prompts
- `\gamma^{(l)}`：跨 hop / 跨层的权重系数

如果只写 `GLoRA + hop-specific prompts`，信息量太低。  
如果把所有低秩矩阵都展开到这一列，又会比原表其他方法密太多。  
所以最后选的是“对象名 + 一个关键符号”的折中写法。

### 为什么 `inserting pattern` 这样写

DAGPrompT 的插入有两个层面：

1. 用 GLoRA 改 message passing 和 projection
2. 用 layer-wise class prompts 在各层 embedding 上做相似度提示

因此 `inserting pattern` 列保留了两步：

- `\textbf{H}^{(l)} \leftarrow (\textbf{A}+P_AQ_A^{\top}) \textbf{H}^{(l-1)} (W_0+PQ^{\top})`
- `S^{(l)} \leftarrow \mathrm{Sim}(\textbf{H}^{(l)}, \textbf{P}^{(l)})`

第一行体现 prompt/adapter 如何进入 GNN 层内。  
第二行体现 hop-specific prompting 如何发生在各层表示与 class prompts 之间。

相比“low-rank adaptation of message passing and projection with hop-specific prompts”这种文字摘要，这样更接近旧表的写法，也更便于和前面其他方法直接对比。

### 为什么 `prompt tuning` 这样写

DAGPrompT 的最终预测不是单层相似度，而是把各层得分加权聚合：

- `\bar{S} \leftarrow \sum_{l=0}^{L} \gamma^{(l)} S^{(l)}`

这是它 prompt tuning/answering 里最有辨识度的一步，因此保留成主公式。

另外加了一个非常短的词组：

- `Similarity Loss`

原因是仅写聚合式还不足以说明它的训练目标风格；但把整套损失展开会明显超出原表风格。所以最终用“聚合式 + 极短训练词组”的方式处理。

## 4. IGAP

当前表格写法：

- `prompt components`
  - `signal prompts: \mathcal{P}_s=[\textbf{p}_{s1},...,\textbf{p}_{sL}]`
  - `spectral aligner`
  - `label prompt: \textbf{P}_{l}=[\textbf{p}_1,...,\textbf{p}_d]`
- `inserting pattern`
  - `\tilde{\textbf{x}}_{i} \leftarrow \textbf{x}_{i} + \sum_{s} \alpha_{is} \textbf{p}_{s}`
  - `\textbf{U}^{pt}_{K} \leftarrow \textbf{P}\textbf{U}^{ft}_{K}`
- `prompt tuning`
  - `\mathcal{L}_{\mathrm{InfoNCE}}^{cls}`

### 为什么 `prompt components` 这样写

IGAP 的贡献不是单一 prompt，而是三个互相配合的 prompt/align 模块：

- graph signal prompt
- spectral space alignment prompt
- label prompt

因此这里必须把三者都列出来，不然会错误地把 IGAP 简化成 feature prompt 或 label prompt 方法。

其中：

- `\mathcal{P}_s=[\textbf{p}_{s1},...,\textbf{p}_{sL}]` 对应 graph signal prompts
- `spectral aligner` 用文字保留，是因为这一项在论文里更像一个低维谱空间对齐模块，而不是一个简单 token 集
- `\textbf{P}_{l}=[\textbf{p}_1,...,\textbf{p}_d]` 对应 trainable label representations

### 为什么 `inserting pattern` 这样写

IGAP 的“插入”有两个真正关键的操作：

1. 在输入信号上加 graph signal compensation
2. 在频谱子空间上做低频对齐

所以这里保留了两行：

- `\tilde{\textbf{x}}_{i} \leftarrow \textbf{x}_{i} + \sum_{s} \alpha_{is} \textbf{p}_{s}`
- `\textbf{U}^{pt}_{K} \leftarrow \textbf{P}\textbf{U}^{ft}_{K}`

第一行对应 graph signal gap 的补偿。  
第二行对应 spectral space alignment prompt 的核心思路。

如果只写“align graph signals and K-smallest spectral components”，虽然意思对，但会和原表旧行的公式化风格不协调。

### 为什么 `prompt tuning` 这样写

IGAP 在分类任务上最终使用的是 classification InfoNCE：

- `\mathcal{L}_{\mathrm{InfoNCE}}^{cls}`

这已经足够代表它如何把下游分类任务重写成与 pre-training 更一致的对比式目标。  
这里没有再加 “trainable label representations” 这类解释，是因为那已经在 `prompt components` 里出现过了，放到这一列会显得重复。

## 5. P2TAG

当前表格写法：

- `prompt components`
  - `prompt graph: \mathcal{G}_{p}`
  - `text prompt: \textbf{w}_{t}`
  - `label text embeddings`
- `inserting pattern`
  - `A_{\mathcal{G}_{ego},\mathcal{G}_{p}}(i,j) \leftarrow \mathds{1}[\mathrm{Sim}(\textbf{x}_{i},\textbf{t}_{j}) > \delta]`
  - `\tilde{\textbf{z}}_{v} \leftarrow \mathrm{MLP}(\mathrm{READOUT}(f_{\mathrm{GNN}}(G_{v};\mathcal{G}_{p})), \textbf{w}_{t})`
- `prompt tuning`
  - `Mixed Prompt Learning`

### 为什么 `prompt components` 这样写

P2TAG 的核心不是单独的 graph prompt，也不是单独的 text prompt，而是 graph-text mixed prompt。

因此这列必须同时保留三件事：

- `\mathcal{G}_{p}`：prompt graph
- `\textbf{w}_{t}`：text prompt
- `label text embeddings`：用于初始化 prompt graph 的标签文本嵌入

如果只写前两个，会丢掉这篇论文最特别的一点：它不是随便造一个 prompt graph，而是用 label text semantics 去初始化它。

### 为什么 `inserting pattern` 这样写

P2TAG 的插入分两步：

1. 把 prompt graph 接到 ego graph 上
2. 把 GNN readout 和 text prompt 一起送进最终 task head

所以这里保留两条最关键的表达：

- `A_{\mathcal{G}_{ego},\mathcal{G}_{p}}(i,j) \leftarrow \mathds{1}[\mathrm{Sim}(\textbf{x}_{i},\textbf{t}_{j}) > \delta]`
- `\tilde{\textbf{z}}_{v} \leftarrow \mathrm{MLP}(\mathrm{READOUT}(f_{\mathrm{GNN}}(G_{v};\mathcal{G}_{p})), \textbf{w}_{t})`

第一行强调 prompt graph 如何连接到原始 ego graph。  
第二行强调最终 forward 真正是 graph prompt 和 text prompt 的联合使用。

如果只写“connect prompt graph to ego graph and concatenate trainable text prompt”，从语义上没错，但明显比原表里其他方法更像自然语言说明，而不是 summary table。

### 为什么 `prompt tuning` 这样写

P2TAG 的 prompt learning 在论文中被明确概括为 mixed prompt learning。  
严格来说，它也可以写成初始化式，例如：

- `\textbf{w}_{t}^{0} \leftarrow f_{\mathrm{LM}}(s_{v})`

但这更像 text prompt initialization，不足以概括整个 tuning 过程。  
而把完整 few-shot objective 展开又会比原表其他行更冗长。

所以这里最后保留成一个短词组：

- `Mixed Prompt Learning`

这是一个有意识的取舍：  
P2TAG 的训练目标比 GraphPrompter、RELIEF、IGAP 那几篇更难压成单个简洁公式，而 `Mixed Prompt Learning` 正好是论文自己的方法概括，也和这一行的 graph-text mixed prompt 主题一致。

## 为什么 5 个方法没有全部写成同一种严格形式

表格追求的是“风格统一”，不是“机械同构”。这 5 个方法分别属于不同类型：

- GraphPrompter：graph in-context learning / retrieval-enhanced prompting
- RELIEF：RL-based feature prompt tuning
- DAGPrompT：prompting + PEFT / LoRA-style adaptation
- IGAP：spectral alignment prompt
- P2TAG：TAG 上的 graph-text mixed prompt

因此三列里出现的最佳压缩对象本来就不同：

- 有的最适合用损失函数概括，例如 IGAP
- 有的最适合用状态更新或奖励式概括，例如 RELIEF
- 有的最适合用总目标式概括，例如 GraphPrompter
- 有的最适合用聚合式概括，例如 DAGPrompT
- 有的更适合用一个方法词组概括，例如 P2TAG

换句话说，统一的是“表达层级”，不是“符号模板”。

## 如果后续还要继续收紧，我建议怎么做

如果你想把表格再往“更像老表”的方向推进一层，我建议按下面的顺序继续压缩：

1. `GraphPrompter`  
   可以把 `prompt components` 再压成  
   `$\mathcal{G}^{S}$ / $G^T$ / $\mathcal{C}$`

2. `RELIEF`  
   可以把 `H-PPO` 单独保留，去掉 `r_t`，但这会损失它最关键的 reward 定义

3. `DAGPrompT`  
   可以把 `Similarity Loss` 去掉，只保留  
   `$\bar{S} \leftarrow \sum_{l=0}^{L} \gamma^{(l)} S^{(l)}$`

4. `IGAP`  
   当前已经比较像旧表，可以基本不动

5. `P2TAG`  
   若一定要再公式化，可以改成一个初始化式加一个 forward 式，但可读性会下降

## 结论

当前表里的这 5 行已经尽量遵循了原表规则：

- `prompt components` 用符号或最少量对象名
- `inserting pattern` 用一到两个核心构造/forward 公式
- `prompt tuning` 用损失函数、更新式，或者极短的方法词组

它们之所以看起来不像旧方法那样完全同构，不是因为写法不统一，而是因为这 5 篇论文本身的方法重心已经明显比 2022-2023 那批 graph prompt 论文更分化了。表格当前的写法，本质上是在“风格统一”和“方法不失真”之间取一个平衡。

# Section 5 改稿建议（基于 `tex/5.tex` 与候选文献池）

## 1. 总体判断

`tex/5.tex` 的主体判断仍然成立：Section 5 试图回答 graph prompt 的四个核心问题，即 prompt 怎么设计、任务怎么对齐、prompt 怎么学习、以及各类方法之间的联系与优缺点。

但从 2024-2026 的候选文献来看，这一章已经明显落后于当前研究版图，主要问题有 5 个：

- 文献时间截断在 2023 年，缺少对 2024-2026 年方法演进的覆盖。
- 现有分类仍以 `prompt as tokens` / `prompt as graphs` 为主，已经不足以容纳新工作中的边提示、拓扑提示、消息传递提示、实例感知提示、通用提示、可编辑提示等分支。
- `Aligning Tasks by Answering Function` 的组织方式偏早期，许多新方法的重点已不再是“手工 answering function”，而是“通过结构/分布/时序/域迁移机制来完成对齐”。
- `Prompt Tuning` 小节对 prompt 学习方式的总结过于简单，缺少强化学习、稀疏选择、实例自适应、鲁棒优化、联邦/持续场景下的 prompt 学习。
- 后半部分的 multi-modal / multi-domain 讨论较泛，和当前候选池中的真实增量方向并不完全匹配。现在更需要强调的是 text-attributed graph、时序/动态图、持续学习、跨域迁移、联邦异质、鲁棒性等更具体的场景。

结论很明确：这不是“补几篇引用”就能解决的问题，而是需要对 Section 5 的组织结构做中等幅度重写。

---

## 2. 按 `tex/5.tex` 的修改点逐段说明

### 2.1 开头总述需要改写

对应位置：`tex/5.tex` 第 1-10 行。

当前问题：

- 第 2 行写的是 “we summarize the most representative works published recently”，但正文列举的“recent”基本都停留在 2022-2023。
- 开头四问仍可保留，但需要加入一句：近两年 graph prompt 已从“节点特征级 prompt”扩展到“边/拓扑/消息/实例/跨域/动态图/联邦/持续学习”等更丰富设定。
- 当前图 `prompt.pdf` 只突出 `tokens / structures / inserting patterns`，已经不够覆盖新方法。

建议修改：

- 保留四问框架，但在引言末尾补充“近两年的新进展主要体现为 prompt 注入空间扩展、适配场景扩展、以及理论/benchmark 开始成熟”。
- 在这一段直接引入 3 篇综述性或总览性文献，作为“新版 Section 5 的入口”：
  - ProG: A Graph Prompt Learning Benchmark
  - Does Graph Prompt Work? A Data Operation Perspective with Theoretical Analysis
  - Graph Prompting for Graph Learning Models: Recent Advances and Future Directions
- 如果要保留图示，建议把 Figure 的含义从三元组扩展为两层 taxonomy：
  - 第一层：prompt 注入位置
  - 第二层：适配目标场景

---

### 2.2 `Prompt Token, Structure, and Inserting Pattern` 需要重组，而不是只补论文

对应位置：`tex/5.tex` 第 14-26 行。

当前问题：

- 现有写法默认 prompt 主要是“token”或“graph”，这在 2023 年合理，但对 2024-2026 文献已经不够。
- 新文献显示 prompt 的差异不只体现在“长什么样”，更体现在“插在哪里”。
- 当前小节对特殊图类型覆盖很弱，没有 signed graph、temporal graph、spatio-temporal graph、heterogeneous graph、dynamic event graph 等。

建议把这一小节改成 4 个分支，而不是 2 个分支：

1. **Feature / Token-level Prompt**
   说明从 GPF/GPF-Plus 延伸到选择性、稀疏化、实例感知。
   推荐补入：
   - A Unified Graph Selective Prompt Learning for Graph Neural Networks
   - Reliable and Compact Graph Fine-tuning via GraphSparse Prompting
   - Instance-Aware Graph Prompt Learning
   - When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph Prompt Learning

2. **Edge / Topology-level Prompt**
   这是当前正文最明显缺失的分支。
   推荐补入：
   - Edge Prompt Tuning for Graph Neural Networks
   - GraphTOP: Graph Topology-Oriented Prompting for Graph Neural Networks
   - DAGPrompT: Distribution-aware Graph Prompt Tuning
   这部分可以明确说明：prompt 已不只是“改节点特征”，还可以“改边”或“改局部拓扑结构”。

3. **Hidden-state / Message-passing-level Prompt**
   当前正文只在 GraphPrompt 上轻触 hidden-layer prompt，但没有形成独立脉络。
   推荐补入：
   - MAGPrompt: Message-Adaptive Graph Prompt Tuning for Graph Neural Networks
   - GraphPrompt（保留，作为早期 hidden/readout 代表）
   这一支应强调“prompt 直接进入 message aggregation 或 representation update”。

4. **Prompt as Graph / Structured Prompt**
   保留 All in One、PRODIGY、SAP，但需要补上“结构化 prompt 的新走向”。
   推荐补入：
   - Graph Your Own Prompt
   - GraphPrompter: Multi-stage Adaptive Prompt Optimization for Graph In-Context Learning
   其中 `Graph Your Own Prompt` 可作为“self-prompt / relation graph regularization”的扩展例子，不一定完全等同于传统 prompt graph，但非常适合放在结构化 prompt 讨论末尾。

特殊图类型建议嵌入到上述 4 个分支里，而不是单独零散提一下：

- Heterogeneous graph：CLEAR
- Signed graph：SGPT
- Temporal interaction graph：TIGPrompt
- Spatio-temporal transfer：STGP
- Dynamic event graph：EVP

这一段的核心改法不是“多加 5 篇”，而是把分类轴从“形态”改成“注入空间 + 图类型”。

---

### 2.3 `Aligning Tasks by Answering Function` 这个标题和内容都该改

对应位置：`tex/5.tex` 第 29-44 行。

当前问题：

- 当前小节把“任务对齐”主要理解为 learnable answering function 和 hand-crafted answering function。
- 这更像早期 prompt paper 的讨论方式，但新方法已经显示：任务对齐常常通过 prompt 结构、分布对齐、领域适配、时间建模、事件建模来实现，而不一定通过一个显式 answering function。
- 如果继续保留现在的组织方式，会让 2024-2026 的新工作很难自然插入。

建议把标题改为：

- `Aligning Downstream Tasks with Pre-training Objectives`
  或
- `Task Alignment Mechanisms in Graph Prompting`

建议重写为 4 个小点：

1. **Task-template alignment**
   保留 All in One、GPPT、GraphPrompt、PRODIGY。
   再补：
   - SGPT：把 signed downstream task 统一成 link prediction 模板
   - CLEAR：把异构图下游任务重构为异构图重建

2. **Distribution / domain alignment**
   这是当前正文完全不够的部分。
   推荐补入：
   - Inductive Graph Alignment Prompt
   - DAGPrompT
   - One Prompt Fits All
   - GP2F
   这几篇能把“为什么 prompt 有助于跨分布/跨域迁移”讲清楚。

3. **Temporal / dynamic alignment**
   推荐补入：
   - Prompt Learning on Temporal Interaction Graphs
   - Prompt-Based Spatio-Temporal Graph Transfer Learning
   - Event-Aware Prompt Learning for Dynamic Graphs
   当前第 5 章几乎没有系统覆盖“时间维”的对齐逻辑，这是明显缺口。

4. **In-context / continual alignment**
   推荐补入：
   - GraphPrompter
   - Prompt-Driven Continual Graph Learning
   - GPT4Rec
   这部分可以说明：一些新工作并不通过传统 supervised task head 对齐，而是通过 prompt selection、prompt memory、view-specific prompt 等机制完成适配。

如果篇幅有限，可以直接删除现有 “learnable answering function / hand-crafted answering function” 的二分法，把它们压缩成一个历史过渡段，只保留 1 段即可。

---

### 2.4 `Prompt Tuning` 小节需要扩充“怎么学 prompt”的方法谱系

对应位置：`tex/5.tex` 第 48-61 行。

当前问题：

- 目前只有 meta-learning、task-specific tuning、pretext-aligned tuning 三类，明显不够。
- 近两年 prompt tuning 的创新主要发生在“选择谁、怎么生成、怎么约束、怎么在复杂场景里学”，而不是只停留在损失函数层面。

建议改成以下 5 类：

1. **Initialization / general prompt learning**
   保留 All in One 的 meta-learning 作为早期代表。

2. **Selective or sparse prompt optimization**
   推荐补入：
   - A Unified Graph Selective Prompt Learning for Graph Neural Networks
   - GraphSparse Prompting
   - SpikingGPF
   这类方法回答的是“是不是所有节点/特征都要 prompt”。

3. **Instance-adaptive or generated prompt**
   推荐补入：
   - Instance-Aware Graph Prompt Learning
   - Prompt-Driven Continual Graph Learning
   - GraphPrompter
   重点说明 prompt 可以由实例、任务阶段、或检索到的 context 动态生成。

4. **RL-based prompt optimization**
   当前正文完全没有这一支。
   推荐补入：
   - RELIEF
   - LEAP
   这两篇非常适合用来说明：prompt 优化已经从普通梯度更新扩展到组合/编辑决策。

5. **Robust or constrained prompt tuning**
   推荐补入：
   - Robust Graph Fine-Tuning with Adversarial Graph Prompting
   - DAGPrompT
   - MAGPrompt
   可以从鲁棒性、分布偏移、消息耦合三个角度说明 prompt learning 不再只是“轻量参数更新”，而是开始承担可靠适配职责。

这一小节建议补一个简短总结句：

- 早期工作关注“prompt 能不能学出来”，新工作更关注“prompt 学得是否高效、可解释、可迁移、可鲁棒”。

---

### 2.5 `Further Discussion` 需要从“方法对比”升级为“维度化讨论”

对应位置：`tex/5.tex` 第 65-80 行。

当前问题：

- 目前讨论部分主要围绕 GPF、HetGPT、GPPT、PRODIGY、ULTRA-DP、VNT 等早期方法做点对点比较。
- 缺少 benchmark 和 theory 的支撑，因此讨论仍偏经验性。
- 也没有覆盖近两年最关键的维度：泛化性、跨域性、动态性、鲁棒性、参数效率。

建议重写为 4 个讨论维度：

1. **Expressiveness vs. efficiency**
   可对比：
   - GPF / GPF-Plus
   - GSPF / GraphSparse / SpikingGPF
   - EdgePrompt / GraphTOP / MAGPrompt

2. **Universal prompt vs. selective prompt**
   可对比：
   - One Prompt Fits All
   - RELIEF
   - LEAP
   这里非常适合讨论“通用性”和“选择性”之间的张力。

3. **In-domain adaptation vs. cross-domain/generalization**
   可对比：
   - IGAP
   - DAGPrompT
   - GP2F
   - FedGPL

4. **Static setting vs. dynamic/continual setting**
   可对比：
   - TIGPrompt
   - STGP
   - GPT4Rec
   - PROMPTCGL
   - EVP

这部分建议显式引入两类支撑文献：

- **Benchmark 支撑**：ProG
  用来说明目前已有统一评测框架，可以避免讨论停留在各说各话。
- **Theory 支撑**：Does Graph Prompt Work?
  用来解释 prompt 为什么在“数据操作”意义上有效，以及其误差边界。

如果只想小改而不重写全文，至少应在这一小节新增一段“2024 之后的趋势总结”，否则第 5 章会显得停留在 graph prompt 的早期阶段。

---

### 2.6 `Graph Prompting in Multi-Modal and Multi-Domain Areas` 建议改标题和范围

对应位置：`tex/5.tex` 第 84-122 行。

当前问题：

- 现在这一节的前半是宽泛的 multi-modal/LLM 讨论，后半是 domain adaptation。
- 但候选池中的新增核心文献并不主要集中在“泛化的多模态”，而是集中在更具体的 graph setting：TAG、时序图、持续学习、跨域、联邦、动态图。
- 如果按现在的标题和内容硬补新文献，会显得拼贴。

建议改为更贴近新文献的标题，例如：

- `Graph Prompting in Complex Graph Settings`
  或
- `Graph Prompting Beyond Static Homogeneous Graphs`

然后拆成 4 个更贴近候选池的部分：

1. **Text-attributed graphs**
   推荐把现有 `Prompt in Text-Attributed Graphs` 重写，并加入：
   - Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs
   这篇比当前泛泛而谈的 LLM for graph 更贴合“graph prompt”主线。

2. **Temporal, dynamic, and streaming graphs**
   推荐新增：
   - Prompt Learning on Temporal Interaction Graphs
   - Prompt-Based Spatio-Temporal Graph Transfer Learning
   - GPT4Rec
   - Event-Aware Prompt Learning for Dynamic Graphs

3. **Continual, federated, and cross-domain settings**
   推荐新增：
   - Prompt-Driven Continual Graph Learning
   - Against Multifaceted Graph Heterogeneity via Asymmetric Federated Prompt Learning
   - GP2F
   - One Prompt Fits All

4. **Robustness and reliability**
   推荐新增：
   - Robust Graph Fine-Tuning with Adversarial Graph Prompting
   - GraphSparse Prompting
   - DAGPrompT

如果你想保留 multi-modal 小节，也建议降权处理，不要让它占据比动态图/跨域/持续学习更大的篇幅，因为从当前 graph prompting 的发展看，后者更像主线增量。

---

## 3. 最值得补入正文主线的文献

如果正文篇幅有限，不建议把 29 篇全都塞进去。下面这批是最值得进入主线叙述的：

- **ProG**
  作用：给讨论和结论部分提供 benchmark 支撑。

- **Does Graph Prompt Work?**
  作用：给“为什么有效”提供理论基础。

- **Graph Prompting for Graph Learning Models: Recent Advances and Future Directions**
  作用：作为新版 related discussion 的总览参照。

- **Edge Prompt Tuning for Graph Neural Networks**
  作用：补足“边提示”这个当前正文缺失的设计分支。

- **GraphTOP**
  作用：补足“拓扑提示”分支。

- **MAGPrompt**
  作用：把 prompt 从输入层推进到消息传递层。

- **Instance-Aware Graph Prompt Learning**
  作用：补“固定 prompt”到“实例自适应 prompt”的演进。

- **RELIEF / LEAP**
  作用：补 RL-based tuning。

- **Inductive Graph Alignment Prompt / DAGPrompT / GP2F / One Prompt Fits All**
  作用：系统补全跨域、分布迁移、归纳泛化的讨论。

- **Prompt Learning on Temporal Interaction Graphs / Prompt-Based Spatio-Temporal Graph Transfer Learning / Event-Aware Prompt Learning for Dynamic Graphs**
  作用：补“时间与动态”这一大缺口。

- **Prompt-Driven Continual Graph Learning / GPT4Rec / FedGPL**
  作用：补持续学习、流式推荐、联邦异质等更真实的部署场景。

- **Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs**
  作用：替换目前 multi-modal 小节中过于泛化、与 graph prompt 主线联系不够紧的描述。

---

## 4. 建议新增或改造的表格/总结

当前第 5 章如果只靠文字叙述，会很难容纳 2024-2026 的新增方向。建议至少新增一个表或改造现有 summary table。

建议 summary table 增加以下列：

- Prompt 注入位置：feature / edge / topology / message / readout / prompt graph
- 适配场景：static / hetero / signed / temporal / dynamic / continual / federated / cross-domain / TAG
- Prompt 学习方式：gradient / sparse selection / RL / generator / adversarial
- 是否需要 task head：yes / no
- 是否有理论或 benchmark 支撑

这样可以把第 5 章从“列举方法”升级成“系统分类”。

---

## 5. 不建议直接照搬进正文主论述的文献

- `Towards Graph Prompt Learning: A Survey and Beyond`
  这篇目前是作者暂时撤稿/修订中，可以作为内部参考，但不建议在正文中把它作为强支撑引用。

- `Graph Your Own Prompt`
  这篇很有启发性，但它更像“自提示/结构一致性正则”的扩展定义。适合放在 discussion 或 prompt-as-structure 的边界讨论中，不建议当作主线代表作之一。

- 2026 年仅 arXiv 的若干工作
  如 MAGPrompt、GP2F、AGP、SpikingGPF 等，可用于“最新趋势”或“未来方向”，但如果正文强调已成熟共识，最好以 2024-2025 已发表/已接收论文为主体。

---

## 6. 一个可执行的改稿方案

如果你准备真正动 `tex/5.tex`，建议按以下顺序改：

1. 先改第 1 段引言和总图，把分类口径换新。
2. 重写 `Prompt Token, Structure, and Inserting Pattern`，把“两分法”改成“按注入空间分类”。
3. 重写 `Aligning Tasks by Answering Function`，把重心从 answering function 改成 task alignment mechanism。
4. 扩写 `Prompt Tuning`，加入 selective / RL / robust / generated prompt。
5. 重写 `Further Discussion`，引入 benchmark 和 theory。
6. 把 `Multi-Modal and Multi-Domain Areas` 改成更贴合候选池的复杂图场景章节。

按这个顺序改，工作量是可控的，而且每一步都有明确落点。

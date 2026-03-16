# `tex/` 全局修改建议

> 范围说明：本文件针对 `tex/` 目录下除第 5 章之外的其他主体内容，给出全书级别的修改建议。  
> 第 5 章的细化改稿意见请配合阅读：[Section5-修改建议.md](/mnt/d/Graph/gpl-survey/docs/papers/Section5-修改建议.md)。

## 1. 总体判断

当前稿件的主线仍然清晰：它试图把 graph prompt 放在 “pre-training, prompting, predicting” 的大框架下理解，并从 AGI 的跨模态、跨域、跨任务视角建立统一叙述。

但如果现在要把这篇 2023 口径的 survey 更新到 2025-2026 水平，仅修改 `5.tex` 远远不够。原因很简单：

- 第 1 章引言仍在用 2023 年的“新兴方向”口吻介绍 graph prompt。
- 第 2 章 taxonomy、literature overview、existing work comparison 都停留在早期版图。
- 第 3 章和第 4 章虽然偏基础，但很多论断已经需要和后续的新 benchmark / theory / transferable prompt 结果相衔接。
- 第 6 章应用、第 7 章 ProG、第 8 章挑战与未来方向，都没有反映 2024-2026 的新增主线。
- 图表、taxonomy、summary table、bibliography 也都需要同步更新，否则正文即使改了，整篇 survey 的结构仍然会显得失配。

因此建议把这次改稿理解为一次“全书口径校正”，而不是局部补 cite。

---

## 2. 最优先需要统一的全局问题

### 2.1 叙述时间点需要整体后移

当前多个章节还在使用以下类型的表述：

- “Recently, some researchers have started...”
- “there are only a few graph prompt works...”
- “a consistent framework remains unavailable”
- “there is a lack of evaluation criteria / benchmark / theory”

这些句子在 2023 年成立，但现在已经明显过时。至少需要统一改成：

- graph prompt 已从少量早期方法扩展到更丰富的方法谱系；
- 已出现 benchmark、理论分析和新的 survey；
- 研究重点已从“prompt 是否有效”转向“prompt 如何更高效、更可迁移、更鲁棒、更适配复杂图场景”。

这类措辞上的统一，应该同时体现在：

- `tex/0.main.tex` 的 abstract
- `tex/1.intro.tex`
- `tex/2.methodology.tex`
- `tex/8.Discussion.tex`
- `tex/9.Conclusion.tex`

---

### 2.2 survey 的主问题设置需要和现在的文献版图重新对齐

当前全书是按 AGI 三问题来组织：

- cross-modalities
- cross-domains
- cross-tasks

这个视角仍然能保留，但有两个明显问题：

1. 现在候选池中最有代表性的新增工作，并不主要集中在“泛化的跨模态”，而是集中在：
   - dynamic / temporal graphs
   - continual learning
   - streaming recommendation
   - federated heterogeneity
   - cross-domain adaptation
   - robustness

2. 第 5 章已经逐渐从“AGI 愿景叙述”走向“pretrained GNN adaptation 的具体机制叙述”。如果前后文继续强行用 AGI 大词框住，会造成 scope mismatch。

建议：

- 不必删除 AGI 叙事，但要降虚增实。
- 引言和方法学里应明确说明：本文当前真正覆盖最充分的是 `graph prompt for pretrained graph model adaptation`，并进一步延展到 text-attributed / dynamic / federated / cross-domain 等复杂设定。
- 第 6 章和第 8 章应顺势把“复杂图场景”作为主轴，而不是泛泛谈 AGI 愿景。

---

### 2.3 图表、taxonomy、summary table 现在是系统性过时，不是局部过时

需要联动修改的对象至少包括：

- `tex/pic/taxonomy.tex`
- `tex/table/graph_prompt_summary.tex`
- `tex/pic/prompt.pdf`
- `tex/pic/reference_venue.pdf`
- `tex/pic/top_keywords_bar.png`

原因：

- taxonomy 仍以 2023 年的章节结构和代表作组织，无法容纳新的 prompt 注入空间和复杂场景。
- summary table 只包含早期十余篇方法，已经无法支撑“survey”这个定位。
- literature overview 的 venue distribution 和 keyword 图如果继续沿用旧语料，会与正文新增文献不一致。
- prompt 总图如果仍只强调 token / structure / inserting pattern，则难以覆盖 edge/topology/message/universal/instance-aware 等更新方向。

这部分建议不要零敲碎打，应该作为一个单独任务：在正文结构定稿后，再整体重画/重导出。

---

### 2.4 bibliography 需要系统补充

`tex/zotero.bib` 当前没有覆盖本轮新增候选文献中的核心论文，因此只改正文是不够的。

至少应补入这些新主线文献：

- ProG: A Graph Prompt Learning Benchmark
- Does Graph Prompt Work? A Data Operation Perspective with Theoretical Analysis
- Graph Prompting for Graph Learning Models: Recent Advances and Future Directions
- A Unified Graph Selective Prompt Learning for Graph Neural Networks
- Prompt Learning on Temporal Interaction Graphs
- Prompt-Based Spatio-Temporal Graph Transfer Learning
- SGPT
- Instance-Aware Graph Prompt Learning
- GraphSparse Prompting
- FedGPL
- RELIEF
- IGAP
- DAGPrompT
- CLEAR
- EdgePrompt
- GraphPrompter
- One Prompt Fits All
- GraphTOP
- MAGPrompt
- GP2F
- Adversarial Graph Prompting
- P2TAG
- PROMPTCGL
- EVP
- LEAP

建议做法：

- 先确定“正文主线必引文献”，优先补 12-15 篇。
- 之后再补扩展讨论文献，避免一次性把 bib 搞得过重。

---

## 3. 分文件修改建议

## 3.1 `tex/0.main.tex`

这是全书入口，虽然正文内容不多，但有两个明显问题。

### 需要修改的点

- **Abstract 口径过旧**
  当前 abstract 仍在强调“first to propose a unified framework”“over 100 works”“AGI application to graph data remains nascent”等说法，需要重新校准。

- **Abstract 需要显式体现新进展**
  现在 abstract 没有反映：
  - benchmark 已出现
  - graph prompt 已有理论分析
  - graph prompt 已扩展到 dynamic / cross-domain / continual / federated 等场景

- **ProG / website 的描述顺序有歧义**
  当前句子：
  `ProG and the website can be accessed by ... respectively`
  读起来容易混淆 library 和 website 对应哪个链接。

### 建议怎么改

- 将 abstract 中 “pioneering / first / emerging” 的口吻改为“systematizes a rapidly expanding field”。
- 在 abstract 中加入 benchmark 和 theory 的一句概括。
- 将 ProG 的描述改为：
  - `We also discuss ProG, a benchmark and software ecosystem for standardized evaluation...`
  - 再分开给 library repo 和 awesome list。

---

## 3.2 `tex/1.intro.tex`

引言是除第 5 章外，最需要改的章节之一。

### 主要问题

- **开篇 AGI 叙述过大，graph prompt 主线过晚进入**
  当前第一段用了较多篇幅讲 ChatGPT / Midjourney / AGI，而 graph prompt 的方法问题要到后面才出现。

- **图 1 的“三大 AGI 问题”仍可保留，但解释需要更贴合 graph prompt**
  现在 candidate pool 已显示，真实增长点是 dynamic / continual / federated / cross-domain，而不是泛泛的所有 AGI 子问题。

- **“Recently, some researchers have started...” 已经过时**
  需要改成“graph prompt 已形成较为完整的方法谱系”。

- **“缺乏 evaluation criteria” 这类断言需要更新**
  ProG 已可作为 benchmark 支撑，理论文献也开始出现。

- **RQ 设置需要细调**
  当前 RQ2 是 why prompt，RQ3 是 how to design，RQ4 是 deployment，RQ5 是 challenges。  
  这套结构还可以用，但要在引言中提前声明：
  - benchmark / theory 是新版 survey 的重要增量；
  - real-world deployment 不再只等于“写工具包”，还包括流式、持续、联邦、跨域等复杂环境。

### 建议怎么改

- 压缩 AGI 背景，尽快把问题收束到：
  - graph pre-training 与 downstream gap
  - prompt 的 parameter efficiency
  - graph-specific prompt design difficulty
  - complex graph settings

- 在介绍当前局限时加入三类更新：
  - benchmark：ProG
  - theory：Does Graph Prompt Work?
  - survey update：Graph Prompting for Graph Learning Models

- 在 RQ 部分加入一句说明：
  - 新版 survey 不只回答“prompt 怎么设计”，也关注“prompt 如何在跨域、动态图、联邦和持续学习场景中发挥作用”。

### 建议新增进入引言的代表作

- ProG
- Does Graph Prompt Work?
- GPT4Rec
- GraphPrompter
- DAGPrompT
- GP2F
- Prompt-Driven Continual Graph Learning

---

## 3.3 `tex/2.methodology.tex`

这是全书第二个最需要重写的地方，因为 taxonomy 决定了后面所有章节的组织方式。

### 主要问题

- **taxonomy 仍是 2023 版**
  当前 taxonomy 把 graph prompt 主要分成：
  - pre-training strategies
  - prompt design
  - multi-modal prompting
  - domain adaptation
  但现在明显不够。

- **`Prompt Design` 内部结构也已过时**
  它仍围绕：
  - prompt tokens / graphs
  - answering function
  - prompt tuning
  这与新文献已经不匹配。

- **literature overview 的统计图很可能失真**
  如果语料更新了，venue distribution 和 keyword 图必须重算。

- **existing work comparison 只对比到 2023 survey**
  现在应该补 2025 的 survey work，并重新定位本文的差异。

### 建议怎么改

建议把 taxonomy 改成“双轴”而不是“树状只按章节走”：

1. **按 prompt 注入空间**
   - feature/token
   - edge/topology
   - message/readout
   - prompt graph / structured prompt

2. **按适配场景**
   - homogeneous static graph
   - hetero graph
   - signed graph
   - text-attributed graph
   - temporal/dynamic graph
   - continual/streaming/federated
   - cross-domain / transfer
   - robust / adversarial

然后把章节安排映射到这两个轴，而不是让 taxonomy 完全复制章节标题。

### 需要同步修改的内容

- `Research Objectives` 表格中的问题定义
- `Taxonomy` 正文描述
- `Literature Overview`
- `Connection to Existing Work`
- `pic/taxonomy.tex`

### `Connection to Existing Work` 建议补充

- 保留对 `wu2023survey` 的比较，但需要说明它的时间边界。
- 新增对 2025 survey 的比较。
- 明确本文新版相对已有 survey 的差异：
  - 更强调 benchmark + theory + complex settings
  - 更强调 prompt 注入空间与适配场景的统一 taxonomy

---

## 3.4 `tex/3.Preliminaries.tex`

这一章看似基础，实际上有不少内容需要口径更新。

### 主要问题

- **“Why Prompt?” 仍是纯作者观点，缺少后续理论工作呼应**
  现在已经有 `Does Graph Prompt Work?` 这类理论工作，应该补进来。

- **flexibility vs. expressiveness 框架仍可保留，但需要降绝对化口吻**
  现在 prompt 不只是“加 token 提高 flexibility”，而是已经扩展到边、拓扑、消息传递和复杂场景适配。

- **pre-training and fine-tuning 介绍太传统**
  新工作表明并非所有 graph prompt 都强依赖特定 pretext；一些方法开始走 pretraining-agnostic / universal prompt 路线。

- **部分技术例子需要核对准确性**
  例如 “Graph Convolution Networks (GCN)~\cite{niepert2016learning}” 这一处引用很可疑，建议全文检查基础模型引用是否准确。

### 建议怎么改

- 在 `Why Prompt?` 小节末尾加入一段：
  - 现代理论工作从 data operation 视角分析 prompt 的有效性；
  - prompt 不只是“输入技巧”，还可被视为对图变换算子的近似。

- 在 `Pre-training and Fine-tuning` 小节加一句：
  - 近年也出现了对 pretext 依赖更弱、强调通用适配的 graph prompt 方法。

- 在图 `WhyPrompt2.pdf` 的配文或正文解释中强调：
  - 这个图是“理解 prompt 的一个视角”，不是完整分类体系。

### 推荐补入或呼应的文献

- Does Graph Prompt Work?
- One Prompt Fits All
- LEAP
- MAGPrompt

---

## 3.5 `tex/4.Pre-training.tex`

这一章基础框架问题不大，但需要和新版第 5 章的叙述接轨。

### 主要问题

- **当前写法默认 prompt 方法高度依赖具体 pretext**
  但 2024-2026 新文献中，已经出现“通用 prompt / pretraining-agnostic prompt / representation-level adaptation”的趋势。

- **只讲经典 node/edge/graph/multi-task pre-training，不够解释新 prompt 方向**
  例如：
  - text-attributed graph pre-training
  - graph-text joint pre-training
  - dynamic graph pre-training
  - heterogeneous/signed graph 适配
  都会影响 prompt 的设计空间。

- **`Further Discussion` 结尾对 prompting 的评价过于绝对**
  当前写成 prompting 几乎是“不可阻挡趋势”，语气太满，也没有反映选择性 prompt、通用 prompt、adapter 式 prompt 等分化路径。

### 建议怎么改

- 保留 node/edge/graph/multi-task 四分法作为基础综述，但在开头或结尾补一句：
  - 近年的 graph prompt 已逐渐从“针对预训练任务定制”扩展到“更通用的 downstream adaptation interface”。

- 在每类 pre-training 的结尾各补一句“与 prompt 的关系”：
  - node-level pretraining 更容易衍生 feature/message-level prompt
  - edge-level pretraining 更容易衍生 link/template/edge prompt
  - graph-level pretraining 更容易衍生 prompt graph / in-context graph prompting

- `Further Discussion` 段落建议降低价值判断，改为：
  - prompting 是一条重要路线，但并非完全替代 fine-tuning；
  - 新工作也在探索 prompt、adapter、LoRA、partial tuning 的边界。

### 与第 5 章联动的必要修改

- `table/graph_prompt_summary.tex` 必须重做，否则第 4 章末尾的 summary table 会和新版第 5 章脱节。

---

## 3.6 `tex/5.tex`

这一章的详细建议已经单列在 [Section5-修改建议.md](/mnt/d/Graph/gpl-survey/docs/papers/Section5-修改建议.md)。

这里只强调一件事：

- 第 5 章一旦改成新版 taxonomy，`2.methodology.tex`、`4.Pre-training.tex`、`6.Applications.tex`、`8.Discussion.tex` 都必须同步改口径，否则前后文会断裂。

---

## 3.7 `tex/6.Applications.tex`

这一章目前只有 23 行，是全书最明显偏弱的一章之一。

### 主要问题

- **内容过于泛化且偏“展望式”**
  现在主要列了 online social networks、recommender systems、knowledge management、biology，但很多地方是在说“未来有潜力”，而不是总结 graph prompt 已有的代表性应用。

- **与当前候选池的新增文献错位**
  现在真正能支撑“应用/复杂场景”章节的新增文献包括：
  - GPT4Rec：流式推荐
  - P2TAG：文本属性图 few-shot 节点分类
  - STGP：时空图迁移
  - SGPT：signed graph
  - PROMPTCGL：持续图学习
  - FedGPL：联邦异质场景
  - EVP：动态图事件建模

- **“application” 与 “setting” 混在一起**
  现在有的像行业应用，有的像任务环境。建议统一口径。

### 建议怎么改

建议把 `Potential Applications` 改成更扎实的：

- `Applications and Advanced Settings`
  或
- `Graph Prompting in Realistic Graph Scenarios`

然后按以下 4 类组织：

1. **Recommendation and streaming environments**
   - GPT4Rec

2. **Text-attributed and multimodal-leaning graph settings**
   - P2TAG

3. **Temporal, dynamic, and continual graphs**
   - TIGPrompt
   - STGP
   - PROMPTCGL
   - EVP

4. **Cross-domain, federated, and robust deployment**
   - FedGPL
   - GP2F
   - DAGPrompT
   - Adversarial Graph Prompting

如果篇幅不够，不建议保留现在知识管理/biology 那种泛泛讨论，应改成“有具体 graph prompt 方法支撑的场景”。

---

## 3.8 `tex/7.ProG.tex`

这一章标题和内容都需要升级。

### 主要问题

- **当前把 ProG 写成 library-only**
  但现在候选池中的 ProG 论文更重要的价值之一，是 benchmark。

- **正文提到的集成方法和评测规模明显过旧**
  现在不应只强调 All in One / GPPT / GPF / GPF-Plus。

- **这一章与第 5 章的 benchmark 讨论尚未形成呼应**
  既然 ProG 已是 candidate pool 中唯一 benchmark 类论文，就应该让它在 survey 里承担“评测基座”的角色，而不是只做工具宣传。

### 建议怎么改

建议把标题改成：

- `ProG: Benchmark and Ecosystem for Graph Prompting`
  或
- `ProG: Standardized Evaluation for Graph Prompt Learning`

正文建议拆成两部分：

1. **Benchmark perspective**
   - ProG 统一了哪些 pre-training methods、prompt methods、datasets、metrics
   - 它为什么对 graph prompt survey 很关键
   - 它如何帮助比较不同 prompt 的效率、灵活性和性能

2. **Software ecosystem**
   - library
   - awesome list
   - reproducibility value

如果第 5 章新增 benchmark 讨论，这一章就不再是附录式工具介绍，而是 survey 证据链的一部分。

---

## 3.9 `tex/8.Discussion.tex`

这一章需要重写，不建议只做小修。

### 当前问题

- **challenge 列表仍然是 2023 年视角**
  例如“缺乏理论基础”“缺乏 transferable prompt”这些今天仍然是问题，但现在应该改成“已有初步进展，但仍存在哪些缺口”。

- **future directions 与当前新增文献脱节**
  例如 transferable learning 已不应只作为未来愿景，因为现在已经有：
  - IGAP
  - DAGPrompT
  - GP2F
  - One Prompt Fits All

- **没有覆盖新的关键挑战**
  当前缺少：
  - benchmark consistency
  - robustness
  - dynamic/continual adaptation
  - federated heterogeneity
  - universal vs selective prompt 的理论张力

### 建议怎么改

建议把 `Current Challenges` 改成下面 5 类：

1. **Benchmark consistency and fair evaluation**
   - 用 ProG 引出“已有起点，但仍不完整”

2. **Theory and mechanism understanding**
   - 用 Does Graph Prompt Work? 说明理论开始出现，但还不够

3. **Transferability across domains and settings**
   - IGAP / DAGPrompT / GP2F / UniPrompt

4. **Prompt design under complex graph dynamics**
   - TIGPrompt / GPT4Rec / PROMPTCGL / EVP / FedGPL

5. **Reliability, robustness, and interpretability**
   - GraphSparse / AGP / Graph Your Own Prompt / selective prompt methods

`Future Directions` 则建议对应改成：

- unified prompt theory
- graph foundation model adaptation
- prompting for dynamic and lifelong graphs
- trustworthy and robust graph prompting
- reproducible benchmark and deployment ecosystem

这样写，能自然承接新版第 5 章，而不是和正文脱节。

---

## 3.10 `tex/9.Conclusion.tex`

这一章现在过短，不足以承接新版 survey 的增量。

### 建议怎么改

- 在结论中增加 3 个点：
  - graph prompt 的版图已经从早期 token/graph prompt 扩展到 edge/topology/message/universal prompt；
  - benchmark 与 theory 的出现，标志着该方向从“现象性成功”转向“体系化发展”；
  - 真正重要的未来问题不只是“有没有 prompt”，而是“prompt 如何在复杂场景中可靠部署”。

- 结论应与第 8 章保持一致，不要再只重复 AGI 宏大叙事。

---

## 4. 图表与辅助文件的修改建议

## 4.1 `tex/pic/taxonomy.tex`

这是高优先级重做项。

当前问题：

- 树结构完全复制旧章节结构；
- 代表文献几乎都停留在 2023；
- 无法表达“注入空间”和“适配场景”两个正交维度。

建议：

- 重新设计 taxonomy，不必坚持单棵树。
- 至少把 `Prompt Design` 改成：
  - feature/token
  - edge/topology
  - message/readout
  - prompt graph/structured
- 把 `Advanced Settings` 单独列出：
  - hetero
  - signed
  - TAG
  - temporal/dynamic
  - continual/federated/cross-domain

---

## 4.2 `tex/table/graph_prompt_summary.tex`

这是必须重做项。

当前问题：

- 只覆盖早期代表作；
- 列设计高度依赖旧 taxonomy；
- 新文献加入后表格会严重失衡。

建议：

- 至少新增以下列：
  - prompt injection space
  - graph setting
  - adaptation scope
  - optimization type
  - publication status

- 只保留 12-15 篇“主线代表作”，不要试图把所有文献都塞进一张表。

建议进入主表的文献：

- GPPT
- GPF / GPF-Plus
- All in One
- GraphPrompt
- PRODIGY
- EdgePrompt
- GraphTOP
- IA-GPL
- RELIEF
- IGAP
- DAGPrompT
- GraphPrompter
- UniPrompt
- TIGPrompt 或 PROMPTCGL

---

## 4.3 `tex/zotero.bib`

建议把 bib 更新单独作为一个任务处理。

原因：

- 新正文至少需要 12-15 篇新文献；
- 现有 bib 对应键值风格要保持统一；
- taxonomy、table、discussion、applications 都会依赖这些引用。

---

## 5. 推荐的改稿顺序

如果要控制风险，建议按下面顺序推进：

1. 先定新版第 5 章结构。
2. 用新版第 5 章反推 `2.methodology.tex` 的 taxonomy。
3. 修改 `1.intro.tex` 和 `0.main.tex`，统一全书叙事口径。
4. 修改 `6.Applications.tex`、`7.ProG.tex`、`8.Discussion.tex`。
5. 最后统一重做：
   - `pic/taxonomy.tex`
   - `table/graph_prompt_summary.tex`
   - `zotero.bib`
   - abstract / conclusion 的收束表述

这个顺序的好处是：先把“核心分类”定下来，再改前言和后文，不容易来回返工。

---

## 6. 一句话总结

这篇 survey 现在最需要的，不是“把 2024-2026 论文补进去”，而是把整本稿件从“2023 年的 graph prompt 起步期综述”，升级成“面向 benchmark、theory、复杂图场景与真实部署问题的新版系统综述”。

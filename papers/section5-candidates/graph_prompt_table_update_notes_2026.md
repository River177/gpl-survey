# Graph Prompt 表格更新说明（2026）

这份说明用于筛选 2024-2026 年的 graph prompting 方法，看哪些值得加入 `tex/table/graph_prompt_summary.tex`。

## 适用范围

当前这张表是“方法表”，不是“综述表”或“benchmark 表”。因此，一个候选工作只有在满足下面条件时才适合加入：

1. 它是一个具体的 graph prompting 方法，而不是 survey、benchmark 或纯理论分析论文。
2. 它能映射到当前表格的列：
   - pre-training task
   - prompt design
   - downstream task
   - answering function
3. 它足够有代表性，值得单独占一行。
4. 最好已经发表在较强的会议/期刊；如果仍是 preprint，也应当机制明确、代表性较强。

下文中的“权威性”采用以下简单分级：

- 高：顶会或较强正式发表 venue，例如 KDD、WWW、NeurIPS、SIGIR、ICDE、CIKM 等
- 中：已正式发表但 venue 更专门，或仍是高质量 preprint、但方法贡献较清楚
- 低：仅 arXiv、过于专门化，或与当前表格不够匹配

## 高优先级新增候选

如果要更新这张表，这几篇是最值得优先加入的。

| 方法 | 发表 venue / 状态 | 权威性 | 是否建议入表 | 如果表格长度要控制，建议替换谁 | 原因 |
|---|---|---:|---:|---|---|
| Inductive Graph Alignment Prompt | WWW 2024 | 高 | 是 | 替换 `ULTRA-DP` | 这是一个更强、且已正式发表的 prompt-based adaptation 方法，明确连接了 graph pre-training 与下游适配，比当前未发表的 `ULTRA-DP` 更适合作为代表。 |
| RELIEF | KDD 2025 | 高 | 是 | 替换 `SGL-PT` | 机制上引入了 reinforcement-learning-driven feature prompt tuning，更通用，也比当前未发表的 `SGL-PT` 更新。 |
| DAGPrompT | WWW 2025 | 高 | 是 | 替换 `PGCL` 或 `SAP` | 这是近两年最强的一类通用 graph prompt tuning 方法之一，机制清楚，实验也扎实。 |
| GraphPrompter | ICDE 2025 | 高 | 如果希望覆盖 graph in-context learning，则建议加入 | 替换 `PGCL` | 如果你希望表格不仅覆盖标准 downstream prompt tuning，也覆盖 graph in-context learning，那么它很有代表性。 |
| Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs | KDD 2024 | 高 | 如果希望主表反映 TAG / 多模态方向，则建议加入 | 优先新增；若必须替换，可替换 `SAP` | 它代表了 text-attributed graph 上的 prompting 方法，这是当前表里没有覆盖的。 |

## 有条件加入的候选

这些方法本身是有效候选，但是否加入，取决于你想让这张表覆盖得多宽。

| 方法 | 发表 venue / 状态 | 权威性 | 是否建议入表 | 备注 |
|---|---|---:|---:|---|
| GPT4Rec | SIGIR 2024 | 高 | 视情况而定 | 论文质量强，但高度偏向 streaming recommendation。更适合写在 application / discussion 中，而不是主方法表，除非你明确希望表格覆盖推荐系统 prompting。 |
| Prompt-Based Spatio-Temporal Graph Transfer Learning | CIKM 2024 | 高 | 视情况而定 | 是一篇不错的 prompt-based transfer 方法，但针对时空图，场景较专。只有在你希望主表覆盖 dynamic / temporal graph 时才值得加入。 |
| CLEAR | 2025，正式发表为 LNCS chapter | 中 | 视情况而定 | 适合作为 heterogeneous graph prompting 的补充方法。如果你想在 `HetGPT` 之外再加一个异构图代表方法，可以考虑。 |
| SGPT | CIKM 2025 | 高 | 视情况而定 | signed graph 上的 prompting 很新，也有意思，但仍偏领域特化。更适合作为 extension，而不是核心代表行。 |
| One Prompt Fits All | arXiv 2025 | 中 | 暂时可观察 | “universal adaptation” 方向很贴近你的表，但目前还是 preprint。后续如果发表了，会很值得加入。 |
| Edge Prompt Tuning for GNNs | arXiv 2025 | 中 | 暂时可观察 | 在机制上有新意，因为它提示的是 edge，而不是只提示 node feature。发表后会是很好的补充。 |
| MAGPrompt | arXiv 2026 | 中 | 暂时可观察 | 机制上把 prompting 推到 message-passing 层面，思路不错，但时间太新。 |
| Unsupervised Prompting for Graph Neural Networks | arXiv 2025 | 中 | 暂时可观察 | 一个额外检到的方法，优点是摆脱了 label 依赖，但目前还没有正式发表。 |
| GP2F | arXiv 2026 | 中 | 暂时可观察 | 跨域 prompt transfer 很相关，但还太新。 |
| GraphTOP | arXiv 2025 | 中 | 暂时可观察 | topology-oriented prompting 的方向值得关注，但目前还是 preprint。 |

## 不建议加入主方法表的候选

这些论文对正文讨论可能有价值，但不适合作为主方法表中的一行。

| 论文 | 发表 venue / 状态 | 是否建议入表 | 不建议入表的原因 |
|---|---|---:|---|
| ProG: A Graph Prompt Learning Benchmark | NeurIPS 2024 | 否 | 这是 benchmark，不是新的 prompting 方法。更适合在 evaluation / tooling 部分引用。 |
| Towards Graph Prompt Learning: A Survey and Beyond | arXiv survey | 否 | 综述论文，不是方法行。 |
| Graph Prompting for Graph Learning Models: Recent Advances and Future Directions | KDD 2025 | 否 | 这是综述 / perspective，不是方法。 |
| Does Graph Prompt Work? A Data Operation Perspective with Theoretical Analysis | arXiv 2025 | 否 | 偏理论与分析，不是一个新的 prompting 机制。 |
| Prompt-Driven Continual Graph Learning | arXiv 2025 | 目前不建议 | continual learning 场景较专，而且仍是 preprint，不适合作为当前主表代表方法。 |
| Graph Your Own Prompt | arXiv 2025 | 否 | 更接近 self-prompting / consistency 风格，不太适合当前表格的标准 taxonomy。 |
| Learning and Editing Universal Graph Prompt Tuning via Reinforcement Learning | arXiv 2025 | 目前不建议 | 太新，且尚未正式发表。 |
| Reliable and Compact Graph Fine-tuning via GraphSparse Prompting | arXiv 2024 | 目前不建议 | 更像 graph fine-tuning / sparsification 方向，不是一个很干净的 prompt taxonomy 行。 |
| Against Multifaceted Graph Heterogeneity via Asymmetric Federated Prompt Learning | arXiv 2024 | 否 | federated setting 过于专门化。 |
| Instance-Aware Graph Prompt Learning | arXiv 2024 | 目前不建议 | 想法有意思，但仍是 preprint，且代表性还不如更强的已发表方法。 |
| Prompt Learning on Temporal Interaction Graphs | arXiv 2024 | 否 | 当前 metadata 不能确认它有对应正式发表版本，而且 dynamic graph 范围较专。 |
| When Prompting Meets Spiking | arXiv 2026 | 否 | 太新，也过于专门化。 |
| Robust Graph Fine-Tuning with Adversarial Graph Prompting | arXiv 2026 | 目前不建议 | 更偏 robustness 特定问题，而不是主流代表方法。 |

## 完整候选筛选结果

这部分覆盖了本地 `section5-candidates` 文件夹中的候选论文，以及检索中额外发现的一篇方法论文。

| 方法 | 年份 | 发表 venue / 状态 | 权威性 | 是否建议入表 | 备注 |
|---|---:|---|---:|---:|---|
| Inductive Graph Alignment Prompt | 2024 | WWW 2024 | 高 | 是 | 已发表，且非常适合替换 `ULTRA-DP`。 |
| Prompt-Based Spatio-Temporal Graph Transfer Learning | 2024 | CIKM 2024 | 高 | 视情况而定 | 时空图方向较专。 |
| ProG | 2024 | NeurIPS 2024 | 高 | 否 | benchmark，不是方法行。 |
| GPT4Rec | 2024 | SIGIR 2024 | 高 | 视情况而定 | 推荐系统特化。 |
| A Unified Graph Selective Prompt Learning for GNNs | 2024 | 仅 arXiv | 中 | 暂时观察 | 没找到明确正式发表版本。 |
| Pre-Training and Prompting for Few-Shot Node Classification on TAGs | 2024 | KDD 2024 | 高 | 是 | 很适合补齐 TAG / 多模态方向。 |
| RELIEF | 2025 | KDD 2025 | 高 | 是 | 很适合作为新的核心代表方法。 |
| Does Graph Prompt Work? | 2025 | 仅 arXiv | 中 | 否 | 理论/分析论文。 |
| GraphSparse Prompting | 2024 | 仅 arXiv | 中 | 暂时不建议 | 更偏 fine-tuning 方向。 |
| Asymmetric Federated Prompt Learning | 2024 | 仅 arXiv | 低 | 否 | 过于专门化。 |
| Instance-Aware Graph Prompt Learning | 2024 | 仅 arXiv | 中 | 暂时不建议 | 还不够成熟。 |
| SGPT | 2025 | CIKM 2025 | 高 | 视情况而定 | signed graph 上的代表方法。 |
| DAGPrompT | 2025 | WWW 2025 | 高 | 是 | 很适合主表。 |
| Prompt-Driven Continual Graph Learning | 2025 | 仅 arXiv | 中 | 暂时不建议 | continual setting 较专。 |
| CLEAR | 2025 | LNCS 正式发表 | 中 | 视情况而定 | 可作为 heterogeneous graph 的补充方法。 |
| Edge Prompt Tuning for GNNs | 2025 | 仅 arXiv | 中 | 暂时观察 | 机制有新意，但未正式发表。 |
| GraphPrompter | 2025 | ICDE 2025 | 高 | 是 | 如果要覆盖 graph in-context learning，它很重要。 |
| Graph Prompting for Graph Learning Models: Recent Advances and Future Directions | 2025 | KDD 2025 | 高 | 否 | survey / perspective。 |
| One Prompt Fits All | 2025 | 仅 arXiv | 中 | 暂时观察 | universal adaptation 很有潜力。 |
| Graph Your Own Prompt | 2025 | 仅 arXiv | 低 | 否 | 不够贴合当前表格 taxonomy。 |
| Event-Aware Prompt Learning for Dynamic Graphs | 2025 | 仅 arXiv | 中 | 暂时不建议 | dynamic graph 特化。 |
| GraphTOP | 2025 | 仅 arXiv | 中 | 暂时观察 | topology-oriented prompting 有潜力。 |
| Learning and Editing Universal Graph Prompt Tuning via RL | 2025 | 仅 arXiv | 中 | 暂时不建议 | 太新。 |
| Robust Graph Fine-Tuning with Adversarial Graph Prompting | 2026 | 仅 arXiv | 中 | 暂时不建议 | robustness 特化。 |
| When Prompting Meets Spiking | 2026 | 仅 arXiv | 低 | 否 | 太新且过于专门。 |
| MAGPrompt | 2026 | 仅 arXiv | 中 | 暂时观察 | message-adaptive 机制值得后续跟踪。 |
| GP2F | 2026 | 仅 arXiv | 中 | 暂时观察 | cross-domain prompting 很相关，但还太早。 |
| Unsupervised Prompting for Graph Neural Networks | 2025 | 仅 arXiv | 中 | 暂时观察 | 本地候选外额外检到的方法，优点是摆脱 label supervision，但暂未正式发表。 |

## 如果需要替换现有表格行，建议顺序

如果希望控制表格长度，优先按下面顺序替换：

1. 用 `Inductive Graph Alignment Prompt (WWW 2024)` 替换 `ULTRA-DP`
2. 用 `RELIEF (KDD 2025)` 替换 `SGL-PT`
3. 用 `DAGPrompT (WWW 2025)` 替换 `PGCL`
4. 如果还想再换一行：
   - 如果你希望表格覆盖 graph in-context learning，就用 `GraphPrompter (ICDE 2025)` 替换 `SAP`
   - 如果你更想体现 TAG / 多模态扩展，就用 `Pre-Training and Prompting for Few-Shot Node Classification on TAGs (KDD 2024)` 替换 `SAP`

## 最小更新方案

如果你希望保守更新，但明显比现在新，建议只加这三篇：

- Inductive Graph Alignment Prompt (WWW 2024)
- RELIEF (KDD 2025)
- DAGPrompT (WWW 2025)

如果你希望做一个更完整的 2026 版本，再额外加入两篇：

- GraphPrompter (ICDE 2025)
- Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs (KDD 2024)


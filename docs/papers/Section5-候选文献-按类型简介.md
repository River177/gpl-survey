# Section 5 候选文献（30篇）按类型简介

> 目标：将候选池按文献类型整理，便于后续改写第5章时按需引用。  
> 说明：每篇仅保留“1-2句用途导向简介”，强调它能补第5章哪个缺口。

---

## A. Benchmark（1篇）

### 1) ProG: A Graph Prompt Learning Benchmark (2024)
- 链接：https://arxiv.org/abs/2406.05346
- 简介：构建统一评测框架，重点解决不同 graph prompt 方法难以公平比较的问题。对第5章价值在于给“方法优劣比较”提供共同实验底座。

---

## B. Theory（1篇）

### 2) Does Graph Prompt Work? A Data Operation Perspective with Theoretical Analysis (2024)
- 链接：https://arxiv.org/abs/2410.01635
- 简介：从数据操作/理论视角解释 graph prompt 生效机制与边界条件。可用于第5章讨论“为什么有效、什么时候失效”。

---

## C. Survey（2篇）

### 3) Graph Prompting for Graph Learning Models: Recent Advances and Future Directions (2025)
- 链接：https://arxiv.org/abs/2506.08326
- 简介：面向 graph prompting 的阶段性综述，覆盖方法、应用与挑战。可用于第5章 related discussion 对照。

### 4) Towards Graph Prompt Learning: A Survey and Beyond (2024)
- 链接：https://arxiv.org/abs/2408.14520
- 简介：补充 2024 版本的综述视角，帮助对齐术语和分类口径。可用于检查第5章分类是否完整。

---

## D. Application（1篇）

### 5) GPT4Rec: Graph Prompt Tuning for Streaming Recommendation (2024)
- 链接：https://arxiv.org/abs/2406.08229
- 简介：将 graph prompt 用于流式推荐场景，强调动态数据下的可适配性。可作为第5章方法外延到真实场景的示例。

---

## E. Method（25篇）

### 6) A Unified Graph Selective Prompt Learning for Graph Neural Networks (2024)
- 链接：https://arxiv.org/abs/2406.10498
- 简介：提出选择性 prompt 机制，避免“一刀切”提示注入。补强第5章 token 设计分支。

### 7) Prompt Learning on Temporal Interaction Graphs (2024)
- 链接：https://arxiv.org/abs/2402.06326
- 简介：面向时序交互图的 prompt 学习，强调时间维建模。补齐第5章对动态图的覆盖。

### 8) Prompt-Based Spatio-Temporal Graph Transfer Learning (2024)
- 链接：https://arxiv.org/abs/2405.12452
- 简介：针对时空图迁移场景，讨论 prompt 在跨域适配中的作用。可用于第5章 transferability 讨论。

### 9) SGPT: Few-Shot Prompt Tuning for Signed Graphs (2024)
- 链接：https://arxiv.org/abs/2412.12155
- 简介：聚焦 signed graph 的少样本提示调优。补充第5章在特殊图结构上的方法可迁移性。

### 10) Instance-Aware Graph Prompt Learning (2024)
- 链接：https://arxiv.org/abs/2411.17676
- 简介：引入实例感知提示，强调样本个体差异。适合放在第5章 prompt token/structure 的进化脉络里。

### 11) Reliable and Compact Graph Fine-tuning via GraphSparse Prompting (2024)
- 链接：https://arxiv.org/abs/2410.21749
- 简介：用稀疏提示提升参数效率与可靠性。可补第5章“效率 vs 性能”的平衡讨论。

### 12) Against Multifaceted Graph Heterogeneity via Asymmetric Federated Prompt Learning (2024)
- 链接：https://arxiv.org/abs/2411.02003
- 简介：联邦+异构设定下的 prompt 学习。可补第5章跨域异质场景的实证支撑。

### 13) RELIEF: Reinforcement Learning Empowered Graph Feature Prompt Tuning (2024)
- 链接：https://arxiv.org/abs/2408.03195
- 简介：将 RL 引入 prompt 调优策略，强调策略层学习。可补第5章 prompt tuning 方法维度。

### 14) Inductive Graph Alignment Prompt: Bridging the Gap ... from Spectral Perspective (2024)
- 链接：https://arxiv.org/abs/2402.13556
- 简介：从谱域角度桥接 pre-train 与 inductive fine-tune。可用于第5章任务对齐机制补强。

### 15) DAGPrompT: Distribution-aware Graph Prompt Tuning (2025)
- 链接：https://arxiv.org/abs/2501.15142
- 简介：强调分布感知的提示优化，面向分布偏移问题。补第5章泛化稳定性。

### 16) CLEAR: Cluster-based Prompt Learning on Heterogeneous Graphs (2025)
- 链接：https://arxiv.org/abs/2502.08918
- 简介：以聚类结构辅助异构图 prompt 学习。补第5章 hetero graph 分支。

### 17) Edge Prompt Tuning for Graph Neural Networks (2025)
- 链接：https://arxiv.org/abs/2503.00750
- 简介：将提示从节点扩展到边，丰富插入模式。可直接扩展第5章 inserting pattern 小节。

### 18) DP-GPL: Differentially Private Graph Prompt Learning (2025)
- 链接：https://arxiv.org/abs/2503.10544
- 简介：在 graph prompt 中引入差分隐私约束。适合放在第5章风险与约束讨论。

### 19) GraphPrompter: Multi-stage Adaptive Prompt Optimization for Graph In-Context Learning (2025)
- 链接：https://arxiv.org/abs/2505.02027
- 简介：面向 graph ICL 的多阶段自适应优化。可补第5章 answering/tuning 的新范式。

### 20) One Prompt Fits All: Universal Graph Adaptation for Pretrained Models (2025)
- 链接：https://arxiv.org/abs/2509.22416
- 简介：探索统一提示跨任务/跨域适配。补第5章 transferable prompt 议题。

### 21) GraphTOP: Graph Topology-Oriented Prompting for Graph Neural Networks (2025)
- 链接：https://arxiv.org/abs/2510.22451
- 简介：拓扑导向提示设计，突出结构先验。补第5章 graph-based prompt 设计路径。

### 22) MAGPrompt: Message-Adaptive Graph Prompt Tuning for Graph Neural Networks (2026)
- 链接：https://arxiv.org/abs/2602.05567
- 简介：消息自适应提示与 message passing 深度耦合。代表最新一批方法演进。

### 23) GP2F: Cross-Domain Graph Prompting with Adaptive Fusion of Pre-trained GNNs (2026)
- 链接：https://arxiv.org/abs/2602.11629
- 简介：跨域融合多个预训练 GNN 并用 prompt 适配。补第5章 domain transfer 机制。

### 24) Robust Graph Fine-Tuning with Adversarial Graph Prompting (2026)
- 链接：https://arxiv.org/abs/2601.00229
- 简介：在对抗场景下评估 prompt 微调鲁棒性。补第5章 robustness 维度。

### 25) When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph Prompt Learning (2026)
- 链接：https://arxiv.org/abs/2601.02662
- 简介：结合脉冲机制与稀疏提示，探索新型计算范式。可作为前沿探索方向。

### 26) Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs (2024)
- 链接：https://arxiv.org/abs/2407.15431
- 简介：文本属性图少样本分类中的预训练+提示框架。补第5章 text-attributed graph 过渡场景。

### 27) Prompt-Driven Continual Graph Learning (2025)
- 链接：https://arxiv.org/abs/2502.06327
- 简介：持续学习场景下的 prompt 机制。补第5章对增量任务的适配能力。

### 28) Event-Aware Prompt Learning for Dynamic Graphs (2025)
- 链接：https://arxiv.org/abs/2510.11339
- 简介：动态事件图中的事件感知提示设计。补第5章 dynamic answering 方向。

### 29) Learning and Editing Universal Graph Prompt Tuning via Reinforcement Learning (2025)
- 链接：https://arxiv.org/abs/2512.08763
- 简介：强调“可编辑”的通用 prompt，并用 RL 优化。补第5章 prompt lifecycle 视角。

### 30) Graph Your Own Prompt (2025)
- 链接：https://arxiv.org/abs/2509.23373
- 简介：提出自定义结构化 prompt 构造思路。可用于扩展第5章 graph-form prompt 讨论。

---

## 使用建议（给后续改稿）
- **正文优先引用**：Method 主干 + Benchmark + Theory（15篇内收敛）；
- **讨论区引用**：Survey + Application + 隐私/鲁棒/联邦类；
- **避免堆砌**：每个小节控制 3–5 篇代表作，保留“演进线”而非“列表线”。
# Section 5 候选文献池（2024–2026）

> 说明：面向 `tex/5.tex` 方法章节筛选。来源以 arXiv 检索为主，先保证覆盖，再在下一步收敛。  
> 字段：`title | year | venue | url | type | tag | reason`

## A. 主干方法候选（优先）

1. **ProG: A Graph Prompt Learning Benchmark** | 2024 | arXiv (NeurIPS'24 D&B 相关) | https://arxiv.org/abs/2406.05346 | Benchmark | Benchmark | 提供统一评测底座，补齐第5章可比性。
2. **Does Graph Prompt Work? A Data Operation Perspective with Theoretical Analysis** | 2024 | arXiv (ICML'25 相关) | https://arxiv.org/abs/2410.01635 | Theory | Theory | 稀缺理论解释，补“为何有效/何时失效”。
3. **A Unified Graph Selective Prompt Learning for Graph Neural Networks** | 2024 | arXiv | https://arxiv.org/abs/2406.10498 | Method | Token,Tuning | 选择性提示，补 token 设计新分支。
4. **Prompt Learning on Temporal Interaction Graphs** | 2024 | arXiv | https://arxiv.org/abs/2402.06326 | Method | Dynamic,Tuning | 补时序图场景。
5. **Prompt-Based Spatio-Temporal Graph Transfer Learning** | 2024 | arXiv | https://arxiv.org/abs/2405.12452 | Method | Dynamic,Transfer | 补跨域+时空迁移。
6. **SGPT: Few-Shot Prompt Tuning for Signed Graphs** | 2024 | arXiv | https://arxiv.org/abs/2412.12155 | Method | Token,Tuning | 补 signed graph 特殊结构任务。
7. **Instance-Aware Graph Prompt Learning** | 2024 | arXiv | https://arxiv.org/abs/2411.17676 | Method | Token,Insertion | 实例级提示，补个体化机制。
8. **Reliable and Compact Graph Fine-tuning via GraphSparse Prompting** | 2024 | arXiv | https://arxiv.org/abs/2410.21749 | Method | Tuning,Theory | 稀疏高效调参，补效率维度。
9. **Against Multifaceted Graph Heterogeneity via Asymmetric Federated Prompt Learning** | 2024 | arXiv | https://arxiv.org/abs/2411.02003 | Method | Transfer,Tuning | 补联邦+异构设置。
10. **RELIEF: Reinforcement Learning Empowered Graph Feature Prompt Tuning** | 2024 | arXiv | https://arxiv.org/abs/2408.03195 | Method | Tuning | 补 RL 优化提示策略。
11. **Inductive Graph Alignment Prompt: Bridging the Gap ... from Spectral Perspective** | 2024 | arXiv | https://arxiv.org/abs/2402.13556 | Method | Transfer,Theory | 光谱视角，连接 pre-train 与 inductive fine-tune。
12. **DAGPrompT: Distribution-aware Graph Prompt Tuning** | 2025 | arXiv | https://arxiv.org/abs/2501.15142 | Method | Tuning,Theory | 分布感知提示，补泛化稳定性。
13. **CLEAR: Cluster-based Prompt Learning on Heterogeneous Graphs** | 2025 | arXiv | https://arxiv.org/abs/2502.08918 | Method | Transfer,Token | 异构图聚类式提示。
14. **Edge Prompt Tuning for Graph Neural Networks** | 2025 | arXiv | https://arxiv.org/abs/2503.00750 | Method | Insertion,Tuning | 从节点扩展到边级提示。
15. **DP-GPL: Differentially Private Graph Prompt Learning** | 2025 | arXiv | https://arxiv.org/abs/2503.10544 | Method | Theory,Tuning | 补隐私约束下 prompt 学习。
16. **GraphPrompter: Multi-stage Adaptive Prompt Optimization for Graph In-Context Learning** | 2025 | arXiv | https://arxiv.org/abs/2505.02027 | Method | Answering,Tuning | ICL + 多阶段优化，补 answering 机制。
17. **One Prompt Fits All: Universal Graph Adaptation for Pretrained Models** | 2025 | arXiv | https://arxiv.org/abs/2509.22416 | Method | Transfer,Tuning | 统一适配，补跨任务迁移。
18. **GraphTOP: Graph Topology-Oriented Prompting for Graph Neural Networks** | 2025 | arXiv | https://arxiv.org/abs/2510.22451 | Method | Graph,Insertion | 拓扑导向提示，补结构视角。
19. **MAGPrompt: Message-Adaptive Graph Prompt Tuning for Graph Neural Networks** | 2026 | arXiv | https://arxiv.org/abs/2602.05567 | Method | Token,Tuning | 消息自适应，补 message passing 联动。
20. **GP2F: Cross-Domain Graph Prompting with Adaptive Fusion of Pre-trained GNNs** | 2026 | arXiv | https://arxiv.org/abs/2602.11629 | Method | Transfer,Tuning | 跨域融合 pre-trained GNNs。
21. **Robust Graph Fine-Tuning with Adversarial Graph Prompting** | 2026 | arXiv | https://arxiv.org/abs/2601.00229 | Method | Theory,Tuning | 对抗鲁棒性维度。
22. **When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph Prompt Learning** | 2026 | arXiv | https://arxiv.org/abs/2601.02662 | Method | Tuning,Theory | 稀疏+脉冲机制，探索新范式。

## B. 辅助与扩展候选（次优先）

23. **Graph Prompting for Graph Learning Models: Recent Advances and Future Directions** | 2025 | arXiv | https://arxiv.org/abs/2506.08326 | Survey | Benchmark,Theory | 可作为第5章 related discussion 参考。
24. **Towards Graph Prompt Learning: A Survey and Beyond** | 2024 | arXiv | https://arxiv.org/abs/2408.14520 | Survey | Benchmark | 补综述对照。
25. **Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs** | 2024 | arXiv | https://arxiv.org/abs/2407.15431 | Method | Token,Transfer | 补 text-attributed graph。
26. **GPT4Rec: Graph Prompt Tuning for Streaming Recommendation** | 2024 | arXiv | https://arxiv.org/abs/2406.08229 | Application | Transfer,Dynamic | 场景化示例，可在 discussion 简提。
27. **Prompt-Driven Continual Graph Learning** | 2025 | arXiv | https://arxiv.org/abs/2502.06327 | Method | Dynamic,Tuning | 补持续学习。
28. **Event-Aware Prompt Learning for Dynamic Graphs** | 2025 | arXiv | https://arxiv.org/abs/2510.11339 | Method | Dynamic,Answering | 动态事件图方向。
29. **Learning and Editing Universal Graph Prompt Tuning via Reinforcement Learning** | 2025 | arXiv | https://arxiv.org/abs/2512.08763 | Method | Tuning | prompt 编辑机制。
30. **Graph Your Own Prompt** | 2025 | arXiv | https://arxiv.org/abs/2509.23373 | Method | Graph,Insertion | 新型结构化 prompt 设计。

---

## 去重与保留说明

- 已去除明显非图提示主线（纯 CV/NLP prompt）条目；
- 保留少量“安全/鲁棒/隐私”条目用于第5章 `Further Discussion`；
- 下一阶段将从上述 30 篇收敛到 12–18 篇核心增量清单。
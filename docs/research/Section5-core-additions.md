# Section 5 核心增量清单（12–18篇）

> 目标：从候选池中选出可直接推动 `tex/5.tex` 改写的核心文献。  
> 口径：优先方法主干 + 理论 + 评测，避免堆砌。

## 核心 15 篇

1. **ProG: A Graph Prompt Learning Benchmark (2406.05346)**  
   - 纳入理由：统一评测基线，支撑第5章“方法比较”可信度。  
   - 拟插入：5.4 Further Discussion（评测标准）。

2. **Does Graph Prompt Work? (2410.01635)**  
   - 纳入理由：少有理论解释，补“有效性与失效边界”。  
   - 拟插入：5.4 Further Discussion（Theory）。

3. **A Unified Graph Selective Prompt Learning (2406.10498)**  
   - 纳入理由：Token 选择机制明显区别早期统一加法提示。  
   - 拟插入：5.1 Prompt Token/Structure。

4. **Instance-Aware Graph Prompt Learning (2411.17676)**  
   - 纳入理由：实例级提示，补个体化 prompt 设计路径。  
   - 拟插入：5.1 Prompt Token/Structure。

5. **Edge Prompt Tuning for GNNs (2503.00750)**  
   - 纳入理由：边级提示扩展“插入模式”定义边界。  
   - 拟插入：5.1 Inserting Pattern。

6. **DAGPrompT (2501.15142)**  
   - 纳入理由：分布感知提示，泛化导向明显。  
   - 拟插入：5.3 Prompt Tuning。

7. **CLEAR (2502.08918)**  
   - 纳入理由：异构图聚类式提示，补 hetero 分支。  
   - 拟插入：5.1 或 5.3（heterogeneous setting）。

8. **SGPT: Few-shot Prompt Tuning for Signed Graphs (2412.12155)**  
   - 纳入理由：signed graph 任务扩展，体现结构多样性。  
   - 拟插入：5.3 Prompt Tuning（task-specific）。

9. **Prompt Learning on Temporal Interaction Graphs (2402.06326)**  
   - 纳入理由：补动态图/时序图提示机制。  
   - 拟插入：5.3 Prompt Tuning（dynamic）。

10. **Prompt-Based Spatio-Temporal Graph Transfer Learning (2405.12452)**  
    - 纳入理由：时空迁移，补 transfer 维度。  
    - 拟插入：5.4 Further Discussion（Transferability）。

11. **Against Multifaceted Graph Heterogeneity via Asymmetric Federated Prompt Learning (2411.02003)**  
    - 纳入理由：联邦+异构联合设置，具现实价值。  
    - 拟插入：5.4（跨域/联邦可迁移）。

12. **Reliable and Compact Graph Fine-tuning via GraphSparse Prompting (2410.21749)**  
    - 纳入理由：参数效率与压缩，补工程可落地性。  
    - 拟插入：5.3（efficiency）。

13. **RELIEF: RL Empowered Graph Feature Prompt Tuning (2408.03195)**  
    - 纳入理由：优化策略层创新，连接 prompt 与策略学习。  
    - 拟插入：5.3（learning strategy）。

14. **MAGPrompt (2602.05567)**  
    - 纳入理由：最新（2026）消息自适应提示，体现前沿增量。  
    - 拟插入：5.1/5.3（message-adaptive prompt）。

15. **GP2F: Cross-Domain Graph Prompting with Adaptive Fusion (2602.11629)**  
    - 纳入理由：直接面向跨域适配，补第5章长期痛点。  
    - 拟插入：5.4（cross-domain adaptation）。

---

## 备选替换（如需收缩到12篇）
- GraphTOP (2510.22451)
- One Prompt Fits All (2509.22416)
- Robust Graph Fine-Tuning with Adversarial Graph Prompting (2601.00229)

---

## 改写落位建议（章节级）

- **5.1 新增小段**：`Recent token/edge/selective/topology-aware prompt designs (2024–2026)`  
- **5.3 新增小段**：`Efficient and robust prompt tuning (sparse/RL/federated/dynamic)`  
- **5.4 新增小段**：`Theory, benchmark, transferability, and reliability`

> 下一步可直接据此改 `tex/5.tex`，并补充 `zotero.bib` 引用键。
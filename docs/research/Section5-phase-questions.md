# Section 5 阶段性问题拆解（主代理执行版）

> 目标：仅围绕 `tex/5.tex`（Prompt Design for Graph Tasks）完成 2024–2026 文献增量准备。  
> 原则：先补证据，再改正文；先结构化问题，再逐阶段执行。

## Q1. 第5章当前已覆盖的方法谱系是什么？哪些由 2022–2023 文献主导？

### 已覆盖谱系（当前）
1. **Prompt as Tokens**：GPF/GPF-Plus/SGL-PT/HetGPT 等；
2. **Prompt as Graphs**：All in One/PRODIGY 等；
3. **Answering Function**：learnable head / hand-crafted template；
4. **Prompt Tuning**：meta-learning、task-specific、pretext-aligned；
5. **扩展方向（在第5章后半）**：多模态与跨域提示。

### 主导时段
- 关键方法几乎全部来自 **2022–2023**；
- 2024+ 在第5章中的系统增量不足，导致“方法演进链条”断档。

---

## Q2. 为覆盖 2024–2026，最小可行检索式集合是什么？每条检索式补什么缺口？

### 检索式 S1（主线方法）
```text
all:"graph prompt" AND ("graph neural network" OR GNN)
```
- 补缺口：新 Prompt 结构/插入模式/调参机制。

### 检索式 S2（理论与边界）
```text
"graph prompt" AND (theory OR "data operation" OR "negative transfer" OR robustness)
```
- 补缺口：为何有效、何时失效、稳定性边界。

### 检索式 S3（异构与跨域）
```text
("heterogeneous graph" OR "cross-domain" OR federated) AND (prompt OR prompting)
```
- 补缺口：跨域迁移、异构图、联邦设置。

### 检索式 S4（时序/动态图）
```text
("temporal graph" OR dynamic graph) AND (prompt learning OR prompt tuning)
```
- 补缺口：第5章缺少时序任务提示范式。

### 检索式 S5（基准与评测）
```text
"graph prompt" AND (benchmark OR evaluation)
```
- 补缺口：统一评测与方法可比性。

---

## Q3. 候选池如何去重、分级（A/B/C）并映射第5章框架？

### 去重规则
1. 按 arXiv id 去重；
2. 同标题多版本仅保留最新版本；
3. 同工作“预印本+已发表”仅保留一条主记录（附备注）。

### 分级规则
- **A 级（核心）**：方法创新明确 + 与第5章框架强相关 + 有较完整实验；
- **B 级（重要补充）**：场景创新或机制增量明显；
- **C 级（边缘观察）**：相关但偏应用或偏安全攻防，不作为主干。

### 映射标签
- `Token` / `Graph` / `Insertion` / `Answering` / `Tuning` / `Theory` / `Transfer` / `Dynamic` / `Benchmark`

---

## Q4. 哪些候选应进入“核心增量清单”（12–18篇）？理由是什么？

筛选原则：
1. 必须能落位到第5章某小节；
2. 优先 2024–2026；
3. 兼顾“方法-理论-评测-迁移”完整链条；
4. 仅保留可形成连续叙事的工作，不堆砌。

> 已在 `Section5-core-additions.md` 给出 15 篇核心增量与逐条理由。

---

## Q5. 下一步改写第5章，新增段落应插入哪些小节？

### 插入位点建议
1. **5.1 Prompt Token/Structure/Insertion**：补 2024–2026 新结构（选择性、边级、分布感知、拓扑导向）；
2. **5.2 Aligning Tasks by Answering Function**：补 CoT/ICL 风格图推理提示；
3. **5.3 Prompt Tuning**：补鲁棒/稀疏/联邦/动态场景调优；
4. **5.4 Further Discussion**：新增“安全风险、负迁移、可解释性与评测标准”小段。

### 对应输入
- 候选池：`Section5-candidate-pool-2024-2026.md`
- 核心清单：`Section5-core-additions.md`

---

## 当前阶段结论
- 第5章问题不是“缺文献”，而是“缺 2024–2026 的系统化编排”；
- 现已完成分阶段问题框架，后续可直接进入“按清单改 TeX 正文”。
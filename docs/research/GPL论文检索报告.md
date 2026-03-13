# 图神经网络提示学习（Graph Prompt）论文检索与核心种子文献分析报告

> 更新时间：2026-03-13  
> 范围：Graph Prompt / Prompt Tuning for GNN / Graph + LLM 交叉方向  
> 用途：后续综述写作、实验选题、基线搭建与文献追踪

---

## Executive Summary

本报告对 **Graph Prompt Learning** 方向进行了系统化梳理，重点完成了：

1. 候选文献池构建（2022–2026，含顶会与预印本）；
2. 核心种子论文筛选（8 篇，含方法、基准、理论三类）；
3. 可复现检索式设计（高精度、概念扩展、LLM交叉、预印本追踪）；
4. 后续扩展工作流（ResearchRabbit / Connected Papers / DBLP / OpenReview / arXiv）。

整体趋势显示：该领域正从早期“离散提示 + 任务对齐”，演进到“统一多任务提示框架”，并进一步与 **LLM 推理增强** 深度融合。

---

## 1. 候选论文列表（全局视野）

> 说明：以下为高价值候选集合（节选），覆盖高被引基础工作与前沿交叉方向。

| 标题 | 年份 | Venue/arXiv | 约引用 | 备注 |
|---|---:|---|---:|---|
| GPPT: Graph Pre-training and Prompt Tuning to Generalize GNNs | 2022 | KDD | ~310 | 早期奠基 |
| GraphPrompt: Unifying Pre-Training and Downstream Tasks for GNNs | 2023 | WWW | ~350 | 统一框架 |
| All in One: Multi-Task Prompting for GNNs | 2023 | KDD | ~329 | 多任务代表作 |
| Universal Prompt Tuning for GNNs | 2023 | NeurIPS | ~227 | 通用提示范式 |
| PRODIGY: Enabling In-context Learning Over Graphs | 2023 | NeurIPS | ~132 | 图 ICL 关键工作 |
| Graph Neural Prompting with Large Language Models | 2024 | AAAI | ~161 | 图 + LLM 交叉 |
| ProG: A Graph Prompt Learning Benchmark | 2024 | NeurIPS | ~48 | 统一评测基准 |
| Does Graph Prompt Work? (Data Operation + Theory) | 2025 | ICML | ~16 | 理论反思 |

补充候选（方向扩展）：One for All、HGPrompt、Generalized Graph Prompt、CLEAR、MultiGPrompt、GraphLLM 等。

---

## 2. 核心种子论文（8 篇）与入选理由

### 2.1 GPPT (KDD 2022)
- **定位**：图提示学习的早期奠基工作之一。  
- **核心思想**：将下游节点分类重构为与预训练更一致的链接预测形式。  
- **价值**：开启“提示作为任务对齐器”的主线。

### 2.2 GraphPrompt (WWW 2023)
- **定位**：统一不同粒度图任务的重要框架。  
- **核心思想**：将任务统一到子图相似度空间。  
- **价值**：降低任务迁移壁垒。

### 2.3 All in One (KDD 2023)
- **定位**：多任务提示学习代表作（KDD 最佳研究论文）。  
- **核心思想**：通过诱导图与图级提示 token 做统一建模。  
- **价值**：推动“一个模型覆盖多任务”的方向。

### 2.4 PRODIGY (NeurIPS 2023)
- **定位**：图领域 In-context Learning 里程碑。  
- **核心思想**：构造 PromptGraph，将示例与查询图联合推理。  
- **价值**：降低参数微调依赖，增强小样本适应。

### 2.5 Graph Neural Prompting with LLMs (AAAI 2024)
- **定位**：图与大语言模型融合代表作。  
- **核心思想**：把图结构信息压缩为可被 LLM 利用的软提示。  
- **价值**：缓解纯文本推理中的事实幻觉风险。

### 2.6 Universal Prompt Tuning (NeurIPS 2023)
- **定位**：通用/可插拔提示机制的重要工作。  
- **核心思想**：减少提示对特定预训练任务的强绑定。  
- **价值**：提升跨模型、跨预训练策略的泛化能力。

### 2.7 ProG Benchmark (NeurIPS 2024)
- **定位**：领域评测基础设施。  
- **核心思想**：统一数据、预处理、评估流程。  
- **价值**：提升横向对比与复现可靠性。

### 2.8 Does Graph Prompt Work? (ICML 2025)
- **定位**：理论剖析视角代表作。  
- **核心思想**：从数据操作/谱域角度解释提示机制生效条件。  
- **价值**：为负迁移诊断与稳健性改进提供理论抓手。

---

## 3. 检索策略与检索式（可复现）

### A. 高精度标题锚定（Exact Match）
```text
intitle:"graph prompt" OR intitle:"graph prompting"
```
- 用途：快速锁定“以图提示为主创新点”的文献。

### B. 概念扩展召回（Variant Recall）
```text
"graph prompt learning" OR "prompt tuning for graph" OR "prompting graph neural networks"
```
- 用途：覆盖术语变体，避免漏检。

### C. LLM 交叉定向检索
```text
("large language model" OR "LLM" OR "in-context learning")
AND ("graph neural network" OR "knowledge graph")
AND "prompt"
```
- 用途：捕获图-大模型融合方向。

### D. 预印本前沿追踪
```text
source:arxiv AND ("graph prompt" OR "graph prompting" OR "one-for-all graph")
```
- 用途：补齐顶会发表前的前沿进展。

---

## 4. 证据快照（种子论文）

- GPPT — KDD 2022，约 ~310 引用；
- GraphPrompt — WWW 2023，约 ~350 引用；
- All in One — KDD 2023，约 ~329 引用；
- PRODIGY — NeurIPS 2023，约 ~132 引用；
- GNP — AAAI 2024，约 ~161 引用；
- Universal Prompt Tuning — NeurIPS 2023，约 ~227 引用；
- ProG Benchmark — NeurIPS 2024，约 ~48 引用；
- Does Graph Prompt Work — ICML 2025，约 ~16 引用。

> 注：引用数为检索时点近似值，Google Scholar 与 DBLP/Semantic Scholar 口径不同。

---

## 5. 后续扩展工作流（建议执行）

### 5.1 ResearchRabbit
1. 用 8 篇种子文献建集合；
2. 跑 Earlier Work 回溯“图预训练 + 提示学习”源头；
3. 跑 Later Work 捕获 2025–2026 衍生方向；
4. 关注高产作者/实验室，做前沿预警。

### 5.2 Connected Papers
1. 以综述为中心生成图谱；
2. 优先关注边缘孤岛节点（潜在新方向）；
3. 提取 Prior / Derivative 列表做二轮筛选。

### 5.3 DBLP / OpenReview / arXiv
- DBLP：确认 venue 质量与正式收录；
- OpenReview：阅读 reviewer 争议点与 rebuttal；
- arXiv：跟踪未正式发表但高潜力工作。

---

## 6. 扩展关键词矩阵（用于系统综述）

- Pre-train, Prompt, and Predict + Graphs
- Graph-in-Context Learning
- Heterogeneous Graph Prompting
- Sub-graph Similarity Prompt
- Token-based vs Graph-based Prompts
- Graph Retrieval-Augmented Generation (Graph RAG)
- Parameter-Efficient Fine-Tuning + GNN
- Cross-domain Graph Transfer
- Federated Graph Prompt Learning
- Topology-aware Prompt
- Multi-task Graph Foundation Models
- Negative Transfer in Graph Prompt

---

## 7. 行动建议（可直接执行）

1. **先跑通 ProG 基线**：以统一框架快速建立实验对照。  
2. **优先做图 + LLM 融合方向**：围绕 ICL 与软提示构造新实验。  
3. **聚焦负迁移与理论边界**：在异构图/跨域设置中找稳定性突破点。

---

## 附：本次格式整理说明

- 已将原始长段落内容重排为 Markdown 结构化文档；
- 增加标题层级、分节、表格、列表、代码块；
- 保留原报告核心信息与结论，不改变研究主张。

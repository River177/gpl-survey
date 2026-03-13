# 第5章（Prompt Design for Graph Tasks）文献补全与升级计划（2026版）

> 项目：gpl-survey  
> 目标章节：`tex/5.tex`  
> 计划日期：2026-03-13

---

## 1. 目标与边界

**目标**：仅针对第5章，完成“已有文献盘点 + 缺失文献检索 + 章节升级改写计划”，并形成可执行路线，后续按计划逐步落地到 TeX 正文与参考文献。

**边界**：
- 本阶段先不直接大改正文内容；
- 先完成“盘点和检索计划”，并定义后续执行步骤与验收标准；
- 改动焦点仅限 `tex/5.tex`，必要时增补 `tex/zotero.bib`。

---

## 2. 第5章已收录文献盘点（基于 `tex/5.tex` 引用键）

共识别 **34** 个引用键，按主题分组如下。

### 2.1 Graph Prompt 主线方法（核心）
- `sun2022gppt` — GPPT
- `liu2023graphprompt` — GraphPrompt
- `sun2023all` — All in One
- `fang2022prompt` — Prompt tuning for GNNs (GPF)
- `fang2023universal` — Universal Prompt Tuning
- `zhu2023sglpt` — SGL-PT
- `chen2023ultradp` — ULTRA-DP
- `ma2023hetgpt` — HetGPT
- `gong2023prompt` — Prompt Tuning for Multi-View Graph Contrastive Learning
- `tan2023virtual` — Virtual Node Tuning
- `ge2023enhancing` — Structure-Based Prompt
- `huang2023prodigy` — PRODIGY (In-context Learning over Graphs)

### 2.2 预训练/优化相关支撑
- `you2020graph` — GraphCL
- `finn2017modelagnostic` — MAML

### 2.3 多模态与 LLM 交叉
- `li2023survey` — Graph + LLM Survey
- `liu2023graph` — Graph Foundation Models Survey
- `wen2023augmenting` — G2P2
- `zhao2023gimlet` — GIMLET
- `li2023promptbased` — Prompt-Based Zero/Few-shot Node Classification
- `chen2023exploring` — Exploring LLMs on Graphs
- `fatemi2023talk` — Talk like a graph
- `jin2023patton` — PATTON
- `wang2023knowledge` — KGP for MD-QA
- `edwards2023synergpt` — SynerGPT
- `li2023graphadapter` — GraphAdapter
- `liu2023gitmol` — GIT-Mol

### 2.4 跨域/迁移/OOD
- `zhu2023graphcontrol` — GraphControl
- `zhang2023structure` — KG transfer with prompt tuning
- `yi2023contrastive` — Cross-domain Recommendation + Prompt
- `liu2023one` — One for All
- `cao2023when` — Pre-train feasibility
- `zhao2023graphglow` — GraphGLOW
- `guo2023datacentric` — OOD with data-centric framework

---

## 3. 缺失风险（第5章当前版本）

第5章当前文献主体集中在 **2022–2023**，对 **2024–2026** 增量覆盖不足，主要缺口：

1. **基准与标准化缺口**：缺少 2024 后统一 benchmark 与复现实证文献。  
2. **理论解释缺口**：缺少 2025 后关于“为什么 graph prompt 有效/何时失效”的理论文献。  
3. **新范式缺口**：缺少 Prompt + LLM 深融合（GraphRAG/Agent/推理增强）的系统纳入。  
4. **异构与拓扑提示缺口**：缺少 hetero/topology-aware 新方法链路。  
5. **负迁移与跨域鲁棒性缺口**：缺少针对失败边界与迁移稳定性的最新结果。

---

## 4. 缺失文献检索方案（执行设计）

### 4.1 数据源
- Google Scholar（高召回）
- arXiv（前沿）
- DBLP（venue核验）
- OpenReview（审稿争议与限制）

### 4.2 检索式（第5章定向）

**A. Prompt 主线补全（2024+）**
```text
("graph prompt" OR "graph prompting" OR "prompt tuning for graph")
AND (GNN OR "graph neural network")
AND (2024 OR 2025 OR 2026)
```

**B. 理论与边界**
```text
("graph prompt" AND (theory OR theoretical OR "negative transfer" OR generalization))
```

**C. 异构/拓扑方向**
```text
("heterogeneous graph" OR "topology-aware") AND (prompt OR prompting)
```

**D. LLM 融合（仅与第5章方法框架相关）**
```text
("graph" AND (LLM OR "large language model" OR "in-context" OR RAG) AND prompt)
```

### 4.3 纳入标准（筛选）
- 时间：优先 2024–2026；
- 质量：顶会/顶刊优先（NeurIPS/ICML/ICLR/KDD/WWW/AAAI/TKDE 等）；
- 相关性：必须能映射到第5章的方法框架（Prompt token / structure / insertion / answering / tuning）；
- 可用性：优先含代码/实验设置清晰的文献。

### 4.4 排除标准
- 仅“prompt engineering for text”且无图方法实质；
- 仅应用报告、无方法细节/无实证；
- 与第5章范式不相关（无法映射到统一框架）。

---

## 5. 执行步骤（后续按此执行）

### Step 1：建立候选池（目标 25–40 篇）
- 输出：`docs/research/Section5-candidate-pool-2024-2026.md`
- 字段：标题、年份、venue、任务、方法类型、代码、与第5章映射标签。

### Step 2：二次筛选（收敛到 12–18 篇核心增量）
- 输出：`docs/research/Section5-core-additions.md`
- 标签：
  - Prompt as Tokens
  - Prompt as Graphs
  - Answering Function
  - Prompt Tuning
  - Theory/Transfer/Robustness

### Step 3：形成第5章增量改写蓝图
- 输出：`docs/research/Section5-rewrite-outline.md`
- 内容：逐小节“新增段落点 + 引用位点 + 替换建议句”。

### Step 4：落地 TeX 修改（执行阶段）
- 修改：`tex/5.tex`、必要时 `tex/zotero.bib`
- 输出：
  - 新增 2024–2026 文献段落
  - 更新对比表（若需要，迁移或扩展 `table/graph_prompt_summary.tex`）

### Step 5：质量校验
- 引用键完整性检查；
- 文献与论述一一对应检查；
- 章节逻辑一致性检查（Q1-Q4 不断裂）。

---

## 6. 交付物与验收标准

### 6.1 交付物
1. 候选池清单（含筛选理由）
2. 核心增量文献清单（12–18篇）
3. 第5章改写提纲
4. 第5章 TeX 实际改稿（下一阶段）

### 6.2 验收标准
- 第5章新增文献中，**2024–2026 占比 >= 60%**；
- 每个新增文献都能映射到第5章统一框架某一环节；
- 至少新增 1 组“理论/负迁移/边界”讨论；
- 文献引用可编译且无悬空键。

---

## 7. 风险与对策

- **风险1：新文献数量多但质量参差**  
  对策：先 DBLP/venue 核验，再纳入正文。

- **风险2：第5章篇幅膨胀**  
  对策：正文保留核心链路，扩展材料放 `docs/research` 附录文件。

- **风险3：与第6/8章边界重叠**  
  对策：第5章只保留“方法框架与机制”，应用与趋势放第6/8章。

---

## 8. 后续执行顺序（固定）

1) 先出候选池  
2) 再出核心增量清单  
3) 再出第5章改写提纲  
4) 最后改 `tex/5.tex`

> 本计划文件已作为后续执行基线，后续所有动作按本计划推进并逐项勾选。
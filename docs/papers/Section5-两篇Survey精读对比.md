# Section 5 两篇 Survey 精读对比（已下载）

> 精读对象：
> 1) **Towards Graph Prompt Learning: A Survey and Beyond** (arXiv:2408.14520v2, 2024)  
> 2) **Graph Prompting for Graph Learning Models: Recent Advances and Future Directions** (arXiv:2506.08326v1, 2025, KDD'25 Tutorial/Survey Track)

> 下载位置：`papers/surveys/`

---

## 0. 文献状态与可用性说明

- `2408.14520` 在 arXiv 页面显示 **v3 withdrawn**（无可用 PDF）。本次采用 **v2 PDF（20页）**进行精读，保证信息完整。  
- `2506.08326` 为可用版本（11页），可正常精读。

---

## 1. Survey A（2408.14520v2）精读要点

### 1.1 核心定位
- 主打“大而全”的图提示学习综述，强调与 AGI 背景的连接；
- 明确覆盖 100+ 相关工作，并给出较完整 taxonomy。

### 1.2 方法框架（对第5章最相关）
- 强调 **Prompting Tokenization**、**Alignment Strategy**、**Prompt Tuning** 的统一叙述；
- 在 homogeneous / heterogeneous 两类图上分别展开；
- 讨论了输入图提示、输出表示提示等多种策略。

### 1.3 优点
- 方法与应用覆盖面广；
- 对数据集与评测维度（Acc/F1/AUC、参数量、FLOPs、迁移性）有明确整理；
- 可作为第5章“历史全景”补充来源。

### 1.4 局限
- 版本状态不稳定（最新版撤回）；
- 结构偏“汇总式”，部分方法对比深度不够；
- 对 2025–2026 的最新演化覆盖不足（时间上天然限制）。

---

## 2. Survey B（2506.08326v1）精读要点

### 2.1 核心定位
- 明确围绕“**pre-training, prompting**”两阶段框架；
- 作为 2025 年 Survey/Tutorial Track 工作，分类更贴近方法实现。

### 2.2 方法框架（对第5章最相关）
- 将 graph prompting 分为：
  1) **Data-level prompting**（feature-based / insertion-based）
  2) **Representation-level prompting**（output / hidden）
  3) **Task-level prompting**（link-prediction based / similarity-based）
- 对方法进行了更工程化的比较维度：
  - Single Forward Pass
  - 下游任务普适性（DT universality）

### 2.3 优点
- 分类清晰、落地性强，适合作为第5章主框架增强；
- 明确指出 task-level prompting 目前对任务类型的局限；
- 在挑战与未来方向中更强调“通用兼容性”“跨模型适配”。

### 2.4 局限
- 篇幅较短，理论深度相对有限；
- 对安全/鲁棒/隐私类新问题展开不足；
- 对 2026 新方法的吸收仍需我们二次补齐。

---

## 3. 与当前稿件（`tex/5.tex`）逐点对比

### 3.1 一致点（可保留）
- 当前稿件已有 Prompt Token / Structure / Inserting Pattern 三元框架；
- 已覆盖 learnable vs hand-crafted answering；
- 已讨论 meta-learning、task-specific、pretext-aligned 三类 tuning。

### 3.2 差异点（必须补）
1. **分类口径差异**：当前第5章偏“机制叙述”，缺少 B 文献那种 data/representation/task-level 明确映射。  
2. **评测维度不足**：当前稿件对“单次前向、任务普适性、参数效率”不够结构化。  
3. **新问题不足**：安全/鲁棒/隐私/联邦/动态图等 2024+ 维度尚未系统并入。  
4. **文献时效性不足**：当前主干方法仍偏 2022–2023。

---

## 4. 可吸收到第5章的具体改写点（按小节）

### 4.1 插入到 5.1（Prompt Token, Structure, Insertion）
- 新增“与 Survey B 对齐”的小段：Data-level / Representation-level / Task-level 三分法；
- 将现有方法映射到这三类，减少概念重复。

### 4.2 插入到 5.2（Aligning Tasks by Answering Function）
- 补充 task-level prompting 的边界：为何目前更偏分类任务；
- 增加 similarity-based 与 link-based 的适用条件对比。

### 4.3 插入到 5.3（Prompt Tuning）
- 增加效率维度（single forward / 参数量 / FLOPs）描述模板；
- 增加 2024–2026 新方法在 dynamic/federated/privacy 下的 tuning 线索。

### 4.4 插入到 5.4（Further Discussion）
- 增加“通用兼容性”讨论（跨图结构、跨骨干模型、跨任务）；
- 增加“理论解释+鲁棒性风险”小节（与 `Does Graph Prompt Work?` 等衔接）。

---

## 5. 对第5章改写的结论建议

1. **框架层**：保留你当前三元框架（token/structure/insertion），并新增“data/representation/task-level”映射表。  
2. **证据层**：把 Survey A 当“全景背景”，Survey B 当“方法骨架”。  
3. **时效层**：用已整理的 2024–2026 核心15篇补齐新分支。  
4. **写作层**：正文讲主线，扩展材料放 `docs/papers`，避免第5章膨胀。

---

## 6. 本次新增文件清单（可追踪）

- `papers/surveys/2408.14520v2-Towards-Graph-Prompt-Learning-A-Survey-and-Beyond.pdf`
- `papers/surveys/2506.08326v1-Graph-Prompting-for-Graph-Learning-Models-Recent-Advances-and-Future-Directions.pdf`
- `docs/papers/Section5-两篇Survey精读对比.md`

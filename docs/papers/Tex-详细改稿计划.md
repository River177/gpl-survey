# `tex/` 详细改稿计划

> 目标：将当前 2023 口径的 graph prompt survey，系统升级为覆盖 2024-2026 新进展的新版稿件。  
> 范围：`tex/` 主体章节、配套图表、summary table、bib。  
> 配套文档：
> - [Section5-修改建议.md](/mnt/d/Graph/gpl-survey/docs/papers/Section5-修改建议.md)
> - [Tex-全局修改建议.md](/mnt/d/Graph/gpl-survey/docs/papers/Tex-全局修改建议.md)

---

## 1. 改稿目标

这次改稿不是“补几篇文献”，而是完成 4 个具体目标：

1. 把 survey 的时间口径从 2023 推进到 2025-2026。
2. 把第 5 章从“早期 graph prompt 方法综述”升级成“覆盖 benchmark、theory、复杂图场景的新体系”。
3. 让引言、taxonomy、应用、讨论、结论与新版第 5 章保持一致。
4. 让图表、summary table、bib 与正文同步，不出现“正文更新了但图表还是旧版”的问题。

---

## 2. 总体策略

建议采用“两轮式改稿”：

### 第一轮：结构校正

先解决“框架是否正确”，不追求语言润色到位。

这一轮重点是：

- 新 taxonomy 定稿
- 第 5 章重组
- 引言/方法学/讨论章节与第 5 章对齐
- 应用章节重写成更贴近候选文献的版本

### 第二轮：证据补全与统一表达

在框架稳定后，再处理：

- 图表重做
- summary table 更新
- bibliography 补全
- 全文措辞统一
- 交叉引用、caption、摘要、结论收口

不建议一开始就同时改正文、重画图、补 bib，因为 taxonomy 一旦变，前面的工作会返工。

---

## 3. 阶段划分

## 阶段 0：改稿前整理

### 目标

确认本次改稿的“主线文献池”和“正文优先引用池”，避免后面引用失控。

### 要做的事

1. 从 `docs/papers/Section5-候选文献-按类型简介.md` 中选出两组文献：
   - 主线文献：12-15 篇，进入正文主叙述
   - 扩展文献：10-15 篇，进入 discussion / applications / future directions

2. 为这些文献建立一个简单映射表：
   - 文献标题
   - 所属章节
   - 用途
   - 是否已发表
   - 是否必须进 bib

3. 确定一条写作原则：
   - 正文主线优先引用已发表或已接收文献
   - 2026 arXiv 文献更多用于“最新趋势”和“未来方向”

### 产出

- 一份“正文优先文献清单”

### 验收标准

- 任何一个章节都知道自己优先引用哪些文献
- 不会出现同一小节塞 8-10 篇边缘论文的情况

---

## 阶段 1：先定新版 taxonomy 和章节结构

### 目标

在动正文之前，先定全书的分类框架。

### 为什么优先做

如果 taxonomy 不先定：

- `1.intro.tex` 无法改准
- `2.methodology.tex` 无法改准
- `5.tex` 会改一遍又返工
- `table/graph_prompt_summary.tex` 和 `pic/taxonomy.tex` 都没法做

### 要改的文件

- `tex/2.methodology.tex`
- `tex/pic/taxonomy.tex`

### 要做的事

1. 把 taxonomy 从旧版结构：
   - pre-training strategies
   - prompt design
   - multi-modal prompting
   - domain adaptation

   改为新版双轴框架：

   - 轴 1：prompt 注入空间
     - feature/token
     - edge/topology
     - message/readout
     - prompt graph/structured

   - 轴 2：适配场景
     - homogeneous static
     - hetero
     - signed
     - text-attributed
     - temporal/dynamic
     - continual/streaming
     - federated
     - cross-domain
     - robust/adversarial

2. 改写 `Survey Methodology` 里对 taxonomy 的解释。

3. 调整 `Research Objectives` 和各章节映射的说明：
   - 保留 AGI 视角
   - 但将真正的技术主线切回 “graph prompt for pretrained graph model adaptation”

4. 确定新版第 5 章的内部结构标题。

### 产出

- 新版 taxonomy 文本
- 新版 taxonomy 图草稿
- 新版第 5 章结构骨架

### 验收标准

- taxonomy 能自然容纳 EdgePrompt、GraphTOP、MAGPrompt、TIGPrompt、PROMPTCGL、FedGPL、GP2F 这些文献
- 不再依赖旧的 “prompt as tokens / prompt as graphs + answering function” 作为唯一核心组织方式

---

## 阶段 2：重写第 5 章主体

### 目标

把第 5 章改成全书新的技术核心。

### 要改的文件

- `tex/5.tex`
- `tex/table/graph_prompt_summary.tex`
- 可能还包括 `tex/pic/prompt.pdf`

### 要做的事

#### 2.1 改开头总述

- 更新“recent works”的时间口径
- 在开头加入 benchmark、theory、survey update
- 说明 prompt 的版图已扩展到 edge/topology/message/dynamic/cross-domain 等

#### 2.2 重写 prompt design 小节

按新版结构拆成：

1. Feature / token-level prompt
2. Edge / topology-level prompt
3. Hidden-state / message-passing prompt
4. Structured prompt / prompt graph

并将特殊图类型嵌入其中：

- hetero
- signed
- temporal
- spatio-temporal
- dynamic event

#### 2.3 重写 task alignment 小节

将标题从 `Aligning Tasks by Answering Function` 改为更中性的：

- `Task Alignment Mechanisms`
  或
- `Aligning Downstream Tasks with Pre-training Objectives`

内容改成：

1. task-template alignment
2. distribution / domain alignment
3. temporal / dynamic alignment
4. in-context / continual alignment

#### 2.4 重写 prompt tuning 小节

改成：

1. general/meta initialization
2. selective or sparse optimization
3. instance-adaptive/generated prompt
4. RL-based optimization
5. robust/constrained prompt learning

#### 2.5 重写 discussion 小节

按维度讨论：

1. expressiveness vs efficiency
2. universal vs selective prompt
3. in-domain vs cross-domain transfer
4. static vs dynamic/continual setting

并引入：

- ProG 作为 benchmark 支撑
- Does Graph Prompt Work? 作为 theory 支撑

#### 2.6 重做 summary table

建议保留 12-15 篇主线代表作，不要覆盖所有文献。

表头建议至少包括：

- pretraining relation
- prompt injection space
- optimization type
- target setting
- downstream scope
- answering head requirement
- publication status

### 推荐进入第 5 章主线的核心文献

- ProG
- Does Graph Prompt Work?
- EdgePrompt
- GraphTOP
- MAGPrompt
- Instance-Aware Graph Prompt Learning
- RELIEF
- IGAP
- DAGPrompT
- GraphPrompter
- One Prompt Fits All
- TIGPrompt
- PROMPTCGL
- P2TAG
- FedGPL 或 GP2F

### 产出

- 新版 `5.tex`
- 新版 `graph_prompt_summary.tex`

### 验收标准

- 第 5 章不再只像 2023 年综述的延长版
- 2024-2026 的关键方向都有落点
- 小节标题和 taxonomy 一致

---

## 阶段 3：回改前文，让引言与方法学对齐新版第 5 章

### 目标

避免出现“第 5 章已经是新版，前面还在讲 2023 年起步期”的断裂。

### 要改的文件

- `tex/0.main.tex`
- `tex/1.intro.tex`
- `tex/2.methodology.tex`
- `tex/3.Preliminaries.tex`
- `tex/4.Pre-training.tex`

### 要做的事

#### 3.1 改 abstract

- 删除或弱化：
  - pioneering
  - first
  - nascent
- 加入：
  - benchmark
  - theory
  - complex settings

#### 3.2 改 introduction

- 压缩 AGI 宏观背景
- 更快进入 graph prompt 的核心问题：
  - pretrain-downstream gap
  - parameter-efficient adaptation
  - graph-specific prompt complexity
  - dynamic / cross-domain / federated / continual settings

- 更新关于“缺少 benchmark / theory”的表述
- 更新 RQ 的解释，使其能覆盖新版第 5 章

#### 3.3 改 methodology

- 用新版 taxonomy 重写
- 更新 literature overview 的文字
- 更新 “connection to existing work”

#### 3.4 改 preliminaries

- 在 `Why Prompt?` 中加入理论工作呼应
- 降低一些绝对化判断
- 衔接“prompt 不再只是输入层 feature manipulation”

#### 3.5 改 pre-training chapter

- 保留 node/edge/graph/multi-task 四分法
- 但在每类后说明与 prompt 设计的关系
- 结尾明确：prompt 已开始走向 pretraining-agnostic / universal adaptation

### 产出

- 新版 abstract
- 新版引言
- 对齐后的 methodology / preliminaries / pre-training

### 验收标准

- 第 1-4 章与第 5 章在术语和叙述上不冲突
- 前文不会再把 graph prompt 描述成只有少量工作的新兴现象

---

## 阶段 4：重写“应用 / 复杂场景 / 部署”相关章节

### 目标

把后半部分从“泛化展望”改成“有文献支撑的复杂场景总结”。

### 要改的文件

- `tex/6.Applications.tex`
- `tex/7.ProG.tex`

### 要做的事

#### 4.1 重写 applications

建议把标题从 `Potential Applications` 调整为：

- `Applications and Advanced Settings`
  或
- `Graph Prompting in Realistic Graph Scenarios`

内容改成 4 块：

1. recommendation and streaming
   - GPT4Rec

2. text-attributed graph
   - P2TAG

3. temporal / dynamic / continual
   - TIGPrompt
   - STGP
   - PROMPTCGL
   - EVP

4. cross-domain / federated / robust deployment
   - FedGPL
   - GP2F
   - DAGPrompT
   - AGP

#### 4.2 升级 ProG 章节

把 `ProG` 从“工具介绍”升级为：

- benchmark + ecosystem

需要写清楚：

1. ProG 解决了什么 benchmark 缺口
2. 它如何统一不同 prompt 方法的评测
3. 它为什么对 survey 讨论很重要
4. library 和 awesome list 各自承担什么角色

### 产出

- 重写后的 applications 章节
- 升级后的 ProG 章节

### 验收标准

- 第 6 章不再是泛泛而谈的潜在应用
- 第 7 章不再只是附属性工具介绍

---

## 阶段 5：重写 challenges 和 future directions

### 目标

把第 8 章从 2023 年愿景型总结，升级成能承接新版正文的研究议程。

### 要改的文件

- `tex/8.Discussion.tex`
- `tex/9.Conclusion.tex`

### 要做的事

#### 5.1 重写 current challenges

建议改成 5 类：

1. benchmark consistency and fair evaluation
2. theory and mechanism understanding
3. transferability across domains and settings
4. prompting under dynamic / continual / federated settings
5. robustness, reliability, and interpretability

#### 5.2 重写 future directions

建议改成：

1. unified theory for graph prompting
2. prompting for large graph models / foundation graph models
3. prompting in dynamic and lifelong graph learning
4. trustworthy and robust graph prompting
5. standardized benchmark and deployment ecosystem

#### 5.3 扩写 conclusion

结论至少补三层信息：

1. 方法版图已经扩大
2. benchmark 和 theory 开始成熟
3. 真正重要的问题转向复杂场景部署

### 产出

- 新版 discussion
- 新版 conclusion

### 验收标准

- 第 8 章的挑战和未来方向能对应正文已经讨论过的问题
- 第 9 章不只是重复 abstract 和 AGI 愿景

---

## 阶段 6：统一图表、表格、统计图和 bibliography

### 目标

完成“证据层”和“展示层”的同步更新。

### 要改的文件

- `tex/pic/taxonomy.tex`
- `tex/table/graph_prompt_summary.tex`
- `tex/pic/prompt.pdf`
- `tex/pic/reference_venue.pdf`
- `tex/pic/top_keywords_bar.png`
- `tex/zotero.bib`

### 要做的事

#### 6.1 更新 bibliography

顺序建议：

1. 先补正文主线必引 12-15 篇
2. 再补 discussion / applications 扩展文献
3. 最后检查 citation key 风格统一

#### 6.2 重做 statistics figures

如果 literature overview 语料更新：

- 重新统计 venue distribution
- 重新统计 title keywords

否则正文会和图不一致。

#### 6.3 重画 prompt / taxonomy 图

- prompt 总图应从单纯 token/structure/inserting pattern 扩展到更高层 taxonomy
- taxonomy 图应体现新版两轴逻辑

### 产出

- 完整 bib
- 新版 taxonomy 图
- 新版 summary table
- 新版统计图

### 验收标准

- 所有正文引用都能解析
- 图表内容与正文完全一致
- 没有“正文说 2025 新方向，图上还是 2023 方法”的情况

---

## 阶段 7：全文统一与质量检查

### 目标

收尾，防止局部改好了但全书风格和引用关系仍混乱。

### 要做的事

1. 统一术语：
   - graph prompt / graph prompting / graph prompt learning
   - prompt tuning / prompt learning / prompt-based adaptation
   - dynamic / temporal / continual / streaming
   - transfer / cross-domain / domain adaptation

2. 统一语气：
   - 删除明显过时的“nascent / only a few works / first”
   - 降低没有证据支撑的绝对判断

3. 检查交叉引用：
   - section labels
   - figure refs
   - table refs
   - bibliography refs

4. 检查章节间的一致性：
   - taxonomy 与正文
   - applications 与 discussion
   - ProG 与 benchmark 讨论
   - abstract / intro / conclusion 的总述一致

5. 编译检查：
   - bib 是否报错
   - figure/table 是否溢出
   - 行文是否明显过长或失衡

### 产出

- 一版可编译、结构统一的新稿

### 验收标准

- 无未定义引用
- 无明显重复叙述
- 全书的“新版定位”一致

---

## 4. 各阶段依赖关系

建议严格按下面依赖推进：

1. 阶段 0
2. 阶段 1
3. 阶段 2
4. 阶段 3
5. 阶段 4
6. 阶段 5
7. 阶段 6
8. 阶段 7

关键依赖：

- 第 1 阶段没定稿前，不要动图表和 summary table。
- 第 2 阶段没定稿前，不要大规模补 bib。
- 第 5 阶段应在第 2-4 阶段之后做，否则 challenge/future direction 写不准。

---

## 5. 建议的执行优先级

如果你想把工作拆成几个较稳的小任务，建议按下面的优先级分批完成：

### 第一优先级

- `tex/5.tex`
- `tex/2.methodology.tex`
- `tex/1.intro.tex`

这是决定全书方向的核心。

### 第二优先级

- `tex/6.Applications.tex`
- `tex/7.ProG.tex`
- `tex/8.Discussion.tex`

这是把新版主线落到后半部分。

### 第三优先级

- `tex/0.main.tex`
- `tex/3.Preliminaries.tex`
- `tex/4.Pre-training.tex`
- `tex/9.Conclusion.tex`

这是做口径统一和收尾。

### 第四优先级

- `tex/pic/taxonomy.tex`
- `tex/table/graph_prompt_summary.tex`
- `tex/zotero.bib`
- 统计图

这是做展示层与证据层同步。

---

## 6. 建议的工作量划分

如果按“实际可执行任务”来切，可以切成 6 个任务包：

### 任务包 A：结构定稿

- 新 taxonomy
- 新第 5 章目录
- 新 applications 目录

### 任务包 B：技术主章改写

- `5.tex`
- `graph_prompt_summary.tex`

### 任务包 C：前文对齐

- `0.main.tex`
- `1.intro.tex`
- `2.methodology.tex`
- `3.Preliminaries.tex`
- `4.Pre-training.tex`

### 任务包 D：后文对齐

- `6.Applications.tex`
- `7.ProG.tex`
- `8.Discussion.tex`
- `9.Conclusion.tex`

### 任务包 E：图表和 bib

- taxonomy figure
- summary table
- bibliography
- statistics figures

### 任务包 F：全书统一与编译检查

- terminology
- refs
- format
- compile

---

## 7. 风险点与规避方式

### 风险 1：第 5 章写得太满，其他章节跟不上

规避方式：

- 第 5 章先定“主线文献”而不是贪多
- 复杂场景文献分流到第 6 章和第 8 章

### 风险 2：taxonomy 改了，后面所有图表都要返工

规避方式：

- taxonomy 先定稿
- 图表最后做

### 风险 3：bib 一次性补太多，引用混乱

规避方式：

- 先补主线文献
- 再补扩展文献

### 风险 4：仍然保留太多 2023 年措辞

规避方式：

- 最后一轮统一扫：
  - recently
  - emerging
  - nascent
  - first
  - only a few

---

## 8. 最终交付标准

改稿完成后，至少应满足下面 8 条：

1. 第 5 章已系统纳入 2024-2026 主线文献。
2. 引言不再把 graph prompt 写成只有少量工作的起步方向。
3. methodology 的 taxonomy 能覆盖新版正文。
4. applications 能反映真实复杂场景，而不是泛泛展望。
5. ProG 被写成 benchmark + ecosystem，而不只是工具。
6. discussion 能反映 benchmark、theory、dynamic、transfer、robustness 等问题。
7. summary table、taxonomy 图、statistics 图与正文一致。
8. bib 完整，全文可编译，无未定义引用。

---

## 9. 一句话执行建议

最稳妥的执行方式是：

**先定 taxonomy，再重写第 5 章，再回改前后文，最后统一图表和 bib。**

如果跳过这个顺序，后面大概率会重复返工。

# 图提示综述修订计划

> **面向代理式执行者：** 必须使用子技能 `superpowers:subagent-driven-development`（推荐）或 `superpowers:executing-plans`，按任务逐项执行本计划。步骤使用复选框语法（`- [ ]`）进行跟踪。

**目标：** 在尽量少改动整体结构的前提下，将 2023 年版图提示综述草稿刷新为适用于 2026 年投稿的版本；保留主 taxonomy，并将不适合纳入 taxonomy 的近年方法转移到 Applications 章节。

**整体方案：** 保持章节顺序和 taxonomy 主干不变，先更新论述口径与文献覆盖，再通过主 taxonomy 章节中的既有小节吸收 2024-2026 年工作。任何不适配当前 taxonomy 的近年工作，都应记录在 Applications 或 Discussion 中，而不是强行重构 taxonomy。

**技术栈：** LaTeX、BibTeX、Markdown 计划文档、`docs/` 下的本地论文筛选记录

---

## 约束与范围

- 保持 `tex/0.main.tex` 中的顶层章节结构不变。
- 保持 `tex/pic/taxonomy.tex` 中的 taxonomy 树不变，除非事实错误迫使我们做最小修补。
- 优先进行文字层面的更新，而不是结构性重写。
- 将本轮刷新目标时间窗设为 `2024-01-01` 到 `2026-03-22`。
- 不适合既有 taxonomy 的方法放入 `tex/6.Applications.tex`；如果需要趋势层面的总结，则写入 `tex/8.Discussion.tex`。

## 全局成功标准

- 稿件中不再包含过时的投稿说明、陈旧的新颖性表述或不一致的年份范围。
- 新近论文的加入是系统化完成的，而非零散补丁式添加。
- taxonomy 章节仍然是整篇综述的核心。
- 溢出方法会被明确放入 Applications，而不是被默默遗漏。
- ProG 会被准确表述为已发表的 benchmark/toolkit 论文，而非未发表的附属产物。
- 对于过旧的方法，会在其不再服务于更新后叙事时进行有选择的压缩或替换。
- 全文可以在参考文献和交叉引用都正确解析的情况下顺利编译。

## 主要工作流

### 工作流 1：刷新 ProG 的定位表述

- 更新所有与 ProG 相关的措辞，使其被一致表述为已发表的 benchmark/toolkit 论文，而不只是内部库或附属产物。
- 检查摘要、引言、方法学、Applications，以及 `tex/7.ProG.tex` 中的术语、论断与引用是否一致。

### 工作流 2：用更具代表性的工作刷新核心综述

- 在保持现有 taxonomy 结构不变的前提下，用 2024-2026 年的代表性工作更新以 taxonomy 为中心的综述内容。
- 对过旧的方法进行压缩、降级或替换，但保留必要的历史脉络。

### 工作流 3：可选的生态扩展

- 可选地将近期论文同步到 `Awesome-Graph-Prompt`。
- 可选地将新收集到的代码库、benchmark 或 wrapper 更新到 ProG 中，以覆盖近期代表性方法。
- 可选地评估是否应将 `ProG-V2` 作为一个单独界定范围的后续项目来规划。

## 当前执行状态

- **已正式完成的检查点：** `CP0`
- **当前实际进度：** 仅发现 `tex/0.main.tex`、`tex/1.intro.tex`、`tex/2.methodology.tex` 有本轮文稿改写痕迹。
- **已完成的文稿改写范围：**
  - `tex/0.main.tex`：摘要与前言入口已更新，旧的投稿/拒稿说明已去除。
  - `tex/1.intro.tex`：引言整体口径已按 2026 年综述语境重写。
  - `tex/2.methodology.tex`：方法学与 `Connection to Existing Work` 已更新。
- **尚未完成的正文范围：**
  - `tex/5.tex`：仍为旧版 taxonomy 主体内容，未见本轮代表性方法刷新。
  - `tex/6.Applications.tex`：仍为旧版应用章节，未见 overflow 承接更新。
  - `tex/7.ProG.tex`：仍将 ProG 主要表述为统一库，尚未刷新为已发表 benchmark/toolkit 论文定位。
  - `tex/8.Discussion.tex`：仍为旧版挑战与展望内容，未见近年趋势补充。
- **本次进度回填原则：**
  - 仅按 `tex/` 目录中的直接文稿证据标记完成状态。
  - 即使 `docs/` 中已有辅助笔记或计划材料，若未在正文中体现，不视为对应 task 已完成。
- **最近一次基线验证：** `pdflatex -interaction=nonstopmode -halt-on-error 0.main.tex` 已在 `2026-04-12` 成功执行。
- **Task 1 产出：** `docs/research/2026-03-22-manuscript-baseline.md`

## 检查点总览

- **CP0 基线冻结：** 已完成
- **CP1 近期论文池就绪：** 未完成
- **CP2 Taxonomy 映射锁定：** 未完成
- **CP3 前言部分更新：** 部分完成，目前仅 `tex/0.main.tex`、`tex/1.intro.tex`、`tex/2.methodology.tex` 有直接改写证据，且 ProG 定位尚未统一。
- **CP4 核心 Taxonomy 更新：** 未完成
- **CP5 溢出内容补入：** 未完成
- **CP6 参考文献与资源同步：** 未完成
- **CP7 发布候选版构建：** 未完成

### Task 1：冻结基线并记录修订范围

**文件：**
- Read: `tex/0.main.tex`
- Read: `tex/1.intro.tex`
- Read: `tex/2.methodology.tex`
- Read: `tex/5.tex`
- Read: `tex/6.Applications.tex`
- Read: `tex/8.Discussion.tex`
- Update or create: `docs/research/2026-03-22-manuscript-baseline.md`

- [x] 先完整编译当前稿件一次，并记录它是否能够在不手动修复的情况下成功编译。
- [x] 记录当前章节布局、主要表格/图片以及所有编译警告。
- [x] 记录所有显然已经过时、需要尽早删除的内容，尤其是 `tex/0.main.tex` 中红色的投稿说明。
- [x] 以书面形式确认编辑策略：taxonomy 主干不变，近期论文加入现有节点，不适配 taxonomy 的内容转移到 Applications。

**检查点 CP0**

- 退出标准：存在一份基线说明文档，已列出当前风险，并且明确写明本轮修订边界。

### Task 2：构建 2024-2026 年论文池

**文件：**
- Create: `docs/papers/2026-03-22-recent-graph-prompt-paper-pool.md`
- Update: `tex/zotero.bib`

- [ ] 收集 2024-2026 年的候选论文，重点覆盖图提示学习、图提示调优、图提示迁移、graph-LLM prompt interface，以及应用驱动的图提示工作。
- [ ] 为每篇论文记录 venue、年份、任务类型、prompt 类型，以及一句话贡献总结。
- [ ] 排除那些仅讨论图基础模型、泛化 graph-LLM survey，或根本没有实质性 prompt 组成部分的应用系统论文。
- [ ] 将每篇论文标记为 `core taxonomy`、`applications overflow`、`discussion/trend` 或 `discard`。
- [ ] 将所有保留论文缺失的 BibTeX 条目加入 `tex/zotero.bib`，但正文中的 citation 插入推迟到映射完成之后。

**检查点 CP1**

- 退出标准：论文池文件已经存在，且每篇保留论文都有初步去向标签。

### Task 3：锁定 Taxonomy 映射

**文件：**
- Create: `docs/research/2026-03-22-taxonomy-mapping.md`
- Read: `tex/pic/taxonomy.tex`
- Read: `tex/2.methodology.tex`
- Read: `tex/5.tex`
- Read: `tex/6.Applications.tex`
- Read: `tex/8.Discussion.tex`

- [ ] 创建一张映射表，列包括：论文、venue/year、主要贡献、当前 taxonomy bucket、目标稿件章节，以及分配理由。
- [ ] 强制每篇保留论文进入以下三类去向之一：现有 taxonomy 小节、Applications 溢出区、或 Discussion 趋势分析。
- [ ] 识别当前 taxonomy 中那些确实获得了较多近年后续工作的叶子节点，并将其标记为应扩写。
- [ ] 识别当前 taxonomy 中那些后续工作很少、应主要保留历史角色的叶子节点。
- [ ] 标记那些边界适配的论文，并记录为什么它们不足以触发一次 taxonomy 重设计。

**检查点 CP2**

- 退出标准：每篇保留论文都有最终目标章节，且团队已确认不需要重构 taxonomy。

### Task 4：刷新前言部分与综述定位

**文件：**
- Modify: `tex/0.main.tex`
- Modify: `tex/1.intro.tex`
- Modify: `tex/2.methodology.tex`

- [x] 删除 `tex/0.main.tex` 中红色的拒稿/投稿说明。
- [x] 重写摘要和引言中已经过时的新颖性表述，使其适用于 2026 年投稿。
- [x] 更新诸如 `first`、`pioneering`、`recent` 等已不再站得住脚的措辞。
- [x] 更新方法学部分中的论文计数和时间窗口，使其反映扩展后的语料范围。
- [x] 保留原有研究问题和叙事弧线，但改写所有暗示该领域仍停留在 2023 年规模的句子。
- [x] 验证摘要、引言和方法学使用相同的年份范围和论文计数口径。
- [x] 用 2023 年之后发表的图提示综述更新 `Connection to Existing Work`，并将更宽泛但相关性较弱的 survey 降为背景参考。
- [x] 统一摘要、引言和方法学的学术语气，去掉修订痕迹式措辞和过程化表述。
- [ ] 重新审查前言部分和综述定位中的所有 ProG 相关措辞，使 ProG 被一致表述为已发表的 benchmark/toolkit 论文，而不只是内部开发库。

**检查点 CP3**

- 退出标准：前言部分已去除陈旧论断，内部表述一致，与新的修订范围对齐，并采用正式的综述语气。

### Task 5：在不重构的前提下更新核心 Taxonomy 章节

**文件：**
- Modify: `tex/5.tex`
- Modify if needed: `tex/table/*`

- [ ] 逐一审查 `tex/5.tex` 中现有的小节，并决定每个小节需要加入 0 篇、1 篇或多篇近期代表论文。
- [ ] 仅在现有类别下插入近期论文：prompt-as-tokens、prompt-as-graphs、answering functions、prompt tuning、multimodal prompting、domain adaptation。
- [ ] 对每篇新增论文，都使用当前 taxonomy 的语言来解释，而不是引入新的类别名称。
- [ ] 识别那些如今已经过旧、过于孤立或代表性不足的历史方法，并在保留必要历史锚点的前提下，对其进行压缩或用更强的近年代表作替换。
- [ ] 更新摘要表格，使新增引用不仅出现在段落文字中，也能出现在结构化对比里。
- [ ] 在可能的情况下保持段落顺序稳定；除非局部重写不可避免，否则将近期工作追加在现有段落块的末尾。
- [ ] 在需要时加入简短过渡句，说明即便出现了新变体，当前 taxonomy 仍然有效。

**检查点 CP4**

- 退出标准：`tex/5.tex` 已通过既有 taxonomy 覆盖近期代表性方法，且没有哪个主要小节明显落后于当前领域进展。

### Task 6：在 Applications 和 Discussion 中承接非 Taxonomy 方法

**文件：**
- Modify: `tex/6.Applications.tex`
- Modify: `tex/8.Discussion.tex`

- [ ] 在 `tex/6.Applications.tex` 中新增一个紧凑的 overflow 小节，用于容纳近期那些由应用驱动、系统驱动，或难以放入 taxonomy 的方法。
- [ ] 保留现有应用领域划分，但在近期工作实质改变图景的地方更新代表性引用。
- [ ] 在 `tex/8.Discussion.tex` 中加入讨论文本，覆盖那些过于宽泛、不适合放入 taxonomy 的趋势，例如 graph-LLM 集成模式、评测碎片化、prompt 可解释性或跨领域迁移问题。
- [ ] 明确写出承接关系：如果一篇论文不在 taxonomy 章节中，Applications 或 Discussion 章节应说明它为什么仍然重要。
- [ ] 更新与 ProG 相关的讨论，使综述能够反映其已发表的 benchmark 状态，并澄清它与更广泛 graph prompting 生态之间的关系。

**检查点 CP5**

- 退出标准：近期非 taxonomy 工作是可见的，稿件不会悄悄遗漏重要趋势。

### Task 7：同步参考文献、统计信息与支撑资源

**文件：**
- Modify: `tex/zotero.bib`
- Modify: `tex/2.methodology.tex`
- Modify if needed: `tex/pic/taxonomy.tex`
- Modify if needed: `tex/pic/reference_venue.pdf`
- Modify if needed: `tex/pic/top_keywords_bar.pdf`

- [ ] 对所有新增 BibTeX 条目进行去重和规范化。
- [ ] 检查在加入 2024-2026 年论文后，venue 分布和关键词统计是否仍然站得住脚。
- [ ] 决定是完整重生成统计图，还是保留原图并在正文中明确弱化定量论断。
- [ ] 确保摘要、方法学和讨论中提到的论文计数，与实际由参考文献驱动的覆盖范围一致。
- [ ] 验证稿件中使用的每个新 citation key 都能被正确解析。

**检查点 CP6**

- 退出标准：参考文献干净，计数一致，支撑图表不再与正文矛盾。

### Task 8：最终编辑检查与构建验证

**文件：**
- Modify as needed: `tex/*.tex`
- Read: build logs

- [ ] 反复编译全文，直到交叉引用和参考文献稳定下来。
- [ ] 修复未解析的引用、损坏的图表引用，以及明显的格式回归问题。
- [ ] 最后再检查一次时态一致性、年份表述以及过强的新颖性论断。
- [ ] 检查 Applications 是否包含映射文件中识别出的所有 overflow 方法。
- [ ] 检查是否有 taxonomy 变更被无意中混入。
- [ ] 最后统一检查摘要、引言、方法学、Applications 与 `tex/7.ProG.tex` 中关于 ProG 的引用、术语和论断是否一致。
- [ ] 如仍有未解决问题，在 `docs/research/2026-03-22-revision-closeout.md` 中记录一份简短的 release note。

**检查点 CP7**

- 退出标准：稿件可编译，本轮修订在结构上是保守的，且所有剩余限制都已被明确记录。

## 建议编辑顺序

- [x] 先做 Task 1
- [ ] 然后做 Task 2
- [ ] 在任何正文大改之前完成 Task 3
- [x] 在 Task 5 之前完成 Task 4
- [ ] 在 Task 6 之前完成 Task 5
- [ ] 在正文更新完成后执行 Task 7
- [ ] 最后执行 Task 8

## 非目标

- 不要从零开始重设计 taxonomy。
- 不要把这篇综述扩展成泛化的图基础模型或 graph-LLM survey。
- 除非出现硬性投稿要求，否则不要新增顶层章节。
- 如果某篇近期论文与 taxonomy 的匹配度很差，不要强行把它塞进 taxonomy。

## 可选扩展轨道

### Task 9：论文之外的生态刷新

**文件 / 仓库：**
- Optional update: `Awesome-Graph-Prompt`
- Optional update: `ProG`
- Optional planning note if needed: `docs/research/2026-03-22-ecosystem-extension.md`

- [ ] 将最新已接收论文和高价值预印本同步到 `Awesome-Graph-Prompt`。
- [ ] 在实现质量足够的前提下，将新收集到的代码库、benchmark 或 wrapper 加入 ProG，以覆盖近期代表性方法。
- [ ] 评估是否有必要推进 `ProG-V2` 发布，包括范围、迁移成本、benchmark 覆盖与维护负担。
- [ ] 如果决定推进 `ProG-V2`，应另外写一份边界清晰的独立计划，而不是把它混入综述修订任务中。

**可选检查点 OP1**

- 退出标准：生态侧更新要么已经完成，要么已附理由明确延期；任何 `ProG-V2` 相关工作都已有单独的范围定义。

## 实际完成定义

- 更新后的综述读起来应像同一篇论文的刷新版，而不是重写后的新稿。
- 读者仍然可以立刻恢复并理解原有 taxonomy 逻辑。
- 审稿人能够看出这次文献更新是系统性的，并且覆盖到了 2026 年初。

# gpl-survey 文档目录

本目录只作为 TeX 正文之外的研究材料、修订计划和审计记录。当前执行入口只有两个：

1. `docs/audits/待修复问题清单.md`：按当前 TeX 源码复核后的有效问题清单。
2. `docs/plan/图提示综述修订计划.md`：大版本修订路线图和检查点记录。

## 当前文档分层

### Active：后续修稿优先参考

| 文件 | 用途 | 状态 |
|---|---|---|
| `audits/待修复问题清单.md` | 当前仍需修的问题，已按 TeX 源码重新核查 | 主清单 |
| `plan/图提示综述修订计划.md` | 2026 刷新计划、任务边界、检查点 | 保留 |
| `papers/近期图提示论文池.md` | 2024--2026 近期论文池和初步去向 | 保留，后续映射表可从这里生成 |
| `audits/dblp_reference_audit.md` | DBLP 元数据核查结果 | 保留，参考文献清理时使用 |
| `audits/zotero-bib-audit-2026-04-28.md` | Zotero/BibTeX 清理记录 | 保留，作为引用审计记录 |

### Reference：保留为背景材料，不作为当前待办入口

| 文件 | 处理建议 |
|---|---|
| `audits/稿件基线记录.md` | 历史基线快照，保留 |
| `audits/表格审查问题清单.md` | 表格专项旧审查，已并入主清单；保留为细节来源 |
| `audits/表格公式核查报告.md` | 更早的表格公式核查，内容多已过期；保留为审计记录 |
| `research/6.Applications_recent_literature.md` | Section 6 近期文献建议；大部分已进入当前正文，保留为来源记录 |
| `papers/Section5-候选文献-按类型简介.md` | 比正式论文池更宽的候选池，保留 |
| `papers/Section5-两篇Survey精读对比.md` | 面向 Section 5 的 survey 精读，保留 |
| `research/三篇图提示综述论文精读.md` | 更完整的 survey 横向比较，可作为上一个文件的扩展版 |
| `research/GPL论文检索报告.md` | 早期检索报告和种子文献分析，保留为背景 |

### Archive candidates：建议后续归档或删除

| 文件 | 原因 | 建议 |
|---|---|---|
| `docs/5_zh.md` | 与 `research/5.tex中文翻译.md` 内容高度重叠，且根目录文件不符合当前分层 | 合并到 `research/5.tex中文翻译.md` 后归档或删除 |
| `research/5.tex中文翻译.md` | 只是 Section 5 翻译快照，不应驱动当前修稿 | 若仍有用则保留在 `research/`，否则归档 |
| `docs/GNN` | 当前是指向 `/home/river/Documents/notes/quartz/content/GNN` 的已跟踪符号链接，在本机为 broken symlink | 建议删除该 symlink，或改成真实可访问的相对路径 |

## 维护约定

1. 新问题只写入 `audits/待修复问题清单.md`，不要再新建多个并行待办清单。
2. 文献池、引用审计、正文问题分开维护：论文候选放 `papers/`，BibTeX/Zotero/DBLP 和正文问题核查放 `audits/`。
3. 旧审查文档保留时必须在索引中标注状态，避免把已修复问题重复带入下一轮修稿。
4. 若生成新的 mapping 或 closeout 文档，优先放在 `research/`，并在本 README 更新索引。

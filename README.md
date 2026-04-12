```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=tex_zh/build tex_zh/0.main.tex
```

## 项目结构

```text
gpl-survey/
├─ docs/        # 研究记录、计划文档与论文相关说明
├─ papers/      # 综述原文、候选论文、Zotero 导出与 PDF 资料
├─ scripts/     # 文献下载、Zotero 附件整理等辅助脚本
├─ tex/         # 英文版论文 TeX 源码、图片、表格与编译产物
├─ tex_zh/      # 中文版论文 TeX 源码、图片、表格与编译产物
├─ .agents/     # 项目内可复用的技能与辅助配置
├─ .gitignore
├─ README.md
└─ skills-lock.json
```

## 目录说明

- `docs/`
  - `papers/`：论文池、精读记录、候选文献梳理。
  - `plan/`：修订计划、阶段任务与检查点。
  - `research/`：taxonomy 对比、检索报告、补充调研笔记。
- `papers/`
  - `surveys/`：核心综述论文 PDF 与相关版本。
  - `section5-candidates/`：Section 5 候选论文及配套的 `.bib`、`.json` 数据。
  - `zotero/`、`zotero-test/`：Zotero 下载与测试用资料目录。
- `scripts/`
  - `download_bib_papers.py`：根据文献信息下载论文资料。
  - `attach_pdfs_to_zotero.py`：整理并挂接 PDF 到 Zotero 资料。
- `tex/`
  - 主论文英文稿，包含 `0.main.tex` 及分章节文件、图片目录 `pic/`、表格目录 `table/`。
- `tex_zh/`
  - 主论文中文稿，目录组织与 `tex/` 基本对应，便于双语维护。

## 使用建议

- 日常写作主要在 `tex/` 或 `tex_zh/` 下进行。
- 资料检索和阶段性分析优先沉淀到 `docs/`。
- 新下载的论文与参考数据统一放在 `papers/`。

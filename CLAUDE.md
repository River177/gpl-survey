# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX-based academic survey paper on **Graph Prompt Learning** — a research paper project with bilingual support (English and Chinese). The paper follows IEEE Transactions format and is maintained in parallel English (`tex/`) versions.

## Build Commands

### Compile the paper (XeLaTeX + Biber)

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=tex_zh/build tex_zh/0.main.tex
```

For the English version:
```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=tex/build tex/0.main.tex
```

### Manual compile sequence (if latexmk is unavailable)

```bash
cd tex
xelatex 0.main.tex
biber 0.main
xelatex 0.main.tex
xelatex 0.main.tex
```

## Project Structure

```
gpl-survey/
├── tex/                    # English paper source
│   ├── 0.main.tex         # Main entry point
│   ├── 1.intro.tex        # Section 1: Introduction
│   ├── 2.methodology.tex  # Section 2: Methodology
│   ├── 3.Preliminaries.tex
│   ├── 4.Pre-training.tex
│   ├── 5.tex              # Section 5 (main methods table)
│   ├── 6.Applications.tex
│   ├── 7.ProG.tex
│   ├── 8.Discussion.tex
│   ├── 9.Conclusion.tex
│   ├── Ack.tex            # Acknowledgments
│   ├── zotero.bib         # Bibliography
│   ├── mydef.sty          # Custom style definitions
│   ├── pic/               # Figures
│   └── table/             # Table files
├── tex_zh/                # Chinese paper source (parallel structure)
├── docs/                  # Research notes, plans, paper analyses
│   ├── papers/            # Candidate papers, literature pool
│   ├── plan/              # Revision plans and checkpoints
│   └── research/         # Taxonomy comparisons, search reports
├── papers/                # Downloaded papers, Zotero exports
│   └── section5-candidates/  # Section 5 candidate methods data
├── scripts/               # Utility scripts
│   ├── download_bib_papers.py
│   ├── attach_pdfs_to_zotero.py
│   └── import_graphprompt_new_to_zotero.py
└── .agents/skills/        # Reusable skills for this project
```

## Paper Architecture

- **Main document**: `tex/0.main.tex` uses IEEEtran class with `\input{}` for each section
- **Bibliography**: Managed via `zotero.bib` (Biber backend)
- **Custom macros**: Defined in `mydef.sty`
- **Bibliography style**: `IEEEtranSN` (natbib compatible)

## Working with Skills

This project has configured skills in `skills-lock.json` for:
- `scientific-writing`: For drafting and revising paper sections
- `read-arxiv-paper`: For reading and summarizing ArXiv papers
- `arxiv-search`: For finding relevant papers
- `peer-review`: For reviewing paper content
- `pyzotero`: For Zotero reference management

Skills are stored in `.agents/skills/` and `skills-lock.json` tracks their sources and hashes.

## Common Tasks

### Adding a new section
Create the `.tex` file in `tex/` and add `\input{filename}` (without `.tex` extension) to `0.main.tex` before `\bibliography{zotero.bib}`.

### Adding references
Edit `tex/zotero.bib` directly. Run `biber 0.main` then `xelatex 0.main.tex` twice to update citations.

### Working with candidate methods
Candidate papers for Section 5 are tracked in `papers/section5-candidates/` with JSON files for metadata and markdown files for method summaries.

## Notes

- Build artifacts (`.aux`, `.bbl`, `.blg`, `.log`, `.out`, `.synctex.gz`, `.pdf`) are gitignored
- PDF files across the entire repository are gitignored
- `texmf-local/` is used for local LaTeX package overrides (e.g., `dsfont`)

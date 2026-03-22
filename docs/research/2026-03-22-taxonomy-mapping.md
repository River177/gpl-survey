# Taxonomy Mapping

Date: 2026-03-22

## Purpose

Lock the destination of every retained 2024-2026 paper from Task 2 before editing the manuscript. This mapping keeps the current taxonomy stable and routes poor fits into `Applications` or `Discussion` rather than forcing a taxonomy redesign.

## Mapping policy

- Primary rule: assign each retained paper one primary destination only.
- Preferred destination order:
  1. existing taxonomy subsection in `tex/5.tex`
  2. `tex/6.Applications.tex` for application-driven or scenario-driven methods
  3. `tex/8.Discussion.tex` for theory, benchmarks, privacy, robustness, continual learning, or in-context trends that do not fit the current taxonomy cleanly
- If a paper touches multiple axes, map it by its dominant contribution and record the secondary fit in the rationale.
- No new top-level taxonomy node is introduced in this refresh.

## Summary

- Retained papers mapped: 19
- Mapped to existing taxonomy in `tex/5.tex`: 10
- Routed to `tex/6.Applications.tex`: 2
- Routed to `tex/8.Discussion.tex`: 7
- Conclusion: the current taxonomy remains serviceable for a conservative 2026 refresh; no redesign is required

## Final mapping table

| Bib key | Venue/year | Main contribution | Current taxonomy bucket | Target manuscript section | Rationale |
| --- | --- | --- | --- | --- | --- |
| `zi2024prog` | arXiv/2024 | Benchmark and unified evaluation framework for graph prompt methods | No clean fit; closest to `Connection, Pros, and Cons` | `tex/8.Discussion.tex` under a planned benchmark/evaluation discussion block | This is an evaluation resource rather than a new prompt mechanism, so it should strengthen the discussion on comparison standards rather than be forced into the method taxonomy. |
| `wang2024does` | arXiv/2024 | Theoretical analysis of graph prompting as graph data operations | No clean fit; closest to `Further Discussion` and `Why Graph Prompt?` | `tex/8.Discussion.tex` with a cross-reference to `tex/3.Preliminaries.tex` if needed | The paper explains why graph prompting works but does not introduce a new prompt category. It is better used to support the theory and limitation discussion. |
| `jiang2024unified` | arXiv/2024 | Selective prompt learning over both nodes and edges | `Prompt Token, Structure, and Inserting Pattern -> Prompt as Tokens` | `tex/5.tex` in `Prompt Token, Structure, and Inserting Pattern` | The dominant contribution is still prompt design at the feature level, even though the paper also touches edge prompting. |
| `chen2024temporal` | arXiv/2024 | Temporally-aware prompt generator for temporal interaction graphs | `Prompt Tuning -> Task-specific Tuning` | `tex/5.tex` in `Prompt Tuning` | The method is best treated as a task- and scenario-specific tuning strategy for dynamic graphs without creating a new temporal taxonomy branch. |
| `hu2024spatiotemporal` | arXiv/2024 | Unified prompt framework for cross-task and cross-domain spatio-temporal transfer | No clean fit; closest to `Graph Domain Adaptation with Prompting` | `tex/6.Applications.tex` in a planned overflow subsection for emerging application-driven directions | The contribution is strongly tied to spatio-temporal urban tasks and a transfer pipeline, so it is better handled as application-driven overflow than as a generic taxonomy node. |
| `zhai2024sgpt` | arXiv/2024 | Few-shot signed graph prompt tuning with graph and task templates | `Prompt Tuning -> Task-specific Tuning` | `tex/5.tex` in `Prompt Tuning` | Signed graphs are a specialized downstream setting, and the paper mainly extends task-specific prompt tuning to this regime. |
| `jiang2024graphsparse` | arXiv/2024 | Sparse and compact prompt selection for efficient tuning | `Prompt Tuning -> Task-specific Tuning` | `tex/5.tex` in `Prompt Tuning` | The core novelty is an efficiency-oriented learning strategy for prompts rather than a new prompt representation family. |
| `zhu2024relief` | arXiv/2024 | Reinforcement-learning policy for selecting where and what to prompt | `Prompt Tuning -> Task-specific Tuning` | `tex/5.tex` in `Prompt Tuning` | The paper changes how prompts are learned, not the taxonomy of prompt objects, so it belongs under prompt-learning strategy. |
| `guo2024asymmetric` | arXiv/2024 | Federated prompt learning under multifaceted graph heterogeneity | No clean fit; closest to `Graph Domain Adaptation with Prompting` | `tex/6.Applications.tex` in the planned overflow subsection | Federated heterogeneity is a deployment scenario that goes beyond the current taxonomy's semantic/structural transfer split. |
| `chen2025dagprompt` | arXiv/2025 | Distribution-aware prompting with hop-specific prompts and low-rank adaptation | `Prompt Tuning -> Tuning in Line with Pretext` | `tex/5.tex` in `Prompt Tuning` with a note in `Further Discussion` | Its main value is a more sophisticated tuning mechanism under hard distributions; the LoRA-style encoder adaptation makes it borderline, but still close enough to prompt tuning for a conservative update. |
| `wang2025clear` | arXiv/2025 | Cluster-based prompts and meta-path-aware injection for heterogeneous graphs | `Prompt Token, Structure, and Inserting Pattern -> Prompt as Graphs` | `tex/5.tex` in `Prompt Token, Structure, and Inserting Pattern` | The prompts are structurally organized and injected along meta-path semantics, so the closest stable bucket is structure-aware prompt design rather than a new heterogeneity branch. |
| `wang2025continual` | arXiv/2025 | Prompt-driven continual graph learning with fixed backbone | No clean fit; closest to `Prompt Tuning` | `tex/8.Discussion.tex` under a planned emerging settings block | Continual learning is a new training regime orthogonal to the current taxonomy, so it should appear as an emerging direction rather than a main taxonomy node. |
| `fu2025edge` | arXiv/2025 | Explicit edge prompts injected through message passing | `Prompt Token, Structure, and Inserting Pattern -> Prompt as Tokens` | `tex/5.tex` in `Prompt Token, Structure, and Inserting Pattern` | This is the cleanest recent extension of the inserting-pattern story because it makes edges first-class prompt carriers. |
| `xu2025dpgpl` | arXiv/2025 | Differentially private graph prompt learning and privacy-risk analysis | No clean fit; closest to `Further Discussion` | `tex/8.Discussion.tex` under a planned privacy/reliability block | Privacy is a deployment and trustworthiness concern, not a new prompt-design family. |
| `lv2025graphprompter` | arXiv/2025 | Multi-stage adaptive prompt optimization for graph in-context learning | No clean fit; closest to `Aligning Tasks by Answering Function` | `tex/8.Discussion.tex` under a planned graph in-context learning block | The current taxonomy does not explicitly model graph in-context learning, and this paper would require a new orthogonal branch if absorbed directly. |
| `huang2025oneprompt` | arXiv/2025 | Universal adaptation method for in-domain and cross-domain pretrained models | `Graph Domain Adaptation with Prompting -> Semantic Alignment` | `tex/5.tex` in `Graph Domain Adaptation with Prompting` | The paper is primarily about broad downstream adaptation under distribution shift. Semantic scenario adaptation is the closest stable destination, even though it also contains theory. |
| `zhang2026adversarial` | arXiv/2026 | Adversarial graph prompting for robust PEFT-style adaptation | No clean fit; closest to `Further Discussion` | `tex/8.Discussion.tex` under a planned robustness block | Robustness is an orthogonal evaluation property and should not create a new taxonomy axis in this revision. |
| `nguyen2026magprompt` | arXiv/2026 | Message-adaptive prompt tuning inside message passing | `Prompt Token, Structure, and Inserting Pattern -> Prompt as Tokens` | `tex/5.tex` in `Prompt Token, Structure, and Inserting Pattern` | The most stable way to absorb it is as a new insertion design that moves prompts from input-only manipulation into message-level adaptation. |
| `he2026gp2f` | arXiv/2026 | Cross-domain prompting with adaptive fusion of frozen and adapted branches | `Graph Domain Adaptation with Prompting -> Structural Alignment` | `tex/5.tex` in `Graph Domain Adaptation with Prompting` | The paper explicitly uses topology-consistent constraints and cross-domain fusion, so structural alignment is the closest primary bucket, with semantic transfer noted secondarily. |

## Leaves that should be expanded in this refresh

These existing taxonomy leaves received meaningful recent follow-up and should be updated in the main text:

- `Prompt Token, Structure, and Inserting Pattern -> Prompt as Tokens`
  - supported by `jiang2024unified`, `fu2025edge`, `nguyen2026magprompt`
- `Prompt Token, Structure, and Inserting Pattern -> Prompt as Graphs`
  - supported by `wang2025clear`
- `Prompt Tuning -> Task-specific Tuning`
  - supported by `chen2024temporal`, `zhai2024sgpt`, `jiang2024graphsparse`, `zhu2024relief`
- `Prompt Tuning -> Tuning in Line with Pretext`
  - supported by `chen2025dagprompt`
- `Graph Domain Adaptation with Prompting -> Semantic Alignment`
  - supported by `huang2025oneprompt`
- `Graph Domain Adaptation with Prompting -> Structural Alignment`
  - supported by `he2026gp2f`
- `Further Discussion`
  - needs explicit additions for benchmark, theory, privacy, robustness, continual learning, and graph in-context learning trends

## Leaves that should remain mostly historical

These current leaves have little direct 2024-2026 follow-up in the retained pool and should not be expanded aggressively:

- `Prompt as Graphs` as a broad general-purpose family
  - only one clear retained addition (`wang2025clear`) and it is heterogeneity-specific
- `Aligning Tasks by Answering Function -> Handling Different Level Tasks`
  - recent papers rarely foreground this as their main novelty
- `Aligning Tasks by Answering Function -> Learnable Answering Function`
  - limited explicit recent follow-up in the retained pool
- `Aligning Tasks by Answering Function -> Hand-crafted Answering Function`
  - little recent direct extension
- `Prompt Tuning -> Meta-Learning Technique`
  - no strong retained 2024-2026 follow-up in the current pool
- `Multi-Modal Prompting with Graphs`
  - not the main center of gravity in this retained paper pool
- `Large Language Models in Graph Data Processing`
  - better handled in discussion or scoped overflow if needed, not as a major 2024-2026 expansion target here

## Borderline fits and why they do not trigger taxonomy redesign

- `chen2025dagprompt`
  - Borderline because it mixes prompting with LoRA-like encoder adaptation.
  - Decision: keep it under `Prompt Tuning` and mention the PEFT blur in `Further Discussion`.
- `wang2025clear`
  - Borderline because heterogeneous meta-path prompts could motivate a dedicated heterogeneity branch.
  - Decision: keep it under structured prompt design because one paper is not enough to justify a new branch.
- `lv2025graphprompter`
  - Borderline because graph in-context learning could become its own taxonomy axis in a larger rewrite.
  - Decision: keep it in `Discussion` for this conservative update.
- `guo2024asymmetric`
  - Borderline because federated prompt learning intersects domain adaptation, heterogeneity, and deployment.
  - Decision: keep it in `Applications` as a scenario-driven extension.
- `hu2024spatiotemporal`
  - Borderline because it combines cross-task, cross-domain, and spatio-temporal transfer in one framework.
  - Decision: keep it in `Applications` rather than stretching the general taxonomy.
- `huang2025oneprompt`
  - Borderline because it includes both theoretical analysis and adaptation.
  - Decision: place it in semantic alignment, with a short note in `Further Discussion` if space permits.
- `he2026gp2f`
  - Borderline because it spans both semantic and structural transfer.
  - Decision: assign it primarily to structural alignment due to topology-consistent fusion.

## Editorial implication for Task 4 and Task 5

- `tex/5.tex` should absorb the 10 taxonomy-mapped papers by extending existing paragraphs, not by adding new top-level subsections.
- `tex/6.Applications.tex` should receive a small overflow block for spatio-temporal transfer and federated heterogeneous prompting.
- `tex/8.Discussion.tex` should explicitly host benchmark, theory, continual learning, graph in-context learning, privacy, and robustness updates.
- No taxonomy redraw is required in `tex/pic/taxonomy.tex` for the current refresh.

## CP2 status

Task 3 can be treated as complete once this mapping is used as the sole routing document for manuscript edits.

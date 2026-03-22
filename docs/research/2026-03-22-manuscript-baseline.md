# Manuscript Baseline

Date: 2026-03-22

## Purpose

Freeze the current state of the survey manuscript before the 2026 literature-refresh pass. This note records the current build status, section layout, major assets, obvious stale content, and the editing boundary for the revision.

## Baseline Build

- Working directory: `D:/GPL/gpl-survey/tex`
- Command used: `latexmk -pdf -interaction=nonstopmode -halt-on-error 0.main.tex`
- Result: build succeeded
- Output: `tex/0.main.pdf`
- Built PDF size at baseline: about 20 pages

## Build Warnings at Baseline

Non-blocking warnings observed in `tex/0.main.log`:

- `LaTeX Warning: No \author given.` appears multiple times.
- `Package caption Warning: Unknown document class (or package), standard defaults will be used.`
- Multiple `Overfull \hbox` warnings, especially around:
  - `tex/pic/taxonomy.tex`
  - `tex/3.Preliminaries.tex`
  - `tex/4.Pre-training.tex`
  - `tex/5.tex`
  - `tex/7.ProG.tex`
  - bibliography output
- Multiple `Underfull \vbox` and `Underfull \hbox` warnings.
- `IEEEtranSN.bst` reports missing hyphenation pattern for language `en`.
- `latexmk` prints an odd transient `Missing bbl file '0.main.bbl'` message even though the final build completes and `0.main.bbl` is produced. Treat as a tooling quirk unless it reproduces in later runs with citation failures.

Current conclusion: the manuscript is buildable without manual fixes, but the warning profile is noisy and should be re-checked after content updates.

## Current Manuscript Structure

Top-level assembly in `tex/0.main.tex`:

1. `tex/1.intro.tex`
2. `tex/2.methodology.tex`
3. `tex/3.Preliminaries.tex`
4. `tex/4.Pre-training.tex`
5. `tex/5.tex`
6. `tex/6.Applications.tex`
7. `tex/7.ProG.tex`
8. `tex/8.Discussion.tex`
9. `tex/9.Conclusion.tex`
10. `tex/Ack.tex`

Major section layout at baseline:

- `Introduction`
- `Survey Methodology`
- `Preliminaries`
- `Pre-training GNNs for Graph Prompting`
- `Prompt Design for Graph Tasks`
- `Graph Prompting in Multi-Modal and Multi-Domain Areas`
- `Potential Applications`
- `ProG: A Unified Library for Graph Prompting`
- `Challenges and Future Directions`
- `Conclusion`
- `Acknowledgments`

## Major Figures and Tables at Baseline

Figures:

- `tex/1.intro.tex`
  - `pic/ThreeChallenges.pdf`
  - `pic/PromptExample.pdf`
  - `pic/pt.pdf`
- `tex/2.methodology.tex`
  - `pic/taxonomy.tex`
  - `pic/reference_venue.pdf`
  - `pic/top_keywords_bar.pdf`
- `tex/3.Preliminaries.tex`
  - one figure block
- `tex/4.Pre-training.tex`
  - `pic/WhyPrompt2.pdf`
  - `pic/pretraining.pdf`
- `tex/5.tex`
  - `pic/prompt.pdf`
- `tex/7.ProG.tex`
  - `pic/ProG_pipeline.pdf`

Tables:

- `tex/2.methodology.tex`
  - research objectives table
- `tex/4.Pre-training.tex`
  - `table/graph_prompt_summary.tex`

## Obvious Stale or High-Risk Content

### Must remove early

- `tex/0.main.tex:98`
  - Red submission-history note about TKDE rejection and later venue plans.

### Must rewrite or soften

- `tex/0.main.tex:88`
  - Claims such as `pioneering survey`, `the first to propose`, `over 100 works`, `remains nascent`, and similar 2023-positioning language.
- `tex/1.intro.tex:108`
  - `the first of its kind` claim.
- `tex/1.intro.tex:111`
  - `the first endeavor` claim regarding the prompt-model perspective.
- `tex/1.intro.tex:127`
  - `over a hundred recent works` will likely become numerically stale after the refresh.
- `tex/2.methodology.tex:76`
  - `more than 100 high-quality papers published within the past 5 years` is now time-sensitive and must be recomputed.
- `tex/2.methodology.tex:98`
  - comparison against earlier surveys is written from a 2023/2024 vantage point and must be updated carefully.
- `tex/5.tex:2`
  - `most representative works published recently` is too vague for a 2026 refresh.
- `tex/5.tex:88`, `tex/5.tex:105`, `tex/5.tex:122`
  - several `currently`, `recent`, and future-looking claims need re-timing.
- `tex/6.Applications.tex` and `tex/8.Discussion.tex`
  - multiple claims say the area is still under-explored or mainly future work; these need to be re-evaluated against 2024-2026 literature.

### Likely still structurally valid

- The main section ordering in `tex/0.main.tex`
- The taxonomy tree in `tex/pic/taxonomy.tex`
- The central decomposition in `tex/5.tex`:
  - prompt token / structure / inserting pattern
  - answering function
  - prompt tuning
  - multimodal prompting
  - domain adaptation

## Revision Boundary Confirmed

This refresh will follow the conservative editing policy below:

- Keep the top-level manuscript structure unchanged.
- Keep the taxonomy backbone unchanged unless a factual error forces a minimal patch.
- Add 2024-2026 work under existing taxonomy leaves whenever the fit is reasonable.
- If a recent method does not fit the taxonomy cleanly, place it in `tex/6.Applications.tex` and, if trend-level discussion is needed, in `tex/8.Discussion.tex`.
- Prefer textual updates over section redesign.

## Immediate Risks for the Next Tasks

- The current manuscript still contains several absolute novelty claims that will become review targets if not removed early.
- Quantitative statements about paper count, year span, venue distribution, and keyword statistics are likely stale.
- `ProG` and the companion repository are still framed as active ecosystem assets; their current status should be verified before being emphasized again.
- The warning-heavy build means layout regressions may be hard to spot later unless warnings are compared before and after major edits.

## CP0 Status

CP0 can be treated as complete once this note is committed into the revision workflow:

- Build status recorded
- Section and asset layout recorded
- Obvious stale content recorded
- Editing boundary recorded

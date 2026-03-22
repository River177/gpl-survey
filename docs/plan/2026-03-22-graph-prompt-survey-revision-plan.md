# Graph Prompt Survey Revision Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refresh the 2023 graph prompt survey draft to a 2026-ready version with minimal structural changes, preserving the main taxonomy and routing non-taxonomy recent methods into the Applications section.

**Architecture:** Keep the section order and taxonomy backbone unchanged, update claims and literature coverage, then absorb 2024-2026 work through existing subsections in the main taxonomy chapter. Any recent work that does not fit the current taxonomy should be documented in Applications or Discussion instead of forcing a taxonomy redesign.

**Tech Stack:** LaTeX, BibTeX, Markdown planning notes, local paper screening notes under `docs/`

---

## Constraints and Scope

- Keep the top-level section structure in `tex/0.main.tex` unchanged.
- Keep the taxonomy tree in `tex/pic/taxonomy.tex` unchanged unless a factual error forces a minimal patch.
- Prefer textual updates over structural rewrites.
- Treat the target refresh window as `2024-01-01` to `2026-03-22`.
- Route methods that do not fit the existing taxonomy into `tex/6.Applications.tex` and, if needed, trend-level discussion into `tex/8.Discussion.tex`.

## Global Success Criteria

- The manuscript no longer contains outdated submission notes, stale novelty claims, or inconsistent year ranges.
- Recent papers are added systematically rather than ad hoc.
- The taxonomy chapter still reads as the center of the survey.
- Overflow methods are handled explicitly in Applications instead of silently omitted.
- ProG is described accurately as a published benchmark/toolkit paper rather than an unpublished companion artifact.
- Overly old methods are selectively compressed or replaced when they no longer serve the updated survey narrative.
- The full manuscript compiles cleanly with resolved references and bibliography.

## Main Workstreams

### Workstream 1: ProG Positioning Refresh

- Update all ProG-related wording so that ProG is described consistently as a published benchmark/toolkit paper rather than merely an internal library or companion artifact.
- Check the abstract, introduction, methodology, Applications, and `tex/7.ProG.tex` for terminology, claims, and citation consistency.

### Workstream 2: Core Survey Refresh with Better Representative Methods

- Update the taxonomy-centered review with representative work from 2024-2026 while keeping the existing taxonomy structure unchanged.
- Compress, demote, or replace overly old methods when they no longer provide strong coverage of the current field, while preserving a necessary historical backbone.

### Workstream 3: Optional Ecosystem Extension

- Optionally sync recent papers into `Awesome-Graph-Prompt`.
- Optionally update ProG with newly collected codebases, benchmarks, or wrappers for recent representative methods.
- Optionally evaluate whether `ProG-V2` should be planned as a separate scoped follow-up project.

## Current Execution State

- **Completed checkpoints:** `CP0`, `CP1`, `CP2`, `CP3`
- **Current focus:** `Task 5 / CP4`, namely updating `tex/5.tex` with recent representative methods while preserving the existing taxonomy structure.
- **Key completed outputs:**
  - `docs/research/2026-03-22-manuscript-baseline.md`
  - `docs/papers/2026-03-22-recent-graph-prompt-paper-pool.md`
  - `docs/research/2026-03-22-taxonomy-mapping.md`
- **Positioning updates already completed:**
  - stale submission-note and novelty-claim cleanup in front matter
  - `Connection to Existing Work` refreshed with post-2023 graph-prompt surveys
  - academic tone unified across abstract, introduction, and methodology
- **New planning requirements incorporated:**
  - revise ProG-related wording to reflect its published benchmark-paper status
  - replace some overly old methods with more representative recent methods where appropriate
  - keep ecosystem refresh tasks such as `Awesome-Graph-Prompt` updates and `ProG-V2` as optional follow-up work
- **Latest verification:** `pdflatex -interaction=nonstopmode -halt-on-error 0.main.tex` completed successfully on `2026-03-22`

## Checkpoints Overview

- **CP0 Baseline Frozen:** current manuscript status, warnings, and revision scope are recorded.
- **CP1 Recent Paper Pool Ready:** screened 2024-2026 paper list is complete enough for revision.
- **CP2 Taxonomy Mapping Locked:** each retained recent paper has a destination section.
- **CP3 Front Matter Updated:** title-page text, abstract, intro, and methodology are time-consistent.
- **CP4 Core Taxonomy Updated:** `tex/5.tex` and its summary material reflect recent representative methods.
- **CP5 Overflow Coverage Added:** non-taxonomy work is captured in Applications and trend discussion.
- **CP6 References and Assets Synced:** bibliography, tables, counts, and figures are internally consistent.
- **CP7 Release Candidate Built:** the paper compiles and passes final editorial checks.

### Task 1: Freeze Baseline and Record Revision Scope

**Files:**
- Read: `tex/0.main.tex`
- Read: `tex/1.intro.tex`
- Read: `tex/2.methodology.tex`
- Read: `tex/5.tex`
- Read: `tex/6.Applications.tex`
- Read: `tex/8.Discussion.tex`
- Update or create: `docs/research/2026-03-22-manuscript-baseline.md`

- [x] Build the current manuscript once and record whether it compiles without manual fixes.
- [x] Record the current section layout, major tables/figures, and any compile warnings.
- [x] Record all obviously stale content that must be removed early, especially the red submission note in `tex/0.main.tex`.
- [x] Confirm the editing policy in writing: taxonomy backbone unchanged, recent papers added under existing nodes, overflow moved to Applications.

**Checkpoint CP0**

- Exit criteria: one baseline note exists, current risks are listed, and the revision boundary is explicitly documented.

### Task 2: Build the 2024-2026 Paper Pool

**Files:**
- Create: `docs/papers/2026-03-22-recent-graph-prompt-paper-pool.md`
- Update: `tex/zotero.bib`

- [x] Collect candidate papers from 2024-2026 focused on graph prompt learning, graph prompt tuning, graph prompt transfer, graph-LLM prompt interfaces, and application-driven graph prompting.
- [x] For each paper, record venue, year, task type, prompt type, and a one-sentence contribution summary.
- [x] Exclude papers that are only about graph foundation models, general graph-LLM surveys, or application systems with no meaningful prompt component.
- [x] Mark each paper as `core taxonomy`, `applications overflow`, `discussion/trend`, or `discard`.
- [x] Add missing BibTeX entries for retained papers into `tex/zotero.bib`, but defer in-text citation insertion until mapping is complete.

**Checkpoint CP1**

- Exit criteria: the paper pool file exists and every retained paper has a preliminary disposition label.

### Task 3: Lock the Taxonomy Mapping

**Files:**
- Create: `docs/research/2026-03-22-taxonomy-mapping.md`
- Read: `tex/pic/taxonomy.tex`
- Read: `tex/2.methodology.tex`
- Read: `tex/5.tex`
- Read: `tex/6.Applications.tex`
- Read: `tex/8.Discussion.tex`

- [x] Create a mapping table with columns: paper, venue/year, main contribution, current taxonomy bucket, target manuscript section, and rationale.
- [x] Force every retained paper into one of three destinations: existing taxonomy subsection, Applications overflow, or Discussion trend analysis.
- [x] Identify current taxonomy leaves that genuinely received meaningful recent work and should be expanded.
- [x] Identify current taxonomy leaves that have seen little follow-up and should remain mostly historical.
- [x] Mark any papers that are borderline fits and document why they should not trigger a taxonomy redesign.

**Checkpoint CP2**

- Exit criteria: every retained paper has a final destination section and the team agrees no taxonomy redesign is required.

### Task 4: Refresh Front Matter and Survey Positioning

**Files:**
- Modify: `tex/0.main.tex`
- Modify: `tex/1.intro.tex`
- Modify: `tex/2.methodology.tex`

- [x] Remove the red rejection/submission note from `tex/0.main.tex`.
- [x] Rewrite stale novelty claims in the abstract and introduction so they are accurate for a 2026 submission.
- [x] Update wording such as `first`, `pioneering`, or `recent` where they are no longer defensible.
- [x] Update paper counts and time windows in the methodology section to reflect the expanded corpus.
- [x] Keep the original research questions and narrative arc, but rephrase any sentence that implies the field is still at its 2023 scale.
- [x] Verify that abstract, introduction, and methodology use the same year range and paper-count framing.
- [x] Update `Connection to Existing Work` with graph-prompt surveys published after 2023 and demote broader but less directly related surveys to background references.
- [x] Unify the academic tone across abstract, introduction, and methodology by removing revision-trace wording and procedural phrasing.
- [ ] Revisit all ProG-related wording in the front matter and survey positioning so that ProG is described consistently as a published benchmark/toolkit paper rather than only as an internally developed library.

**Checkpoint CP3**

- Exit criteria: front matter is free of stale claims, internally consistent, aligned with the new revision scope, and written in a formal survey tone.

### Task 5: Update the Core Taxonomy Chapter Without Restructuring It

**Files:**
- Modify: `tex/5.tex`
- Modify if needed: `tex/table/*`

- [ ] Review each existing subsection in `tex/5.tex` and decide whether to add 0, 1, or several recent representative papers.
- [ ] Insert recent papers under the existing categories only: prompt-as-tokens, prompt-as-graphs, answering functions, prompt tuning, multimodal prompting, and domain adaptation.
- [ ] For each added paper, explain it through the current taxonomy language instead of introducing new category names.
- [ ] Identify legacy methods that are now too old, too isolated, or too weakly representative, and compress or replace them with stronger recent exemplars while keeping necessary historical anchors.
- [ ] Update summary tables so newly cited papers are visible in the structured comparison, not only in paragraph text.
- [ ] Keep paragraph ordering stable where possible; append recent work near the end of each existing block unless a local rewrite is necessary.
- [ ] Add short transition sentences where needed to clarify that the taxonomy remains valid despite newer variants.

**Checkpoint CP4**

- Exit criteria: `tex/5.tex` covers the recent representative methods through the existing taxonomy and no major subsection is left obviously outdated.

### Task 6: Capture Non-Taxonomy Methods in Applications and Discussion

**Files:**
- Modify: `tex/6.Applications.tex`
- Modify: `tex/8.Discussion.tex`

- [ ] Add a compact overflow subsection to `tex/6.Applications.tex` for recent methods that are application-driven, system-driven, or otherwise awkward to place in the taxonomy.
- [ ] Keep the existing application domains, but update their representative citations where recent work materially changes the picture.
- [ ] Add discussion text in `tex/8.Discussion.tex` for trends that are too broad for taxonomy placement, such as graph-LLM integration patterns, evaluation fragmentation, prompt interpretability, or cross-domain transfer issues.
- [ ] Make the handoff explicit: if a paper is not in the taxonomy chapter, the Applications or Discussion section should say why it matters.
- [ ] Update the ProG-related discussion so that the survey reflects its published benchmark status and clarifies how it relates to the broader graph prompting ecosystem.

**Checkpoint CP5**

- Exit criteria: recent non-taxonomy work is visible and the manuscript does not silently drop important trends.

### Task 7: Synchronize References, Statistics, and Supporting Assets

**Files:**
- Modify: `tex/zotero.bib`
- Modify: `tex/2.methodology.tex`
- Modify if needed: `tex/pic/taxonomy.tex`
- Modify if needed: `tex/pic/reference_venue.pdf`
- Modify if needed: `tex/pic/top_keywords_bar.pdf`

- [ ] Deduplicate and normalize all new BibTeX entries.
- [ ] Check whether the venue distribution and keyword statistics are still defensible after adding 2024-2026 papers.
- [ ] Decide whether to fully regenerate the statistics figures or to keep them and explicitly soften any quantitative claim in text.
- [ ] Ensure the paper count mentioned in the abstract, methodology, and discussion matches the actual bibliography-driven coverage.
- [ ] Verify that every new citation key used in the manuscript resolves correctly.

**Checkpoint CP6**

- Exit criteria: bibliography is clean, counts are consistent, and supporting figures/tables no longer contradict the text.

### Task 8: Final Editorial Pass and Build Verification

**Files:**
- Modify as needed: `tex/*.tex`
- Read: build logs

- [ ] Compile the full manuscript until cross-references and bibliography stabilize.
- [ ] Fix unresolved citations, broken figure/table references, and obvious formatting regressions.
- [ ] Run a final pass for tense consistency, year phrasing, and overly strong novelty claims.
- [ ] Check that Applications contains all overflow methods identified in the mapping file.
- [ ] Check that no taxonomy change slipped in unintentionally.
- [ ] Run a final consistency check on ProG references, terminology, and claims across the abstract, introduction, methodology, Applications, and `tex/7.ProG.tex`.
- [ ] Record the final unresolved issues, if any, in a short release note under `docs/research/2026-03-22-revision-closeout.md`.

**Checkpoint CP7**

- Exit criteria: the manuscript builds, the revision is structurally conservative, and any remaining limitations are explicitly recorded.

## Editing Order Recommendation

- [x] Task 1 first
- [x] Task 2 second
- [x] Task 3 before any major manuscript edits
- [x] Task 4 before Task 5
- [ ] Task 5 before Task 6
- [ ] Task 7 after the main text updates
- [ ] Task 8 last

## Non-Goals

- Do not redesign the taxonomy from scratch.
- Do not expand the survey into a general graph foundation model or graph-LLM survey.
- Do not add new top-level sections unless a hard submission requirement appears.
- Do not force every recent paper into the taxonomy if the fit is poor.

## Optional Extension Track

### Task 9: Ecosystem Refresh Beyond the Manuscript

**Files / Repositories:**
- Optional update: `Awesome-Graph-Prompt`
- Optional update: `ProG`
- Optional planning note if needed: `docs/research/2026-03-22-ecosystem-extension.md`

- [ ] Sync the most recent accepted and high-value preprint papers into `Awesome-Graph-Prompt`.
- [ ] Update ProG to include newly collected codebases, benchmarks, or wrappers for recent representative methods where implementation quality is sufficient.
- [ ] Evaluate whether a `ProG-V2` release is warranted, including scope, migration cost, benchmark coverage, and maintenance burden.
- [ ] If `ProG-V2` is pursued, write a separate scoped plan rather than folding it into the survey-editing tasks.

**Optional Checkpoint OP1**

- Exit criteria: ecosystem-side updates are either completed or explicitly deferred with rationale, and any `ProG-V2` work has a separate scope definition.

## Practical Completion Definition

- The updated survey reads as a refreshed version of the same paper, not a rewritten manuscript.
- A reader can still recover the original taxonomy logic immediately.
- A reviewer can see that the literature update is systematic and current through early 2026.

# Graph Prompt Table Update Notes (2026)

This note screens post-2023 graph prompting papers for possible inclusion in tex/table/graph_prompt_summary.tex.

## Scope

The current table is a method table, not a survey-of-surveys table. A candidate should be added only if it is:

1. A concrete graph prompting method, not just a survey, benchmark, or theory paper.
2. Mappable to the current columns:
   - pre-training task
   - prompt design
   - downstream task
   - answering function
3. Representative enough to justify one row.
4. Preferably peer-reviewed in a strong venue, or at least a strong preprint with a clear new mechanism.

Authority labels used below:

- High: top-tier or clearly established peer-reviewed venue (KDD, WWW, NeurIPS, SIGIR, ICDE, CIKM, etc.)
- Medium: peer-reviewed but more specialized venue, or strong preprint with a clear method contribution
- Low: preprint only, very specialized, or not a good fit for this table

## Recommended High-Priority Additions

These are the best candidates to add if the table is updated for 2024-2026.

| Method                                                       | Venue / status | Authority | Add to table?                                                | Suggested replacement if table length must stay fixed        | Why                                                          |
| :----------------------------------------------------------- | :------------- | :-------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Inductive Graph Alignment Prompt                             | WWW 2024       | High      | Yes                                                          | Replace ULTRA-DP                                             | Stronger published bridge between graph pre-training and downstream adaptation; clearly prompt-based and closer to the current table scope. |
| RELIEF                                                       | KDD 2025       | High      | Yes                                                          | Replace SGL-PT                                               | New mechanism: reinforcement-learning-driven feature prompt tuning. More up to date and more general than the current unpublished SGL-PT row. |
| DAGPrompT                                                    | WWW 2025       | High      | Yes                                                          | Replace PGCL or SAP                                          | One of the strongest recent general-purpose prompt tuning methods; distribution-aware design and strong empirical results. |
| GraphPrompter                                                | ICDE 2025      | High      | Yes, if in-context learning should be represented            | Replace PGCL                                                 | Important if the table should cover graph in-context learning, not just standard downstream prompt tuning. |
| Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs | KDD 2024       | High      | Yes, if TAG / multimodal extension should appear in the main table | Add rather than replace, or replace SAP if table size is fixed | Represents a clear TAG-specific prompting setting not covered by the current table. |

## Conditional Additions

These methods are real candidates, but whether they belong in the table depends on how broad or specialized the table should be.

| Method                                               | Venue / status                   | Authority | Add to table? | Notes                                                        |
| :--------------------------------------------------- | :------------------------------- | :-------- | :------------ | :----------------------------------------------------------- |
| GPT4Rec                                              | SIGIR 2024                       | High      | Maybe         | Strong paper, but highly application-specific to streaming recommendation. Better for applications/discussion than for the main method table unless recommendation methods are explicitly represented. |
| Prompt-Based Spatio-Temporal Graph Transfer Learning | CIKM 2024                        | High      | Maybe         | Good paper, but specialized to spatio-temporal graph transfer. Worth adding only if dynamic / temporal graphs are considered in scope. |
| CLEAR                                                | peer-reviewed LNCS chapter, 2025 | Medium    | Maybe         | Useful heterogeneous-graph prompt method. Could be added if a second hetero-graph row is wanted beyond HetGPT. |
| SGPT                                                 | CIKM 2025                        | High      | Maybe         | Signed-graph prompting is new and interesting, but highly specialized. Better as a domain-specific extension than as a core representative row. |
| One Prompt Fits All (UniPrompt)                      | NeurIPS 2025                     | Medium-High | Maybe         | Conceptually strong and directly relevant to universal adaptation. It is now accepted to the NeurIPS 2025 main conference, so it deserves closer attention in the cross-domain discussion. |
| Edge Prompt Tuning for GNNs (EdgePrompt)             | arXiv 2025                       | Medium    | Maybe later   | Good mechanism novelty: prompting edges rather than only node features. Worth adding once published. |
| MAGPrompt                                            | arXiv 2026                       | Medium    | Maybe later   | Good mechanism novelty at the message-passing level. Too early for a stable survey table unless the paper becomes influential quickly. |
| Unsupervised Prompting for GNNs                      | arXiv 2025                       | Medium    | Maybe later   | Interesting because it removes label dependence, but still preprint-only and not in the local candidate folder. |
| GP2F                                                 | arXiv 2026                       | Medium    | Maybe later   | Relevant to cross-domain prompt transfer, but too new and not yet peer-reviewed. |
| GraphTOP                                             | arXiv 2025                       | Medium    | Maybe later   | Topology-oriented prompting is potentially useful, but still preprint-only. |

## Do Not Add To The Main Method Table

These papers are useful for discussion, benchmarking, or future work, but should not occupy one of the main method rows.

| Paper                                                        | Venue / status | Add to table? | Why not                                                      |
| :----------------------------------------------------------- | :------------- | :------------ | :----------------------------------------------------------- |
| ProG: A Graph Prompt Learning Benchmark                      | NeurIPS 2024   | No            | Benchmark, not a new prompting method row. Should be cited in evaluation/tooling sections instead. |
| Towards Graph Prompt Learning: A Survey and Beyond           | arXiv survey   | No            | Survey paper, not a method row.                              |
| Graph Prompting for Graph Learning Models: Recent Advances and Future Directions | KDD 2025       | No            | Survey / perspective paper, not a method row.                |
| Does Graph Prompt Work? A Data Operation Perspective with Theoretical Analysis | arXiv 2025     | No            | Theory / analysis paper, not a new prompting mechanism row.  |
| Prompt-Driven Continual Graph Learning                       | arXiv 2025     | No for now    | Interesting setting, but still preprint-only and not a standard prompt-tuning row in the current taxonomy. |
| Graph Your Own Prompt                                        | arXiv 2025     | No            | More like self-prompting / consistency regularization than a standard graph prompt-tuning method for this table. |
| Learning and Editing Universal Graph Prompt Tuning via Reinforcement Learning | arXiv 2025     | No for now    | Too new and still preprint-only.                             |
| Reliable and Compact Graph Fine-tuning via GraphSparse Prompting | arXiv 2024     | No for now    | More of a graph fine-tuning / sparsification direction; not cleanly aligned with the current table's prompt taxonomy. |
| Against Multifaceted Graph Heterogeneity via Asymmetric Federated Prompt Learning | arXiv 2024     | No            | Federated setting is too specialized for the core table.     |
| Instance-Aware Graph Prompt Learning                         | arXiv 2024     | No for now    | Interesting, but still preprint-only and not clearly stronger than the best published additions. |
| Prompt Learning on Temporal Interaction Graphs               | arXiv 2024     | No            | Current metadata does not confirm a matching published version; dynamic-graph scope is also specialized. |
| When Prompting Meets Spiking                                 | arXiv 2026     | No for now    | Too new and too specialized.                                 |
| Robust Graph Fine-Tuning with Adversarial Graph Prompting    | arXiv 2026     | No for now    | Too new and more robustness-specific than core-method representative. |

## Full Candidate Screening

This list covers the local section5-candidates folder plus one extra external method found during web search.

| Method                                                       | Year | Venue / publication status   | Authority | Add to table? | Notes                                                        |
| :----------------------------------------------------------- | :--- | :--------------------------- | :-------- | :------------ | :----------------------------------------------------------- |
| Inductive Graph Alignment Prompt                             | 2024 | WWW 2024                     | High      | Yes           | Strong published method; very good replacement candidate for ULTRA-DP. |
| Prompt-Based Spatio-Temporal Graph Transfer Learning         | 2024 | CIKM 2024                    | High      | Maybe         | Good but temporal-graph specific.                            |
| ProG                                                         | 2024 | NeurIPS 2024                 | High      | No            | Benchmark only.                                              |
| GPT4Rec                                                      | 2024 | SIGIR 2024                   | High      | Maybe         | Recommendation-specific.                                     |
| A Unified Graph Selective Prompt Learning for GNNs           | 2024 | arXiv only                   | Medium    | Maybe later   | Could be useful, but no clear peer-reviewed version found.   |
| Pre-Training and Prompting for Few-Shot Node Classification on TAGs | 2024 | KDD 2024                     | High      | Yes           | Best TAG-specific method candidate for the table.            |
| RELIEF                                                       | 2025 | KDD 2025                     | High      | Yes           | Strong and general feature-prompt method.                    |
| Does Graph Prompt Work?                                      | 2025 | arXiv only                   | Medium    | No            | Theory / analysis, not a method row.                         |
| GraphSparse Prompting                                        | 2024 | arXiv only                   | Medium    | No for now    | More graph fine-tuning than a clean prompt-table row.        |
| Asymmetric Federated Prompt Learning                         | 2024 | arXiv only                   | Low       | No            | Too specialized.                                             |
| Instance-Aware Graph Prompt Learning                         | 2024 | arXiv only                   | Medium    | No for now    | Preprint only.                                               |
| SGPT                                                         | 2025 | CIKM 2025                    | High      | Maybe         | Good signed-graph extension, but specialized.                |
| DAGPrompT                                                    | 2025 | WWW 2025                     | High      | Yes           | One of the clearest new core additions.                      |
| Prompt-Driven Continual Graph Learning                       | 2025 | arXiv only                   | Medium    | No for now    | Continual-learning setting.                                  |
| CLEAR                                                        | 2025 | LNCS / peer-reviewed chapter | Medium    | Maybe         | Heterogeneous graph prompting extension.                     |
| Edge Prompt Tuning for GNNs                                  | 2025 | arXiv only                   | Medium    | Maybe later   | Good mechanism novelty, but still preprint-only.             |
| GraphPrompter                                                | 2025 | ICDE 2025                    | High      | Yes           | Best candidate if in-context graph learning should be represented. |
| Graph Prompting for Graph Learning Models: Recent Advances and Future Directions | 2025 | KDD 2025                     | High      | No            | Survey / perspective only.                                   |
| One Prompt Fits All                                          | 2025 | NeurIPS 2025                | Medium-High | Maybe       | Promising universal adaptation method with official NeurIPS 2025 acceptance. |
| Graph Your Own Prompt                                        | 2025 | arXiv only                   | Low       | No            | Not a clean fit to the current table's taxonomy.             |
| Event-Aware Prompt Learning for Dynamic Graphs               | 2025 | arXiv only                   | Medium    | No for now    | Dynamic-graph specific and preprint-only.                    |
| GraphTOP                                                     | 2025 | arXiv only                   | Medium    | Maybe later   | Topology-oriented prompting is interesting but not yet peer-reviewed. |
| Learning and Editing Universal Graph Prompt Tuning via RL    | 2025 | arXiv only                   | Medium    | No for now    | Too new and not yet established.                             |
| Robust Graph Fine-Tuning with Adversarial Graph Prompting    | 2026 | arXiv only                   | Medium    | No for now    | Robustness-specific, preprint-only.                          |
| When Prompting Meets Spiking                                 | 2026 | arXiv only                   | Low       | No            | Too specialized and too early.                               |
| MAGPrompt                                                    | 2026 | arXiv only                   | Medium    | Maybe later   | Interesting message-passing prompt mechanism.                |
| GP2F                                                         | 2026 | arXiv only                   | Medium    | Maybe later   | Cross-domain adaptation is relevant, but too early.          |
| Unsupervised Prompting for Graph Neural Networks             | 2025 | arXiv only                   | Medium    | Maybe later   | Extra method found outside the local folder; interesting because it removes label supervision, but not yet peer-reviewed. |

## Concrete Replacement Suggestions

If the table size should stay roughly the same, use the following replacement order.

1. Replace ULTRA-DP with Inductive Graph Alignment Prompt (WWW 2024).
2. Replace SGL-PT with RELIEF (KDD 2025).
3. Replace PGCL with DAGPrompT (WWW 2025).
4. If one more slot is needed:
   - replace SAP with GraphPrompter (ICDE 2025) if graph in-context learning should be represented;
   - otherwise replace SAP with Pre-Training and Prompting for Few-Shot Node Classification on TAGs (KDD 2024) if TAG methods should be represented in the main table.

## Suggested Minimal Update Path

If the goal is a conservative but clearly more up-to-date table, add exactly these three:

- Inductive Graph Alignment Prompt (WWW 2024)
- RELIEF (KDD 2025)
- DAGPrompT (WWW 2025)

If the goal is a broader 2026 update, add two more:

- GraphPrompter (ICDE 2025)
- Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs (KDD 2024)

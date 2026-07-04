# Zotero/BibTeX Citation Audit - 2026-04-28

This note records the citation metadata cleanup applied to `tex/zotero.bib` and the intended synchronization target in Zotero.

## Scope

- Source file audited: `tex/zotero.bib`
- Initial entries: 249
- Final entries after cleanup: 245
- Main external checks used: arXiv, Crossref, DBLP, OpenReview, DOI resolver
- Build verification: English paper compiled successfully from `tex/` with `latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build 0.main.tex`

## Duplicate Entries Removed

The following duplicate BibTeX entries were removed from `tex/zotero.bib`:

| Removed key | Kept key | Reason |
|---|---|---|
| `chen2024temporal` | `chen2024prompt` | Same arXiv paper, duplicate title. Kept the key used by the main text. |
| `hu2024spatiotemporal` | `hu_prompt-based_2024` | Same paper; kept the formal CIKM 2024 entry with DOI and pages. |
| `fu_edge_2024` | `fu2025edge` | Same ICLR 2025 paper; kept the concise entry used by the main text. |
| `huang_one_2025` | `huang2025oneprompt` | Same UniPrompt paper; kept the key used by the main text. |

## Corrected Entries

| Key | Change |
|---|---|
| `sun2023graph` | Added arXiv ID `2311.16534`, DOI `10.48550/arXiv.2311.16534`, and arXiv URL. |
| `chen2024prompt` | Corrected author `Zhao, Yinglong` to `Zhao, Feng`; added arXiv ID and URL. |
| `huang2025oneprompt` | Normalized title casing and added OpenReview URL. |
| `liu2023gitmol` | Added missing author `Tao, Jun`. |
| `luo2020progressive` | Corrected title to `Source-Free Progressive Graph Learning for Open-Set Domain Adaptation`; added missing author `Chen, Zhuoxiao`; added volume, number, and pages. |
| `chai2023graphllm` | Updated final publication year to 2026 and added IEEE Transactions on Big Data volume/number/pages. |
| `yi2023contrastive` | Updated from abbreviated/preprint-like metadata to ACM TOIS 2024 metadata; added DOI, volume, number, and pages. |
| `yang2023datacentric` | Replaced incomplete author list with Crossref author list; added IEEE Transactions on Big Data volume/number/pages. |
| `anonymous2023decoupling` | Replaced anonymous under-review metadata with ICLR 2024 metadata and real authors; added OpenReview URL. |
| `anonymous2023graph` | Replaced anonymous under-review metadata with AAAI 2024 metadata; added real authors, volume, number, pages, DOI. |
| `anonymous2023when` | Replaced anonymous under-review metadata with ICLR 2024 metadata and real authors; added OpenReview URL. |
| `zhu2023graphcontrol` | Added missing author `Jiao, Dian`; added pages. |

## Validation Results

- Normalized duplicate-title scan: 0 duplicates remaining.
- Anonymous / under-review metadata scan: 0 remaining matches.
- LaTeX build from `tex/`: completed successfully and produced `tex/build/0.main.pdf`.
- Root-level build command from `AGENTS.md` still fails because `mydef.sty` is resolved relative to `tex/`; this is unrelated to the bibliography changes.

## Zotero Synchronization Plan

The Zotero library should be synchronized so that items in collection path `GPL/zotero` match the corrected metadata above. Duplicate Zotero items corresponding to the removed BibTeX keys should be reviewed and either merged or removed from that collection, while retained items should be updated in place.

## Zotero Synchronization Completed

The local Zotero database `/Users/river/Zotero/zotero.sqlite` was backed up before editing:

- Backup: `/Users/river/Zotero/zotero.sqlite.gpl-bib-sync-1777361067.bak`

Zotero contained two child collections named `zotero` under `GPL`:

- `GPL/zotero` with collection key `4LMKXTQV`
- `GPL/zotero` with collection key `N48BZH5I`

Both collections contained duplicate copies of the affected items, so both copies were updated. No Zotero item was deleted or merged.

Updated Zotero item pairs:

| BibTeX key | Zotero item IDs updated |
|---|---|
| `sun2023graph` | 328, 507 |
| `chen2024prompt` | 326, 505 |
| `liu2023gitmol` | 294, 473 |
| `luo2020progressive` | 270, 448 |
| `chai2023graphllm` | 261, 437 |
| `yi2023contrastive` | 227, 403 |
| `yang2023datacentric` | 223, 398 |
| `anonymous2023decoupling` | 205, 379 |
| `anonymous2023graph` | 204, 378 |
| `anonymous2023when` | 176, 347 |
| `zhu2023graphcontrol` | 164, 335 |

Post-update checks:

- Zotero SQLite integrity check: `ok`
- Anonymous creators remaining in updated Zotero items: 0
- `chen2024prompt` now has `Feng Zhao` in both Zotero copies.
- `liu2023gitmol` now has `Jun Tao` in both Zotero copies.
- `anonymous2023decoupling`, `anonymous2023graph`, and `anonymous2023when` are now real conference-paper entries rather than anonymous under-review entries.

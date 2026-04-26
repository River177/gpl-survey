#!/usr/bin/env python3
"""Import recent application papers into Zotero from docs/research/6.Applications_recent_literature.md"""

import os
import sys

# Load .env credentials
with open('.env') as f:
    for line in f:
        if '=' in line and not line.startswith('#'):
            k, v = line.strip().split('=', 1)
            os.environ[k] = v

from pyzotero import Zotero
import time

zot = Zotero(
    library_id=os.environ['ZOTERO_LIBRARY_ID'],
    library_type='user',
    api_key=os.environ['ZOTERO_API_KEY']
)

# Verify connection
user = zot.key_info()
print(f"Connected. Library ID: {os.environ['ZOTERO_LIBRARY_ID']}")

# Papers to import based on 6.Applications_recent_literature.md
# Format: (itemType, title, year, venue, url, creators, key)
papers = [
    {
        'itemType': 'conferencePaper',
        'title': 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation',
        'creators': [{'creatorType': 'author', 'lastName': 'Yang'}],
        'year': '2024',
        'conferenceName': 'WWW 2024',
        'url': 'https://hub.hku.hk/handle/10722/355968',
        'key': 'yang2024graphpro',
        'tags': ['recommender-systems', 'graph-prompt', 'application']
    },
    {
        'itemType': 'conferencePaper',
        'title': 'GPT4Rec: Graph Prompt Tuning for Streaming Recommendation',
        'creators': [{'creatorType': 'author', 'lastName': 'Zhang'}],
        'year': '2024',
        'conferenceName': 'SIGIR 2024',
        'url': 'https://researchportal.hkust.edu.hk/en/publications/gpt4rec-graph-prompt-tuning-for-streaming-recommendation-2/',
        'key': 'zhang2024gpt4rec',
        'tags': ['recommender-systems', 'graph-prompt', 'streaming', 'application']
    },
    {
        'itemType': 'journalArticle',
        'title': 'PT4Rec: a universal prompt-tuning framework for graph contrastive learning-based recommendations',
        'creators': [{'creatorType': 'author', 'lastName': 'Xiao'}],
        'year': '2025',
        'publication': 'Machine Learning',
        'url': 'https://link.springer.com/article/10.1007/s10994-024-06658-0',
        'key': 'xiao2025pt4rec',
        'tags': ['recommender-systems', 'graph-prompt', 'contrastive-learning', 'application']
    },
    {
        'itemType': 'journalArticle',
        'title': 'Candidate-aware graph prompt-tuning for recommendation',
        'creators': [{'creatorType': 'author', 'lastName': 'Li'}],
        'year': '2025',
        'publication': 'Pattern Recognition',
        'url': 'https://www.sciencedirect.com/science/article/pii/S0031320325003930',
        'key': 'li2025cgpt',
        'tags': ['recommender-systems', 'graph-prompt', 'application']
    },
    {
        'itemType': 'conferencePaper',
        'title': 'Node-Time Conditional Prompt Learning in Dynamic Graphs',
        'creators': [{'creatorType': 'author', 'lastName': 'Yu'}],
        'year': '2025',
        'conferenceName': 'ICLR 2025',
        'url': 'https://proceedings.iclr.cc/paper_files/paper/2025/hash/f342338902ea2d8aaf3af94b941ebba6-Abstract-Conference.html',
        'key': 'yu2025dygprompt',
        'tags': ['social-networks', 'dynamic-graphs', 'graph-prompt', 'application']
    },
    {
        'itemType': 'conferencePaper',
        'title': 'UniGAD: Unifying Multi-level Graph Anomaly Detection',
        'creators': [{'creatorType': 'author', 'lastName': 'Lin'}],
        'year': '2024',
        'conferenceName': 'NeurIPS 2024',
        'url': 'https://proceedings.neurips.cc/paper_files/paper/2024/hash/f57de20ab7bb1540bcac55266ebb5401-Abstract-Conference.html',
        'key': 'lin2024unigad',
        'tags': ['social-networks', 'anomaly-detection', 'graph', 'application']
    },
    {
        'itemType': 'conferencePaper',
        'title': 'KnowGPT: Knowledge Graph based Prompting for Large Language Models',
        'creators': [{'creatorType': 'author', 'lastName': 'Zhang'}],
        'year': '2024',
        'conferenceName': 'NeurIPS 2024',
        'url': 'https://arxiv.org/abs/2312.06185',
        'key': 'zhang2024knowgpt',
        'tags': ['knowledge-graph', 'LLM', 'prompting', 'application']
    },
    {
        'itemType': 'preprint',
        'title': 'GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning',
        'creators': [{'creatorType': 'author', 'lastName': 'Mavromatis'}],
        'year': '2024',
        'url': 'https://arxiv.org/abs/2405.20139',
        'key': 'mavromatis2024gnnrag',
        'tags': ['knowledge-graph', 'RAG', 'LLM', 'graph', 'application']
    },
    {
        'itemType': 'journalArticle',
        'title': 'APKGC: An adaptive and prompt-tuning framework for knowledge graph completion',
        'creators': [{'creatorType': 'author', 'lastName': 'Zhang'}],
        'year': '2026',
        'publication': 'Knowledge-Based Systems',
        'url': 'https://www.sciencedirect.com/science/article/pii/S0950705125019884',
        'key': 'zhang2026apkgc',
        'tags': ['knowledge-graph', 'knowledge-graph-completion', 'prompt-tuning', 'application']
    },
    {
        'itemType': 'conferencePaper',
        'title': 'MOAT: Graph Prompting for 3D Molecular Graphs',
        'creators': [{'creatorType': 'author', 'lastName': 'Long'}],
        'year': '2024',
        'conferenceName': 'CIKM 2024',
        'url': 'https://dl.acm.org/doi/10.1145/3627673.3679628',
        'key': 'long2024moat',
        'tags': ['biology', 'molecular-graphs', '3D', 'graph-prompt', 'application']
    },
    {
        'itemType': 'conferencePaper',
        'title': 'DDIPrompt: Drug-Drug Interaction Event Prediction based on Graph Prompt Learning',
        'creators': [{'creatorType': 'author', 'lastName': 'Wang'}],
        'year': '2024',
        'conferenceName': 'CIKM 2024',
        'url': 'https://arxiv.org/abs/2402.11472',
        'key': 'wang2024ddiprompt',
        'tags': ['biology', 'drug-interaction', 'graph-prompt', 'application']
    },
    {
        'itemType': 'conferencePaper',
        'title': 'Learning to Predict Mutation Effects of Protein-Protein Interactions by Microenvironment-aware Hierarchical Prompt Learning',
        'creators': [{'creatorType': 'author', 'lastName': 'Wu'}],
        'year': '2024',
        'conferenceName': 'ICML 2024',
        'url': 'https://arxiv.org/abs/2405.10348',
        'key': 'wu2024promptddg',
        'tags': ['biology', 'protein', 'mutation', 'prompt-learning', 'application']
    },
    {
        'itemType': 'journalArticle',
        'title': 'Fine-grained multimodal molecular pretraining via prompt learning',
        'creators': [{'creatorType': 'author', 'lastName': 'Li'}],
        'year': '2025',
        'publication': 'Knowledge-Based Systems',
        'url': 'https://www.sciencedirect.com/science/article/pii/S0950705125014200',
        'key': 'li2025molfineprompt',
        'tags': ['biology', 'molecular', 'multimodal', 'prompt-learning', 'application']
    },
    {
        'itemType': 'journalArticle',
        'title': 'FFCL-KGC: Feature fusion contrastive learning via dual prompting for knowledge graph completion',
        'creators': [{'creatorType': 'author', 'lastName': 'Zhang'}],
        'year': '2026',
        'publication': 'Expert Systems with Applications',
        'url': 'https://www.sciencedirect.com/science/article/pii/S09507417425037327',
        'key': 'zhang2026ffclkgc',
        'tags': ['knowledge-graph', 'knowledge-graph-completion', 'dual-prompt', 'application']
    },
    {
        'itemType': 'preprint',
        'title': 'Bridging Molecular Graphs and Large Language Models',
        'creators': [{'creatorType': 'author', 'lastName': 'Graph2Token'}],
        'year': '2025',
        'url': 'https://arxiv.org/abs/2503.03135',
        'key': 'graph2token2025',
        'tags': ['biology', 'molecular', 'LLM', 'graph-language', 'application']
    },
]

# Check which papers already exist in Zotero by URL
print("\n--- Checking existing items by URL ---")
existing_urls = set()
all_items = zot.everything(zot.items(limit=1000))
for item in all_items:
    url = item['data'].get('url', '')
    if url:
        existing_urls.add(url)
print(f"Total existing items: {len(all_items)}, checked {len(existing_urls)} URLs")

# Import missing papers
print("\n--- Importing missing papers ---")
created = []
skipped = []
errors = []

for paper in papers:
    url = paper['url']
    key = paper['key']
    if url in existing_urls:
        print(f"  SKIP (exists): {key} - {paper['title']}")
        skipped.append(key)
        continue

    template = zot.item_template(paper['itemType'])
    template['title'] = paper['title']
    template['creators'] = [
        {**c, 'firstName': ''} if 'lastName' in c else c
        for c in paper['creators']
    ]
    template['url'] = paper['url']
    # Skip tags for now - will add manually later
    # template['tags'] = [{'tag': t} for t in paper.get('tags', [])]
    if 'year' in paper:
        template['date'] = paper['year']
    if 'conferenceName' in paper:
        template['conferenceName'] = paper['conferenceName']
    if 'publication' in paper:
        template['publicationTitle'] = paper['publication']

    try:
        result = zot.create_items([template])
        if result['success']:
            created_key = list(result['success'].values())[0]
            created.append((key, created_key, paper['title']))
            print(f"  CREATED: {key} -> {created_key} - {paper['title']}")
        else:
            errors.append((key, paper['title'], result))
            print(f"  ERROR: {key} - {paper['title']}: {result}")
    except Exception as e:
        errors.append((key, paper['title'], str(e)))
        print(f"  EXCEPTION: {key} - {paper['title']}: {e}")

    time.sleep(0.3)  # Rate limiting

print(f"\n--- Summary ---")
print(f"  Already existed: {len(skipped)}")
print(f"  Newly created: {len(created)}")
print(f"  Errors: {len(errors)}")
if errors:
    print("\nErrors:")
    for key, title, err in errors:
        print(f"  {key}: {title}")
        print(f"    -> {err}")

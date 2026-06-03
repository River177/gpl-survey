"""Generate the Top-15 title-keyword bar chart (top_keywords_bar.pdf/.eps).

Extracts keywords from the titles of the references cited in tex/*.tex and
renders a horizontal bar chart of the 15 most frequent keywords.

Unlike a naive word-frequency count, this script treats well-known multi-word
concepts (e.g. "Graph Neural Network", "Large Language Model", "Prompt Tuning")
as single keywords via greedy longest-phrase matching, and avoids double
counting their constituent words as separate unigrams.

Usage:
    python3 scripts/gen_top_keywords.py
"""
import os
import re
import sys
from collections import Counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paper_utils import collect_cited_keys, parse_bib  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX_DIR = os.path.join(ROOT, "tex")
BIB_PATH = os.path.join(TEX_DIR, "zotero.bib")
OUT_PDF = os.path.join(TEX_DIR, "pic", "top_keywords_bar.pdf")
OUT_EPS = os.path.join(TEX_DIR, "pic", "top_keywords_bar.eps")

TOP_N = 15

STOPWORDS = set("""
a an the of for and or to in on with via using use based toward towards from
into over under as at by is are be can do does how what why when where which
your you we our their its it this that these those more less most are
""".split())

# Generic words that are not informative keywords on their own.
GENERIC = set("""
learning model models method methods approach approaches framework frameworks
study survey paper analysis problem problems task tasks system systems
view views level levels work works general generic novel beyond comprehensive
empirical towards unifying enhancing improving understanding exploring
""".split())

# Singularize / normalize tokens BEFORE phrase matching so plural and variant
# forms collapse onto a single canonical token.
SING = {
    "graphs": "graph", "networks": "network", "models": "model",
    "prompts": "prompt", "prompting": "prompt",
    "representations": "representation", "embeddings": "embedding",
    "transformers": "transformer", "languages": "language",
    "classifications": "classification", "adaptations": "adaptation",
    "predictions": "prediction", "augmentations": "augmentation",
    "applications": "application", "recommendations": "recommendation",
    "recommender": "recommendation", "strategies": "strategy",
    "gnns": "gnn", "llms": "llm",
    "pretraining": "pre-training", "pre-trained": "pre-training",
    "pretrained": "pre-training", "pretrain": "pre-training",
}

# Multi-word concepts (tokens already singularized). Matched greedily,
# longest first. Value = display label.
PHRASES = {
    ("graph", "neural", "network"): "Graph Neural Network",
    ("graph", "contrastive", "learning"): "Graph Contrastive Learning",
    ("large", "language", "model"): "Large Language Model",
    ("graph", "foundation", "model"): "Graph Foundation Model",
    ("self-supervised", "learning"): "Self-Supervised Learning",
    ("neural", "network"): "Neural Network",
    ("language", "model"): "Language Model",
    ("prompt", "tuning"): "Prompt Tuning",
    ("prompt", "learning"): "Prompt Learning",
    ("graph", "prompt"): "Graph Prompt",
    ("contrastive", "learning"): "Contrastive Learning",
    ("representation", "learning"): "Representation Learning",
    ("transfer", "learning"): "Transfer Learning",
    ("heterogeneous", "graph"): "Heterogeneous Graph",
    ("knowledge", "graph"): "Knowledge Graph",
    ("foundation", "model"): "Foundation Model",
    ("text-attributed", "graph"): "Text-Attributed Graph",
    ("node", "classification"): "Node Classification",
    ("link", "prediction"): "Link Prediction",
    ("domain", "adaptation"): "Domain Adaptation",
    ("question", "answering"): "Question Answering",
    ("data", "augmentation"): "Data Augmentation",
}
MAX_PHRASE = max(len(k) for k in PHRASES)

# Single tokens that map directly to a (possibly multi-word) display label,
# e.g. consolidating abbreviations with their expanded concept.
UNI_MAP = {
    "gnn": "Graph Neural Network",
    "llm": "Large Language Model",
    "pre-training": "Pre-training",
    "self-supervised": "Self-Supervised",
    "few-shot": "Few-Shot",
    "zero-shot": "Zero-Shot",
    "in-context": "In-Context Learning",
}


def _words(title):
    title = title.lower().replace("{", "").replace("}", "")
    tokens = re.findall(r"[a-z][a-z0-9\-]*[a-z0-9]|[a-z]", title)
    return [SING.get(t, t) for t in tokens]


def extract_keywords(title):
    words = _words(title)
    out = []
    i = 0
    n = len(words)
    while i < n:
        matched = False
        for L in range(MAX_PHRASE, 1, -1):
            if i + L <= n:
                key = tuple(words[i:i + L])
                if key in PHRASES:
                    out.append(PHRASES[key])
                    i += L
                    matched = True
                    break
        if matched:
            continue
        w = words[i]
        i += 1
        if w in UNI_MAP:
            out.append(UNI_MAP[w])
            continue
        if w in STOPWORDS or w in GENERIC or len(w) < 2:
            continue
        out.append(w[:1].upper() + w[1:])
    return out


def compute_counts():
    keys = collect_cited_keys(TEX_DIR)
    bib = parse_bib(BIB_PATH)
    counts = Counter()
    for k in keys:
        if k in bib and bib[k].get("title"):
            # count each keyword at most once per title
            counts.update(set(extract_keywords(bib[k]["title"])))
    return counts


def main():
    counts = compute_counts()
    top = counts.most_common(TOP_N)

    labels = [w for w, _ in top][::-1]
    values = [n for _, n in top][::-1]

    fig, ax = plt.subplots(figsize=(9, 6))
    bars = ax.barh(range(len(values)), values, color="#4C72B0",
                   edgecolor="white")
    ax.set_yticks(range(len(values)))
    ax.set_yticklabels(labels, fontsize=14, fontweight="bold")
    ax.set_xlabel("Frequency in titles", fontsize=14, fontweight="bold")
    ax.tick_params(axis="x", labelsize=12)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for b, v in zip(bars, values):
        ax.text(v + max(values) * 0.01, b.get_y() + b.get_height() / 2,
                str(v), va="center", ha="left", fontsize=12, fontweight="bold")
    ax.set_xlim(0, max(values) * 1.12)
    plt.tight_layout()

    os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
    fig.savefig(OUT_PDF, bbox_inches="tight")
    fig.savefig(OUT_EPS, bbox_inches="tight", format="eps")
    print(f"Wrote {OUT_PDF} and {OUT_EPS}")
    for w, n in top:
        print(f"  {n:3d}  {w}")


if __name__ == "__main__":
    main()

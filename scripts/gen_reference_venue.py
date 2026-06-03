"""Generate the venue-distribution pie chart (reference_venue.pdf).

Counts canonical venues over the references actually cited in tex/*.tex and
renders a pie chart matching the survey style (bold labels "Venue, X%").

Usage:
    python3 scripts/gen_reference_venue.py
"""
import os
import sys
from collections import Counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paper_utils import collect_cited_keys, parse_bib, canonical_venue  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX_DIR = os.path.join(ROOT, "tex")
BIB_PATH = os.path.join(TEX_DIR, "zotero.bib")
OUT_PDF = os.path.join(TEX_DIR, "pic", "reference_venue.pdf")

# Venues with share below this fraction are merged into "Others".
OTHER_THRESHOLD = 0.012

PALETTE = [
    "#aec7e8", "#ffbb78", "#98df8a", "#9e9ac8", "#c5b0d5", "#f7b6d2",
    "#c49c94", "#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd", "#8c564b",
    "#17becf", "#bcbd22", "#7f7f7f", "#d62728", "#e377c2", "#8c6d31",
    "#393b79", "#637939", "#843c39", "#7b4173",
]


def compute_counts():
    keys = collect_cited_keys(TEX_DIR)
    bib = parse_bib(BIB_PATH)
    counts = Counter()
    for k in keys:
        if k in bib:
            counts[canonical_venue(bib[k])] += 1
    total = sum(counts.values())

    # Merge tiny venues (and any leftover 'Others'/'Unknown') into 'Others'.
    big, others = {}, 0
    for venue, n in counts.items():
        if venue in ("Others", "Unknown") or n / total < OTHER_THRESHOLD:
            others += n
        else:
            big[venue] = n
    if others:
        big["Others"] = big.get("Others", 0) + others

    # Sort by count desc, but keep arXiv first (largest) and Others last.
    items = sorted(big.items(), key=lambda x: (-x[1], x[0]))
    items = [it for it in items if it[0] != "Others"]
    if "Others" in big:
        items.append(("Others", big["Others"]))
    return items, total


def main():
    items, total = compute_counts()
    labels = [v for v, _ in items]
    sizes = [n for _, n in items]
    pct = [100 * n / total for n in sizes]
    wedge_labels = [f"{lab}, {p:.0f}%" for lab, p in zip(labels, pct)]

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, _texts = ax.pie(
        sizes,
        startangle=90,
        counterclock=False,
        colors=[PALETTE[i % len(PALETTE)] for i in range(len(sizes))],
        wedgeprops={"linewidth": 0.5, "edgecolor": "white"},
    )

    # Place bold labels with leader lines (good for thin slices).
    for w, lab in zip(wedges, wedge_labels):
        ang = (w.theta2 + w.theta1) / 2.0
        import math
        x = math.cos(math.radians(ang))
        y = math.sin(math.radians(ang))
        ha = "left" if x >= 0 else "right"
        ax.annotate(
            lab,
            xy=(x, y),
            xytext=(1.25 * x, 1.18 * y),
            ha=ha, va="center",
            fontsize=13, fontweight="bold",
            arrowprops={"arrowstyle": "-", "color": "0.4", "lw": 0.8,
                        "connectionstyle": "arc3"},
        )

    ax.set_aspect("equal")
    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
    fig.savefig(OUT_PDF, bbox_inches="tight")
    print(f"Wrote {OUT_PDF}")
    print(f"Total cited refs: {total}")
    for lab, p, n in zip(labels, pct, sizes):
        print(f"  {n:3d} ({p:4.1f}%)  {lab}")


if __name__ == "__main__":
    main()

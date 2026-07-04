#!/usr/bin/env python3
"""Generate controlled-text redraws for the graph prompt survey figures.

The outputs are vector PDFs/SVGs with editable/searchable text, plus PNG
previews for quick review. The script intentionally avoids AI-rendered text,
third-party logos, screenshots, and photographic assets.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "tmp" / "mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / "tmp" / "xdg-cache"))

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (
    Circle,
    FancyArrowPatch,
    FancyBboxPatch,
    PathPatch,
    Polygon,
    Rectangle,
    RegularPolygon,
)
from matplotlib.path import Path

OUT = ROOT / "tex" / "pic" / "redraw-controlled"

COL = {
    "ink": "#202124",
    "muted": "#5F6368",
    "grid": "#D7DCE2",
    "blue": "#4C72B0",
    "blue2": "#DDE9F7",
    "teal": "#2A9D8F",
    "teal2": "#DFF3EF",
    "green": "#55A868",
    "green2": "#E5F2E1",
    "amber": "#E69F00",
    "amber2": "#FFF2CC",
    "coral": "#C44E52",
    "coral2": "#F8DFDF",
    "purple": "#8172B3",
    "purple2": "#ECE6F6",
    "peach": "#F8E7D8",
    "snow": "#71C7C9",
    "light": "#F8FAFC",
}


mpl.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 7,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "axes.linewidth": 0,
        "savefig.facecolor": "white",
        "savefig.edgecolor": "white",
    }
)


def canvas(width: float, height: float, figsize: tuple[float, float] | None = None):
    fig = plt.figure(figsize=figsize or (width, height), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def save(fig, name: str):
    OUT.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "svg", "png"):
        path = OUT / f"{name}.{ext}"
        kwargs = {"bbox_inches": "tight", "pad_inches": 0.015}
        if ext == "png":
            kwargs["dpi"] = 450
        fig.savefig(path, **kwargs)
    plt.close(fig)


def txt(ax, x, y, s, size=7, weight="normal", color=None, ha="center", va="center", **kw):
    return ax.text(
        x,
        y,
        s,
        fontsize=size,
        fontweight=weight,
        color=color or COL["ink"],
        ha=ha,
        va=va,
        linespacing=1.08,
        **kw,
    )


def box(
    ax,
    x,
    y,
    w,
    h,
    fc="white",
    ec=None,
    lw=0.75,
    radius=0.04,
    ls="-",
    alpha=1.0,
    zorder=1,
):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.01,rounding_size={radius}",
        fc=fc,
        ec=ec or COL["ink"],
        lw=lw,
        linestyle=ls,
        alpha=alpha,
        zorder=zorder,
    )
    ax.add_patch(patch)
    return patch


def rect(ax, x, y, w, h, fc="white", ec=None, lw=0.7, ls="-", alpha=1.0, zorder=1):
    patch = Rectangle(
        (x, y),
        w,
        h,
        fc=fc,
        ec=ec or COL["ink"],
        lw=lw,
        linestyle=ls,
        alpha=alpha,
        zorder=zorder,
    )
    ax.add_patch(patch)
    return patch


def arrow(ax, x1, y1, x2, y2, color=None, lw=0.8, ms=7, style="-|>", ls="-", rad=0.0, zorder=3):
    patch = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle=style,
        mutation_scale=ms,
        color=color or COL["muted"],
        lw=lw,
        linestyle=ls,
        connectionstyle=f"arc3,rad={rad}",
        zorder=zorder,
    )
    ax.add_patch(patch)
    return patch


def line(ax, x1, y1, x2, y2, color=None, lw=0.7, ls="-", zorder=2):
    ax.plot([x1, x2], [y1, y2], color=color or COL["ink"], lw=lw, ls=ls, zorder=zorder)


def dashed_box(ax, x, y, w, h, fc="white", ec=None, lw=0.75, radius=0.04):
    return box(ax, x, y, w, h, fc=fc, ec=ec or COL["ink"], lw=lw, radius=radius, ls=(0, (3, 2)))


def draw_feature_bars(ax, x, y, w=0.08, h=0.30, n=4, color=None, ec=None):
    step = h / n
    for i in range(n):
        rect(
            ax,
            x,
            y + i * step,
            w,
            step * 0.92,
            fc=(color or COL["green2"]) if i % 2 else "#F2F5F1",
            ec=ec or COL["ink"],
            lw=0.45,
        )


def graph_points(x, y, w, h):
    pts = np.array(
        [
            [0.50, 0.52],
            [0.26, 0.68],
            [0.70, 0.75],
            [0.15, 0.34],
            [0.42, 0.18],
            [0.78, 0.32],
        ]
    )
    return np.column_stack([x + pts[:, 0] * w, y + pts[:, 1] * h])


def draw_graph(
    ax,
    x,
    y,
    w,
    h,
    highlights: Iterable[int] | None = None,
    whole=False,
    edge_highlights: Sequence[tuple[int, int]] | None = None,
    node_fc="white",
    edge_color=None,
    lw=0.75,
    r=None,
    alpha=1.0,
):
    highlights = set(highlights or [])
    edge_highlights = set(tuple(sorted(e)) for e in (edge_highlights or []))
    pts = graph_points(x, y, w, h)
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (3, 4)]
    if whole:
        box(ax, x + 0.06 * w, y + 0.06 * h, 0.88 * w, 0.88 * h, fc=COL["green2"], ec=COL["green"], lw=0.55, radius=0.035, alpha=0.65)
    rr = r if r is not None else min(w, h) * 0.085
    for a, b in edges:
        e = tuple(sorted((a, b)))
        color = COL["coral"] if e in edge_highlights else (edge_color or COL["ink"])
        line(ax, pts[a, 0], pts[a, 1], pts[b, 0], pts[b, 1], color=color, lw=lw if e not in edge_highlights else lw * 1.45, zorder=2)
    for i, (px, py) in enumerate(pts):
        if i in highlights:
            box(ax, px - rr * 1.8, py - rr * 1.5, rr * 3.6, rr * 3.0, fc=COL["green2"], ec=COL["green"], lw=0.6, radius=0.025, ls=(0, (3, 2)), zorder=2.5)
        ax.add_patch(Circle((px, py), rr, fc=node_fc, ec=COL["ink"], lw=lw, zorder=3, alpha=alpha))
    return pts


def draw_embedding(ax, x, y, w, h, count=4):
    gap = w * 0.08
    bw = (w - gap * (count - 1)) / count
    for i in range(count):
        rect(ax, x + i * (bw + gap), y, bw, h, fc="white", ec=COL["ink"], lw=0.55)
        for j in range(4):
            shade = 0.18 + 0.16 * (j + i % 2)
            color = (1.0, 0.74 + shade * 0.15, 0.12 + shade * 0.25)
            rect(ax, x + i * (bw + gap), y + j * h / 4, bw, h / 4, fc=color, ec=COL["ink"], lw=0.35)


def draw_neural_net(ax, x, y, w, h, color=None):
    layers = [3, 4, 3]
    xs = np.linspace(x + 0.12 * w, x + 0.88 * w, len(layers))
    nodes = []
    for xi, n in zip(xs, layers):
        ys = np.linspace(y + 0.18 * h, y + 0.82 * h, n)
        layer = [(xi, yy) for yy in ys]
        nodes.append(layer)
    for a, b in zip(nodes[:-1], nodes[1:]):
        for p in a:
            for q in b:
                line(ax, p[0], p[1], q[0], q[1], color=COL["ink"], lw=0.45)
    for layer in nodes:
        for px, py in layer:
            ax.add_patch(Circle((px, py), min(w, h) * 0.055, fc="white", ec=color or "#888888", lw=0.75, zorder=3))


def draw_hex(ax, x, y, r=0.06, color=None):
    ax.add_patch(RegularPolygon((x, y), 6, radius=r, orientation=np.pi / 6, fc=color or COL["amber"], ec=color or COL["amber"], lw=0.5, zorder=4))


def draw_snowflake(ax, x, y, r=0.055, color=None):
    c = color or COL["snow"]
    for a in np.linspace(0, np.pi, 3, endpoint=False):
        dx, dy = np.cos(a) * r, np.sin(a) * r
        line(ax, x - dx, y - dy, x + dx, y + dy, color=c, lw=0.8, zorder=4)
    ax.add_patch(Circle((x, y), r * 0.14, fc=c, ec=c, lw=0, zorder=4))


def draw_flame(ax, x, y, s=0.11, color=None):
    c = color or COL["coral"]
    verts = [
        (x, y - s * 0.55),
        (x - s * 0.48, y - s * 0.18),
        (x - s * 0.20, y + s * 0.22),
        (x - s * 0.08, y + s * 0.55),
        (x + s * 0.12, y + s * 0.18),
        (x + s * 0.46, y - s * 0.05),
        (x, y - s * 0.55),
    ]
    codes = [Path.MOVETO] + [Path.CURVE3] * 5 + [Path.CURVE3]
    ax.add_patch(PathPatch(Path(verts, codes), fc=c, ec=c, lw=0.3, zorder=4))


def draw_image_icon(ax, x, y, w, h):
    rect(ax, x, y, w, h, fc="white", ec=COL["blue"], lw=0.6)
    tri1 = Polygon([(x + 0.10 * w, y + 0.18 * h), (x + 0.44 * w, y + 0.65 * h), (x + 0.70 * w, y + 0.18 * h)], fc="#9DB8D4", ec=COL["blue"], lw=0.4)
    tri2 = Polygon([(x + 0.42 * w, y + 0.18 * h), (x + 0.70 * w, y + 0.55 * h), (x + 0.93 * w, y + 0.18 * h)], fc="#668EB8", ec=COL["blue"], lw=0.4)
    ax.add_patch(tri1)
    ax.add_patch(tri2)
    ax.add_patch(Circle((x + 0.22 * w, y + 0.78 * h), min(w, h) * 0.08, fc=COL["amber"], ec=COL["amber"], lw=0))


def draw_doc_icon(ax, x, y, w, h, color=None):
    rect(ax, x, y, w, h, fc="white", ec=color or COL["muted"], lw=0.55)
    for i in range(4):
        line(ax, x + 0.16 * w, y + (0.25 + 0.14 * i) * h, x + 0.84 * w, y + (0.25 + 0.14 * i) * h, color=color or COL["muted"], lw=0.45)


def draw_social_icon(ax, x, y, w, h):
    pts = [(0.23, 0.65), (0.55, 0.72), (0.74, 0.46), (0.43, 0.34), (0.20, 0.22)]
    pts = [(x + px * w, y + py * h) for px, py in pts]
    for a, b in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 3), (1, 3)]:
        line(ax, pts[a][0], pts[a][1], pts[b][0], pts[b][1], color=COL["teal"], lw=0.6)
    for px, py in pts:
        ax.add_patch(Circle((px, py), min(w, h) * 0.08, fc=COL["teal"], ec="white", lw=0.45, zorder=3))


def draw_molecule_icon(ax, x, y, w, h):
    pts = [(0.22, 0.55), (0.45, 0.75), (0.70, 0.62), (0.58, 0.35), (0.33, 0.30)]
    pts = [(x + px * w, y + py * h) for px, py in pts]
    for a, b in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)]:
        line(ax, pts[a][0], pts[a][1], pts[b][0], pts[b][1], color=COL["ink"], lw=0.55)
    colors = [COL["purple"], COL["blue"], COL["amber"], COL["coral"], "white"]
    for (px, py), fc in zip(pts, colors):
        ax.add_patch(Circle((px, py), min(w, h) * 0.065, fc=fc, ec=COL["ink"], lw=0.45, zorder=3))


def panel_title(ax, x, y, label):
    txt(ax, x, y, label, size=6.4, weight="bold")


def figure1():
    fig, ax = canvas(3.65, 1.85, figsize=(7.25, 3.55))
    y0, ph = 0.25, 1.35
    gaps = [1.18, 1.18]
    for gx in gaps:
        line(ax, gx, 0.22, gx, 1.68, color=COL["grid"], lw=0.55, ls="--")

    # (a) Cross-modalities
    x = 0.06
    rows = [1.20, 0.82, 0.44]
    labels = [("Image", COL["blue"], COL["blue2"]), ("Text", COL["teal"], COL["teal2"]), ("Graph", COL["amber"], COL["amber2"])]
    for (lab, ec, fc), yy in zip(labels, rows):
        box(ax, x, yy, 0.58, 0.27, fc=fc, ec=ec, lw=0.65, radius=0.035)
        if lab == "Image":
            draw_image_icon(ax, x + 0.06, yy + 0.06, 0.22, 0.14)
        elif lab == "Text":
            draw_doc_icon(ax, x + 0.07, yy + 0.06, 0.20, 0.15, color=COL["teal"])
        else:
            draw_doc_icon(ax, x + 0.07, yy + 0.08, 0.08, 0.14)
            draw_doc_icon(ax, x + 0.23, yy + 0.11, 0.08, 0.14)
            line(ax, x + 0.15, yy + 0.15, x + 0.23, yy + 0.18, color=COL["amber"], lw=0.5)
        txt(ax, x + 0.43, yy + 0.14, lab, size=5.6, weight="bold", color=ec)
    arrow(ax, x + 0.66, 1.34, x + 0.77, 1.34, color=COL["blue"], lw=0.7, ms=7)
    arrow(ax, x + 0.66, 0.95, x + 0.77, 0.95, color=COL["teal"], lw=0.7, ms=7)
    arrow(ax, x + 0.66, 0.55, x + 0.77, 0.55, color=COL["amber"], lw=0.7, ms=7)
    box(ax, x + 0.78, 0.80, 0.27, 0.25, fc=COL["blue2"], ec=COL["blue"], lw=0.55, radius=0.025)
    txt(ax, x + 0.915, 0.925, "Transfer", size=5.3, weight="bold", color=COL["blue"])
    panel_title(ax, x + 0.50, 0.10, "(a) Cross-modalities")

    # (b) Cross-domains
    x = 1.25
    cards = [
        ("Biology", COL["purple"], COL["purple2"], draw_molecule_icon),
        ("Knowledge", COL["blue"], COL["blue2"], None),
        ("Society", COL["teal"], COL["teal2"], draw_social_icon),
        ("Molecule", COL["amber"], COL["amber2"], draw_graph),
    ]
    positions = [(x + 0.03, 1.04), (x + 0.57, 1.04), (x + 0.03, 0.52), (x + 0.57, 0.52)]
    for (lab, ec, fc, fn), (cx, cy) in zip(cards, positions):
        box(ax, cx, cy, 0.48, 0.42, fc=fc, ec=ec, lw=0.65, radius=0.045)
        txt(ax, cx + 0.24, cy + 0.34, lab, size=5.2, weight="bold", color=ec)
        if fn is draw_graph:
            draw_graph(ax, cx + 0.10, cy + 0.07, 0.30, 0.22, r=0.025, lw=0.5)
        elif fn is None:
            ax.add_patch(Circle((cx + 0.24, cy + 0.18), 0.11, fc="white", ec=COL["muted"], lw=0.5))
            txt(ax, cx + 0.24, cy + 0.18, "W", size=8, weight="bold", color=COL["muted"])
        else:
            fn(ax, cx + 0.07, cy + 0.06, 0.34, 0.25)
    panel_title(ax, x + 0.52, 0.10, "(b) Cross-domains")

    # (c) Cross-tasks
    x = 2.43
    draw_graph(ax, x + 0.03, 0.83, 0.37, 0.45, r=0.032, lw=0.62)
    rows = [
        ("Graph-level", "Molecule\ninhibit HIV?", COL["purple"], 1.26, True, []),
        ("Edge-level", "Did Jobs\nfound Apple?", COL["teal"], 0.86, False, [(1, 2)]),
        ("Node-level", "Is this account\nmalicious?", COL["amber"], 0.46, False, []),
    ]
    for title, question, color, yy, whole, edges in rows:
        arrow(ax, x + 0.43, yy + 0.04, x + 0.56, yy + 0.04, color=color, lw=0.75, ms=7)
        draw_graph(ax, x + 0.59, yy - 0.12, 0.30, 0.27, highlights=[2] if title == "Node-level" else [], whole=whole, edge_highlights=edges, r=0.021, lw=0.46)
        txt(ax, x + 0.95, yy + 0.10, title, size=5.9, weight="bold", ha="left")
        line(ax, x + 0.95, yy + 0.04, x + 1.23, yy + 0.04, color=COL["ink"], lw=0.45)
        txt(ax, x + 0.95, yy - 0.10, question, size=5.0, ha="left", va="top", style="italic")
    panel_title(ax, x + 0.58, 0.10, "(c) Cross-tasks")
    save(fig, "fig1_three_challenges_controlled")


def draw_language_panel(ax, x, y, w, h, label=True):
    dashed_box(ax, x, y, w, h, fc="white", ec="#15345D", lw=0.65, radius=0.035)
    box(ax, x + 0.06 * w, y + 0.63 * h, 0.88 * w, 0.27 * h, fc=COL["amber2"], ec=COL["amber"], lw=0.6, radius=0.035)
    txt(ax, x + 0.13 * w, y + 0.82 * h, "Prompt", size=7.2, weight="bold", color=COL["amber"], ha="left")
    txt(ax, x + 0.08 * w, y + 0.75 * h, "Help me answer a multiple choice question", size=5.45, weight="bold", ha="left")
    txt(
        ax,
        x + 0.08 * w,
        y + 0.69 * h,
        "Question: Greenhouses are great for plants like\nA. Pizza    B. Lollipops    C. French beans",
        size=5.0,
        ha="left",
        va="top",
    )
    arrow(ax, x + 0.50 * w, y + 0.62 * h, x + 0.50 * w, y + 0.54 * h, color=COL["blue"], lw=0.8)
    box(ax, x + 0.10 * w, y + 0.39 * h, 0.80 * w, 0.14 * h, fc="#86B7AE", ec="#6FA99F", lw=0.5, radius=0.035)
    draw_graph(ax, x + 0.17 * w, y + 0.415 * h, 0.12 * w, 0.085 * h, r=0.013 * h, lw=0.45, node_fc="none", edge_color="white")
    txt(ax, x + 0.55 * w, y + 0.46 * h, "Pre-trained Large\nLanguage Model", size=7.0, weight="bold", color="white")
    arrow(ax, x + 0.50 * w, y + 0.38 * h, x + 0.50 * w, y + 0.30 * h, color=COL["blue"], lw=0.8)
    box(ax, x + 0.06 * w, y + 0.16 * h, 0.88 * w, 0.13 * h, fc="#FFF0E5", ec=COL["coral"], lw=0.6, radius=0.03)
    txt(ax, x + 0.13 * w, y + 0.235 * h, "Answer", size=6.8, weight="bold", color=COL["coral"], ha="left")
    txt(ax, x + 0.30 * w, y + 0.205 * h, "The correct answer is C. French beans.", size=5.6, ha="left")
    if label:
        txt(ax, x + 0.50 * w, y - 0.08 * h, "(a) Language prompt", size=7.3, weight="bold")


def draw_graph_prompt_panel(ax, x, y, w, h, label=True):
    dashed_box(ax, x, y, w, h, fc="white", ec="#15345D", lw=0.65, radius=0.035)
    cols = [x + 0.18 * w, x + 0.50 * w, x + 0.82 * w]
    top_labels = ["Downstream\nTasks", "Pretraining\nTasks", "Downstream\nTasks"]
    for cx, lab in zip(cols, top_labels):
        txt(ax, cx, y + 0.86 * h, lab, size=6.1, weight="bold")
    box(ax, cols[0] - 0.12 * w, y + 0.55 * h, 0.24 * w, 0.13 * h, fc=COL["coral2"], ec=COL["coral"], lw=0.6, radius=0.025)
    box(ax, cols[1] - 0.12 * w, y + 0.55 * h, 0.24 * w, 0.13 * h, fc=COL["coral2"], ec=COL["coral"], lw=0.6, radius=0.025)
    box(ax, cols[2] - 0.12 * w, y + 0.55 * h, 0.24 * w, 0.13 * h, fc="#B8DAD7", ec=COL["teal"], lw=0.6, radius=0.025)
    txt(ax, cols[0], y + 0.615 * h, "Pretrained\nGraph Model", size=5.6, weight="bold")
    txt(ax, cols[1], y + 0.615 * h, "Pretraining\nGraph Model", size=5.6, weight="bold")
    txt(ax, cols[2], y + 0.615 * h, "Pretrained\nGraph Model", size=5.6, weight="bold")
    draw_flame(ax, cols[0] - 0.12 * w, y + 0.73 * h, s=0.055 * h)
    draw_snowflake(ax, cols[2] - 0.10 * w, y + 0.73 * h, r=0.030 * h)
    txt(ax, cols[0] - 0.02 * w, y + 0.73 * h, "Fine-tuning", size=5.5, color=COL["blue"], ha="left")
    txt(ax, cols[2] + 0.03 * w, y + 0.73 * h, "Prompt\ntuning", size=5.5, color=COL["blue"], ha="left")
    arrow(ax, cols[0] + 0.13 * w, y + 0.615 * h, cols[1] - 0.13 * w, y + 0.615 * h, color=COL["ink"], lw=0.75, style="<|-|>", ms=6)
    arrow(ax, cols[1] + 0.13 * w, y + 0.615 * h, cols[2] - 0.13 * w, y + 0.615 * h, color=COL["ink"], lw=0.75, style="-|>", ms=6)
    for cx, domain in zip(cols, ["Task Domain", "Pretraining Domain", "Task Domain"]):
        dashed_box(ax, cx - 0.115 * w, y + 0.22 * h, 0.23 * w, 0.25 * h, fc="white", ec=COL["ink"], lw=0.5, radius=0.02)
        draw_graph(ax, cx - 0.075 * w, y + 0.28 * h, 0.15 * w, 0.11 * h, r=0.011 * h, lw=0.42)
        if cx == cols[2]:
            draw_hex(ax, cx + 0.047 * w, y + 0.355 * h, r=0.024 * h)
            txt(ax, cx + 0.00 * w, y + 0.355 * h, "+", size=7, weight="bold")
        txt(ax, cx, y + 0.245 * h, domain, size=4.8)
        arrow(ax, cx, y + 0.47 * h, cx, y + 0.55 * h, color=COL["ink"], lw=0.65, ms=5)
    box(ax, x + 0.26 * w, y + 0.055 * h, 0.48 * w, 0.065 * h, fc="white", ec=COL["ink"], lw=0.5, radius=0.015, ls=(0, (2, 1)))
    draw_flame(ax, x + 0.31 * w, y + 0.087 * h, s=0.032 * h)
    txt(ax, x + 0.36 * w, y + 0.087 * h, "tuned", size=4.7, ha="left")
    draw_snowflake(ax, x + 0.48 * w, y + 0.087 * h, r=0.016 * h)
    txt(ax, x + 0.52 * w, y + 0.087 * h, "frozen", size=4.7, ha="left")
    draw_hex(ax, x + 0.64 * w, y + 0.087 * h, r=0.018 * h)
    txt(ax, x + 0.67 * w, y + 0.087 * h, "prompt", size=4.7, ha="left")
    if label:
        txt(ax, x + 0.50 * w, y - 0.08 * h, "(b) Graph prompt", size=7.3, weight="bold")


def figure2():
    # Separate subfigures to match the existing LaTeX structure.
    fig, ax = canvas(2.65, 1.95, figsize=(3.25, 2.35))
    draw_language_panel(ax, 0.05, 0.18, 2.55, 1.67, label=False)
    save(fig, "fig2a_language_prompt_controlled")

    fig, ax = canvas(3.35, 1.95, figsize=(4.20, 2.35))
    draw_graph_prompt_panel(ax, 0.05, 0.18, 3.25, 1.67, label=False)
    save(fig, "fig2b_graph_prompt_controlled")

    fig, ax = canvas(6.60, 2.10, figsize=(7.35, 2.80))
    draw_language_panel(ax, 0.06, 0.30, 2.56, 1.62, label=True)
    draw_graph_prompt_panel(ax, 2.82, 0.30, 3.70, 1.62, label=True)
    save(fig, "fig2_language_vs_graph_prompt_controlled")


def figure5():
    fig, ax = canvas(3.55, 6.35, figsize=(5.35, 9.45))
    sep_color = "#B8BDC5"
    line(ax, 0.05, 4.95, 3.50, 4.95, color=sep_color, lw=0.55, ls="--")
    line(ax, 0.05, 3.55, 3.50, 3.55, color=sep_color, lw=0.55, ls="--")

    # (a)
    draw_graph(ax, 0.07, 5.45, 0.48, 0.55, r=0.040, lw=0.65)
    txt(ax, 0.31, 5.35, "Input Graph", size=5.6)
    arrow(ax, 0.62, 5.70, 0.78, 5.70, color=COL["muted"], lw=0.75)
    dashed_box(ax, 0.82, 5.32, 1.10, 0.72, fc="white", ec=COL["ink"], lw=0.65, radius=0.04)
    txt(ax, 1.37, 5.93, "Shallow Node Embedding", size=6.2, weight="bold")
    txt(ax, 1.37, 5.73, "Nodes with free parameters", size=5.15)
    draw_embedding(ax, 1.04, 5.42, 0.62, 0.27, count=4)
    arrow(ax, 1.95, 5.70, 2.10, 5.70, color=COL["muted"], lw=0.75)
    dashed_box(ax, 2.14, 5.32, 1.30, 0.72, fc="white", ec=COL["ink"], lw=0.65, radius=0.04)
    txt(ax, 2.79, 5.94, "Downstream Tasks", size=6.2, weight="bold")
    for i, (lab, hl, whole) in enumerate([("Node-level", [2], False), ("Edge-level", [], False), ("Graph-level", [], True)]):
        xx = 2.22 + i * 0.39
        draw_graph(ax, xx, 5.58, 0.31, 0.27, highlights=hl, whole=whole, edge_highlights=[(1, 2)] if lab == "Edge-level" else [], r=0.019, lw=0.42)
        txt(ax, xx + 0.155, 5.48, lab, size=4.7)
    txt(ax, 2.80, 5.38, "Flexibility", size=6.1, weight="bold", color=COL["coral"])
    txt(ax, 1.78, 5.12, "(a) Shallow Node Embedding Methods", size=7.0, weight="bold")

    # (b)
    draw_graph(ax, 0.08, 4.20, 0.48, 0.55, r=0.040, lw=0.65)
    txt(ax, 0.32, 4.10, "Input Graph", size=5.6)
    arrow(ax, 0.62, 4.45, 0.78, 4.45, color=COL["muted"], lw=0.75)
    dashed_box(ax, 0.82, 3.96, 1.15, 0.88, fc="white", ec=COL["ink"], lw=0.65, radius=0.04)
    txt(ax, 1.39, 4.70, "Graph Neural Networks", size=6.2, weight="bold")
    draw_flame(ax, 1.00, 4.36, s=0.13)
    draw_neural_net(ax, 1.08, 4.16, 0.70, 0.42, color="#888888")
    txt(ax, 1.40, 4.08, "Expressiveness", size=6.1, weight="bold", color=COL["coral"])
    arrow(ax, 2.03, 4.42, 2.46, 4.42, color=COL["ink"], lw=0.8, style="<|-|>", ms=6)
    txt(ax, 2.25, 4.52, "Task-specific", size=5.0, weight="bold", style="italic")
    txt(ax, 2.25, 4.34, "Supervision", size=5.0, weight="bold", style="italic")
    dashed_box(ax, 2.52, 3.96, 0.82, 0.88, fc="white", ec=COL["ink"], lw=0.65, radius=0.04)
    txt(ax, 2.93, 4.70, "Specific Downstream\nTask", size=6.0, weight="bold")
    draw_graph(ax, 2.68, 4.25, 0.45, 0.35, highlights=[2], r=0.026, lw=0.5)
    txt(ax, 2.93, 4.10, "e.g. Node\nClassification", size=5.1)
    txt(ax, 1.78, 3.72, "(b) Deep Graph Neural Networks", size=7.0, weight="bold")

    # (c)
    dashed_box(ax, 0.08, 0.50, 0.93, 2.80, fc="white", ec=COL["ink"], lw=0.65, radius=0.04)
    txt(ax, 0.55, 3.10, "Pre-training\nGraph Model", size=6.1, weight="bold")
    draw_graph(ax, 0.30, 2.45, 0.48, 0.45, r=0.034, lw=0.60)
    arrow(ax, 0.55, 2.35, 0.55, 2.12, color=COL["muted"], lw=0.75)
    draw_neural_net(ax, 0.24, 1.45, 0.62, 0.45, color="#888888")
    draw_flame(ax, 0.20, 1.65, s=0.13)
    arrow(ax, 0.55, 1.38, 0.55, 1.12, color=COL["muted"], lw=0.75)
    txt(ax, 0.55, 0.98, "Pretext Task", size=5.7)
    txt(ax, 0.55, 0.72, "Expressiveness", size=6.1, weight="bold", color=COL["coral"])

    dashed_box(ax, 1.15, 2.35, 2.25, 0.95, fc="white", ec=COL["ink"], lw=0.65, radius=0.04)
    txt(ax, 2.27, 3.12, "Fine-tuning for Specific Tasks", size=6.2, weight="bold")
    for i, (lab, hl, edges) in enumerate([("Node-level\nPrediction", [2], []), ("Edge-level\nPrediction", [], [(1, 2)])]):
        xx = 1.36 + i * 0.92
        draw_graph(ax, xx, 2.82, 0.44, 0.30, highlights=hl, edge_highlights=edges, r=0.022, lw=0.48)
        arrow(ax, xx + 0.22, 2.78, xx + 0.22, 2.64, color=COL["coral"], lw=0.65, ms=5)
        box(ax, xx - 0.02, 2.47, 0.48, 0.16, fc=COL["coral2"], ec=COL["coral"], lw=0.55, radius=0.025)
        draw_flame(ax, xx, 2.55, s=0.06)
        txt(ax, xx + 0.22, 2.55, "Pre-trained\nGraph Model", size=4.15, weight="bold")
        txt(ax, xx + 0.22, 2.40, lab, size=4.65, va="top")
    txt(ax, 3.20, 2.95, "...", size=8, weight="bold")

    dashed_box(ax, 1.15, 0.50, 2.25, 1.60, fc="white", ec=COL["ink"], lw=0.65, radius=0.04)
    txt(ax, 2.27, 1.95, "Prompt Tuning for Downstream Tasks", size=6.2, weight="bold")
    for i, (lab, whole) in enumerate([("Node-level\nPrediction", False), ("Graph-level\nPrediction", True)]):
        xx = 1.28 + i * 0.98
        draw_graph(ax, xx, 1.50, 0.42, 0.28, highlights=[4] if not whole else [], whole=whole, r=0.020, lw=0.46)
        txt(ax, xx + 0.53, 1.63, "+", size=7.5, weight="bold", color=COL["coral"])
        draw_hex(ax, xx + 0.70, 1.63, r=0.055)
        box(ax, xx + 0.01, 1.33, 0.79, 0.06, fc="none", ec=COL["amber"], lw=0.6, radius=0.018)
        arrow(ax, xx + 0.40, 1.32, xx + 0.40, 1.18, color=COL["teal"], lw=0.65, ms=5)
        box(ax, xx + 0.07, 1.02, 0.66, 0.20, fc="#BFE5E2", ec=COL["teal"], lw=0.55, radius=0.025)
        draw_snowflake(ax, xx + 0.14, 1.12, r=0.04)
        txt(ax, xx + 0.43, 1.12, "Pre-trained\nGraph Model", size=4.8, weight="bold")
        arrow(ax, xx + 0.40, 1.00, xx + 0.40, 0.82, color=COL["teal"], lw=0.65, ms=5)
        txt(ax, xx + 0.40, 0.73, lab, size=5.0, va="top")
    txt(ax, 3.25, 1.65, "...", size=8, weight="bold")
    txt(ax, 2.28, 0.59, "Flexibility across tasks/domains", size=5.8, weight="bold", color=COL["coral"])

    box(ax, 0.32, 0.12, 2.90, 0.26, fc="white", ec=COL["ink"], lw=0.55, radius=0.025, ls=(0, (3, 2)))
    draw_flame(ax, 0.63, 0.25, s=0.085)
    txt(ax, 0.79, 0.25, "tuned", size=5.2, ha="left")
    draw_snowflake(ax, 1.48, 0.25, r=0.055)
    txt(ax, 1.62, 0.25, "frozen", size=5.2, ha="left")
    draw_hex(ax, 2.38, 0.25, r=0.060)
    txt(ax, 2.54, 0.25, "prompt", size=5.2, ha="left")
    txt(ax, 1.78, 3.42, "(c) Comparison between fine-tune and prompt", size=7.0, weight="bold")
    save(fig, "fig5_why_prompt_controlled")


def figure6():
    fig, ax = canvas(3.55, 2.45, figsize=(7.20, 4.65))
    box(ax, 0.05, 1.98, 1.10, 0.24, fc=COL["coral2"], ec=COL["ink"], lw=0.55, radius=0.025)
    box(ax, 1.37, 1.98, 1.18, 0.24, fc=COL["blue2"], ec=COL["ink"], lw=0.55, radius=0.025)
    txt(ax, 0.60, 2.10, "Task-specific Fine-tuning", size=6.1, weight="bold")
    txt(ax, 1.96, 2.10, "Task-agnostic Prompting", size=6.1, weight="bold")
    arrow(ax, 0.60, 1.84, 0.60, 1.98, color=COL["ink"], lw=0.65, ms=5)
    arrow(ax, 1.96, 1.84, 1.96, 1.98, color=COL["ink"], lw=0.65, ms=5)
    box(ax, 0.05, 0.36, 2.85, 1.55, fc="#FBECDF", ec=COL["ink"], lw=0.65, radius=0.045)
    txt(ax, 1.48, 1.77, "Graph Pre-training", size=7.2, weight="bold")
    rect(ax, 0.23, 0.52, 1.28, 1.10, fc="white", ec=COL["ink"], lw=0.55)
    rect(ax, 1.51, 0.52, 1.20, 1.10, fc="white", ec=COL["ink"], lw=0.55)
    line(ax, 0.05, 1.24, 2.90, 1.24, color=COL["muted"], lw=0.42, ls="--")
    line(ax, 0.05, 0.88, 2.90, 0.88, color=COL["muted"], lw=0.42, ls="--")
    line(ax, 1.51, 0.52, 1.51, 1.62, color=COL["muted"], lw=0.42, ls="--")
    txt(ax, 0.09, 1.45, "Node-\nlevel", size=5.4, weight="bold", ha="left")
    txt(ax, 0.09, 1.08, "Edge-\nlevel", size=5.4, weight="bold", ha="left")
    txt(ax, 0.09, 0.72, "Graph-\nlevel", size=5.4, weight="bold", ha="left")
    txt(ax, 0.87, 0.44, "Contrastive Method", size=5.9, weight="bold")
    txt(ax, 2.11, 0.44, "Predictive Method", size=5.9, weight="bold")
    rows = [1.34, 0.98, 0.62]
    for yy in rows:
        draw_graph(ax, 0.30, yy, 0.25, 0.22, r=0.014, lw=0.38)
        arrow(ax, 0.58, yy + 0.11, 0.70, yy + 0.11, color=COL["muted"], lw=0.55, ms=5)
        draw_graph(ax, 0.73, yy, 0.27, 0.22, highlights=[2, 4] if yy == rows[0] else [4], whole=yy == rows[2], edge_highlights=[(1, 2)] if yy == rows[1] else [], r=0.014, lw=0.38)
        arrow(ax, 1.02, yy + 0.11, 1.18, yy + 0.11, color=COL["ink"], lw=0.55, style="<|-|>", ms=5)
        txt(ax, 1.10, yy + 0.02, "Max.\nsim.", size=3.8)
        draw_graph(ax, 1.22, yy, 0.25, 0.22, highlights=[1, 3] if yy == rows[0] else [4], whole=yy == rows[2], edge_highlights=[(1, 2)] if yy == rows[1] else [], r=0.014, lw=0.38)
        draw_graph(ax, 1.58, yy, 0.24, 0.22, r=0.014, lw=0.38)
        arrow(ax, 1.84, yy + 0.11, 1.96, yy + 0.11, color=COL["muted"], lw=0.55, ms=5)
        if yy == rows[0]:
            draw_graph(ax, 1.99, yy, 0.24, 0.22, highlights=[0], r=0.014, lw=0.38)
            txt(ax, 2.11, yy + 0.22, "?", size=5.5)
            for k in range(3):
                draw_feature_bars(ax, 2.35 + k * 0.10, yy + 0.01, w=0.025, h=0.18, n=3, color=COL["amber2"])
        elif yy == rows[1]:
            draw_graph(ax, 1.99, yy, 0.24, 0.22, edge_highlights=[(1, 2)], r=0.014, lw=0.38)
            arrow(ax, 2.26, yy + 0.11, 2.38, yy + 0.11, color=COL["muted"], lw=0.55, ms=5)
            draw_graph(ax, 2.40, yy, 0.24, 0.22, edge_highlights=[(1, 2)], r=0.014, lw=0.38)
        else:
            dashed_box(ax, 1.99, yy + 0.01, 0.28, 0.20, fc=COL["green2"], ec=COL["muted"], lw=0.45, radius=0.02)
            draw_graph(ax, 2.00, yy + 0.02, 0.26, 0.18, r=0.012, lw=0.34, alpha=0.45)
            txt(ax, 2.13, yy + 0.11, "?", size=5.5)
            arrow(ax, 2.30, yy + 0.11, 2.42, yy + 0.11, color=COL["muted"], lw=0.55, ms=5)
            draw_graph(ax, 2.45, yy, 0.23, 0.22, r=0.014, lw=0.38)
            draw_feature_bars(ax, 2.66, yy + 0.02, w=0.025, h=0.18, n=3, color=COL["amber2"])

    # Right callouts.
    callouts = [
        ("Graph\nReconstruction", 1.45),
        ("Auxiliary Property\nPrediction", 0.96),
        ("Masked Feature\nRegression", 0.47),
    ]
    for lab, yy in callouts:
        box(ax, 2.98, yy, 0.50, 0.36, fc=COL["light"], ec=COL["green"], lw=0.55, radius=0.035)
        txt(ax, 3.23, yy + 0.27, lab, size=4.8, weight="bold")
        if "Graph" in lab:
            draw_graph(ax, 3.06, yy + 0.05, 0.16, 0.13, r=0.009, lw=0.32)
            arrow(ax, 3.24, yy + 0.12, 3.34, yy + 0.12, color=COL["muted"], lw=0.45, ms=4)
            draw_graph(ax, 3.30, yy + 0.05, 0.16, 0.13, highlights=[3, 4], r=0.009, lw=0.32)
        elif "Auxiliary" in lab:
            draw_graph(ax, 3.05, yy + 0.05, 0.15, 0.13, r=0.009, lw=0.32)
            arrow(ax, 3.22, yy + 0.12, 3.31, yy + 0.12, color=COL["muted"], lw=0.45, ms=4)
            for i in range(3):
                rect(ax, 3.35, yy + 0.08 + i * 0.045, 0.09, 0.025, fc="white", ec=COL["ink"], lw=0.25)
                txt(ax, 3.365, yy + 0.092 + i * 0.045, "x", size=2.8, color=COL["green"])
        else:
            draw_feature_bars(ax, 3.10, yy + 0.09, w=0.04, h=0.16, n=3)
            txt(ax, 3.12, yy + 0.24, "?", size=4.5)
            arrow(ax, 3.20, yy + 0.17, 3.32, yy + 0.17, color=COL["muted"], lw=0.45, ms=4)
            draw_feature_bars(ax, 3.36, yy + 0.09, w=0.04, h=0.16, n=3, color=COL["amber2"])
    box(ax, 0.14, 0.10, 3.25, 0.16, fc="white", ec=COL["muted"], lw=0.45, radius=0.015, ls=(0, (3, 2)))
    legend = [
        ("Original node", 0.32),
        ("Augmented node", 0.78),
        ("Original edge", 1.24),
        ("Selected edge", 1.70),
        ("Masked edge", 2.15),
        ("Node feature", 2.58),
        ("Augmented / masked region", 3.04),
    ]
    for lab, xx in legend:
        if "node" in lab:
            fc = "white" if "Original" in lab else COL["green2"]
            ax.add_patch(Circle((xx, 0.18), 0.035, fc=fc, ec=COL["ink"], lw=0.45))
        elif "edge" in lab:
            ls = "--" if "Masked" in lab else "-"
            color = COL["coral"] if "Selected" in lab else COL["ink"]
            line(ax, xx - 0.04, 0.18, xx + 0.04, 0.18, color=color, lw=0.65, ls=ls)
        elif "feature" in lab:
            draw_feature_bars(ax, xx - 0.025, 0.13, w=0.025, h=0.10, n=3, color=COL["amber2"])
        else:
            box(ax, xx - 0.05, 0.14, 0.10, 0.08, fc=COL["green2"], ec=COL["green"], lw=0.35, radius=0.012, ls=(0, (2, 1)))
        txt(ax, xx + 0.06, 0.18, lab, size=3.7, ha="left")
    save(fig, "fig6_pretraining_controlled")


def figure7():
    fig, ax = canvas(3.55, 2.30, figsize=(7.15, 4.55))
    dashed_box(ax, 0.05, 1.23, 1.16, 0.98, fc="white", ec="#15345D", lw=0.7, radius=0.04)
    dashed_box(ax, 0.05, 0.12, 1.16, 0.98, fc="white", ec="#15345D", lw=0.7, radius=0.04)
    dashed_box(ax, 1.28, 0.12, 2.22, 2.09, fc="white", ec="#15345D", lw=0.7, radius=0.04)
    txt(ax, 0.63, 2.08, "Original Graph", size=8.5, weight="bold")
    draw_graph(ax, 0.16, 1.45, 0.58, 0.42, r=0.040, lw=0.65)
    for bx, by in [(0.20, 1.75), (0.72, 1.80), (0.28, 1.40), (0.58, 1.35), (0.82, 1.48)]:
        draw_feature_bars(ax, bx, by, w=0.045, h=0.20, n=4, color=COL["green2"])
    arrow(ax, 0.95, 1.83, 0.78, 1.93, color=COL["muted"], lw=0.6, ms=5, ls="--")
    txt(ax, 1.05, 1.69, "Node feature", size=5.2, ha="right")

    txt(ax, 0.63, 0.98, "Prompt Graph", size=8.5, weight="bold")
    pnodes = [(0.22, 0.68), (0.56, 0.72), (0.20, 0.38), (0.55, 0.35), (0.38, 0.22)]
    pedges = [(0, 1), (0, 3), (1, 2), (1, 3), (2, 3), (2, 4)]
    for a, b in pedges:
        line(ax, pnodes[a][0], pnodes[a][1], pnodes[b][0], pnodes[b][1], color="#C00000", lw=0.65)
    for px, py in pnodes:
        ax.add_patch(Circle((px, py), 0.045, fc="white", ec=COL["purple"], lw=1.2, zorder=3))
        draw_feature_bars(ax, px - 0.06, py - 0.18, w=0.040, h=0.16, n=3, color=COL["green2"])
    arrow(ax, 0.88, 0.72, 0.60, 0.72, color=COL["purple"], lw=0.65, ms=5)
    txt(ax, 1.05, 0.72, "Prompt Token", size=5.0, color=COL["purple"], ha="right")
    arrow(ax, 0.88, 0.54, 0.57, 0.62, color="#C00000", lw=0.65, ms=5, ls="--")
    txt(ax, 1.05, 0.54, "Token Structure", size=5.0, color="#C00000", ha="right")
    arrow(ax, 0.88, 0.32, 0.55, 0.22, color=COL["green"], lw=0.65, ms=5, ls="--")
    txt(ax, 1.05, 0.32, "Token feature", size=5.0, color=COL["green"], ha="right")

    txt(ax, 2.39, 2.08, "Four Kinds of Inserting Patterns", size=8.1, weight="bold")
    cells = [
        (1.36, 1.19, "By Cross Links"),
        (2.43, 1.19, "By Feature Adding"),
        (1.36, 0.22, "By Concatenating"),
        (2.43, 0.22, "By Multiplication"),
    ]
    for cx, cy, lab in cells:
        rect(ax, cx, cy, 0.95, 0.78, fc="white", ec=COL["ink"], lw=0.55)
        txt(ax, cx + 0.475, cy + 0.68, "Prompted Graph", size=6.0)
        txt(ax, cx + 0.475, cy + 0.08, lab, size=6.1, weight="bold")

    # Cross links.
    cx, cy, _ = cells[0]
    draw_graph(ax, cx + 0.06, cy + 0.24, 0.40, 0.34, r=0.020, lw=0.45)
    q = [(cx + 0.61, cy + 0.47), (cx + 0.80, cy + 0.48), (cx + 0.66, cy + 0.31), (cx + 0.82, cy + 0.28)]
    for a, b in [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]:
        line(ax, q[a][0], q[a][1], q[b][0], q[b][1], color="#C00000", lw=0.55)
    for px, py in q:
        ax.add_patch(Circle((px, py), 0.028, fc="white", ec=COL["purple"], lw=1.0, zorder=3))
    for target in q[:3]:
        arrow(ax, cx + 0.36, cy + 0.44, target[0] - 0.02, target[1], color=COL["green"], lw=0.55, ms=4, ls="--", rad=0.18)

    # Feature adding.
    cx, cy, _ = cells[1]
    draw_graph(ax, cx + 0.08, cy + 0.24, 0.42, 0.34, r=0.020, lw=0.45)
    box(ax, cx + 0.58, cy + 0.26, 0.28, 0.25, fc="white", ec=COL["amber"], lw=0.55, radius=0.03, ls="--")
    ax.add_patch(Circle((cx + 0.66, cy + 0.40), 0.028, fc="white", ec=COL["purple"], lw=1.0))
    txt(ax, cx + 0.72, cy + 0.34, "+", size=8, weight="bold", color=COL["coral"])
    draw_feature_bars(ax, cx + 0.80, cy + 0.31, w=0.035, h=0.18, n=4, color=COL["green2"])
    arrow(ax, cx + 0.62, cy + 0.40, cx + 0.48, cy + 0.40, color=COL["coral"], lw=0.65, ms=5)

    # Concatenating.
    cx, cy, _ = cells[2]
    draw_graph(ax, cx + 0.08, cy + 0.24, 0.42, 0.34, r=0.020, lw=0.45)
    box(ax, cx + 0.55, cy + 0.27, 0.32, 0.26, fc="white", ec=COL["amber"], lw=0.55, radius=0.03, ls="--")
    ax.add_patch(Circle((cx + 0.64, cy + 0.42), 0.028, fc="white", ec=COL["purple"], lw=1.0))
    draw_feature_bars(ax, cx + 0.76, cy + 0.33, w=0.035, h=0.18, n=4, color=COL["green2"])
    arrow(ax, cx + 0.60, cy + 0.42, cx + 0.47, cy + 0.42, color=COL["coral"], lw=0.65, ms=5)

    # Multiplication.
    cx, cy, _ = cells[3]
    draw_graph(ax, cx + 0.08, cy + 0.24, 0.42, 0.34, r=0.020, lw=0.45)
    box(ax, cx + 0.55, cy + 0.27, 0.32, 0.26, fc="white", ec=COL["amber"], lw=0.55, radius=0.03, ls="--")
    ax.add_patch(Circle((cx + 0.64, cy + 0.43), 0.028, fc="white", ec=COL["purple"], lw=1.0))
    txt(ax, cx + 0.64, cy + 0.32, "x", size=7.2, weight="bold", color=COL["coral"])
    draw_feature_bars(ax, cx + 0.76, cy + 0.33, w=0.035, h=0.18, n=4, color=COL["green2"])
    arrow(ax, cx + 0.60, cy + 0.42, cx + 0.47, cy + 0.42, color=COL["coral"], lw=0.65, ms=5)
    save(fig, "fig7_prompt_patterns_controlled")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    figure1()
    figure2()
    figure5()
    figure6()
    figure7()
    print(f"Wrote controlled redraws to {OUT}")


if __name__ == "__main__":
    main()

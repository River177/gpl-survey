#!/usr/bin/env python3
"""Generate editable Draw.io redraws for selected GPL survey figures.

The output is intentionally uncompressed .drawio XML. Diagrams.net can open it
directly, and every label/shape/edge remains editable.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import copy
import html
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tex" / "pic" / "redraw-drawio"
PREVIEW = OUT / "preview-svg"

FONT = "Helvetica"
INK = "#111827"
MUTED = "#64748B"
BLUE = "#4A90D9"
BLUE_DARK = "#2563EB"
TEAL = "#2A9D8F"
GREEN = "#5BA58B"
AMBER = "#D4A252"
YELLOW = "#F2C94C"
ORANGE = "#F4A261"
CORAL = "#E76F51"
RED = "#C00000"
PURPLE = "#7C3AED"
LAVENDER = "#F1E8FF"
MINT = "#E8F5EE"
PEACH = "#FFF0E5"
SAND = "#FFF7D6"
SKY = "#EAF4FF"
GRAY_BG = "#F8FAFC"


def esc(value: str) -> str:
    return value.replace("\n", "<br>")


def style(parts: list[str]) -> str:
    return ";".join(parts) + ";"


def strip_html(value: str) -> str:
    value = value.replace("<br/>", "\n").replace("<br>", "\n")
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value)


@dataclass
class SvgItem:
    kind: str
    attrs: dict


@dataclass
class Page:
    name: str
    width: int
    height: int
    page_id: str
    cells: list[ET.Element] = field(default_factory=list)
    svg: list[SvgItem] = field(default_factory=list)
    counter: int = 2

    def next_id(self, prefix: str) -> str:
        value = f"{self.page_id}_{prefix}_{self.counter}"
        self.counter += 1
        return value

    def add_rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        label: str = "",
        *,
        fill: str = "#FFFFFF",
        stroke: str = INK,
        stroke_width: float = 1.5,
        rounded: bool = True,
        dashed: bool = False,
        font_size: float = 14,
        font_color: str = INK,
        bold: bool = False,
        italic: bool = False,
        align: str = "center",
        valign: str = "middle",
        opacity: int | None = None,
    ) -> str:
        cell_id = self.next_id("rect")
        font_style = (1 if bold else 0) + (2 if italic else 0)
        parts = [
            f"rounded={1 if rounded else 0}",
            "whiteSpace=wrap",
            "html=1",
            "arcSize=8",
            f"fillColor={fill}",
            f"strokeColor={stroke}",
            f"strokeWidth={stroke_width}",
            f"fontFamily={FONT}",
            f"fontSize={font_size}",
            f"fontColor={font_color}",
            f"fontStyle={font_style}",
            f"align={align}",
            f"verticalAlign={valign}",
            "spacingLeft=8",
            "spacingRight=8",
        ]
        if dashed:
            parts.extend(["dashed=1", "dashPattern=8 5"])
        if opacity is not None:
            parts.append(f"opacity={opacity}")
        cell = ET.Element(
            "mxCell",
            id=cell_id,
            value=esc(label),
            style=style(parts),
            vertex="1",
            parent="1",
        )
        ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), as_="geometry")
        cell[-1].attrib["as"] = cell[-1].attrib.pop("as_")
        self.cells.append(cell)
        self.svg.append(
            SvgItem(
                "rect",
                dict(
                    x=x,
                    y=y,
                    w=w,
                    h=h,
                    label=label,
                    fill=fill,
                    stroke=stroke,
                    stroke_width=stroke_width,
                    rounded=rounded,
                    dashed=dashed,
                    font_size=font_size,
                    font_color=font_color,
                    bold=bold,
                    italic=italic,
                    align=align,
                    valign=valign,
                    opacity=opacity,
                ),
            )
        )
        return cell_id

    def add_text(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        label: str,
        *,
        font_size: float = 14,
        font_color: str = INK,
        bold: bool = False,
        italic: bool = False,
        align: str = "center",
        valign: str = "middle",
    ) -> str:
        cell_id = self.next_id("text")
        font_style = (1 if bold else 0) + (2 if italic else 0)
        parts = [
            "text",
            "html=1",
            "strokeColor=none",
            "fillColor=none",
            "whiteSpace=wrap",
            "rounded=0",
            f"fontFamily={FONT}",
            f"fontSize={font_size}",
            f"fontColor={font_color}",
            f"fontStyle={font_style}",
            f"align={align}",
            f"verticalAlign={valign}",
            "spacingLeft=4",
            "spacingRight=4",
        ]
        cell = ET.Element(
            "mxCell",
            id=cell_id,
            value=esc(label),
            style=style(parts),
            vertex="1",
            parent="1",
        )
        ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), as_="geometry")
        cell[-1].attrib["as"] = cell[-1].attrib.pop("as_")
        self.cells.append(cell)
        self.svg.append(
            SvgItem(
                "text",
                dict(
                    x=x,
                    y=y,
                    w=w,
                    h=h,
                    label=label,
                    font_size=font_size,
                    font_color=font_color,
                    bold=bold,
                    italic=italic,
                    align=align,
                    valign=valign,
                ),
            )
        )
        return cell_id

    def add_ellipse(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        label: str = "",
        *,
        fill: str = "#FFFFFF",
        stroke: str = INK,
        stroke_width: float = 1.5,
        font_size: float = 12,
        font_color: str = INK,
        bold: bool = False,
    ) -> str:
        cell_id = self.next_id("ellipse")
        parts = [
            "ellipse",
            "whiteSpace=wrap",
            "html=1",
            f"fillColor={fill}",
            f"strokeColor={stroke}",
            f"strokeWidth={stroke_width}",
            f"fontFamily={FONT}",
            f"fontSize={font_size}",
            f"fontColor={font_color}",
            f"fontStyle={1 if bold else 0}",
        ]
        cell = ET.Element(
            "mxCell",
            id=cell_id,
            value=esc(label),
            style=style(parts),
            vertex="1",
            parent="1",
        )
        ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), as_="geometry")
        cell[-1].attrib["as"] = cell[-1].attrib.pop("as_")
        self.cells.append(cell)
        self.svg.append(
            SvgItem(
                "ellipse",
                dict(
                    x=x,
                    y=y,
                    w=w,
                    h=h,
                    label=label,
                    fill=fill,
                    stroke=stroke,
                    stroke_width=stroke_width,
                    font_size=font_size,
                    font_color=font_color,
                    bold=bold,
                ),
            )
        )
        return cell_id

    def add_shape(
        self,
        shape_name: str,
        x: float,
        y: float,
        w: float,
        h: float,
        label: str = "",
        *,
        fill: str = "#FFFFFF",
        stroke: str = INK,
        stroke_width: float = 1.5,
        font_size: float = 12,
        font_color: str = INK,
        bold: bool = False,
    ) -> str:
        cell_id = self.next_id(shape_name)
        parts = [
            f"shape={shape_name}",
            "whiteSpace=wrap",
            "html=1",
            f"fillColor={fill}",
            f"strokeColor={stroke}",
            f"strokeWidth={stroke_width}",
            f"fontFamily={FONT}",
            f"fontSize={font_size}",
            f"fontColor={font_color}",
            f"fontStyle={1 if bold else 0}",
        ]
        cell = ET.Element(
            "mxCell",
            id=cell_id,
            value=esc(label),
            style=style(parts),
            vertex="1",
            parent="1",
        )
        ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), as_="geometry")
        cell[-1].attrib["as"] = cell[-1].attrib.pop("as_")
        self.cells.append(cell)
        self.svg.append(
            SvgItem(
                "shape",
                dict(
                    shape=shape_name,
                    x=x,
                    y=y,
                    w=w,
                    h=h,
                    label=label,
                    fill=fill,
                    stroke=stroke,
                    stroke_width=stroke_width,
                    font_size=font_size,
                    font_color=font_color,
                    bold=bold,
                ),
            )
        )
        return cell_id

    def add_line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        *,
        stroke: str = INK,
        stroke_width: float = 1.5,
        dashed: bool = False,
        arrow: bool = True,
        curved: bool = False,
    ) -> str:
        cell_id = self.next_id("edge")
        parts = [
            "html=1",
            f"rounded={1 if curved else 0}",
            f"strokeColor={stroke}",
            f"strokeWidth={stroke_width}",
            f"endArrow={'classic' if arrow else 'none'}",
            f"endFill={1 if arrow else 0}",
        ]
        if dashed:
            parts.extend(["dashed=1", "dashPattern=8 5"])
        cell = ET.Element(
            "mxCell",
            id=cell_id,
            value="",
            style=style(parts),
            edge="1",
            parent="1",
        )
        geo = ET.SubElement(cell, "mxGeometry", width="50", height="50", relative="1", as_="geometry")
        geo.attrib["as"] = geo.attrib.pop("as_")
        sp = ET.SubElement(geo, "mxPoint", x=str(x1), y=str(y1), as_="sourcePoint")
        sp.attrib["as"] = sp.attrib.pop("as_")
        tp = ET.SubElement(geo, "mxPoint", x=str(x2), y=str(y2), as_="targetPoint")
        tp.attrib["as"] = tp.attrib.pop("as_")
        self.cells.append(cell)
        self.svg.append(
            SvgItem(
                "line",
                dict(
                    x1=x1,
                    y1=y1,
                    x2=x2,
                    y2=y2,
                    stroke=stroke,
                    stroke_width=stroke_width,
                    dashed=dashed,
                    arrow=arrow,
                ),
            )
        )
        return cell_id

    def add_feature_stack(self, x: float, y: float, cell_w: float = 14, cell_h: float = 12, fill: str = "#E8F5EE") -> None:
        for i in range(4):
            self.add_rect(
                x,
                y + i * cell_h,
                cell_w,
                cell_h,
                "",
                fill=fill if i % 2 else "#FFFFFF",
                stroke=INK,
                stroke_width=1,
                rounded=False,
            )

    def mx_model(self) -> ET.Element:
        model = ET.Element(
            "mxGraphModel",
            dx="1200",
            dy="800",
            grid="1",
            gridSize="10",
            guides="1",
            tooltips="1",
            connect="1",
            arrows="1",
            fold="1",
            page="1",
            pageScale="1",
            pageWidth=str(self.width),
            pageHeight=str(self.height),
            math="0",
            shadow="0",
        )
        root = ET.SubElement(model, "root")
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        for cell in self.cells:
            root.append(copy.deepcopy(cell))
        return model


def graph(
    p: Page,
    cx: float,
    cy: float,
    *,
    scale: float = 1.0,
    node_fill: str = "#FFFFFF",
    stroke: str = INK,
    highlight: tuple[float, float, float, float] | None = None,
    features: bool = False,
    prompt: bool = False,
) -> None:
    pts = [
        (-42, -35),
        (26, -38),
        (0, 0),
        (-58, 12),
        (-25, 48),
        (46, 37),
    ]
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (2, 5)]
    if highlight:
        hx, hy, hw, hh = highlight
        p.add_rect(cx + hx * scale, cy + hy * scale, hw * scale, hh * scale, "", fill=SAND, stroke=AMBER, stroke_width=1.5, rounded=True, dashed=True)
    if prompt:
        extra = [(78, -12), (104, 24), (75, 53)]
        for a, b in [(2, 6), (6, 7), (7, 8), (8, 6), (5, 7)]:
            aa = (pts + extra)[a]
            bb = (pts + extra)[b]
            p.add_line(cx + aa[0] * scale, cy + aa[1] * scale, cx + bb[0] * scale, cy + bb[1] * scale, stroke=RED, stroke_width=2.2, arrow=False)
        pts = pts + extra
    for a, b in edges:
        p.add_line(cx + pts[a][0] * scale, cy + pts[a][1] * scale, cx + pts[b][0] * scale, cy + pts[b][1] * scale, stroke=stroke, stroke_width=1.7, arrow=False)
    for i, (x, y) in enumerate(pts):
        fill = node_fill
        outline = stroke
        width = 2.0
        if prompt and i >= 6:
            fill = "#FFFFFF"
            outline = PURPLE
            width = 3.0
        p.add_ellipse(cx + (x - 10) * scale, cy + (y - 10) * scale, 20 * scale, 20 * scale, "", fill=fill, stroke=outline, stroke_width=width)
        if features and i in {0, 1, 3, 4}:
            p.add_feature_stack(cx + (x - 28) * scale, cy + (y - 26) * scale, cell_w=8 * scale, cell_h=7 * scale, fill=MINT)


def small_mlp(p: Page, x: float, y: float, scale: float = 1.0) -> None:
    layers = [(0, 3), (55, 4), (110, 3)]
    nodes = []
    for lx, count in layers:
        layer_nodes = []
        for i in range(count):
            ny = y + (i - (count - 1) / 2) * 35 * scale
            layer_nodes.append((x + lx * scale, ny))
            p.add_ellipse(x + lx * scale - 11 * scale, ny - 11 * scale, 22 * scale, 22 * scale, "", fill="#FFFFFF", stroke="#7B8794", stroke_width=3)
        nodes.append(layer_nodes)
    for left, right in zip(nodes, nodes[1:]):
        for a in left:
            for b in right:
                p.add_line(a[0], a[1], b[0], b[1], stroke=INK, stroke_width=1.1, arrow=False)


def feature_matrix(p: Page, x: float, y: float, cols: int = 3, rows: int = 4, scale: float = 1.0) -> None:
    shades = ["#FFF7D6", "#FFE599", "#FFD966", "#F2C94C"]
    for c in range(cols):
        for r in range(rows):
            fill = shades[(r + c) % len(shades)]
            p.add_rect(x + c * 18 * scale, y + r * 15 * scale, 16 * scale, 14 * scale, "", fill=fill, stroke=INK, stroke_width=1, rounded=False)


def fig1() -> Page:
    p = Page("Fig 1 - Three transfer challenges", 1220, 620, "fig1")
    p.add_rect(20, 20, 1180, 560, "", fill="#FFFFFF", stroke="#FFFFFF", stroke_width=0)

    # Panel A
    p.add_text(95, 530, 260, 48, "(a) Cross-modalities", font_size=24, bold=True)
    p.add_rect(60, 70, 250, 100, "", fill=PEACH, stroke=CORAL, stroke_width=2.2)
    p.add_rect(112, 100, 105, 56, "", fill="#D9F0D2", stroke=GREEN, stroke_width=1)
    p.add_rect(135, 87, 105, 56, "", fill="#9FD7A2", stroke=GREEN, stroke_width=1, opacity=85)
    p.add_rect(158, 74, 105, 56, "", fill="#7FB3D5", stroke=BLUE, stroke_width=1, opacity=75)
    p.add_text(325, 105, 90, 40, "Image", font_size=18, bold=True, italic=True, font_color=INK)
    p.add_line(326, 125, 310, 125, stroke=BLUE_DARK, stroke_width=2.3)

    p.add_rect(60, 215, 250, 100, "Title: ...<br>Abstract: ...<br>Keywords: ...", fill=MINT, stroke=GREEN, stroke_width=2.2, font_size=20, bold=True, align="left")
    p.add_text(330, 247, 80, 38, "Text", font_size=18, bold=True, italic=True)
    p.add_rect(440, 225, 56, 70, "", fill="#FFFFFF", stroke=BLUE, stroke_width=2)
    p.add_line(420, 266, 310, 266, stroke=BLUE_DARK, stroke_width=2.3)

    p.add_rect(60, 360, 250, 100, "", fill=SAND, stroke="#F5B400", stroke_width=2.2)
    for dx, dy in [(0, 25), (65, 0), (130, 24), (92, 58), (18, 58)]:
        p.add_rect(95 + dx, 385 + dy, 32, 42, "", fill="#FFFFFF", stroke=MUTED, stroke_width=1.5)
    p.add_line(126, 424, 160, 392, stroke=BLUE_DARK, stroke_width=1.8, arrow=False)
    p.add_line(190, 402, 232, 424, stroke=BLUE_DARK, stroke_width=1.8, arrow=False)
    p.add_line(171, 425, 189, 457, stroke=BLUE_DARK, stroke_width=1.8, arrow=False)
    p.add_text(325, 405, 90, 40, "Graph", font_size=18, bold=True, italic=True)
    p.add_line(326, 420, 310, 420, stroke=BLUE_DARK, stroke_width=2.3)
    p.add_line(373, 145, 373, 407, stroke=BLUE_DARK, stroke_width=2.0, arrow=False)

    # Panel B
    p.add_text(520, 530, 260, 48, "(b) Cross-domains", font_size=24, bold=True)
    domain_cards = [
        (520, 70, "#F1E8FF", PURPLE, "Biology"),
        (520, 215, MINT, GREEN, "Knowledge"),
        (520, 360, SAND, "#F5B400", "Society"),
    ]
    for x, y, fill, stroke, label in domain_cards:
        p.add_rect(x, y, 300, 100, "", fill=fill, stroke=stroke, stroke_width=2.2)
        p.add_text(x + 22, y + 60, 120, 35, label, font_size=19, bold=True, italic=True, align="left")
    graph(p, 672, 115, scale=0.72, stroke=PURPLE, node_fill="#FFFFFF")
    p.add_ellipse(690, 95, 20, 20, "", fill=CORAL, stroke=CORAL)
    p.add_ellipse(736, 112, 20, 20, "", fill=BLUE, stroke=BLUE)
    p.add_ellipse(705, 137, 20, 20, "", fill=YELLOW, stroke=AMBER)
    p.add_ellipse(646, 108, 20, 20, "", fill=PURPLE, stroke=PURPLE)
    p.add_ellipse(672, 250, 90, 75, "W", fill="#F8FAFC", stroke=MUTED, stroke_width=1.5, font_size=38, font_color=MUTED, bold=True)
    graph(p, 675, 405, scale=0.78, stroke=BLUE_DARK, node_fill="#FFFFFF")
    for dx, dy in [(-40, -20), (20, -28), (0, 25), (50, 15), (-52, 35)]:
        p.add_ellipse(675 + dx, 405 + dy, 18, 18, "", fill=BLUE_DARK, stroke=BLUE_DARK)

    # Panel C
    p.add_text(870, 530, 260, 48, "(c) Cross-tasks", font_size=24, bold=True)
    task_specs = [
        (925, 90, LAVENDER, PURPLE, "Graph-level", "Molecule<br>inhibit HIV?", (-60, -35, 120, 70)),
        (925, 235, MINT, GREEN, "Edge-level", "Did Jobs<br>found Apple?", (-25, -44, 86, 38)),
        (925, 380, SAND, "#F5B400", "Node-level", "Is this account<br>malicious?", (20, -48, 58, 38)),
    ]
    for gx, gy, fill, stroke, title, question, hi in task_specs:
        graph(p, gx, gy, scale=0.72, highlight=hi, stroke=INK, node_fill="#FFFFFF")
        p.add_text(1015, gy - 35, 170, 28, title, font_size=20, bold=True, align="left")
        p.add_line(1015, gy - 5, 1125, gy - 5, stroke=INK, stroke_width=1.3, arrow=False)
        p.add_text(1015, gy + 0, 190, 70, question, font_size=19, italic=True, align="left", valign="top")

    return p


def fig2() -> Page:
    p = Page("Fig 2 - Language prompt and graph prompt", 980, 430, "fig2")
    p.add_rect(20, 20, 445, 365, "", fill="#FFFFFF", stroke="#CBD5E1", stroke_width=1.5)
    p.add_text(40, 40, 100, 48, "Prompt", font_size=24, bold=True, italic=True, font_color="#F5B400", align="left")
    p.add_rect(150, 35, 285, 80, "Help me answer a multiple choice<br>Question: Greenhouses are great for plants like<br>A. Pizza   B. Lollipops   C. French beans", fill=SAND, stroke=AMBER, stroke_width=1.5, font_size=14, align="left")
    p.add_line(292, 115, 292, 155, stroke=BLUE_DARK, stroke_width=2.0)
    p.add_rect(150, 155, 285, 88, "Pre-trained Large<br>Language Model", fill="#79B3A6", stroke="#79B3A6", stroke_width=1.5, font_size=22, font_color="#FFFFFF", bold=True)
    p.add_text(168, 178, 56, 48, "LLM", font_size=18, bold=True, font_color="#FFFFFF")
    p.add_line(292, 243, 292, 285, stroke=BLUE_DARK, stroke_width=2.0)
    p.add_text(40, 290, 100, 45, "Answer", font_size=24, bold=True, italic=True, font_color=RED, align="left")
    p.add_rect(150, 285, 285, 55, "The correct answer is C. French beans.", fill=PEACH, stroke=CORAL, stroke_width=1.5, font_size=15, align="left")
    p.add_text(20, 388, 445, 30, "(a) Prompting for language models", font_size=16, bold=True)

    p.add_rect(500, 20, 450, 365, "", fill="#FFFFFF", stroke="#CBD5E1", stroke_width=1.5)
    p.add_text(585, 25, 80, 45, "Fine-tuning", font_size=14, font_color=BLUE_DARK)
    p.add_text(812, 25, 90, 45, "Prompt tuning", font_size=14, font_color=BLUE_DARK)
    p.add_line(520, 58, 545, 110, stroke=INK, stroke_width=2.0)
    p.add_line(930, 58, 902, 295, stroke=INK, stroke_width=2.0)
    boxes = [
        (552, 92, 165, 58, "Pretrained<br>Graph Model", "#FF9AA2", "Tuned"),
        (552, 210, 165, 70, "", "#FFFFFF", ""),
        (765, 92, 165, 58, "Pretrained<br>Graph Model", "#9ED4D7", "Frozen"),
        (765, 210, 165, 70, "", "#FFFFFF", ""),
    ]
    for x, y, w, h, label, fill, _ in boxes:
        p.add_rect(x, y, w, h, label, fill=fill, stroke=INK, stroke_width=1.6, dashed=(label.startswith("Task")), font_size=16)
    graph(p, 635, 245, scale=0.55, stroke=INK, node_fill="#FFFFFF")
    graph(p, 848, 245, scale=0.50, stroke=INK, node_fill="#FFFFFF", highlight=(12, -30, 80, 60))
    p.add_shape("hexagon", 905, 226, 28, 28, "", fill=ORANGE, stroke=ORANGE)
    p.add_text(564, 292, 145, 30, "Task domain", font_size=14)
    p.add_text(775, 292, 145, 30, "Prompted task domain", font_size=14)
    p.add_line(634, 210, 634, 152, stroke=INK, stroke_width=2.0)
    p.add_line(848, 210, 848, 152, stroke=INK, stroke_width=2.0)
    p.add_line(717, 121, 765, 121, stroke=INK, stroke_width=2.0)
    p.add_line(717, 245, 765, 245, stroke=INK, stroke_width=2.0)
    p.add_rect(650, 318, 150, 36, "Legend: red = tuned, teal = frozen, hexagon = prompt", fill="#FFFFFF", stroke="#CBD5E1", stroke_width=1.2, font_size=11)
    p.add_text(500, 388, 450, 30, "(b) Prompt tuning for graph models", font_size=16, bold=True)
    return p


def fig5() -> Page:
    p = Page("Fig 5 - Why prompt learning", 1180, 1260, "fig5")
    p.add_rect(20, 20, 1140, 1200, "", fill="#FFFFFF", stroke="#FFFFFF", stroke_width=0)

    # A: shallow embeddings
    p.add_text(390, 30, 420, 40, "(a) Shallow Node Embedding Methods", font_size=24, bold=True)
    graph(p, 95, 150, scale=0.82)
    p.add_rect(190, 70, 430, 170, "", fill="#FFFFFF", stroke=INK, stroke_width=2, dashed=True)
    p.add_text(215, 82, 365, 75, "Shallow Node Embedding<br>(nodes with free parameters)", font_size=22, bold=True)
    p.add_text(230, 176, 150, 30, "e.g. DeepWalk", font_size=18, bold=True, italic=True)
    feature_matrix(p, 410, 145, cols=2, rows=4, scale=1.15)
    p.add_text(500, 150, 48, 45, "...", font_size=28, bold=True)
    feature_matrix(p, 560, 145, cols=1, rows=4, scale=1.15)
    p.add_line(620, 155, 690, 155, stroke=INK, stroke_width=2.2)
    p.add_rect(690, 70, 450, 185, "", fill="#FFFFFF", stroke=INK, stroke_width=2, dashed=True)
    p.add_text(780, 82, 260, 35, "Downstream Tasks", font_size=24, bold=True)
    for i, (cx, title, hi) in enumerate([(770, "Node-level", (12, -42, 70, 40)), (910, "Edge-level", (-20, -40, 88, 38)), (1050, "Graph-level", (-66, -44, 132, 82))]):
        graph(p, cx, 145, scale=0.48, highlight=hi)
        p.add_text(cx - 52, 205, 110, 28, title, font_size=15, italic=True)
    p.add_text(820, 226, 250, 26, "Flexibility", font_size=19, bold=True, font_color=RED)

    # B: GNNs
    p.add_text(410, 282, 420, 40, "(b) Deep Graph Neural Networks", font_size=24, bold=True)
    graph(p, 95, 420, scale=0.82)
    p.add_rect(190, 330, 950, 190, "", fill="#FFFFFF", stroke=INK, stroke_width=2, dashed=True)
    p.add_text(215, 345, 310, 35, "Graph Neural Networks", font_size=24, bold=True, align="left")
    small_mlp(p, 385, 435, scale=1.15)
    p.add_text(230, 478, 260, 38, "Expressiveness", font_size=22, bold=True, font_color=RED)
    p.add_line(650, 425, 805, 425, stroke=INK, stroke_width=2.0, arrow=True)
    p.add_line(805, 425, 650, 425, stroke=INK, stroke_width=2.0, arrow=True)
    p.add_text(662, 380, 130, 70, "Task-specific<br>Supervision", font_size=20, bold=True, italic=True)
    p.add_text(850, 345, 280, 35, "Specific Downstream Task", font_size=24, bold=True, align="left")
    graph(p, 970, 425, scale=0.70, highlight=(12, -42, 70, 40))
    p.add_text(1060, 390, 58, 78, "?<br>e.g. Node<br>Classification", font_size=15, italic=True, font_color=GREEN, align="left")

    # C: pre-training and prompt
    p.add_text(250, 1192, 680, 42, "(c) Comparison between fine-tune and prompt", font_size=24, bold=True)
    p.add_rect(60, 600, 320, 500, "", fill="#FFFFFF", stroke=INK, stroke_width=2, dashed=True)
    p.add_text(95, 615, 250, 62, "Pre-training<br>Graph Model", font_size=24, bold=True)
    graph(p, 220, 760, scale=0.78)
    small_mlp(p, 190, 930, scale=1.05)
    p.add_line(220, 810, 220, 850, stroke=RED, stroke_width=2.0)
    p.add_line(220, 1010, 220, 1050, stroke=RED, stroke_width=3.0)
    p.add_text(122, 1040, 220, 44, "Expressiveness", font_size=22, bold=True, font_color=RED)
    p.add_text(132, 990, 190, 36, "Pretext Task", font_size=18, bold=True, italic=True)

    p.add_rect(420, 600, 700, 245, "", fill="#FFFFFF", stroke=INK, stroke_width=2, dashed=True)
    p.add_text(580, 615, 380, 35, "Fine-tuning for Specific Tasks", font_size=24, bold=True)
    for x, title, hi in [(560, "Node-level Prediction", (10, -28, 68, 48)), (870, "Edge-level Prediction", (-35, -38, 88, 40))]:
        graph(p, x, 715, scale=0.58, highlight=hi)
        p.add_rect(x - 70, 760, 210, 56, "Pre-trained<br>Graph Model", fill=PEACH, stroke=INK, stroke_width=1.5, font_size=17, bold=True)
        p.add_line(x + 35, 738, x + 35, 760, stroke=RED, stroke_width=1.8)
        p.add_text(x - 86, 817, 230, 26, title, font_size=16, italic=True)
    p.add_text(1055, 710, 50, 40, "...", font_size=26, bold=True)

    p.add_rect(420, 875, 700, 285, "", fill="#FFFFFF", stroke=INK, stroke_width=2, dashed=True)
    p.add_text(560, 890, 420, 35, "Prompt Tuning for Downstream Tasks", font_size=24, bold=True)
    for x, title, hi in [(560, "Node-level Prediction", (8, -25, 62, 48)), (870, "Graph-level Prediction", (-65, -40, 130, 78))]:
        graph(p, x, 970, scale=0.58, highlight=hi, prompt=True)
        p.add_shape("hexagon", x + 110, 944, 42, 42, "", fill=YELLOW, stroke=YELLOW)
        p.add_text(x + 70, 940, 38, 48, "+", font_size=30, bold=True)
        p.add_text(x - 95, 1068, 250, 30, title, font_size=16, italic=True)
    p.add_rect(535, 1025, 470, 48, "Pre-trained Graph Model", fill="#9ED4D7", stroke=INK, stroke_width=1.5, font_size=20, bold=True, font_color="#FFFFFF")
    p.add_text(530, 1118, 505, 34, "Flexibility across tasks/domains", font_size=21, bold=True, font_color=RED)
    p.add_text(1055, 960, 50, 40, "...", font_size=26, bold=True)
    p.add_rect(70, 1110, 250, 34, "Legend: red outline = tuned, teal box = frozen, yellow hexagon = prompt", fill="#FFFFFF", stroke="#CBD5E1", stroke_width=1, font_size=11, align="left")
    return p


def fig6() -> Page:
    p = Page("Fig 6 - Graph pre-training methods", 1160, 680, "fig6")
    p.add_rect(20, 20, 1120, 620, "", fill="#FFFFFF", stroke="#FFFFFF", stroke_width=0)
    p.add_rect(70, 70, 290, 42, "Task-specific Fine-tuning", fill="#FFFFFF", stroke=INK, stroke_width=1.5, font_size=17, bold=True)
    p.add_rect(405, 70, 290, 42, "Task-agnostic Prompting", fill="#FFFFFF", stroke=INK, stroke_width=1.5, font_size=17, bold=True)
    p.add_line(215, 112, 215, 135, stroke=INK, stroke_width=1.8)
    p.add_line(550, 112, 550, 135, stroke=INK, stroke_width=1.8)
    p.add_rect(70, 135, 625, 445, "", fill=PEACH, stroke=INK, stroke_width=1.5)
    p.add_text(95, 145, 260, 38, "Graph Pre-training", font_size=23, bold=True, align="left")

    rows = [(190, "Node-level"), (315, "Edge-level"), (440, "Graph-level")]
    for y, label in rows:
        p.add_rect(90, y, 585, 105, "", fill="#FFFFFF", stroke=INK, stroke_width=1.5, dashed=True)
        p.add_text(100, y + 34, 130, 32, label, font_size=17, align="left")
        graph(p, 275, y + 52, scale=0.48, highlight=(10, -38, 62, 44) if label != "Edge-level" else (-24, -40, 90, 38))
        p.add_line(330, y + 52, 380, y + 52, stroke=INK, stroke_width=1.8)
        graph(p, 430, y + 52, scale=0.44, features=True)
        p.add_line(485, y + 52, 535, y + 52, stroke=INK, stroke_width=1.8)
        graph(p, 590, y + 52, scale=0.44, features=True)
    p.add_text(235, 550, 170, 28, "Contrastive Method", font_size=16)
    p.add_text(480, 550, 170, 28, "Predictive Method", font_size=16)

    p.add_rect(740, 95, 360, 470, "", fill=GRAY_BG, stroke="#CBD5E1", stroke_width=1.5)
    p.add_text(770, 112, 310, 38, "Representative Objectives", font_size=22, bold=True)
    cards = [
        (770, 165, "Graph Reconstruction", "Recover masked nodes, edges, or attributes<br>from corrupted graph views.", BLUE),
        (770, 265, "Auxiliary Property Prediction", "Predict graph statistics or domain properties<br>as self-supervision.", TEAL),
        (770, 365, "Masked Feature Regression", "Mask node or edge features and reconstruct<br>continuous attributes.", AMBER),
        (770, 465, "Forecasting / Sequential Pre-training", "Learn temporal or sequence-aware graph<br>representations before adaptation.", CORAL),
    ]
    for x, y, title, body, color in cards:
        p.add_rect(x, y, 300, 78, "", fill="#FFFFFF", stroke=color, stroke_width=1.6)
        p.add_rect(x, y, 8, 78, "", fill=color, stroke=color, stroke_width=0, rounded=False)
        p.add_text(x + 18, y + 8, 260, 23, title, font_size=15, bold=True, align="left")
        p.add_text(x + 18, y + 34, 260, 36, body, font_size=11.5, font_color=MUTED, align="left")
        graph(p, x + 255, y + 39, scale=0.27, stroke=INK, node_fill="#FFFFFF")
    return p


def fig7() -> Page:
    p = Page("Fig 7 - Prompt tokens and insertion patterns", 880, 560, "fig7")
    p.add_rect(15, 18, 340, 500, "", fill="#FFFFFF", stroke="#0F2547", stroke_width=2, dashed=True)
    p.add_text(85, 40, 210, 35, "Original Graph", font_size=20, bold=True)
    graph(p, 175, 150, scale=0.75, features=True)
    p.add_text(210, 145, 115, 30, "Node feature", font_size=18, align="left")
    p.add_rect(35, 275, 300, 210, "", fill="#FFFFFF", stroke=INK, stroke_width=1.5)
    p.add_text(90, 290, 210, 30, "Prompt Graph", font_size=20, bold=True)
    graph(p, 150, 390, scale=0.70, features=True, prompt=True)
    p.add_text(182, 348, 135, 30, "Token Structure", font_size=15, font_color=RED, align="left")
    p.add_text(195, 406, 125, 28, "Prompt Token", font_size=15, font_color=PURPLE, align="left")
    p.add_text(205, 455, 120, 28, "Token feature", font_size=15, font_color=GREEN, align="left")
    p.add_line(185, 362, 138, 373, stroke=RED, stroke_width=2.0)
    p.add_line(198, 416, 172, 398, stroke=PURPLE, stroke_width=2.0, dashed=True)
    p.add_line(207, 454, 188, 462, stroke=GREEN, stroke_width=2.0, dashed=True)

    p.add_rect(385, 18, 475, 500, "", fill="#FFFFFF", stroke="#0F2547", stroke_width=2, dashed=True)
    p.add_text(445, 35, 360, 32, "Four Kinds of Inserting Patterns", font_size=20, bold=True)
    panels = [
        (405, 80, "By Cross Links", True, False, False),
        (635, 80, "By Feature Adding", False, True, False),
        (405, 315, "By Concatenating", False, False, False),
        (635, 315, "By Multiplication", False, True, True),
    ]
    for x, y, title, cross, add_feat, mult in panels:
        p.add_rect(x, y, 210, 155, "", fill="#FFFFFF", stroke=INK, stroke_width=1.4, rounded=False)
        p.add_text(x + 35, y + 8, 140, 24, "Prompted Graph", font_size=16)
        graph(p, x + 90, y + 82, scale=0.48, features=True, prompt=cross)
        if add_feat:
            p.add_rect(x + 98, y + 72, 88, 56, "", fill=SAND, stroke="#F5B400", stroke_width=1.5, dashed=True)
            p.add_shape("hexagon", x + 160, y + 88, 24, 24, "", fill=PURPLE if not mult else "#FFFFFF", stroke=PURPLE, stroke_width=3)
            p.add_text(x + 138, y + 91, 18, 20, "+" if not mult else "x", font_size=17, font_color=RED, bold=True)
        if not cross and not add_feat:
            p.add_rect(x + 108, y + 73, 84, 56, "", fill=SAND, stroke="#F5B400", stroke_width=1.5, dashed=True)
            p.add_shape("hexagon", x + 153, y + 88, 24, 24, "", fill="#FFFFFF", stroke=PURPLE, stroke_width=3)
        p.add_text(x + 20, y + 162, 170, 25, title, font_size=15, bold=True)
    return p


def write_mxfile(path: Path, pages: list[Page]) -> None:
    mxfile = ET.Element(
        "mxfile",
        host="app.diagrams.net",
        modified="2026-07-04T00:00:00.000Z",
        agent="Codex",
        version="24.7.17",
        type="device",
    )
    for page in pages:
        diagram = ET.SubElement(mxfile, "diagram", id=page.page_id, name=page.name)
        diagram.append(page.mx_model())
    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ")
    path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def svg_text_lines(label: str) -> list[str]:
    text = strip_html(label)
    return [line for line in text.split("\n") if line != ""]


def svg_color(value: str) -> str:
    return "none" if value == "none" else value


def render_svg(page: Page, path: Path) -> None:
    markers: dict[str, str] = {}

    def marker_id(color: str) -> str:
        key = color.replace("#", "")
        if key not in markers:
            markers[key] = color
        return f"arrow-{key}"

    body: list[str] = []
    for item in page.svg:
        a = item.attrs
        if item.kind == "line":
            dash = ' stroke-dasharray="8 5"' if a["dashed"] else ""
            marker = f' marker-end="url(#{marker_id(a["stroke"])})"' if a["arrow"] else ""
            body.append(
                f'<line x1="{a["x1"]:.2f}" y1="{a["y1"]:.2f}" x2="{a["x2"]:.2f}" y2="{a["y2"]:.2f}" '
                f'stroke="{a["stroke"]}" stroke-width="{a["stroke_width"]}" fill="none"{dash}{marker}/>'
            )
        elif item.kind in {"rect", "text", "ellipse", "shape"}:
            if item.kind == "rect":
                rx = 10 if a.get("rounded") else 0
                dash = ' stroke-dasharray="8 5"' if a.get("dashed") else ""
                opacity = f' opacity="{a["opacity"] / 100:.2f}"' if a.get("opacity") is not None else ""
                body.append(
                    f'<rect x="{a["x"]:.2f}" y="{a["y"]:.2f}" width="{a["w"]:.2f}" height="{a["h"]:.2f}" '
                    f'rx="{rx}" fill="{svg_color(a["fill"])}" stroke="{svg_color(a["stroke"])}" '
                    f'stroke-width="{a["stroke_width"]}"{dash}{opacity}/>'
                )
            elif item.kind == "ellipse":
                body.append(
                    f'<ellipse cx="{a["x"] + a["w"] / 2:.2f}" cy="{a["y"] + a["h"] / 2:.2f}" '
                    f'rx="{a["w"] / 2:.2f}" ry="{a["h"] / 2:.2f}" fill="{svg_color(a["fill"])}" '
                    f'stroke="{svg_color(a["stroke"])}" stroke-width="{a["stroke_width"]}"/>'
                )
            elif item.kind == "shape":
                x, y, w, h = a["x"], a["y"], a["w"], a["h"]
                if a["shape"] == "hexagon":
                    pts = [
                        (x + w * 0.25, y),
                        (x + w * 0.75, y),
                        (x + w, y + h * 0.5),
                        (x + w * 0.75, y + h),
                        (x + w * 0.25, y + h),
                        (x, y + h * 0.5),
                    ]
                elif a["shape"] == "triangle":
                    pts = [(x + w / 2, y), (x + w, y + h), (x, y + h)]
                else:
                    pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
                body.append(
                    '<polygon points="'
                    + " ".join(f"{px:.2f},{py:.2f}" for px, py in pts)
                    + f'" fill="{svg_color(a["fill"])}" stroke="{svg_color(a["stroke"])}" stroke-width="{a["stroke_width"]}"/>'
                )
            if item.kind != "text":
                label = a.get("label", "")
            else:
                label = a["label"]
            if label:
                lines = svg_text_lines(label)
                if lines:
                    weight = "700" if a.get("bold") else "400"
                    style_attr = "italic" if a.get("italic") else "normal"
                    font_size = a["font_size"]
                    if a.get("align") == "left":
                        tx = a["x"] + 8
                        anchor = "start"
                    elif a.get("align") == "right":
                        tx = a["x"] + a["w"] - 8
                        anchor = "end"
                    else:
                        tx = a["x"] + a["w"] / 2
                        anchor = "middle"
                    total_h = len(lines) * font_size * 1.18
                    if a.get("valign") == "top":
                        ty = a["y"] + font_size + 4
                    else:
                        ty = a["y"] + a["h"] / 2 - total_h / 2 + font_size
                    body.append(
                        f'<text x="{tx:.2f}" y="{ty:.2f}" text-anchor="{anchor}" '
                        f'font-family="{FONT}, Arial, sans-serif" font-size="{font_size}" '
                        f'font-weight="{weight}" font-style="{style_attr}" fill="{a.get("font_color", INK)}">'
                    )
                    for i, line in enumerate(lines):
                        dy = 0 if i == 0 else font_size * 1.18
                        body.append(f'<tspan x="{tx:.2f}" dy="{dy:.2f}">{html.escape(line)}</tspan>')
                    body.append("</text>")

    defs = ["<defs>"]
    for key, color in markers.items():
        defs.append(
            f'<marker id="arrow-{key}" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">'
            f'<path d="M0,0 L0,6 L9,3 z" fill="{color}"/></marker>'
        )
    defs.append("</defs>")
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{page.width}" height="{page.height}" viewBox="0 0 {page.width} {page.height}">',
        *defs,
        '<rect width="100%" height="100%" fill="#FFFFFF"/>',
        *body,
        "</svg>",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(svg), encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    PREVIEW.mkdir(parents=True, exist_ok=True)
    pages = [fig1(), fig2(), fig5(), fig6(), fig7()]
    write_mxfile(OUT / "gpl_survey_figures_drawio.drawio", pages)
    for page in pages:
        slug = page.page_id + "_" + re.sub(r"[^a-z0-9]+", "_", page.name.lower()).strip("_")
        write_mxfile(OUT / f"{slug}.drawio", [page])
        render_svg(page, PREVIEW / f"{slug}.svg")
    print(f"Wrote {len(pages)} Draw.io pages to {OUT}")


if __name__ == "__main__":
    main()

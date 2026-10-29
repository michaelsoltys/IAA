"""Flex -> Bison pipeline, two variants (slides_parse.md):
  parse-pipeline-parser.svg  Bison stage highlighted       ("The Big Picture")
  parse-pipeline-tools.svg   Flex and Bison highlighted    ("The Tool Chain")
vertical() is kept for a narrow-column layout but is not used in the deck."""
import matplotlib.pyplot as plt
from parse_style import (box, arrow, save, SLATE, MUTED, YELLOW_FILL,
                         YELLOW_EDGE, GRAY_FILL, GRAY_EDGE)

STAGES = [  # (title, detail, is_tool)
    ("Source code", '{"age": 30}', False),
    ("Flex / Lex", "regex rules", True),
    ("Token stream", "LBRACE STRING COLON\nNUMBER RBRACE", False),
    ("Bison / Yacc", "CFG rules", True),
    ("Parse tree", "or result", False),
]


def style(i, highlight):
    title, detail, tool = STAGES[i]
    if i in highlight:
        return YELLOW_FILL, YELLOW_EDGE, 2.0
    if tool:
        return "white", SLATE, 1.4
    return GRAY_FILL, GRAY_EDGE, 1.2


def stage(ax, x, y, w, h, i, highlight):
    title, detail, tool = STAGES[i]
    fc, ec, lw = style(i, highlight)
    box(ax, x, y, w, h, "", fc, ec, lw=lw)
    ax.text(x, y + 0.2 * h, title, ha="center", va="center", fontsize=15,
            color=SLATE, weight="bold" if tool else "normal")
    mono = not tool and i != 4
    ax.text(x, y - 0.22 * h, detail, ha="center", va="center",
            fontsize=11.5 if mono else 12.5, color=MUTED,
            family="DejaVu Sans Mono" if mono else None,
            style="normal" if mono else "italic", linespacing=1.15)


def horizontal(highlight, name):
    fig = plt.figure(figsize=(13, 1.9))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13); ax.set_ylim(0, 1.9); ax.axis("off")
    w, h, gap = 2.3, 1.45, 0.35
    for i in range(5):
        x = 0.05 + w / 2 + i * (w + gap)
        stage(ax, x, 0.95, w, h, i, highlight)
        if i < 4:
            arrow(ax, x + w / 2 + 0.04, 0.95, x + w / 2 + gap - 0.04, 0.95)
    save(fig, name)


def vertical(highlight, name):
    W, H = 3.6, 6.4
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    w, h, gap = 3.4, 1.0, 0.3
    for i in range(5):
        y = H - 0.08 - h / 2 - i * (h + gap)
        stage(ax, W / 2, y, w, h, i, highlight)
        if i < 4:
            arrow(ax, W / 2, y - h / 2 - 0.03, W / 2, y - h / 2 - gap + 0.03)
    save(fig, name)


horizontal({3}, "parse-pipeline-parser")
horizontal({1, 3}, "parse-pipeline-tools")

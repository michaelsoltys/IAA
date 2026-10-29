"""Shared style for the parsing-deck figures (slides_parse.md).

Colors follow the drawio figures in this folder: pale yellow fill with a
gold stroke for highlighted items, slate for lines and text.
Run each parse-*.py script from Figures/src; output lands in Figures/.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "path"})

SLATE = "#334155"
MUTED = "#64748b"
LIGHT = "#94a3b8"
YELLOW_FILL = "#fff2cc"
YELLOW_EDGE = "#d6b656"
GRAY_FILL = "#f1f5f9"
GRAY_EDGE = "#cbd5e1"
BLUE_FILL = "#dae8fc"
BLUE_EDGE = "#6c8ebf"

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def box(ax, x, y, w, h, text, fill=GRAY_FILL, edge=GRAY_EDGE, size=12,
        color=SLATE, weight="normal", lw=1.4, family=None, pad=0.02,
        style="normal", margin=0.18):
    """Rounded box centered at (x, y).  If w is None, fit the text width
    (axes limits and aspect must already be set)."""
    t = ax.text(x, y, text, ha="center", va="center", fontsize=size,
                color=color, weight=weight, family=family, style=style,
                zorder=3)
    if w is None:
        r = ax.figure.canvas.get_renderer()
        bb = t.get_window_extent(r).transformed(ax.transData.inverted())
        w = bb.width + 2 * margin
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle=f"round,pad={pad},rounding_size=0.08",
                                fc=fill, ec=edge, lw=lw, zorder=2))
    return w


def arrow(ax, x0, y0, x1, y1, color=SLATE, lw=1.4, rad=0.0, ms=14):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=ms,
                                connectionstyle=f"arc3,rad={rad}",
                                shrinkA=0, shrinkB=0))


def save(fig, name):
    for ext in ("svg", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=200,
                    bbox_inches="tight", pad_inches=0.05, transparent=False,
                    facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- trees
class Node:
    def __init__(self, label, children=(), lexeme=None, terminal=False,
                 accent=False):
        self.label, self.children = label, list(children)
        self.lexeme, self.terminal, self.accent = lexeme, terminal, accent


def T(label, lexeme=None):
    return Node(label, lexeme=lexeme, terminal=True)


def N(label, *children, accent=False):
    return Node(label, children, accent=accent)


def _layout(node, depth, xs):
    node.depth = depth
    if not node.children:
        node.x = xs[0]
        xs[0] += 1
    else:
        for c in node.children:
            _layout(c, depth + 1, xs)
        node.x = (node.children[0].x + node.children[-1].x) / 2


def draw_tree(root, name, ipu=0.62, xgap=1.0, ygap=1.0, size=12,
              leaves_bottom=False, notes=()):
    xs = [0]
    _layout(root, 0, xs)
    nodes = []

    def walk(n):
        nodes.append(n)
        for c in n.children:
            walk(c)
    walk(root)
    maxd = max(n.depth for n in nodes)
    if leaves_bottom:
        for n in nodes:
            if n.terminal:
                n.depth = maxd
    pos = {id(n): (n.x * xgap, -n.depth * ygap) for n in nodes}
    allx = [p[0] for p in pos.values()] + [nx for nx, _, _ in notes]
    ally = [p[1] for p in pos.values()]
    x0, x1 = min(allx) - 0.7, max(allx) + 0.7 + (1.6 if notes else 0)
    y0, y1 = min(ally) - 0.75 * ygap, max(ally) + 0.35 * ygap
    # ipu = inches per data unit, so text size is independent of tree width
    fig = plt.figure(figsize=((x1 - x0) * ipu, (y1 - y0) * ipu))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.canvas.draw()
    h = 0.4 * ygap
    for n in nodes:
        x, y = pos[id(n)]
        for c in n.children:
            cx, cy = pos[id(c)]
            ax.plot([x, cx], [y - h / 2, cy + h / 2], color=LIGHT, lw=1.2,
                    zorder=1)
    for n in nodes:
        x, y = pos[id(n)]
        if n.terminal:
            box(ax, x, y, None, h, n.label, YELLOW_FILL, YELLOW_EDGE,
                size=size * 0.75, family="DejaVu Sans Mono", margin=0.12)
            if n.lexeme is not None:
                ax.text(x, y - 0.33 * ygap, n.lexeme, ha="center", va="top",
                        fontsize=size * 0.9, color=MUTED,
                        family="DejaVu Sans Mono")
        elif n.accent:
            box(ax, x, y, None, h, n.label, BLUE_FILL, BLUE_EDGE, size=size,
                style="italic", margin=0.14)
        else:
            ax.text(x, y, n.label, ha="center", va="center", fontsize=size,
                    color=SLATE, style="italic", zorder=3,
                    bbox=dict(boxstyle="round,pad=0.2", fc="white",
                              ec="none"))
    for (x, y, text) in notes:
        ax.text(x, y, text, ha="left", va="center", fontsize=size * 0.85,
                color=MUTED, style="italic")
    save(fig, name)

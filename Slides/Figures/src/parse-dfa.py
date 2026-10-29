"""Small DFA for two Flex rules:  [0-9]+ -> NUMBER   and   "true" -> TRUE.
States are named by the prefix read so far.  Missing edges go to a reject state.
Output: ../parse-dfa.svg/.png  (slides_parse.md, "Flex: The Lexer"; see Section 9.3)"""
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from parse_style import save, SLATE, MUTED, YELLOW_FILL, YELLOW_EDGE

R = 0.42
fig = plt.figure(figsize=(6.9, 3.15))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(-1.0, 8.6); ax.set_ylim(-2.15, 2.2); ax.set_aspect("equal")
ax.axis("off")

S = {"start": (0.0, 0.0), "N": (2.2, 1.05),
     "t": (2.0, -1.0), "tr": (3.6, -1.0), "tru": (5.2, -1.0),
     "true": (6.8, -1.0)}
ACCEPT = {"N": "NUMBER", "true": "TRUE"}
LABEL = {"start": "", "N": "", "t": "t", "tr": "tr", "tru": "tru",
         "true": "true"}

for k, (x, y) in S.items():
    acc = k in ACCEPT
    ax.add_patch(Circle((x, y), R, fc=YELLOW_FILL if acc else "white",
                        ec=YELLOW_EDGE if acc else SLATE, lw=1.6, zorder=2))
    if acc:
        ax.add_patch(Circle((x, y), R - 0.07, fc="none",
                            ec=YELLOW_EDGE, lw=1.4, zorder=3))
    ax.text(x, y, LABEL[k], ha="center", va="center", fontsize=11,
            color=SLATE, family="DejaVu Sans Mono", zorder=4)


def edge(a, b, label, rad=0.0, lpos=(0, 0.2)):
    (x0, y0), (x1, y1) = S[a], S[b]
    d = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / d, (y1 - y0) / d
    ax.add_patch(FancyArrowPatch((x0 + R * ux, y0 + R * uy),
                                 (x1 - R * ux, y1 - R * uy),
                                 arrowstyle="-|>", mutation_scale=14,
                                 color=SLATE, lw=1.4,
                                 connectionstyle=f"arc3,rad={rad}"))
    mx, my = (x0 + x1) / 2 + lpos[0], (y0 + y1) / 2 + lpos[1]
    ax.text(mx, my, label, ha="center", va="center", fontsize=14,
            color=SLATE, family="DejaVu Sans Mono")


def loop(k, label):
    x, y = S[k]
    a0, a1 = math.radians(60), math.radians(120)
    ax.add_patch(FancyArrowPatch((x + R * math.cos(a0), y + R * math.sin(a0)),
                                 (x + R * math.cos(a1), y + R * math.sin(a1)),
                                 arrowstyle="-|>", mutation_scale=12,
                                 color=SLATE, lw=1.4,
                                 connectionstyle="arc3,rad=2.4", zorder=5))
    ax.text(x + 0.42, y + R + 0.5, label, ha="left", va="center", fontsize=14,
            color=SLATE, family="DejaVu Sans Mono")


# start arrow
ax.add_patch(FancyArrowPatch((-0.95, 0), (-R, 0), arrowstyle="-|>",
                             mutation_scale=14, color=SLATE, lw=1.4))
ax.text(-0.68, 0.25, "start", ha="center", fontsize=13, color=MUTED,
        style="italic")
edge("start", "N", "[0-9]", lpos=(-0.35, 0.22))
loop("N", "[0-9]")
edge("start", "t", "t", lpos=(-0.25, -0.2))
edge("t", "tr", "r")
edge("tr", "tru", "u")
edge("tru", "true", "e")
ax.text(S["N"][0] + R + 0.2, S["N"][1], "return NUMBER", ha="left",
        va="center", fontsize=14, color=MUTED, style="italic")
ax.text(S["true"][0], S["true"][1] - R - 0.3, "return TRUE", ha="center",
        va="center", fontsize=14, color=MUTED, style="italic")
save(fig, "parse-dfa")

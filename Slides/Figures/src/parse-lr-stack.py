"""LR (shift/reduce) parse of [1, 2] with the deck's grammar:
    json     -> value
    value    -> NUMBER | ... | array
    array    -> LBRACK RBRACK | LBRACK elements RBRACK
    elements -> value | value COMMA elements
Stack bottom is at the bottom of each frame.  The trace is what Bison's
LALR(1) table does: after `value` it shifts on COMMA and reduces
elements -> value on RBRACK (right recursion keeps the whole list on the stack).
Output: ../parse-lr-stack.svg/.png  (slides_parse.md, after "Theory Meets Practice")"""
import matplotlib.pyplot as plt
from parse_style import (box, save, SLATE, MUTED, YELLOW_FILL, YELLOW_EDGE,
                         BLUE_FILL, BLUE_EDGE)

TERMS = {"LBRACK", "RBRACK", "COMMA", "NUMBER"}
# (action, stack after the action, remaining input)
STEPS = [
    ("shift LBRACK", ["LBRACK"], "1 , 2 ] $"),
    ("shift NUMBER", ["LBRACK", "NUMBER"], ", 2 ] $"),
    ("reduce\nvalue → NUMBER", ["LBRACK", "value"], ", 2 ] $"),
    ("shift COMMA", ["LBRACK", "value", "COMMA"], "2 ] $"),
    ("shift NUMBER", ["LBRACK", "value", "COMMA", "NUMBER"], "] $"),
    ("reduce\nvalue → NUMBER", ["LBRACK", "value", "COMMA", "value"], "] $"),
    ("reduce\nelements → value", ["LBRACK", "value", "COMMA", "elements"],
     "] $"),
    ("reduce elements →\nvalue COMMA elements", ["LBRACK", "elements"], "] $"),
    ("shift RBRACK", ["LBRACK", "elements", "RBRACK"], "$"),
    ("reduce array →\nLBRACK elements RBRACK", ["array"], "$"),
    ("reduce\nvalue → array", ["value"], "$"),
    ("reduce\njson → value", ["json"], "$  accept"),
]

COLS, ROWS = 6, 2
CW, CH = 2.0, 0.42          # cell width / height
FW = 2.45                   # frame pitch
DEPTH = 4
FH = DEPTH * CH + 1.3      # frame height incl. labels

fig = plt.figure(figsize=(COLS * FW * 0.9, ROWS * FH * 0.9))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, COLS * FW); ax.set_ylim(0, ROWS * FH); ax.axis("off")

for i, (action, stack, rest) in enumerate(STEPS):
    r, c = divmod(i, COLS)
    cx = c * FW + FW / 2
    base = (ROWS - 1 - r) * FH + 0.62          # bottom of stack area
    ax.text(cx, base + DEPTH * CH + 0.34, f"{i + 1}. {action}",
            ha="center", va="center", fontsize=12, color=SLATE,
            linespacing=1.1, weight="bold" if action.startswith("shift")
            else "normal")
    # stack outline (open top)
    x0, x1 = cx - CW / 2 - 0.06, cx + CW / 2 + 0.06
    ax.plot([x0, x0, x1, x1], [base + DEPTH * CH, base - 0.05,
                                base - 0.05, base + DEPTH * CH],
            color=MUTED, lw=1.2)
    for j, sym in enumerate(stack):
        term = sym in TERMS
        top = j == len(stack) - 1
        box(ax, cx, base + j * CH + CH / 2, CW - 0.06, CH - 0.07, sym,
            YELLOW_FILL if term else BLUE_FILL,
            YELLOW_EDGE if term else BLUE_EDGE, size=11.5,
            family="DejaVu Sans Mono", weight="bold" if top else "normal",
            lw=1.0, pad=0.0)
    ax.text(cx, base - 0.33, "input: " + rest, ha="center", va="center",
            fontsize=11, color=MUTED, family="DejaVu Sans Mono")
save(fig, "parse-lr-stack")

"""How `members` unrolls for three key-value pairs (right recursion):
{"a": 1, "b": 2, "c": 3}.  members -> STRING COLON value
                                    | STRING COLON value COMMA members
Output: ../parse-members-tree.svg/.png  (slides_parse.md, "Recursive Rules")"""
from parse_style import N, T, draw_tree


def pair(k, v, rest=None):
    kids = [T("STRING", f'"{k}"'), T("COLON", ":"),
            N("value", T("NUMBER", str(v)))]
    if rest is not None:
        kids += [T("COMMA", ","), rest]
    return N("members", *kids, accent=True)


tree = pair("a", 1, pair("b", 2, pair("c", 3)))
draw_tree(tree, name="parse-members-tree", xgap=1.4,
          ygap=1.0, size=15,
          notes=[(13.85, -2.0, "base case")])

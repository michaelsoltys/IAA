"""Parse tree for {"name": "Alice", "age": 30} under the deck's JSON grammar.
Output: ../parse-json-tree.svg/.png  (slides_parse.md, "What is a Parser?")"""
from parse_style import N, T, draw_tree

tree = N("json",
         N("value",
           N("object",
             T("LBRACE", "{"),
             N("members",
               T("STRING", '"name"'), T("COLON", ":"),
               N("value", T("STRING", '"Alice"')),
               T("COMMA", ","),
               N("members",
                 T("STRING", '"age"'), T("COLON", ":"),
                 N("value", T("NUMBER", "30")))),
             T("RBRACE", "}"))))

draw_tree(tree, name="parse-json-tree", xgap=1.3,
          ygap=1.0, size=15, leaves_bottom=False)

---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Parser Tools and Context-Free Grammars
  COMP 454: Automata, Languages and Computation
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Parser Tools and CFGs
mdc: false
---

# Parser Tools and CFGs

Parsers — From context-free grammars on the page to working compilers built with Bison and Yacc.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

<!--
A nice opening: parsing is one of the few corners of computer science where
the theory was *finished* before the industry caught up. By the late 1960s
Knuth had already worked out LR(k) parsing in his 1965 paper "On the
Translation of Languages from Left to Right" — and that paper still
underlies essentially every compiler shipped today. Sixty years later, we
are still using a 1965 algorithm to compile Rust.

Donald Knuth wrote that LR paper while procrastinating on TAOCP. He spent
months on it because he wanted to settle, once and for all, when a grammar
could be parsed deterministically left-to-right. The answer turned out to
be: "exactly when it's LR(k)" — and the proof is constructive.
-->


---

# The Big Picture

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A grammar describes the language; a parser generator turns it into a working recognizer.

</div>


- **Context-Free Grammars (CFGs)** define languages
- **Parsers** recognize whether strings belong to those languages
- **Parser generators** automatically create parsers from CFG specifications


CFG Specification → Parser Generator → Working Parser


---

# What is a Parser?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

It reads tokens, checks them against grammar rules, and either accepts or builds a parse tree.

</div>


A parser is a program that:

1. **Reads** a sequence of tokens (from a lexer)
2. **Analyzes** them according to grammar rules
3. **Determines** if the input is valid (syntactically correct)
4. **Optionally** builds a parse tree or performs actions


**Example:** Is a JSON object like name:Alice valid?


---

# CFG Review

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Terminals, non-terminals, productions, and a start symbol — the four ingredients of a grammar.

</div>

A Context-Free Grammar consists of:


- **Terminals:** Basic symbols (tokens)
- **Non-terminals:** Syntactic categories like object, array, value
- **Production rules:** How non-terminals expand
- **Start symbol:** Where parsing begins


Example productions:

- value → STRING or NUMBER or object or array
- object → empty braces or braces with members
- array → empty brackets or brackets with elements


---

# The Tool Chain

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Flex turns characters into tokens; Bison turns tokens into a parse — two tools, one pipeline.

</div>

<div class="grid grid-cols-2 gap-8 mt-8">
<div>


**Flex (Lexer Generator)**
- Input: Regular expressions
- Output: Lexical analyzer (scanner)
- Converts character stream to tokens

**Bison (Parser Generator)**
- Input: CFG rules
- Output: Parser
- Analyzes token stream


</div>
<div>


Source Code

→ Flex/Lex (regex rules)

→ Token Stream

→ Bison/Yacc (CFG rules)

→ Parse Result


</div>
</div>

---

# Flex: The Lexer

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Each regex maps to a token — a direct application of regular languages from Section 9.3.

</div>

Flex uses **regular expressions** to define tokens:

- Match literal braces: return LBRACE, RBRACE
- Match "true": return TRUE token
- Match "false": return FALSE token
- Match quoted strings: return STRING token
- Match numbers: return NUMBER token
- Skip whitespace


This connects to **Regular Languages** (Section 9.3)!


---

# Bison: The Parser

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Each rule is a CFG production — a direct application of context-free grammars from Section 9.4.

</div>

Bison uses **CFG production rules**:

- value: STRING or NUMBER or TRUE or FALSE or object or array
- object: LBRACE RBRACE or LBRACE members RBRACE
- array: LBRACK RBRACK or LBRACK elements RBRACK


This connects to **Context-Free Grammars** (Section 9.4)!


---

# Lex vs Flex

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Lex is the 1975 Bell Labs original; Flex is the open-source rewrite — same `.l` syntax.

</div>

<div class="grid grid-cols-2 gap-8">
<div>

**Lex** (original, 1975)
- Created at Bell Labs
- Part of original Unix
- Proprietary versions exist

</div>
<div>

**Flex** (modern, 1987)
- "Fast Lexical Analyzer"
- Open source replacement
- Faster and more features
- What you should use today

</div>
</div>


**Both use the same .l file format!**


<!--
Lex was written by Mike Lesk and Eric Schmidt in 1975 — yes, *that* Eric
Schmidt, who later ran Google. He was a Bell Labs summer intern at the
time. So when students complain about Flex, remind them that the author
went on to do reasonably well in life.

Flex itself was written by Vern Paxson, who later became famous as the
author of Bro/Zeek, the network intrusion detection system. Apparently
once you've written one good lexer, you can't stop scanning things.
-->

---

# Flex/Lex Code Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A real `.l` file: pattern on the left, C action on the right — that's the whole language.

</div>

**File: json_lexer.l**

```
%%
"true"          { return TRUE; }
"false"         { return FALSE; }
"null"          { return NULL_VAL; }
[0-9]+          { return NUMBER; }
[ \t\n]+        { /* skip whitespace */ }
.               { return yytext[0]; }
%%
```


**Structure:** Pattern on left, action on right

Each line: **regex** → **C code to execute**


---

# Understanding Flex Rules

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Reading the patterns row by row — and noticing they're all just regular expressions.

</div>

| Pattern | Meaning | Token Returned |
|---------|---------|----------------|
| "true" | Literal string | TRUE |
| "false" | Literal string | FALSE |
| [0-9]+ | One or more digits | NUMBER |
| [ \t\n]+ | Whitespace | (skip) |
| . | Any other character | The character itself |


**Key insight:** These are **regular expressions** - the theory from Section 9.3!


---

# Yacc vs Bison

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Yacc is the 1975 LALR(1) original; Bison is the GNU rewrite — backward compatible, more features.

</div>

<div class="grid grid-cols-2 gap-8">
<div>

**Yacc** (original, 1975)
- "Yet Another Compiler-Compiler"
- Created at Bell Labs
- LALR(1) parser generator

**Bison** (modern, 1985)
- GNU replacement for Yacc
- Backward compatible
- Additional features (GLR parsing)
- What you should use today


**Both use the same .y file format!**


</div>
<div style="text-align: center;">

<img src="/gnu_head.png" style="max-height: 200px; margin: 0 auto;" />

<div style="font-size: 0.7em; color: #444; margin-top: 10px; text-align: left;">

**Bison: The Yacc-compatible Parser Generator** -- the official GNU manual is the definitive reference for writing grammars, building parsers, handling conflicts, and using advanced features like GLR parsing and Bison's C++ skeleton.

<div style="font-size: 0.85em; color: gray; margin-top: 6px; text-align: center;">

https://www.gnu.org/software/bison/manual/

</div>

</div>

</div>
</div>

<!--
Yacc was written by Stephen C. Johnson at Bell Labs in 1975, originally to
help build a Fortran 77 compiler. The name "Yet Another Compiler-Compiler"
was a self-deprecating joke — there were already several compiler-compilers
floating around, and Johnson assumed his would just be one more. It
ended up being the one everybody used for the next half-century.

Bison was the GNU Project's clean-room rewrite, started by Robert Corbett
at Berkeley in 1985 and adopted by Richard Stallman. The name is the
obvious pun: Yacc → Bison, both bovine. There's also a much less famous
parser generator called "Buffalo" that nobody uses, which I think is
deeply unfair.

A historical note worth dropping: the LALR(1) algorithm Yacc implements
was developed by Frank DeRemer in his 1969 PhD thesis. DeRemer's insight
was that you could compress LR(1) parse tables by a factor of 10 or more
with almost no loss of expressive power — and that compression is what
made parser generators *practical* on 1970s hardware. Without DeRemer,
Yacc would have needed megabytes of RAM, and we'd probably still be
hand-writing recursive-descent parsers.
-->


---

# Bison/Yacc Code Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A real `.y` file: non-terminal on the left, alternatives separated by `|` — pure CFG productions.

</div>

**File: json_parser.y**

```
%%
json: value ;

value: STRING
     | NUMBER
     | TRUE
     | FALSE
     | object
     | array
     ;

object: LBRACE RBRACE
      | LBRACE members RBRACE
      ;
%%
```

---

# Understanding Bison Rules

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Reading each Bison rule line by line — direct translations of CFG productions into ASCII.

</div>

**Rule structure:** non-terminal: alternatives ;

| Rule | Meaning |
|------|---------|
| json: value | A JSON doc is a value |
| value: STRING or NUMBER... | Value can be several things |
| object: LBRACE RBRACE | Empty braces = empty object |
| object: LBRACE members RBRACE | Braces with members inside |


**Key insight:** These are **CFG production rules** - the theory from Section 9.4!


---

# Complete File Structure

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Both `.l` and `.y` files share the same three-section layout split by `%%`.

</div>

<div class="grid grid-cols-2 gap-4">
<div>

**Flex file (.l)**

```
%{
  /* C declarations */
  #include "parser.tab.h"
%}
%%
  /* regex rules */
%%
  /* C functions */
```

</div>
<div>

**Bison file (.y)**

```
%{
  /* C declarations */
%}
%token STRING NUMBER
%%
  /* grammar rules */
%%
  /* C functions */
```

</div>
</div>


Both have three sections separated by %%


---

# JSON Grammar in Bison

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Side-by-side: textbook CFG on the left, the same rules in Bison `.y` syntax on the right.

</div>

<div class="grid grid-cols-2 gap-4">
<div>

**CFG (Theory)**

- json → value
- value → STRING or NUMBER or TRUE or FALSE or NULL or object or array
- object → empty or with members
- members → member or member, members
- array → empty or with elements
- elements → value or value, elements

</div>
<div>

**Bison (Practice)**

- json: value;
- value: STRING or NUMBER or TRUE or FALSE or NULL_VAL or object or array;
- object: braces empty or braces with members;
- members: STRING COLON value or STRING COLON value COMMA members;

</div>
</div>

---

# Recursive Rules

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Self-referential productions are how CFGs express lists of unbounded length.

</div>


**Key insight:** Lists are naturally recursive!

**Members** (key-value pairs in objects):
- Base case: One member
- Recursive: One member, comma, more members

**Elements** (values in arrays):
- Base case: One element
- Recursive: One value, comma, more values


This is exactly how CFGs handle **unbounded repetition**!


---

# Building a JSON Parser

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Five-step recipe: write rules, generate code, compile, run — that's a working parser.

</div>


1. **Write lexer rules** (json_lexer.l) - uses regular expressions
2. **Write grammar rules** (json_parser.y) - uses CFG
3. **Generate code:** flex and bison commands
4. **Compile:** gcc to create executable
5. **Run:** pipe JSON input to parser


---

# Theory Meets Practice

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Every concept in Chapter 9 has a direct counterpart in real lexer and parser tools.

</div>

| Theory (Chapter 9) | Practice (Parser Tools) |
|-------------------|------------------------|
| Regular Expressions | Flex/Lex patterns |
| Finite Automata | Lexer state machine |
| Context-Free Grammar | Bison/Yacc rules |
| Pushdown Automata | Parser stack |
| Derivations | Parse tree construction |


**The tools automate what we learn in theory!**


---

# Why This Matters

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Compilers, data formats, config files, protocols — parsers are quietly running everywhere.

</div>


- **Compilers:** Parse programming languages (C, Java, Python)
- **Data formats:** Parse JSON, XML, YAML, HTML
- **Configuration files:** Parse nginx.conf, .gitignore
- **Domain-specific languages:** SQL, regular expressions, math notation
- **Protocol parsing:** HTTP headers, email formats


Every time you use a programming language, a parser (built from CFG theory) is at work!


<!--
A few real-world points worth dropping here:

GCC used Bison for *decades* — until around 2004, when the C++ committee
added enough ambiguous syntax (e.g., the famous "most vexing parse")
that LALR(1) couldn't keep up, and the GCC team rewrote the C++ frontend
as a hand-written recursive-descent parser. Clang made the same choice
from day one. So context-free grammars actually *lost* a battle here:
real C++ is no longer parsed with a CFG-based tool.

Python's parser also made the jump: until version 3.8, CPython used a
custom LL(1) parser. In Python 3.9 it was replaced with a PEG parser
(Parsing Expression Grammar) — a different formalism that handles
left-recursion and lookahead more gracefully. Guido van Rossum himself
came out of semi-retirement to work on it.

The lesson for students: CFGs are the *theoretical* sweet spot, but real
language designers often need either more power (PEG, GLR) or more
control (hand-written). Knowing the theory tells you *why* the trade-offs
are what they are.
-->


---

# Resources

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Where to read the specs and find the manuals — and the JSON-parser assignment.

</div>


- **JSON specification:** https://www.json.org/json-en.html
- **Bison manual:** https://www.gnu.org/software/bison/manual/
- **Flex manual:** https://github.com/westes/flex
- **Classic reference:** http://dinosaur.compilertools.net


**Assignment:** Complete the JSON parser in GitHub Classroom

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

From Theory to Practice

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

<v-clicks>

- **Context-Free Grammars (CFGs)** define languages
- **Parsers** recognize whether strings belong to those languages
- **Parser generators** automatically create parsers from CFG specifications

</v-clicks>

<v-click>

CFG Specification → Parser Generator → Working Parser

</v-click>

---

# What is a Parser?

<v-clicks>

A parser is a program that:

1. **Reads** a sequence of tokens (from a lexer)
2. **Analyzes** them according to grammar rules
3. **Determines** if the input is valid (syntactically correct)
4. **Optionally** builds a parse tree or performs actions

</v-clicks>

<v-click>

**Example:** Is a JSON object like name:Alice valid?

</v-click>

---

# CFG Review

A Context-Free Grammar consists of:

<v-clicks>

- **Terminals:** Basic symbols (tokens)
- **Non-terminals:** Syntactic categories like object, array, value
- **Production rules:** How non-terminals expand
- **Start symbol:** Where parsing begins

</v-clicks>

<v-click>

Example productions:

- value → STRING or NUMBER or object or array
- object → empty braces or braces with members
- array → empty brackets or brackets with elements

</v-click>

---

# The Tool Chain

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

<v-clicks>

**Flex (Lexer Generator)**
- Input: Regular expressions
- Output: Lexical analyzer (scanner)
- Converts character stream to tokens

**Bison (Parser Generator)**
- Input: CFG rules
- Output: Parser
- Analyzes token stream

</v-clicks>

</div>
<div>

<v-click>

Source Code

→ Flex/Lex (regex rules)

→ Token Stream

→ Bison/Yacc (CFG rules)

→ Parse Result

</v-click>

</div>
</div>

---

# Flex: The Lexer

Flex uses **regular expressions** to define tokens:

- Match literal braces: return LBRACE, RBRACE
- Match "true": return TRUE token
- Match "false": return FALSE token
- Match quoted strings: return STRING token
- Match numbers: return NUMBER token
- Skip whitespace

<v-click>

This connects to **Regular Languages** (Section 9.3)!

</v-click>

---

# Bison: The Parser

Bison uses **CFG production rules**:

- value: STRING or NUMBER or TRUE or FALSE or object or array
- object: LBRACE RBRACE or LBRACE members RBRACE
- array: LBRACK RBRACK or LBRACK elements RBRACK

<v-click>

This connects to **Context-Free Grammars** (Section 9.4)!

</v-click>

---

# Lex vs Flex

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

<v-click>

**Both use the same .l file format!**

</v-click>

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

<v-click>

**Structure:** Pattern on left, action on right

Each line: **regex** → **C code to execute**

</v-click>

---

# Understanding Flex Rules

| Pattern | Meaning | Token Returned |
|---------|---------|----------------|
| "true" | Literal string | TRUE |
| "false" | Literal string | FALSE |
| [0-9]+ | One or more digits | NUMBER |
| [ \t\n]+ | Whitespace | (skip) |
| . | Any other character | The character itself |

<v-click>

**Key insight:** These are **regular expressions** - the theory from Section 9.3!

</v-click>

---

# Yacc vs Bison

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

<v-click>

**Both use the same .y file format!**

</v-click>

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

**Rule structure:** non-terminal: alternatives ;

| Rule | Meaning |
|------|---------|
| json: value | A JSON doc is a value |
| value: STRING or NUMBER... | Value can be several things |
| object: LBRACE RBRACE | Empty braces = empty object |
| object: LBRACE members RBRACE | Braces with members inside |

<v-click>

**Key insight:** These are **CFG production rules** - the theory from Section 9.4!

</v-click>

---

# Complete File Structure

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

<v-click>

Both have three sections separated by %%

</v-click>

---

# JSON Grammar in Bison

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

<v-clicks>

**Key insight:** Lists are naturally recursive!

**Members** (key-value pairs in objects):
- Base case: One member
- Recursive: One member, comma, more members

**Elements** (values in arrays):
- Base case: One element
- Recursive: One value, comma, more values

</v-clicks>

<v-click>

This is exactly how CFGs handle **unbounded repetition**!

</v-click>

---

# Building a JSON Parser

<v-clicks>

1. **Write lexer rules** (json_lexer.l) - uses regular expressions
2. **Write grammar rules** (json_parser.y) - uses CFG
3. **Generate code:** flex and bison commands
4. **Compile:** gcc to create executable
5. **Run:** pipe JSON input to parser

</v-clicks>

---

# Theory Meets Practice

| Theory (Chapter 9) | Practice (Parser Tools) |
|-------------------|------------------------|
| Regular Expressions | Flex/Lex patterns |
| Finite Automata | Lexer state machine |
| Context-Free Grammar | Bison/Yacc rules |
| Pushdown Automata | Parser stack |
| Derivations | Parse tree construction |

<v-click>

**The tools automate what we learn in theory!**

</v-click>

---

# Why This Matters

<v-clicks>

- **Compilers:** Parse programming languages (C, Java, Python)
- **Data formats:** Parse JSON, XML, YAML, HTML
- **Configuration files:** Parse nginx.conf, .gitignore
- **Domain-specific languages:** SQL, regular expressions, math notation
- **Protocol parsing:** HTTP headers, email formats

</v-clicks>

<v-click>

Every time you use a programming language, a parser (built from CFG theory) is at work!

</v-click>

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

<v-clicks>

- **JSON specification:** https://www.json.org/json-en.html
- **Bison manual:** https://www.gnu.org/software/bison/manual/
- **Flex manual:** https://github.com/westes/flex
- **Classic reference:** http://dinosaur.compilertools.net

</v-clicks>

<v-click>

**Assignment:** Complete the JSON parser in GitHub Classroom

</v-click>

---

# Summary

<v-clicks>

1. **CFGs** are the theoretical foundation for parsing
2. **Parser generators** (Bison/Yacc) convert CFGs to working code
3. **Lexers** (Flex/Lex) handle tokenization using regular expressions
4. **Together:** Theory + tools = real-world language processors

</v-clicks>

<v-click>

**Key takeaway:** The theory you learn in class directly powers the tools used in industry!

</v-click>

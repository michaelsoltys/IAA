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
mdc: true
---

# Parser Tools and CFGs

From Theory to Practice

---

# The Big Picture

<v-clicks>

- **Context-Free Grammars (CFGs)** define languages
- **Parsers** recognize whether strings belong to those languages
- **Parser generators** automatically create parsers from CFG specifications

</v-clicks>

<v-click>

CFG Specification --> Parser Generator --> Working Parser

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

- value --> STRING or NUMBER or object or array
- object --> empty braces or braces with members
- array --> empty brackets or brackets with elements

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

--> Flex/Lex (regex rules)

--> Token Stream

--> Bison/Yacc (CFG rules)

--> Parse Result

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

This connects to **Regular Languages** (Chapter 9.3)!

</v-click>

---

# Bison: The Parser

Bison uses **CFG production rules**:

- value: STRING or NUMBER or TRUE or FALSE or object or array
- object: LBRACE RBRACE or LBRACE members RBRACE
- array: LBRACK RBRACK or LBRACK elements RBRACK

<v-click>

This connects to **Context-Free Grammars** (Chapter 9.4)!

</v-click>

---

# JSON Grammar in Bison

<div class="grid grid-cols-2 gap-4">
<div>

**CFG (Theory)**

- json --> value
- value --> STRING or NUMBER or TRUE or FALSE or NULL or object or array
- object --> empty or with members
- members --> member or member, members
- array --> empty or with elements
- elements --> value or value, elements

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

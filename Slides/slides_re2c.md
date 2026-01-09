---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## RE2C and Regular Languages
  COMP 454: Automata, Languages and Computation
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: RE2C and Regular Languages
mdc: true
---

# RE2C and Regular Languages

From Regular Expressions to Efficient Scanners

---

# The Big Picture

<v-clicks>

- **Regular expressions** define patterns
- **Finite automata** recognize those patterns
- **RE2C** compiles regex to highly optimized code

</v-clicks>

<v-click>

```
Regular Expression  →  RE2C  →  Optimized C Code (DFA)
     (theory)         (tool)        (practice)
```

</v-click>

---

# What is RE2C?

<v-clicks>

**RE2C** = "Regular Expressions to C"

- A lexer generator (like Flex, but different approach)
- Converts regular expressions directly to C code
- Generates **direct-coded DFAs** (no tables!)
- Produces extremely fast scanners

</v-clicks>

<v-click>

**Used in:** PHP (official lexer), Ninja build system, and many performance-critical applications

</v-click>

---

# RE2C vs Flex

<div class="grid grid-cols-2 gap-8">
<div>

**Flex**
<v-clicks>

- Table-driven DFA
- Lookup tables at runtime
- Portable, well-documented
- Easier to debug

</v-clicks>

</div>
<div>

**RE2C**
<v-clicks>

- Direct-coded DFA
- Generates `goto` statements
- Faster execution
- Smaller memory footprint

</v-clicks>

</div>
</div>

<v-click>

Both implement the same theory: **Regular Expression → NFA → DFA → Code**

</v-click>

---

# Regular Language Review

A language is **regular** if it can be described by:

<v-clicks>

- **Regular expression**
- **DFA** (Deterministic Finite Automaton)
- **NFA** (Nondeterministic Finite Automaton)

</v-clicks>

<v-click>

**Theorem:** These three are equivalent!

This is the foundation for all lexer generators.

</v-click>

---

# RE2C Syntax

```c
/*!re2c
    re2c:define:YYCTYPE = char;
    re2c:yyfill:enable = 0;

    digit = [0-9];
    letter = [a-zA-Z];

    digit+          { return NUMBER; }
    letter+         { return IDENTIFIER; }
    [ \t\n]+        { goto loop; }  // skip whitespace
    *               { return ERROR; }
*/
```

<v-click>

Notice: Regular expression patterns on the left, actions on the right!

</v-click>

---

# How RE2C Works

<v-clicks>

1. **Parse** regular expressions
2. **Build** NFA using Thompson's construction
3. **Convert** NFA to DFA (subset construction)
4. **Minimize** DFA (optional)
5. **Generate** C code with `goto` statements

</v-clicks>

<v-click>

**Key insight:** Each DFA state becomes a label, each transition becomes a `goto`!

</v-click>

---

# Generated Code Example

**Input regex:** `[0-9]+`

**Generated C code:**
```c
yy1:
    yych = *YYCURSOR++;
    if (yych <= '/') goto yy3;
    if (yych <= '9') goto yy4;
yy3:
    { return ERROR; }
yy4:
    yych = *YYCURSOR++;
    if (yych <= '/') goto yy5;
    if (yych <= '9') goto yy4;
yy5:
    { return NUMBER; }
```

<v-click>

This IS the DFA, encoded as control flow!

</v-click>

---

# The Theory Connection

| Theory (Chapter 9) | RE2C Implementation |
|-------------------|---------------------|
| Regular Expression | Input specification |
| Thompson's Construction | NFA building |
| Subset Construction | NFA → DFA conversion |
| DFA Minimization | Optimization phase |
| DFA States | Code labels (`yy1:`, `yy2:`, ...) |
| DFA Transitions | `goto` statements |

---

# Example: Tokenizing Numbers

**Regular expression for JSON numbers:**

```
-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?
```

<v-clicks>

Breaking it down:
- `-?` — optional minus sign
- `(0|[1-9][0-9]*)` — integer part (no leading zeros except for 0)
- `(\.[0-9]+)?` — optional decimal part
- `([eE][+-]?[0-9]+)?` — optional exponent

</v-clicks>

<v-click>

RE2C compiles this to a DFA with ~15-20 states!

</v-click>

---

# Performance Benefits

<v-clicks>

**Why is direct-coded DFA faster?**

1. **No table lookups** — transitions are direct jumps
2. **Better branch prediction** — CPU can predict `goto` patterns
3. **Smaller code size** — no transition tables in memory
4. **Cache-friendly** — code locality is better

</v-clicks>

<v-click>

**Benchmarks:** RE2C-generated lexers can be 2-3x faster than table-driven ones

</v-click>

---

# Practical Example: Simple Lexer

```c
#include <stdio.h>

int lex(const char *YYCURSOR) {
    const char *YYMARKER;
    /*!re2c
        re2c:define:YYCTYPE = char;
        re2c:yyfill:enable = 0;

        [0-9]+      { return 1; }  // NUMBER
        [a-z]+      { return 2; }  // WORD
        [ \t\n]+    { return 0; }  // WHITESPACE
        *           { return -1; } // ERROR
    */
}
```

<v-click>

Run `re2c lexer.re -o lexer.c` to generate C code!

</v-click>

---

# RE2C in Real World

<v-clicks>

**PHP Language**
- The official PHP lexer is built with RE2C
- Handles PHP's complex syntax efficiently
- Millions of requests rely on this daily

**Ninja Build System**
- Fast build tool (used by Chrome, LLVM)
- RE2C parses build files quickly

**Other uses:**
- Protocol parsers, log analyzers, data validators

</v-clicks>

---

# Theory to Practice Pipeline

```
1. Define patterns as regular expressions
       ↓
2. RE2C builds NFA (Thompson's construction)
       ↓
3. Convert to DFA (subset construction)
       ↓
4. Minimize DFA (Hopcroft's algorithm)
       ↓
5. Generate direct-coded scanner
       ↓
6. Compile and run at high speed!
```

<v-click>

**Everything you learn in Chapter 9.3 powers this!**

</v-click>

---

# Limitations

<v-clicks>

**What RE2C (and regex) CANNOT do:**

- Match balanced parentheses: `(()())` — not regular!
- Count occurrences: "same number of a's and b's"
- Parse nested structures (need CFG for that)

</v-clicks>

<v-click>

**Pumping Lemma** tells us these are impossible with finite automata.

That's why we need **parsers** (CFGs) for programming languages!

</v-click>

---

# RE2C Resources

<v-clicks>

- **Official site:** https://re2c.org/
- **Documentation:** https://re2c.org/manual/manual.html
- **GitHub:** https://github.com/skvadrik/re2c
- **Try online:** https://re2c.org/manual/manual_c.html (examples)

</v-clicks>

<v-click>

**Installation:**
```bash
# Ubuntu/Debian
sudo apt-get install re2c

# macOS
brew install re2c
```

</v-click>

---

# Comparison: Lexer Tools

| Tool | Approach | Speed | Portability |
|------|----------|-------|-------------|
| **Flex** | Table-driven DFA | Good | Excellent |
| **RE2C** | Direct-coded DFA | Excellent | Good |
| **Ragel** | Multiple backends | Excellent | Good |
| **Hand-written** | Manual | Varies | Excellent |

<v-click>

**Choose based on:** Performance needs, team familiarity, target platform

</v-click>

---

# Summary

<v-clicks>

1. **Regular expressions** define what we want to match
2. **Finite automata** (DFA/NFA) are the computational model
3. **RE2C** compiles regex to highly optimized C code
4. **Performance:** Direct-coded DFAs avoid table lookups
5. **Real-world impact:** Powers PHP, build systems, and more

</v-clicks>

<v-click>

**Key takeaway:** The regular language theory from Chapter 9.3 directly enables tools like RE2C that power production systems!

</v-click>

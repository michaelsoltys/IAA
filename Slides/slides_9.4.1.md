---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.4.1: Context-Free Grammars
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Context-Free Grammars
mdc: false
---

# Context-Free Grammars

Section 9.4.1 - Context-Free Grammars

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

<!--
Noam Chomsky introduced context-free grammars in 1956 as part of his work on natural language syntax, not programming languages. John Backus developed a similar notation to describe FORTRAN syntax (1959), and Peter Naur refined it for Algol 60, explicitly crediting Chomsky. The notation became known as Backus-Naur Form (BNF), and its equivalence to CFGs cemented the bridge between Chomsky's linguistic hierarchy and programming language design — one of the most fruitful connections between linguistics and computer science.
-->

---

# Overview

Context-free grammars formalize the syntax of programming languages

<v-clicks>

**Key concepts:**
1. **CFG definition** — the 4-tuple $G = (V, T, P, S)$
2. **Derivations** — how strings are generated
3. **Parse trees** — structural representation of derivations
4. **Ambiguity** — when a string has two different parse trees
5. **Chomsky Normal Form** — a canonical form for CFGs
6. **CYK algorithm** — membership testing for CFLs
7. **Pumping Lemma** — proving languages are not context-free
8. **Closure properties** — what operations preserve CFLs

</v-clicks>

---
layout: section
---

# CFG Definition

Generative grammars for programming languages

---

# Context-Free Grammar

A **context-free grammar (CFG)** is $G = (V, T, P, S)$

<v-clicks>

- **$V$** — Finite set of **variables** (nonterminals)
- **$T$** — Finite set of **terminals**
- **$P$** — Finite set of **productions** (rules)
- **$S \in V$** — **Start variable**

Each production has the form $A \longrightarrow \alpha$ where $A \in V$ and $\alpha \in (V \cup T)^*$

</v-clicks>

<!--
The "context-free" in CFG means the left side of every rule is a single variable — the rewrite applies regardless of surrounding context. In a context-sensitive grammar, by contrast, a rule like $aAb \rightarrow aXYb$ says "rewrite $A$ as $XY$, but only when it appears between $a$ and $b$." This distinction is what makes CFGs so amenable to efficient parsing.
-->

---

# Example: Palindromes

$$P \longrightarrow \varepsilon \mid 0 \mid 1 \mid 0P0 \mid 1P1$$

<v-click>

**Lemma:** This grammar generates exactly the set of palindromes over $\{0, 1\}$

</v-click>

<v-click>

**Proof ($\Rightarrow$):** If $w$ is a palindrome, show $P \stackrel{*}{\Rightarrow} w$ by induction on $|w|$

- **BS:** $|w| \leq 1$, so $w = \varepsilon, 0, 1$ — use $P \longrightarrow \varepsilon, 0, 1$
- **IS:** For $|w| \geq 2$, $w = 0x0$ or $w = 1x1$, and by IH $P \stackrel{*}{\Rightarrow} x$

</v-click>

<v-click>

**Proof ($\Leftarrow$):** If $P \stackrel{*}{\Rightarrow} w$, show $w = w^R$ by induction on derivation steps

- **BS:** Derivation has 1 step
- **IS:** $P \Rightarrow 0P0 \stackrel{*}{\Rightarrow} 0x0 = w$ (or with 1 instead of 0)

</v-click>

---

# Example: Algebraic Expressions

$G = (\{E, T, F\}, \Sigma, P, E)$ where $\Sigma = \{a, +, \times, (, )\}$

$$E \longrightarrow E + T \mid T$$
$$T \longrightarrow T \times F \mid F$$
$$F \longrightarrow (E) \mid a$$

<v-click>

**Structural meaning of the three productions:**

- An **expression** is a term or the sum of an expression and a term
- A **term** is a factor or the product of a term and a factor
- A **factor** is a parenthesized expression or the terminal $a$

The simplest expression: a single term, which is a single factor: $a$

</v-click>

---

# Derivations

If $\alpha A \beta \in (V \cup T)^*$, $A \in V$, and $A \longrightarrow \gamma$ is a production, then:

$$\alpha A \beta \Rightarrow \alpha \gamma \beta$$

We use $\stackrel{*}{\Rightarrow}$ to denote 0 or more steps

<v-click>

**Language of a grammar:**
$$L(G) = \{w \in T^* \mid S \stackrel{*}{\Rightarrow} w\}$$

</v-click>

<v-click>

**Sentential form:** If $S \stackrel{*}{\Rightarrow} \alpha$ where $\alpha \in (V \cup T)^*$, then $\alpha$ is a sentential form

$L(G)$ is the set of sentential forms that are in $T^*$

</v-click>

---

# Parse Trees

The **parse tree** for $(G, w)$ is a rooted tree where:

<v-clicks>

- $S$ labels the root
- The symbols of $w$ are the leaves (left to right)
- Each interior node has the form:

$$A \longrightarrow X_1 X_2 X_3 \ldots X_n$$

where $A$ is the parent and $X_1, \ldots, X_n$ are the children

</v-clicks>

<v-click>

**Five equivalent ways to show $w \in L(G)$:**
1. Recursive inference (body $\longrightarrow$ head)
2. Derivation (head $\longrightarrow$ body)
3. Left-most derivation
4. Right-most derivation
5. Yield of a parse tree

</v-click>

---

# Ambiguity

A grammar is **ambiguous** if there exists a string $w$ with two different parse trees

<v-click>

**Example:** $G = (\{E\}, [0\text{-}9], \{E \rightarrow E+E, E*E\}, E)$

$$E \Rightarrow E+E \Rightarrow E+E*E$$
$$E \Rightarrow E*E \Rightarrow E+E*E$$

Two different parse trees — two different meanings!

</v-click>

<!--
The "dangling else" problem is a famous ambiguity in programming languages. In C, `if (a) if (b) x; else y;` — does the `else` belong to the inner or outer `if`? Most languages resolve this by convention (match with nearest `if`), but it caused real bugs in early compilers. Python sidesteps it entirely by using indentation to determine scope.
-->

<v-click>

**Why it matters:** Parse trees assign meaning to strings. Two different parse trees mean two possible interpretations — hence the "ambiguity"

**The expression grammar** $E \rightarrow E+T \mid T$, $T \rightarrow T \times F \mid F$, $F \rightarrow (E) \mid a$ resolves this by encoding operator precedence

</v-click>

---
layout: section
---

# Simplifying CFGs

Eliminating useless symbols, $\varepsilon$-productions, and unit productions

---

# Useful, Generating, and Reachable Symbols

$X \in V \cup T$ is **useful** if:
$$S \stackrel{*}{\Rightarrow} \alpha X \beta \stackrel{*}{\Rightarrow} w \in T^*$$

<v-clicks>

**Generating:** $X \stackrel{*}{\Rightarrow} w \in T^*$
- Every symbol in $T$ is generating
- If $A \longrightarrow \alpha$ and every symbol in $\alpha$ is generating, then $A$ is generating

**Reachable:** $S \stackrel{*}{\Rightarrow} \alpha X \beta$
- $S$ is reachable
- If $A$ is reachable and $A \longrightarrow \alpha$, then every symbol in $\alpha$ is reachable

**A symbol is useful iff it is generating AND reachable**

</v-clicks>

---

# Eliminating $\varepsilon$-Productions

If $L$ has a CFG, then $L - \{\varepsilon\}$ has a CFG without $A \longrightarrow \varepsilon$

<v-clicks>

**Nullable variables:** $A$ is nullable if $A \stackrel{*}{\Rightarrow} \varepsilon$

**Computing nullable variables:**
- If $A \longrightarrow \varepsilon$, then $A$ is nullable
- If $B \longrightarrow C_1 C_2 \ldots C_k$ and all $C_i$ are nullable, then $B$ is nullable

**Elimination procedure:**
1. Remove all $A \longrightarrow \varepsilon$
2. If $A \longrightarrow X_1 X_2 \ldots X_k$ and $m \leq k$ of the $X_i$'s are nullable, add $2^m$ versions with nullable variables present/absent
3. Exception: if $m = k$, do not add the all-absent case

</v-clicks>

---

# Eliminating Unit Productions

A **unit production** has the form $A \longrightarrow B$

<v-clicks>

**Unit pairs:** $(A, B)$ is a unit pair if $A \stackrel{*}{\Rightarrow} B$

**Computing unit pairs:**
- $(A, A)$ is a unit pair for all $A$
- If $(A, B)$ is a unit pair and $B \longrightarrow C$ is a production, then $(A, C)$ is a unit pair

**Elimination:**
- For each unit pair $(A, B)$: if $B \longrightarrow \alpha$ is a non-unit production, add $A \longrightarrow \alpha$
- Remove all unit productions

</v-clicks>

---

# Chomsky Normal Form

A CFG is in **Chomsky Normal Form (CNF)** if all rules are:

$$A \longrightarrow BC \quad \text{or} \quad A \longrightarrow a$$

<v-click>

**Theorem:** Every CFL without $\varepsilon$ has a CFG in CNF

</v-click>

<v-click>

**Proof outline:**
1. Eliminate $\varepsilon$-productions
2. Eliminate unit productions
3. Eliminate useless symbols
4. For bodies of length $\geq 2$: replace terminals with new variables
5. Break bodies of length $\geq 3$ into cascades of length-2 productions

</v-click>

<!--
Chomsky Normal Form is named after Noam Chomsky, who introduced it in 1959. The restriction to binary branching ($A \rightarrow BC$) is what makes the CYK dynamic programming algorithm possible — each cell in the table considers all ways to split a substring into two parts. Without binary branching, the algorithm would need to consider all possible partitions, blowing up the complexity. CNF is also central to the proof of the Pumping Lemma for CFLs, since binary trees have a clean relationship between height and number of leaves.
-->

---
layout: section
---

# CYK Algorithm

Membership testing using dynamic programming

---

# CYK Algorithm

**Cocke-Kasami-Younger algorithm:** Given $G$ in CNF and $w = a_1 a_2 \ldots a_n$, build an $n \times n$ table

<v-clicks>

$X \in (i, j) \iff X \stackrel{*}{\Rightarrow} a_i a_{i+1} \ldots a_j$

$w \in L(G)$ iff $S \in (1, n)$

</v-clicks>

<v-click>

**Initialization:** For $i = 1$ to $n$, for each variable $X_j$:
- Put $X_j$ in $(i, i)$ iff $\exists\; X_j \longrightarrow a_i$

</v-click>

<v-click>

**Fill table:** For $i < j$:
- For $k = i$ to $j-1$:
  - If $\exists\; X_p \in (i, k)$ and $X_q \in (k+1, j)$ and $X_r \longrightarrow X_p X_q$
  - Put $X_r$ in $(i, j)$

**Complexity:** $O(n^3 \cdot |G|)$ — a dynamic programming algorithm! <span style="font-size: 0.6em; color: navy;">Alg 42, Pg 243, alg:cyk</span>

</v-click>

<!--
The CYK algorithm was discovered independently three times: by John Cocke (1969, unpublished), Tadao Kasami (1965, in a technical report), and Daniel Younger (1967). Its $O(n^3)$ complexity stood as the best general CFG parser for decades. Leslie Valiant showed in 1975 that CFG parsing can be reduced to Boolean matrix multiplication, so any improvement to matrix multiplication (currently $O(n^{2.371})$) automatically improves parsing — though the constant factors make this impractical.
-->

---
layout: section
---

# Pumping Lemma for CFLs

Proving languages are not context-free

---

# Pumping Lemma for CFLs

**Theorem:** For every CFL $L$, there exists a $p$ such that any $s \in L$ with $|s| \geq p$ can be written as $s = uvxyz$ where: <span style="font-size: 0.6em; color: navy;">Lem 9.53, Pg 244, lem:pumping-cfl</span>

<v-clicks>

1. $uv^i xy^i z \in L$ for all $i \geq 0$
2. $|vy| > 0$
3. $|vxy| \leq p$

</v-clicks>

<v-click>

**Proof idea:** In a CNF parse tree for a long string, some variable $A$ must repeat on a root-to-leaf path. The subtrees rooted at the two occurrences of $A$ give us the decomposition into $u, v, x, y, z$

</v-click>

---

# Pumping Lemma: Application

**Example:** $L = \{0^n 1^n 2^n \mid n \geq 1\}$ is **not** context-free

<v-click>

**Proof:** Assume $L$ is CF with pumping length $p$. Take $s = 0^p 1^p 2^p$

Since $|vxy| \leq p$, the substring $vxy$ cannot contain all three symbols. Pumping ($i = 2$) will increase at most two of the three counts, breaking $0^n 1^n 2^n$. Contradiction!

</v-click>

<v-click>

**Corollary:** CFLs are **not** closed under intersection!

- $L_1 = \{0^n 1^n 2^i \mid n, i \geq 1\}$ is CF
- $L_2 = \{0^i 1^n 2^n \mid n, i \geq 1\}$ is CF
- But $L_1 \cap L_2 = \{0^n 1^n 2^n \mid n \geq 1\}$ is not CF

</v-click>

---
layout: section
---

# Closure Properties

What operations preserve context-free languages?

---

# Closure Properties of CFLs

**CFLs are closed under:**

<v-clicks>

- **Union** — combine start variables
- **Concatenation** — sequence start variables
- **Kleene star** ($*$ and $+$)
- **Homomorphism** — define $s(a) = \{h(a)\}$, so $h(L) = s(L)$
- **Reversal** — replace each $A \longrightarrow \alpha$ by $A \longrightarrow \alpha^R$
- **Substitution** — if $s(a)$ is CF for all $a$, then $s(L)$ is CF
- **Intersection with regular languages** — if $L$ is CF and $R$ is regular, $L \cap R$ is CF

</v-clicks>

---

# CFLs are NOT Closed Under...

<v-clicks>

**Intersection:** $L_1 \cap L_2$ may not be CF (as shown with $0^n 1^n 2^n$)

**Complementation:** $L = \{ww \mid w \in \{0,1\}^*\}$ is not CF, but $L^c$ is CF!

</v-clicks>

<v-click>

**CFG for $L^c$:** First note no odd-length string is of the form $ww$

$$S \longrightarrow O \mid E$$
$$O \longrightarrow a \mid b \mid aaO \mid abO \mid baO \mid bbO$$

$O$ generates all odd-length strings. $E$ generates even-length strings not of the form $ww$: strings where position $i$ and position $n/2 + i$ differ for some $i$

</v-click>

---

# Decidable and Undecidable Properties

**Decidable:**
- **Emptiness:** Is $L(G) = \emptyset$? (Check if $S$ is generating)
- **Membership:** Is $w \in L(G)$? (Use CYK algorithm)

<v-click>

**Undecidable properties of CFLs:**

<v-clicks>

1. Is a given CFG $G$ **ambiguous**?
2. Is a given CFL **inherently ambiguous**?
3. Is the **intersection** of two CFLs empty?
4. Given $G_1, G_2$, is $L(G_1) = L(G_2)$?
5. Is a given CFL equal to $\Sigma^*$? (universality)

</v-clicks>

</v-click>

---

# Other Grammars

**Context-sensitive grammars (CSG):** Rules $\alpha \rightarrow \beta$ where $|\alpha| \leq |\beta|$

<v-clicks>

**Fact:** $\text{CSL} = \text{NTIME}(n)$

**Rewriting systems** (Semi-Thue systems): No restrictions — $\alpha \rightarrow \beta$ for arbitrary $\alpha, \beta \in (V \cup T)^*$

**Fact:** A language has a rewriting system iff it is "computable" — this corresponds to the most general model of computation

This leads us to **Turing machines** ...

</v-clicks>

<!--
The Chomsky hierarchy — regular (Type 3), context-free (Type 2), context-sensitive (Type 1), recursively enumerable (Type 0) — was published by Chomsky in 1956. Each level corresponds to a class of automata: finite automata, pushdown automata, linear-bounded automata, and Turing machines. The hierarchy remains the organizing framework for formal language theory 70 years later.

Semi-Thue systems are named after Axel Thue (1914), who studied word rewriting problems decades before Turing or Chomsky. His "word problem" — given a set of rewrite rules, can string $u$ be transformed into string $v$? — was shown undecidable by Post and Markov (independently, 1947). This was one of the earliest undecidability results outside of pure logic.
-->

---

# Advanced Results

<v-clicks>

**Chomsky-Schützenberger Theorem:** If $L$ is a CFL, then there exists a regular language $R$, an $n$, and a homomorphism $h$, such that $L = h(\text{PAREN}_n \cap R)$

**Parikh's Theorem:** If $\Sigma = \{a_1, \ldots, a_n\}$, the signature of $x \in \Sigma^*$ is $(\#a_1(x), \ldots, \#a_n(x))$. Regular languages and CFLs have the same signatures!

</v-clicks>

<!--
The Chomsky-Schützenberger theorem (1963) says every CFL can be obtained by taking a "Dyck language" (matched parentheses of $n$ types), intersecting it with a regular language, and applying a homomorphism. This is a remarkable structural result — it says that the essence of context-freeness is nested matching, and everything else is just regular control and relabeling.

Parikh's theorem (1966) is surprising: if you only care about *how many* of each symbol appear (not their order), CFLs are no more powerful than regular languages. The language $\{a^n b^n\}$ is CF but not regular — yet its set of signatures $\{(n, n) \mid n \geq 0\}$ is also the signature set of the regular language $(ab)^*$. Order is what separates the two classes.
-->

---

# Summary

<v-clicks>

- A **CFG** is $G = (V, T, P, S)$ — variables, terminals, productions, start
- **Derivations** generate strings; **parse trees** give structure
- **Ambiguity** means multiple parse trees for one string
- **CNF** normalizes rules to $A \rightarrow BC$ or $A \rightarrow a$
- **CYK** algorithm tests membership in $O(n^3)$ time
- **Pumping Lemma** proves languages are not CF (e.g., $0^n 1^n 2^n$)
- CFLs closed under union, concatenation, star, but **not** intersection or complement
- Many properties of CFGs are **undecidable**

</v-clicks>

---

# Exercises

1. Show that the palindrome grammar generates exactly the palindromes over $\{0,1\}$

2. Give a CFG for $\{a^n b^m \mid n \neq m\}$

3. Convert the expression grammar to Chomsky Normal Form

4. Use CYK to test whether $a + a \times a \in L(G)$ for the expression grammar

5. Use the Pumping Lemma to show $\{a^n b^n c^n \mid n \geq 0\}$ is not CF

6. Show that CFLs are closed under intersection with regular languages

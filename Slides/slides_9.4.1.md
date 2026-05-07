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

Section 9.4.1 — The grammars that describe nested structure: programming languages, balanced parentheses, and arithmetic expressions.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

<!--
Noam Chomsky introduced context-free grammars in 1956 as part of his work on natural language syntax, not programming languages. John Backus developed a similar notation to describe FORTRAN syntax (1959), and Peter Naur refined it for Algol 60, explicitly crediting Chomsky. The notation became known as Backus-Naur Form (BNF), and its equivalence to CFGs cemented the bridge between Chomsky's linguistic hierarchy and programming language design — one of the most fruitful connections between linguistics and computer science.
-->

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A roadmap of the eight ideas we'll need to define, parse, and reason about context-free languages.

</div>

Context-free grammars formalize the syntax of programming languages


**Key concepts:**
1. **CFG definition** — the 4-tuple $G = (V, T, P, S)$
2. **Derivations** — how strings are generated
3. **Parse trees** — structural representation of derivations
4. **Ambiguity** — when a string has two different parse trees
5. **Chomsky Normal Form** — a canonical form for CFGs
6. **CYK algorithm** — membership testing for CFLs
7. **Pumping Lemma** — proving languages are not context-free
8. **Closure properties** — what operations preserve CFLs


---
layout: section
---

# CFG Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Generative grammars for programming languages — productions that rewrite variables into strings.

</div>

---

# Context-Free Grammar

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The four pieces — variables, terminals, productions, and a start symbol — that together generate a language.

</div>

A **context-free grammar (CFG)** is $G = (V, T, P, S)$


- **$V$** — Finite set of **variables** (nonterminals)
- **$T$** — Finite set of **terminals**
- **$P$** — Finite set of **productions** (rules)
- **$S \in V$** — **Start variable**

Each production has the form $A \longrightarrow \alpha$ where $A \in V$ and $\alpha \in (V \cup T)^*$


<!--
The "context-free" in CFG means the left side of every rule is a single variable — the rewrite applies regardless of surrounding context. In a context-sensitive grammar, by contrast, a rule like $aAb \rightarrow aXYb$ says "rewrite $A$ as $XY$, but only when it appears between $a$ and $b$." This distinction is what makes CFGs so amenable to efficient parsing.
-->

---

# Example: Palindromes

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A tiny five-rule grammar that captures exactly the strings reading the same forwards and backwards.

</div>

$$P \longrightarrow \varepsilon \mid 0 \mid 1 \mid 0P0 \mid 1P1$$


**Lemma:** This grammar generates exactly the set of palindromes over $\{0, 1\}$


**Proof ($\Rightarrow$):** If $w$ is a palindrome, show $P \stackrel{*}{\Rightarrow} w$ by induction on $|w|$

- **BS:** $|w| \leq 1$, so $w = \varepsilon, 0, 1$ — use $P \longrightarrow \varepsilon, 0, 1$
- **IS:** For $|w| \geq 2$, $w = 0x0$ or $w = 1x1$, and by IH $P \stackrel{*}{\Rightarrow} x$


**Proof ($\Leftarrow$):** If $P \stackrel{*}{\Rightarrow} w$, show $w = w^R$ by induction on derivation steps

- **BS:** Derivation has 1 step
- **IS:** $P \Rightarrow 0P0 \stackrel{*}{\Rightarrow} 0x0 = w$ (or with 1 instead of 0)


---

# Example: Algebraic Expressions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A three-variable grammar that builds operator precedence ($\times$ binds tighter than $+$) into the parse tree.

</div>

$G = (\{E, T, F\}, \Sigma, P, E)$ where $\Sigma = \{a, +, \times, (, )\}$

$$E \longrightarrow E + T \mid T$$
$$T \longrightarrow T \times F \mid F$$
$$F \longrightarrow (E) \mid a$$


**Structural meaning of the three productions:**

- An **expression** is a term or the sum of an expression and a term
- A **term** is a factor or the product of a term and a factor
- A **factor** is a parenthesized expression or the terminal $a$

The simplest expression: a single term, which is a single factor: $a$


---

# Derivations

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

How a grammar generates strings: rewrite one variable at a time until only terminals remain.

</div>

If $\alpha A \beta \in (V \cup T)^*$, $A \in V$, and $A \longrightarrow \gamma$ is a production, then:

$$\alpha A \beta \Rightarrow \alpha \gamma \beta$$

We use $\stackrel{*}{\Rightarrow}$ to denote 0 or more steps


**Language of a grammar:**
$$L(G) = \{w \in T^* \mid S \stackrel{*}{\Rightarrow} w\}$$


**Sentential form:** If $S \stackrel{*}{\Rightarrow} \alpha$ where $\alpha \in (V \cup T)^*$, then $\alpha$ is a sentential form

$L(G)$ is the set of sentential forms that are in $T^*$


---

# Parse Trees

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The structural picture of a derivation — and five equivalent ways to certify that $w \in L(G)$.

</div>

The **parse tree** for $(G, w)$ is a rooted tree where:


- $S$ labels the root
- The symbols of $w$ are the leaves (left to right)
- Each interior node has the form:

$$A \longrightarrow X_1 X_2 X_3 \ldots X_n$$

where $A$ is the parent and $X_1, \ldots, X_n$ are the children


**Five equivalent ways to show $w \in L(G)$:**
1. Recursive inference (body $\longrightarrow$ head)
2. Derivation (head $\longrightarrow$ body)
3. Left-most derivation
4. Right-most derivation
5. Yield of a parse tree


---

# Ambiguity

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

When the same string admits two parse trees — and why that can mean two different meanings.

</div>

A grammar is **ambiguous** if there exists a string $w$ with two different parse trees


**Example:** $G = (\{E\}, [0\text{-}9], \{E \rightarrow E+E, E*E\}, E)$

$$E \Rightarrow E+E \Rightarrow E+E*E$$
$$E \Rightarrow E*E \Rightarrow E+E*E$$

Two different parse trees — two different meanings!


<!--
The "dangling else" problem is a famous ambiguity in programming languages. In C, `if (a) if (b) x; else y;` — does the `else` belong to the inner or outer `if`? Most languages resolve this by convention (match with nearest `if`), but it caused real bugs in early compilers. Python sidesteps it entirely by using indentation to determine scope.
-->


**Why it matters:** Parse trees assign meaning to strings. Two different parse trees mean two possible interpretations — hence the "ambiguity"

**The expression grammar** $E \rightarrow E+T \mid T$, $T \rightarrow T \times F \mid F$, $F \rightarrow (E) \mid a$ resolves this by encoding operator precedence


---
layout: section
---

# Simplifying CFGs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Eliminating useless symbols, $\varepsilon$-productions, and unit productions — three normalization passes.

</div>

---

# Useful, Generating, and Reachable Symbols

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A symbol earns its keep only if it can both be reached from $S$ *and* generate a terminal string.

</div>

$X \in V \cup T$ is **useful** if:
$$S \stackrel{*}{\Rightarrow} \alpha X \beta \stackrel{*}{\Rightarrow} w \in T^*$$


**Generating:** $X \stackrel{*}{\Rightarrow} w \in T^*$
- Every symbol in $T$ is generating
- If $A \longrightarrow \alpha$ and every symbol in $\alpha$ is generating, then $A$ is generating

**Reachable:** $S \stackrel{*}{\Rightarrow} \alpha X \beta$
- $S$ is reachable
- If $A$ is reachable and $A \longrightarrow \alpha$, then every symbol in $\alpha$ is reachable

**A symbol is useful iff it is generating AND reachable**


---

# Eliminating $\varepsilon$-Productions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Find the *nullable* variables, then enumerate which ones to drop on the right-hand side.

</div>

If $L$ has a CFG, then $L - \{\varepsilon\}$ has a CFG without $A \longrightarrow \varepsilon$


**Nullable variables:** $A$ is nullable if $A \stackrel{*}{\Rightarrow} \varepsilon$

**Computing nullable variables:**
- If $A \longrightarrow \varepsilon$, then $A$ is nullable
- If $B \longrightarrow C_1 C_2 \ldots C_k$ and all $C_i$ are nullable, then $B$ is nullable

**Elimination procedure:**
1. Remove all $A \longrightarrow \varepsilon$
2. If $A \longrightarrow X_1 X_2 \ldots X_k$ and $m \leq k$ of the $X_i$'s are nullable, add $2^m$ versions with nullable variables present/absent
3. Exception: if $m = k$, do not add the all-absent case


---

# Eliminating Unit Productions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Rules of the form $A \to B$ just rename variables — short-circuit them by inlining $B$'s productions.

</div>

A **unit production** has the form $A \longrightarrow B$


**Unit pairs:** $(A, B)$ is a unit pair if $A \stackrel{*}{\Rightarrow} B$

**Computing unit pairs:**
- $(A, A)$ is a unit pair for all $A$
- If $(A, B)$ is a unit pair and $B \longrightarrow C$ is a production, then $(A, C)$ is a unit pair

**Elimination:**
- For each unit pair $(A, B)$: if $B \longrightarrow \alpha$ is a non-unit production, add $A \longrightarrow \alpha$
- Remove all unit productions


---

# Chomsky Normal Form

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A canonical form where every rule is either $A \to BC$ or $A \to a$ — the shape that makes CYK possible.

</div>

A CFG is in **Chomsky Normal Form (CNF)** if all rules are:

$$A \longrightarrow BC \quad \text{or} \quad A \longrightarrow a$$


**Theorem:** Every CFL without $\varepsilon$ has a CFG in CNF


**Proof outline:**
1. Eliminate $\varepsilon$-productions
2. Eliminate unit productions
3. Eliminate useless symbols
4. For bodies of length $\geq 2$: replace terminals with new variables
5. Break bodies of length $\geq 3$ into cascades of length-2 productions


<!--
Chomsky Normal Form is named after Noam Chomsky, who introduced it in 1959. The restriction to binary branching ($A \rightarrow BC$) is what makes the CYK dynamic programming algorithm possible — each cell in the table considers all ways to split a substring into two parts. Without binary branching, the algorithm would need to consider all possible partitions, blowing up the complexity. CNF is also central to the proof of the Pumping Lemma for CFLs, since binary trees have a clean relationship between height and number of leaves.
-->

---
layout: section
---

# CYK Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Membership testing for CFLs in $O(n^3)$ time using dynamic programming on substrings.

</div>

---

# CYK Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Fill an $n \times n$ table: cell $(i,j)$ holds every variable that derives the substring $a_i \ldots a_j$.

</div>

**Cocke-Kasami-Younger algorithm:** Given $G$ in CNF and $w = a_1 a_2 \ldots a_n$, build an $n \times n$ table


$X \in (i, j) \iff X \stackrel{*}{\Rightarrow} a_i a_{i+1} \ldots a_j$

$w \in L(G)$ iff $S \in (1, n)$


**Initialization:** For $i = 1$ to $n$, for each variable $X_j$:
- Put $X_j$ in $(i, i)$ iff $\exists\; X_j \longrightarrow a_i$


**Fill table:** For $i < j$:
- For $k = i$ to $j-1$:
  - If $\exists\; X_p \in (i, k)$ and $X_q \in (k+1, j)$ and $X_r \longrightarrow X_p X_q$
  - Put $X_r$ in $(i, j)$

**Complexity:** $O(n^3 \cdot |G|)$ — a dynamic programming algorithm! <span style="font-size: 0.6em; color: navy;">Alg 42, Pg 243, alg:cyk</span>


<!--
The CYK algorithm was discovered independently three times: by John Cocke (1969, unpublished), Tadao Kasami (1965, in a technical report), and Daniel Younger (1967). Its $O(n^3)$ complexity stood as the best general CFG parser for decades. Leslie Valiant showed in 1975 that CFG parsing can be reduced to Boolean matrix multiplication, so any improvement to matrix multiplication (currently $O(n^{2.371})$) automatically improves parsing — though the constant factors make this impractical.
-->

---
layout: section
---

# Pumping Lemma for CFLs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The standard tool for proving a language is *not* context-free — sufficiently long strings must pump.

</div>

---

# Pumping Lemma for CFLs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Long strings split as $uvxyz$ where pumping $v$ and $y$ in tandem stays in the language.

</div>

**Theorem:** For every CFL $L$, there exists a $p$ such that any $s \in L$ with $|s| \geq p$ can be written as $s = uvxyz$ where: <span style="font-size: 0.6em; color: navy;">Lem 9.53, Pg 244, lem:pumping-cfl</span>


1. $uv^i xy^i z \in L$ for all $i \geq 0$
2. $|vy| > 0$
3. $|vxy| \leq p$


**Proof idea:** In a CNF parse tree for a long string, some variable $A$ must repeat on a root-to-leaf path. The subtrees rooted at the two occurrences of $A$ give us the decomposition into $u, v, x, y, z$


---

# Pumping Lemma: Application

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Use the lemma to prove $\{0^n 1^n 2^n\}$ is not CF — and discover CFLs aren't closed under intersection.

</div>

**Example:** $L = \{0^n 1^n 2^n \mid n \geq 1\}$ is **not** context-free


**Proof:** Assume $L$ is CF with pumping length $p$. Take $s = 0^p 1^p 2^p$

Since $|vxy| \leq p$, the substring $vxy$ cannot contain all three symbols. Pumping ($i = 2$) will increase at most two of the three counts, breaking $0^n 1^n 2^n$. Contradiction!


**Corollary:** CFLs are **not** closed under intersection!

- $L_1 = \{0^n 1^n 2^i \mid n, i \geq 1\}$ is CF
- $L_2 = \{0^i 1^n 2^n \mid n, i \geq 1\}$ is CF
- But $L_1 \cap L_2 = \{0^n 1^n 2^n \mid n \geq 1\}$ is not CF


---
layout: section
---

# Closure Properties

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Which set operations on CFLs always yield another CFL — and which surprisingly fail.

</div>

---

# Closure Properties of CFLs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Union, concatenation, Kleene star, reversal, homomorphism, and intersection with regular all preserve CF.

</div>

**CFLs are closed under:**


- **Union** — combine start variables
- **Concatenation** — sequence start variables
- **Kleene star** ($*$ and $+$)
- **Homomorphism** — define $s(a) = \{h(a)\}$, so $h(L) = s(L)$
- **Reversal** — replace each $A \longrightarrow \alpha$ by $A \longrightarrow \alpha^R$
- **Substitution** — if $s(a)$ is CF for all $a$, then $s(L)$ is CF
- **Intersection with regular languages** — if $L$ is CF and $R$ is regular, $L \cap R$ is CF


---

# CFLs are NOT Closed Under...

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Intersection and complement break the class — and the complement of $\{ww\}$ is a striking witness.

</div>

**Intersection:** $L_1 \cap L_2$ may not be CF (as shown with $0^n 1^n 2^n$)

**Complementation:** $L = \{ww \mid w \in \{0,1\}^*\}$ is not CF, but $L^c$ is CF!


**CFG for $L^c$:** First note no odd-length string is of the form $ww$

$$S \longrightarrow O \mid E$$
$$O \longrightarrow a \mid b \mid aaO \mid abO \mid baO \mid bbO$$

$O$ generates all odd-length strings. $E$ generates even-length strings not of the form $ww$: strings where position $i$ and position $n/2 + i$ differ for some $i$


---

# Decidable and Undecidable Properties

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Emptiness and membership are decidable — but ambiguity, equivalence, and universality are not.

</div>

**Decidable:**
- **Emptiness:** Is $L(G) = \emptyset$? (Check if $S$ is generating)
- **Membership:** Is $w \in L(G)$? (Use CYK algorithm)


**Undecidable properties of CFLs:**


1. Is a given CFG $G$ **ambiguous**?
2. Is a given CFL **inherently ambiguous**?
3. Is the **intersection** of two CFLs empty?
4. Given $G_1, G_2$, is $L(G_1) = L(G_2)$?
5. Is a given CFL equal to $\Sigma^*$? (universality)


---

# Other Grammars

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Stepping up the Chomsky hierarchy — context-sensitive grammars and unrestricted rewriting systems.

</div>

**Context-sensitive grammars (CSG):** Rules $\alpha \rightarrow \beta$ where $|\alpha| \leq |\beta|$


**Fact:** $\text{CSL} = \text{NTIME}(n)$

**Rewriting systems** (Semi-Thue systems): No restrictions — $\alpha \rightarrow \beta$ for arbitrary $\alpha, \beta \in (V \cup T)^*$

**Fact:** A language has a rewriting system iff it is "computable" — this corresponds to the most general model of computation

This leads us to **Turing machines** ...


<!--
The Chomsky hierarchy — regular (Type 3), context-free (Type 2), context-sensitive (Type 1), recursively enumerable (Type 0) — was published by Chomsky in 1956. Each level corresponds to a class of automata: finite automata, pushdown automata, linear-bounded automata, and Turing machines. The hierarchy remains the organizing framework for formal language theory 70 years later.

Semi-Thue systems are named after Axel Thue (1914), who studied word rewriting problems decades before Turing or Chomsky. His "word problem" — given a set of rewrite rules, can string $u$ be transformed into string $v$? — was shown undecidable by Post and Markov (independently, 1947). This was one of the earliest undecidability results outside of pure logic.
-->

---

# Advanced Results

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two classical theorems showing that CFLs reduce, in different senses, to nested matching and to commutative counting.

</div>

**Chomsky-Schützenberger Theorem:** If $L$ is a CFL, then there exists a regular language $R$, an $n$, and a homomorphism $h$, such that $L = h(\text{PAREN}_n \cap R)$

**Parikh's Theorem:** If $\Sigma = \{a_1, \ldots, a_n\}$, the signature of $x \in \Sigma^*$ is $(\#a_1(x), \ldots, \#a_n(x))$. Regular languages and CFLs have the same signatures!


<!--
The Chomsky-Schützenberger theorem (1963) says every CFL can be obtained by taking a "Dyck language" (matched parentheses of $n$ types), intersecting it with a regular language, and applying a homomorphism. This is a remarkable structural result — it says that the essence of context-freeness is nested matching, and everything else is just regular control and relabeling.

Parikh's theorem (1966) is surprising: if you only care about *how many* of each symbol appear (not their order), CFLs are no more powerful than regular languages. The language $\{a^n b^n\}$ is CF but not regular — yet its set of signatures $\{(n, n) \mid n \geq 0\}$ is also the signature set of the regular language $(ab)^*$. Order is what separates the two classes.
-->

---

# Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Practice problems to cement grammar design, CNF conversion, CYK, the pumping lemma, and closure proofs.

</div>

1. Show that the palindrome grammar generates exactly the palindromes over $\{0,1\}$

2. Give a CFG for $\{a^n b^m \mid n \neq m\}$

3. Convert the expression grammar to Chomsky Normal Form

4. Use CYK to test whether $a + a \times a \in L(G)$ for the expression grammar

5. Use the Pumping Lemma to show $\{a^n b^n c^n \mid n \geq 0\}$ is not CF

6. Show that CFLs are closed under intersection with regular languages

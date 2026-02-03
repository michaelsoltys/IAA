---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.3.3: Regular Expressions
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Regular Expressions
mdc: true
---

<style>
.slidev-layout.cover {
  background: white !important;
  color: black !important;
}
.slidev-layout.cover h1 {
  color: black !important;
}
</style>

# Regular Expressions

Section 9.3.3 - Regular Languages

---

# Overview

**Regular Expressions** provide an algebraic notation for describing regular languages

<v-clicks>

**Key concepts:**
1. **RE definition** — structural induction over $\Sigma$, $\varepsilon$, $\emptyset$
2. **RE semantics** — the language $L(R)$ described by an RE
3. **RE $\Rightarrow$ $\varepsilon$-NFA** — structural induction with invariants
4. **DFA $\Rightarrow$ RE** — two methods
   - Method 1: Dynamic Programming
   - Method 2: Generalized NFA (GNFA)
5. **The fundamental equivalence** — RE $\Leftrightarrow$ FA

</v-clicks>

<v-click>

Regular Expressions are familiar from text processing (grep, sed, VIM, etc.), though practical implementations go beyond the formal definition

</v-click>

---
layout: section
---

# RE Definition

Algebraic notation for sets of strings

---

# Operations on Languages

Three fundamental operations:

<v-clicks>

**Union:**
$$L \cup M = \{ w \mid w \in L \text{ or } w \in M \}$$

**Concatenation:**
$$LM = \{ xy \mid x \in L \text{ and } y \in M \}$$

**Kleene Star (Closure):**
$$L^* = \{ x_1 x_2 \ldots x_n \mid x_i \in L, n \geq 0 \}$$

Note: $n = 0$ gives $\varepsilon \in L^*$ for any $L$

</v-clicks>

---

# Regular Expressions: Formal Definition

A **Regular Expression (RE)** is a syntactic object defined by **structural induction**:

<v-clicks>

**Basis Case:** The following are REs:
- $a \in \Sigma$ (any symbol from the alphabet)
- $\varepsilon$ (the empty string)
- $\emptyset$ (the empty set)

**Induction Step:** If $E, F$ are REs, then so are:
- $E + F$ (union)
- $EF$ (concatenation)
- $(E)^*$ (Kleene star)
- $(E)$ (parenthesization)

</v-clicks>

<v-click>

REs are a **model of computation**, just like DFAs or NFAs — they describe languages

</v-click>

---

# RE Semantics

**Exercise:** What are the languages $L(a)$, $L(\varepsilon)$, $L(\emptyset)$, $L(E+F)$, $L(EF)$, $L(E^*)$?

<v-click>

**Answers:**
- $L(a) = \{a\}$
- $L(\varepsilon) = \{\varepsilon\}$
- $L(\emptyset) = \emptyset$
- $L(E + F) = L(E) \cup L(F)$
- $L(EF) = L(E) \cdot L(F) = \{xy \mid x \in L(E), y \in L(F)\}$
- $L(E^*) = (L(E))^*$

</v-click>

<v-click>

**Example:** RE for strings of 0s and 1s **not** containing 101 as a substring:

$$(\varepsilon + 0)(1^* + 00^*0)^*(\varepsilon + 0)$$

</v-click>

---
layout: section
---

# RE $\Leftrightarrow$ FA

The fundamental equivalence theorem

---

# The Equivalence Theorem

**Theorem:** A language is regular if and only if it is given by some regular expression

<v-click>

**Two directions to prove:**

1. **RE $\Rightarrow$ $\varepsilon$-NFA:** Convert a regular expression to an automaton
2. **DFA $\Rightarrow$ RE:** Convert an automaton to a regular expression

</v-click>

<v-click>

Combined with the DFA $\Leftrightarrow$ NFA equivalence from section 9.3.2:

$$\text{DFA} \iff \text{NFA} \iff \varepsilon\text{-NFA} \iff \text{RE}$$

All four formalisms describe **exactly** the same class of languages!

</v-click>

---

# RE to $\varepsilon$-NFA: Overview

Convert RE $R$ to an $\varepsilon$-NFA using **structural induction**

<v-click>

**Three invariants** maintained at each step — the NFA $A$ has:
1. Exactly **one** accepting state
2. **No arrow into** the initial state
3. **No arrow out of** the accepting state

</v-click>

<v-click>

**Convention:** If there is no arrow out of state $q$ on symbol $\sigma$, the computation **rejects**. (Formally: there is a "trash state" $T$ with self-loops on all symbols)

</v-click>

---

# RE to $\varepsilon$-NFA: Basis Case

For the three base cases $\varepsilon$, $\emptyset$, and $a \in \Sigma$:

<v-clicks>

**$\varepsilon$:**

$\to \bigcirc \xrightarrow{\varepsilon} \bigodot$

(Start state connected to accept state via $\varepsilon$)

**$\emptyset$:**

$\to \bigcirc \qquad \bigodot$

(Start state and accept state with **no** connection)

**$a \in \Sigma$:**

$\to \bigcirc \xrightarrow{a} \bigodot$

(Start state connected to accept state via symbol $a$)

</v-clicks>

<v-click>

Each satisfies all three invariants: one accept state, no arrows in to start, no arrows out of accept

</v-click>

---

# RE to $\varepsilon$-NFA: Union ($R + S$)

Given NFAs for $R$ and $S$ (shown as boxes), build an NFA for $R + S$:

<v-clicks>

1. Create a **new start state**
2. Connect it via $\varepsilon$ to the start states of $R$ and $S$
3. Create a **new accept state**
4. Connect the accept states of $R$ and $S$ to it via $\varepsilon$

**Structure:**

$$\to \bigcirc \xrightarrow{\varepsilon} \boxed{R} \xrightarrow{\varepsilon} \bigodot$$
$$\qquad \searrow^{\varepsilon} \boxed{S} \nearrow^{\varepsilon}$$

All three invariants are preserved

</v-clicks>

---

# RE to $\varepsilon$-NFA: Concatenation ($RS$)

Given NFAs for $R$ and $S$, build an NFA for $RS$:

<v-clicks>

1. Chain $R$'s accept state to $S$'s start state via $\varepsilon$:

$$\to \boxed{R} \xrightarrow{\varepsilon} \boxed{S} \to \bigodot$$

- Start state = $R$'s start state
- Accept state = $S$'s accept state
- Old accept of $R$ and old start of $S$ become interior states

All three invariants are preserved

</v-clicks>

---

# RE to $\varepsilon$-NFA: Kleene Star ($R^*$)

Given NFA for $R$, build an NFA for $R^*$:

<v-clicks>

1. Create a **new start state** (which is also the accept state, for $\varepsilon \in L(R^*)$)
2. Connect new start to $R$'s start via $\varepsilon$
3. Connect $R$'s accept back to $R$'s start via $\varepsilon$ (the loop)
4. Connect $R$'s accept to the new accept state via $\varepsilon$
5. Also: $\varepsilon$-transition from new start directly to new accept (bypass $R$ entirely)

**Key:** The bypass handles $\varepsilon \in R^*$; the loop handles $R, RR, RRR, \ldots$

</v-clicks>

---

# RE to $\varepsilon$-NFA: Example

Convert $(0 + 01)^*$ step by step:

<v-clicks>

**Step 1:** Build NFAs for $0$ and $1$ (basis case)

$0: \to \bigcirc \xrightarrow{0} \bigodot \qquad 1: \to \bigcirc \xrightarrow{1} \bigodot$

**Step 2:** Build NFA for $01$ (concatenation)

$\to \bigcirc \xrightarrow{0} \bigcirc \xrightarrow{\varepsilon} \bigcirc \xrightarrow{1} \bigodot$

**Step 3:** Build NFA for $0 + 01$ (union)

**Step 4:** Build NFA for $(0 + 01)^*$ (star — add loop and bypass)

</v-clicks>

---
layout: section
---

# DFA to RE

Two conversion methods

---

# Method 1: Dynamic Programming

Given DFA $A$ with $n$ states, define:

$R_{ij}^{(k)}$ = RE whose language is the set of strings that take $A$ from state $q_i$ to state $q_j$ with all **intermediate** states having index $\leq k$

<v-click>

**The answer:** $R = R_{1j_1}^{(n)} + R_{1j_2}^{(n)} + \cdots + R_{1j_l}^{(n)}$ where $F = \{q_{j_1}, \ldots, q_{j_l}\}$

(Union over all accepting states, using all $n$ states as intermediates)

</v-click>

---

# Method 1: Basis and Induction

**Basis ($k = 0$):** No intermediate states allowed — only direct transitions

$$R_{ij}^{(0)} = x + a_1 + a_2 + \cdots + a_m$$

where $i \xrightarrow{a_l} j$ are direct transitions, and:
- $x = \emptyset$ if $i \neq j$
- $x = \varepsilon$ if $i = j$ (can stay in same state with empty string)

<v-click>

**Induction ($k > 0$):**

$$R_{ij}^{(k)} = \underbrace{R_{ij}^{(k-1)}}_{\text{path skips state } k} + \underbrace{R_{ik}^{(k-1)} \left( R_{kk}^{(k-1)} \right)^* R_{kj}^{(k-1)}}_{\text{path visits state } k \text{ at least once}}$$

</v-click>

<v-click>

The second term says: go from $i$ to $k$, loop at $k$ zero or more times, then go from $k$ to $j$ — all using intermediate states $\leq k-1$

</v-click>

---

# Method 1: Example

Convert the DFA that accepts strings containing $00$ as a substring

States: $q_1$ (start), $q_2$ (seen one 0), $q_3$ (seen 00, accepting)

<v-click>

**Basis ($k = 0$):**
- $R_{11}^{(0)} = \varepsilon + 1$, $\quad R_{12}^{(0)} = 0$, $\quad R_{13}^{(0)} = \emptyset$
- $R_{21}^{(0)} = 1$, $\quad R_{22}^{(0)} = \varepsilon$, $\quad R_{23}^{(0)} = 0$
- $R_{31}^{(0)} = \emptyset$, $\quad R_{32}^{(0)} = \emptyset$, $\quad R_{33}^{(0)} = \varepsilon + 0 + 1$

</v-click>

<v-click>

**Exercise:** Complete the construction by computing $R^{(1)}$, $R^{(2)}$, $R^{(3)}$, and finally the RE $R = R_{13}^{(3)}$

</v-click>

---

# Method 2: Generalized NFA (GNFA)

A **Generalized NFA (GNFA)** allows **regular expressions** as labels on transitions

<v-clicks>

**Formal definition:**
$$\delta: (Q - \{q_{\text{accept}}\}) \times (Q - \{q_0\}) \to \mathcal{R}$$

where start and accept states are **unique**

**Acceptance:** $G$ accepts $w = w_1 w_2 \ldots w_n$ (where $w_i \in \Sigma^*$) if there exists a sequence of states $q_0, q_1, \ldots, q_n = q_{\text{accept}}$ such that for all $i$:
$$w_i \in L(R_i) \quad \text{where } R_i = \delta(q_{i-1}, q_i)$$

</v-clicks>

---

# GNFA: Conversion Procedure

**Step 1:** Convert DFA to GNFA
- If no arrow $i \to j$, label it with $\emptyset$
- For each state $i$, label the self-loop with $\varepsilon$

<v-click>

**Step 2:** Eliminate states one by one

If state $q$ has:
- incoming edge $R_1$ from $q_i$
- self-loop $R_2$
- outgoing edge $R_3$ to $q_j$
- and direct edge $R_4$ from $q_i$ to $q_j$

Replace with single edge from $q_i$ to $q_j$:

$$q_i \xrightarrow{R_1 R_2^* R_3 + R_4} q_j$$

</v-click>

<v-click>

**Step 3:** Continue until only $q_{\text{start}} \xrightarrow{R} q_{\text{accept}}$ remains

The label $R$ is the desired regular expression!

</v-click>

---

# GNFA: Why It Works

<v-clicks>

**State elimination preserves the language:**

The new edge $R_1 R_2^* R_3 + R_4$ captures exactly the strings that could traverse from $q_i$ to $q_j$:
- $R_4$: go directly (not through $q$)
- $R_1 R_2^* R_3$: go to $q$ via $R_1$, loop zero or more times via $R_2$, leave via $R_3$

**Order of elimination doesn't matter** — different orders produce equivalent (though possibly different-looking) REs

**Exercise:** Show that NFAs and GNFAs are equivalent — they recognize the same class of languages

</v-clicks>

---

# The Complete Picture

**Theorem:** A language is regular if and only if it is given by some regular expression

<v-click>

We have now established the **equivalence of four formalisms**:

$$\text{DFA} \iff \text{NFA} \iff \varepsilon\text{-NFA} \iff \text{RE}$$

</v-click>

<v-click>

| Conversion | Method |
|-----------|--------|
| RE $\to$ $\varepsilon$-NFA | Structural induction (3 invariants) |
| NFA $\to$ DFA | Subset construction |
| DFA $\to$ RE | Dynamic Programming or GNFA |
| DFA $\to$ NFA | Trivial (every DFA is an NFA) |

Each formalism offers a different **perspective** on regular languages:
- **DFA:** algorithmic, deterministic
- **NFA:** design flexibility, compact
- **RE:** algebraic, declarative

</v-click>

---

# Summary

<v-clicks>

- **Regular Expressions** are defined by structural induction: basis ($a, \varepsilon, \emptyset$), induction ($E+F, EF, E^*$)

- **RE $\to$ $\varepsilon$-NFA:** Structural induction maintaining three invariants (one accept state, no arrows into start, no arrows out of accept)

- **DFA $\to$ RE: Method 1** (Dynamic Programming): Build $R_{ij}^{(k)}$ by induction on $k$, using the recurrence that paths either skip or visit state $k$

- **DFA $\to$ RE: Method 2** (GNFA): Eliminate states one by one, replacing edges with combined REs using the rule $R_1 R_2^* R_3 + R_4$

- **Four equivalent formalisms:** DFA, NFA, $\varepsilon$-NFA, RE — all describe exactly the class of regular languages

</v-clicks>

---

# Exercises

1. Define the semantics of RE: What are $L(a)$, $L(\varepsilon)$, $L(\emptyset)$, $L(E+F)$, $L(EF)$, $L(E^*)$?

2. Give a RE for the set of strings of 0s and 1s **not** containing 101 as a substring

3. Convert the RE $(0 + 01)^*$ to an $\varepsilon$-NFA using the structural induction method

4. For the DFA accepting strings with $00$ as a substring, compute $R^{(1)}$, $R^{(2)}$, $R^{(3)}$ and the final RE

5. Convert a 3-state DFA to a RE using the GNFA method

6. Show that NFAs and GNFAs are equivalent

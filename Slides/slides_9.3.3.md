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
mdc: false
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

Section 9.3.3 — An algebraic notation for regular languages, and its full equivalence with finite automata.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

From REs to $\varepsilon$-NFAs, and from DFAs back to REs — closing the loop on the four formalisms.

</div>

**Regular Expressions** provide an algebraic notation for describing regular languages


**Key concepts:**
1. **RE definition** — structural induction over $\Sigma$, $\varepsilon$, $\emptyset$
2. **RE semantics** — the language $L(R)$ described by an RE
3. **RE $\Rightarrow$ $\varepsilon$-NFA** — structural induction with invariants
4. **DFA $\Rightarrow$ RE** — two methods
   - Method 1: Dynamic Programming
   - Method 2: Generalized NFA (GNFA)
5. **The fundamental equivalence** — RE $\Leftrightarrow$ FA


Regular Expressions are familiar from text processing (grep, sed, VIM, etc.), though practical implementations go beyond the formal definition


---
layout: section
---

# RE Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three operations and three base cases — all built up by structural induction.

</div>

Algebraic notation for sets of strings

---

# Operations on Languages

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Union, concatenation, and Kleene star — the three building blocks REs are made of.

</div>

Three fundamental operations:


**Union:**
$$L \cup M = \{ w \mid w \in L \text{ or } w \in M \}$$

**Concatenation:**
$$LM = \{ xy \mid x \in L \text{ and } y \in M \}$$

**Kleene Star (Closure):**
$$L^* = \{ x_1 x_2 \ldots x_n \mid x_i \in L, n \geq 0 \}$$

Note: $n = 0$ gives $\varepsilon \in L^*$ for any $L$


---

# Regular Expressions: Formal Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

REs are *syntactic objects* — strings of symbols built up by recursive rules.

</div>

A **Regular Expression (RE)** is a syntactic object defined by **structural induction**:


**Basis Case:** The following are REs:
- $a \in \Sigma$ (any symbol from the alphabet)
- $\varepsilon$ (the empty string)
- $\emptyset$ (the empty set)

**Induction Step:** If $E, F$ are REs, then so are:
- $E + F$ (union)
- $EF$ (concatenation)
- $(E)^*$ (Kleene star)
- $(E)$ (parenthesization)


REs are a **model of computation**, just like DFAs or NFAs — they describe languages


---

# RE Semantics

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Each piece of RE syntax denotes a *language* — that's the meaning function $L(\cdot)$.

</div>

**Exercise:** What are the languages $L(a)$, $L(\varepsilon)$, $L(\emptyset)$, $L(E+F)$, $L(EF)$, $L(E^*)$?


**Answers:**
- $L(a) = \{a\}$
- $L(\varepsilon) = \{\varepsilon\}$
- $L(\emptyset) = \emptyset$
- $L(E + F) = L(E) \cup L(F)$
- $L(EF) = L(E) \cdot L(F) = \{xy \mid x \in L(E), y \in L(F)\}$
- $L(E^*) = (L(E))^*$


**Example:** RE for strings of 0s and 1s **not** containing 101 as a substring:

$$(\varepsilon + 0)(1^* + 00^*0)^*(\varepsilon + 0)$$


---
layout: section
---

# RE $\Leftrightarrow$ FA

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The headline theorem of the chapter — REs and finite automata describe the *same* class of languages.

</div>

The fundamental equivalence theorem

---

# The Equivalence Theorem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two directions to prove — RE-to-NFA, and DFA-to-RE — together they collapse all four formalisms.

</div>

**Theorem:** A language is regular if and only if it is given by some regular expression <span style="font-size: 0.6em; color: navy;">Thm 9.18, Pg 225, thm:2</span>


**Two directions to prove:**

1. **RE $\Rightarrow$ $\varepsilon$-NFA:** Convert a regular expression to an automaton
2. **DFA $\Rightarrow$ RE:** Convert an automaton to a regular expression


Combined with the DFA $\Leftrightarrow$ NFA equivalence from section 9.3.2:

$$\text{DFA} \iff \text{NFA} \iff \varepsilon\text{-NFA} \iff \text{RE}$$

All four formalisms describe **exactly** the same class of languages!


---

# RE to $\varepsilon$-NFA: Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Build the NFA piece by piece — three invariants make every step glue cleanly to the next.

</div>

Convert RE $R$ to an $\varepsilon$-NFA using **structural induction**


**Three invariants** maintained at each step — the NFA $A$ has:
1. Exactly **one** accepting state
2. **No arrow into** the initial state
3. **No arrow out of** the accepting state


**Convention:** If there is no arrow out of state $q$ on symbol $\sigma$, the computation **rejects**. (Formally: there is a "trash state" $T$ with self-loops on all symbols)


<!--
This structural induction construction is known as **Thompson's construction**, after Ken Thompson, who described it in his 1968 CACM paper "Programming Techniques: Regular expression search algorithm." Thompson used it to build one of the first practical regex engines, which powered the text editor QED and later ed — the standard Unix line editor (the "ed" in sed, grep's ancestor).

Thompson is one of the towering figures of CS. With Dennis Ritchie he created Unix (1969) and the B programming language (precursor to C). He later co-created UTF-8 encoding and the Go programming language. He won the Turing Award in 1983. His classic book with Ritchie — "The UNIX Programming Environment" (1984, co-authored with Rob Pike) — wait, actually the famous book is "The Unix Programming Environment" by Kernighan and Pike (1984). Thompson and Ritchie's iconic contribution was the paper "The UNIX Time-Sharing System" (1974, CACM). The whole ecosystem — Unix, C, regex, grep, lex — grew from the same Bell Labs culture of the 1970s.

The beauty of Thompson's construction is that it produces an NFA with at most 2n states for a regex of length n (linear!), and the three invariants we maintain are exactly what make the inductive step work cleanly.
-->

---

# RE to $\varepsilon$-NFA: Basis Case

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Tiny two-state machines for $\varepsilon$, $\emptyset$, and a single symbol — the atoms of the construction.

</div>

For the three base cases $\varepsilon$, $\emptyset$, and $a \in \Sigma$:


**$\varepsilon$:**

$\to \bigcirc \xrightarrow{\varepsilon} \bigodot$

(Start state connected to accept state via $\varepsilon$)

**$\emptyset$:**

$\to \bigcirc \qquad \bigodot$

(Start state and accept state with **no** connection)

**$a \in \Sigma$:**

$\to \bigcirc \xrightarrow{a} \bigodot$

(Start state connected to accept state via symbol $a$)


Each satisfies all three invariants: one accept state, no arrows in to start, no arrows out of accept


---

# RE to $\varepsilon$-NFA: Union ($R + S$)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A new start branches via $\varepsilon$ into both sub-machines, and they merge into a new accept.

</div>

Given NFAs for $R$ and $S$ (shown as boxes), build an NFA for $R + S$:


1. Create a **new start state**
2. Connect it via $\varepsilon$ to the start states of $R$ and $S$
3. Create a **new accept state**
4. Connect the accept states of $R$ and $S$ to it via $\varepsilon$

**Structure:**

$$\to \bigcirc \xrightarrow{\varepsilon} \boxed{R} \xrightarrow{\varepsilon} \bigodot$$
$$\qquad \searrow^{\varepsilon} \boxed{S} \nearrow^{\varepsilon}$$

All three invariants are preserved


---

# RE to $\varepsilon$-NFA: Concatenation ($RS$)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Glue $R$'s accept to $S$'s start with a single $\varepsilon$-arrow — that's all concatenation needs.

</div>

Given NFAs for $R$ and $S$, build an NFA for $RS$:


1. Chain $R$'s accept state to $S$'s start state via $\varepsilon$:

$$\to \boxed{R} \xrightarrow{\varepsilon} \boxed{S} \to \bigodot$$

- Start state = $R$'s start state
- Accept state = $S$'s accept state
- Old accept of $R$ and old start of $S$ become interior states

All three invariants are preserved


---

# RE to $\varepsilon$-NFA: Kleene Star ($R^*$)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Add a loop to repeat $R$ and a bypass to skip it entirely — handling the $\varepsilon$ case.

</div>

Given NFA for $R$, build an NFA for $R^*$:


1. Create a **new start state** (which is also the accept state, for $\varepsilon \in L(R^*)$)
2. Connect new start to $R$'s start via $\varepsilon$
3. Connect $R$'s accept back to $R$'s start via $\varepsilon$ (the loop)
4. Connect $R$'s accept to the new accept state via $\varepsilon$
5. Also: $\varepsilon$-transition from new start directly to new accept (bypass $R$ entirely)

**Key:** The bypass handles $\varepsilon \in R^*$; the loop handles $R, RR, RRR, \ldots$


---

# RE to $\varepsilon$-NFA: Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Watch the construction in action — assembling $(0 + 01)^*$ piece by piece, basis to star.

</div>

Convert $(0 + 01)^*$ step by step:


**Step 1:** Build NFAs for $0$ and $1$ (basis case)

$0: \to \bigcirc \xrightarrow{0} \bigodot \qquad 1: \to \bigcirc \xrightarrow{1} \bigodot$

**Step 2:** Build NFA for $01$ (concatenation)

$\to \bigcirc \xrightarrow{0} \bigcirc \xrightarrow{\varepsilon} \bigcirc \xrightarrow{1} \bigodot$

**Step 3:** Build NFA for $0 + 01$ (union)

**Step 4:** Build NFA for $(0 + 01)^*$ (star — add loop and bypass)


---
layout: section
---

# DFA to RE

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two routes back: dynamic programming on path indices, or state-elimination via GNFAs.

</div>

Two conversion methods

---

# Method 1: Dynamic Programming

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Define $R_{ij}^{(k)}$ — the RE for paths from $q_i$ to $q_j$ using only the first $k$ states as intermediates.

</div>

Given DFA $A$ with $n$ states, define:

$R_{ij}^{(k)}$ = RE whose language is the set of strings that take $A$ from state $q_i$ to state $q_j$ with all **intermediate** states having index $\leq k$


**The answer:** $R = R_{1j_1}^{(n)} + R_{1j_2}^{(n)} + \cdots + R_{1j_l}^{(n)}$ where $F = \{q_{j_1}, \ldots, q_{j_l}\}$

(Union over all accepting states, using all $n$ states as intermediates)


---

# Method 1: Basis and Induction

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A path either skips state $k$ entirely or visits it — that case split is the recurrence.

</div>

**Basis ($k = 0$):** No intermediate states allowed — only direct transitions

$$R_{ij}^{(0)} = x + a_1 + a_2 + \cdots + a_m$$

where $i \xrightarrow{a_l} j$ are direct transitions, and:
- $x = \emptyset$ if $i \neq j$
- $x = \varepsilon$ if $i = j$ (can stay in same state with empty string)


**Induction ($k > 0$):**

$$R_{ij}^{(k)} = \underbrace{R_{ij}^{(k-1)}}_{\text{path skips state } k} + \underbrace{R_{ik}^{(k-1)} \left( R_{kk}^{(k-1)} \right)^* R_{kj}^{(k-1)}}_{\text{path visits state } k \text{ at least once}}$$


The second term says: go from $i$ to $k$, loop at $k$ zero or more times, then go from $k$ to $j$ — all using intermediate states $\leq k-1$


---

# Method 1: Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Apply the DP recurrence to a 3-state DFA — and see why the table grows fast.

</div>

Convert the DFA that accepts strings containing $00$ as a substring

States: $q_1$ (start), $q_2$ (seen one 0), $q_3$ (seen 00, accepting)


**Basis ($k = 0$):**
- $R_{11}^{(0)} = \varepsilon + 1$, $\quad R_{12}^{(0)} = 0$, $\quad R_{13}^{(0)} = \emptyset$
- $R_{21}^{(0)} = 1$, $\quad R_{22}^{(0)} = \varepsilon$, $\quad R_{23}^{(0)} = 0$
- $R_{31}^{(0)} = \emptyset$, $\quad R_{32}^{(0)} = \emptyset$, $\quad R_{33}^{(0)} = \varepsilon + 0 + 1$


**Exercise:** Complete the construction by computing $R^{(1)}$, $R^{(2)}$, $R^{(3)}$, and finally the RE $R = R_{13}^{(3)}$


---

# Method 2: Generalized NFA (GNFA)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Allow whole REs as edge labels — a flexible intermediate form for collapsing automata into one expression.

</div>

A **Generalized NFA (GNFA)** allows **regular expressions** as labels on transitions


**Formal definition:**
$$\delta: (Q - \{q_{\text{accept}}\}) \times (Q - \{q_0\}) \to \mathcal{R}$$

where start and accept states are **unique**

**Acceptance:** $G$ accepts $w = w_1 w_2 \ldots w_n$ (where $w_i \in \Sigma^*$) if there exists a sequence of states $q_0, q_1, \ldots, q_n = q_{\text{accept}}$ such that for all $i$:
$$w_i \in L(R_i) \quad \text{where } R_i = \delta(q_{i-1}, q_i)$$


---

# GNFA: Conversion Procedure

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Rip out states one at a time, replacing detours with a single combined RE on each surviving edge.

</div>

**Step 1:** Convert DFA to GNFA
- If no arrow $i \to j$, label it with $\emptyset$
- For each state $i$, label the self-loop with $\varepsilon$


**Step 2:** Eliminate states one by one

If state $q$ has:
- incoming edge $R_1$ from $q_i$
- self-loop $R_2$
- outgoing edge $R_3$ to $q_j$
- and direct edge $R_4$ from $q_i$ to $q_j$

Replace with single edge from $q_i$ to $q_j$:

$$q_i \xrightarrow{R_1 R_2^* R_3 + R_4} q_j$$


**Step 3:** Continue until only $q_{\text{start}} \xrightarrow{R} q_{\text{accept}}$ remains

The label $R$ is the desired regular expression!


---

# GNFA: Why It Works

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The combined edge $R_1 R_2^* R_3 + R_4$ captures *exactly* the strings the eliminated state could carry.

</div>

**State elimination preserves the language:**

The new edge $R_1 R_2^* R_3 + R_4$ captures exactly the strings that could traverse from $q_i$ to $q_j$:
- $R_4$: go directly (not through $q$)
- $R_1 R_2^* R_3$: go to $q$ via $R_1$, loop zero or more times via $R_2$, leave via $R_3$

**Order of elimination doesn't matter** — different orders produce equivalent (though possibly different-looking) REs

**Exercise:** Show that NFAs and GNFAs are equivalent — they recognize the same class of languages


---

# The Complete Picture

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

DFA, NFA, $\varepsilon$-NFA, RE — four formalisms, one class of languages, four perspectives.

</div>

**Theorem:** A language is regular if and only if it is given by some regular expression <span style="font-size: 0.6em; color: navy;">Thm 9.18, Pg 225, thm:2</span>


We have now established the **equivalence of four formalisms**:

$$\text{DFA} \iff \text{NFA} \iff \varepsilon\text{-NFA} \iff \text{RE}$$


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


---

# Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Six problems exercising both directions of the equivalence — RE design, conversions, and a GNFA proof.

</div>

1. Define the semantics of RE: What are $L(a)$, $L(\varepsilon)$, $L(\emptyset)$, $L(E+F)$, $L(EF)$, $L(E^*)$?

2. Give a RE for the set of strings of 0s and 1s **not** containing 101 as a substring

3. Convert the RE $(0 + 01)^*$ to an $\varepsilon$-NFA using the structural induction method

4. For the DFA accepting strings with $00$ as a substring, compute $R^{(1)}$, $R^{(2)}$, $R^{(3)}$ and the final RE

5. Convert a 3-state DFA to a RE using the GNFA method

6. Show that NFAs and GNFAs are equivalent

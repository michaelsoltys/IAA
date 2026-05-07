---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.3.1: Deterministic Finite Automata
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Deterministic Finite Automata
mdc: false
---

# Deterministic Finite Automata

Section 9.3.1 — The simplest model of computation: finite memory, no tape, just states and transitions.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A roadmap for the section: from the 5-tuple definition all the way to closure under regular operations.

</div>

This section introduces the **Deterministic Finite Automaton (DFA)** — the simplest model of computation


**Key concepts:**
1. **DFA definition** — the 5-tuple $(Q, \Sigma, \delta, q_0, F)$
2. **Running a DFA** — how strings are accepted or rejected
3. **Transition diagrams and tables** — two ways to present $\delta$
4. **Extended Transition Function** — processing entire strings
5. **Language of a DFA** — the set of accepted strings
6. **Regular languages** — languages recognized by DFAs
7. **Regular operations** — union, concatenation, Kleene star


---
layout: section
---

# DFA Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The 5-tuple, the picture, and how a DFA actually runs on a string.

</div>

A model of computation without memory

---

# DFA: Formal Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

States, alphabet, transition function, start state, accepting set — the entire machine packed into five symbols.

</div>

A **Deterministic Finite Automaton (DFA)** is a 5-tuple $A = (Q, \Sigma, \delta, q_0, F)$


- **$Q$** — Finite set of **states**
- **$\Sigma$** — Finite set of input symbols (**alphabet**)
- **$\delta: Q \times \Sigma \to Q$** — **Transition function** (the "program")
  - Given $q \in Q$ and $a \in \Sigma$, $\delta(q, a) = p \in Q$
- **$q_0 \in Q$** — **Start state** (initial state)
- **$F \subseteq Q$** — Set of **final** (accepting) states


---

# Running a DFA

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Feed in symbols one at a time, follow the arrows — accept if you land in $F$ at the end.

</div>

To see whether $A$ **accepts** a string $w = a_1 a_2 \ldots a_n$:


$$\delta(q_0, a_1) = q_1, \quad \delta(q_1, a_2) = q_2, \quad \ldots, \quad \delta(q_{n-1}, a_n) = q_n$$

**Accept** iff $q_n \in F$

More precisely: $A$ accepts $w$ if there exists a sequence of states $r_0, r_1, \ldots, r_n$ such that:
1. $r_0 = q_0$ (start in the initial state)
2. $\delta(r_i, w_{i+1}) = r_{i+1}$ for $i = 0, 1, \ldots, n-1$
3. $r_n \in F$ (end in an accepting state)

Otherwise, $A$ **rejects** $w$


---

# Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A 3-state DFA for the language of binary strings containing $01$ as a substring.

</div>

A language with a DFA

<div class="grid grid-cols-2 gap-8">
<div>

$L_{01} = \{ w \mid w \text{ is of the form } x01y \in \Sigma^* \}$

The set of strings over $\Sigma = \{0, 1\}$ containing $01$ as a substring


So: $111 \notin L_{01}$, but $001 \in L_{01}$

**DFA:** i
- $\Sigma = \{0,1\}$
- $Q = \{q_0, q_1, q_2\}$
- $F = \{q_1\}$


</div>
<div>


**Transition table:**
$$
\begin{array}{c||c|c}
       & 0   & 1   \\\hline\hline
q_0    & q_2 & q_0 \\\hline
\ast q_1 & q_1 & q_1 \\\hline
q_2    & q_2 & q_1
\end{array}
$$


**Transition diagram:**

<img src="/Figures/L01.drawio.svg" class="h-50" />


</div>
</div>

---

# Understanding the $L_{01}$ DFA

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Each state encodes *what we've seen so far* — the DFA's only memory is which state it's in.

</div>

The three states capture the "memory" of the automaton:


- **$q_0$** — Haven't seen a $0$ yet (still looking)
  - On $1$: stay in $q_0$ (still no $0$)
  - On $0$: go to $q_2$ (saw a $0$!)

- **$q_2$** — Have seen a $0$, waiting for a $1$
  - On $0$: stay in $q_2$ (still have a recent $0$)
  - On $1$: go to $q_1$ (saw $01$!)

- **$q_1$** — Have seen $01$ — **accept** (absorbing state)
  - On $0$ or $1$: stay in $q_1$ (already accepted)


**Note:** Simply presenting a DFA is not sufficient — we must also **prove** it is correct!


---

# Transition Diagram vs Transition Table

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A picture and a table — same information, different audiences. Use whichever helps you debug.

</div>

Two equivalent ways to present the transition function $\delta$:


**Transition diagram:** A directed graph
- Nodes = states (double circle for accepting)
- Arrows labeled with symbols = transitions
- Arrow from nowhere = start state

**Transition table:** A matrix
- Rows = states
- Columns = input symbols
- Entries = next states
- $\ast$ marks accepting states

Both encode the same information — use whichever is clearer


---

# Exercises: Designing DFAs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Practice the hardest skill in this chapter: figuring out *what to remember* with finitely many states.

</div>

**Exercise 1:** Design a DFA for $\{ w : |w| \geq 3 \text{ and its third symbol is } 0 \}$

**Exercise 2:** Design a DFA for $\{ w : \text{every odd position of } w \text{ is a } 1 \}$

**Exercise 3:** Consider these two languages:
- $B_n = \{ a^k : k \text{ is a multiple of } n \} \subseteq \{a\}^*$
- $C_n = \{ (w)_b \in \{0,1\}^* : w \text{ is divisible by } n \}$

where $(w)_b$ is the binary representation of $w \in \mathbb{N}$. What are their DFAs?

**Exercise 4:** Design a DFA for a vending machine over alphabet $\{\textcircled{1}, \textcircled{5}, \textcircled{10}, \textcircled{25}\}$ that accepts sequences of coins summing to a multiple of 25


---
layout: section
---

# Extended Transition Function

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Going from "process one symbol" to "process a whole string" — by induction on length.

</div>

Processing entire strings

---

# Extended Transition Function (ETF)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Lift $\delta$ from one symbol to whole strings via induction — the official way to define acceptance.

</div>

Given $\delta$, define the **Extended Transition Function** $\hat\delta$ inductively:


**Basis Case:**
$$\hat\delta(q, \varepsilon) = q$$

**Induction Step:** If $w = xa$ where $x \in \Sigma^*$ and $a \in \Sigma$:
$$\hat\delta(q, w) = \hat\delta(q, xa) = \delta(\hat\delta(q, x), a)$$


**Key properties:**
- $\hat\delta: Q \times \Sigma^* \to Q$ (extends $\delta$ from single symbols to strings)
- $w \in L(A) \iff \hat\delta(q_0, w) \in F$


---

# ETF: Intuition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Watch the recursion peel off symbols from the right, then collapse back left to right.

</div>

The ETF processes a string **one symbol at a time**, left to right:


To compute $\hat\delta(q_0, \texttt{1001})$:

$$\hat\delta(q_0, \texttt{1001}) = \delta(\hat\delta(q_0, \texttt{100}), \texttt{1})$$
$$= \delta(\delta(\hat\delta(q_0, \texttt{10}), \texttt{0}), \texttt{1})$$
$$= \delta(\delta(\delta(\hat\delta(q_0, \texttt{1}), \texttt{0}), \texttt{0}), \texttt{1})$$
$$= \delta(\delta(\delta(\delta(\hat\delta(q_0, \varepsilon), \texttt{1}), \texttt{0}), \texttt{0}), \texttt{1})$$
$$= \delta(\delta(\delta(\delta(q_0, \texttt{1}), \texttt{0}), \texttt{0}), \texttt{1})$$


The recursion "peels off" the last symbol until reaching $\varepsilon$, then evaluates $\delta$ from left to right


---
layout: section
---

# Language and Regular Languages

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

What set of strings does a DFA *mean* — and which sets can DFAs describe at all?

</div>

Defining the class of regular languages

---

# Language of a DFA

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The DFA is a piece of *syntax*; the language $L(A)$ is its *semantics* — the set of strings it accepts.

</div>

The **language** of a DFA $A$ is:
$$L(A) = \{ w \mid \hat\delta(q_0, w) \in F \}$$


**Important distinction:**
- $A$ is a **syntactic** object (a machine, a piece of "hardware")
- $L(A)$ is a **semantic** object (a set of strings, a "meaning")

$L$ is a function that assigns a **meaning** or **interpretation** to a syntactic object

This syntax/semantics distinction is fundamental in computer science


---

# Regular Languages

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A language is *regular* exactly when some DFA recognizes it — and three operations preserve that property.

</div>

**Definition:** A language $L$ is **regular** iff there exists a DFA $A$ such that $L = L(A)$


What operations on languages **preserve** regularity?


**Regular operations:**
1. **Union:** $L \cup M = \{ w \mid w \in L \text{ or } w \in M \}$
2. **Concatenation:** $LM = \{ xy \mid x \in L \text{ and } y \in M \}$
3. **Kleene Star:** $L^* = \{ x_1 x_2 \ldots x_n \mid x_i \in L, n \geq 0 \}$


**Caution:** For alphabets, $\Sigma^+ = \Sigma^* - \{\varepsilon\}$. But for general languages, $L^+ = L^* - \{\varepsilon\}$ is **not** necessarily true! (Why?)


---

# Closure Under Regular Operations

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The product construction: run two DFAs in parallel as one machine over pairs of states.

</div>

**Theorem:** Regular languages are closed under regular operations (union, concatenation, and Kleene star) <span style="font-size: 0.6em; color: navy;">Thm 9.8, Pg 221, thm:1</span>


**Proof (union):** Given regular $A, B$ with DFAs $M_1, M_2$:

Build DFA $M$ with $Q_M = Q_{M_1} \times Q_{M_2}$ (Cartesian product)

$$\delta_M((r_1, r_2), a) = (\delta_{M_1}(r_1, a), \delta_{M_2}(r_2, a))$$

Accept if either component reaches an accepting state


**Key idea:** The state of $M$ is really a **pair** of states — one from each machine. States are just finite descriptors; they can be anything, including sets of states from other machines!

**For concatenation and star:** We need **nondeterminism** (next section)


---

# Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Six problems to consolidate the chapter — proofs, designs, and one subtle question about $L^+$.

</div>

1. Prove that the DFA for $L_{01}$ is correct (by induction on $|w|$)

2. Design a DFA for $\{ w : |w| \geq 3 \text{ and the third symbol is } 0 \}$

3. Design a DFA for $\{ w : \text{every odd position is a } 1 \}$

4. Design DFAs for $B_n$ (multiples of $n$ in unary) and $C_n$ (multiples of $n$ in binary)

5. Why is $L^+ = L^* - \{\varepsilon\}$ not necessarily true for a general language $L$?

6. Complete the proof of closure under union by specifying the accepting states of the product construction

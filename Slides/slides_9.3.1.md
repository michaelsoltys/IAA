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

# Deterministic Finite Automata

Section 9.3.1 - Regular Languages

---

# Overview

This section introduces the **Deterministic Finite Automaton (DFA)** — the simplest model of computation

<v-clicks>

**Key concepts:**
1. **DFA definition** — the 5-tuple $(Q, \Sigma, \delta, q_0, F)$
2. **Running a DFA** — how strings are accepted or rejected
3. **Transition diagrams and tables** — two ways to present $\delta$
4. **Extended Transition Function** — processing entire strings
5. **Language of a DFA** — the set of accepted strings
6. **Regular languages** — languages recognized by DFAs
7. **Regular operations** — union, concatenation, Kleene star

</v-clicks>

---
layout: section
---

# DFA Definition

A model of computation without memory

---

# DFA: Formal Definition

A **Deterministic Finite Automaton (DFA)** is a 5-tuple $A = (Q, \Sigma, \delta, q_0, F)$

<v-clicks>

- **$Q$** — Finite set of **states**
- **$\Sigma$** — Finite set of input symbols (**alphabet**)
- **$\delta: Q \times \Sigma \to Q$** — **Transition function** (the "program")
  - Given $q \in Q$ and $a \in \Sigma$, $\delta(q, a) = p \in Q$
- **$q_0 \in Q$** — **Start state** (initial state)
- **$F \subseteq Q$** — Set of **final** (accepting) states

</v-clicks>

---

# Running a DFA

To see whether $A$ **accepts** a string $w = a_1 a_2 \ldots a_n$:

<v-clicks>

$$\delta(q_0, a_1) = q_1, \quad \delta(q_1, a_2) = q_2, \quad \ldots, \quad \delta(q_{n-1}, a_n) = q_n$$

**Accept** iff $q_n \in F$

More precisely: $A$ accepts $w$ if there exists a sequence of states $r_0, r_1, \ldots, r_n$ such that:
1. $r_0 = q_0$ (start in the initial state)
2. $\delta(r_i, w_{i+1}) = r_{i+1}$ for $i = 0, 1, \ldots, n-1$
3. $r_n \in F$ (end in an accepting state)

Otherwise, $A$ **rejects** $w$

</v-clicks>

---

# Example: Language $L_{01}$

$$L_{01} = \{ w \mid w \text{ is of the form } x01y \in \Sigma^* \}$$

The set of strings over $\Sigma = \{0, 1\}$ that contain $01$ as a substring

<v-click>

So: $111 \notin L_{01}$, but $001 \in L_{01}$

</v-click>

<v-click>

**DFA:** $\Sigma = \{0,1\}$, $Q = \{q_0, q_1, q_2\}$, $F = \{q_1\}$

</v-click>

<v-click>

**Transition table:**

| | $0$ | $1$ |
|---|---|---|
| $q_0$ | $q_2$ | $q_0$ |
| $\ast q_1$ | $q_1$ | $q_1$ |
| $q_2$ | $q_2$ | $q_1$ |

</v-click>

---

# Understanding the $L_{01}$ DFA

The three states capture the "memory" of the automaton:

<v-clicks>

- **$q_0$** — Haven't seen a $0$ yet (still looking)
  - On $1$: stay in $q_0$ (still no $0$)
  - On $0$: go to $q_2$ (saw a $0$!)

- **$q_2$** — Have seen a $0$, waiting for a $1$
  - On $0$: stay in $q_2$ (still have a recent $0$)
  - On $1$: go to $q_1$ (saw $01$!)

- **$q_1$** — Have seen $01$ — **accept** (absorbing state)
  - On $0$ or $1$: stay in $q_1$ (already accepted)

</v-clicks>

<v-click>

**Note:** Simply presenting a DFA is not sufficient — we must also **prove** it is correct!

</v-click>

---

# Transition Diagram vs Transition Table

Two equivalent ways to present the transition function $\delta$:

<v-clicks>

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

</v-clicks>

---

# Exercises: Designing DFAs

<v-clicks>

**Exercise 1:** Design a DFA for $\{ w : |w| \geq 3 \text{ and its third symbol is } 0 \}$

**Exercise 2:** Design a DFA for $\{ w : \text{every odd position of } w \text{ is a } 1 \}$

**Exercise 3:** Consider these two languages:
- $B_n = \{ a^k : k \text{ is a multiple of } n \} \subseteq \{a\}^*$
- $C_n = \{ (w)_b \in \{0,1\}^* : w \text{ is divisible by } n \}$

where $(w)_b$ is the binary representation of $w \in \mathbb{N}$. What are their DFAs?

**Exercise 4:** Design a DFA for a vending machine over alphabet $\{1¢, 5¢, 10¢, 25¢\}$ that accepts sequences of coins summing to a multiple of 25

</v-clicks>

---
layout: section
---

# Extended Transition Function

Processing entire strings

---

# Extended Transition Function (ETF)

Given $\delta$, define the **Extended Transition Function** $\hat\delta$ inductively:

<v-clicks>

**Basis Case:**
$$\hat\delta(q, \varepsilon) = q$$

**Induction Step:** If $w = xa$ where $x \in \Sigma^*$ and $a \in \Sigma$:
$$\hat\delta(q, w) = \hat\delta(q, xa) = \delta(\hat\delta(q, x), a)$$

</v-clicks>

<v-click>

**Key properties:**
- $\hat\delta: Q \times \Sigma^* \to Q$ (extends $\delta$ from single symbols to strings)
- $w \in L(A) \iff \hat\delta(q_0, w) \in F$

</v-click>

---

# ETF: Intuition

The ETF processes a string **one symbol at a time**, left to right:

<v-click>

To compute $\hat\delta(q_0, \texttt{1001})$:

$$\hat\delta(q_0, \texttt{1001}) = \delta(\hat\delta(q_0, \texttt{100}), \texttt{1})$$
$$= \delta(\delta(\hat\delta(q_0, \texttt{10}), \texttt{0}), \texttt{1})$$
$$= \delta(\delta(\delta(\hat\delta(q_0, \texttt{1}), \texttt{0}), \texttt{0}), \texttt{1})$$
$$= \delta(\delta(\delta(\delta(\hat\delta(q_0, \varepsilon), \texttt{1}), \texttt{0}), \texttt{0}), \texttt{1})$$
$$= \delta(\delta(\delta(\delta(q_0, \texttt{1}), \texttt{0}), \texttt{0}), \texttt{1})$$

</v-click>

<v-click>

The recursion "peels off" the last symbol until reaching $\varepsilon$, then evaluates $\delta$ from left to right

</v-click>

---
layout: section
---

# Language and Regular Languages

Defining the class of regular languages

---

# Language of a DFA

The **language** of a DFA $A$ is:
$$L(A) = \{ w \mid \hat\delta(q_0, w) \in F \}$$

<v-clicks>

**Important distinction:**
- $A$ is a **syntactic** object (a machine, a piece of "hardware")
- $L(A)$ is a **semantic** object (a set of strings, a "meaning")

$L$ is a function that assigns a **meaning** or **interpretation** to a syntactic object

This syntax/semantics distinction is fundamental in computer science

</v-clicks>

---

# Regular Languages

**Definition:** A language $L$ is **regular** iff there exists a DFA $A$ such that $L = L(A)$

<v-click>

What operations on languages **preserve** regularity?

</v-click>

<v-click>

**Regular operations:**
1. **Union:** $L \cup M = \{ w \mid w \in L \text{ or } w \in M \}$
2. **Concatenation:** $LM = \{ xy \mid x \in L \text{ and } y \in M \}$
3. **Kleene Star:** $L^* = \{ x_1 x_2 \ldots x_n \mid x_i \in L, n \geq 0 \}$

</v-click>

<v-click>

**Caution:** For alphabets, $\Sigma^+ = \Sigma^* - \{\varepsilon\}$. But for general languages, $L^+ = L^* - \{\varepsilon\}$ is **not** necessarily true! (Why?)

</v-click>

---

# Closure Under Regular Operations

**Theorem:** Regular languages are closed under regular operations (union, concatenation, and Kleene star)

<v-click>

**Proof (union):** Given regular $A, B$ with DFAs $M_1, M_2$:

Build DFA $M$ with $Q_M = Q_{M_1} \times Q_{M_2}$ (Cartesian product)

$$\delta_M((r_1, r_2), a) = (\delta_{M_1}(r_1, a), \delta_{M_2}(r_2, a))$$

Accept if either component reaches an accepting state

</v-click>

<v-click>

**Key idea:** The state of $M$ is really a **pair** of states — one from each machine. States are just finite descriptors; they can be anything, including sets of states from other machines!

**For concatenation and star:** We need **nondeterminism** (next section)

</v-click>

---

# Summary

<v-clicks>

- A **DFA** is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$ — a finite-state machine with no memory beyond its current state

- DFAs are presented as **transition diagrams** (graphs) or **transition tables** (matrices)

- The **Extended Transition Function** $\hat\delta$ processes entire strings by applying $\delta$ one symbol at a time

- The **language** $L(A)$ is the set of strings accepted by $A$ — a semantic interpretation of a syntactic object

- A language is **regular** if some DFA recognizes it

- Regular languages are **closed** under union, concatenation, and Kleene star

- Closure under union uses the **product construction**; concatenation and star require **nondeterminism**

</v-clicks>

---

# Exercises

1. Prove that the DFA for $L_{01}$ is correct (by induction on $|w|$)

2. Design a DFA for $\{ w : |w| \geq 3 \text{ and the third symbol is } 0 \}$

3. Design a DFA for $\{ w : \text{every odd position is a } 1 \}$

4. Design DFAs for $B_n$ (multiples of $n$ in unary) and $C_n$ (multiples of $n$ in binary)

5. Why is $L^+ = L^* - \{\varepsilon\}$ not necessarily true for a general language $L$?

6. Complete the proof of closure under union by specifying the accepting states of the product construction

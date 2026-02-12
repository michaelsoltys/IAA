---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.3.2: Nondeterministic Finite Automata
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Nondeterministic Finite Automata
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

# Nondeterministic Finite Automata

Section 9.3.2 - Regular Languages

---

# Overview

This section introduces **nondeterminism** — a more flexible (but equally powerful) model

<v-clicks>

**Key concepts:**
1. **NFA definition** — transition relation instead of function
2. **Nondeterministic branching** — multiple possible next states
3. **$\varepsilon$-transitions** — moving without consuming input
4. **$\varepsilon$-closure** — all states reachable via $\varepsilon$
5. **Extended transition relation** — processing strings in an NFA
6. **Subset construction** — converting NFA to DFA
7. **DFA $\Leftrightarrow$ NFA equivalence** — same class of languages

</v-clicks>

---
layout: section
---

# NFA Definition

Transition relations and branching

---

# From DFA to NFA

A **Nondeterministic Finite Automaton (NFA)** is defined like a DFA, except the transition function becomes a **transition relation**:

<v-clicks>

$$\delta \subseteq Q \times \Sigma \times Q$$

On the same pair $(q, a)$ there may be **more than one** possible next state (or **none**)

Equivalently:
$$\delta: Q \times \Sigma \to \mathcal{P}(Q)$$

where $\mathcal{P}(Q)$ is the **power set** of $Q$

</v-clicks>

<v-click>

**Analogy:** Like the `fork()` mechanism in C — in a particular configuration, an NFA can be in **several states simultaneously**, allowing a degree of parallelism

</v-click>

---

# NFA Acceptance

An NFA $N$ **accepts** $w = y_1 y_2 \ldots y_m$ (where $y_i \in \Sigma \cup \{\varepsilon\}$) if:

<v-clicks>

There exists a sequence of states $r_0, r_1, \ldots, r_m$ such that:
1. $r_0 = q_0$ (start in initial state)
2. $r_{i+1} \in \delta(r_i, y_{i+1})$ for $i = 0, 1, \ldots, m-1$
3. $r_m \in F$ (end in an accepting state)

**Key point:** $w$ is accepted if there **exists** a padding of $w$ with $\varepsilon$'s for which there **exists** an accepting sequence of states

The NFA accepts if **at least one** computation path leads to acceptance

</v-clicks>

---

# Example: $L_n$ — $n$-th Symbol from End

$L_n = \{ w \mid \text{the } n\text{-th symbol from the end is } 1 \}$

<v-click>

**NFA for $L_n$:**

$$q_0 \xrightarrow{1} q_1 \xrightarrow{0,1} q_2 \xrightarrow{0,1} \cdots \xrightarrow{0,1} q_n$$

with self-loop $q_0 \xrightarrow{0,1} q_0$ and $q_n$ accepting

- States: $q_0, q_1, \ldots, q_n$ — only $n + 1$ states!
- The NFA "guesses" when the $n$-th from last position occurs

</v-click>

<v-click>

**Question:** How many states does any DFA for $L_n$ require?

**Answer:** At least $2^n$ states! The NFA is **exponentially** more compact

</v-click>

---

# $\varepsilon$-Transitions

An **$\varepsilon$-NFA** extends the NFA with $\varepsilon$-transitions — transitions that consume **no input**:

$$\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to \mathcal{P}(Q)$$

<v-click>

**Example: Decimal numbers**

An $\varepsilon$-NFA accepting decimal numbers like $3.14$, $51.$, $.14$, $+3.0$, $-0.5$ but **not** a bare decimal point:

<img src="/Figures/floating-point.drawio.svg" class="mx-auto h-48 my-4" />

$\varepsilon$-transitions are convenient for **designing** NFAs by connecting sub-machines

</v-click>

---

# $\varepsilon$-Closure

To define the ETF for $\varepsilon$-NFAs, we need the **$\varepsilon$-closure**:

<v-clicks>

Given state $q$, $\varepsilon\text{-close}(q)$ is the set of all states reachable from $q$ by following arrows labeled $\varepsilon$

**Formal definition (inductive):**
- $q \in \varepsilon\text{-close}(q)$ (reflexive)
- If $p \in \varepsilon\text{-close}(q)$ and $p \xrightarrow{\varepsilon} r$, then $r \in \varepsilon\text{-close}(q)$ (transitive)

**For a set of states $S$:**
$$\varepsilon\text{-close}(S) = \bigcup_{q \in S} \varepsilon\text{-close}(q)$$

</v-clicks>

---

# Extended Transition Relation for NFAs

Define $\hat\delta$ for $\varepsilon$-NFAs:

<v-clicks>

**Basis:** $\hat\delta(q, \varepsilon) = \varepsilon\text{-close}(q)$

**Induction:** Suppose $w = xa$

Let $\hat\delta(q, x) = \{p_1, p_2, \ldots, p_n\}$

and $\bigcup_{i=1}^{n} \delta(p_i, a) = \{r_1, r_2, \ldots, r_m\}$

Then:
$$\hat\delta(q, w) = \bigcup_{i=1}^{m} \varepsilon\text{-close}(r_i)$$

</v-clicks>

<v-click>

**Intuition:** Process the string, and after each real transition on a symbol, follow all possible $\varepsilon$-transitions

</v-click>

---
layout: section
---

# Subset Construction

Converting NFA to DFA

---

# The Subset Construction

**Theorem:** DFAs and NFAs (including $\varepsilon$-NFAs) are equivalent

<v-click>

**Proof ($\Rightarrow$):** Every DFA is a restricted NFA (trivial)

</v-click>

<v-click>

**Proof ($\Leftarrow$):** Given NFA $N$, construct DFA $M$:

$$Q_M = \mathcal{P}(Q_N) \qquad \text{(subsets of NFA states)}$$
$$(q_M)_0 = \varepsilon\text{-close}(\{(q_N)_0\})$$
$$F_M = \{ S \in \mathcal{P}(Q_N) : S \cap F_N \neq \emptyset \}$$
$$\delta_M(S, a) = \bigcup_{q \in S} \varepsilon\text{-close}(\delta_N(q, a))$$

</v-click>

<v-click>

**Cost:** Since $|\mathcal{P}(Q_N)| = 2^{|Q_N|}$, there is a potential **exponential blowup** in states

This is expected: we simulate a more expressive model (NFA) with a more restricted one (DFA)

</v-click>

---

# Subset Construction: Example

Convert the NFA for $L_2$ (penultimate symbol is $0$) to a DFA

<v-clicks>

**NFA:** 4 states $\{q_0, q_1, q_2, q_3\}$ — self-loop at $q_0$, nondeterministic branch on $0$

**DFA via subset construction:** States are subsets of $\{q_0, q_1, q_2, q_3\}$

Potentially $2^4 = 16$ states

**Observation:** Many states are **unreachable** from the initial state $\{q_0\}$

**Optimization:** Only generate states reachable from $\{q_0\}$ — start from $\{q_0\}$ and explore transitions on demand

</v-clicks>

---

# Exponential Blowup is Sometimes Necessary

**Exercise:** Construct a family of NFAs $N_k$ such that:
- $|Q_{N_k}| = O(k)$ (linear in $k$)
- The smallest equivalent DFA $D_k$ has $|Q_{D_k}| = O(2^k)$ (exponential!)

<v-click>

The language $L_n$ (the $n$-th symbol from the end is $1$) provides such a family:
- NFA: $n + 1$ states
- Any DFA: at least $2^n$ states

</v-click>

<v-click>

**Takeaway:** The exponential blowup in the subset construction is not an artifact of the construction — it is sometimes **unavoidable**

</v-click>

---

# DFA $\Leftrightarrow$ NFA Equivalence

**Corollary:** A language is regular
- $\iff$ it is recognized by some DFA
- $\iff$ it is recognized by some NFA
- $\iff$ it is recognized by some $\varepsilon$-NFA

<v-click>

**Implications:**

Nondeterminism **does not increase** the expressive power of finite automata — DFAs and NFAs recognize exactly the same class of languages

But NFAs can be **exponentially more compact** than equivalent DFAs

</v-click>

<v-click>

**Exercise:** Finish the proof that regular languages are closed under concatenation and Kleene star (these are easier to show with NFAs than DFAs)

</v-click>

---

# Summary

<v-clicks>

- An **NFA** uses a transition **relation** — multiple next states (or none) are possible

- **$\varepsilon$-transitions** allow state changes without consuming input

- **$\varepsilon$-closure** captures all states reachable via $\varepsilon$-transitions

- The **subset construction** converts any NFA to an equivalent DFA
  - DFA states = subsets of NFA states
  - Potential exponential blowup: $2^n$ states

- **DFAs and NFAs are equivalent** in power — they recognize the same class of languages

- NFAs can be **exponentially more compact** (e.g., $L_n$: $n+1$ NFA states vs. $2^n$ DFA states)

- NFAs make it easier to prove closure under **concatenation** and **Kleene star**

</v-clicks>

---

# Exercises

1. How many states does any DFA for $L_n$ require? Prove your answer

2. Explain why, when padding a string with $\varepsilon$'s, we never need a contiguous stretch longer than the number of states

3. Modify the subset construction so that only states reachable from the initial state are generated

4. Construct a family of NFAs $N_k$ where $|Q_{N_k}| = O(k)$ but the equivalent DFA has $O(2^k)$ states

5. Use NFAs to prove that regular languages are closed under concatenation

6. Use NFAs to prove that regular languages are closed under Kleene star

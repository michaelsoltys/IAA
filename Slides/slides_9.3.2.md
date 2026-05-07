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

# Nondeterministic Finite Automata

Section 9.3.2 — Let the machine guess: same languages as DFAs, but exponentially smaller.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

NFAs, $\varepsilon$-transitions, and the subset construction — three ways nondeterminism stays inside regular languages.

</div>

This section introduces **nondeterminism** — a more flexible (but equally powerful) model


**Key concepts:**
1. **NFA definition** — transition relation instead of function
2. **Nondeterministic branching** — multiple possible next states
3. **$\varepsilon$-transitions** — moving without consuming input
4. **$\varepsilon$-closure** — all states reachable via $\varepsilon$
5. **Extended transition relation** — processing strings in an NFA
6. **Subset construction** — converting NFA to DFA
7. **DFA $\Leftrightarrow$ NFA equivalence** — same class of languages


---
layout: section
---

# NFA Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Replace the transition function with a relation — now a state can branch into many possibilities.

</div>

Transition relations and branching

---

# From DFA to NFA

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

One small change in the transition function — and the machine can be in many states at once.

</div>

A **Nondeterministic Finite Automaton (NFA)** is defined like a DFA, except the transition function becomes a **transition relation**:


$$\delta \subseteq Q \times \Sigma \times Q$$

On the same pair $(q, a)$ there may be **more than one** possible next state (or **none**)

Equivalently:
$$\delta: Q \times \Sigma \to \mathcal{P}(Q)$$

where $\mathcal{P}(Q)$ is the **power set** of $Q$


**Analogy:** Like the `fork()` mechanism in C — in a particular configuration, an NFA can be in **several states simultaneously**, allowing a degree of parallelism


---

# NFA Acceptance

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

An NFA accepts if *some* run lands in $F$ — existential, not universal.

</div>

An NFA $N$ **accepts** $w = y_1 y_2 \ldots y_m$ (where $y_i \in \Sigma \cup \{\varepsilon\}$) if:


There exists a sequence of states $r_0, r_1, \ldots, r_m$ such that:
1. $r_0 = q_0$ (start in initial state)
2. $r_{i+1} \in \delta(r_i, y_{i+1})$ for $i = 0, 1, \ldots, m-1$
3. $r_m \in F$ (end in an accepting state)

**Key point:** $w$ is accepted if there **exists** a padding of $w$ with $\varepsilon$'s for which there **exists** an accepting sequence of states

The NFA accepts if **at least one** computation path leads to acceptance


---

# Example: $L_n$ — $n$-th Symbol from End

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The classic exponential gap: $n+1$ NFA states vs at least $2^n$ DFA states for the same language.

</div>

$L_n = \{ w \mid \text{the } n\text{-th symbol from the end is } 1 \}$


**NFA for $L_n$:**

$$q_0 \xrightarrow{1} q_1 \xrightarrow{0,1} q_2 \xrightarrow{0,1} \cdots \xrightarrow{0,1} q_n$$

with self-loop $q_0 \xrightarrow{0,1} q_0$ and $q_n$ accepting

- States: $q_0, q_1, \ldots, q_n$ — only $n + 1$ states!
- The NFA "guesses" when the $n$-th from last position occurs


**Question:** How many states does any DFA for $L_n$ require?

**Answer:** At least $2^n$ states! The NFA is **exponentially** more compact


---

# $\varepsilon$-Transitions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Free moves between states — handy for gluing sub-machines together when building NFAs.

</div>

An **$\varepsilon$-NFA** extends the NFA with $\varepsilon$-transitions — transitions that consume **no input**:

$$\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to \mathcal{P}(Q)$$


**Example: Decimal numbers**

An $\varepsilon$-NFA accepting decimal numbers like $3.14$, $51.$, $.14$, $+3.0$, $-0.5$ but **not** a bare decimal point:

<img src="/Figures/floating-point.drawio.svg" class="mx-auto h-48 my-4" />

$\varepsilon$-transitions are convenient for **designing** NFAs by connecting sub-machines


---

# $\varepsilon$-Closure

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

All states you can drift to "for free" from $q$ — needed before you can define string acceptance.

</div>

To define the ETF for $\varepsilon$-NFAs, we need the **$\varepsilon$-closure**:


Given state $q$, $\varepsilon\text{-close}(q)$ is the set of all states reachable from $q$ by following arrows labeled $\varepsilon$

**Formal definition (inductive):**
- $q \in \varepsilon\text{-close}(q)$ (reflexive)
- If $p \in \varepsilon\text{-close}(q)$ and $p \xrightarrow{\varepsilon} r$, then $r \in \varepsilon\text{-close}(q)$ (transitive)

**For a set of states $S$:**
$$\varepsilon\text{-close}(S) = \bigcup_{q \in S} \varepsilon\text{-close}(q)$$


---

# Extended Transition Relation for NFAs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

After each real symbol, take every $\varepsilon$-jump available — that's the entire trick.

</div>

Define $\hat\delta$ for $\varepsilon$-NFAs:


**Basis:** $\hat\delta(q, \varepsilon) = \varepsilon\text{-close}(q)$

**Induction:** Suppose $w = xa$

Let $\hat\delta(q, x) = \{p_1, p_2, \ldots, p_n\}$

and $\bigcup_{i=1}^{n} \delta(p_i, a) = \{r_1, r_2, \ldots, r_m\}$

Then:
$$\hat\delta(q, w) = \bigcup_{i=1}^{m} \varepsilon\text{-close}(r_i)$$


**Intuition:** Process the string, and after each real transition on a symbol, follow all possible $\varepsilon$-transitions


---
layout: section
---

# Subset Construction

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Track *which subset* of NFA states you might be in — that subset is itself a DFA state.

</div>

Converting NFA to DFA

---

# The Subset Construction

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The DFA's states are *sets* of NFA states — at the cost of a $2^n$ blowup in the worst case.

</div>

**Theorem:** DFAs and NFAs (including $\varepsilon$-NFAs) are equivalent


**Proof ($\Rightarrow$):** Every DFA is a restricted NFA (trivial)


**Proof ($\Leftarrow$):** Given NFA $N$, construct DFA $M$:

$$Q_M = \mathcal{P}(Q_N) \qquad \text{(subsets of NFA states)}$$
$$(q_M)_0 = \varepsilon\text{-close}(\{(q_N)_0\})$$
$$F_M = \{ S \in \mathcal{P}(Q_N) : S \cap F_N \neq \emptyset \}$$
$$\delta_M(S, a) = \bigcup_{q \in S} \varepsilon\text{-close}(\delta_N(q, a))$$


**Cost:** Since $|\mathcal{P}(Q_N)| = 2^{|Q_N|}$, there is a potential **exponential blowup** in states

This is expected: we simulate a more expressive model (NFA) with a more restricted one (DFA)


---

# Subset Construction: Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Walk through the construction on $L_2$ — and notice most of the $2^4$ subsets are unreachable.

</div>

Convert the NFA for $L_2$ (penultimate symbol is $0$) to a DFA


**NFA:** 4 states $\{q_0, q_1, q_2, q_3\}$ — self-loop at $q_0$, nondeterministic branch on $0$

**DFA via subset construction:** States are subsets of $\{q_0, q_1, q_2, q_3\}$

Potentially $2^4 = 16$ states

**Observation:** Many states are **unreachable** from the initial state $\{q_0\}$

**Optimization:** Only generate states reachable from $\{q_0\}$ — start from $\{q_0\}$ and explore transitions on demand


---

# Exponential Blowup is Sometimes Necessary

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The blowup isn't a flaw of the construction — *some* languages genuinely need $2^n$ DFA states.

</div>

**Exercise:** Construct a family of NFAs $N_k$ such that:
- $|Q_{N_k}| = O(k)$ (linear in $k$)
- The smallest equivalent DFA $D_k$ has $|Q_{D_k}| = O(2^k)$ (exponential!)


The language $L_n$ (the $n$-th symbol from the end is $1$) provides such a family:
- NFA: $n + 1$ states
- Any DFA: at least $2^n$ states


**Takeaway:** The exponential blowup in the subset construction is not an artifact of the construction — it is sometimes **unavoidable**


---

# DFA $\Leftrightarrow$ NFA Equivalence

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Nondeterminism gives convenience, not power: same class of languages, dramatically smaller machines.

</div>

**Corollary:** A language is regular
- $\iff$ it is recognized by some DFA
- $\iff$ it is recognized by some NFA
- $\iff$ it is recognized by some $\varepsilon$-NFA


**Implications:**

Nondeterminism **does not increase** the expressive power of finite automata — DFAs and NFAs recognize exactly the same class of languages

But NFAs can be **exponentially more compact** than equivalent DFAs


**Exercise:** Finish the proof that regular languages are closed under concatenation and Kleene star (these are easier to show with NFAs than DFAs)


---

# Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Six problems on lower bounds, $\varepsilon$-padding, and using NFAs to prove closure properties.

</div>

1. How many states does any DFA for $L_n$ require? Prove your answer

2. Explain why, when padding a string with $\varepsilon$'s, we never need a contiguous stretch longer than the number of states

3. Modify the subset construction so that only states reachable from the initial state are generated

4. Construct a family of NFAs $N_k$ where $|Q_{N_k}| = O(k)$ but the equivalent DFA has $O(2^k)$ states

5. Use NFAs to prove that regular languages are closed under concatenation

6. Use NFAs to prove that regular languages are closed under Kleene star

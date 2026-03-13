---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.5: Turing Machines & 9.5.1: Nondeterministic TMs
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Turing Machines and Nondeterministic TMs
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

# Turing Machines

Sections 9.5 & 9.5.1 - Computational Foundations

---

# Overview

The Turing machine is the most general model of computation

<v-clicks>

**Key concepts:**
1. **TM definition** — finite control with an infinite tape
2. **Configurations** — snapshots of the computation
3. **Language of a TM** — the set of accepted strings
4. **RE and recursive languages** — two fundamental classes
5. **Robustness** — variants of TMs are equivalent
6. **Nondeterministic TMs** — multiple possible moves
7. **NTM = TM** — nondeterminism does not add power

</v-clicks>

---
layout: section
---

# Turing Machine Definition

Finite control and an infinite tape

---

# The Turing Machine

A **Turing machine** has a finite control and an **infinite tape**

<v-click>

**Initial setup:**
- Input $w = w_1 w_2 \ldots w_n$ is placed on the tape
- Head is positioned on the first symbol $w_1$
- State is $q_0$
- All other squares contain blanks ($\square$)

$$
\begin{array}{|c|c|c|c|c|c|c|c|c}
\hline
w_1 & w_2 & w_3 & \ldots & w_n & \square & \square & \square & \ldots \\
\hline
\end{array}
$$

</v-click>

---

# Formal Definition

A **Turing machine** is a 7-tuple $(Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$

<v-clicks>

- **$Q$** — Finite set of **states**
- **$\Sigma$** — Finite **input alphabet** ($\square \notin \Sigma$)
- **$\Gamma$** — Finite **tape alphabet** ($\Sigma \cup \{\square\} \subseteq \Gamma$)
- **$\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\}$** — **Transition function**
- **$q_0 \in Q$** — **Start state**
- **$q_{\text{accept}} \in Q$** — **Accepting state**
- **$q_{\text{reject}} \in Q$** — **Rejecting state** ($q_{\text{reject}} \neq q_{\text{accept}}$)

</v-clicks>

<v-click>

**Transition:** $\delta(q, X) = (p, Y, D)$ means: in state $q$ reading $X$, write $Y$, move direction $D$, enter state $p$

</v-click>

---

# Configurations

A **configuration** captures the entire state of a TM at one moment

<v-clicks>

A configuration is a string $upv$ where:
- $u, v \in \Gamma^*$ and $p \in Q$
- The state is $p$
- The head is scanning the first symbol of $v$
- The tape contains only blanks following the last symbol of $v$

**Initial configuration:** $q_0 w$ where $w$ is the input

</v-clicks>

---

# Yield Relation

Configuration $C_1$ **yields** configuration $C_2$ (written $C_1 \rightarrow C_2$) if one step of $M$ transforms $C_1$ into $C_2$

<v-clicks>

**Left move:** If $\delta(q_i, b) = (q_j, c, L)$, then:
$$uaq_i bv \rightarrow uq_j acv$$

**Right move:** If $\delta(q_i, b) = (q_j, c, R)$, then:
$$uaq_i bv \rightarrow uacq_j v$$

We write $\stackrel{*}{\rightarrow}$ for zero or more steps

</v-clicks>

---

# Acceptance and Language

**Acceptance:** The TM halts when it enters $q_{\text{accept}}$ or $q_{\text{reject}}$

<v-clicks>

- $M$ **accepts** $w$ if $q_0 w \stackrel{*}{\rightarrow} \alpha\, q_{\text{accept}}\, \beta$
- $M$ **rejects** $w$ if $q_0 w \stackrel{*}{\rightarrow} \alpha\, q_{\text{reject}}\, \beta$
- $M$ may also **loop** — never entering $q_{\text{accept}}$ or $q_{\text{reject}}$

**Language of a TM:**
$$L(M) = \{w \in \Sigma^* \mid q_0 w \stackrel{*}{\rightarrow} \alpha\, q_{\text{accept}}\, \beta\}$$

</v-clicks>

<v-click>

**Exercise:** Design a TM $M$ such that $L(M)$ is the language of palindromes

</v-click>

---
layout: section
---

# RE and Recursive Languages

Two fundamental language classes

---

# Recursively Enumerable Languages

Languages accepted by TMs are called **recursively enumerable (RE)**, also known as **recognizable** or **Turing-recognizable**

<v-clicks>

**Definition:** $L$ is RE if there exists a TM $M$ such that:
- $M$ **accepts** (halts in $q_{\text{accept}}$) for all $x \in L$
- $M$ **does not accept** $x \notin L$ (may reject or loop!)

In other words: $L$ is RE iff $L = L(M)$ for some TM $M$

**Key point:** $M$ is not required to halt on all inputs — it may loop forever on strings not in $L$

</v-clicks>

---

# Recursive (Decidable) Languages

A language $L$ is **recursive** (decidable, Turing-decidable) if there exists a TM $M$ such that:

<v-clicks>

- $M$ halts in $q_{\text{accept}}$ for all $x \in L$
- $M$ halts in $q_{\text{reject}}$ for all $x \notin L$

In other words: $L$ is decidable iff $L = L(M)$ for some TM $M$ that **always halts**

</v-clicks>

<v-click>

**The key difference:**

| | RE | Recursive |
|---|---|---|
| $x \in L$ | Accept | Accept |
| $x \notin L$ | Reject **or loop** | Reject (must halt) |

Recursive languages correspond to **algorithmically recognizable** languages

</v-click>

---

# The Language Hierarchy

$$\text{Regular} \subsetneq \text{CFL} \subsetneq \text{Recursive} \subsetneq \text{RE} \subsetneq \text{All languages}$$

<v-clicks>

- **Regular:** Recognized by DFAs (finite memory)
- **CFL:** Recognized by PDAs (stack memory)
- **Recursive:** Decided by TMs that always halt
- **RE:** Accepted by TMs (may not halt)
- **All languages:** Includes non-RE languages

Each inclusion is **strict** — we will prove some of these separations

</v-clicks>

---

# Robustness

**Robustness:** Different variants of TMs are all equivalent

<v-clicks>

**Equivalent variants:**
- Tape infinite in **one direction** only
- **Multiple tapes** (each with its own head)
- **Two-dimensional** tape
- Stay-put option (L, R, or S)

It is straightforward to "translate" between these models — a multi-tape TM can simulate its tapes on a single tape using tracks and markers

**This robustness is evidence that TMs capture the right notion of computation**

</v-clicks>

---
layout: section
---

# Nondeterministic Turing Machines

Section 9.5.1 — Multiple possible moves

---

# Nondeterministic TM (NTM)

A **Nondeterministic TM** is like a normal TM, except the transition function is now a **transition relation**

<v-click>

$$\delta(q, a) = \{(q_1, b_1, D_1), (q_2, b_2, D_2), \ldots, (q_k, b_k, D_k)\}$$

Several possible moves on a given state and symbol!

</v-click>

<v-click>

**Acceptance:** An NTM $N$ accepts $w$ if **there exists** at least one sequence of choices leading to $q_{\text{accept}}$

The computation is a **tree**, not a single path — each node can branch into multiple children

</v-click>

---

# Example: NTM for "Last Symbol is 1"

$N$ decides $L(N) = \{w \in \{0,1\}^* \mid \text{last symbol of } w \text{ is } 1\}$

<v-click>

**Transitions:**

$$\delta(q_0, 0) = \{(q_0, 0, R),\; (q, 0, R)\}$$
$$\delta(q_0, 1) = \{(q_0, 1, R),\; (r, 1, R)\}$$
$$\delta(r, \square) = \{(q_{\text{accept}}, \square, R)\}$$
$$\delta(r, 0/1) = \{(q, 0, R)\}$$

</v-click>

<v-click>

**Idea:** At each step, $N$ nondeterministically guesses "is this the last symbol?" If it guesses yes and the symbol is 1, it checks that the next symbol is $\square$ (end of input) and accepts

State $q$ is a "dead" state — wrong guesses go here and never accept

</v-click>

---

# Computation Tree for NTM on 011

The computation of $N$ on input $011$ forms a **tree**:

<v-click>

```
                    q₀011
                   /      \
              0q₀11       0q11
             /     \        ✗
          01q₀1   01r1
         /    \      \
     011q₀   011r   010q
       ✗       |      ✗
          011□qₐ
           ✓
```

</v-click>

<v-click>

$N$ **accepts** $011$ because there exists a path reaching $q_{\text{accept}}$

It doesn't matter that other branches fail — one accepting path suffices!

</v-click>

---

# NTM = Deterministic TM

**Theorem:** If $N$ is a nondeterministic TM, then there exists a deterministic TM $D$ such that $L(N) = L(D)$

<v-click>

**Proof idea:** $D$ simulates $N$ using **breadth-first search** of the computation tree

</v-click>

<v-click>

$D$ maintains a sequence of configurations on tape 1:

$$
\begin{array}{|c|c|c|c|c|}
\hline
\cdots & \text{config}_1 & \text{config}_2 & \text{config}_3^\star & \cdots \\
\hline
\end{array}
$$

and uses a second tape for scratch work

</v-click>

---

# The BFS Simulation

<v-clicks>

**How $D$ works:**

1. The configuration marked with $\star$ is the **current** one
2. $D$ copies it to the second tape and examines it
3. **If accepting:** $D$ accepts
4. **If not:** and $N$ has $k$ possible moves from this configuration, $D$ appends the $k$ new configurations to the end of tape 1
5. Mark the **next** configuration on the list as current
6. Repeat

</v-clicks>

<v-click>

**Why BFS?** Depth-first search could follow an infinite branch and miss an accepting path. BFS systematically explores all branches level by level

</v-click>

---

# Cost of the Simulation

If the maximum number of choices of $N$ is $m$ (the **degree of nondeterminism**), and $N$ makes $n$ moves before accepting:

<v-click>

$$D \text{ examines } 1 + m + m^2 + m^3 + \cdots + m^n \approx n \cdot m^n \text{ configurations}$$

</v-click>

<v-click>

**Key observations:**

- The simulation is **exponential** in the number of NTM steps
- Nondeterminism does not strengthen the model for **decidability**
- But does it strengthen it for **efficiency**? This is the **P vs NP** question!
- NTMs allow for more convenient machine design

</v-click>

---

# Simulation as a General Technique

The idea of **simulation** is a fundamental thread in computability

<v-clicks>

- One TM can always simulate another
- The "other" TM can be encoded in the states of the simulator
- Or its description can be placed on the tape

**This is not surprising:** TMs capture what we mean by "computer"

**Real-world analogy:** VMware simulating Windows on a Linux machine

**Exercise:** Show how $M_1$ can simulate $M_2$. One idea: use states $(s_{\text{on}}, p)$ and $(s_{\text{off}}, p)$ where some $p$'s are in $Q_{M_2}$ and some correspond to actions of $M_1$

</v-clicks>

---

# Universal Turing Machine

Alan Turing showed the existence of a **Universal Turing Machine (UTM)**

<v-clicks>

A UTM is capable of **simulating any TM** from its description

A UTM is what we mean by a **computer** — capable of running any algorithm

The proof requires care in defining a consistent encoding of TMs and inputs

**Every Computer Scientist should at some point write a UTM in their favorite programming language...**

This exercise really means:
- Designing your own programming language (how you present TM descriptions)
- Designing your own compiler (how your machine interprets those descriptions)

</v-clicks>

---

# Summary

<v-clicks>

- A **Turing machine** is $(Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$ — finite control + infinite tape
- **Configurations** $upv$ capture the full state of a computation
- **RE languages:** accepted by some TM (may not halt on non-members)
- **Recursive languages:** decided by a TM that always halts
- TMs are **robust** — many variants are equivalent
- **Nondeterministic TMs** allow multiple possible moves per configuration
- NTMs accept if **any** computation path reaches $q_{\text{accept}}$
- **NTM = TM** via breadth-first simulation (but exponential slowdown)
- **Universal TMs** can simulate any TM — this is what "computer" means

</v-clicks>

---

# Exercises

1. Design a TM that accepts the language of palindromes over $\{0, 1\}$

2. Explain why a TM with a tape infinite in only one direction is equivalent to a standard TM

3. Give the computation tree for the NTM $N$ (last-symbol-is-1) on input $101$

4. In the BFS simulation of an NTM, why is breadth-first search essential? What goes wrong with depth-first search?

5. Show how one TM $M_1$ can simulate another TM $M_2$

6. Explain the difference between RE and recursive languages, and give an example of a language that is RE but not recursive

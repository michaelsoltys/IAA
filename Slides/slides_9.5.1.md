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

# Turing Machines

Section 9.5.1 — Turing's machine model — the most general definition of "computable" we have, and still the standard 90 years on.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

<!--
Turing introduced this model in his 1936 paper "On Computable Numbers, with an Application to the Entscheidungsproblem." He was 23 and unknown. The paper was a response to Hilbert's 1928 challenge asking for a procedure to decide the truth of arbitrary first-order statements. Turing's answer — no such procedure can exist — required first defining what "procedure" even means, and the machine on the next few slides is his definition. Alonzo Church had published a similar impossibility result using the λ-calculus months earlier, but Turing's formulation is what stuck: it's visibly mechanical, and that's what made the Church–Turing thesis believable.
-->

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The seven concepts we'll need: TM definition, configurations, language, RE vs recursive, robustness, and NTMs.

</div>

The Turing machine is the most general model of computation


**Key concepts:**
1. **TM definition** — finite control with an infinite tape
2. **Configurations** — snapshots of the computation
3. **Language of a TM** — the set of accepted strings
4. **RE and recursive languages** — two fundamental classes
5. **Robustness** — variants of TMs are equivalent
6. **Nondeterministic TMs** — multiple possible moves
7. **NTM = TM** — nondeterminism does not add power


---
layout: section
---

# Turing Machine Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Finite control and an infinite tape — read, write, move left or right, repeat.

</div>

---

# The Turing Machine

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The picture: input on the tape, head on the first cell, blanks everywhere else, control in the start state.

</div>

A **Turing machine** has a finite control and an **infinite tape**


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


---

# Formal Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The 7-tuple — note the *two* halting states, $q_{\text{accept}}$ and $q_{\text{reject}}$, that decide the verdict.

</div>

A **Turing machine** is a 7-tuple $(Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$


- **$Q$** — Finite set of **states**
- **$\Sigma$** — Finite **input alphabet** ($\square \notin \Sigma$)
- **$\Gamma$** — Finite **tape alphabet** ($\Sigma \cup \{\square\} \subseteq \Gamma$)
- **$\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\}$** — **Transition function**
- **$q_0 \in Q$** — **Start state**
- **$q_{\text{accept}} \in Q$** — **Accepting state**
- **$q_{\text{reject}} \in Q$** — **Rejecting state** ($q_{\text{reject}} \neq q_{\text{accept}}$)


**Transition:** $\delta(q, X) = (p, Y, D)$ means: in state $q$ reading $X$, write $Y$, move direction $D$, enter state $p$


<!--
Turing didn't call these "Turing machines" — he called them "a-machines" (automatic machines), to distinguish them from "c-machines" (choice machines, an early form of nondeterminism) and "o-machines" (oracle machines) which he introduced later. The name "Turing machine" was coined by Alonzo Church in his 1937 review of Turing's paper in the Journal of Symbolic Logic.
-->

---

# Configurations

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The string $upv$ that captures everything — tape contents, head position, and current state — in one snapshot.

</div>

A **configuration** captures the entire state of a TM at one moment


A configuration is a string $upv$ where:
- $u, v \in \Gamma^*$ and $p \in Q$
- The state is $p$
- The head is scanning the first symbol of $v$
- The tape contains only blanks following the last symbol of $v$

**Initial configuration:** $q_0 w$ where $w$ is the input


---

# Yield Relation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

How one configuration becomes the next — exactly two cases, depending on whether the head moves $L$ or $R$.

</div>

Configuration $C_1$ **yields** configuration $C_2$ (written $C_1 \rightarrow C_2$) if one step of $M$ transforms $C_1$ into $C_2$


**Left move:** If $\delta(q_i, b) = (q_j, c, L)$, then:
$$uaq_i bv \rightarrow uq_j acv$$

**Right move:** If $\delta(q_i, b) = (q_j, c, R)$, then:
$$uaq_i bv \rightarrow uacq_j v$$

We write $\stackrel{*}{\rightarrow}$ for zero or more steps


---

# Acceptance and Language

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three possible outcomes — accept, reject, or *loop forever* — and the asymmetry that makes TMs different.

</div>

**Acceptance:** The TM halts when it enters $q_{\text{accept}}$ or $q_{\text{reject}}$


- $M$ **accepts** $w$ if $q_0 w \stackrel{*}{\rightarrow} \alpha\, q_{\text{accept}}\, \beta$
- $M$ **rejects** $w$ if $q_0 w \stackrel{*}{\rightarrow} \alpha\, q_{\text{reject}}\, \beta$
- $M$ may also **loop** — never entering $q_{\text{accept}}$ or $q_{\text{reject}}$

**Language of a TM:**
$$L(M) = \{w \in \Sigma^* \mid q_0 w \stackrel{*}{\rightarrow} \alpha\, q_{\text{accept}}\, \beta\}$$


**Exercise:** Design a TM $M$ such that $L(M)$ is the language of palindromes


---
layout: section
---

# RE and Recursive Languages

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two fundamental language classes — the difference is whether the machine is *guaranteed* to halt.

</div>

---

# Recursively Enumerable Languages

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Some TM accepts every $x \in L$ — but on $x \notin L$, the machine is allowed to loop forever.

</div>

Languages accepted by TMs are called **recursively enumerable (RE)**, also known as **recognizable** or **Turing-recognizable**


**Definition:** $L$ is RE if there exists a TM $M$ such that:
- $M$ **accepts** (halts in $q_{\text{accept}}$) for all $x \in L$
- $M$ **does not accept** $x \notin L$ (may reject or loop!)

In other words: $L$ is RE iff $L = L(M)$ for some TM $M$

**Key point:** $M$ is not required to halt on all inputs — it may loop forever on strings not in $L$


---

# Recursive (Decidable) Languages

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A *decider* always halts with a verdict — these are the languages we'd call "algorithmically solvable."

</div>

A language $L$ is **recursive** (decidable, Turing-decidable) if there exists a TM $M$ such that:


- $M$ halts in $q_{\text{accept}}$ for all $x \in L$
- $M$ halts in $q_{\text{reject}}$ for all $x \notin L$

In other words: $L$ is decidable iff $L = L(M)$ for some TM $M$ that **always halts**


**The key difference:**

| | RE | Recursive |
|---|---|---|
| $x \in L$ | Accept | Accept |
| $x \notin L$ | Reject **or loop** | Reject (must halt) |

Recursive languages correspond to **algorithmically recognizable** languages


<!--
The asymmetry between RE and recursive is where incomputability lives. The halting problem — "does M halt on input x?" — is RE (a universal simulator can confirm a YES by observing the halt) but not recursive (you can't safely say NO in finite time, because the simulator might just not have run long enough yet). Post's theorem makes this precise: L is recursive iff both L and its complement are RE. That extra "loop forever" option in the RE definition is not a defect of the definition — it's a feature of the universe of algorithms.
-->

---

# The Language Hierarchy

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The full Chomsky-style ladder, from finite memory all the way up to languages no machine can recognize.

</div>

$$\text{Regular} \subsetneq \text{CFL} \subsetneq \text{Recursive} \subsetneq \text{RE} \subsetneq \text{All languages}$$


- **Regular:** Recognized by DFAs (finite memory)
- **CFL:** Recognized by PDAs (stack memory)
- **Recursive:** Decided by TMs that always halt
- **RE:** Accepted by TMs (may not halt)
- **All languages:** Includes non-RE languages

Each inclusion is **strict** — we will prove some of these separations


---

# Robustness

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Multi-tape, two-dimensional, one-way infinite — every reasonable TM variant computes the same class.

</div>

**Robustness:** Different variants of TMs are all equivalent


**Equivalent variants:**
- Tape infinite in **one direction** only
- **Multiple tapes** (each with its own head)
- **Two-dimensional** tape
- Stay-put option (L, R, or S)

It is straightforward to "translate" between these models — a multi-tape TM can simulate its tapes on a single tape using tracks and markers

**This robustness is evidence that TMs capture the right notion of computation**


<!--
The robustness story is much stronger than just "multi-tape = single-tape." In the 1930s, four entirely different formulations of "computable" were proposed independently: Church's λ-calculus, Gödel/Herbrand recursive functions, Kleene's μ-recursive functions, and Turing machines. Post's tag systems came shortly after, and later additions include register machines and combinatory logic. All have been proved pairwise equivalent. That pile of coincidences is what justifies the Church–Turing thesis — the claim that "effectively computable" has only one extension. No one has since proposed a reasonable physical model that exceeds it.
-->

---
layout: section
---

# Nondeterministic Turing Machines

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

What happens when the transition function is allowed to branch — and why this *doesn't* increase computational power.

</div>

---

# Nondeterministic TM (NTM)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Multiple moves available at each step — accept if *any* path through the computation tree reaches $q_{\text{accept}}$.

</div>

A **Nondeterministic TM** is like a normal TM, except the transition function is now a **transition relation**


$$\delta(q, a) = \{(q_1, b_1, D_1), (q_2, b_2, D_2), \ldots, (q_k, b_k, D_k)\}$$

Several possible moves on a given state and symbol!


**Acceptance:** An NTM $N$ accepts $w$ if **there exists** at least one sequence of choices leading to $q_{\text{accept}}$

The computation is a **tree**, not a single path — each node can branch into multiple children


---

# Example: NTM for "Last Symbol is 1"

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A simple NTM that *guesses* which symbol is the last — wrong guesses go to a dead state.

</div>

$N$ decides $L(N) = \{w \in \{0,1\}^* \mid \text{last symbol of } w \text{ is } 1\}$


**Transitions:**

$$\delta(q_0, 0) = \{(q_0, 0, R),\; (q, 0, R)\}$$
$$\delta(q_0, 1) = \{(q_0, 1, R),\; (r, 1, R)\}$$
$$\delta(r, \square) = \{(q_{\text{accept}}, \square, R)\}$$
$$\delta(r, 0/1) = \{(q, 0, R)\}$$


**Idea:** At each step, $N$ nondeterministically guesses "is this the last symbol?" If it guesses yes and the symbol is 1, it checks that the next symbol is $\square$ (end of input) and accepts

State $q$ is a "dead" state — wrong guesses go here and never accept


---

# Computation Tree for NTM on 011

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The computation branches into a tree — and one accepting leaf is enough for $N$ to accept the input.

</div>

The computation of $N$ on input $011$ forms a **tree**:


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


$N$ **accepts** $011$ because there exists a path reaching $q_{\text{accept}}$

It doesn't matter that other branches fail — one accepting path suffices!


---

# NTM = Deterministic TM

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Nondeterminism adds no computational power — a deterministic TM can simulate any NTM.

</div>

**Theorem:** If $N$ is a nondeterministic TM, then there exists a deterministic TM $D$ such that $L(N) = L(D)$


**Proof idea:** $D$ simulates $N$ using **breadth-first search** of the computation tree


$D$ maintains a sequence of configurations on tape 1:

$$
\begin{array}{|c|c|c|c|c|}
\hline
\cdots & \text{config}_1 & \text{config}_2 & \text{config}_3^\star & \cdots \\
\hline
\end{array}
$$

and uses a second tape for scratch work


---

# The BFS Simulation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$D$ keeps a queue of configurations on tape and explores the computation tree level by level.

</div>

**How $D$ works:**

1. The configuration marked with $\star$ is the **current** one
2. $D$ copies it to the second tape and examines it
3. **If accepting:** $D$ accepts
4. **If not:** and $N$ has $k$ possible moves from this configuration, $D$ appends the $k$ new configurations to the end of tape 1
5. Mark the **next** configuration on the list as current
6. Repeat


**Why BFS?** Depth-first search could follow an infinite branch and miss an accepting path. BFS systematically explores all branches level by level


---

# Cost of the Simulation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The simulation costs roughly $m^n$ — and whether that exponential blow-up is *necessary* is the P vs NP question.

</div>

If the maximum number of choices of $N$ is $m$ (the **degree of nondeterminism**), and $N$ makes $n$ moves before accepting:


$$D \text{ examines } 1 + m + m^2 + m^3 + \cdots + m^n \approx n \cdot m^n \text{ configurations}$$


**Key observations:**

- The simulation is **exponential** in the number of NTM steps
- Nondeterminism does not strengthen the model for **decidability**
- But does it strengthen it for **efficiency**? This is the **P vs NP** question!
- NTMs allow for more convenient machine design


<!--
The question "can nondeterminism save time, not just save description?" is the P vs NP question. Stephen Cook formalized it in his 1971 STOC paper introducing NP-completeness, and Leonid Levin arrived at essentially the same result independently in the USSR around the same time. The Clay Mathematics Institute listed P vs NP among its seven Millennium Problems in 2000, with a $1M prize. Cook's original reduction target was SAT, using a variant of the NTM simulation on the previous slide. Fifty-plus years on, we still don't know whether the exponential in m^n is necessary or can be compressed to a polynomial.
-->

---

# Simulation as a General Technique

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

One TM running another is the deep idea behind universality — and behind every virtual machine you've used.

</div>

The idea of **simulation** is a fundamental thread in computability


- One TM can always simulate another
- The "other" TM can be encoded in the states of the simulator
- Or its description can be placed on the tape

**This is not surprising:** TMs capture what we mean by "computer"

**Real-world analogy:** VMware simulating Windows on a Linux machine

**Exercise:** Show how $M_1$ can simulate $M_2$. One idea: use states $(s_{\text{on}}, p)$ and $(s_{\text{off}}, p)$ where some $p$'s are in $Q_{M_2}$ and some correspond to actions of $M_1$


---

# Universal Turing Machine

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A single TM that, given the description of any other TM, runs it — the theoretical ancestor of every computer.

</div>

Alan Turing showed the existence of a **Universal Turing Machine (UTM)**


A UTM is capable of **simulating any TM** from its description

A UTM is what we mean by a **computer** — capable of running any algorithm

The proof requires care in defining a consistent encoding of TMs and inputs

**Every Computer Scientist should at some point write a UTM in their favorite programming language...**

This exercise really means:
- Designing your own programming language (how you present TM descriptions)
- Designing your own compiler (how your machine interprets those descriptions)


<!--
The UTM is the conceptual ancestor of every stored-program computer. Von Neumann read Turing's 1936 paper at Princeton — Turing was there 1936–38 finishing his PhD under Church — and later cited it as the theoretical foundation of the 1945 EDVAC report, the document that fixed the "program lives in memory alongside the data" architecture that every modern CPU still uses. So the reason your laptop can run an arbitrary program is, quite literally, the same reason a UTM can: a description of the computation is just another string on the tape.
-->

---

# Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Practice problems on TM design, tape variants, NTM computation trees, the BFS simulation, and RE vs recursive.

</div>

1. Design a TM that accepts the language of palindromes over $\{0, 1\}$

2. Explain why a TM with a tape infinite in only one direction is equivalent to a standard TM

3. Give the computation tree for the NTM $N$ (last-symbol-is-1) on input $101$

4. In the BFS simulation of an NTM, why is breadth-first search essential? What goes wrong with depth-first search?

5. Show how one TM $M_1$ can simulate another TM $M_2$

6. Explain the difference between RE and recursive languages, and give an example of a language that is RE but not recursive

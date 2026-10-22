---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.4.2: Pushdown Automata
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Pushdown Automata
mdc: false
---

# Pushdown Automata

Section 9.4.2 — A finite automaton with a stack — the machine model that matches the power of context-free grammars.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The six ideas we'll cover: definition, configurations, two acceptance modes, CFG equivalence, and DPDAs.

</div>

Pushdown automata are the machine model for context-free languages


**Key concepts:**
1. **PDA definition** — an NFA with a stack
2. **Configurations** — tracking state, input, and stack
3. **Acceptance** — by final state or empty stack
4. **Equivalence of CFGs and PDAs**
5. **Deterministic PDAs** — a restricted but important subclass
6. **Prefix property** — relating acceptance modes for DPDAs


---
layout: section
---

# PDA Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

An NFA augmented with a stack — finite control plus an unbounded last-in-first-out memory.

</div>

---

# Pushdown Automaton (PDA)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The 6-tuple: states, input alphabet, stack alphabet, transitions, start state, and accepting states.

</div>

A **Pushdown Automaton** is an NFA with a stack — formally:

$$P = (Q, \Sigma, \Gamma, \delta, q_0, F)$$


- **$Q$** — Finite set of **states**
- **$\Sigma$** — Finite **input alphabet**
- **$\Gamma$** — Finite **stack alphabet** ($\Sigma \subseteq \Gamma$)
- **$\delta(q, a, X) = \{(p_1, \gamma_1), \ldots, (p_n, \gamma_n)\}$** — Transition function
- **$q_0$** — **Initial state**
- **$F$** — **Accepting states**


The PDA pushes and pops symbols on the stack; the stack is assumed to be as large as necessary

---

# Simulation: A PDA for Palindromes

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A step-through demo of the palindrome PDA: input tape, stack, state diagram, and every nondeterministic branch.

</div>

<div class="flex gap-6">
<div class="flex-1">

**What the demo shows:**
1. **Push phase:** in $q_0$, read each symbol and push it
2. **Guess the middle:** move to $q_1$ on $\varepsilon$ (even length) or on the middle symbol (odd length)
3. **Pop and match:** in $q_1$, pop when the input symbol matches the top
4. **Accept:** with $\$$ on top, move to $q_2$; accept if the input is consumed

The PDA accepts $w$ iff some guess of the middle reaches $q_2$

</div>
<div class="flex-1">

**During the demo:**

- Inputs to try: $abba$, $aba$, $abab$
- Right arrow steps, left arrow goes back
- "Explore all branches" lists all $2n+1$ guesses and which accept

</div>
</div>

---

# How the Transition Function Works

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

What $\gamma$ encodes: pop, no change, or replace-and-push — the three things a step can do to the stack.

</div>

$\delta(q, a, X) = \{(p_1, \gamma_1), \ldots, (p_n, \gamma_n)\}$

The PDA is in state $q$, reads $a$ from input, and sees $X$ on top of stack


**What $\gamma$ means:**
- If $\gamma = \varepsilon$: the stack is **popped** (X is removed)
- If $\gamma = X$: the stack is **unchanged**
- If $\gamma = YZ$: $X$ is replaced by $Z$, and $Y$ is pushed on top

**Nondeterminism:** Multiple $(p_i, \gamma_i)$ pairs mean the PDA can choose

**$\varepsilon$-transitions:** $\delta(q, \varepsilon, X)$ allows moves without consuming input


---

# Example: Even Palindromes

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Push the first half, *guess* the midpoint, then pop and match — this is why nondeterminism matters.

</div>

**Exercise:** What is a simple PDA for $\{ww^R \mid w \in \{0,1\}^*\}$?


**Idea:**
1. **Phase 1:** Push each input symbol onto the stack
2. **Guess** the midpoint (nondeterministically)
3. **Phase 2:** Match remaining input against the stack (pop and compare)
4. **Accept** when stack is empty


The PDA nondeterministically guesses where the middle of the string is — this is key! A DFA cannot do this because it has no memory of what it has seen

---
layout: section
---

# Configurations and Acceptance

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Tracking the PDA's computation step by step — and the two equivalent ways it can accept a string.

</div>

---

# Configurations

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A snapshot $(q, w, \gamma)$ — current state, remaining input, and stack contents — and how one step changes it.

</div>

A **configuration** is a tuple $(q, w, \gamma)$:


- $q$ — current **state**
- $w$ — **remaining input**
- $\gamma$ — **contents of the stack**


**Transition:** If $(p, \alpha) \in \delta(q, a, X)$, then:

$$(q, aw, X\beta) \vdash (p, w, \alpha\beta)$$

We write $\vdash^*$ for zero or more steps


**Lemma:** If $(q, x, \alpha) \vdash^* (p, y, \beta)$, then $(q, xw, \alpha\gamma) \vdash^* (p, yw, \beta\gamma)$ <span style="font-size: 0.6em; color: navy;">Lem 9.39, Pg 239, lem:configs</span>

*Extra input and stack content below the action don't interfere with the computation*


---

# Two Modes of Acceptance

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Accept by reaching a final state, or by emptying the stack — for nondeterministic PDAs the two are equivalent.

</div>

Two types of PDAs that accept in different ways: 

**Acceptance by final state:**
$$L(P) = \{w \mid (q_0, w, \$) \vdash^* (q, \varepsilon, \alpha),\; q \in F\}$$


**Acceptance by empty stack:**
$$L(P) = \{w \mid (q_0, w, \$) \vdash^* (q, \varepsilon, \varepsilon)\}$$


**Theorem:** $L$ is accepted by a PDA by final state **iff** it is accepted by a PDA by empty stack <span style="font-size: 0.6em; color: navy;">Lem 9.41, Pg 239, lem:acceptance</span>

**Proof sketch:**
- Final state $\Rightarrow$ empty stack: When $\$$ is popped, enter an accepting state
- Empty stack $\Rightarrow$ final state: When an accepting state is entered, pop all the stack


---
layout: section
---

# Equivalence of CFGs and PDAs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The fundamental connection — generative grammars and stack machines define exactly the same languages.

</div>

---

# CFGs and PDAs Are Equivalent

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A language is context-free *iff* some PDA accepts it — proved by translating each into the other.

</div>

**Theorem:** A language is context-free **iff** it is accepted by some PDA


**Two directions:**
1. **CFG → PDA:** Simulate the grammar with a stack
2. **PDA → CFG:** Encode stack operations as grammar variables


---

# From Grammar to PDA

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The PDA carries the *tail* of a left-sentential form on its stack — variables expand, terminals match.

</div>

**Key idea:** A **left sentential form** is:

$$\underbrace{x}_{\in T^*} \overbrace{A\alpha}^{\text{tail}}$$


- The **tail** appears on the stack
- $x$ is the prefix of the input consumed so far
- Total input is $w = xy$, and hopefully $A\alpha \stackrel{*}{\Rightarrow} y$

**How the PDA operates:**
1. Start with start variable on the stack
2. If a variable $A$ is on top, **guess** a production $A \longrightarrow \beta$ and replace
3. If a terminal is on top, **match** it against the input and pop
4. Accept by empty stack


---

# Example: Palindrome PDA

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The full PDA transition table for the palindrome grammar — guess a production or match a terminal.

</div>

Grammar: $P \longrightarrow \varepsilon \mid 0 \mid 1 \mid 0P0 \mid 1P1$


**PDA transitions:**

$$\delta(q_0, \varepsilon, \$) = \{(q, P\$)\}$$
$$\delta(q, \varepsilon, P) = \{(q, 0P0), (q, 0), (q, \varepsilon), (q, 1P1), (q, 1)\}$$
$$\delta(q, 0, 0) = \delta(q, 1, 1) = \{(q, \varepsilon)\}$$
$$\delta(q, 0, 1) = \delta(q, 1, 0) = \emptyset$$
$$\delta(q, \varepsilon, \$) = (q, \varepsilon)$$


---

# Example: Running the Palindrome PDA

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.4em;">

A first attempt to trace the PDA on $100001$ — and what goes wrong with a bad guess.

</div>

**Derivation:** $P \Rightarrow 1P1 \Rightarrow 10P01 \Rightarrow 100P001 \Rightarrow 100001$

**PDA computation on input $100001$:**

<div class="flex gap-6 text-sm">
<div class="flex-1">

| Step | State | Input left | Stack |
|------|-------|------------|-------|
| 0 | $q_0$ | $100001$ | $\$$ |
| 1 | $q$ | $100001$ | $P\$$ |
| 2 | $q$ | $100001$ | $1P1\$$ |
| 3 | $q$ | $00001$ | $P1\$$ |
| 4 | $q$ | $00001$ | $0P01\$$ |

</div>
<div class="flex-1">

| Step | State | Input left | Stack |
|------|-------|------------|-------|
| 5 | $q$ | $0001$ | $P01\$$ |
| 6 | $q$ | $0001$ | $001\$$ |
| 7 | $q$ | $001$ | $01\$$ |
| 8 | $q$ | $01$ | $1\$$ |
| 9 | $q$ | $1$ | ERROR |

</div>
</div>


Wait — the PDA is nondeterministic! It tries the right guess: at step 6, choose $P \rightarrow \varepsilon$, giving stack $01\$$, and matching succeeds

<style>
table th, table td { padding-top: 0.15rem !important; padding-bottom: 0.15rem !important; }
</style>

---

# Correct Computation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.4em;">

The accepting branch — pick $P \to \varepsilon$ at the right moment and the stack matches the rest of the input.

</div>

**Derivation:** $P \Rightarrow 1P1 \Rightarrow 10P01 \Rightarrow 100P001 \Rightarrow 100001$

<div class="flex gap-6 text-sm">
<div class="flex-1">

| Step | Action | Input left | Stack |
|------|--------|------------|-------|
| 0 | Start | $100001$ | $\$$ |
| 1 | Push $P\$$ | $100001$ | $P\$$ |
| 2 | $P \rightarrow 1P1$ | $100001$ | $1P1\$$ |
| 3 | Match 1 | $00001$ | $P1\$$ |
| 4 | $P \rightarrow 0P0$ | $00001$ | $0P01\$$ |

</div>
<div class="flex-1">

| Step | Action | Input left | Stack |
|------|--------|------------|-------|
| 5 | Match 0 | $0001$ | $P01\$$ |
| 6 | $P \rightarrow 0P0$ | $0001$ | $0P001\$$ |
| 7 | Match 0 | $001$ | $P001\$$ |
| 8 | $P \rightarrow \varepsilon$ | $001$ | $001\$$ |
| 9-12 | Match 0,0,1,$\$$ | $\varepsilon$ | $\varepsilon$ |

</div>
</div>

Accept!

<style>
table th, table td { padding-top: 0.15rem !important; padding-bottom: 0.15rem !important; }
</style>

---

# From PDA to Grammar

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Encode each "net pop one symbol while moving from $p$ to $q$" event as a grammar variable $A_{[pXq]}$.

</div>

**Idea:** "Net popping" of one symbol of the stack, while consuming some input


**Variables:** $A_{[pXq]}$ for $p, q \in Q$, $X \in \Gamma$

**Meaning:** $A_{[pXq]} \stackrel{*}{\Rightarrow} w$ iff $w$ takes PDA from state $p$ to state $q$, and pops $X$ off the stack


**Productions:**

For all $p$: $S \longrightarrow A_{[q_0 \$ p]}$

Whenever $(r, Y_1 Y_2 \ldots Y_k) \in \delta(q, a, X)$:
$$A_{[qXr_k]} \longrightarrow a A_{[rY_1r_1]} A_{[r_1Y_2r_2]} \ldots A_{[r_{k-1}Y_kr_k]}$$
where $a \in \Sigma \cup \{\varepsilon\}$ and $r_1, \ldots, r_k \in Q$ range over all possible states

If $(r, \varepsilon) \in \delta(q, a, X)$: $A_{[qXr]} \longrightarrow a$


---

# Correctness of the Translation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A double induction — on derivation steps one direction, on PDA moves the other — proves the equivalence.

</div>

**Claim:** $A_{[qXp]} \stackrel{*}{\Rightarrow} w \iff (q, w, X) \vdash^* (p, \varepsilon, \varepsilon)$


**Left to right ($\Rightarrow$):** By induction on the number of derivation steps

**Right to left ($\Leftarrow$):** By induction on the number of PDA moves


This establishes that the grammar generates exactly the language accepted by the PDA, completing the equivalence proof

---
layout: section
---

# Deterministic PDAs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A restricted but important subclass — the model behind every real LR/LL parser used in compilers.

</div>

---

# Deterministic PDA (DPDA)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

At most one move available, and no conflict between reading input and taking an $\varepsilon$-transition.

</div>

A PDA is **deterministic** if:


1. $|\delta(q, a, X)| \leq 1$ for all $q, a, X$
2. If $|\delta(q, a, X)| = 1$ for some $a \in \Sigma$, then $|\delta(q, \varepsilon, X)| = 0$

**Condition 2** prevents choosing between reading input and taking an $\varepsilon$-transition


**Theorem:** If $L$ is regular, then $L = L(P)$ for some DPDA $P$

**Proof:** Simply ignore the stack — a DFA is a DPDA!

---

# DPDAs and Acceptance

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

For DPDAs the two modes diverge — empty-stack acceptance fails on languages with the prefix property.

</div>

**Important:** For DPDAs, the two acceptance modes are **not** equivalent!


**Prefix property:** $L$ has the prefix property if there exists $x, y \in L$ such that $y = xz$ for some $z$

**Example:** $\{0\}^*$ has the prefix property (e.g., $0$ and $00$)


**Theorem:** $L$ is accepted by a DPDA by empty stack $\iff$ $L$ is accepted by a DPDA by final state **and** $L$ does not have the prefix property

*Why?* If the stack empties on input $x$, the DPDA can't continue reading $z$ to accept $xz$


---

# DPDAs and Ambiguity

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

DPDA languages have unambiguous grammars — and they sit strictly between regular and full CFL.

</div>

**Theorem:** If $L$ is accepted by a DPDA, then $L$ is **unambiguous**


**Meaning:** There exists an unambiguous CFG for $L$

Since the DPDA has a unique computation path on each input, the corresponding grammar produces a unique parse tree for each string


**The hierarchy:**

$$\text{Regular} \subsetneq \text{DPDA} \subsetneq \text{CFL}$$

- Regular: DFA (no stack)
- DPDA: deterministic stack (e.g., $\{0^n 1^n\}$)
- CFL: nondeterministic stack (e.g., $\{ww^R\}$)

---

# Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Practice problems on PDA design, acceptance modes, the CFG-PDA translation, and prefix-property reasoning.

</div>

1. Design a PDA for $\{ww^R \mid w \in \{0,1\}^*\}$ (accept by empty stack)

2. Design a PDA for $\{a^n b^m \mid n \leq m \leq 2n\}$

3. Convert the palindrome grammar to a PDA and trace the computation on $10101$

4. Show that acceptance by final state and empty stack are equivalent for nondeterministic PDAs

5. Explain why DPDAs accepting by empty stack cannot accept languages with the prefix property

6. Show that $A_{[qXp]} \stackrel{*}{\Rightarrow} w \iff (q, w, X) \vdash^* (p, \varepsilon, \varepsilon)$

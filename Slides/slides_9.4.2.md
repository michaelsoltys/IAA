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

<!--
Pushdown automata were introduced by Marcel-Paul Schützenberger (1961) and independently by Antony Oettinger (1961). Oettinger was studying automatic syntactic analysis of natural language at Harvard and realized that a finite automaton with a stack could parse nested sentence structures that flat finite-state machines could not. The timing was not accidental — Chomsky's context-free grammars (1956) had been adopted for programming language syntax (Algol 60), and there was urgent need for a machine model that could parse them efficiently.
-->

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


<!--
The stack is what separates PDAs from finite automata — it gives the machine unbounded memory, but only in a last-in-first-out discipline. This is exactly the right amount of memory for matching nested structures: parentheses, HTML tags, recursive function calls. Every compiler's parser is, at its core, a pushdown automaton. The call stack in any programming language is literally a pushdown store — function calls push frames, returns pop them. PDAs are not just abstract theory; they are the architecture of every running program.
-->

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


<!--
The even palindrome language $\{ww^R\}$ is the classic example of a language that requires both nondeterminism and a stack. A DPDA cannot recognize it — there is no way to deterministically know when you've reached the midpoint without some marker. The odd palindrome language $\{wcw^R\}$ (with a center marker $c$) is recognizable by a DPDA because the marker tells you exactly when to switch from pushing to popping. This distinction — nondeterminism being essential, not just convenient — is what makes $\{ww^R\}$ a key example in the theory.
-->

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A first attempt to trace the PDA on $100001$ — and what goes wrong with a bad guess.

</div>

**Derivation:** $P \Rightarrow 1P1 \Rightarrow 10P01 \Rightarrow 100P001 \Rightarrow 100001$


**PDA computation on input $100001$:**

| Step | State | Remaining Input | Stack |
|------|-------|----------------|-------|
| 0 | $q_0$ | $100001$ | $\$$ |
| 1 | $q$ | $100001$ | $P\$$ |
| 2 | $q$ | $100001$ | $1P1\$$ |
| 3 | $q$ | $00001$ | $P1\$$ |
| 4 | $q$ | $00001$ | $0P01\$$ |
| 5 | $q$ | $0001$ | $P01\$$ |
| 6 | $q$ | $0001$ | $001\$$ |
| 7 | $q$ | $001$ | $01\$$ |
| 8 | $q$ | $01$ | $1\$$ |
| 9 | $q$ | $1$ | ERROR |


Wait — the PDA is nondeterministic! It tries the right guess: at step 6, choose $P \rightarrow \varepsilon$, giving stack $01\$$, and matching succeeds


---

# Correct Computation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The accepting branch — pick $P \to \varepsilon$ at the right moment and the stack matches the rest of the input.

</div>

**Derivation:** $P \Rightarrow 1P1 \Rightarrow 10P01 \Rightarrow 100P001 \Rightarrow 100001$

| Step | Action | Remaining Input | Stack |
|------|--------|----------------|-------|
| 0 | Start | $100001$ | $\$$ |
| 1 | Push $P\$$ | $100001$ | $P\$$ |
| 2 | $P \rightarrow 1P1$ | $100001$ | $1P1\$$ |
| 3 | Match 1 | $00001$ | $P1\$$ |
| 4 | $P \rightarrow 0P0$ | $00001$ | $0P01\$$ |
| 5 | Match 0 | $0001$ | $P01\$$ |
| 6 | $P \rightarrow 0P0$ | $0001$ | $0P001\$$ |
| 7 | Match 0 | $001$ | $P001\$$ |
| 8 | $P \rightarrow \varepsilon$ | $001$ | $001\$$ |
| 9-12 | Match 0,0,1,$\$$ | $\varepsilon$ | $\varepsilon$ |

Accept!

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


<!--
The CFG-PDA equivalence theorem is one of the most satisfying results in automata theory: it says that the same class of languages (context-free) arises whether you think generatively (grammars producing strings) or computationally (machines accepting strings). This duality mirrors the regular languages, where regular expressions (generative) and finite automata (computational) define the same class. There is no such clean equivalence at higher levels of the Chomsky hierarchy — context-sensitive grammars correspond to linear-bounded automata, but the relationship is less elegant and harder to prove.

The PDA→CFG direction (encoding stack operations as grammar variables $A_{[pXq]}$) produces grammars that are typically enormous — the number of variables is $|Q|^2 \cdot |\Gamma|$. For a PDA with 10 states and 5 stack symbols, that is 500 variables. The construction is important for the proof but never used in practice.
-->

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


<!--
Deterministic PDAs are the workhorses of real parsing. Every LR parser (used by yacc/bison) and LL parser (used by recursive descent compilers) is essentially a DPDA. The languages they recognize — the deterministic context-free languages (DCFLs) — include virtually all programming language syntaxes. The class of DCFLs is closed under complementation (a surprisingly difficult theorem proved by Greibach in 1973), but not under union or intersection. This means that if a DPDA accepts a language $L$, another DPDA accepts $\overline{L}$ — but you cannot always combine two DPDAs with union.
-->

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


<!--
Each inclusion is strict and witnessed by a single language. $\{0^n 1^n\}$ separates DPDA from Regular (a DFA cannot count). $\{ww^R\}$ separates CFL from DPDA (a DPDA cannot guess the midpoint). And $\{0^n 1^n 2^n\}$ separates beyond CFL — no PDA, deterministic or not, can enforce three-way equality.

The inherent ambiguity question is also interesting here. There exist CFLs that are *inherently ambiguous* — every grammar for them is ambiguous. The classic example is $\{a^i b^j c^k \mid i = j \text{ or } j = k\}$. But every DPDA language has an unambiguous grammar, so inherently ambiguous languages are exactly the CFLs that lie strictly above the DPDA level.
-->

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

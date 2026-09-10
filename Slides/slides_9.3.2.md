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

<!--
Michael Rabin and Dana Scott wrote the paper that defined NFAs as a summer job. IBM Yorktown Heights, 1957; both were Alonzo Church's students at Princeton. The paper came out in 1959 in the IBM Journal of Research and Development: "Finite Automata and Their Decision Problems," twelve pages. The 1976 Turing Award citation names that one paper, "which introduced the idea of nondeterministic machines."
-->

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

<!--
For finite automata, nondeterminism is a convenience: same languages, smaller machines. For Turing machines it is the P versus NP question, still open. The Turing Award citation called nondeterministic machines "an enormously valuable concept" because of that later life, not because NFAs accept more than DFAs. They don't.
-->

---

# Example 1: $\varepsilon$-Transitions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Free moves between states — handy for gluing sub-machines together when building NFAs.

</div>

<div class="flex gap-8 items-start">
<div style="text-align: left; flex: 1; min-width: 0;">

An **$\varepsilon$-NFA** extends the NFA with $\varepsilon$-transitions — transitions that consume **no input**:

$$\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to \mathcal{P}(Q)$$

**Example: Decimal numbers** like $3.14$, $51.$, $.14$, $+3.0$, $-0.5$, but **not** a bare decimal point.

$\varepsilon$-transitions are convenient for **designing** NFAs by connecting sub-machines.

</div>
<div style="flex: 0 1 48%;">

<img src="/Figures/floating-point.drawio.svg" class="w-full" />

</div>
</div>

<!--
Ken Thompson compiled regular expressions to ε-NFAs in 1968, then simulated the NFA directly. That is the engine inside the original Unix grep. ε-edges are how you glue "optional sign" to "digits" to "optional fraction" without inventing a new start state for every combination. The decimal machine on the slide is Figure 9.3 in the book: 3.14, 51., and .14 are in; a lone "." is out.
-->

---

# Example 2: $L_n$ — $n$-th Symbol from End

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

<!--
Myhill–Nerode: every pair of distinct length-n strings is distinguishable. If x and y differ in some bit, a short suffix can place that bit in the n-th-from-the-end position, so one continuation is accepted and the other is not. That is 2^n pairwise-inequivalent prefixes, so any DFA needs 2^n states. The NFA just guesses when the window starts and then counts n symbols. grep-style patterns of the form (0|1)*1(0|1)^{n-1} are this language, which is why a naive DFA compiler can explode on them.
-->

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

<!--
The book's fork() analogy is pedagogical, not historical: Unix fork is later. Rabin's own picture was that the machine replicates itself, one copy per choice, and the input is accepted if any copy accepts. Scott was careful to say a nondeterministic automaton is not a probabilistic one. The two are still mixed up: an NFA does not roll dice; it has a set of legal next states, and "exists a path" is the acceptance rule.
-->

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

<!--
Existential acceptance: some path lands in F. The dual machine, which accepts only if every path does, is also equivalent to a DFA: complement the accepting states of the subset-construction DFA. Padding with ε is how the definition absorbs ε-moves into the same "sequence of states" story. The next exercise in the book is why you never need a run of ε's longer than |Q|: pigeonhole on states along a pure-ε path.
-->

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

<!--
ε-closure is ordinary graph reachability on the subgraph of ε-edges. An ε-cycle does not make the set infinite: Q is finite, so the inductive rule just fills a subset of Q. Compiler texts write it ε-closure(T) and move(T,a); the extended transition on the next slide is exactly ε-closure(move(T,a)).
-->

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

<!--
Close, then consume a symbol, then close again. The original grep did this on the fly: at each input character it stored the current set of NFA states, never building the DFA. That is why a pattern can be exponential as a DFA and still run in linear time as an NFA simulation. The subset construction on the next slide is the same idea, frozen into an explicit table.
-->

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

<!--
Rabin and Scott called this the subset construction; it is also the powerset construction. The same 1959 paper proved that two-way finite automata, which can move the head left as well as right, still accept only the regular languages. Nondeterminism, two-way motion, extra tapes: for finite memory, none of those add languages. They add states, or convenience.
-->

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

<!--
Of the 16 subsets, only a handful are reachable. That is typical: the full powerset is the worst case, not the usual case. lex and flex build this DFA, then minimize it. grep often skips the table and keeps the current subset in a bitset. Same construction, different commitment.
-->

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

<!--
L_n is the standard witness, and it is tight: the subset construction on that NFA produces a DFA with exactly 2^n reachable states, one for each possible guess-window. So the construction is optimal infinitely often, not merely "up to 2^n in theory."
-->

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

<!--
Kleene's 1956 paper, "Representation of Events in Nerve Nets and Finite Automata," is the other ancestor. McCulloch and Pitts had nerve nets in 1943; Kleene extracted regular events from them. Rabin and Scott moved the subject off biology and onto tapes. Concatenation and star are the reason ε-NFAs exist as a design tool: put an ε-edge from the accepting states of N1 to the start of N2, or from the accepting states back to the start, and you are done. Doing the same with DFAs is the product construction plus extra bookkeeping.
-->

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

<!--
Problem 1 is Myhill–Nerode on L_n, 2^n classes. Problem 2 is pigeonhole: an ε-path longer than |Q| repeats a state and the cycle can be cut. Problems 5 and 6 are the ε-gluing just mentioned; they are the NFA half of Kleene's theorem, which the next section finishes with regular expressions.
-->

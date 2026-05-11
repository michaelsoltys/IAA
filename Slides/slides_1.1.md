---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 1.1: What is Correctness?
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: What is Correctness?
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

# What is Correctness?

Section 1.1 — What it means for an algorithm to do *exactly* what it's supposed to do, and how we prove it.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

<!--
Why does correctness deserve a chapter of its own? Two reminders from people who knew. Edsger Dijkstra, 1970: "Program testing can be used to show the presence of bugs, but never to show their absence." And Donald Knuth, in a 1977 letter to Peter van Emde Boas: "Beware of bugs in the above code; I have only proved it correct, not tried it." The two quotes together capture the entire game — testing isn't proof, and proof isn't testing, and a serious algorithmicist needs to think about both. A concrete reminder of the cost: in 1994, a math professor named Thomas Nicely noticed that the Pentium chip was producing wrong answers for certain floating-point divisions. Intel knew about the bug and had quietly decided not to recall — until the story broke. The eventual replacement program cost Intel roughly $475 million in 1994 dollars. The bug was in a *division algorithm*, which is exactly where this chapter ends up.
-->

---

# Correctness Framework

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The five pieces — pre, post, termination, partial, full — that together capture *correctness*.

</div>

To show an algorithm is correct, we must show it does what it is supposed to do.


Key concepts:

1. **Precondition** - what must be true *before* the algorithm runs
2. **Postcondition** - what must be true *after* the algorithm runs
3. **Termination** - the algorithm stops after finitely many steps
4. **Partial Correctness** - correctness *without* termination
5. **Full Correctness** - partial correctness *with* termination


<!--
The pre/post-condition framing didn't fall from the sky — it was deliberately invented. Tony Hoare's 1969 paper "An Axiomatic Basis for Computer Programming" introduced the triple {P} S {Q} ("if P holds before S runs, then Q holds after") and built up logical rules for composing them through sequencing, conditionals, and loops. That paper essentially created the field of formal verification and won Hoare the 1980 Turing Award. The same Hoare invented QuickSort a decade earlier, and later gave the famous 2009 talk where he called the null reference his "billion-dollar mistake" — he had introduced it in ALGOL W in 1965 "simply because it was so easy to implement." One person, three formative contributions and one formative regret.
-->

---

# Boolean Notation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The symbol cheat-sheet — $\wedge, \vee, \neg, \rightarrow, \forall, \exists$ — that we'll lean on for the rest of the course.

</div>

- $\wedge$ is "and"
- $\vee$ is "or"
- $\neg$ is "not"
- $\rightarrow$ is Boolean implication: $x \rightarrow y \equiv \neg x \vee y$
- $\leftrightarrow$ is Boolean equivalence: $\alpha \leftrightarrow \beta \equiv (\alpha \rightarrow \beta) \wedge (\beta \rightarrow \alpha)$
- $\forall$ is "for all" (universal quantifier)
- $\exists$ is "there exists" (existential quantifier)
- $\Rightarrow$ abbreviates "implies"


<!--
A bit of history behind the symbols. George Boole — the Boole of "Boolean" — was an entirely self-taught Irish mathematician who never attended university; he was hired as a professor at Queen's College Cork on the strength of his published work. His 1854 book "An Investigation of the Laws of Thought" was an attempt to do for logic what algebra had done for arithmetic, treating "and", "or", and "not" as operations on a two-element algebra. Nearly a century later, in 1937, MIT graduate student Claude Shannon noticed in his master's thesis that Boolean algebra was exactly the right language for analyzing telephone relay circuits — the leap that made digital electronics possible. The quantifier symbols come later: ∃ from Giuseppe Peano in 1897 (an inverted E for "esiste"), and ∀ from Gerhard Gentzen's 1934 work on natural deduction (an inverted A for "alle"). Frege had the *concept* of universal quantification in 1879 but used a peculiar two-dimensional notation that nobody else adopted.
-->

---

# Formal Definition of Partial Correctness

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

*If* the input is well-formed *and* the algorithm halts, *then* the output is correct — termination not promised yet.

</div>

Let $\mathscr{A}$ be an algorithm with:
- $\mathcal{I}_\mathscr{A}$ = set of well-formed inputs
- $\alpha_\mathscr{A}$ = precondition
- $\beta_\mathscr{A}$ = postcondition


**Partial Correctness:**

$$
(\forall I \in \mathcal{I}_\mathscr{A})[(\alpha_\mathscr{A}(I) \wedge \exists O(O = \mathscr{A}(I))) \rightarrow \beta_\mathscr{A}(\mathscr{A}(I))]
$$


In words: For any well-formed input $I$, if $I$ satisfies the precondition and $\mathscr{A}(I)$ produces an output, then this output satisfies the postcondition.


---

# Full Correctness

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Add the missing piece — *the algorithm actually halts* — and now you have a real proof of correctness.

</div>

**Full Correctness** = Partial Correctness + Termination


**Problem 1.1:** How would you modify the partial correctness formula to express full correctness? <span style="font-size: 0.6em; color: navy;">Prb 1.1, Pg 2, prb:full-correctness</span>


---

# Loop Invariants

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The single most powerful tool for proving programs correct — finding the right one is half art, half practice.

</div>

A **loop invariant** is an assertion that stays true after each execution of a loop.


- Coming up with the right invariant is a *creative endeavor*
- We use **induction** to prove invariants hold
- The invariant helps prove: $\alpha_\mathscr{A}(I) \rightarrow \beta_\mathscr{A}(\mathscr{A}(I))$
- Many different invariants may work; the art is selecting them judiciously


<!--
The notion of an invariant as the central tool for reasoning about programs is due to Robert Floyd's 1967 paper "Assigning Meanings to Programs." Floyd's idea was to attach a logical assertion to each edge in a flowchart, then verify each instruction by checking the assertions before and after — turning program-correctness into a finite set of local proofs. Hoare took this and refined it into the cleaner triple-based logic two years later. Floyd received the 1978 Turing Award largely for this work; his citation specifically credits "the invention of fundamental techniques for the construction and analysis of efficient algorithms." Worth knowing: Floyd had no doctorate. He was a self-taught computer scientist who became a full professor at Stanford by sheer force of his work — a useful counterweight to the idea that this subject belongs to people with the right credentials.
-->

---

# Complexity

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

How many *steps* does the algorithm take, in the worst case, as a function of input size?

</div>

Given algorithm $\mathscr{A}$ and input $x$:


- **Running time** = number of steps to terminate on input $x$
- A "step" = assignment, arithmetic operation, or Boolean test
- **Worst-case complexity** $T(n)$ = maximal running time on any input of size $n$


---

# Big O Notation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The four flavors — $O, o, \Omega, \Theta$ — that let us compare growth rates while ignoring constants and small inputs.

</div>

For functions $f, g : \mathbb{N} \rightarrow \mathbb{R}$:


- $g(n) \in O(f(n))$ if $\exists c, n_0$ such that $\forall n \geq n_0$: $g(n) \leq c \cdot f(n)$

- $g(n) \in o(f(n))$ if $\lim_{n \rightarrow \infty} \frac{g(n)}{f(n)} = 0$

- $g(n) \in \Omega(f(n))$ if $\exists c, n_0$ such that $\forall n \geq n_0$: $g(n) \geq c \cdot f(n)$

- $g(n) \in \Theta(f(n))$ if $g(n) \in O(f(n)) \cap \Omega(f(n))$


**Example:** $an^2 + bn + c = \Theta(n^2)$ where $a > 0$


<!--
The "O" notation is older than computer science by a wide margin. Paul Bachmann introduced it in 1894 in *Analytische Zahlentheorie*, and Edmund Landau popularized it through his 1909 number-theory textbook — that's why mathematicians still sometimes call these "Landau symbols." For decades, computer scientists borrowed the notation informally and inconsistently: people would write "O(n)" when they really meant Θ(n), and use Ω to mean two different things depending on whether they'd learned it from number theory or from a CS paper. Donald Knuth had enough and wrote a 1976 SIGACT News article titled "Big Omicron and big Omega and big Theta," explicitly proposing the standard definitions you see on this slide. The article is barely four pages and very readable — Knuth essentially refereed a notation dispute by writing the canonical paper everyone has cited since.
-->

---

# Division Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Our running example: long division by repeated subtraction — small enough to analyze in full, rich enough to teach the method.

</div>

<span style="font-size: 0.6em; color: navy;">Alg 1, Pg 4, alg:p1</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Algorithms/A1_Division.go" style="font-size: 0.6em; color: teal;">[Go implementation]</a>

**Input:** $x \geq 0$, $y > 0$, $x, y \in \mathbb{N}$

**Output:** quotient $q$ and remainder $r$ such that $x = q \cdot y + r$ and $0 \leq r < y$

```text
Division Algorithm:
  q ← 0
  r ← x
  while y ≤ r:
    r ← r - y
    q ← q + 1
  return q, r
```


**Example:** $x = 25$, $y = 3$ → $q = 8$, $r = 1$


<!--
Repeated subtraction is genuinely how the earliest computers did integer division — there was no hardware "divide" instruction on a typical 1950s machine, and even the standard binary long-division algorithm was usually open-coded as a shift-and-subtract loop. Division has always been the troublesome operation: it's the slowest of the four basic arithmetic operations, the one where rounding rules cause the most lawsuits, and the one Intel famously got wrong in the Pentium FDIV bug. The bug, by the way, was in a *table* used by the SRT division algorithm — five entries in a 1066-entry lookup table were missing. The cost to Intel was $475 million in 1994 dollars, a number worth quoting when students complain that proving a humble division algorithm correct is overkill.
-->

---

# Division: Loop Invariant

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The relation $x = qy + r$ holds *every* time we reach the loop guard — and the basis is one line of arithmetic.

</div>

**Loop Invariant:**

$$x = (q \cdot y) + r \quad \text{and} \quad r \geq 0$$


**Basis case** (before line 3):
- $q = 0$, $r = x$
- So $x = (0 \cdot y) + x = x$ ✓
- Since $x \geq 0$ and $r = x$, we have $r \geq 0$ ✓


---

# Division: Induction Step

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

One iteration moves $r \to r-y$ and $q \to q+1$ — and the algebra shows the invariant survives.

</div>

Suppose $x = (q \cdot y) + r$ and $r \geq 0$, and we go through the loop once more.


Let $q', r'$ be the new values after one iteration.

Since we entered the loop: $y \leq r$

Since $r' = r - y$ and $y \leq r$: $r' \geq 0$ ✓

For the main equation:
$$x = (q \cdot y) + r = ((q+1) \cdot y) + (r - y) = (q' \cdot y) + r'$$

So the loop invariant is preserved. ✓


---

# Division: Partial Correctness

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The loop exit condition $r < y$ plus the invariant snaps together to give the postcondition exactly.

</div>

Using the loop invariant to prove postcondition:


- Loop ends when $y > r$, i.e., $r < y$
- Loop invariant gives us: $x = (q \cdot y) + r$ and $r \geq 0$
- Combining: $x = (q \cdot y) + r$ and $0 \leq r < y$

This is exactly our postcondition! ✓


---

# Division: Termination

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The remainders form a strictly decreasing sequence of non-negative integers — they can't go on forever.

</div>

To show termination, we use the **Least Number Principle (LNP)**.


Consider the sequence $r_0, r_1, r_2, \ldots$ where:
- $r_0 = x$
- $r_i$ = value of $r$ after $i$-th iteration
- $r_{i+1} = r_i - y$

Key observations:
1. $r_i \geq 0$ (we only enter loop if $y \leq r$)
2. $r_{i+1} < r_i$ (since $y > 0$)

By LNP, this sequence cannot go on forever → **Algorithm terminates** ✓


<!--
The Least Number Principle looks innocuous — "every non-empty set of natural numbers has a smallest element" — but it's logically equivalent to mathematical induction and to the well-ordering of ℕ. Without one of these three (equivalent) principles, you cannot prove that the natural numbers behave the way you think they do. Generalizing this to *more complex* sequences gets you to well-founded relations and ordinals, and that machinery is what termination provers (in tools like Coq, Isabelle, and Dafny) use under the hood. Translation of this slide into modern practice: when an industrial verifier proves a program terminates, it is usually doing exactly what we just did — finding a "ranking function" mapping program states into a well-ordered set, and showing that each loop iteration strictly decreases the rank.
-->

---

# Division: Complexity

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The loop runs $\lfloor x/y \rfloor$ times — efficient for large $y$, terrible when $y = 1$.

</div>

**Problem 1.3:** What is the running time of the division algorithm? <span style="font-size: 0.6em; color: navy;">Prb 1.3, Pg 5, exr:running-time-div</span>


Assume each of these takes one step:
- Assignments (lines 1, 2)
- Arithmetic operations (lines 4, 5)
- Testing "$\leq$" (line 3)


**Analysis:**
- Number of loop iterations = $\lfloor x/y \rfloor$
- Each iteration: 3 steps (test + 2 operations)
- Total: $O(x/y)$ or $O(q)$

<!--
A quick etymological aside to close the section. The word "algorithm" has nothing to do with Greek "arithmos" (number) — it's a Latinization of the name al-Khwārizmī, a 9th-century Persian mathematician who worked at the House of Wisdom in Baghdad. His treatise on Hindu-Arabic numerals was translated into Latin in the 12th century as "Algoritmi de numero Indorum" ("Al-Khwārizmī on the Hindu numerals"); medieval scholars took "Algoritmi" to be a general word for the procedural arithmetic he was teaching, and the term stuck. The same al-Khwārizmī gave us the word "algebra," from the title of his other book, "Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wa-l-muqābala." So the discipline you're enrolled in is named after one specific person — and Euclid's algorithm, which we'll see in Section 1.2, predates him by roughly 1,100 years, which says something about how long humans have been doing this kind of work.
-->


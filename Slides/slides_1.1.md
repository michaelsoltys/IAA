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


---

# Next: Euclid's Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Preview — a 2,300-year-old algorithm that still powers modern cryptography.

</div>

Coming up in Section 1.2:
- Greatest Common Divisor (GCD)
- Euclid's algorithm (~300 BC)
- Why is it fast? (Important for cryptography!)

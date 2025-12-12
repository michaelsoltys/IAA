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

# What is Correctness?

Section 1.1 - Preliminaries

---

# Correctness Framework

To show an algorithm is correct, we must show it does what it is supposed to do.

<v-clicks>

Key concepts:

1. **Precondition** - what must be true *before* the algorithm runs
2. **Postcondition** - what must be true *after* the algorithm runs
3. **Termination** - the algorithm stops after finitely many steps
4. **Partial Correctness** - correctness *without* termination
5. **Full Correctness** - partial correctness *with* termination

</v-clicks>

---

# Boolean Notation

<v-clicks>

- $\wedge$ is "and"
- $\vee$ is "or"
- $\neg$ is "not"
- $\rightarrow$ is Boolean implication: $x \rightarrow y \equiv \neg x \vee y$
- $\leftrightarrow$ is Boolean equivalence: $\alpha \leftrightarrow \beta \equiv (\alpha \rightarrow \beta) \wedge (\beta \rightarrow \alpha)$
- $\forall$ is "for all" (universal quantifier)
- $\exists$ is "there exists" (existential quantifier)
- $\Rightarrow$ abbreviates "implies"

</v-clicks>

---

# Formal Definition of Partial Correctness

Let $\mathscr{A}$ be an algorithm with:
- $\mathcal{I}_\mathscr{A}$ = set of well-formed inputs
- $\alpha_\mathscr{A}$ = precondition
- $\beta_\mathscr{A}$ = postcondition

<v-click>

**Partial Correctness:**

$$
(\forall I \in \mathcal{I}_\mathscr{A})[(\alpha_\mathscr{A}(I) \wedge \exists O(O = \mathscr{A}(I))) \rightarrow \beta_\mathscr{A}(\mathscr{A}(I))]
$$

</v-click>

<v-click>

In words: For any well-formed input $I$, if $I$ satisfies the precondition and $\mathscr{A}(I)$ produces an output, then this output satisfies the postcondition.

</v-click>

---

# Full Correctness

**Full Correctness** = Partial Correctness + Termination

<v-click>

**Problem 1.1:** How would you modify the partial correctness formula to express full correctness?

</v-click>

---

# Loop Invariants

A **loop invariant** is an assertion that stays true after each execution of a loop.

<v-clicks>

- Coming up with the right invariant is a *creative endeavor*
- We use **induction** to prove invariants hold
- The invariant helps prove: $\alpha_\mathscr{A}(I) \rightarrow \beta_\mathscr{A}(\mathscr{A}(I))$
- Many different invariants may work; the art is selecting them judiciously

</v-clicks>

---

# Complexity

Given algorithm $\mathscr{A}$ and input $x$:

<v-clicks>

- **Running time** = number of steps to terminate on input $x$
- A "step" = assignment, arithmetic operation, or Boolean test
- **Worst-case complexity** $T(n)$ = maximal running time on any input of size $n$

</v-clicks>

---

# Big O Notation

For functions $f, g : \mathbb{N} \rightarrow \mathbb{R}$:

<v-clicks>

- $g(n) \in O(f(n))$ if $\exists c, n_0$ such that $\forall n \geq n_0$: $g(n) \leq c \cdot f(n)$

- $g(n) \in o(f(n))$ if $\lim_{n \rightarrow \infty} \frac{g(n)}{f(n)} = 0$

- $g(n) \in \Omega(f(n))$ if $\exists c, n_0$ such that $\forall n \geq n_0$: $g(n) \geq c \cdot f(n)$

- $g(n) \in \Theta(f(n))$ if $g(n) \in O(f(n)) \cap \Omega(f(n))$

</v-clicks>

<v-click>

**Example:** $an^2 + bn + c = \Theta(n^2)$ where $a > 0$

</v-click>

---

# Division Algorithm

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

<v-click>

**Example:** $x = 25$, $y = 3$ → $q = 8$, $r = 1$

</v-click>

---

# Division: Loop Invariant

**Loop Invariant:**

$$x = (q \cdot y) + r \quad \text{and} \quad r \geq 0$$

<v-click>

**Basis case** (before line 3):
- $q = 0$, $r = x$
- So $x = (0 \cdot y) + x = x$ ✓
- Since $x \geq 0$ and $r = x$, we have $r \geq 0$ ✓

</v-click>

---

# Division: Induction Step

Suppose $x = (q \cdot y) + r$ and $r \geq 0$, and we go through the loop once more.

<v-clicks>

Let $q', r'$ be the new values after one iteration.

Since we entered the loop: $y \leq r$

Since $r' = r - y$ and $y \leq r$: $r' \geq 0$ ✓

For the main equation:
$$x = (q \cdot y) + r = ((q+1) \cdot y) + (r - y) = (q' \cdot y) + r'$$

So the loop invariant is preserved. ✓

</v-clicks>

---

# Division: Partial Correctness

Using the loop invariant to prove postcondition:

<v-clicks>

- Loop ends when $y > r$, i.e., $r < y$
- Loop invariant gives us: $x = (q \cdot y) + r$ and $r \geq 0$
- Combining: $x = (q \cdot y) + r$ and $0 \leq r < y$

This is exactly our postcondition! ✓

</v-clicks>

---

# Division: Termination

To show termination, we use the **Least Number Principle (LNP)**.

<v-clicks>

Consider the sequence $r_0, r_1, r_2, \ldots$ where:
- $r_0 = x$
- $r_i$ = value of $r$ after $i$-th iteration
- $r_{i+1} = r_i - y$

Key observations:
1. $r_i \geq 0$ (we only enter loop if $y \leq r$)
2. $r_{i+1} < r_i$ (since $y > 0$)

By LNP, this sequence cannot go on forever → **Algorithm terminates** ✓

</v-clicks>

---

# Division: Complexity

**Problem 1.3:** What is the running time of the division algorithm?

<v-click>

Assume each of these takes one step:
- Assignments (lines 1, 2)
- Arithmetic operations (lines 4, 5)
- Testing "$\leq$" (line 3)

</v-click>

<v-click>

**Analysis:**
- Number of loop iterations = $\lfloor x/y \rfloor$
- Each iteration: 3 steps (test + 2 operations)
- Total: $O(x/y)$ or $O(q)$

</v-click>

---

# Summary

<v-clicks>

- **Correctness** connects a problem with an algorithm that solves it
- **Hoare's Logic** provides the framework: precondition, postcondition, invariant
- **Loop invariants** are proven by induction
- **Partial correctness** = postcondition follows from precondition (if algorithm terminates)
- **Full correctness** = partial correctness + termination
- **Big O notation** gives asymptotic bounds on complexity
- **Division algorithm** demonstrates all these concepts

</v-clicks>

---

# Key Questions

<v-clicks>

1. **Problem 1.1:** Modify the partial correctness formula for full correctness

2. **Problem 1.3:** Analyze the running time of the division algorithm

3. **Problem 1.4:** What if the precondition changes to allow $x, y \in \mathbb{Z}$?

4. **Problem 1.5:** Write a program that outputs intermediate values of $q$ and $r$

</v-clicks>

---

# Next: Euclid's Algorithm

Coming up in Section 1.2:
- Greatest Common Divisor (GCD)
- Euclid's algorithm (~300 BC)
- Why is it fast? (Important for cryptography!)

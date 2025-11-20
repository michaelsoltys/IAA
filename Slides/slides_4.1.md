---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 4.1: Longest Monotone Subsequence
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Longest Monotone Subsequence Problem
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

# Longest Monotone Subsequence

Section 4.1 - Dynamic Programming

---

# Problem Definition

**Input:** $d, a_1, a_2, \ldots, a_d \in \mathbb{N}$

**Output:** $L =$ length of the longest monotone non-decreasing subsequence

---

# What is a Subsequence?

A subsequence **need not be consecutive**

For $a_{i_1}, a_{i_2}, \ldots, a_{i_k}$ to be a monotone subsequence:

<v-clicks>

- **Indices are increasing:** $1 \leq i_1 < i_2 < \ldots < i_k \leq d$

- **Values are non-decreasing:** $a_{i_1} \leq a_{i_2} \leq \ldots \leq a_{i_k}$

</v-clicks>

---

# Example

Consider the sequence: $\{4, 6, 5, 9, 1\}$

<v-clicks>

Some monotone subsequences:
- $\{4, 6, 9\}$ - length 3 ✓
- $\{4, 5, 9\}$ - length 3 ✓
- $\{4, 6\}$ - length 2
- $\{1\}$ - length 1

The **longest monotone subsequence (LMS)** has length **3**

</v-clicks>

---

# Dynamic Programming Approach

## Step 1: Define Subproblems

Let $R(j) =$ length of the longest monotone subsequence **that ends at** $a_j$

<v-click>

The final answer is:

$$L = \max_{1 \leq j \leq d} R(j)$$

</v-click>

---

# Step 2: Find the Recurrence

**Base case:** $R(1) = 1$

**Recursive case** for $j > 1$:

$$
R(j) = \begin{cases}
1 & \text{if } a_i > a_j \text{ for all } 1 \leq i < j \\
1 + \max_{1 \leq i < j} \{R(i) \mid a_i \leq a_j\} & \text{otherwise}
\end{cases}
$$

<v-click>

**Idea:** Either $a_j$ starts a new subsequence, or it extends a previous one

</v-click>

---

# Step 3: Write the Algorithm

```text
LMS Algorithm:
  R(1) ← 1
  for j = 2 to d:
    max ← 0
    for i = 1 to j-1:
      if R(i) > max and aᵢ ≤ aⱼ:
        max ← R(i)
    R(j) ← max + 1
```

<v-click>

**Time complexity:** $O(d^2)$

**Space complexity:** $O(d)$

</v-click>

---

# Example Walkthrough

Sequence: $\{4, 6, 5, 9, 1\}$

| Index $j$ | $a_j$ | $R(j)$ | Explanation |
|-----------|-------|--------|-------------|
| 1 | 4 | 1 | Base case |
| 2 | 6 | 2 | Extends from $a_1$: 4 ≤ 6 |
| 3 | 5 | 2 | Extends from $a_1$: 4 ≤ 5 |
| 4 | 9 | 3 | Extends from $a_2$ or $a_3$ |
| 5 | 1 | 1 | Cannot extend any previous |

<v-click>

**Result:** $L = \max\{1, 2, 2, 3, 1\} = 3$

</v-click>

---

# Key Questions

<v-clicks>

1. **Backtracking:** Once we have computed array $R$, how can we build an actual subsequence of length $L$?

2. **Correctness:** What are appropriate pre/post-conditions? How do we prove correctness with a loop invariant?

3. **Variant:** What if consecutive elements can differ by at most $s$?
   - Example: For $s=1$ and sequence $\{7, 6, 1, 4, 7, 8, 20\}$
   - Answer: $\{7, 6, 7, 8\}$ with length 4

</v-clicks>

---

# Summary

<v-clicks>

- **Problem:** Find longest non-decreasing subsequence
- **Approach:** Dynamic programming with subproblem $R(j)$
- **Recurrence:** Build from previous valid positions
- **Complexity:** $O(d^2)$ time, $O(d)$ space
- **Key insight:** Optimal substructure - LMS ending at $j$ extends LMS from earlier positions

</v-clicks>

---

# Next Steps

- Practice implementing the algorithm
- Work on the exercises (backtracking, correctness proof)
- Consider the variant with step constraint
- Next section: All Pairs Shortest Path (Floyd's Algorithm)

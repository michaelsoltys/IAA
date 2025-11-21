---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 4.3: Simple Knapsack Problem
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Simple Knapsack Problem
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

# Simple Knapsack Problem

Section 4.3 - Dynamic Programming

---

# The Problem

**Input:** Weights $w_1, w_2, \ldots, w_d, C \in \mathbb{N}$
- $w_i$ = weight of object $i$
- $C$ = capacity of the knapsack

**Output:** $M = \max_{j \leq C}\{j \mid R(d,j) = \text{true}\}$

Find the maximum total weight that fits in the knapsack.

<v-click>

**Key Note:** This is an $\NP$-hard problem, so we cannot expect a polynomial-time solution in general.

</v-click>

---

# Why Dynamic Programming Works

<v-clicks>

- We want to fill a knapsack to capacity $C$
- We must decide: include each object or not?
- Checking all $2^d$ subsets is intractable for large $d$
- But we can reuse computations for intermediate capacities

</v-clicks>

---

# Subproblem Definition

Define a Boolean array $R(i,j)$ for $0 \leq i \leq d$ and $0 \leq j \leq C$:

$$R(i,j) = \begin{cases}
\text{true} & \text{if } \exists S \subseteq [i] \text{ such that } K(S) = j \\
\text{false} & \text{otherwise}
\end{cases}$$

where $K(S) = \sum_{i \in S} w_i$

<v-click>

**Intuition:** Can we construct weight $j$ using only the first $i$ objects?

</v-click>

---

# Base Cases

Initialize the array:

<v-clicks>

- $R(0, j) = \text{false}$ for $j = 1, 2, \ldots, C$
  - Cannot make any positive weight with zero objects

- $R(i, 0) = \text{true}$ for $i = 0, 1, \ldots, d$
  - Can always make weight 0 (select nothing)

</v-clicks>

---

# The Recurrence Relation

For $i, j > 0$:

$$R(i,j) = \text{true} \iff R(i-1,j) = \text{true} \vee (j \geq w_i \wedge R(i-1,j-w_i) = \text{true})$$

<v-clicks>

**Two cases:**

1. **Don't include object $i$:** If we can make $j$ without object $i$, then $R(i,j) = \text{true}$
   - This is $R(i-1,j) = \text{true}$

2. **Include object $i$:** If we can make $j - w_i$ with the first $i-1$ objects, then we can make $j$ with object $i$
   - This is $R(i-1,j-w_i) = \text{true}$

</v-clicks>

---

# Example Walkthrough

**Input:** Weights $\{3, 4, 5\}$ with capacity $C = 10$

| $i \backslash j$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | T | F | F | F | F | F | F | F | F | F | F |
| 1 ($w_1=3$) | T | F | F | **T** | F | F | F | F | F | F | F |
| 2 ($w_2=4$) | T | F | F | T | **T** | F | F | **T** | F | F | F |
| 3 ($w_3=5$) | T | F | F | T | T | **T** | F | T | **T** | **T** | **T** |

<v-click>

**Answer:** $M = 10$ (we can fit all objects: $3+4+5=12 > 10$, so max is $5+5=10$? No, $3+4+5=12$, but capacity is 10, so $5+4=9$ or $5+3=8$ or $4+3=7$. Actually $3+4=7, 5+4=9, 5+3=8, 5+5$ invalid. Max is 9.)

</v-click>

---

# The Algorithm: Space-Saving Trick

Instead of storing a $d \times C$ table, use a 1D array $S(j)$ and update it in **decreasing** order of $j$:

```text
SKS Algorithm:
  S(0) ← true
  for j = 1 to C:
    S(j) ← false
  for i = 1 to d:
    for j = C down to 1:  // DECREASING!
      if j ≥ wᵢ and S(j - wᵢ) = true:
        S(j) ← true
```

<v-clicks>

- After iteration $i$, $S(j) = R(i,j)$
- We iterate $j$ **backwards** to avoid using updated values from the same iteration
- This overwrites $R(i-1,j)$ with $R(i,j)$ in place

</v-clicks>

---

# Why Decreasing Order Matters

<v-clicks>

**Problem with increasing order:**
```
S = [T, F, F, F, ...]  (initially, only S(0) = true)
When processing w₁ = 3:
- j = 1: S(1) = S(1-3)? Invalid
- j = 2: S(2) = S(2-3)? Invalid
- j = 3: S(3) = S(0) = T  ← Mark S(3) = T
- j = 4: S(4) = S(1) = T  ← WRONG! S(1) was updated
```

**Why decreasing order works:**
```
j = C, C-1, ..., 1
We use S(j - wᵢ), which is always to the left
Since j decreases, j - wᵢ hasn't been updated yet in this iteration
```

</v-clicks>

---

# Time and Space Complexity

<v-clicks>

- **Time Complexity:** $O(d \cdot C)$
  - Outer loop: $d$ iterations
  - Inner loop: $C$ iterations per object

- **Space Complexity:** $O(C)$
  - Only store one 1D array instead of $d \times C$ table

</v-clicks>

---

# The Catch: What About the Input Size?

<v-clicks>

The input is given in **binary**:
- Encoding $C$ in binary requires only $\log C$ bits
- But our algorithm takes $O(d \cdot C)$ time
- This means time is **exponential** in the input size!

$$C = 2^{\log C} \text{ (exponential in bits needed)}$$

**Conclusion:**
- If $C$ is polynomial in $d$, then $O(d \cdot C)$ is polynomial in input size
- Otherwise, this is called a **pseudo-polynomial** algorithm

</v-clicks>

---

# Approximation Algorithms

Since SKS is $\NP$-hard, we cannot solve it optimally in general.

**Compromise:** Design an algorithm that:
- Runs in polynomial time
- Provides a solution close to optimal (with guarantees)

<v-click>

**Example:** A greedy algorithm might give $M'$ where $M' > \frac{1}{2}C$ when optimal $M = $ something smaller.

</v-click>

---

# Key Questions and Exercises

<v-clicks>

1. **Space-saving trick:** Why doesn't overwriting cause problems when we iterate in decreasing order?

2. **Formal correctness:** Prove that $S(j) = R(i,j)$ after the $i$-th iteration using induction.

3. **Reconstruction:** How do we build the actual subset of objects that achieves weight $M$?

4. **Greedy comparison:** What is the "obvious" greedy solution, and how does it compare to the DP solution?

</v-clicks>

---

# Summary

<v-clicks>

- **Problem:** Fill a knapsack to maximize weight (NP-hard)
- **Approach:** Dynamic programming with $R(i,j)$ table
- **Recurrence:** Choose to include/exclude each object
- **Optimization:** Use 1D array with backward iteration (space-saving trick)
- **Complexity:** $O(d \cdot C)$ time, $O(C)$ space (pseudo-polynomial)
- **Key insight:** Optimal substructure - best solution for capacity $j$ builds on solutions for smaller capacities

</v-clicks>

---

# Next Steps

- Practice implementing the algorithm
- Work on exercises: reconstruction, formal correctness, greedy comparison
- Consider variants: 0-1 knapsack vs. unbounded knapsack
- Learn about approximation algorithms for NP-hard problems

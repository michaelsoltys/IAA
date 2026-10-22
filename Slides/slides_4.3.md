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

# Simple Knapsack Problem

Section 4.3 — An NP-hard packing problem with a clean dynamic-programming solution.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# The Problem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Pack as much weight as possible without exceeding the knapsack's capacity.

</div>

**Input:** Weights $w_1, w_2, \ldots, w_d, C \in \mathbb{N}$
- $w_i$ = weight of object $i$
- $C$ = capacity of the knapsack

**Output:** $M = \max_{j \leq C}\{j \mid R(d,j) = \text{true}\}$

Find the maximum total weight that fits in the knapsack.


**Key Note:** This is an $\textbf{NP}$-hard problem, so we cannot expect a polynomial-time solution in general.


---

# Why Dynamic Programming Works

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Brute force tries $2^d$ subsets — DP reuses partial answers across capacities.

</div>

- We want to fill a knapsack to capacity $C$
- We must decide: include each object or not?
- Checking all $2^d$ subsets is intractable for large $d$
- But we can reuse computations for intermediate capacities


---

# Subproblem Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$R(i,j)$ asks: can we hit exactly weight $j$ using only the first $i$ objects?

</div>

Define a Boolean array $R(i,j)$ for $0 \leq i \leq d$ and $0 \leq j \leq C$:

$$
R(i,j) = \begin{cases}
\text{T} & \text{if } \exists S \subseteq [i] \text{ such that } K(S) = j \\
\text{F} & \text{otherwise}
\end{cases}
$$

where $K(S) = \sum_{i \in S} w_i$


**Intuition:** Can we construct weight $j$ using only the first $i$ objects?


---

# Base Cases

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Zero objects can only make zero weight; weight zero is always reachable.

</div>

Initialize the array:


- $R(0, j) = \text{F}$ for $j = 1, 2, \ldots, C$
  - Cannot make any positive weight with zero objects

- $R(i, 0) = \text{T}$ for $i = 0, 1, \ldots, d$
  - Can always make weight 0 (select nothing)


---

# The Recurrence Relation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Each new object: include it or skip it — and OR the two outcomes.

</div>

For $i, j > 0$:

$$R(i,j) = \text{T} \iff R(i-1,j) = \text{T} \vee (j \geq w_i \wedge R(i-1,j-w_i) = \text{T})$$


**Two cases:**

1. **Don't include object $i$:** If we can make $j$ without object $i$, then $R(i,j) = \text{true}$
   - This is $R(i-1,j) = \text{true}$

2. **Include object $i$:** If we can make $j - w_i$ with the first $i-1$ objects, then we can make $j$ with object $i$
   - This is $R(i-1,j-w_i) = \text{true}$


---

# Example Walkthrough

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Trace the $R(i,j)$ table on a small instance to see the recurrence in action.

</div>

**Input:** Weights $\{3, 4, 5\}$ with capacity $C = 10$

| $i \backslash j$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | T | F | F | F | F | F | F | F | F | F | F |
| 1 ($w_1=3$) | T | F | F | **T** | F | F | F | F | F | F | F |
| 2 ($w_2=4$) | T | F | F | T | **T** | F | F | **T** | F | F | F |
| 3 ($w_3=5$) | T | F | F | T | T | **T** | F | T | **T** | **T** | F |


---

# The Algorithm: Space-Saving Trick

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Collapse the $d \times C$ table to a single 1D array by iterating capacity in reverse.

</div>

<span style="font-size: 0.6em; color: navy;">Alg 23, Pg 81, alg:sks</span>

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


- After iteration $i$, $S(j) = R(i,j)$
- We iterate $j$ **backwards** to avoid using updated values from the same iteration
- This overwrites $R(i-1,j)$ with $R(i,j)$ in place


---

# Why Decreasing Order Matters

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Going backwards keeps $S(j-w_i)$ untouched this round — preventing using object $i$ twice.

</div>

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


---

# Time and Space Complexity

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$O(d \cdot C)$ time and $O(C)$ space — but read on for the catch about $C$.

</div>

- **Time Complexity:** $O(d \cdot C)$
  - Outer loop: $d$ iterations
  - Inner loop: $C$ iterations per object

- **Space Complexity:** $O(C)$
  - Only store one 1D array instead of $d \times C$ table


---

# The Catch: What About the Input Size?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Pseudo-polynomial: efficient when $C$ is small, exponential when $C$ is encoded compactly.

</div>

The input is given in **binary**:
- Encoding $C$ in binary requires only $\log C$ bits
- But our algorithm takes $O(d \cdot C)$ time
- This means time is **exponential** in the input size!

$$C = 2^{\log C} \text{ (exponential in bits needed)}$$

**Conclusion:**
- If $C$ is polynomial in $d$, then $O(d \cdot C)$ is polynomial in input size
- Otherwise, this is called a **pseudo-polynomial** algorithm

---

# Recent News: Near-Linear Subset Sum (Claimed)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A claimed algorithm essentially optimal in the largest number $N$. Not yet verified.

</div>

- Chen, Mao, and Zhang (Zhejiang University) claim Subset Sum in $O(N^{1+\varepsilon})$ time for any $\varepsilon > 0$
- This is essentially optimal in the largest number $N$
- The authors supplied the plan; GPT Astra Ultra wrote out the 105-page proof
- The result still needs independent verification

<span style="font-size: 0.6em; color: navy;">Source: arXiv 2610.12953; <a href="https://postcutoff.com/e/2026-10-09-subset-sum-near-linear-time-gpt-astra-ultra/">postcutoff.com/e/2026-10-09-subset-sum-near-linear-time-gpt-astra-ultra/</a></span>


---

# Approximation Algorithms

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Trade exact optimality for guaranteed polynomial time and bounded error.

</div>

Since SKS is $\textbf{NP}$-hard, we cannot solve it optimally in general.

**Compromise:** Design an algorithm that:
- Runs in polynomial time
- Provides a solution close to optimal (with guarantees)


**Example:** A greedy algorithm might give $M'$ where $M' > \frac{1}{2}C$ when optimal $M = $ something smaller.

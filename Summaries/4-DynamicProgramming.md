# Chapter 4: Dynamic Programming

## Overview

> "Those who cannot remember the past are condemned to repeat it." — George Santayana

Dynamic programming is an algorithmic technique closely related to divide-and-conquer, but while divide-and-conquer works "top down" (recursively), dynamic programming works "bottom up." The approach creates an array of simpler subproblems and computes the solution to a complex problem by using solutions to easier subproblems stored in the array.

## General Framework

**Three Steps for Dynamic Programming Solutions:**
1. **Define a class of subproblems** (often as an array)
2. **Give a recurrence** based on solving each subproblem in terms of simpler subproblems
3. **Give an algorithm** for computing the recurrence

**Goal:** Typically to maximize profit or minimize cost.

## Problems and Algorithms

### 1. Longest Monotone Subsequence (LMS)

**Problem:**
- **Input:** d, a₁, a₂, ..., aₐ ∈ ℕ
- **Output:** L = length of longest monotone non-decreasing subsequence

A subsequence aᵢ₁, aᵢ₂, ..., aᵢₖ is monotone if:
- 1 ≤ i₁ < i₂ < ... < iₖ ≤ d
- aᵢ₁ ≤ aᵢ₂ ≤ ... ≤ aᵢₖ

**Example:** LMS of {4,6,5,9,1} is 3

**Solution:**
1. **Subproblems:** R(j) = length of longest monotone subsequence ending in aⱼ
2. **Answer extraction:** L = max₁≤ⱼ≤ₙ R(j)
3. **Recurrence:** R(1) = 1, and for j > 1:

```
R(j) = {
  1                                    if aᵢ > aⱼ for all 1≤i<j
  1 + max₁≤ᵢ<ⱼ{R(i) | aᵢ ≤ aⱼ}        otherwise
}
```

**Algorithm (Algorithm 4.1):**
```
R(1) ← 1
for j := 2 to d:
    max ← 0
    for i := 1 to j-1:
        if R(i) > max and aᵢ ≤ aⱼ:
            max ← R(i)
    R(j) ← max + 1
```

**Complexity:** O(d²)

**Extensions:**
- **Backtracking:** Once R is computed, construct actual subsequence by working backwards
- **Variant:** Find longest subsequence where consecutive members differ by at most s

### 2. All Pairs Shortest Path

**Problem:**
- **Input:** Directed graph G=(V,E), V={1,2,...,n}, cost function C(i,j) ∈ ℕ⁺ ∪ {∞}
- **Output:** Array D where D(i,j) = length of shortest directed path from i to j

**Key Observation:** Exponentially many paths possible (Ω(2ⁿ) paths in O(n) nodes), so exhaustive search infeasible.

**Solution - Floyd-Warshall Algorithm (Algorithm 4.2):**

1. **Subproblems:** A(k,i,j) = length of shortest path from i to j where all intermediate nodes are in {1,2,...,k}
2. **Goal:** A(n,i,j) = D(i,j)
3. **Initialization:** A(0,i,j) = C(i,j)
4. **Recurrence:** For k > 0:

```
A(k,i,j) = min{ A(k-1,i,j), A(k-1,i,k) + A(k-1,k,j) }
```

**Space optimization:** Only need 2D array B(i,j), can overwrite A(k-1,*,*) with A(k,*,*)

**Algorithm:**
```
for i := 1 to n:
    for j := 1 to n:
        B(i,j) ← C(i,j)

for k := 1 to n:
    for i := 1 to n:
        for j := 1 to n:
            B(i,j) ← min{B(i,j), B(i,k) + B(k,j)}

return D ← B
```

**Complexity:** O(n³)

**Remarkable:** Runs in O(n³) time even though graph may have O(n²) edges.

**Why overwriting works:** Shortest path from i to k (or k to j) does not contain k as intermediate node, so A(k,i,k) = A(k-1,i,k) and A(k,k,j) = A(k-1,k,j).

#### 2.1 Bellman-Ford Algorithm

For finding shortest path from s to t in directed graph with non-negative edge costs:

**Subproblem:** opt(i,v) = minimal cost of i-path from v to t (path using at most i edges)

**Recurrence:** For i > 0:
```
opt(i,v) = min{ opt(i-1,v), min_{w∈V}{ c(v,w) + opt(i-1,w) } }
```

### 3. Simple Knapsack Problem (SKS)

**Problem:**
- **Input:** w₁, w₂, ..., wₐ, C ∈ ℕ (C = knapsack capacity)
- **Output:** max_S { K(S) | K(S) ≤ C }, where S ⊆ [d] and K(S) = Σᵢ∈S wᵢ

**Important:** NP-hard problem (no polynomial-time algorithm expected in general case)

**Solution:**

1. **Subproblems:** Boolean array R(i,j) for 0≤i≤d and 0≤j≤C:
```
R(i,j) = {
  true   if ∃S⊆[i] such that K(S) = j
  false  otherwise
}
```

2. **Answer extraction:** M = max_{j≤C} {j | R(d,j) = true}

3. **Initialization:**
   - R(0,j) = false for j=1,2,...,C
   - R(i,0) = true for i=0,1,...,d

4. **Recurrence:** For i,j > 0:
```
R(i,j) = true ⟺ R(i-1,j) = true ∨ (j≥wᵢ ∧ R(i-1,j-wᵢ) = true)
```

**Algorithm (Algorithm 4.3):**

**Space optimization:** Use 1D array S(j) to represent 2D array R(i,j)

```
S(0) ← true
for j := 1 to C:
    S(j) ← false

for i := 1 to d:
    for decreasing j := C down to 1:
        if (j ≥ wᵢ and S(j-wᵢ) = true):
            S(j) ← true
```

**Critical:** Inner loop must be decreasing to avoid incorrect overwriting.

**Complexity:** O(d·C)

**Why not polynomial?** Input size is O(d + log C) bits. Since C can be exponential in log C, algorithm is pseudo-polynomial (works for "small" C).

**Complexity Analysis:**
- If C = O(dᵏ) for constant k, then polynomial time
- If |C| = O(log d), then polynomial time
- Otherwise, exponential in input size

**Program Refinement:** Example of iterative improvement:
1. Start with 2D array R(i,j)
2. Realize only need two rows
3. Further realize can use single row by updating right-to-left

#### 3.1 Greedy Approximation

A "natural" greedy algorithm (order weights heaviest to lightest, add while possible) gives solution M̄ where either:
- M̄ = M (optimal), or
- M̄ > ½C (approximation guarantee)

This introduces **approximation algorithms** - efficient algorithms that don't give optimal solutions but provide guarantees on closeness to optimal.

#### 3.2 Dispersed Knapsack Problem

**Promise problem** variant where weights have special property:

**Input:** w₁,...,wₐ,C ∈ ℕ such that wᵢ ≥ Σⱼ₌ᵢ₊₁ᵈ wⱼ for i=1,...,d-1
**Output:** S_max ⊆ [d] maximizing K(S_max) subject to K(S_max) ≤ C

**Solution:** Greedy algorithm works optimally!

**Algorithm (Algorithm 4.4):**
```
S ← ∅
for i := 1 to d:
    if wᵢ + Σⱼ∈S wⱼ ≤ C:
        S ← S ∪ {i}
```

**Key:** Define "promising" appropriately and show it's a loop invariant.

#### 3.3 General Knapsack Problem (GKS)

**Problem:**
- **Input:** w₁,...,wₐ, v₁,...,vₐ, C ∈ ℕ
- **Output:** max_{S⊆[d]} { V(S) | K(S) ≤ C }, where V(S) = Σᵢ∈S vᵢ

Each weight wᵢ has associated value vᵢ. Goal: maximize value subject to weight constraint.

**Note:** SKS is special case where vᵢ = wᵢ for all i.

**Solution:**
1. Compute Boolean array R(i,j) as in SKS
2. Define value array:
```
V(i,j) = max{ V(S) | S⊆[i] and K(S) = j }
```

**Recurrence:** For i,j > 0:
```
V(i,j) = {
  V(i-1,j)                              if j < wᵢ or R(i-1,j-wᵢ) = false
  max{vᵢ + V(i-1,j-wᵢ), V(i-1,j)}      otherwise
}
```

**Alternative formulation:** If definition changes to K(S) ≤ j (instead of K(S) = j), then R array not needed:
```
V(i,j) = {
  V(i-1,j)                              if j < wᵢ
  max{vᵢ + V(i-1,j-wᵢ), V(i-1,j)}      otherwise
}
```

### 4. Activity Selection Problem

**Problem:**
- **Input:** List of activities (s₁,f₁,p₁),...,(sₙ,fₙ,pₙ) where pᵢ>0, sᵢ<fᵢ
  - sᵢ = start time
  - fᵢ = finish time
  - pᵢ = profit
- **Output:** Set S⊆[n] of non-overlapping activities maximizing total profit P(S) = Σᵢ∈S pᵢ

**Typical application:** Scheduling lectures in single classroom

**Solution:**

1. **Sort activities by finish time:** f₁ ≤ f₂ ≤ ... ≤ fₙ

2. **Identify distinct finish times:** u₁ < u₂ < ... < uₖ (k ≤ n)

3. **Set u₀:** Earliest start time, u₀ = min₁≤ᵢ≤ₙ sᵢ

4. **Subproblems:** Array A(0..k):
```
A(j) = max_{S⊆[n]} { P(S) | S feasible and fᵢ ≤ uⱼ for each i∈S }
```

where S **feasible** means no two activities overlap.

5. **Auxiliary array H(1..n):** H(i) = largest l such that u_l ≤ sᵢ

Compute H using binary search: O(n log n) total time

6. **Initialization:** A(0) = 0

7. **Recurrence:**
```
A(j) = max{ A(j-1), max_{1≤i≤n}{ pᵢ + A(H(i)) | fᵢ = uⱼ } }
```

**Intuition:** Try scheduling each activity finishing at uⱼ, find most profitable combination.

**Algorithm (Algorithm 4.5):**
```
A(0) ← 0
for j := 1 to k:
    max ← 0
    for i := 1 to n:
        if fᵢ = uⱼ:
            if pᵢ + A(H(i)) > max:
                max ← pᵢ + A(H(i))
    if A(j-1) > max:
        max ← A(j-1)
    A(j) ← max
```

**Backtracking:** To find actual activities:
- If A(k) = A(k-1): no activity ends at u_k, recurse on A(k-1)
- If A(k) > A(k-1): some activity ends at u_k, find i₀ where A(k) = p_{i₀} + A(H(i₀))

### 5. Jobs with Deadlines, Durations and Profits

**Problem:**
- **Input:** List of jobs (d₁,t₁,p₁),...,(dₙ,tₙ,pₙ)
  - dᵢ = duration
  - tᵢ = deadline
  - pᵢ = profit
- **Output:** Feasible schedule C(1..n) maximizing profit P(C)

**Feasibility conditions:** C(i)=-1 means not scheduled; C(i)≥0 means scheduled at time C(i):
1. If C(i) ≥ 0, then C(i) + dᵢ ≤ tᵢ (finish by deadline)
2. If i≠j and C(i),C(j) ≥ 0, then jobs don't overlap:
   - C(i) + dᵢ ≤ C(j), or
   - C(j) + dⱼ ≤ C(i)

**Key difference from activities:** Jobs can be scheduled anytime before deadline (flexible), activities have fixed start/finish times.

**Hardness:** "At least as hard as SKS" - can reduce SKS to job scheduling by setting dᵢ=wᵢ, tᵢ=C, pᵢ=wᵢ.

This is example of **reduction** - powerful tool in computational complexity for comparing problem difficulty.

**Solution:**

1. **Sort jobs by deadline:** t₁ ≤ t₂ ≤ ... ≤ tₙ

2. **Subproblems:** A(i,t) for all integer times 0 ≤ t ≤ tₙ:
```
A(i,t) = max{ P(C) : C feasible, only jobs in [i] scheduled,
                     all scheduled jobs finish by time t }
```

3. **Key insight:** If job i occurs in optimal schedule, assume it's last (has latest deadline), so finishes at t_min = min{tᵢ,t}

4. **Recurrence:** For i,t:
```
A(i,t) = {
  A(i-1,t)                                  if t_min < dᵢ
  max{ A(i-1,t), pᵢ + A(i-1,t_min-dᵢ) }    otherwise
}
```

### 6. Further Examples

#### 6.1 Consecutive Subsequence Sum Problem (CSSP)

**Problem:**
- **Input:** Real numbers r₁,...,rₙ
- **Output:** M = max₁≤ᵢ≤ⱼ≤ₙ Sᵢⱼ where Sᵢⱼ = rᵢ + rᵢ₊₁ + ... + rⱼ

**Example:** For {1, -5, 3, -1, 2, -8, 3}, answer is S₃₅ = 3+(-1)+2 = 4

**Naive solution:** O(n²) by computing all (n choose 2) sums

**Dynamic programming solution:** O(n)

**Subproblems:** M(j) = max{S₁ⱼ, S₂ⱼ, ..., Sⱼⱼ}

**Algorithm (Algorithm 4.6):**
```
M(1) ← r₁
for j := 2 to n:
    if M(j-1) > 0:
        M(j) ← M(j-1) + rⱼ
    else:
        M(j) ← rⱼ
```

**Answer:** M = max₁≤ⱼ≤ₙ M(j)

#### 6.2 Shuffle Problem

**Definition:** String w is a **shuffle** of u and v (written w = u⊙v) if there exist strings xᵢ, yᵢ such that:
- u = x₁x₂...xₖ
- v = y₁y₂...yₖ
- w = x₁y₁x₂y₂...xₖyₖ

**Square:** String w is a **square** if w = u⊙u for some u.

**Complexity results:**
- Recognizing if w = u⊙v is polynomial time (Mansfield 1982)
- Recognizing squares is NP-complete (Buss & Soltys)
- Recognizing iterated shuffles (w = u⊙u⊙...⊙u) is NP-complete (Warmuth & Haussler)

**Algorithm idea (Mansfield 1982):**

1. **Construct grid graph:** (|x|+1)×(|y|+1) nodes from (0,0) to (|x|,|y|)

2. **Add edges:** For i<|x|, j<|y|:
```
((i,j),(i+1,j))  if x_{i+1} = w_{i+j+1}
((i,j),(i,j+1))  if y_{j+1} = w_{i+j+1}
```

3. **Path correspondence:** Path from (0,0) to (|x|,|y|) represents a shuffle

4. **Number of paths bounded by:** (|x|+|y| choose |x|) - can be exponential

5. **Dynamic programming:** Compute partial solutions along diagonal lines to avoid exponential search

**Example:**
- Shuffle of "000" and "111" yielding "010101" has unique path
- Shuffle of "011" and "011" yielding "001111" has 8 distinct paths

## Key Concepts and Techniques

### Program Refinement

Example: Simple Knapsack Algorithm
1. **Robust initial idea:** Compute full 2D array R(i,j)
2. **First refinement:** Realize only need two rows
3. **Final refinement:** Update single row right-to-left (**mise en place**)

### Space Optimization Techniques

**Overwriting methods:**
- Floyd-Warshall: Overwrite A(k-1,*,*) with A(k,*,*)
- Simple Knapsack: Use decreasing loop to avoid conflicts

**When overwriting works:**
- Values being read aren't affected by values being written
- Careful loop ordering preserves needed values

### Reduction

**Definition:** Restating one problem in terms of another to show relative difficulty.

**Examples:**
- SKS reduces to Job Scheduling
- Job Scheduling "at least as hard as" SKS

**Power:** If can solve harder problem efficiently, automatically solve easier problem efficiently.

### Promise Problems

Problems where convenient condition on inputs is assumed (need not check).

**Example:** Dispersed Knapsack - assumes wᵢ ≥ Σⱼ₌ᵢ₊₁ᵈ wⱼ

**Note:** Different from "promising" in greedy algorithm correctness proofs.

### Complexity Considerations

**Pseudo-polynomial algorithms:** Polynomial in numeric value of input, exponential in input size.

**Example:** Simple Knapsack is O(d·C) but C requires log C bits.

**NP-hardness:** Indicates problem probably intractable (no efficient general solution).

### Approximation Algorithms

When exact solution intractable, design efficient algorithm with guarantees:
- May not be optimal
- But provably close to optimal

**Example:** Greedy SKS gives solution > ½C when not optimal.

## Problem Classification

| Problem | Complexity | Key Feature |
|---------|-----------|-------------|
| LMS | O(d²) | Polynomial, tractable |
| Floyd-Warshall | O(n³) | Polynomial, remarkable given O(n²) edges |
| Bellman-Ford | O(n·\|E\|·\|V\|) | Single-source shortest path |
| Simple Knapsack | O(d·C) | Pseudo-polynomial, NP-hard |
| General Knapsack | O(d·C) | Pseudo-polynomial, NP-hard |
| Dispersed Knapsack | O(d) | Greedy works! |
| Activity Selection | O(n log n) | Polynomial, tractable |
| Job Scheduling | NP-hard | At least as hard as SKS |
| Consecutive Sum | O(n) | Very efficient DP |
| Shuffle | O(\|x\|·\|y\|) | Polynomial (Mansfield) |
| Square Recognition | NP-complete | Buss & Soltys |

## Exercises and Extensions

The chapter includes numerous exercises covering:
- **Correctness proofs:** Pre/post-conditions, loop invariants
- **Backtracking:** Constructing actual optimal solutions from computed arrays
- **Implementation:** Programming the algorithms
- **Variants:** Modified problems testing understanding
- **Theoretical:** Complexity analysis, reductions

**Selected key exercises:**
- Prove LMS algorithm correctness with loop invariant
- Explain why Floyd overwriting works
- Construct counterexample if SKS loop not decreasing
- Define feasibility for activity schedules
- Show SKS reduces to job scheduling
- Compute H array efficiently using binary search

## Historical Notes and References

**Key researchers:**
- **Robert Floyd & Stephen Warshall:** All-pairs shortest paths
- **Richard Bellman:** Dynamic programming pioneer, shortest paths
- **Alan Mansfield (1982):** Polynomial shuffle algorithm
- **Kurt Warmuth & David Haussler:** Iterated shuffle complexity
- **Sam Buss & Michael Soltys:** Square recognition NP-completeness

**Applications:**
- **Formal languages:** Shuffle operation (Ginsburg & Spanier)
- **Concurrent processes:** Modeling (Riddle, Shaw)
- **Complexity theory:** Understanding problem difficulty

**Additional topics:**
- Matroids provide abstract model for greedy algorithms
- General model for dynamic programming currently being developed (Alek)

## Relationship to Other Chapters

- **Chapter 2 (Greedy):** Contrast bottom-up DP vs greedy's opportunistic choices
- **Chapter 3 (Divide-and-Conquer):** Contrast bottom-up DP vs top-down D&C
- **Chapter 8 (Computational Foundations):** NP-completeness, reductions, complexity
- **Section 2.4 (Jobs with deadlines):** Unit-time job scheduling (DP generalizes)

## Key Takeaways

1. **DP = Subproblems + Recurrence + Algorithm:** Three-step framework
2. **Bottom-up approach:** Build solutions from simplest to most complex
3. **Memoization:** Store subproblem solutions to avoid recomputation
4. **Space optimization:** Often can reduce dimensions of storage
5. **Pseudo-polynomial ≠ Polynomial:** Be careful about input encoding
6. **Reductions show hardness:** Powerful technique for understanding difficulty
7. **Approximation when exact intractable:** Practical compromise
8. **Promise problems can be easier:** Additional structure enables efficiency

## Common Patterns

1. **Array index problems:** LMS, Consecutive Sum
2. **Graph problems:** Floyd-Warshall, Bellman-Ford
3. **Optimization under constraints:** Knapsack variants
4. **Scheduling problems:** Activities, Jobs
5. **String problems:** Shuffle

**General recipe:**
- Define array indexed by problem parameters
- Initialize base cases
- Fill array using recurrence relation
- Extract answer from computed array
- Optionally backtrack to construct solution

---

**Summary:** Dynamic programming provides a powerful algorithmic paradigm for solving optimization problems by breaking them into overlapping subproblems. While not always yielding polynomial-time solutions (e.g., NP-hard knapsack), DP often provides the best known approaches and insights into problem structure. The chapter emphasizes both theoretical understanding (correctness, complexity) and practical implementation (space optimization, backtracking).

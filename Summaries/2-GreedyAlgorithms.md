# Chapter 2: Greedy Algorithms

## Overview

> "It may be profitable to you to reflect, in future, that there never were greed and cunning in the world yet, that did not do too much, and overreach themselves." — D. Copperfield, Dickens

Greedy algorithms make **locally optimal** choices hoping they lead to a **globally optimal** solution. They're prone to "instant gratification" — choosing what looks best right now without looking ahead. Sometimes this works beautifully (Kruskal's algorithm, job scheduling), sometimes it fails spectacularly (certain coin denominations).

**Key characteristic:** Greedy algorithms are simple and fast, but don't always work. When they do work, correctness proofs typically use **promising** as a loop invariant.

## Introduction: The Greedy Strategy

**Classic example:** Making change
- **Input:** Amount n, denominations C = {1, 5, 25, 100}
- **Greedy strategy:** Give largest coin possible, repeat
- **For {1,5,25}:** Always optimal!
- **For {1,10,25}:** Can fail (e.g., 30 = 25+1+1+1+1+1 vs. 10+10+10)

**When greedy works:** Problem has **greedy-choice property** and **optimal substructure**

**Proving greedy works:** Show that "promising" is a loop invariant

## Section 2.1: Minimum Cost Spanning Trees (MCST)

### Graph Terminology

**Undirected graph G = (V,E):**
- **Path:** Sequence v₁,v₂,...,vₖ where each (vᵢ,vᵢ₊₁) ∈ E
- **Connected:** Path exists between every pair of vertices
- **Cycle:** Simply closed path v₁,...,vₖ,v₁ with k ≥ 3
- **Acyclic:** No cycles
- **Tree:** Connected and acyclic

**Spanning tree T ⊆ E:**
- Connects all nodes of G
- Contains no cycles
- Same number of edges for all spanning trees of G

**Key lemmas:**
- **Lemma 2.1:** Every tree with n nodes has exactly n-1 edges
- **Lemma 2.2:** Graph with n nodes and > n-1 edges must contain cycle

**Cost function:** c(e) ≥ 0 for each edge e
**Total cost:** c(G) = Σc(e) for all edges in G

**MCST:** Spanning tree T where c(T) ≤ c(T') for all spanning trees T'

### Kruskal's Algorithm

**Idea:** Build tree edge-by-edge, always choosing cheapest edge that doesn't create cycle

**Algorithm 4 — Kruskal:**
```
1. Sort edges: c(e₁) ≤ c(e₂) ≤ ... ≤ c(eₘ)
2. T ← ∅
3. for i = 1 to m:
4.     if T ∪ {eᵢ} has no cycle:
5.         T ← T ∪ {eᵢ}
```

**Cycle detection:** Use connected component tracking
- Array D[i] = j means vertex i is in component Vⱼ
- Edge (r,s) creates cycle iff D[r] = D[s]
- When adding edge, merge components

**Algorithm 5 — Merging Components:**
```
k ← D[r]
l ← D[s]
for j = 1 to n:
    if D[j] = l:
        D[j] ← k
```

**Complexity:** O(m² + m·n) where m = |E|, n = |V|
- Sorting: O(m²) with insertion sort
- Each iteration: O(n) for merging components
- Can be improved with better data structures (union-find)

### Correctness Proof

**Must show:**
1. T is a spanning tree (connected and acyclic)
2. T is minimum cost

**Acyclicity:** Obvious — never add edge that creates cycle

**Connectivity:** Proved via loop invariant:
```
T ∪ {eᵢ₊₁,...,eₘ} connects all nodes in V
```

**Lemma 2.3:** Kruskal outputs a tree (given G connected)

**Key concept: Promising**

**Definition:** Edge set T is **promising** if T can be extended to a MCST
- That is, ∃ MCST T' such that T ⊆ T'

**Lemma 2.4 (Main correctness):** "T is promising" is a loop invariant

**Proof structure:**
- **Basis:** T = ∅ is promising (any MCST extends it)
- **Induction step:** If T is promising before iteration, it remains promising after

**Two cases when considering edge eᵢ:**

**Case 1: eᵢ rejected** (would create cycle)
- T unchanged, still promising
- eᵢ cannot be in any extension of T (would create cycle)

**Case 2: eᵢ accepted** (no cycle created)
- Must show T ∪ {eᵢ} still promising
- Let T₁ be MCST extending T

**Subcase 2a:** eᵢ ∈ T₁ — obviously T ∪ {eᵢ} promising

**Subcase 2b:** eᵢ ∉ T₁ — use **Exchange Lemma**:

**Lemma 2.5 (Exchange Lemma):** Let T₁, T₂ be spanning trees of G.
For every edge e ∈ T₂ - T₁, there exists e' ∈ T₁ - T₂ such that
T₃ = (T₁ ∪ {e}) - {e'} is a spanning tree.

**Application:** When eᵢ ∉ T₁, exchange gives edge eⱼ with j > i
- Since edges sorted by cost: c(eᵢ) ≤ c(eⱼ)
- Therefore c(T₃) ≤ c(T₁), so T₃ also MCST
- Since T ∪ {eᵢ} ⊆ T₃, it's promising ✓

**Additional properties:**
- **Smallest edge:** If c(e₁) < c(eᵢ) for all i > 1, then e₁ in every MCST
- **All MCSTs reachable:** For every MCST, some tie-breaking produces it
- **Spanning forest:** If G disconnected, Kruskal produces minimum spanning forest

## Section 2.2: Jobs with Deadlines and Profits

### Problem Statement

**Input:** n jobs, each with:
- **Profit:** gᵢ ∈ ℝ⁺ (gain from completing job i)
- **Deadline:** dᵢ ∈ ℕ (must complete by time dᵢ)
- **Duration:** 1 unit time for all jobs

**Schedule S:** Array S(1), S(2),..., S(d) where d = max dᵢ
- S(t) = i means job i scheduled at time t
- S(t) = 0 means no job at time t

**Feasible schedule:**
1. **Meets deadlines:** If S(t) = i > 0, then t ≤ dᵢ
2. **Each job once:** If t₁ ≠ t₂ and S(t₁) ≠ 0, then S(t₁) ≠ S(t₂)

**Profit:** P(S) = Σg_{S(t)} where g₀ = 0

**Goal:** Find feasible schedule S maximizing P(S)

### Greedy Algorithm

**Strategy:**
1. Order jobs by profit (g₁ ≥ g₂ ≥ ... ≥ gₙ)
2. Schedule each job as late as possible within its deadline

**Algorithm 6 — Job Scheduling:**
```
1. Sort jobs: g₁ ≥ g₂ ≥ ... ≥ gₙ
2. d ← max dᵢ
3. for t = 1 to d:
4.     S(t) ← 0
5. for i = 1 to n:
6.     Find largest t: S(t) = 0 and t ≤ dᵢ
7.     S(t) ← i  (if such t exists)
```

**Surprising insight:** **Procrastination is optimal!**
- Scheduling jobs late keeps early slots free
- Allows higher-profit jobs with early deadlines to be accommodated

### Correctness Proof

**Key concept: Promising schedule**

**Definition:** Schedule S is **promising** (after iteration i) if S can be extended to optimal schedule using jobs from {i+1, i+2,..., n}

**Extension:** S' extends S if whenever S(t) ≠ 0, then S(t) = S'(t)

**Example:** S' = (2,0,1,0,3) extends S = (2,0,0,0,3)

**Theorem 2.1:** The greedy solution to job scheduling is optimal

**Lemma 2.6:** "S is promising" is loop invariant

**Proof structure:**

**Basis:** S = (0,0,...,0) promising — any optimal schedule extends it

**Induction step:** Consider job i. Let S_opt extend S optimally. Show S' (after iteration i) still promising.

**Case 1: Job i cannot be scheduled**
- S' = S, so S_opt' = S_opt works
- Subtle point: i not used in S_opt (otherwise could be scheduled)

**Case 2: Job i scheduled at time t₀** (latest possible)

**Subcase 2a:** i scheduled in S_opt at time t₁

- If t₁ = t₀: S_opt' = S_opt works
- If t₁ < t₀: Swap positions t₀ and t₁ in S_opt to get S_opt'
  - Why feasible? Both jobs meet deadlines, no conflicts
  - Why extends S'? S'(t₀) = i now matches
  - Why equal profit? Just swapping, same jobs scheduled
- If t₁ > t₀: **Impossible** (t₀ was latest possible for i)

**Subcase 2b:** i not scheduled in S_opt
- Define S_opt': Same as S_opt except S_opt'(t₀) = i
- Must show: S_opt'(t₀) = j ⇒ gⱼ ≤ gᵢ

**Claim:** If S_opt(t₀) = j, then gⱼ ≤ gᵢ

**Proof by contradiction:**
- Assume gⱼ > gᵢ
- Then j considered before i
- Since S'(t₀) = i was available, j must have been scheduled elsewhere (say t₂)
- But S_opt extends S, so S(t₂) = j
- Since S(t₀) = 0 and t₀ ≤ dⱼ, job j should have been scheduled at t₀ in S
- Contradiction! (Algorithm schedules greedily)

Therefore gⱼ ≤ gᵢ, so replacing j with i doesn't decrease profit ✓

**Why lemma ⇒ theorem:** After all iterations, S can be extended using ∅ — so S itself is optimal!

## Section 2.3: Further Examples and Problems

### Make Change

**Input:** Amount n, denominations C
**Output:** Smallest set of coins summing to n

**Algorithm 7 — Make Change:**
```
C ← {1, 10, 25, 100}
L ← ∅; s ← 0
while (s < n):
    find largest x ∈ C: s + x ≤ n
    L ← L ∪ {x}
    s ← s + x
return L
```

**For C = {1,10,25,100}:** May not be optimal!
- Example: n = 30 gives {25,1,1,1,1,1} (6 coins) vs. optimal {10,10,10} (3 coins)

**For C = {1, p, p², ..., pⁿ}:** Greedy IS optimal!
- Powers of base p always work
- Proof uses "promising list" invariant

### Maximum Weight Matching

**Bipartite graph:** G = (V₁ ∪ V₂, E) where E ⊆ V₁ × V₂

**Matching M ⊆ E:** No two edges share vertex

**Weight:** w(M) = Σw(e) for e ∈ M

**Greedy approach:** Order edges by weight, add if no conflict

**Problem:** Greedy doesn't always work!
- Counterexamples exist where greedy fails

**Special case:** If all weights are distinct powers of 2, greedy works
- Requires proof using "promising matching" invariant

### Dijkstra's Shortest Path Algorithm

**Input:**
- Graph G = (V,E)
- Start node s
- Cost function c(e) for each edge

**Output:** Shortest path from s to all other nodes

**Greedy strategy:**
- Maintain set S of explored nodes
- For each u ∈ S, store d(u) = cheapest path cost within S

**Algorithm:**
```
S ← {s}
d(s) ← 0
while S ≠ V:
    for each v ∈ V - S:
        d'(v) ← min_{u∈S, e=(u,v)} [d(u) + c(e)]
    Choose v minimizing d'(v)
    S ← S ∪ {v}
    d(v) ← d'(v)
```

**Complexity:** O(n²)

**Correctness:** At each step, choose closest unexplored node
- Greedy choice is safe because all costs non-negative
- No shorter path can go through unexplored nodes

**Application: OSPF Protocol**
- Open Shortest Path First
- Routing protocol for Internet (RFC 2328)
- Uses Dijkstra to compute shortest paths tree
- Fundamental to Internet routing infrastructure

## Common Patterns and Proof Techniques

### The Promising Invariant Pattern

**General template for proving greedy correctness:**

1. **Define "promising":** Partial solution can be extended to optimal
2. **Prove basis:** Empty/initial solution is promising
3. **Prove induction step:** If solution promising before iteration, remains promising after
4. **Case analysis:**
   - Greedy choice rejected: Show still promising (choice wouldn't help)
   - Greedy choice accepted: Show still promising (use exchange argument)
5. **Conclude:** After all iterations, partial solution IS optimal solution

### Exchange Lemma Technique

**Common pattern:** To show greedy choice is safe:
1. Suppose optimal solution O doesn't include greedy choice g
2. Identify element e in O that "conflicts" with g
3. Show can swap e for g to get O'
4. Prove O' is also optimal (or better)
5. Conclude g can be in optimal solution

**Examples:**
- Kruskal: Exchange edges in spanning trees
- Job scheduling: Swap job positions

### Case Analysis Structure

**When proving greedy correctness:**
1. **Choice accepted:** Show how to extend to optimal
2. **Choice rejected:** Show rejection doesn't hurt (no loss of optimality)

**Often split accepted case:**
- Subcase a: Greedy choice in optimal solution
- Subcase b: Greedy choice not in optimal solution (use exchange)

## Important Exercises

### Correctness Proofs
- **Exercise 2.1:** Prove Lemma 2.1 (trees have n-1 edges)
- **Exercise 2.2:** Prove Lemma 2.2 (> n-1 edges ⇒ cycle)
- **Exercise 2.3:** Prove connectivity of Kruskal output
- **Exercise 2.4:** Prove Exchange Lemma
- **Exercise 2.5:** Prove make-change correctness for power denominations
- **Exercise 2.6:** Prove Dijkstra correctness

### Complexity Analysis
- **Exercise 2.7:** Analyze Kruskal complexity with insertion sort
- **Exercise 2.8:** Improve Kruskal with union-find
- **Exercise 2.9:** Analyze job scheduling complexity

### Counterexamples
- **Exercise 2.10:** Find coin denominations where greedy fails
- **Exercise 2.11:** Find bipartite graph where greedy matching fails

### Implementation
- **Exercise 2.12:** Implement Kruskal with component tracking
- **Exercise 2.13:** Implement job scheduling
- **Exercise 2.14:** Implement Dijkstra's algorithm
- **Exercise 2.15:** Implement OSPF routing daemon

### Extensions
- **Exercise 2.16:** Show smallest-cost edge always in some MCST
- **Exercise 2.17:** Show all MCSTs reachable by tie-breaking
- **Exercise 2.18:** Define and prove spanning forest for disconnected graphs

## Key Concepts and Takeaways

### When Greedy Works

**Greedy-choice property:** Locally optimal choice leads to globally optimal solution

**Optimal substructure:** Optimal solution contains optimal solutions to subproblems

**Problems where greedy works:**
- MCST (Kruskal, Prim)
- Single-source shortest paths (Dijkstra) — non-negative weights only
- Job scheduling with unit times
- Huffman coding
- Activity selection
- Make change with special denominations

### When Greedy Fails

**Problems where greedy fails:**
- General coin change
- Knapsack (fractional works, 0/1 doesn't)
- Longest path
- Traveling salesman
- Graph coloring

**Key insight:** Greedy needs special problem structure to work

### Proof Complexity

**Proving greedy works is often harder than the algorithm itself!**

**Two-step process:**
1. Show algorithm produces feasible solution
2. Show solution is optimal (typically via "promising")

**Exchange arguments are powerful:**
- Show optimal can be transformed to include greedy choices
- Without decreasing quality

### Comparison with Other Paradigms

**Greedy vs. Dynamic Programming:**
- Greedy: Make choice, never reconsider
- DP: Consider all choices, build up from subproblems
- Greedy: O(n) or O(n log n) typically
- DP: O(n²) or worse typically

**Greedy vs. Divide-and-Conquer:**
- Greedy: One subproblem (make choice, solve rest)
- D&C: Multiple subproblems (split, solve all, combine)

## Notes and Historical Context

### Kruskal's Algorithm

**Joseph Kruskal (1956):** Published algorithm for MCST
- Independently discovered by others around same time
- Prim's algorithm (1957) is alternative greedy MCST algorithm

**Applications:**
- Network design (minimize cable/wire length)
- Clustering (hierarchical clustering uses reverse-Kruskal)
- Image segmentation
- Approximation algorithms

### Job Scheduling

**Procrastination principle:** Counterintuitive but optimal!

**Generalization:** With arbitrary durations (not unit time), greedy doesn't work
- Problem becomes NP-hard
- Dynamic programming gives pseudo-polynomial solution

### Dijkstra's Algorithm

**Edsger Dijkstra (1959):** Pioneering computer scientist
- Invented algorithm while shopping with fiancée
- Thought through problem without paper/pencil
- Structured programming advocate
- "Go To Statement Considered Harmful"

**Limitations:**
- Requires non-negative edge weights
- For negative weights, use Bellman-Ford
- For all-pairs, use Floyd-Warshall

**Optimizations:**
- With binary heap: O((|V| + |E|) log |V|)
- With Fibonacci heap: O(|E| + |V| log |V|)

### OSPF and Internet Routing

**Real-world impact:** Dijkstra's algorithm routes packets across Internet!

**Link-state routing:**
- Each router knows network topology
- Computes shortest paths tree
- Updates when topology changes

**RFC 2328:** Detailed specification of OSPF Version 2

## Summary

Chapter 2 introduces greedy algorithms through two major examples:

1. **Kruskal's algorithm (MCST):** Shows greedy working perfectly
   - Build tree incrementally, always choosing cheapest safe edge
   - Proof uses "promising" invariant and Exchange Lemma
   - O(m²) time, optimal solution guaranteed

2. **Job scheduling:** Shows greedy optimality in surprising context
   - Procrastination principle: schedule jobs as late as possible
   - Proof uses "promising schedule" invariant
   - Elegant case analysis handles all situations

**Unifying theme:** "Promising" as loop invariant

**Key technique:** Exchange arguments to show greedy choices can appear in optimal solutions

**Practical lesson:** Greedy is fast and simple when it works, but correctness proofs are non-trivial and require special problem structure

**Contrast:** When greedy fails (some coin denominations, maximum weight matching in general), other techniques needed (dynamic programming, branch-and-bound, approximation algorithms)

The chapter demonstrates that algorithm design requires both creativity (finding greedy approach) and rigor (proving it works), with the proof often being more challenging than the algorithm itself.

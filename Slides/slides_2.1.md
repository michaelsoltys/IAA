---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 2.1: Minimum Cost Spanning Trees
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Minimum Cost Spanning Trees
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

# Minimum Cost Spanning Trees

Section 2.1 - Greedy Algorithms

---

# Graph Representation

**Adjacency Matrix:** For a graph $G = (V, E)$ with $n = |V|$ nodes

<v-click>

$$A_G[i,j] = \begin{cases} 1 & \text{if } (i,j) \in E \\ 0 & \text{otherwise} \end{cases}$$

</v-click>

<v-click>

**Encoding as a string:** Concatenate rows of $A_G$ to get $s_G \in \{0,1\}^{n^2}$

To check if $(i,j)$ is an edge: look at position $(i-1)n + j$ in $s_G$

</v-click>

---

# Graph Definitions

<v-clicks>

- **Undirected graph:** $G = (V, E)$ where $(u,v) \in E \Leftrightarrow (v,u) \in E$
- **Degree:** Number of edges touching a vertex
- **Path:** Sequence $v_1, v_2, \ldots, v_k$ where each $(v_i, v_{i+1}) \in E$
- **Connected:** Every pair of nodes has a path between them
- **Cycle:** Simply closed path $v_1, \ldots, v_k, v_1$ with all $v_i$ distinct, $k \geq 3$
- **Acyclic:** No cycles
- **Tree:** Connected + Acyclic
- **Spanning tree:** Subset $T \subseteq E$ such that $(V, T)$ is a tree

</v-clicks>

---

# Trees Have $n-1$ Edges

**Lemma:** Every tree with $n$ nodes has exactly $n-1$ edges.

<v-click>

**Proof sketch:**

</v-click>

<v-clicks>

1. **Claim:** Every tree has a leaf (node with degree 1)
   - If no leaf exists, every node has $\geq 2$ edges
   - Start anywhere, keep walking → must form a cycle (contradiction!)

2. **By induction on $n$:**
   - Base case: $n = 1$ trivially has 0 edges ✓
   - Inductive step: Remove a leaf and its edge from tree $T$
   - Get tree $T'$ with $n$ nodes, which has $n-1$ edges by IH
   - So $T$ has $(n-1) + 1 = n$ edges when we add back the leaf

</v-clicks>

---

# Minimum Cost Spanning Tree

**Setup:**
- Graph $G = (V, E)$ with cost function $c: E \rightarrow \mathbb{R}^+$
- Total cost: $c(T) = \sum_{e \in T} c(e)$

<v-click>

**Definition:** $T$ is a **Minimum Cost Spanning Tree (MCST)** if:
1. $T$ is a spanning tree for $G$
2. For any other spanning tree $T'$: $c(T) \leq c(T')$

</v-click>

<v-click>

**Goal:** Find a MCST for $G$

</v-click>

---

# Kruskal's Algorithm

```text
Kruskal's Algorithm:
1. Sort edges: c(e₁) ≤ c(e₂) ≤ ... ≤ c(eₘ)
2. T ← ∅
3. for i = 1 to m:
4.     if T ∪ {eᵢ} has no cycle:
5.         T ← T ∪ {eᵢ}
6. return T
```

<v-click>

**Key insight:** Greedy approach - always add the cheapest edge that doesn't create a cycle

</v-click>

---

# Cycle Detection with Connected Components

How do we check if adding an edge creates a cycle?

<v-clicks>

- Maintain array $D[i]$ where $D[i] = j$ means vertex $i$ is in component $V_j$
- Initialize: $D[i] \leftarrow i$ for all $i$
- Edge $e_i = (r, s)$ forms a cycle iff $D[r] = D[s]$

</v-clicks>

<v-click>

**Merging Components** (when adding edge $(r,s)$):
```text
k ← D[r]
l ← D[s]
for j = 1 to n:
    if D[j] = l:
        D[j] ← k
```

</v-click>

---

# Why Does Kruskal's Algorithm Work?

We need to show the output $T$ is:
1. **Acyclic** - obvious, we never add an edge that creates a cycle
2. **Connected** - less obvious!

<v-click>

**Loop Invariant for Connectivity:**

> The edge set $T \cup \{e_{i+1}, \ldots, e_m\}$ connects all nodes in $V$

</v-click>

<v-click>

If we reject $e_i$ because it forms a cycle, then $T$ already has a path connecting the endpoints of $e_i$, so connectivity is preserved.

</v-click>

---

# The "Promising" Property

**Definition:** A set $T$ of edges is **promising** if it can be extended to a MCST.

<v-click>

**Theorem:** "$T$ is promising" is a loop invariant for Kruskal's algorithm.

</v-click>

<v-click>

**Why this matters:** After the algorithm terminates, $T$ is promising AND all edges have been considered → $T$ must itself be a MCST!

</v-click>

---

# Proof: Promising is Invariant

**Basis:** $T = \emptyset$ is promising (empty set extends to any MCST)

**Induction Step:** Assume $T$ is promising. Show it remains so after considering edge $e_i$.

<v-click>

**Case 1:** $e_i$ is rejected (creates cycle)
- $T$ unchanged, still promising
- The MCST extending $T$ couldn't have used $e_i$ anyway (would create cycle)

</v-click>

---

# Proof: Case 2 - Edge Accepted

$e_i$ is accepted. Must show $T \cup \{e_i\}$ is promising.

Since $T$ is promising, there exists MCST $T_1$ with $T \subseteq T_1$.

<v-clicks>

**Subcase a:** $e_i \in T_1$
- Then $T \cup \{e_i\} \subseteq T_1$, so $T \cup \{e_i\}$ is promising ✓

**Subcase b:** $e_i \notin T_1$
- Use the **Exchange Lemma**!

</v-clicks>

---

# Exchange Lemma

**Lemma:** Let $G$ be connected, $T_1$ and $T_2$ be spanning trees. For every edge $e \in T_2 - T_1$, there exists $e' \in T_1 - T_2$ such that $T_1 \cup \{e\} - \{e'\}$ is a spanning tree.

<v-click>

```
    T₁                    T₂
   ┌───────────┐    ┌───────────┐
   │     ●     │    │     ●     │
   │    /      │    │      \    │
   │   ● e'    │    │    e  ●   │
   │           │    │           │
   └───────────┘    └───────────┘
```

</v-click>

<v-click>

**Idea:** Adding $e$ to $T_1$ creates a cycle; some edge $e'$ in that cycle must be in $T_1 - T_2$

</v-click>

---

# Completing the Proof

**Subcase b continued:** $e_i \notin T_1$

<v-clicks>

- By Exchange Lemma: $\exists e_j \in T_1 - T_2$ such that $T_3 = (T_1 \cup \{e_i\}) - \{e_j\}$ is a spanning tree
- Key observation: $i < j$ (otherwise $e_j$ would have been rejected earlier, forming a cycle in $T$)
- Since edges are sorted: $c(e_i) \leq c(e_j)$
- Therefore: $c(T_3) \leq c(T_1)$
- So $T_3$ is also a MCST!
- Since $T \cup \{e_i\} \subseteq T_3$, we have $T \cup \{e_i\}$ is promising ✓

</v-clicks>

---

# Example Run

Graph with 5 nodes, 7 edges (all cost 1):

| Iteration | Edge | Current $T$ | MCST extending $T$ |
|-----------|------|-------------|-------------------|
| 0 | — | $\emptyset$ | $\{e_1,e_3,e_4,e_7\}$ |
| 1 | $e_1$ | $\{e_1\}$ | $\{e_1,e_3,e_4,e_7\}$ |
| 2 | $e_2$ | $\{e_1,e_2\}$ | $\{e_1,e_2,e_4,e_7\}$ |
| 3 | $e_3$ | $\{e_1,e_2\}$ | $\{e_1,e_2,e_4,e_7\}$ |
| 4 | $e_4$ | $\{e_1,e_2,e_4\}$ | $\{e_1,e_2,e_4,e_7\}$ |
| 5 | $e_5$ | $\{e_1,e_2,e_4\}$ | $\{e_1,e_2,e_4,e_7\}$ |
| 6 | $e_6$ | $\{e_1,e_2,e_4,e_6\}$ | $\{e_1,e_2,e_4,e_6\}$ |
| 7 | $e_7$ | $\{e_1,e_2,e_4,e_6\}$ | $\{e_1,e_2,e_4,e_6\}$ |

---

# Complexity Analysis

<v-clicks>

1. **Sorting edges:** $O(m \log m)$ or $O(m^2)$ with insertion sort
2. **Main loop:** $m$ iterations
3. **Cycle check:** $O(1)$ using component array
4. **Merge components:** $O(n)$ per merge, at most $n-1$ merges

**Total:** $O(m \log m + mn)$ or with better data structures: $O(m \log n)$

</v-clicks>

---

# Key Problems

<v-clicks>

1. **Problem 2.6:** Prove that every tree with $n$ nodes has $n-1$ edges

2. **Problem 2.8:** Prove Kruskal's algorithm outputs a tree (connected and acyclic)

3. **Problem 2.11:** Prove the Exchange Lemma

4. **Problem 2.12:** If $e_1$ has strictly smallest cost, show every MCST includes $e_1$

5. **Problem 2.14:** Implement Kruskal's algorithm for grid graphs

</v-clicks>

---

# Summary

<v-clicks>

- **MCST Problem:** Find spanning tree with minimum total edge cost
- **Kruskal's Algorithm:** Greedy - add cheapest non-cycle-forming edge
- **Key Invariant:** "$T$ is promising" (can be extended to MCST)
- **Exchange Lemma:** Allows swapping edges between spanning trees
- **Complexity:** $O(m \log m)$ with efficient sorting
- **Correctness:** Proven via loop invariant and induction

</v-clicks>

---

# Next: Jobs with Deadlines and Profits

Another greedy algorithm where "promising" is the key invariant!

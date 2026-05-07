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

# Minimum Cost Spanning Trees

Section 2.1 — Connect every node in a weighted graph using the cheapest possible set of edges; greedy works, and the proof is gorgeous.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Graph Representation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

How we encode a graph as an $n^2$-bit string — the input format we'll assume throughout.

</div>

**Adjacency Matrix:** For a graph $G = (V, E)$ with $n = |V|$ nodes


$$A_G[i,j] = \begin{cases} 1 & \text{if } (i,j) \in E \\ 0 & \text{otherwise} \end{cases}$$


**Encoding as a string:** Concatenate rows of $A_G$ to get $s_G \in \{0,1\}^{n^2}$

To check if $(i,j)$ is an edge: look at position $(i-1)n + j$ in $s_G$


---

# Graph Definitions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The vocabulary — paths, cycles, connected, tree, spanning tree — that we'll use for every graph algorithm.

</div>


- **Undirected graph:** $G = (V, E)$ where $(u,v) \in E \Leftrightarrow (v,u) \in E$
- **Degree:** Number of edges touching a vertex
- **Path:** Sequence $v_1, v_2, \ldots, v_k$ where each $(v_i, v_{i+1}) \in E$
- **Connected:** Every pair of nodes has a path between them
- **Cycle:** Simply closed path $v_1, \ldots, v_k, v_1$ with all $v_i$ distinct, $k \geq 3$
- **Acyclic:** No cycles
- **Tree:** Connected + Acyclic
- **Spanning tree:** Subset $T \subseteq E$ such that $(V, T)$ is a tree


---

# Trees Have $n-1$ Edges

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A first induction proof using leaves — the structural fact we'll quote constantly.

</div>

**Lemma:** Every tree with $n$ nodes has exactly $n-1$ edges. <span style="font-size: 0.6em; color: navy;">Lem 2.1, Pg 34, lem:trees</span>


**Proof sketch:**


1. **Claim:** Every tree has a leaf (node with degree 1)
   - If no leaf exists, every node has $\geq 2$ edges
   - Start anywhere, keep walking → must form a cycle (contradiction!)

2. **By induction on $n$:**
   - Base case: $n = 1$ trivially has 0 edges ✓
   - Inductive step: Remove a leaf and its edge from tree $T$
   - Get tree $T'$ with $n$ nodes, which has $n-1$ edges by IH
   - So $T$ has $(n-1) + 1 = n$ edges when we add back the leaf


---

# Minimum Cost Spanning Tree

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Pick $n-1$ edges that connect everything *and* minimize total cost — the classic network-design problem.

</div>

**Setup:**
- Graph $G = (V, E)$ with cost function $c: E \rightarrow \mathbb{R}^+$
- Total cost: $c(T) = \sum_{e \in T} c(e)$


**Definition:** $T$ is a **Minimum Cost Spanning Tree (MCST)** if:
1. $T$ is a spanning tree for $G$
2. For any other spanning tree $T'$: $c(T) \leq c(T')$


**Goal:** Find a MCST for $G$


---

# Kruskal's Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Sort edges cheap-to-expensive and add each one *unless it would close a cycle* — that's the entire algorithm.

</div>

<span style="font-size: 0.6em; color: navy;">Alg 10, Pg 35, alg:kruskal</span>

```text
Kruskal's Algorithm:
1. Sort edges: c(e₁) ≤ c(e₂) ≤ ... ≤ c(eₘ)
2. T ← ∅
3. for i = 1 to m:
4.     if T ∪ {eᵢ} has no cycle:
5.         T ← T ∪ {eᵢ}
6. return T
```


**Key insight:** Greedy approach - always add the cheapest edge that doesn't create a cycle


---

# Cycle Detection with Connected Components

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A simple component array $D[\,]$ — same label means same component, so a cycle is just $D[r] = D[s]$.

</div>

How do we check if adding an edge creates a cycle?


- Maintain array $D[i]$ where $D[i] = j$ means vertex $i$ is in component $V_j$
- Initialize: $D[i] \leftarrow i$ for all $i$
- Edge $e_i = (r, s)$ forms a cycle iff $D[r] = D[s]$


**Merging Components** (when adding edge $(r,s)$):

<span style="font-size: 0.6em; color: navy;">Alg 11, Pg 35, alg:component</span>

```text
k ← D[r]
l ← D[s]
for j = 1 to n:
    if D[j] = l:
        D[j] ← k
```


---

# Why Does Kruskal's Algorithm Work?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Acyclic is automatic; *connected* needs an invariant — the unconsidered edges always plug the gaps.

</div>

We need to show the output $T$ is:
1. **Acyclic** - obvious, we never add an edge that creates a cycle
2. **Connected** - less obvious!


**Loop Invariant for Connectivity:**

> The edge set $T \cup \{e_{i+1}, \ldots, e_m\}$ connects all nodes in $V$


If we reject $e_i$ because it forms a cycle, then $T$ already has a path connecting the endpoints of $e_i$, so connectivity is preserved.


---

# The "Promising" Property

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The central idea: at every step, our partial $T$ can still be completed to *some* MCST — keep this true and we win.

</div>

**Definition:** A set $T$ of edges is **promising** if it can be extended to a MCST.


**Theorem:** "$T$ is promising" is a loop invariant for Kruskal's algorithm. <span style="font-size: 0.6em; color: navy;">Lem 2.10, Pg 37, lem:promising</span>


**Why this matters:** After the algorithm terminates, $T$ is promising AND all edges have been considered → $T$ must itself be a MCST!


---

# Proof: Promising is Invariant

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The basis is trivial; the rejection case is easy — the real work is when we *accept* an edge.

</div>

**Basis:** $T = \emptyset$ is promising (empty set extends to any MCST)

**Induction Step:** Assume $T$ is promising. Show it remains so after considering edge $e_i$.


**Case 1:** $e_i$ is rejected (creates cycle)
- $T$ unchanged, still promising
- The MCST extending $T$ couldn't have used $e_i$ anyway (would create cycle)


---

# Proof: Case 2 - Edge Accepted

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If our chosen $e_i$ is already in the witness MCST, we're done — otherwise we'll need to *swap*.

</div>

$e_i$ is accepted. Must show $T \cup \{e_i\}$ is promising.

Since $T$ is promising, there exists MCST $T_1$ with $T \subseteq T_1$.


**Subcase a:** $e_i \in T_1$
- Then $T \cup \{e_i\} \subseteq T_1$, so $T \cup \{e_i\}$ is promising ✓

**Subcase b:** $e_i \notin T_1$
- Use the **Exchange Lemma**!


---

# Exchange Lemma

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two spanning trees can be transformed into each other one edge at a time — the swap that powers the proof.

</div>

**Lemma:** Let $G$ be connected, $T_1$ and $T_2$ be spanning trees. For every edge $e \in T_2 - T_1$, there exists $e' \in T_1 - T_2$ such that $T_1 \cup \{e\} - \{e'\}$ is a spanning tree. <span style="font-size: 0.6em; color: navy;">Lem 2.11, Pg 39, lem:exch</span>


```
    T₁                    T₂
   ┌───────────┐    ┌───────────┐
   │     ●     │    │     ●     │
   │    /      │    │      \    │
   │   ● e'    │    │    e  ●   │
   │           │    │           │
   └───────────┘    └───────────┘
```


**Idea:** Adding $e$ to $T_1$ creates a cycle; some edge $e'$ in that cycle must be in $T_1 - T_2$


---

# Completing the Proof

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Sorting + the exchange lemma forces $c(e_i) \leq c(e_j)$, so swapping doesn't make things worse.

</div>

**Subcase b continued:** $e_i \notin T_1$


- By Exchange Lemma: $\exists e_j \in T_1 - T_2$ such that $T_3 = (T_1 \cup \{e_i\}) - \{e_j\}$ is a spanning tree
- Key observation: $i < j$ (otherwise $e_j$ would have been rejected earlier, forming a cycle in $T$)
- Since edges are sorted: $c(e_i) \leq c(e_j)$
- Therefore: $c(T_3) \leq c(T_1)$
- So $T_3$ is also a MCST!
- Since $T \cup \{e_i\} \subseteq T_3$, we have $T \cup \{e_i\}$ is promising ✓


---

# Example Run

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Watch the *witness MCST* — the one extending $T$ — change as edges get accepted or rejected.

</div>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Sorting dominates with the simple components array; better data structures buy us $O(m \log n)$.

</div>


1. **Sorting edges:** $O(m \log m)$ or $O(m^2)$ with insertion sort
2. **Main loop:** $m$ iterations
3. **Cycle check:** $O(1)$ using component array
4. **Merge components:** $O(n)$ per merge, at most $n-1$ merges

**Total:** $O(m \log m + mn)$ or with better data structures: $O(m \log n)$


---

# Key Problems

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Trace, prove, implement — five problems that lock in every part of the lecture.

</div>


1. **Problem 2.4:** Prove that every tree with $n$ nodes has $n-1$ edges <span style="font-size: 0.6em; color: navy;">Prb 2.4, Pg 34, exr:cycles</span>

2. **Problem 2.5:** Trace Kruskal's algorithm on a given graph <span style="font-size: 0.6em; color: navy;">Prb 2.5, Pg 35, exr:kruskal-run</span>

3. **Problem 2.12:** If $e_1$ has strictly smallest cost, show every MCST includes $e_1$ <span style="font-size: 0.6em; color: navy;">Prb 2.12, Pg 39, exr:exch_lem</span>

4. **Problem 2.13:** Show that the smallest edge is in every MCST <span style="font-size: 0.6em; color: navy;">Prb 2.13, Pg 39, exr:kruskal_smallest_edge</span>

5. **Problem 2.15:** Implement Kruskal's algorithm <span style="font-size: 0.6em; color: navy;">Prb 2.15, Pg 39, exr:kruskal_program</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Problems/P2.15_Kruskal-Program.py" style="font-size: 0.6em; color: teal;">[Python solution]</a>


---

# Next: Jobs with Deadlines and Profits

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Same proof template, totally different problem — same template, *different swap*.

</div>

Another greedy algorithm where "promising" is the key invariant!

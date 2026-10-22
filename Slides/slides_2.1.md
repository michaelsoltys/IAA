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

# Finding a Path

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A large graph. One path from the top-left corner to the bottom-right, in green.

</div>

<img src="./Figures/grid-path.svg" style="width: 100%; max-height: 420px;" alt="Grid graph with a green path from the top-left node to the bottom-right node" />

---

# Reachability, Then Distances

<div style="color: #9ca3af; font-style: italic; font-size: 0.85em; margin-bottom: 0.5em;">

Unweighted: BFS is linear. Weighted shortest paths sat at Dijkstra for decades, then broke.

</div>

<div style="font-size: 0.78em; text-align: left;">

| Year | Result | Bound |
|------|--------|-------|
| 1959 | BFS (Moore); Dijkstra | unweighted $O(m+n)$; later $O(m + n\log n)$ with Fibonacci heaps |
| 1999 | Thorup, undirected *integers* | $O(m+n)$ in the RAM model |
| 2023 | Duan–Mao–Shu–Yin, undirected *reals* | $O\bigl(m\sqrt{\log n\,\log\log n}\bigr)$, first break of Dijkstra |
| 2025 | Duan–Mao–Mao–Shu–Yin, *directed* | $O(m\log^{2/3}n)$ |
| **2026** | **Kadria–Roditty, undirected reals** | $O\bigl(m\sqrt{\log n}\,(\log\log n\cdot\log\log\log n)^{1/4}\bigr)$ |

</div>

<div style="font-size: 0.72em; text-align: left; margin-top: 0.4em;">

Latest: first improvement since FOCS 2023, by a factor $(\log\log n / \log\log\log n)^{1/4}$, via a nearest-sample distance tool. <a href="https://arxiv.org/abs/2609.15247" style="color: teal;">arXiv:2609.15247</a>

</div>

---

# Graph Representation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

A $1$ where there is an edge. Concatenate the rows and you have the input string $s_G \in \{0,1\}^{n^2}$.

</div>

$$A_G[i,j] = \begin{cases} 1 & \text{if } (i,j) \in E \\ 0 & \text{otherwise} \end{cases}$$

<img src="./Figures/graph-representation.drawio.svg" class="mx-auto block" style="width: 100%; max-height: 390px;" alt="Five-vertex house graph and its 5 by 5 adjacency matrix" />

---

# Graph Definitions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.4em;">

The vocabulary — paths, cycles, connected, tree, spanning tree — that we'll use for every graph algorithm.

</div>

<img src="./Figures/graph-definitions.drawio.svg" class="mx-auto block" style="width: 100%; max-height: 460px;" alt="Eight graph definitions, each with a four-vertex diagram: undirected, degree, path, connected, cycle, acyclic, tree, spanning tree" />

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

Pick $n-1$ edges that connect everything *and* minimize total cost — the classic network-design problem.

</div>

<div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 1.4rem; align-items: center; text-align: left;">

<div>

**Setup:**
- Graph $G = (V, E)$ with cost $c: E \rightarrow \mathbb{R}^+$
- Total cost: $c(T) = \sum_{e \in T} c(e)$

**Definition:** $T$ is a **Minimum Cost Spanning Tree (MCST)** if:
1. $T$ is a spanning tree for $G$
2. For any other spanning tree $T'$: $c(T) \leq c(T')$

**Goal:** Find a MCST for $G$

</div>

<img src="./Figures/house-spanning.drawio.svg" style="width: 100%; max-height: 390px;" alt="House graph G and one spanning tree T on the same five vertices" />

</div>

---

# Kruskal's Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

Sort edges cheap-to-expensive and add each one *unless it would close a cycle*.

</div>

<div style="display: grid; grid-template-columns: 0.85fr 1.25fr; gap: 1.2rem; align-items: center; text-align: left;">

<div>

<span style="font-size: 0.6em; color: navy;">Alg 10, Pg 35, alg:kruskal</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Algorithms/A10_Kruskal.py" style="font-size: 0.6em; color: teal;">[Python implementation]</a>

Kruskal's Algorithm:
```text
Sort: c(e₁) ≤ … ≤ c(eₘ)
T ← ∅
for i = 1 to m:
   if T ∪ {eᵢ} has no cycle:
      T ← T ∪ {eᵢ}
return T
```
In words, order edges by cost, starting with cheapest; keep adding edges unless adding an edge creates a cycle.

</div>

<img src="./Figures/kruskal-hat.drawio.svg" style="width: 100%; max-height: 400px;" alt="Kruskal on the house graph: add the two roof edges, skip the ceiling, add the two walls, skip the floor" />

</div>

---

# Cycle Detection with Connected Components

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

Same $D$ value means same component. A cycle is just $D[r] = D[s]$.

</div>

<div style="display: grid; grid-template-columns: 0.85fr 1.25fr; gap: 1.2rem; align-items: center; text-align: left;">

<div>

- $D[i] = j$ means vertex $i$ is in component $V_j$
- Init: $D[i] \leftarrow i$
- $e_i = (r,s)$ forms cycle iff $D[r] = D[s]$

**Merge** (when adding $(r,s)$): 

<span style="font-size: 0.6em; color: navy;">Alg 11, Pg 35, alg:component</span>

```text
k ← D[r]
l ← D[s]
for j = 1 to n:
    if D[j] = l:
        D[j] ← k
```

</div>

<img src="./Figures/kruskal-components.drawio.svg" style="width: 100%; max-height: 400px;" alt="Kruskal on the hat graph, nodes colored by connected component, with the D array under each step" />

</div>

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

# Exchange Lemma

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

Adding $e$ to $T_1$ creates a cycle; some edge $e'$ on that cycle lies in $T_1 - T_2$.

</div>

**Lemma:** Let $G$ be connected, $T_1$ and $T_2$ be spanning trees. For every $e \in T_2 - T_1$ there is an $e' \in T_1 - T_2$ such that $T_1 \cup \{e\} - \{e'\}$ is a spanning tree. <span style="font-size: 0.6em; color: navy;">Lem 2.11, Pg 39, lem:exch</span>

<img src="./Figures/exchange-lemma.drawio.svg" class="mx-auto block" style="width: 100%; max-height: 380px;" alt="Three spanning trees of a 4-cycle: add e from T2 to T1, forming a cycle, then drop e-prime from T1 minus T2" />

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

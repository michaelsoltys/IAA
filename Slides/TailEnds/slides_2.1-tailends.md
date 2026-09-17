---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 2.1: Kruskal promising proof (tail)
  Pulled from slides_2.1.md. Not in the main lecture.
drawings:
  persist: false
transition: slide-left
title: Kruskal, the promising proof
mdc: false
---

# Kruskal: the promising proof

Section 2.1, slides held out of the main deck

<div style="color: #9ca3af; font-size: 0.85em; margin-top: 1.2em;">

Promising invariant, the accept case, completing the swap, and a witness-MCST trace.

</div>

---

# The "Promising" Property

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The central idea: at every step, our partial $T$ can still be completed to *some* MCST — keep this true and we win.

</div>

**Definition:** A set $T$ of edges is **promising** if it can be extended to a MCST.


**Theorem:** "$T$ is promising" is a loop invariant for Kruskal's algorithm. <span style="font-size: 0.6em; color: navy;">Lem 2.10, Pg 37, lem:promising</span>


**Why this matters:** After the algorithm terminates, $T$ is promising AND all edges have been considered → $T$ must itself be a MCST!

<!--
The same "promising" argument is the reason greedy works on matroids. Whitney defined matroids in 1935; Edmonds showed in the 1960s that the greedy algorithm is optimal precisely on those structures. Graphic matroids (forests of a graph) are the example sitting in this lecture. Kruskal is the special case you can prove with one exchange lemma and no matroid language.
-->

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

---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 3.3: Savitch's Algorithm
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: "Savitch's Algorithm"
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

# Savitch's Algorithm

Section 3.3 - Savitch's Algorithm

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# The Problem: Graph Reachability

Given a directed graph $G$ and two nodes $s$ and $t$:

**Question:** Is there a path from $s$ to $t$?

<v-click>

We're not looking for the *shortest* path — just whether $t$ is **reachable** from $s$.

</v-click>

<v-click>

**Twist:** We want to minimize **space** (memory), not time!

</v-click>

---

# Why Care About Space?

The graph may be given **implicitly**, not explicitly.

<v-click>

**Example:** The World Wide Web
- $V$ = all web pages
- $(x, y) \in E$ if page $x$ has a hyperlink to page $y$
- The graph is **enormous** — we can't store it all in memory
- We query pages piecemeal

</v-click>

<v-click>

Savitch's algorithm solves reachability in space $O(\log^2 n)$ — remarkably small!

</v-click>

---

# The Key Idea

Define $\text{R}(G, u, v, i)$ = true iff there is a path from $u$ to $v$ of length $\leq 2^i$

<v-click>

**Recursive insight:** If a path exists from $u$ to $v$, it must have a **midpoint** $w$:

$$\text{R}(G, u, v, i) \iff (\exists w)[\text{R}(G, u, w, i-1) \wedge \text{R}(G, w, v, i-1)]$$

</v-click>

<v-click>

A path of length $\leq 2^i$ can be split into two paths of length $\leq 2^{i-1}$

</v-click>

---

# Savitch's Algorithm

<span style="font-size: 0.6em; color: navy;">Alg 19, Pg 68, alg:savitch</span>

```text
R(G, u, v, i):
  if i = 0:
    if u = v: return true
    elif (u, v) is an edge: return true
  else:
    for every vertex w:
      if R(G, u, w, i-1) and R(G, w, v, i-1):
        return true
  return false
```

<v-click>

**To solve reachability:** Call $\text{R}(G, s, t, \lceil \log_2 n \rceil)$

since any path in an $n$-node graph has length $\leq n \leq 2^{\lceil \log_2 n \rceil}$

</v-click>

---

# Example: Recursion Stack

Graph: $1 — 2 — 3 — 4$ (path of 4 nodes)

Query: $\text{R}(1, 4, 2)$ — is there a path of length $\leq 4$?

| Step 1 | Step 2 | Step 3 | Step 4 | Step 5 | Step 6 |
|:------:|:------:|:------:|:------:|:------:|:------:|
|        |        | R(1,4,0) | **F** | R(2,4,0) | **F** |
|        |        | R(1,1,0) | **T** | R(1,2,0) | **T** |
|        | R(1,4,1) | R(1,4,1) | R(1,4,1) | R(1,4,1) | R(1,4,1) |
|        | R(1,1,1) | R(1,1,1) | R(1,1,1) | R(1,1,1) | R(1,1,1) |
| R(1,4,2) | R(1,4,2) | R(1,4,2) | R(1,4,2) | R(1,4,2) | R(1,4,2) |

<v-click>

The stack grows **downward** (depth) but reuses space at each level!

</v-click>

---

# Space Analysis

**Why $O(\log^2 n)$ space?**

<v-clicks>

- The recursion depth is at most $i \leq \lceil \log_2 n \rceil$
- At each level, we store one vertex $w$ — takes $s = O(\log n)$ bits
- **Total space:** $i \cdot s = O(\log n) \cdot O(\log n) = O(\log^2 n)$

</v-clicks>

<v-click>

**The trick:** The two recursive calls $\text{R}(G, u, w, i-1)$ and $\text{R}(G, w, v, i-1)$ are made **sequentially**, not in parallel — so the same stack space is reused!

</v-click>

---

# Time Complexity

<v-click>

What's the **time** cost of this space savings?

</v-click>

<v-click>

At each level $i$, we try all $n$ possible midpoints $w$, and each leads to two recursive calls at level $i - 1$:

$$T(n, i) \leq n \cdot 2 \cdot T(n, i-1)$$

</v-click>

<v-click>

This gives exponential time — $O(n^{2 \log n})$ — a huge cost for tiny space!

**Savitch's algorithm trades time for space.**

</v-click>

---

# Key Questions

<v-clicks>

1. **Problem 3.7:** Prove that Savitch's algorithm correctly computes $\text{R}(G, u, v, i)$ and uses at most $i \cdot s$ space. Conclude $O(\log^2 n)$ space. <span style="font-size: 0.6em; color: navy;">Prb 3.7, Pg 67, exr:savitch1</span>

2. **Problem 3.8:** What is the exact time complexity of Savitch's algorithm? <span style="font-size: 0.6em; color: navy;">Prb 3.8, Pg 67, prb:savitchtime</span>

3. **Problem 3.9:** Implement Savitch's algorithm so that at each step it outputs the contents of the recursion stack. <span style="font-size: 0.6em; color: navy;">Prb 3.9, Pg 67, exr:savitch-program</span>

</v-clicks>

---

# Bonus: Quicksort & Git Bisect

Two more divide and conquer ideas from Section 3.4:

<v-clicks>

**Quicksort** — pick a pivot, partition, recurse:
```haskell
qsort [] = []
qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
  where
    smaller = [a | a <- xs, a <= x]
    larger  = [b | b <- xs, b > x]
```

**Git bisect** — binary search through commit history to find which commit introduced a bug. A practical application of divide and conquer!

</v-clicks>

---

# Summary

<v-clicks>

- **Savitch's algorithm** solves graph reachability in $O(\log^2 n)$ space
- **Key idea:** A path of length $\leq 2^i$ has a midpoint splitting it into two paths of length $\leq 2^{i-1}$
- **Space trick:** Sequential (not parallel) recursive calls allow stack reuse
- **Trade-off:** Exponential time for logarithmic space
- **Motivation:** Implicitly represented graphs (e.g., the WWW)

</v-clicks>

---

# Chapter 3 Complete

Divide and Conquer key takeaways:
- **Mergesort:** $O(n \log n)$ sorting via split-merge
- **Karatsuba:** $O(n^{1.59})$ multiplication via reducing recursive calls
- **Savitch:** $O(\log^2 n)$ space via midpoint recursion

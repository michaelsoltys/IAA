---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 4.2: All Pairs Shortest Path
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: All Pairs Shortest Path Problem
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

# All Pairs Shortest Path

Section 4.2 - Dynamic Programming

---
layout: section
---

# Graph Reachability Algorithms

A Journey Through 50+ Years of Algorithm Design

---

# The Golden Age: 1950s-1960s

**BFS & DFS (1950s)** - The Classics

<v-clicks>

- Among the **oldest** algorithms in computer science
- Independently discovered by multiple researchers
- DFS naturally emerges from maze-solving strategies used since ancient times
- BFS guarantees **shortest path** by number of hops
- Both are still the **go-to** algorithms for practical graph traversal today
- The "queue vs stack" distinction between BFS and DFS is one of the most elegant examples of how a single data structure choice completely changes algorithm behavior!

</v-clicks>

---

# The Dutch Master: Dijkstra (1959)

**Edsger W. Dijkstra** - One of computer science's most influential figures

<v-clicks>

- Created while designing shortest routes for the Amsterdam public transport system
- Dijkstra famously wrote: "What is the shortest way to travel from Rotterdam to Groningen?"
- Designed the algorithm **in 20 minutes** without pencil and paper!
- Published in 1959, just 3 pages long
- Still used today in GPS navigation, network routing (OSPF protocol), and more
- Dijkstra was known for his strong opinions - he famously said "GOTO considered harmful" and refused to use BASIC because he thought it would "mutilate the minds" of students!

</v-clicks>

---

# The Bellman-Ford Alliance (1958)

**Richard Bellman** and **Lester Ford Jr.** - Independent discoveries

<v-clicks>

- Developed independently around the same time
- Bellman (of "dynamic programming" fame) published in 1958
- Ford published independently in 1956
- **Key advantage:** Can handle **negative edge weights**!
- Used in distance-vector routing protocols
- Bellman coined the term "dynamic programming" to hide mathematical research from a Secretary of Defense who "had a pathological fear of the word 'research'"

</v-clicks>

---

# The Floyd-Warshall Saga (1962)

**Three minds, one algorithm!**

<v-clicks>

- **Bernard Roy** (1959) - Published first but in French, largely unknown
- **Robert Floyd** (1962) - Popularized in English-speaking world
- **Stephen Warshall** (1962) - Boolean version (transitive closure)
- Floyd's version: one page, crystal clear
- Warshall's version: computes reachability instead of distances
- Sometimes called the "Roy-Floyd-Warshall" algorithm to credit all three discoverers
- Floyd was also famous for "Floyd's cycle-finding algorithm" (the tortoise and hare)

</v-clicks>

---

# The Space Complexity Revolution: Savitch (1970)

**Walter Savitch** - Trading time for space

<v-clicks>

- PhD thesis work at UC Berkeley
- **Savitch's Theorem:** NSPACE($f(n)$) ⊆ DSPACE($f(n)^2$)
- Shows directed reachability in $O(\log^2 n)$ space!
- Time complexity: $2^{O(\log n)} = n^{O(1)}$ but **exponential**
- Proves NL ⊆ SPACE($\log^2 n$)
- Rarely used in practice (too slow!) but **fundamental to complexity theory**
- Taught because it's beautiful and theoretically important, not because you'd ever actually use it!

</v-clicks>

---

# The 21st Century Breakthrough: Reingold (2005)

**Omer Reingold** - Solving a 30+ year old open problem

<v-clicks>

- Proved undirected reachability in L (logarithmic space!)
- Resolved question open since the 1970s
- Won the **Gödel Prize** in 2008
- Uses sophisticated derandomization techniques
- Space: $O(\log n)$ - better than Savitch's $O(\log^2 n)$!
- **Limitation:** Only works for **undirected** graphs
- **Open Question:** Is directed reachability in L? (The **L vs NL** problem)
- Reingold's proof uses "zig-zag products" of graphs - a technique borrowed from expander graph theory
- The paper is notoriously difficult but the result is stunning!

</v-clicks>

---

# Modern Era: Practical Speedups

**Beyond the classics - modern developments**

<v-clicks>

**A* Algorithm (1968)** - Hart, Nilsson, Raphael
- Dijkstra with heuristics
- Used in games, robotics, GPS systems
- Can be **orders of magnitude** faster than Dijkstra

**Johnson's Algorithm (1977)** - All-pairs for sparse graphs
- Combines Bellman-Ford and Dijkstra
- Better than Floyd-Warshall for sparse graphs: $O(n^2 \log n + nm)$

**Fast Matrix Multiplication** (1969-present)
- Strassen (1969): $O(n^{2.807})$
- Current record: $O(n^{2.3728596})$ (2024)
- Theoretical: Can we reach $O(n^2)$?

</v-clicks>

---

# The Complexity Theory Connection

**Why study impractical algorithms?**

<v-clicks>

**Savitch's Algorithm** - Foundation of space complexity
- Defines the relationship between deterministic and nondeterministic space
- Central to understanding **NL-complete** problems

**The Hierarchy:**
- **L** (Logarithmic Space): Undirected reachability [Reingold, 2005]
- **NL** (Nondeterministic Log Space): Directed reachability
- **P** (Polynomial Time): BFS, DFS, Dijkstra, Floyd-Warshall
- **NP**: Where intractable problems live

**Great Open Problems:**
- Is L = NL? (Equivalent to: Is directed reachability in L?)
- Is P = NP? (The million-dollar question!)

</v-clicks>

---

# Algorithm Personalities

Different algorithms for different needs:

<v-clicks>

**The Workhorse (BFS/DFS):** Simple, fast, everyone's first choice
- "I just want to know if there's a path!"

**The Navigator (Dijkstra):** Practical and efficient
- "I need the shortest route from here to everywhere"

**The Completionist (Floyd-Warshall):** Does it all at once
- "I need shortest paths between ALL pairs of cities"

**The Pessimist (Bellman-Ford):** Handles the worst cases
- "What if some roads have negative costs?"

**The Minimalist (Savitch):** Survives on almost nothing
- "I only have log-squared memory available!"

**The Theorist (Reingold):** Pushing boundaries
- "I can do it in logarithmic space... for undirected graphs!"

</v-clicks>

---

# Real-World Applications Today

Where these algorithms live in modern systems:

<v-clicks>

**Internet Routing (OSPF, BGP):** Dijkstra variants
- Your packets reach their destination using these algorithms!

**GPS Navigation:** A*, Dijkstra with preprocessing
- Google Maps, Waze, Apple Maps

**Social Networks:** BFS for friend recommendations
- "People you may know" - 2 or 3 hops away

**Compilers:** DFS for dependency analysis
- Topological sorting of build tasks

**Databases:** Transitive closure (Warshall)
- "Find all employees reporting to this manager"

**Web Crawlers:** BFS for systematic page discovery
- How Google indexes the web

</v-clicks>

---

# Timeline of Discoveries

| Year | Algorithm | Discoverer(s) | Breakthrough |
|------|-----------|---------------|--------------|
| 1950s | BFS, DFS | Multiple | Foundation of graph traversal |
| 1956 | Bellman-Ford | Bellman, Ford | Negative edges |
| 1959 | Dijkstra | Dijkstra | Greedy shortest path |
| 1962 | Floyd-Warshall | Roy, Floyd, Warshall | All-pairs shortest paths |
| 1968 | A* | Hart, Nilsson, Raphael | Heuristic search |
| 1970 | Savitch | Savitch | Space complexity bound |
| 1977 | Johnson | Johnson | Sparse all-pairs |
| 2005 | Reingold | Reingold | L-space undirected reach |

<v-click>

**50+ years of continuous innovation!**

</v-click>

---
layout: section
---

# Now Let's Dive Into Floyd-Warshall

Understanding the All Pairs Shortest Path Algorithm

---

# Problem Definition

**Input:**
- Directed graph $G = (V, E)$ with $V = \{1, 2, \ldots, n\}$
- Cost function $C(i,j) \in \mathbb{N}^+ \cup \{\infty\}$ for all $1 \leq i, j \leq n$
- $C(i,j) = \infty$ if $(i,j)$ is not an edge

**Output:**
- Array $D$ where $D(i,j)$ is the length of the shortest directed path from $i$ to $j$

---

# Directed Graphs

<v-clicks>

- A **directed graph** (or **digraph**) has edges with direction (arrows)
- Different from undirected graphs (Section 2.1 - Minimum Cost Spanning Trees)
- Edge $(i,j)$ goes **from** $i$ **to** $j$ (not bidirectional unless both $(i,j)$ and $(j,i)$ exist)
- Many real-world applications: road networks, networks with one-way links, dependencies

</v-clicks>

---

# Why Not Exhaustive Search?

**Exercise 4.5:** Construct a family of graphs $\{G_n\}$ where:
- $G_n$ has $O(n)$ nodes
- But $\Omega(2^n)$ paths (exponentially many!)

<v-click>

**Example:** "Diamond Chain" graph with 3 layers:

```text
        ┌─── v₁ ───┐     ┌─── v₃ ───┐     ┌─── v₅ ───┐
    s ──┤          ├── ○ ┤          ├── ○ ┤          ├── t
        └─── v₂ ───┘     └─── v₄ ───┘     └─── v₆ ───┘

        Layer 1          Layer 2          Layer 3
```

At each layer: choose top or bottom path → $2 \times 2 \times 2 = 2^3 = 8$ paths

With $n$ layers: $2^n$ paths but only $2n + 2$ nodes

</v-click>

<v-click>

**Conclusion:** Exhaustive search is **not feasible**!

</v-click>

---

# Dynamic Programming Approach

## Step 1: Define Subproblems

Let $A(k, i, j)$ = length of the shortest path from $i$ to $j$ where all **intermediate** nodes are in $\{1, 2, \ldots, k\}$

<v-clicks>

- When $k = 0$: $\{1, 2, \ldots, k\} = \emptyset$ (no intermediate nodes allowed)
- When $k = n$: $A(n, i, j) = D(i, j)$ is our solution

</v-clicks>

---

# Understanding Intermediate Nodes

Consider a path from node $i$ to node $j$:

<v-click>

$$i \rightarrow a_1 \rightarrow a_2 \rightarrow \cdots \rightarrow a_m \rightarrow j$$

</v-click>

<v-click>

- Nodes $a_1, a_2, \ldots, a_m$ are **intermediate** nodes
- Nodes $i$ and $j$ are **endpoints** (not intermediate)
- $A(k, i, j)$ restricts intermediate nodes to $\{1, 2, \ldots, k\}$

</v-click>

<v-click>

**Example:** $A(3, 5, 7)$ = shortest path from 5 to 7 where intermediate nodes (if any) come from $\{1, 2, 3\}$

</v-click>

---

# Step 2: Find the Recurrence

**Initialization:** $A(0, i, j) = C(i, j)$ (no intermediate nodes allowed)

<v-click>

**Recursive case** for $k > 0$:

Consider whether node $k$ is on the shortest path from $i$ to $j$

</v-click>

<v-clicks>

**Case 1:** Node $k$ is **not** on the path
- Shortest path uses only nodes $\{1, \ldots, k-1\}$
- Therefore: $A(k, i, j) = A(k-1, i, j)$

**Case 2:** Node $k$ **is** on the path
- Path goes: $i \rightsquigarrow k \rightsquigarrow j$
- Node $k$ appears exactly once (no benefit to revisiting)
- Therefore: $A(k, i, j) = A(k-1, i, k) + A(k-1, k, j)$

</v-clicks>

---

# The Recurrence Formula

Take the minimum of both cases:

$$A(k, i, j) = \min\{A(k-1, i, j), \; A(k-1, i, k) + A(k-1, k, j)\}$$

<v-clicks>

**Intuition:**
- Should we route through node $k$ or not?
- Try both options and pick the cheaper one
- This exhibits **optimal substructure** (key property for DP)

**Why does $k$ appear exactly once?**
- If $k$ appears twice, we have a cycle involving $k$
- Since costs are positive, cycles increase cost (never optimal)

</v-clicks>

---

# Step 3: The Algorithm

```text
Floyd-Warshall Algorithm:
  // Initialize with direct edge costs
  for i = 1 to n:
    for j = 1 to n:
      B(i,j) ← C(i,j)

  // Consider each node k as potential intermediate
  for k = 1 to n:
    for i = 1 to n:
      for j = 1 to n:
        B(i,j) ← min{B(i,j), B(i,k) + B(k,j)}

  return D ← B
```

---

# The Space-Saving Trick

**Observation:** We only need a **2D array** $B(i,j)$, not 3D!

<v-click>

We can **overwrite** $A(k-1, *, *)$ to compute $A(k, *, *)$

```text
// Before iteration k:  B(i,j) = A(k-1, i, j)
for k = 1 to n:
  for i = 1 to n:
    for j = 1 to n:
      B(i,j) ← min{B(i,j), B(i,k) + B(k,j)}
// After iteration k:   B(i,j) = A(k, i, j)
```

</v-click>

<v-click>

Reduces space from $O(n^3)$ to $O(n^2)$!

</v-click>

---

# Why Does Overwriting Work?

**Concern:** When we compute `B(i,j) ← min{B(i,j), B(i,k) + B(k,j)}`, we might use already-updated values!

<v-click>

**Answer:** The overwriting is **safe** because:

1. We're computing $A(k, i, j)$ for all $i,j$ in iteration $k$
2. We use values $B(i,k)$ and $B(k,j)$
3. These represent paths **to/from** node $k$
4. Such paths **cannot use $k$ as intermediate** (would create cycle with $k$)
5. So $B(i,k) = A(k-1, i, k) = A(k, i, k)$ (adding $k$ doesn't help)
6. Similarly $B(k,j) = A(k-1, k, j) = A(k, k, j)$

</v-click>

<v-click>

**Bottom line:** Whether we read old or new values of $B(i,k)$ and $B(k,j)$, they're the same!

</v-click>

---

# Alternative: Using Two Arrays

Could avoid overwriting entirely:

```text
for k = 1 to n:
  for i = 1 to n:
    for j = 1 to n:
      A_new(i,j) ← min{A_old(i,j), A_old(i,k) + A_old(k,j)}
  A_old ← A_new
```

<v-clicks>

- Uses $O(n^2)$ additional space
- Conceptually clearer (no overwriting concerns)
- Same time complexity $O(n^3)$
- Floyd's single-array version is more elegant and space-efficient

</v-clicks>

---

# Example: 3×3 Grid Graph

```text
1 — 2 — 3
|   |   |
4 — 5 — 6
|   |   |
7 — 8 — 9
```

<v-click>

Assume all edges have cost 1 and are **bidirectional** (so both $(i,j)$ and $(j,i)$ exist)

Let's trace the algorithm step by step

</v-click>

---

# Example: Initialization (k=0)

$A(0, i, j) = C(i, j)$ - direct edge costs

Selected entries (using $\infty$ for no edge):

| From $\backslash$ To | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|--:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **1** | 0 | 1 | $\infty$ | 1 | $\infty$ | $\infty$ | $\infty$ | $\infty$ | $\infty$ |
| **2** | 1 | 0 | 1 | $\infty$ | 1 | $\infty$ | $\infty$ | $\infty$ | $\infty$ |
| **5** | $\infty$ | 1 | $\infty$ | 1 | 0 | 1 | $\infty$ | 1 | $\infty$ |
| **9** | $\infty$ | $\infty$ | $\infty$ | $\infty$ | $\infty$ | 1 | $\infty$ | 1 | 0 |

---

# Example: After k=1

Now paths can use node 1 as intermediate

**Key updates:**
- $A(1, 2, 4) = \min\{\infty, A(0,2,1) + A(0,1,4)\} = \min\{\infty, 1+1\} = 2$
  - New path: $2 \to 1 \to 4$

<v-click>

Nodes 2 and 4 can now reach each other via node 1!

| From $\backslash$ To | 1 | 2 | 3 | 4 | ... |
|--:|:-:|:-:|:-:|:-:|:-:|
| **2** | 1 | 0 | 1 | **2** | ... |
| **4** | 1 | **2** | $\infty$ | 0 | ... |

</v-click>

---

# Example: After k=2

Now paths can use nodes $\{1, 2\}$ as intermediates

**More updates:**
- $A(2, 1, 3) = \min\{\infty, A(1,1,2) + A(1,2,3)\} = \min\{\infty, 1+1\} = 2$
  - Path: $1 \to 2 \to 3$
- $A(2, 1, 5) = \min\{\infty, A(1,1,2) + A(1,2,5)\} = \min\{\infty, 1+1\} = 2$
  - Path: $1 \to 2 \to 5$

<v-click>

Distances from node 1 to distant nodes decrease as we allow more intermediates

</v-click>

---

# Example: After k=9

After all 9 iterations, we have the complete shortest path matrix:

| From $\backslash$ To | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|--:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **1** | 0 | 1 | 2 | 1 | 2 | 3 | 2 | 3 | 4 |
| **5** | 2 | 1 | 2 | 1 | 0 | 1 | 2 | 1 | 2 |
| **9** | 4 | 3 | 2 | 3 | 2 | 1 | 2 | 1 | 0 |

<v-click>

For example: $D(1,9) = 4$
- Shortest path from 1 to 9 has length 4
- One such path: $1 \to 2 \to 5 \to 8 \to 9$

</v-click>

---

# Algorithm Analysis

**Time Complexity:** $O(n^3)$
- Three nested loops, each running $n$ times
- Each iteration does constant work

<v-click>

**Space Complexity:** $O(n^2)$
- Single $n \times n$ matrix $B$
- Input graph also takes $O(n^2)$ space

</v-click>

<v-click>

**Remarkable properties:**
- Graph may have up to $O(n^2)$ edges
- Algorithm runs in $O(n^3)$ time
- Very efficient for **dense graphs**
- Simple and elegant implementation

</v-click>

---

# Correctness

**Pre-condition:**
- Valid directed graph $G=(V,E)$
- Cost function $C$ with $C(i,j) \in \mathbb{N}^+ \cup \{\infty\}$
- $C(i,i) = 0$ for all $i$ (optional: can be handled)

<v-click>

**Post-condition:**
- $D(i,j)$ contains length of shortest path from $i$ to $j$
- If no path exists, $D(i,j) = \infty$

</v-click>

---

# Loop Invariant

**Invariant (for outer loop on $k$):**

After iteration $k$, for all $i, j$:
$$B(i,j) = A(k, i, j)$$

That is: $B(i,j)$ contains the shortest path from $i$ to $j$ using only nodes $\{1, \ldots, k\}$ as intermediates

<v-clicks>

**Proof sketch:**
- **Base case** ($k=0$): $B(i,j) = C(i,j) = A(0,i,j)$ ✓
- **Inductive step:** If true for $k-1$, the recurrence correctly computes $A(k,i,j)$
- **Termination:** When $k=n$, we have $B(i,j) = A(n,i,j) = D(i,j)$ ✓

</v-clicks>

---
layout: section
---

# Bellman-Ford Algorithm

A Different Dynamic Programming Approach

---

# Bellman-Ford Algorithm

**Problem:** Find shortest path from $s$ to $t$ in directed graph

**Different DP formulation:**
- Let $\text{opt}(i,v)$ = minimal cost of an **$i$-path** from $v$ to $t$
- An $i$-path uses **at most** $i$ edges

<v-click>

**Recurrence:** For $i > 0$:
$$\text{opt}(i,v) = \min\{\text{opt}(i-1,v), \; \min_{w \in V}\{c(v,w) + \text{opt}(i-1,w)\}\}$$

</v-click>

<v-clicks>

- **Case 1:** Optimal path uses $< i$ edges: $\text{opt}(i-1,v)$
- **Case 2:** Optimal path uses exactly $i$ edges via edge $(v,w)$: $c(v,w) + \text{opt}(i-1,w)$

</v-clicks>

---

# Bellman-Ford vs Floyd

Key differences:

| Aspect | Floyd-Warshall | Bellman-Ford |
|--------|---------------|--------------|
| **Scope** | All pairs | Single source to single target |
| **DP Parameter** | Intermediate nodes $\leq k$ | Number of edges $\leq i$ |
| **Complexity** | $O(n^3)$ | $O(n \cdot m)$ where $m$ = \|edges\| |
| **Best for** | Dense graphs, all pairs | Sparse graphs, single source |
| **Negative edges** | Not designed for them | Can handle negative edges! |

---

# When to Use Each Algorithm

<v-clicks>

**Use Savitch:**
- Only need reachability (yes/no)
- Graph is huge (e.g., WWW)
- Memory is extremely limited

**Use Dijkstra:**
- Single source shortest paths
- Non-negative edge weights
- Need fast practical solution

**Use Bellman-Ford:**
- Single source shortest paths
- May have negative edge weights (but no negative cycles)
- Sparse graphs

**Use Floyd-Warshall:**
- Need all pairs shortest paths
- Dense graphs or moderate size
- Simple implementation desired

</v-clicks>

---
layout: section
---

# Other Known Reachability Algorithms

A Survey of Classical and Modern Approaches

---

# The Reachability Problem Landscape

The reachability problem is **ubiquitous** in computer science!

<v-click>

**Basic Question:** Given graph $G$ and nodes $s$, $t$, is there a path from $s$ to $t$?

</v-click>

<v-clicks>

**Key Variations:**
- Directed vs. Undirected graphs
- Simple reachability vs. shortest path
- Time complexity vs. space complexity trade-offs
- Deterministic vs. nondeterministic models

</v-clicks>

---

# Classical Graph Traversal: BFS

**Breadth-First Search (BFS)**

**Approach:** Explore nodes level by level from source $s$

```text
BFS(G, s, t):
  queue ← {s}
  visited ← {s}

  while queue is not empty:
    u ← dequeue(queue)
    if u = t:
      return true

    for each neighbor v of u:
      if v not in visited:
        visited ← visited ∪ {v}
        enqueue(queue, v)

  return false
```

---

# BFS Properties

<v-clicks>

**Time Complexity:** $O(n + m)$ where $n$ = vertices, $m$ = edges
- Visit each vertex once
- Examine each edge once

**Space Complexity:** $O(n)$
- Queue can hold up to $n$ vertices
- Visited set has $n$ entries

**Advantages:**
- Very practical and efficient
- Finds **shortest path** (in terms of number of edges)
- Simple to implement

**When to use:** Standard choice for reachability in practice

</v-clicks>

---

# Classical Graph Traversal: DFS

**Depth-First Search (DFS)**

**Approach:** Explore as far as possible along each branch before backtracking

```text
DFS(G, s, t):
  stack ← {s}
  visited ← {s}

  while stack is not empty:
    u ← pop(stack)
    if u = t:
      return true

    for each neighbor v of u:
      if v not in visited:
        visited ← visited ∪ {v}
        push(stack, v)

  return false
```

---

# DFS Properties

<v-clicks>

**Time Complexity:** $O(n + m)$ (same as BFS)

**Space Complexity:** $O(n)$ (stack depth can be $n$ in worst case)

**Advantages:**
- Also very practical
- Better for some applications (cycle detection, topological sorting)
- Can be implemented recursively (elegant)

**Differences from BFS:**
- Does **not** necessarily find shortest path
- Different traversal order
- Uses stack instead of queue

**When to use:** Structural graph analysis (strongly connected components, etc.)

</v-clicks>

---

# Comparison: BFS vs DFS vs Savitch

| Algorithm | Time | Space | Finds Shortest? | Notes |
|-----------|------|-------|-----------------|-------|
| **BFS** | $O(n+m)$ | $O(n)$ | Yes (by hops) | Practical standard |
| **DFS** | $O(n+m)$ | $O(n)$ | No | Good for structure |
| **Savitch** | $2^{O(\log n)}$ | $O(\log^2 n)$ | No | Minimal space |

<v-click>

**Key insight:** Savitch trades time for space
- BFS/DFS are polynomial time but linear space
- Savitch is exponential time but logarithmic space
- Different optimization goals!

</v-click>

---

# Reingold's Algorithm (2005)

**Breakthrough Result:** Undirected reachability in $O(\log n)$ space!

<v-clicks>

**Problem:** Undirected graph $G$, nodes $s$ and $t$, is there a path?

**Complexity:**
- **Space:** $O(\log n)$ - better than Savitch's $O(\log^2 n)$!
- **Time:** Polynomial (but high degree)

**Limitation:** Works only for **undirected** graphs
- Directed reachability is believed to require more space
- This is related to fundamental complexity theory questions

**Significance:**
- Resolved a long-standing open problem
- Uses sophisticated techniques (universal traversal sequences, derandomization)
- Showed that undirected reachability is in **L** (logarithmic space)

</v-clicks>

---

# The Space Complexity Hierarchy

Understanding where reachability fits in computational complexity:

<v-clicks>

**L** (Logarithmic Space): $O(\log n)$ working space
- Undirected reachability ∈ L (Reingold, 2005)

**NL** (Nondeterministic Logarithmic Space): $O(\log n)$ space with nondeterminism
- Directed reachability ∈ NL (complete for NL)
- By Savitch's theorem: NL ⊆ SPACE($\log^2 n$)

**P** (Polynomial Time): $O(n^k)$ time
- BFS, DFS solve reachability in linear time
- L ⊆ NL ⊆ P

**Open Question:** Is L = NL? (Is directed reachability in L?)

</v-clicks>

---

# All Pairs Reachability: Warshall's Algorithm

**Problem:** For all pairs $(i,j)$, determine if $j$ is reachable from $i$

**Warshall's Algorithm** (1962): Boolean version of Floyd-Warshall

```text
Warshall(G):
  // Initialize: R(i,j) = true if edge (i,j) exists
  for i = 1 to n:
    for j = 1 to n:
      R(i,j) ← (i,j) ∈ E or i = j

  // Consider each node k as intermediate
  for k = 1 to n:
    for i = 1 to n:
      for j = 1 to n:
        R(i,j) ← R(i,j) or (R(i,k) and R(k,j))

  return R
```

---

# Warshall vs Floyd-Warshall

| Aspect | Warshall | Floyd-Warshall |
|--------|----------|----------------|
| **Output** | Boolean (reachable?) | Distances |
| **Values** | true/false | Numbers (costs) |
| **Operation** | OR and AND | min and + |
| **Problem** | Transitive closure | All pairs shortest paths |
| **Complexity** | $O(n^3)$ | $O(n^3)$ |

<v-click>

**Key insight:** Floyd-Warshall generalizes Warshall!
- Warshall computes **transitive closure**
- Floyd-Warshall computes **metric closure**
- Same structure, different operations

</v-click>

---

# Matrix Multiplication Approach

**Transitive Closure via Boolean Matrix Multiplication**

<v-click>

Define adjacency matrix $A$ where $A[i,j] = 1$ if edge $(i,j)$ exists

</v-click>

<v-clicks>

**Key observation:**
- $A^2[i,j] = 1$ if there's a path of length $\leq 2$ from $i$ to $j$
- $A^k[i,j] = 1$ if there's a path of length $\leq k$ from $i$ to $j$
- Compute $A^{n-1}$ to get transitive closure

**Complexity:**
- Naive: $O(n^4)$ - compute $n-1$ matrix products
- With repeated squaring: $O(n^3 \log n)$ - only $\log n$ products
- Best known: $O(n^\omega)$ where $\omega \approx 2.37$ (fast matrix multiplication)

</v-clicks>

---

# Practical Algorithms Summary

For **practical** graph reachability:

<v-clicks>

**Single-Source Reachability:**
1. **BFS** - First choice (finds shortest path by hops)
2. **DFS** - When shortest path not needed or doing structural analysis

**Single-Source Shortest Paths (weighted):**
1. **Dijkstra** - Non-negative weights, very efficient
2. **Bellman-Ford** - Allows negative weights
3. **A\*** - With heuristics (not covered, but widely used)

**All-Pairs:**
1. **Floyd-Warshall** - Dense graphs or moderate size
2. **Run Dijkstra $n$ times** - Sparse graphs
3. **Johnson's Algorithm** - Sparse graphs with negative weights

</v-clicks>

---

# Theoretical Algorithms Summary

For **theoretical** interest (space complexity, complexity classes):

<v-clicks>

**Space-Efficient:**
1. **Savitch** - $O(\log^2 n)$ space for directed reachability
2. **Reingold** - $O(\log n)$ space for undirected reachability
3. **BFS/DFS** - $O(n)$ space (linear)

**Research Frontiers:**
- Is directed reachability in L? (L vs NL problem)
- Better space-time trade-offs?
- Parallel and distributed algorithms
- Dynamic graphs (edges added/removed)
- Approximation algorithms for large graphs

</v-clicks>

---

# The Complete Reachability Toolkit

| Algorithm | Year | Time | Space | Graph Type | Problem |
|-----------|------|------|-------|------------|---------|
| **DFS/BFS** | 1950s | $O(n+m)$ | $O(n)$ | Any | Reachability |
| **Warshall** | 1962 | $O(n^3)$ | $O(n^2)$ | Any | All-pairs reach |
| **Dijkstra** | 1959 | $O(n^2)$ | $O(n)$ | Weighted | Single-source SP |
| **Bellman-Ford** | 1958 | $O(nm)$ | $O(n)$ | Weighted | SP w/ neg edges |
| **Floyd-Warshall** | 1962 | $O(n^3)$ | $O(n^2)$ | Weighted | All-pairs SP |
| **Savitch** | 1970 | $2^{O(\log n)}$ | $O(\log^2 n)$ | Directed | Reachability |
| **Reingold** | 2005 | Poly | $O(\log n)$ | Undirected | Reachability |

<v-click>

**Spanning 50+ years of algorithmic development!**

</v-click>

---

# Key Exercises

**Exercise 4.5:** Construct graph family with $O(n)$ nodes but $\Omega(2^n)$ paths

<v-click>

**Exercise (Overwriting):** Explain in detail why Floyd's overwriting trick is correct

</v-click>

<v-click>

**Exercise (Correctness):** State pre/post-conditions and prove correctness using loop invariant

</v-click>

<v-click>

**Exercise (Implementation):** Implement Floyd's algorithm with 2D array and overwriting

</v-click>

<v-click>

**Exercise (Bellman-Ford):** Implement Bellman-Ford algorithm

</v-click>

---

# Summary: All Pairs Shortest Path

<v-clicks>

- **Problem:** Find shortest paths between all pairs of vertices
- **Approach:** Dynamic programming with intermediate node parameter
- **Floyd-Warshall Algorithm:** $O(n^3)$ time, $O(n^2)$ space
- **Recurrence:** $A(k,i,j) = \min\{A(k-1,i,j), A(k-1,i,k) + A(k-1,k,j)\}$
- **Key insight:** Incrementally consider each node as potential intermediate
- **Space optimization:** Can overwrite single 2D array safely
- **Comparison:** Reviewed Savitch (reachability), Dijkstra (single-source), Floyd (all-pairs)

</v-clicks>

---

# Reachability & Shortest Paths: The Big Picture

We've now seen a progression of graph algorithms:

<v-clicks>

1. **Reachability** (Savitch): Just answer "is there a path?"
   - Minimal space: $O(\log^2 n)$

2. **Single-Source** (Dijkstra): Shortest paths from one source
   - Greedy approach: $O(n^2)$

3. **All-Pairs** (Floyd): Shortest paths for every pair
   - Dynamic programming: $O(n^3)$

Each builds on graph traversal ideas but optimizes different aspects!

</v-clicks>

---

# Next Steps

- Practice implementing Floyd's algorithm
- Work through the 3×3 grid example by hand
- Prove the loop invariant formally
- Understand why overwriting is safe (key conceptual point!)
- Compare time/space trade-offs of different algorithms
- Implement Bellman-Ford and compare
- **Next section:** Simple Knapsack Problem (Section 4.3) - our first NP-hard problem!

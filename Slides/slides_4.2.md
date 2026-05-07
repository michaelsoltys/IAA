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

# All Pairs Shortest Path

Section 4.2 — Floyd-Warshall and friends: shortest paths between *every* pair, in $O(n^3)$.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---
layout: section
---

# Graph Reachability Algorithms

A Journey Through 50+ Years of Algorithm Design

---

# The Golden Age: 1950s-1960s

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

BFS and DFS — the bedrock graph algorithms, with us since the early days of computing.

</div>

**BFS & DFS (1950s)** - The Classics


- Among the **oldest** algorithms in computer science
- Independently discovered by multiple researchers
- DFS naturally emerges from maze-solving strategies used since ancient times
- BFS guarantees **shortest path** by number of hops
- Both are still the **go-to** algorithms for practical graph traversal today
- The "queue vs stack" distinction between BFS and DFS is one of the most elegant examples of how a single data structure choice completely changes algorithm behavior!


---

# The Dutch Master: Dijkstra (1959)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Single-source shortest paths, designed in twenty minutes at a café — and still in your GPS today.

</div>

**Edsger W. Dijkstra** - One of computer science's most influential figures


- Created while designing shortest routes for the Amsterdam public transport system
- Dijkstra famously wrote: "What is the shortest way to travel from Rotterdam to Groningen?"
- Designed the algorithm **in 20 minutes** without pencil and paper!
- Published in 1959, just 3 pages long
- Still used today in GPS navigation, network routing (OSPF protocol), and more
- Dijkstra was known for his strong opinions - he famously said "GOTO considered harmful" and refused to use BASIC because he thought it would "mutilate the minds" of students!


<!--
Dijkstra's own account: he and his fiancée Maria were sitting at a café in Amsterdam in 1956, waiting about 20 minutes for a train. No pen, no paper — that forced him to think in a way simple enough to hold entirely in his head. He wasn't even a graph theorist; he was an early software engineer at the Mathematical Centre, trying to find a demo problem for the ARMAC computer. Shortest-path was the simplest thing he could think of that would convince a non-technical audience the machine was useful. He only decided to publish it three years later, "reluctantly," and the paper is barely three pages long.
-->

---

# The Bellman-Ford Alliance (1958)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Slower than Dijkstra, but it tolerates *negative* edge weights — and gave dynamic programming its name.

</div>

**Richard Bellman** and **Lester Ford Jr.** - Independent discoveries


- Developed independently around the same time
- Bellman (of "dynamic programming" fame) published in 1958
- Ford published independently in 1956
- **Key advantage:** Can handle **negative edge weights**!
- Used in distance-vector routing protocols
- Bellman coined the term "dynamic programming" to hide mathematical research from a Secretary of Defense who "had a pathological fear of the word 'research'"


<!--
Bellman's own autobiography (1984) tells the naming story: at RAND under Defense Secretary Charles Wilson, he needed a name "nobody could possibly give a pejorative meaning to." "Dynamic" had an almost physical, active quality; "programming" in 1950s usage meant planning and scheduling, not code. So the name was essentially marketing — carefully engineered to sound respectable to a bureaucrat, not descriptive of the technique. Lester Ford Jr. meanwhile was the "Ford" in Ford–Fulkerson max-flow; his father Lester Ford Sr. was also a mathematician (they co-authored the 1962 book *Flows in Networks*). Four of the foundational algorithms of combinatorial optimization came out of RAND in the same decade, funded by the Air Force.
-->

---

# The Floyd-Warshall Saga (1962)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three independent rediscoveries of the same idea — the textbook example of how credit gets distributed.

</div>

**Three minds, one algorithm!**


- **Bernard Roy** (1959) - Published first but in French, largely unknown
- **Robert Floyd** (1962) - Popularized in English-speaking world
- **Stephen Warshall** (1962) - Boolean version (transitive closure)
- Floyd's version: one page, crystal clear
- Warshall's version: computes reachability instead of distances
- Sometimes called the "Roy-Floyd-Warshall" algorithm to credit all three discoverers
- Floyd was also famous for "Floyd's cycle-finding algorithm" (the tortoise and hare)


<!--
A small case study in how credit propagates through the Anglophone and Francophone literatures. Bernard Roy published the algorithm first, in French, in a 1959 paper about transitive closure in Markov chains — and it was essentially ignored outside France. Floyd (1962) and Warshall (1962) rediscovered it independently; Floyd's is the distance version, Warshall's the Boolean reachability version, structurally identical. Floyd's paper is famous for its brevity: the full algorithm plus correctness fits under a page. He won the Turing Award in 1978 for work on parsing and program verification. Warshall, by contrast, was a working engineer at MIT Lincoln Lab and later at DEC — never an academic, and so doesn't have comparable name recognition despite his work on compiler theory being excellent.
-->

---

# The Space Complexity Revolution: Savitch (1970)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The algorithm we just saw in 3.3 — useless in practice, profound in theory: $O(\log^2 n)$ space.

</div>

**Walter Savitch** - Trading time for space


- PhD thesis work at UC Berkeley
- **Savitch's Theorem:** NSPACE($f(n)$) ⊆ DSPACE($f(n)^2$)
- Shows directed reachability in $O(\log^2 n)$ space!
- Time complexity: $2^{O(\log n)} = n^{O(1)}$ but **exponential**
- Proves NL ⊆ SPACE($\log^2 n$)
- Rarely used in practice (too slow!) but **fundamental to complexity theory**
- Taught because it's beautiful and theoretically important, not because you'd ever actually use it!


---

# The 21st Century Breakthrough: Reingold (2005)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Undirected reachability in $O(\log n)$ space — a 30-year open problem closed by zig-zag products.

</div>

**Omer Reingold** - Solving a 30+ year old open problem


- Proved undirected reachability in L (logarithmic space!)
- Resolved question open since the 1970s
- Won the **Gödel Prize** in 2008
- Uses sophisticated derandomization techniques
- Space: $O(\log n)$ - better than Savitch's $O(\log^2 n)$!
- **Limitation:** Only works for **undirected** graphs
- **Open Question:** Is directed reachability in L? (The **L vs NL** problem)
- Reingold's proof uses "zig-zag products" of graphs - a technique borrowed from expander graph theory
- The paper is notoriously difficult but the result is stunning!


<!--
Reingold's result is "undirected reach is in L" — a question open since the 1970s. The machinery is the "zig-zag product" of graphs (Reingold–Vadhan–Wigderson, 2002), originally invented for a different purpose: explicit constructions of expander graphs. The idea — take a large graph and a small graph, combine them so the result inherits expansion properties while being navigable with tiny memory — was striking enough that it earned the zig-zag paper the Gödel Prize in 2009, the year after Reingold's own Gödel Prize for L=SL. The L vs NL question (directed reachability in L?) remains one of the most important open problems in complexity theory, rivalled only by P vs NP. Most complexity theorists believe L ≠ NL, but no proof is on the horizon.
-->

---

# Modern Era: Practical Speedups

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A* with heuristics, Johnson for sparse graphs, Strassen-style matrix tricks — practical speedups that ship today.

</div>

**Beyond the classics - modern developments**


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


---

# The Complexity Theory Connection

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Reachability is where complexity classes L, NL, and P meet — and where the great open problems live.

</div>

**Why study impractical algorithms?**


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


---

# Algorithm Personalities

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Each algorithm has its own temperament — pick the one whose strengths match your problem.

</div>

Different algorithms for different needs:


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


---

# Real-World Applications Today

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

These algorithms aren't museum pieces — they route packets, recommend friends, and crawl the web every second.

</div>

Where these algorithms live in modern systems:


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


---

# Timeline of Discoveries

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Half a century of breakthroughs in one table — and the ideas keep coming.

</div>

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


**50+ years of continuous innovation!**


---
layout: section
---

# Now Let's Dive Into Floyd-Warshall

Understanding the All Pairs Shortest Path Algorithm

---

# Problem Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Given a directed weighted graph, output an $n \times n$ table of pairwise shortest distances.

</div>

**Input:**
- Directed graph $G = (V, E)$ with $V = \{1, 2, \ldots, n\}$
- Cost function $C(i,j) \in \mathbb{N}^+ \cup \{\infty\}$ for all $1 \leq i, j \leq n$
- $C(i,j) = \infty$ if $(i,j)$ is not an edge

**Output:**
- Array $D$ where $D(i,j)$ is the length of the shortest directed path from $i$ to $j$

---

# Directed Graphs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Edges have direction — $(i,j)$ doesn't imply $(j,i)$ — like one-way streets or import dependencies.

</div>


- A **directed graph** (or **digraph**) has edges with direction (arrows)
- Different from undirected graphs (Section 2.1 - Minimum Cost Spanning Trees)
- Edge $(i,j)$ goes **from** $i$ **to** $j$ (not bidirectional unless both $(i,j)$ and $(j,i)$ exist)
- Many real-world applications: road networks, networks with one-way links, dependencies


---

# Why Not Exhaustive Search?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A graph with $O(n)$ nodes can hide $2^n$ paths — enumerating them all is hopeless.

</div>

**Problem 4.5:** Construct a family of graphs $\{G_n\}$ where:
- $G_n$ has $O(n)$ nodes
- But $\Omega(2^n)$ paths (exponentially many!)


**Example:** "Diamond Chain" graph with 3 layers:

```text
        ┌─── v₁ ───┐     ┌─── v₃ ───┐     ┌─── v₅ ───┐
    s ──┤          ├── ○ ┤          ├── ○ ┤          ├── t
        └─── v₂ ───┘     └─── v₄ ───┘     └─── v₆ ───┘

        Layer 1          Layer 2          Layer 3
```

At each layer: choose top or bottom path → $2 \times 2 \times 2 = 2^3 = 8$ paths

With $n$ layers: $2^n$ paths but only $2n + 2$ nodes


**Conclusion:** Exhaustive search is **not feasible**!


---

# Dynamic Programming Approach

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The Floyd-Warshall idea: parameterize by which intermediate vertices are "allowed" — and grow that set.

</div>

## Step 1: Define Subproblems

Let $A(k, i, j)$ = length of the shortest path from $i$ to $j$ where all **intermediate** nodes are in $\{1, 2, \ldots, k\}$


- When $k = 0$: $\{1, 2, \ldots, k\} = \emptyset$ (no intermediate nodes allowed)
- When $k = n$: $A(n, i, j) = D(i, j)$ is our solution


---

# Understanding Intermediate Nodes

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

"Intermediate" means *strictly between* $i$ and $j$ on the path — endpoints don't count.

</div>

Consider a path from node $i$ to node $j$:


$$i \rightarrow a_1 \rightarrow a_2 \rightarrow \cdots \rightarrow a_m \rightarrow j$$


- Nodes $a_1, a_2, \ldots, a_m$ are **intermediate** nodes
- Nodes $i$ and $j$ are **endpoints** (not intermediate)
- $A(k, i, j)$ restricts intermediate nodes to $\{1, 2, \ldots, k\}$


**Example:** $A(3, 5, 7)$ = shortest path from 5 to 7 where intermediate nodes (if any) come from $\{1, 2, 3\}$


---

# Step 2: Find the Recurrence

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Either node $k$ is on the shortest path, or it isn't — split into two cases and pick the cheaper.

</div>

**Initialization:** $A(0, i, j) = C(i, j)$ (no intermediate nodes allowed)


**Recursive case** for $k > 0$:

Consider whether node $k$ is on the shortest path from $i$ to $j$


**Case 1:** Node $k$ is **not** on the path
- Shortest path uses only nodes $\{1, \ldots, k-1\}$
- Therefore: $A(k, i, j) = A(k-1, i, j)$

**Case 2:** Node $k$ **is** on the path
- Path goes: $i \rightsquigarrow k \rightsquigarrow j$
- Node $k$ appears exactly once (no benefit to revisiting)
- Therefore: $A(k, i, j) = A(k-1, i, k) + A(k-1, k, j)$


---

# The Recurrence Formula

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

One clean line of math captures the entire algorithm — *route through $k$ or skip it*, take the min.

</div>

Take the minimum of both cases:

$$A(k, i, j) = \min\{A(k-1, i, j), \; A(k-1, i, k) + A(k-1, k, j)\}$$


**Intuition:**
- Should we route through node $k$ or not?
- Try both options and pick the cheaper one
- This exhibits **optimal substructure** (key property for DP)

**Why does $k$ appear exactly once?**
- If $k$ appears twice, we have a cycle involving $k$
- Since costs are positive, cycles increase cost (never optimal)


---

# Step 3: The Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three nested loops, four lines of code — and the *outer* loop must be $k$.

</div>

<span style="font-size: 0.6em; color: navy;">Alg 22, Pg 78, alg:floyd</span>

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

<!--
The three-line inner body is arguably the most-cited piece of pseudocode in computer science. What makes it subtle is the loop order: k must be the outermost loop. If you put k inside, correctness breaks — you'd be updating B(i,j) using values that haven't been given the chance to route through all possible intermediates up to k. Students who first meet this algorithm often memorize the lines but misremember the order, and it's worth pausing on that — it's exactly the kind of detail where the DP invariant (B(i,j) = A(k, i, j) after iteration k) pays its rent.
-->

---

# The Space-Saving Trick

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

We don't need to keep history — overwrite the table in place and drop space from $O(n^3)$ to $O(n^2)$.

</div>

**Observation:** We only need a **2D array** $B(i,j)$, not 3D!


We can **overwrite** $A(k-1, *, *)$ to compute $A(k, *, *)$

```text
// Before iteration k:  B(i,j) = A(k-1, i, j)
for k = 1 to n:
  for i = 1 to n:
    for j = 1 to n:
      B(i,j) ← min{B(i,j), B(i,k) + B(k,j)}
// After iteration k:   B(i,j) = A(k, i, j)
```


Reduces space from $O(n^3)$ to $O(n^2)$!


---

# Why Does Overwriting Work?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The row $k$ and column $k$ don't change during iteration $k$ — so reading old or new values gives the same answer.

</div>

**Concern:** When we compute `B(i,j) ← min{B(i,j), B(i,k) + B(k,j)}`, we might use already-updated values!


**Answer:** The overwriting is **safe** because:

1. We're computing $A(k, i, j)$ for all $i,j$ in iteration $k$
2. We use values $B(i,k)$ and $B(k,j)$
3. These represent paths **to/from** node $k$
4. Such paths **cannot use $k$ as intermediate** (would create cycle with $k$)
5. So $B(i,k) = A(k-1, i, k) = A(k, i, k)$ (adding $k$ doesn't help)
6. Similarly $B(k,j) = A(k-1, k, j) = A(k, k, j)$


**Bottom line:** Whether we read old or new values of $B(i,k)$ and $B(k,j)$, they're the same!


---

# Alternative: Using Two Arrays

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If you don't trust the overwriting trick, two arrays make the DP transparent — at the cost of more memory.

</div>

Could avoid overwriting entirely:

```text
for k = 1 to n:
  for i = 1 to n:
    for j = 1 to n:
      A_new(i,j) ← min{A_old(i,j), A_old(i,k) + A_old(k,j)}
  A_old ← A_new
```


- Uses $O(n^2)$ additional space
- Conceptually clearer (no overwriting concerns)
- Same time complexity $O(n^3)$
- Floyd's single-array version is more elegant and space-efficient


---

# Example: 3×3 Grid Graph

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A nine-node grid we'll trace through Floyd-Warshall step by step.

</div>

```text
1 — 2 — 3
|   |   |
4 — 5 — 6
|   |   |
7 — 8 — 9
```


Assume all edges have cost 1 and are **bidirectional** (so both $(i,j)$ and $(j,i)$ exist)

Let's trace the algorithm step by step


---

# Example: Initialization (k=0)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Before any iterations, $B$ is just the cost matrix — direct edges only, no intermediates allowed.

</div>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Allow node 1 as a stepping stone — and watch new shortcuts appear in the table.

</div>

Now paths can use node 1 as intermediate

**Key updates:**
- $A(1, 2, 4) = \min\{\infty, A(0,2,1) + A(0,1,4)\} = \min\{\infty, 1+1\} = 2$
  - New path: $2 \to 1 \to 4$


Nodes 2 and 4 can now reach each other via node 1!

| From $\backslash$ To | 1 | 2 | 3 | 4 | ... |
|--:|:-:|:-:|:-:|:-:|:-:|
| **2** | 1 | 0 | 1 | **2** | ... |
| **4** | 1 | **2** | $\infty$ | 0 | ... |


---

# Example: After k=2

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

With nodes $\{1, 2\}$ now usable as intermediates, more pairs find shorter routes.

</div>

Now paths can use nodes $\{1, 2\}$ as intermediates

**More updates:**
- $A(2, 1, 3) = \min\{\infty, A(1,1,2) + A(1,2,3)\} = \min\{\infty, 1+1\} = 2$
  - Path: $1 \to 2 \to 3$
- $A(2, 1, 5) = \min\{\infty, A(1,1,2) + A(1,2,5)\} = \min\{\infty, 1+1\} = 2$
  - Path: $1 \to 2 \to 5$


Distances from node 1 to distant nodes decrease as we allow more intermediates


---

# Example: After k=9

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

All intermediates allowed — $B$ is now the full shortest-path matrix.

</div>

After all 9 iterations, we have the complete shortest path matrix:

| From $\backslash$ To | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|--:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **1** | 0 | 1 | 2 | 1 | 2 | 3 | 2 | 3 | 4 |
| **5** | 2 | 1 | 2 | 1 | 0 | 1 | 2 | 1 | 2 |
| **9** | 4 | 3 | 2 | 3 | 2 | 1 | 2 | 1 | 0 |


For example: $D(1,9) = 4$
- Shortest path from 1 to 9 has length 4
- One such path: $1 \to 2 \to 5 \to 8 \to 9$


---

# Algorithm Analysis

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$O(n^3)$ time, $O(n^2)$ space — and remarkably tight given that the *output* alone is $\Theta(n^2)$.

</div>

**Time Complexity:** $O(n^3)$
- Three nested loops, each running $n$ times
- Each iteration does constant work


**Space Complexity:** $O(n^2)$
- Single $n \times n$ matrix $B$
- Input graph also takes $O(n^2)$ space


**Remarkable properties:**
- Graph may have up to $O(n^2)$ edges
- Algorithm runs in $O(n^3)$ time
- Very efficient for **dense graphs**
- Simple and elegant implementation


---

# Correctness

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Set up the contract: what we're given, what we promise to return.

</div>

**Pre-condition:**
- Valid directed graph $G=(V,E)$
- Cost function $C$ with $C(i,j) \in \mathbb{N}^+ \cup \{\infty\}$
- $C(i,i) = 0$ for all $i$ (optional: can be handled)


**Post-condition:**
- $D(i,j)$ contains length of shortest path from $i$ to $j$
- If no path exists, $D(i,j) = \infty$


---

# Loop Invariant

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

After iteration $k$, $B(i,j) = A(k, i, j)$ — that single equation drives the whole correctness proof.

</div>

**Invariant (for outer loop on $k$):**

After iteration $k$, for all $i, j$:
$$B(i,j) = A(k, i, j)$$

That is: $B(i,j)$ contains the shortest path from $i$ to $j$ using only nodes $\{1, \ldots, k\}$ as intermediates


**Proof sketch:**
- **Base case** ($k=0$): $B(i,j) = C(i,j) = A(0,i,j)$ ✓
- **Inductive step:** If true for $k-1$, the recurrence correctly computes $A(k,i,j)$
- **Termination:** When $k=n$, we have $B(i,j) = A(n,i,j) = D(i,j)$ ✓


---
layout: section
---

# Bellman-Ford Algorithm

A Different Dynamic Programming Approach

---

# Bellman-Ford Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Same DP idea, different parameter: now the subproblem grows by *number of edges*, not number of vertices.

</div>

**Problem:** Find shortest path from $s$ to $t$ in directed graph

**Different DP formulation:**
- Let $\text{opt}(i,v)$ = minimal cost of an **$i$-path** from $v$ to $t$
- An $i$-path uses **at most** $i$ edges


**Recurrence:** For $i > 0$:
$$\text{opt}(i,v) = \min\{\text{opt}(i-1,v), \; \min_{w \in V}\{c(v,w) + \text{opt}(i-1,w)\}\}$$


- **Case 1:** Optimal path uses $< i$ edges: $\text{opt}(i-1,v)$
- **Case 2:** Optimal path uses exactly $i$ edges via edge $(v,w)$: $c(v,w) + \text{opt}(i-1,w)$


---

# Bellman-Ford vs Floyd

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two DP formulations, two different sweet spots — sparse single-source vs dense all-pairs.

</div>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A practical decision tree — match the algorithm to the question you're actually asking.

</div>


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


---
layout: section
---

# Other Known Reachability Algorithms

A Survey of Classical and Modern Approaches

---

# The Reachability Problem Landscape

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

"Is there a path?" is the simplest graph question — and it shows up *everywhere* in CS.

</div>

The reachability problem is **ubiquitous** in computer science!


**Basic Question:** Given graph $G$ and nodes $s$, $t$, is there a path from $s$ to $t$?


**Key Variations:**
- Directed vs. Undirected graphs
- Simple reachability vs. shortest path
- Time complexity vs. space complexity trade-offs
- Deterministic vs. nondeterministic models


---

# Classical Graph Traversal: BFS

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A queue, a visited set, and you've got reachability *and* shortest path-by-hops in $O(n+m)$.

</div>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Linear time, linear space, finds shortest path by hops — this is why BFS is the practical default.

</div>


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


---

# Classical Graph Traversal: DFS

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Swap the queue for a stack and you get DFS — same complexity, very different traversal order.

</div>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Same $O(n+m)$ as BFS, but DFS is what you reach for when *structure* matters — SCCs, topo sort, cycles.

</div>


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


---

# Comparison: BFS vs DFS vs Savitch

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Same problem, three different optimization targets — fast vs structural vs memory-tight.

</div>

| Algorithm | Time | Space | Finds Shortest? | Notes |
|-----------|------|-------|-----------------|-------|
| **BFS** | $O(n+m)$ | $O(n)$ | Yes (by hops) | Practical standard |
| **DFS** | $O(n+m)$ | $O(n)$ | No | Good for structure |
| **Savitch** | $2^{O(\log n)}$ | $O(\log^2 n)$ | No | Minimal space |


**Key insight:** Savitch trades time for space
- BFS/DFS are polynomial time but linear space
- Savitch is exponential time but logarithmic space
- Different optimization goals!


---

# Reingold's Algorithm (2005)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Undirected reachability is in *L* — a result so clean it earned the Gödel Prize.

</div>

**Breakthrough Result:** Undirected reachability in $O(\log n)$ space!


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


---

# The Space Complexity Hierarchy

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

L, NL, P — and the great open question: is directed reachability in $O(\log n)$ space?

</div>

Understanding where reachability fits in computational complexity:


**L** (Logarithmic Space): $O(\log n)$ working space
- Undirected reachability ∈ L (Reingold, 2005)

**NL** (Nondeterministic Logarithmic Space): $O(\log n)$ space with nondeterminism
- Directed reachability ∈ NL (complete for NL)
- By Savitch's theorem: NL ⊆ SPACE($\log^2 n$)

**P** (Polynomial Time): $O(n^k)$ time
- BFS, DFS solve reachability in linear time
- L ⊆ NL ⊆ P

**Open Question:** Is L = NL? (Is directed reachability in L?)


---

# All Pairs Reachability: Warshall's Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Same skeleton as Floyd-Warshall, but with booleans — *(min, +)* becomes *(or, and)*.

</div>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Identical structure, different *semiring* — the same DP scaffolding handles both.

</div>

| Aspect | Warshall | Floyd-Warshall |
|--------|----------|----------------|
| **Output** | Boolean (reachable?) | Distances |
| **Values** | true/false | Numbers (costs) |
| **Operation** | OR and AND | min and + |
| **Problem** | Transitive closure | All pairs shortest paths |
| **Complexity** | $O(n^3)$ | $O(n^3)$ |


**Key insight:** Floyd-Warshall generalizes Warshall!
- Warshall computes **transitive closure**
- Floyd-Warshall computes **metric closure**
- Same structure, different operations


---

# Matrix Multiplication Approach

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Powers of the adjacency matrix $A$ encode paths of bounded length — and repeated squaring beats the naive bound.

</div>

**Transitive Closure via Boolean Matrix Multiplication**


Define adjacency matrix $A$ where $A[i,j] = 1$ if edge $(i,j)$ exists


**Key observation:**
- $A^2[i,j] = 1$ if there's a path of length $\leq 2$ from $i$ to $j$
- $A^k[i,j] = 1$ if there's a path of length $\leq k$ from $i$ to $j$
- Compute $A^{n-1}$ to get transitive closure

**Complexity:**
- Naive: $O(n^4)$ - compute $n-1$ matrix products
- With repeated squaring: $O(n^3 \log n)$ - only $\log n$ products
- Best known: $O(n^\omega)$ where $\omega \approx 2.37$ (fast matrix multiplication)


---

# Practical Algorithms Summary

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A field guide for picking the right algorithm in real code — single-source, all-pairs, weighted, or not.

</div>

For **practical** graph reachability:


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


---

# Theoretical Algorithms Summary

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The algorithms you study to *understand* computation, even if you'd never run them in production.

</div>

For **theoretical** interest (space complexity, complexity classes):


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


---

# The Complete Reachability Toolkit

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Every algorithm in one matrix — name, year, complexity, and use case at a glance.

</div>

| Algorithm | Year | Time | Space | Graph Type | Problem |
|-----------|------|------|-------|------------|---------|
| **DFS/BFS** | 1950s | $O(n+m)$ | $O(n)$ | Any | Reachability |
| **Warshall** | 1962 | $O(n^3)$ | $O(n^2)$ | Any | All-pairs reach |
| **Dijkstra** | 1959 | $O(n^2)$ | $O(n)$ | Weighted | Single-source SP |
| **Bellman-Ford** | 1958 | $O(nm)$ | $O(n)$ | Weighted | SP w/ neg edges |
| **Floyd-Warshall** | 1962 | $O(n^3)$ | $O(n^2)$ | Weighted | All-pairs SP |
| **Savitch** | 1970 | $2^{O(\log n)}$ | $O(\log^2 n)$ | Directed | Reachability |
| **Reingold** | 2005 | Poly | $O(\log n)$ | Undirected | Reachability |


**Spanning 50+ years of algorithmic development!**


---

# Key Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The problems that nail down the chapter — implement Floyd, prove correctness, handle negative edges.

</div>

**Problem 4.5:** Construct graph family with $O(n)$ nodes but $\Omega(2^n)$ paths <span style="font-size: 0.6em; color: navy;">Prb 4.5, Pg 77, prb:allpairs</span>


**Problem 4.6:** Explain in detail why Floyd's overwriting trick is correct <span style="font-size: 0.6em; color: navy;">Prb 4.6, Pg 78, exr:shortpath1</span>


**Problem 4.7:** State pre/post-conditions and prove correctness using loop invariant <span style="font-size: 0.6em; color: navy;">Prb 4.7, Pg 78, exr:shortpath2</span>


**Problem 4.8:** Implement Floyd's algorithm with 2D array and overwriting <span style="font-size: 0.6em; color: navy;">Prb 4.8, Pg 78, exr:floyd</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Problems/P4.8_Floyd.py" style="font-size: 0.6em; color: teal;">[Python solution]</a>


**Problem 4.9:** Implement Bellman-Ford algorithm <span style="font-size: 0.6em; color: navy;">Prb 4.9, Pg 78, exr:bellman</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Problems/P4.9_Bellman-Ford.py" style="font-size: 0.6em; color: teal;">[Python solution]</a>


---

# Summary: All Pairs Shortest Path

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The takeaways: parameterize over allowed intermediates, write the recurrence, overwrite in place.

</div>


- **Problem:** Find shortest paths between all pairs of vertices
- **Approach:** Dynamic programming with intermediate node parameter
- **Floyd-Warshall Algorithm:** $O(n^3)$ time, $O(n^2)$ space
- **Recurrence:** $A(k,i,j) = \min\{A(k-1,i,j), A(k-1,i,k) + A(k-1,k,j)\}$
- **Key insight:** Incrementally consider each node as potential intermediate
- **Space optimization:** Can overwrite single 2D array safely
- **Comparison:** Reviewed Savitch (reachability), Dijkstra (single-source), Floyd (all-pairs)


---

# Reachability & Shortest Paths: The Big Picture

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A spectrum from "is there a path?" to "shortest paths between every pair" — each step adds work and information.

</div>

We've now seen a progression of graph algorithms:


1. **Reachability** (Savitch): Just answer "is there a path?"
   - Minimal space: $O(\log^2 n)$

2. **Single-Source** (Dijkstra): Shortest paths from one source
   - Greedy approach: $O(n^2)$

3. **All-Pairs** (Floyd): Shortest paths for every pair
   - Dynamic programming: $O(n^3)$

Each builds on graph traversal ideas but optimizes different aspects!

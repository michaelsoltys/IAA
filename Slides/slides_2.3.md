---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 2.3: Further Greedy Examples
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Further Greedy Examples
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

# Further Greedy Examples

Section 2.3 - Greedy Algorithms

---

# Overview

Three more examples of greedy algorithms:

<v-clicks>

1. **Make Change** - Sometimes greedy fails!
2. **Shortest Path (Dijkstra)** - Greedy works beautifully
3. **Huffman Codes** - Optimal data compression

</v-clicks>

---

# Make Change Problem

**Problem:** Pay amount $n$ using the fewest coins

**Denominations:** $C = \{1, 10, 25, 100\}$ (cents)

<v-click>

**Greedy approach:**
```text
Make Change:
1. C ← {1, 10, 25, 100}; L ← ∅; s ← 0
2. while s < n:
3.     find largest x in C such that s + x ≤ n
4.     L ← L ∪ {x}; s ← s + x
5. return L
```

</v-click>

<v-click>

Always pick the largest coin that doesn't exceed the remaining amount.

</v-click>

---

# Make Change: Does Greedy Work?

**Example:** $n = 30$ cents

<v-click>

Greedy: $25 + 1 + 1 + 1 + 1 + 1 = 30$ → **6 coins**

</v-click>

<v-click>

Optimal: $10 + 10 + 10 = 30$ → **3 coins**

</v-click>

<v-click>

**Greedy fails!** The algorithm is not optimal for this denomination.

</v-click>

---

# When Does Make Change Work?

**Theorem:** If $C = \{1, p, p^2, \ldots, p^k\}$ for some $p > 1$, then greedy always finds the optimal solution.

<v-clicks>

Examples where greedy works:
- Binary: $\{1, 2, 4, 8, 16, \ldots\}$
- Decimal: $\{1, 10, 100, 1000, \ldots\}$

Examples where greedy may fail:
- US coins: $\{1, 5, 10, 25\}$ (fails for 30 cents)
- Custom: $\{1, 3, 4\}$ (fails for 6: greedy gives $4+1+1$, optimal is $3+3$)

</v-clicks>

---

# Maximum Weight Matching

**Setup:** Bipartite graph $G = (V_1 \cup V_2, E)$ with edge weights

**Matching:** Set $M \subseteq E$ where no two edges share a vertex

<v-click>

**Natural greedy approach:**
1. Sort edges by weight (descending)
2. Add each edge if it doesn't share vertices with existing edges

</v-click>

<v-click>

**Does it work?** Not always! (Problem 2.29)

</v-click>

<v-click>

**Special case:** If all weights are distinct powers of 2, greedy works!

</v-click>

---

# Shortest Path Problem

**Setup:**
- Graph $G = (V, E)$
- Start node $s$
- Cost function $c(e)$ for each edge

<v-click>

**Goal:** Find cheapest path from $s$ to every other node

(Cost of path = sum of edge costs)

</v-click>

---

# Dijkstra's Algorithm: The Idea

Like old cartographers mapping unknown territory!

<v-clicks>

- Maintain set $S$ of "explored" nodes
- For each $u \in S$, store $d(u)$ = cost of cheapest path from $s$ to $u$ within $S$
- Initially: $S = \{s\}$, $d(s) = 0$

</v-clicks>

<v-click>

**Expanding the frontier:**

```
        ┌─────────────────────┐
        │    Explored S       │
    s ══╪══> ... ══> u ───────┼──> v
        │                     │
        └─────────────────────┘
```

</v-click>

---

# Dijkstra's Algorithm: The Rule

For each unexplored $v \in V - S$, compute:

$$d'(v) = \min_{u \in S, e=(u,v)} [d(u) + c(e)]$$

<v-clicks>

- This is the shortest path to $v$ through explored territory
- Choose $v$ that minimizes $d'(v)$
- Add $v$ to $S$ and set $d(v) = d'(v)$
- Repeat until $S = V$

</v-clicks>

---

# Why Does Dijkstra's Algorithm Work?

**Key insight:** When we add $v$ to $S$, we've found the shortest path to $v$.

<v-click>

**Why?** Any other path to $v$ must:
1. Leave $S$ at some point through some node $w$
2. But we chose $v$ because it had the smallest $d'$ value
3. So any path through $w$ is at least as long

</v-click>

<v-click>

**Important assumption:** All edge costs are non-negative!

(With negative edges, this argument fails)

</v-click>

---

# Dijkstra: Complexity

<v-clicks>

- At most $n$ iterations (add one node per iteration)
- Each iteration: examine all edges leaving $S$
- **Simple implementation:** $O(n^2)$
- **With priority queue:** $O((n + m) \log n)$

</v-clicks>

<v-click>

**Real-world application:** OSPF (Open Shortest Path First) routing protocol uses Dijkstra's algorithm!

</v-click>

---

# Huffman Codes

**Problem:** Compress data using variable-length codes

<v-clicks>

- Fixed-length: Each character uses same number of bits
- Variable-length: Frequent characters get shorter codes

</v-clicks>

<v-click>

**Example:** String of 100 characters over $\{a, b, c, d, e, f\}$

| Char | a | b | c | d | e | f |
|------|---|---|---|---|---|---|
| Freq | 44 | 14 | 11 | 17 | 8 | 6 |

Fixed-length: 6 chars → 3 bits each → 300 bits total

</v-click>

---

# Prefix Codes

**Prefix code:** No codeword is a prefix of another codeword

<v-click>

**Why prefix codes?**
- Decoding is unambiguous
- No separator needed between codewords
- Any code can be converted to a prefix code (no loss)

</v-click>

<v-click>

**Representation:** Binary tree where:
- Leaves = characters (with frequencies)
- Internal nodes = sum of frequencies in subtree
- Code = path from root (0 = left, 1 = right)

</v-click>

---

# Huffman Tree Example

```
              100
             /   \
           a:44   56
                 /   \
               25     31
              /  \   /  \
           c:11 b:14 14  d:17
                    /  \
                  f:6  e:8
```

<v-click>

| Char | Code | Bits |
|------|------|------|
| a | 0 | 1 |
| b | 101 | 3 |
| c | 100 | 3 |
| d | 111 | 3 |
| e | 1101 | 4 |
| f | 1100 | 4 |

</v-click>

---

# Computing Total Bits

With variable-length encoding:

$$44 \times 1 + 14 \times 3 + 11 \times 3 + 17 \times 3 + 8 \times 4 + 6 \times 4$$

<v-click>

$= 44 + 42 + 33 + 51 + 32 + 24 = 226$ bits

</v-click>

<v-click>

**Savings:** $300 - 226 = 74$ bits (25% reduction!)

</v-click>

---

# Huffman's Algorithm

```text
Huffman:
1. n ← |Σ|; Q ← Σ (priority queue by frequency)
2. for i = 1 to n-1:
3.     allocate new node z
4.     left[z] ← x = extract-min(Q)
5.     right[z] ← y = extract-min(Q)
6.     f(z) ← f(x) + f(y)
7.     insert z into Q
8. return remaining node (root of tree)
```

<v-click>

**Greedy choice:** Always merge the two least frequent nodes!

</v-click>

---

# Huffman: Building the Tree

For $\{a:44, b:14, c:11, d:17, e:8, f:6\}$:

<v-clicks>

1. Merge $f(6)$ and $e(8)$ → node with frequency 14
2. Merge $c(11)$ and $b(14)$ → node with frequency 25
3. Merge (fe:14) and $d(17)$ → node with frequency 31
4. Merge (cb:25) and (fed:31) → node with frequency 56
5. Merge $a(44)$ and (cbfed:56) → root with frequency 100

</v-clicks>

---

# Why Huffman is Optimal

**Key insight:** In an optimal tree:
- The two lowest-frequency characters should be siblings
- They should be at the maximum depth

<v-click>

**Proof idea:**
- If lowest-frequency chars aren't at max depth, swap them with deeper nodes
- This can only decrease total bits
- Huffman builds the tree bottom-up, ensuring this property

</v-click>

---

# Huffman: Complexity

<v-clicks>

- $n-1$ iterations (merge operations)
- Each iteration: 2 extract-min + 1 insert
- With binary heap: $O(\log n)$ per operation
- **Total:** $O(n \log n)$

</v-clicks>

<v-click>

**Applications:**
- ZIP, GZIP compression
- JPEG, MP3 (combined with other techniques)
- Many communication protocols

</v-click>

---

# Greedy Algorithms: Summary

| Algorithm | Greedy Choice | Works? |
|-----------|---------------|--------|
| Make Change | Largest coin | Sometimes |
| Max Weight Matching | Heaviest edge | Sometimes |
| Shortest Path | Closest unexplored | Yes (non-negative) |
| Huffman | Merge least frequent | Yes |
| Kruskal (MCST) | Cheapest edge | Yes |
| Job Scheduling | Most profitable | Yes |

---

# When Does Greedy Work?

<v-clicks>

**Look for these properties:**

1. **Greedy choice property:** A locally optimal choice leads to a globally optimal solution

2. **Optimal substructure:** An optimal solution contains optimal solutions to subproblems

3. **Exchange argument:** Can always improve a non-greedy solution to match the greedy choice

4. **"Promising" invariant:** Partial solution can always be extended to optimal

</v-clicks>

---

# Key Problems

<v-clicks>

1. **Problem 2.25:** Show greedy make-change fails for $\{1, 10, 25, 100\}$

2. **Problem 2.26:** Prove greedy works when $C = \{1, p, p^2, \ldots, p^k\}$

3. **Problem 2.29:** Find a bipartite graph where greedy matching fails

4. **Problem 2.31:** Design and prove Dijkstra's algorithm in pseudocode

5. **Problem 2.34:** Implement Huffman compression

</v-clicks>

---

# Summary

<v-clicks>

- **Make Change:** Greedy doesn't always work! Depends on denominations
- **Shortest Path:** Dijkstra's elegant greedy algorithm, $O(n^2)$
- **Huffman Codes:** Greedy tree construction gives optimal compression
- **Key lesson:** Greedy is simple but requires careful analysis
- **Proof techniques:** Exchange arguments, "promising" invariants

</v-clicks>

---

# Next Chapter

**Chapter 3: Divide and Conquer**

- Mergesort
- Binary multiplication
- Savitch's algorithm
- Quicksort

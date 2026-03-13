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
mdc: false
---

# Further Greedy Examples

Section 2.3 - Further Greedy Examples

---

# Overview

Three more examples of greedy algorithms:

1. **Make Change** - Sometimes greedy fails!
2. **Shortest Path (Dijkstra)** - Greedy works beautifully
3. **Huffman Codes** - Optimal data compression

---

# Make Change Problem

**Problem:** Pay amount $n$ using the fewest coins

**Denominations:** $C = \lbrace 1, 10, 25, 100 \rbrace$ (cents)

**Greedy approach to Make Change:**
```text
C ← {1, 10, 25, 100}; L ← ∅; s ← 0
while s < n:
    find largest x in C such that s + x ≤ n
    L ← L ∪ {x}; s ← s + x
return L
```

Always pick the largest coin that doesn't exceed the remaining amount.

<!--
The make-change problem has a surprisingly deep history. It's closely related to the Frobenius coin problem (also called the "money changing problem" or "chicken mcnugget theorem"): given denominations that are coprime, what is the largest amount that CANNOT be made? For two coprime denominations a and b, the answer is ab - a - b. For example, with 3 and 5 cent coins, the largest unmakeable amount is 3*5 - 3 - 5 = 7 cents.

The general problem of determining whether greedy works for a given set of denominations is itself non-trivial. In 1970, Chang and Gill showed it's related to the structure of the denomination system. The US coin system {1, 5, 10, 25} happens to be one where greedy works — the Treasury didn't plan it that way, but it's a happy accident of the denominations being "canonical."
-->

---

# Make Change: Does Greedy Work?

**Example:** $n = 30$ cents

Greedy: $25 + 1 + 1 + 1 + 1 + 1 = 30$ → **6 coins**

Optimal: $10 + 10 + 10 = 30$ → **3 coins**

**Greedy fails!** The algorithm is not optimal for this denomination.

---

# When Does Make Change Work?

**Theorem:** If $C = \lbrace 1, p, p^2, \ldots, p^k \rbrace$ for some $p > 1$, then greedy always finds the optimal solution.

Examples where greedy works:
- Binary: $\lbrace 1, 2, 4, 8, 16, \ldots \rbrace$
- Decimal: $\lbrace 1, 10, 100, 1000, \ldots \rbrace$

Examples where greedy may fail:
- US coins: $\lbrace 1, 5, 10, 25 \rbrace$ (fails for 30 cents)
- Custom: $\lbrace 1, 3, 4 \rbrace$ (fails for 6: greedy gives $4+1+1$, optimal is $3+3$)

---

# Maximum Weight Matching

**Setup:** Bipartite graph $G = (V_1 \cup V_2, E)$ with edge weights

**Matching:** Set $M \subseteq E$ where no two edges share a vertex

**Natural greedy approach:**
1. Sort edges by weight (descending)
2. Add each edge if it doesn't share vertices with existing edges

**Does it work?** Not always! (Problem 2.29)

**Special case:** If all weights are distinct powers of 2, greedy works!

<!--
Maximum weight matching in general graphs is solved optimally by Jack Edmonds' "blossom algorithm" (1965), one of the landmark results in combinatorial optimization. It runs in O(n^3) and introduced the concept of "blossoms" — odd-length cycles that must be contracted to handle non-bipartite graphs. Edmonds' paper "Paths, Trees, and Flowers" is considered one of the most beautiful papers in theoretical CS.

For bipartite graphs specifically, the Hungarian algorithm (Kuhn, 1955, based on work by Konig and Egervary from the 1930s) solves the assignment problem in O(n^3). It's named "Hungarian" because Kuhn credited the two Hungarian mathematicians whose theorems underlie it.
-->

---

# Shortest Path Problem

**Setup:**
- Graph $G = (V, E)$
- Start node $s$
- Cost function $c(e)$ for each edge

**Goal:** Find cheapest path from $s$ to every other node

(Cost of path = sum of edge costs)

<!--
The shortest path problem is one of the most practically important problems in all of computer science. Every time you use Google Maps, a GPS navigator, or a network routing protocol, shortest path algorithms are running behind the scenes.

The problem was first posed formally by mathematicians studying operations research in the 1950s. Before Dijkstra, the only known approaches were either brute-force (try all paths) or the Bellman-Ford algorithm (1956-1958), which handles negative edges but is slower.
-->

---

# Dijkstra's Algorithm: The Idea

Like old cartographers mapping unknown territory!

- Maintain set $S$ of "explored" nodes
- For each $u \in S$, store $d(u)$ = cost of cheapest path from $s$ to $u$ within $S$
- Initially: $S = \lbrace s \rbrace$, $d(s) = 0$

**Expanding the frontier:**

<img src="/Figures/explored.drawio.svg" class="mx-auto h-48 my-4" />

<!--
Edsger W. Dijkstra invented this algorithm in 1956 while sitting at a cafe in Amsterdam. He was 26 years old. As he later recalled: "What is the shortest way to travel from Rotterdam to Groningen? I designed an algorithm for the shortest path in about twenty minutes. One morning I was shopping in Amsterdam with my young fiancee, and tired, we sat down on the cafe terrace to drink a cup of coffee and I was just thinking about whether I could do this, and I then designed the algorithm for the shortest path."

He didn't publish it until 1959 — a 3-page paper in Numerische Mathematik. It's now one of the most cited papers in computer science.

Dijkstra won the Turing Award in 1972, primarily for his contributions to programming methodology (structured programming, semaphores, the "Go To Statement Considered Harmful" letter). He was famously opinionated — he hand-wrote all his manuscripts and distributed them as numbered "EWDs" (over 1,300 of them), refusing to use a word processor.
-->

---

# Dijkstra's Algorithm: The Rule

For each unexplored $v \in V - S$, compute:

$$d'(v) = \min_{u \in S, e=(u,v)} [d(u) + c(e)]$$

- This is the shortest path to $v$ through explored territory
- Choose $v$ that minimizes $d'(v)$
- Add $v$ to $S$ and set $d(v) = d'(v)$
- Repeat until $S = V$

---

# Why Does Dijkstra's Algorithm Work?

**Key insight:** When we add $v$ to $S$, we've found the shortest path to $v$.

**Why?** Any other path to $v$ must:
1. Leave $S$ at some point through some node $w$
2. But we chose $v$ because it had the smallest $d'$ value
3. So any path through $w$ is at least as long

**Important assumption:** All edge costs are non-negative!

(With negative edges, this argument fails)

---

# Dijkstra: Complexity

- At most $n$ iterations (add one node per iteration)
- Each iteration: examine all edges leaving $S$
- **Simple implementation:** $O(n^2)$
- **With priority queue:** $O((n + m) \log n)$

**Real-world application:** OSPF (Open Shortest Path First) routing protocol uses Dijkstra's algorithm!

<!--
The O(n^2) bound is for the simple array-based implementation. With a Fibonacci heap (Fredman and Tarjan, 1987), Dijkstra's algorithm runs in O(m + n log n), which is essentially optimal for sparse graphs. In practice, binary heaps give O((m + n) log n) and are simpler to implement.

OSPF is used in most enterprise and ISP networks worldwide. Every router runs Dijkstra's algorithm to compute its routing table. When a link goes down, routers flood the network with updates and each re-runs Dijkstra — your packets are literally being routed by a 1956 cafe algorithm.

For negative edge weights, you need Bellman-Ford (O(nm)) or, for all-pairs shortest paths, Floyd-Warshall (O(n^3)). Dijkstra with negative edges can give wrong answers — a classic exam pitfall.
-->

---

# Huffman Codes

**Problem:** Compress data using variable-length codes

- Fixed-length: Each character uses same number of bits
- Variable-length: Frequent characters get shorter codes

**Example:** String of 100 characters over $\lbrace a, b, c, d, e, f \rbrace$

| Char | a | b | c | d | e | f |
|------|---|---|---|---|---|---|
| Freq | 44 | 14 | 11 | 17 | 8 | 6 |

Fixed-length: 6 chars → 3 bits each → 300 bits total

<!--
David Huffman invented his coding algorithm in 1952 as a term paper for an MIT course taught by Robert Fano. Fano had been working on a similar problem (Shannon-Fano coding, a top-down approach) and offered students a choice: take the final exam, or find an optimal binary code. Huffman chose the paper, struggled for months, and was about to give up when he hit upon the bottom-up approach. His algorithm turned out to be provably optimal — better than his professor's own method!

Huffman was 27 at the time. He later said he probably wouldn't have even attempted the problem if he had known how hard it was supposed to be. The paper "A Method for the Construction of Minimum-Redundancy Codes" (1952) became one of the foundational papers of information theory.
-->

---

# Prefix Codes

**Prefix code:** No codeword is a prefix of another codeword

**Why prefix codes?**
- Decoding is unambiguous
- No separator needed between codewords
- Any code can be converted to a prefix code (no loss)

**Representation:** Binary tree where:
- Leaves = characters (with frequencies)
- Internal nodes = sum of frequencies in subtree
- Code = path from root (0 = left, 1 = right)

---

# Huffman Tree Example

<div class="grid grid-cols-2 gap-4">
<div>

| Char | Code | Bits |
|------|------|------|
| a | 0 | 1 |
| b | 101 | 3 |
| c | 100 | 3 |
| d | 111 | 3 |
| e | 1101 | 4 |
| f | 1100 | 4 |

</div>
<div class="flex items-center">

<img src="/Figures/huffman.drawio.svg" class="mx-auto h-64" />

</div>
</div>

---

# Computing Total Bits

With variable-length encoding:

$$44 \times 1 + 14 \times 3 + 11 \times 3 + 17 \times 3 + 8 \times 4 + 6 \times 4$$

$= 44 + 42 + 33 + 51 + 32 + 24 = 226$ bits

**Savings:** $300 - 226 = 74$ bits (25% reduction!)

---

# Huffman's Algorithm

```text
n ← |Σ|; Q ← Σ (priority queue by frequency)
for i = 1 to n-1:
    allocate new node z
    left[z] ← x = extract-min(Q)
    right[z] ← y = extract-min(Q)
    f(z) ← f(x) + f(y)
    insert z into Q
return remaining node (root of tree)
```

**Greedy choice:** Always merge the two least frequent nodes!

---

# Huffman: Building the Tree

For $\lbrace a{:}44, b{:}14, c{:}11, d{:}17, e{:}8, f{:}6 \rbrace$:

1. Merge $f(6)$ and $e(8)$ → node with frequency 14
2. Merge $c(11)$ and $b(14)$ → node with frequency 25
3. Merge (fe:14) and $d(17)$ → node with frequency 31
4. Merge (cb:25) and (fed:31) → node with frequency 56
5. Merge $a(44)$ and (cbfed:56) → root with frequency 100

---

# Why Huffman is Optimal

**Key insight:** In an optimal tree:
- The two lowest-frequency characters should be siblings
- They should be at the maximum depth

**Proof idea:**
- If lowest-frequency chars aren't at max depth, swap them with deeper nodes
- This can only decrease total bits
- Huffman builds the tree bottom-up, ensuring this property

---

# Huffman: Complexity

- $n-1$ iterations (merge operations)
- Each iteration: 2 extract-min + 1 insert
- With binary heap: $O(\log n)$ per operation
- **Total:** $O(n \log n)$

**Applications:**
- ZIP, GZIP compression
- JPEG, MP3 (combined with other techniques)
- Many communication protocols

<!--
Huffman coding is everywhere, though often as a building block inside larger compression schemes. In JPEG image compression, the image is first transformed using a Discrete Cosine Transform (DCT), then quantized, and finally the quantized values are Huffman-coded. In MP3 audio, a similar pipeline applies.

ZIP and GZIP use DEFLATE, which combines LZ77 (a dictionary-based method by Lempel and Ziv, 1977) with Huffman coding. The LZ77 step finds repeated patterns; the Huffman step compresses the resulting symbols. This combination is also used in PNG images and HTTP compression.

Morse code (1838) is an early example of variable-length encoding — 'E' is a single dot (most frequent letter in English), while 'Q' is dash-dash-dot-dash. Samuel Morse counted letter frequencies by examining type cases at a local newspaper. Morse code is not a prefix code, which is why it needs pauses between characters.

Shannon's source coding theorem (1948) gives the theoretical limit: you cannot compress below the entropy H of the source. Huffman coding achieves within 1 bit of this limit per symbol, and with block coding (encoding groups of symbols) it can get arbitrarily close.
-->

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

**Look for these properties:**

1. **Greedy choice property:** A locally optimal choice leads to a globally optimal solution

2. **Optimal substructure:** An optimal solution contains optimal solutions to subproblems

3. **Exchange argument:** Can always improve a non-greedy solution to match the greedy choice

4. **"Promising" invariant:** Partial solution can always be extended to optimal

---

# Key Problems

1. **Problem 2.25:** Show greedy make-change fails for $\lbrace 1, 10, 25, 100 \rbrace$

2. **Problem 2.26:** Prove greedy works when $C = \lbrace 1, p, p^2, \ldots, p^k \rbrace$

3. **Problem 2.29:** Find a bipartite graph where greedy matching fails

4. **Problem 2.31:** Design and prove Dijkstra's algorithm in pseudocode

5. **Problem 2.34:** Implement Huffman compression

---

# Summary

- **Make Change:** Greedy doesn't always work! Depends on denominations
- **Shortest Path:** Dijkstra's elegant greedy algorithm, $O(n^2)$
- **Huffman Codes:** Greedy tree construction gives optimal compression
- **Key lesson:** Greedy is simple but requires careful analysis
- **Proof techniques:** Exchange arguments, "promising" invariants

---

# Next Chapter

**Chapter 3: Divide and Conquer**

- Mergesort
- Binary multiplication
- Savitch's algorithm
- Quicksort

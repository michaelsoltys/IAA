---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 1.2.2: Stable Marriage Problem
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Stable Marriage Problem
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

# Stable Marriage Problem

Section 1.2.2 - Ranking Algorithms

---

# Motivation

Real-world matching problems:

<v-clicks>

- Matching **interns** with **hospitals**
- Matching **students** with **colleges**
- The **admission process problem**
- Matching **TAs** with **Slots** at the Learning Resource Center

</v-clicks>

<v-click>

**Goal:** Find a matching that optimizes overall satisfaction of all parties.

</v-click>

<v-click>

This elegant algorithm has been used since the 1960s!

</v-click>

---

# Problem Definition

An instance of the **stable marriage problem** of size $n$:

<v-clicks>

- Set of **boys**: $B = \{b_1, b_2, \ldots, b_n\}$
- Set of **girls**: $G = \{g_1, g_2, \ldots, g_n\}$
- Each boy $b_i$ has a **ranking** $<_i$ of all girls
  - $g <_i g'$ means $b_i$ prefers $g$ over $g'$
- Each girl $g_j$ has a **ranking** $<^j$ of all boys
  - $b <^j b'$ means $g_j$ prefers $b$ over $b'$

</v-clicks>

---

# Matching and Partners

A **matching** (or **marriage**) $M$ is a bijective correspondence between $B$ and $G$.

<v-click>

If $b$ and $g$ are matched in $M$, we say they are **partners**:
- $p_M(b) = g$
- $p_M(g) = b$

</v-click>

---

# Blocking Pairs

A matching $M$ is **unstable** if there exists a **blocking pair**.

<v-click>

A pair $(b, g)$ is a **blocking pair** if:

1. $b$ and $g$ are **not** partners in $M$
2. $b$ prefers $g$ to his current partner $p_M(b)$
3. $g$ prefers $b$ to her current partner $p_M(g)$

</v-click>

<v-click>

<img src="/Figures/BlockingPair.drawio.svg" class="mx-auto h-40" />

Both $b$ and $g$ would rather be with each other than their current partners!

</v-click>

---

# Stable Matching

A matching $M$ is **stable** if it contains **no blocking pairs**.

<v-click>

**Key Question:** Does a stable matching always exist?

</v-click>

<v-click>

**Answer:** Yes! The Gale-Shapley algorithm always produces one.

</v-click>

<v-click>

🏆 **Nobel Prize 2012:** Lloyd S. Shapley and Alvin E. Roth received the Nobel Prize in Economics "for the theory of stable allocations and the practice of market design"

</v-click>

---

# Gale-Shapley Algorithm: Overview

The matching is produced in **stages** $M_1, M_2, \ldots, M_n$

<v-clicks>

**Key properties as stages progress:**

- Boy $b_t$ always has a partner at the end of stage $s$ (for $s \geq t$)
- Partners of boys **do not get better** (from boy's perspective)
- Partners of girls **do not get worse** (from girl's perspective)

</v-clicks>

<v-click>

Boys' situation deteriorates, girls' situation improves!

</v-click>

---

# Gale-Shapley Algorithm: The Idea

At stage $s+1$, boy $b_{s+1}$ tries to get a partner by **proposing** to girls in order of his preference.

<v-click>

When $b_{s+1}$ proposes to girl $g_j$:

</v-click>

<v-clicks>

- **Case 1:** $g_j$ is not engaged → she accepts
- **Case 2:** $g_j$ is engaged to $b$, but prefers $b_{s+1}$ → she breaks off with $b$ and accepts $b_{s+1}$; now $b$ must find a new partner
- **Case 3:** $g_j$ is engaged to $b$ and prefers $b$ → she rejects $b_{s+1}$

</v-clicks>

---

# Gale-Shapley Algorithm

```text
Stage 1: b₁ chooses his top g, M₁ ← {(b₁, g)}

For s = 1 to |B| - 1 (Stage s+1):
    M ← Mₛ
    b* ← bₛ₊₁
    For b* proposes to all g's in order of preference:
        If g was not engaged:
            Mₛ₊₁ ← M ∪ {(b*, g)}
            end current stage
        Else if g was engaged to b but g prefers b*:
            M ← (M - {(b, g)}) ∪ {(b*, g)}
            b* ← b
            repeat from line 6
    Mₛ₊₁ ← M

Return M_{|B|}
```

---

# Example: Preferences

<div class="grid grid-cols-2 gap-4">
<div>

**Boys' preferences:**
| Boy | Ranking |
|-----|---------|
| $b_1$ | $g_2, g_4, g_3, g_1$ |
| $b_2$ | $g_4, g_1, g_2, g_3$ |
| $b_3$ | $g_2, g_1, g_3, g_4$ |
| $b_4$ | $g_3, g_4, g_1, g_2$ |

</div>
<div>

**Girls' preferences:**
| Girl | Ranking |
|------|---------|
| $g_1$ | $b_1, b_3, b_4, b_2$ |
| $g_2$ | $b_3, b_1, b_4, b_2$ |
| $g_3$ | $b_3, b_4, b_1, b_2$ |
| $g_4$ | $b_2, b_1, b_3, b_4$ |

</div>
</div>

---

# Example: Stage 1

$b_1$ chooses his top choice: $g_2$

<v-click>

$$M_1 = \{(b_1, g_2)\}$$

</v-click>

---

# Example: Stage 2

$b^* = b_2$ proposes to $g_4$ (his top choice)

<v-click>

$g_4$ is not engaged → accepts!

</v-click>

<v-click>

$$M_2 = \{(b_1, g_2), (b_2, g_4)\}$$

</v-click>

---

# Example: Stage 3

$b^* = b_3$ proposes to $g_2$ (his top choice)

<v-clicks>

- $g_2$ is engaged to $b_1$
- $g_2$'s ranking: $b_3, b_1, b_4, b_2$ → she prefers $b_3$!
- $g_2$ breaks off with $b_1$, accepts $b_3$
- Now $b^* = b_1$ must find a new partner

</v-clicks>

---

# Example: Stage 3 (continued)

$b^* = b_1$ proposes to $g_4$ (his 2nd choice)

<v-clicks>

- $g_4$ is engaged to $b_2$
- $g_4$'s ranking: $b_2, b_1, b_3, b_4$ → she prefers $b_2$
- $g_4$ rejects $b_1$

</v-clicks>

<v-click>

$b^* = b_1$ proposes to $g_3$ (his 3rd choice)

</v-click>

<v-clicks>

- $g_3$ is not engaged → accepts!

$$M_3 = \{(b_1, g_3), (b_2, g_4), (b_3, g_2)\}$$

</v-clicks>

---

# Example: Stage 4

$b^* = b_4$ proposes to $g_3$ (his top choice)

<v-clicks>

- $g_3$ is engaged to $b_1$
- $g_3$'s ranking: $b_3, b_4, b_1, b_2$ → she prefers $b_4$!
- $g_3$ breaks off with $b_1$, accepts $b_4$
- Now $b^* = b_1$ must find a new partner

</v-clicks>

---

# Example: Stage 4 (continued)

$b^* = b_1$ proposes to $g_1$ (his 4th choice)

<v-click>

$g_1$ is not engaged → accepts!

</v-click>

<v-click>

$$M_4 = \{(b_1, g_1), (b_2, g_4), (b_3, g_2), (b_4, g_3)\}$$

</v-click>

<v-click>

**Final stable matching!**

</v-click>

---

# Why Does It Terminate?

**Key Insight:** Each boy proposes to each girl **at most once**.

<v-clicks>

- Each boy keeps a "bookmark" on his preference list
- The bookmark only moves **forward** (never backward)
- After stage $s$, only $s$ girls are engaged
- Bookmarks must eventually reach a girl who accepts

</v-clicks>

---

# Complexity Analysis

<v-clicks>

- There are $n$ stages
- At stage $s+1$, at most $(s+1)^2$ steps (bookmarks advance)
- Each stage takes $O(n^2)$ steps

</v-clicks>

<v-click>

**Total complexity:** $O(n^3)$

</v-click>

<v-click>

(A "step" = one line of the algorithm: assignment, test, or update)

</v-click>

---

# Optimality Properties

**Definitions:**

<v-clicks>

- A pair $(b, g)$ is **feasible** if there exists a stable matching where $b, g$ are partners
- **Boy-optimal:** every boy is paired with his highest-ranked feasible partner
- **Boy-pessimal:** every boy is paired with his lowest-ranked feasible partner
- Similarly for **girl-optimal/pessimal**

</v-clicks>

---

# Optimality Result

**Theorem:** The Gale-Shapley algorithm (with boys proposing) produces a **boy-optimal** and **girl-pessimal** stable matching.

<v-click>

**Consequence:** The order in which boys propose doesn't matter for the final result!

</v-click>

<v-click>

**To get girl-optimal:** Let the girls propose instead.

</v-click>

---

# Key Problems

<v-clicks>

1. **Problem 1.18:** Show that each $b$ need propose at most once to each $g$

2. **Problem 1.19:** Show that exactly one new girl becomes engaged at each stage, and engaged girls' partners only improve

3. **Problem 1.20:** Show that at stage $n$, $M_n$ is a stable marriage

4. **Problem 1.21:** Show the algorithm produces boy-optimal, girl-pessimal matching

5. **Problem 1.22:** Implement the Gale-Shapley algorithm

</v-clicks>

---

# Summary

<v-clicks>

- **Stable Marriage Problem:** Match boys and girls with no blocking pairs
- **Blocking pair:** Both prefer each other over their current partners
- **Gale-Shapley Algorithm:** Boys propose in order of preference
- **Always terminates** with a stable matching
- **Complexity:** $O(n^3)$
- **Produces boy-optimal, girl-pessimal** matching
- **Nobel Prize 2012!**

</v-clicks>

---

# Applications

<v-clicks>

- **Medical residency matching** (NRMP in the US)
- **College admissions**
- **School choice programs**
- **Kidney exchange programs**
- **Job market matching**

</v-clicks>

<v-click>

The algorithm is still used today to match thousands of medical residents to hospitals every year!

</v-click>

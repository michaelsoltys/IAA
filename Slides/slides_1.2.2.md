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

# Stable Marriage Problem

Section 1.2.2 — Match $n$ boys with $n$ girls so no two would rather elope; a Nobel-winning idea, still matching residents to hospitals today.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Motivation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Where this problem actually shows up — interns, colleges, schools, even kidney exchanges.

</div>

Real-world matching problems:


- Matching **interns** with **hospitals**
- Matching **students** with **colleges**
- The **admission process problem**
- Matching **TAs** with **Slots** at the Learning Resource Center


**Goal:** Find a matching that optimizes overall satisfaction of all parties.


This elegant algorithm has been used since the 1960s!


---

# Problem Definition

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two equal-sized groups, each member with a *strict ranking* of every member of the other group.

</div>

An instance of the **stable marriage problem** of size $n$:


- Set of **boys**: $B = \{b_1, b_2, \ldots, b_n\}$
- Set of **girls**: $G = \{g_1, g_2, \ldots, g_n\}$
- Each boy $b_i$ has a **ranking** $<_i$ of all girls
  - $g <_i g'$ means $b_i$ prefers $g$ over $g'$
- Each girl $g_j$ has a **ranking** $<^j$ of all boys
  - $b <^j b'$ means $g_j$ prefers $b$ over $b'$


---

# Matching and Partners

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A *bijection* between the two sets — every boy paired with exactly one girl, and vice versa.

</div>

A **matching** (or **marriage**) $M$ is a bijective correspondence between $B$ and $G$.


If $b$ and $g$ are matched in $M$, we say they are **partners**:
- $p_M(b) = g$
- $p_M(g) = b$


---

# Blocking Pairs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two people not married to each other but who'd both prefer to be — the matching is unstable.

</div>

A matching $M$ is **unstable** if there exists a **blocking pair**.


A pair $(b, g)$ is a **blocking pair** if:

1. $b$ and $g$ are **not** partners in $M$
2. $b$ prefers $g$ to his current partner $p_M(b)$
3. $g$ prefers $b$ to her current partner $p_M(g)$


<img src="/Figures/BlockingPair.drawio.svg" class="mx-auto h-40" />

Both $b$ and $g$ would rather be with each other than their current partners!


---

# Stable Matching

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

No blocking pairs means nobody can defect — a stable matching always exists, and we can build one efficiently.

</div>

A matching $M$ is **stable** if it contains **no blocking pairs**.


**Key Question:** Does a stable matching always exist?


**Answer:** Yes! The Gale-Shapley algorithm always produces one.


🏆 **Nobel Prize 2012:** Lloyd S. Shapley and Alvin E. Roth received the Nobel Prize in Economics "for the theory of stable allocations and the practice of market design"


---

# Gale-Shapley Algorithm: Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Boys join the matching one at a time; with each stage, *boys settle for less*, *girls trade up*.

</div>

The matching is produced in **stages** $M_1, M_2, \ldots, M_n$


**Key properties as stages progress:**

- Boy $b_t$ always has a partner at the end of stage $s$ (for $s \geq t$)
- Partners of boys **do not get better** (from boy's perspective)
- Partners of girls **do not get worse** (from girl's perspective)


Boys' situation deteriorates, girls' situation improves!


---

# Gale-Shapley Algorithm: The Idea

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Each new boy proposes down his list; girls accept, reject, or *trade up* — bumped boys keep proposing.

</div>

At stage $s+1$, boy $b_{s+1}$ tries to get a partner by **proposing** to girls in order of his preference.


When $b_{s+1}$ proposes to girl $g_j$:


- **Case 1:** $g_j$ is not engaged → she accepts
- **Case 2:** $g_j$ is engaged to $b$, but prefers $b_{s+1}$ → she breaks off with $b$ and accepts $b_{s+1}$; now $b$ must find a new partner
- **Case 3:** $g_j$ is engaged to $b$ and prefers $b$ → she rejects $b_{s+1}$


---

# Gale-Shapley Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The pseudocode — three cases per proposal, an outer loop over stages, and we're done in $O(n^3)$.

</div>

<span style="font-size: 0.6em; color: navy;">Alg 7, Pg 16, alg:gale-shapley</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Algorithms/A7_Gale-Shapley.py" style="font-size: 0.6em; color: teal;">[Python implementation]</a>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A small instance with $n=4$ to trace by hand — note nobody's first choice is mutual.

</div>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The first boy walks in, picks his favorite — easy, no competition yet.

</div>

$b_1$ chooses his top choice: $g_2$


$$M_1 = \{(b_1, g_2)\}$$


---

# Example: Stage 2

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$b_2$ proposes to a *different* girl — clean acceptance, no displacement yet.

</div>

$b^* = b_2$ proposes to $g_4$ (his top choice)


$g_4$ is not engaged → accepts!


$$M_2 = \{(b_1, g_2), (b_2, g_4)\}$$


---

# Example: Stage 3

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

First conflict — $b_3$ wants $g_2$ who's engaged to $b_1$, and $g_2$ trades up.

</div>

$b^* = b_3$ proposes to $g_2$ (his top choice)


- $g_2$ is engaged to $b_1$
- $g_2$'s ranking: $b_3, b_1, b_4, b_2$ → she prefers $b_3$!
- $g_2$ breaks off with $b_1$, accepts $b_3$
- Now $b^* = b_1$ must find a new partner


---

# Example: Stage 3 (continued)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The displaced $b_1$ proposes to his 2nd choice — gets rejected — moves on to his 3rd.

</div>

$b^* = b_1$ proposes to $g_4$ (his 2nd choice)


- $g_4$ is engaged to $b_2$
- $g_4$'s ranking: $b_2, b_1, b_3, b_4$ → she prefers $b_2$
- $g_4$ rejects $b_1$


$b^* = b_1$ proposes to $g_3$ (his 3rd choice)


- $g_3$ is not engaged → accepts!

$$M_3 = \{(b_1, g_3), (b_2, g_4), (b_3, g_2)\}$$


---

# Example: Stage 4

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$b_4$ enters and bumps $b_1$ — *again* — sending poor $b_1$ back to the drawing board.

</div>

$b^* = b_4$ proposes to $g_3$ (his top choice)


- $g_3$ is engaged to $b_1$
- $g_3$'s ranking: $b_3, b_4, b_1, b_2$ → she prefers $b_4$!
- $g_3$ breaks off with $b_1$, accepts $b_4$
- Now $b^* = b_1$ must find a new partner


---

# Example: Stage 4 (continued)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$b_1$ ends up with his *last* choice — a stable matching, but a humbling one for him.

</div>

$b^* = b_1$ proposes to $g_1$ (his 4th choice)


$g_1$ is not engaged → accepts!


$$M_4 = \{(b_1, g_1), (b_2, g_4), (b_3, g_2), (b_4, g_3)\}$$


**Final stable matching!**


---

# Why Does It Terminate?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Bookmarks only move forward — at most $n^2$ proposals before everyone's paired up.

</div>

**Key Insight:** Each boy proposes to each girl **at most once**.


- Each boy keeps a "bookmark" on his preference list
- The bookmark only moves **forward** (never backward)
- After stage $s$, only $s$ girls are engaged
- Bookmarks must eventually reach a girl who accepts


---

# Complexity Analysis

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$n$ stages, each $O(n^2)$, gives $O(n^3)$ — well within reach for matching tens of thousands of residents.

</div>


- There are $n$ stages
- At stage $s+1$, at most $(s+1)^2$ steps (bookmarks advance)
- Each stage takes $O(n^2)$ steps


**Total complexity:** $O(n^3)$


(A "step" = one line of the algorithm: assignment, test, or update)


---

# Optimality Properties

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

There can be many stable matchings — which one is *best*, and best for whom?

</div>

**Definitions:**


- A pair $(b, g)$ is **feasible** if there exists a stable matching where $b, g$ are partners
- **Boy-optimal:** every boy is paired with his highest-ranked feasible partner
- **Boy-pessimal:** every boy is paired with his lowest-ranked feasible partner
- Similarly for **girl-optimal/pessimal**


---

# Optimality Result

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The proposers win, the receivers lose — *who* proposes determines whose side gets the best deal.

</div>

**Theorem:** The Gale-Shapley algorithm (with boys proposing) produces a **boy-optimal** and **girl-pessimal** stable matching. <span style="font-size: 0.6em; color: navy;">Thm 1.24, Pg 19, thm:saaty</span>


**Consequence:** The order in which boys propose doesn't matter for the final result!


**To get girl-optimal:** Let the girls propose instead.


---

# Key Problems

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The exercises that prove the invariants and the optimality theorem — plus a coding assignment.

</div>


1. **Problem 1.19:** Show that exactly one new girl becomes engaged at each stage, and engaged girls' partners only improve <span style="font-size: 0.6em; color: navy;">Prb 1.19, Pg 16, exr:girls2</span>

2. **Problem 1.20:** Show that at stage $n$, $M_n$ is a stable marriage <span style="font-size: 0.6em; color: navy;">Prb 1.20, Pg 17, exr:girls1</span>

3. **Problem 1.21:** Show the algorithm produces boy-optimal, girl-pessimal matching <span style="font-size: 0.6em; color: navy;">Prb 1.21, Pg 17, exr:girls3</span>

4. **Problem 1.22:** Implement the Gale-Shapley algorithm <span style="font-size: 0.6em; color: navy;">Prb 1.22, Pg 17, exr:girls4</span>

5. **Problem 1.23:** Show that each $b$ need propose at most once to each $g$ <span style="font-size: 0.6em; color: navy;">Prb 1.23, Pg 17, exr:gale-shapley</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Problems/P1.23_Gale-Shapley_1.py" style="font-size: 0.6em; color: teal;">[Python solution]</a>


---

# Applications

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A 1962 paper, still placing thousands of doctors and students every year — and saving lives via kidney chains.

</div>


- **Medical residency matching** (NRMP in the US)
- **College admissions**
- **School choice programs**
- **Kidney exchange programs**
- **Job market matching**


The algorithm is still used today to match thousands of medical residents to hospitals every year!

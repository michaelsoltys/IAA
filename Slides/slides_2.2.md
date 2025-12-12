---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 2.2: Jobs with Deadlines and Profits
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Jobs with Deadlines and Profits
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

# Jobs with Deadlines and Profits

Section 2.2 - Greedy Algorithms

---

# Problem Setup

<v-clicks>

- **$n$ jobs**, each takes **unit time**
- **One processor** to schedule them sequentially
- Each job $i$ has:
  - **Profit** $g_i \in \mathbb{R}^+$ (gain if completed)
  - **Deadline** $d_i \in \mathbb{N}$ (must finish by this time)
- If a job is not scheduled by its deadline → **no profit**

</v-clicks>

<v-click>

**Goal:** Find a schedule that maximizes total profit!

</v-click>

---

# What is a Schedule?

A **schedule** $S$ is an array $S(1), S(2), \ldots, S(d)$ where:

<v-clicks>

- $d = \max_i d_i$ (latest deadline)
- $S(t) = i$ means job $i$ is scheduled at time $t$
- $S(t) = 0$ means no job is scheduled at time $t$

</v-clicks>

<v-click>

Think of it as "slots": $|\ \ |\ \ |\ \ |\ \ |\ \ |$

Each slot can hold at most one job.

</v-click>

---

# Feasible Schedules

A schedule $S$ is **feasible** if it satisfies two conditions:

<v-clicks>

**Condition 1:** Every scheduled job meets its deadline
$$S(t) = i > 0 \Rightarrow t \leq d_i$$

**Condition 2:** Each job is scheduled at most once
$$t_1 \neq t_2 \text{ and } S(t_1) \neq 0 \Rightarrow S(t_1) \neq S(t_2)$$

</v-clicks>

<v-click>

**Total profit:** $P(S) = \sum_{t=1}^{d} g_{S(t)}$ where $g_0 = 0$

</v-click>

---

# The Greedy Algorithm

```text
Job Scheduling Algorithm:
1. Sort jobs by non-increasing profit: g₁ ≥ g₂ ≥ ... ≥ gₙ
2. d ← max_i dᵢ
3. for t = 1 to d:
4.     S(t) ← 0
5. for i = 1 to n:
6.     Find largest t such that S(t) = 0 and t ≤ dᵢ
7.     S(t) ← i
8. return S
```

<v-click>

**Key idea:** Process jobs in order of decreasing profit, schedule each as **late as possible** within its deadline.

</v-click>

<v-click>

A scientific confirmation of the benefits of **procrastination**!

</v-click>

---

# Example

Jobs: $(d_1, g_1) = (1, 10)$, $(d_2, g_2) = (1, 10)$, $(d_3, g_3) = (2, 8)$, $(d_4, g_4) = (2, 8)$

<v-clicks>

- Latest deadline $d = 2$, so slots: $|\ \ |\ \ |$
- Job 1 ($g=10$, $d=1$): Schedule at slot 1 → $|1|\ |$
- Job 2 ($g=10$, $d=1$): Slot 1 full, can't schedule before deadline
- Job 3 ($g=8$, $d=2$): Schedule at slot 2 → $|1|3|$
- Job 4 ($g=8$, $d=2$): No free slots before deadline

</v-clicks>

<v-click>

**Final:** $S = (1, 3)$ with profit $P(S) = 10 + 8 = 18$

</v-click>

---

# Why Does This Work?

**Theorem:** The greedy solution to job scheduling is optimal.

<v-click>

**Proof approach:** Same as Kruskal's algorithm!

Show that "$S$ is promising" is a loop invariant.

</v-click>

---

# Promising Schedules

**Definition:** Schedule $S'$ **extends** schedule $S$ if:
- For all $t$: if $S(t) \neq 0$, then $S(t) = S'(t)$

<v-click>

Example: $S' = (2, 0, 1, 0, 3)$ extends $S = (2, 0, 0, 0, 3)$

</v-click>

<v-click>

**Definition:** $S$ is **promising** if it can be extended to an optimal schedule using jobs not yet considered.

</v-click>

---

# The Loop Invariant

**Lemma:** "$S$ is promising" is an invariant for the for-loop in the job scheduling algorithm.

<v-click>

**Basis case:** After 0 iterations, $S = (0, 0, \ldots, 0)$
- Can extend to any optimal schedule using all jobs
- So $S$ is promising ✓

</v-click>

---

# Induction Step Setup

Suppose $S$ is promising, and let $S_{\text{opt}}$ be some optimal schedule extending $S$.

Let $S'$ be the result after considering job $i$.

<v-click>

**Goal:** Show there exists optimal $S'_{\text{opt}}$ extending $S'$.

```
S     = |   | 0 |   | 0 |   | j |   |   |
S_opt = |   | 0 |   | i |   | j |   |   |
```

If $S$ has job $j$ somewhere, $S_{\text{opt}}$ has $j$ in the same position.

</v-click>

---

# Case 1: Job Cannot Be Scheduled

Job $i$ cannot be scheduled (no free slot before deadline).

<v-click>

Then $S' = S$.

</v-click>

<v-click>

Let $S'_{\text{opt}} = S_{\text{opt}}$.

</v-click>

<v-click>

**Subtle point:** $S$ was extendable using jobs $\{i, i+1, \ldots, n\}$, but now we can't use job $i$.

But that's OK! If $S_{\text{opt}}$ used job $i$, there would have been a free slot in $S$ for it (contradiction).

</v-click>

---

# Case 2: Job is Scheduled

Job $i$ is scheduled at time $t_0$ (latest possible free slot).

So $S'(t_0) = i$ where $S(t_0) = 0$.

<v-click>

**Two subcases:**
- (a) Job $i$ is in $S_{\text{opt}}$ at some time $t_1$
- (b) Job $i$ is not in $S_{\text{opt}}$

</v-click>

---

# Subcase 2a: Job $i$ in $S_{\text{opt}}$

Job $i$ is scheduled in $S_{\text{opt}}$ at time $t_1$.

<v-clicks>

**If $t_1 = t_0$:** Let $S'_{\text{opt}} = S_{\text{opt}}$ ✓

**If $t_1 < t_0$:** Swap positions $t_0$ and $t_1$ in $S_{\text{opt}}$
- $S'_{\text{opt}}(t_0) = S_{\text{opt}}(t_1) = i$
- $S'_{\text{opt}}(t_1) = S_{\text{opt}}(t_0)$
- Still feasible (why?)
- Still extends $S'$ (why?)
- Same profit (just swapped)

**If $t_1 > t_0$:** Not possible! ($t_0$ was the latest possible slot)

</v-clicks>

---

# Subcase 2b: Job $i$ Not in $S_{\text{opt}}$

Job $i$ is not scheduled in $S_{\text{opt}}$.

<v-click>

Define $S'_{\text{opt}}$ same as $S_{\text{opt}}$, except $S'_{\text{opt}}(t_0) = i$.

</v-click>

<v-click>

Must show: $P(S'_{\text{opt}}) = P(S_{\text{opt}})$

</v-click>

<v-click>

**Claim:** Let $S_{\text{opt}}(t_0) = j$. Then $g_j \leq g_i$.

</v-click>

<v-click>

If $g_j > g_i$, then job $j$ was considered before job $i$...

</v-click>

---

# Proving the Claim

Assume for contradiction: $g_j > g_i$ (so $j \neq 0$).

<v-clicks>

- Job $j$ was considered before job $i$ (higher profit)
- Since job $i$ was scheduled at $t_0$, and $S(t_0) = 0$...
- ...job $j$ must have been scheduled at some $t_2 \neq t_0$
- (We know $j$ was scheduled in $S$ since $t_0 \leq d_j$)
- So $S(t_2) = j$
- But $S_{\text{opt}}$ extends $S$, so $S_{\text{opt}}(t_2) = j$
- Yet we said $S_{\text{opt}}(t_0) = j$
- **Contradiction!** (job scheduled twice)

</v-clicks>

---

# Completing the Proof

Since $g_j \leq g_i$:

<v-clicks>

- $P(S'_{\text{opt}}) = P(S_{\text{opt}}) - g_j + g_i \geq P(S_{\text{opt}})$
- But $S_{\text{opt}}$ was optimal
- So $P(S'_{\text{opt}}) = P(S_{\text{opt}})$
- Therefore $S'_{\text{opt}}$ is also optimal and extends $S'$ ✓

</v-clicks>

<v-click>

This completes the induction step, proving the loop invariant.

After the algorithm terminates, $S$ is promising and all jobs considered → $S$ is optimal!

</v-click>

---

# Detailed Example

Input (already sorted by profit):

| Job | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-----|---|---|---|---|---|---|---|---|
| $d_i$ | 1 | 1 | 2 | 2 | 4 | 4 | 4 | 4 |
| $g_i$ | 10 | 10 | 8 | 8 | 6 | 6 | 6 | 6 |

<v-click>

Latest deadline $d = 4$, so schedule has 4 slots.

</v-click>

<v-click>

Trace: Starting with $S = (0, 0, 0, 0)$

</v-click>

---

# Example Trace

| Step | Job | Deadline | Action | Schedule |
|------|-----|----------|--------|----------|
| 0 | — | — | Initialize | $(0, 0, 0, 0)$ |
| 1 | 1 | 1 | Place at slot 1 | $(1, 0, 0, 0)$ |
| 2 | 2 | 1 | Can't place | $(1, 0, 0, 0)$ |
| 3 | 3 | 2 | Place at slot 2 | $(1, 3, 0, 0)$ |
| 4 | 4 | 2 | Can't place | $(1, 3, 0, 0)$ |
| 5 | 5 | 4 | Place at slot 4 | $(1, 3, 0, 5)$ |
| 6 | 6 | 4 | Place at slot 3 | $(1, 3, 6, 5)$ |
| 7 | 7 | 4 | Can't place | $(1, 3, 6, 5)$ |
| 8 | 8 | 4 | Can't place | $(1, 3, 6, 5)$ |

<v-click>

**Final profit:** $10 + 8 + 6 + 6 = 30$

</v-click>

---

# Key Problems

<v-clicks>

1. **Problem 2.17:** Trace the algorithm on a given input, showing how "promising" is maintained

2. **Problem 2.18:** Why does the loop invariant imply the theorem?

3. **Problem 2.19:** Answer all the "why's" in the proof

4. **Problem 2.20:** Under what conditions is there a unique optimal schedule?

5. **Problem 2.15:** Implement the job scheduling algorithm

</v-clicks>

---

# Summary

<v-clicks>

- **Problem:** Schedule unit-time jobs with deadlines to maximize profit
- **Greedy approach:** Process by decreasing profit, schedule as late as possible
- **Key invariant:** "$S$ is promising"
- **Proof technique:** Same as Kruskal's - show we can adjust optimal solution
- **Complexity:** $O(n \log n)$ for sorting + $O(nd)$ for scheduling
- Procrastination pays off (mathematically)!

</v-clicks>

---

# What's Different from MCST?

<v-clicks>

Both use "promising" as a loop invariant, but:

| MCST (Kruskal) | Job Scheduling |
|----------------|----------------|
| Add cheapest edge | Add most profitable job |
| Avoid cycles | Respect deadlines |
| Use Exchange Lemma | Use swap argument |
| Build up a tree | Fill schedule slots |

Same proof structure, different problem!

</v-clicks>

---

# Next: Further Greedy Examples

- Make Change
- Shortest Path (Dijkstra)
- Huffman Codes

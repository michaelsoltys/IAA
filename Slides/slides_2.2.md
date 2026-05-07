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

# Jobs with Deadlines and Profits

Section 2.2 — Schedule unit-time jobs to maximize profit, by *procrastinating* — pack the high-value jobs as late as possible.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Problem Setup

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

One processor, $n$ jobs, each with a deadline and a payoff — what's the most money we can make?

</div>


- **$n$ jobs**, each takes **unit time**
- **One processor** to schedule them sequentially
- Each job $i$ has:
  - **Profit** $g_i \in \mathbb{R}^+$ (gain if completed)
  - **Deadline** $d_i \in \mathbb{N}$ (must finish by this time)
- If a job is not scheduled by its deadline → **no profit**


**Goal:** Find a schedule that maximizes total profit!


---

# What is a Schedule?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

An array of $d$ slots — each holds a job ID or zero, with $d$ being the latest deadline among all jobs.

</div>

A **schedule** $S$ is an array $S(1), S(2), \ldots, S(d)$ where:


- $d = \max_i d_i$ (latest deadline)
- $S(t) = i$ means job $i$ is scheduled at time $t$
- $S(t) = 0$ means no job is scheduled at time $t$


<img src="/Figures/slots.drawio.svg" class="mx-auto h-12 my-4" />

Each slot can hold at most one job.


---

# Feasible Schedules

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two rules — meet every deadline, no job twice — and we measure success by total profit.

</div>

A schedule $S$ is **feasible** if it satisfies two conditions:


**Condition 1:** Every scheduled job meets its deadline
$$S(t) = i > 0 \Rightarrow t \leq d_i$$

**Condition 2:** Each job is scheduled at most once
$$t_1 \neq t_2 \text{ and } S(t_1) \neq 0 \Rightarrow S(t_1) \neq S(t_2)$$


**Total profit:** $P(S) = \sum_{t=1}^{d} g_{S(t)}$ where $g_0 = 0$


---

# The Greedy Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Take jobs in *decreasing profit order* and schedule each as *late as it'll fit* — procrastination, optimized.

</div>

<span style="font-size: 0.6em; color: navy;">Alg 12, Pg 42, alg:jobs</span>

Job scheduling algorithm:
```text
Sort jobs by non-increasing profit: g₁ ≥ g₂ ≥ ... ≥ gₙ
d ← max_i dᵢ
for t = 1 to d:
    S(t) ← 0
for i = 1 to n:
    Find largest t such that S(t) = 0 and t ≤ dᵢ
    S(t) ← i
return S
```


**Key idea:** Process jobs in order of decreasing profit, schedule each as **late as possible** within its deadline.


A scientific confirmation of the benefits of **procrastination**!


---

# Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Four jobs, two slots — we get the *two highest payouts* and skip the cheaper duplicates.

</div>

<div class="grid grid-cols-2 gap-4">
<div>

Jobs: $(d_1, g_1) = (1, 10)$, $(d_2, g_2) = (1, 10)$, $(d_3, g_3) = (2, 8)$, $(d_4, g_4) = (2, 8)$


- Latest deadline $d = 2$
- Job 1 ($g=10$, $d=1$): slot 1
- Job 2 ($g=10$, $d=1$): can't schedule
- Job 3 ($g=8$, $d=2$): slot 2
- Job 4 ($g=8$, $d=2$): can't schedule


**Final:** $S = (1, 3)$, profit $= 18$


</div>
<div class="flex items-center">

<img src="/Figures/slots-3.drawio.svg" class="mx-auto h-48" />

</div>
</div>

---

# Why Does This Work?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Same trick as Kruskal — *promising* is the loop invariant, just with schedules instead of edge sets.

</div>

**Theorem:** The greedy solution to job scheduling is optimal. <span style="font-size: 0.6em; color: navy;">Thm 2.18, Pg 42, thm:theorem1</span>


**Proof approach:** Same as Kruskal's algorithm!

Show that "$S$ is promising" is a loop invariant.


---

# Promising Schedules

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

"Extends" is the schedule version of "is a subset of" — and *promising* means extendable to an optimum.

</div>

**Definition:** Schedule $S'$ **extends** schedule $S$ if:
- For all $t$: if $S(t) \neq 0$, then $S(t) = S'(t)$


Example: $S' = (2, 0, 1, 0, 3)$ extends $S = (2, 0, 0, 0, 3)$


**Definition:** $S$ is **promising** if it can be extended to an optimal schedule using jobs not yet considered.


---

# The Loop Invariant

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The empty schedule is trivially promising — we just need to maintain that property through each job.

</div>

**Lemma:** "$S$ is promising" is an invariant for the for-loop in the job scheduling algorithm. <span style="font-size: 0.6em; color: navy;">Lem 2.19, Pg 42, lem:lemma1</span>


**Basis case:** After 0 iterations, $S = (0, 0, \ldots, 0)$
- Can extend to any optimal schedule using all jobs
- So $S$ is promising ✓


---

# Induction Step Setup

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Pick any optimal $S_{\text{opt}}$ that extends $S$ — we'll modify it to extend $S'$ without losing profit.

</div>

Suppose $S$ is promising, and let $S_{\text{opt}}$ be some optimal schedule extending $S$.

Let $S'$ be the result after considering job $i$.


**Goal:** Show there exists optimal $S'_{\text{opt}}$ extending $S'$.

<img src="/Figures/slots-2.drawio.svg" class="mx-auto h-24 my-4" />

If $S$ has job $j$ somewhere, $S_{\text{opt}}$ has $j$ in the same position.


---

# Case 1: Job Cannot Be Scheduled

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If we couldn't fit job $i$, neither could $S_{\text{opt}}$ — so the witness needs no surgery.

</div>

Job $i$ cannot be scheduled (no free slot before deadline).


Then $S' = S$.


Let $S'_{\text{opt}} = S_{\text{opt}}$.


**Subtle point:** $S$ was extendable using jobs $\{i, i+1, \ldots, n\}$, but now we can't use job $i$.

But that's OK! If $S_{\text{opt}}$ used job $i$, there would have been a free slot in $S$ for it (contradiction).


---

# Case 2: Job is Scheduled

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

We placed job $i$ at $t_0$ — now split on whether the witness $S_{\text{opt}}$ also uses job $i$.

</div>

Job $i$ is scheduled at time $t_0$ (latest possible free slot).

So $S'(t_0) = i$ where $S(t_0) = 0$.


**Two subcases:**
- (a) Job $i$ is in $S_{\text{opt}}$ at some time $t_1$
- (b) Job $i$ is not in $S_{\text{opt}}$


---

# Subcase 2a: Job $i$ in $S_{\text{opt}}$

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If $S_{\text{opt}}$ scheduled job $i$ earlier, swap it with whatever's at $t_0$ — same profit, still feasible.

</div>

Job $i$ is scheduled in $S_{\text{opt}}$ at time $t_1$.


**If $t_1 = t_0$:** Let $S'_{\text{opt}} = S_{\text{opt}}$ ✓

**If $t_1 < t_0$:** Swap positions $t_0$ and $t_1$ in $S_{\text{opt}}$
- $S'_{\text{opt}}(t_0) = S_{\text{opt}}(t_1) = i$
- $S'_{\text{opt}}(t_1) = S_{\text{opt}}(t_0)$
- Still feasible (why?)
- Still extends $S'$ (why?)
- Same profit (just swapped)

**If $t_1 > t_0$:** Not possible! ($t_0$ was the latest possible slot)


---

# Subcase 2b: Job $i$ Not in $S_{\text{opt}}$

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Drop whatever $S_{\text{opt}}$ had at $t_0$, replace it with $i$ — and now we owe a proof of "no profit lost."

</div>

Job $i$ is not scheduled in $S_{\text{opt}}$.


Define $S'_{\text{opt}}$ same as $S_{\text{opt}}$, except $S'_{\text{opt}}(t_0) = i$.


Must show: $P(S'_{\text{opt}}) = P(S_{\text{opt}})$


**Claim:** Let $S_{\text{opt}}(t_0) = j$. Then $g_j \leq g_i$.


If $g_j > g_i$, then job $j$ was considered before job $i$...


---

# Proving the Claim

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If a higher-profit job $j$ were sitting at $t_0$, we'd have scheduled it ourselves earlier — contradiction.

</div>

Assume for contradiction: $g_j > g_i$ (so $j \neq 0$).


- Job $j$ was considered before job $i$ (higher profit)
- Since job $i$ was scheduled at $t_0$, and $S(t_0) = 0$...
- ...job $j$ must have been scheduled at some $t_2 \neq t_0$
- (We know $j$ was scheduled in $S$ since $t_0 \leq d_j$)
- So $S(t_2) = j$
- But $S_{\text{opt}}$ extends $S$, so $S_{\text{opt}}(t_2) = j$
- Yet we said $S_{\text{opt}}(t_0) = j$
- **Contradiction!** (job scheduled twice)


---

# Completing the Proof

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The swap can only *increase* profit; combined with $S_{\text{opt}}$'s optimality, equality must hold.

</div>

Since $g_j \leq g_i$:


- $P(S'_{\text{opt}}) = P(S_{\text{opt}}) - g_j + g_i \geq P(S_{\text{opt}})$
- But $S_{\text{opt}}$ was optimal
- So $P(S'_{\text{opt}}) = P(S_{\text{opt}})$
- Therefore $S'_{\text{opt}}$ is also optimal and extends $S'$ ✓


This completes the induction step, proving the loop invariant.

After the algorithm terminates, $S$ is promising and all jobs considered → $S$ is optimal!


---

# Detailed Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Eight jobs, four slots — pre-sorted by profit so we can focus on the *placement* dynamics.

</div>

Input (already sorted by profit):

| Job | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-----|---|---|---|---|---|---|---|---|
| $d_i$ | 1 | 1 | 2 | 2 | 4 | 4 | 4 | 4 |
| $g_i$ | 10 | 10 | 8 | 8 | 6 | 6 | 6 | 6 |


Latest deadline $d = 4$, so schedule has 4 slots.


Trace: Starting with $S = (0, 0, 0, 0)$


---

# Example Trace

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Watch the slots fill up *from the right* — late slots first, exactly as the algorithm prescribes.

</div>

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


**Final profit:** $10 + 8 + 6 + 6 = 30$


---

# Key Problems

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Trace the algorithm, plug holes in the proof, and uniqueness questions about the optimum.

</div>


1. **Problem 2.17:** Trace the algorithm on a given input, showing how "promising" is maintained <span style="font-size: 0.6em; color: navy;">Prb 2.17, Pg 42, exr:job_scheduling</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Problems/P2.17_Job-Scheduling.py" style="font-size: 0.6em; color: teal;">[Python solution]</a>

2. **Problem 2.20:** Under what conditions is there a unique optimal schedule? <span style="font-size: 0.6em; color: navy;">Prb 2.20, Pg 42, prb:jobsexm</span>

3. **Problem 2.21:** Why does the loop invariant imply the theorem? <span style="font-size: 0.6em; color: navy;">Prb 2.21, Pg 43, exr:lemma1</span>

4. **Problem 2.22:** Discuss the subtle point in Case 1 of the proof <span style="font-size: 0.6em; color: navy;">Prb 2.22, Pg 43, prb:subtle</span>

5. **Problem 2.24:** Answer all the "why's" in the proof <span style="font-size: 0.6em; color: navy;">Prb 2.24, Pg 44, exr:whys</span>


---

# What's Different from MCST?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Same template, different swap — Kruskal uses Exchange Lemma, this one swaps slots in a schedule.

</div>


Both use "promising" as a loop invariant, but:

| MCST (Kruskal) | Job Scheduling |
|----------------|----------------|
| Add cheapest edge | Add most profitable job |
| Avoid cycles | Respect deadlines |
| Use Exchange Lemma | Use swap argument |
| Build up a tree | Fill schedule slots |

Same proof structure, different problem!


---

# Next: Further Greedy Examples

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three more — coins, paths, codes — where greedy sometimes triumphs and sometimes embarrassingly fails.

</div>

- Make Change
- Shortest Path (Dijkstra)
- Huffman Codes

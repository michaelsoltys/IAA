---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 3.1: Mergesort
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Mergesort
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

# Mergesort

Section 3.1 — The original divide-and-conquer sort: $O(n \log n)$, stable, optimal.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

<!--
Mergesort was invented by **John von Neumann in 1945**, making it one of the earliest algorithms written for a stored-program computer. He described it in a 23-page report on the EDVAC — before the machine was even built. It may be the first O(n log n) sorting algorithm ever implemented.
-->

---

# The Merging Problem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The subroutine that makes mergesort work — fuse two sorted lists into one in linear time.

</div>

Suppose we have **two sorted lists**:

$$a_1 \leq a_2 \leq \cdots \leq a_n \quad \text{and} \quad b_1 \leq b_2 \leq \cdots \leq b_m$$


**Goal:** Combine them into one sorted list:

$$c_1 \leq c_2 \leq \cdots \leq c_{n+m}$$


---

# Sorting Algorithms

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A quick zoo of the classics — who's $O(n^2)$, who's $O(n \log n)$, and who's stable.

</div>

| Algorithm | Strategy | Time (avg) | Time (worst) | Stable? |
|-----------|----------|:----------:|:------------:|:-------:|
| **Insertion sort** | Insert each item in its proper position | $O(n^2)$ | $O(n^2)$ | Yes |
| **Selection sort** | Find minimum, swap to front, repeat | $O(n^2)$ | $O(n^2)$ | No |
| **Bubble sort** | Swap adjacent pairs, repeat until sorted | $O(n^2)$ | $O(n^2)$ | Yes |
| **Mergesort** | Divide in half, sort each, merge | $O(n \log n)$ | $O(n \log n)$ | Yes |
| **Quicksort** | Pick pivot, partition, recurse <span style="font-size: 0.6em; color: navy;">Prb 3.12, Pg 69, exr:quicksort</span> | $O(n \log n)$ | $O(n^2)$ | No |
| **Heapsort** | Like selection sort, but using a heap | $O(n \log n)$ | $O(n \log n)$ | No |


Mergesort and Quicksort are both **divide and conquer** algorithms. This chapter focuses on **Mergesort**.


<!--
**Stable sorting:** A sorting algorithm is *stable* if it preserves the relative order of elements with equal keys. For example, if two records have the same sort key, a stable sort guarantees they appear in the same order in the output as they did in the input. This matters when sorting by multiple criteria — e.g., sort by name, then by age; stability ensures names stay alphabetical within the same age group.

**Why is selection sort unstable?** Consider [3a, 2, 3b, 1]. Selection sort swaps 1 with 3a, giving [1, 2, 3b, 3a] — the two 3s are now reversed.

**Why is quicksort unstable?** Partitioning can swap equal elements across the pivot.

**Timsort:** Python's built-in `sort()` uses **Timsort** (created by Tim Peters in 2002), a hybrid of mergesort and insertion sort. It exploits existing "runs" of sorted data in real-world inputs. Timsort was so successful it was adopted by Java (2011), Android, Swift, and Rust. The fact that mergesort is stable was a key reason it (rather than quicksort) was chosen as the basis.

**External sorting:** In the 1950s–60s, data lived on magnetic tape, which could only be read sequentially. Mergesort's sequential access pattern made it the natural choice for sorting data too large to fit in memory. This is still the basis for "external merge sort" used today when sorting massive datasets (e.g., database engines, Hadoop MapReduce's shuffle phase).
-->

---

# Merge Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two pointers march down the input lists, always copying the smaller head to the output.

</div>

A sorting algorithm

Merge Two Lists:

<span style="font-size: 0.6em; color: navy;">Alg 16, Pg 62, alg:merge</span>

```text
  Pre-condition: a₁ ≤ a₂ ≤ ··· ≤ aₙ and b₁ ≤ b₂ ≤ ··· ≤ bₘ
  p₁ ← 1; p₂ ← 1; i ← 1
  while i ≤ n + m:
    if a[p₁] ≤ b[p₂]:
      c[i] ← a[p₁]
      p₁ ← p₁ + 1
    else:
      c[i] ← b[p₂]
      p₂ ← p₂ + 1
    i ← i + 1
  Post-condition: c₁ ≤ c₂ ≤ ··· ≤ c_{n+m}
```


**Complexity:** $O(n + m)$ — each element is compared at most once


<!--
**Linked lists:** Mergesort is often considered the best algorithm for sorting linked lists. Unlike quicksort or heapsort, it doesn't need random access — only sequential traversal and pointer manipulation. It can sort a linked list in O(n log n) time with O(1) extra space (no auxiliary array needed).
-->

---

# A Subtle Bug

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A textbook reminder: the obvious loop reads past the end of one array — easy to miss, easy to fix.

</div>

The Merge algorithm as stated is **incorrect**!


**Problem:** If all elements of $a$ are smaller than $b_1$, then after $n$ iterations $p_1 = n + 1$, and checking $a_{p_1} \leq b_{p_2}$ causes an **out-of-bounds** error.


**Fix:** Change the while-loop condition to $p_1 \leq n \wedge p_2 \leq m$, then add a cleanup loop to copy remaining elements.


---

# The Mergesort Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Split the list in half, recurse on each half, then merge — three lines and you're sorted.

</div>

<span style="font-size: 0.6em; color: navy;">Alg 17, Pg 63, alg:mergesort</span>

```text
Mergesort:
  Pre-condition: A list of integers a₁, a₂, ..., aₙ
  L ← a₁, a₂, ..., aₙ
  if |L| ≤ 1:
    return L
  else:
    L₁ ← first ⌈n/2⌉ elements of L
    L₂ ← last  ⌊n/2⌋ elements of L
    return Merge(Mergesort(L₁), Mergesort(L₂))
  Post-condition: a_{i₁} ≤ a_{i₂} ≤ ··· ≤ a_{iₙ}
```


**Divide and Conquer:**
1. **Divide** the list into two halves
2. **Conquer** each half recursively
3. **Combine** with Merge


<!--
**Parallel mergesort:** Mergesort is naturally parallelizable — the two recursive calls are independent and can run on separate processors. This made it one of the earliest algorithms studied in parallel computing. Cole (1988) showed that merge sort can be done in O(log n) time with n processors on a CREW PRAM.
-->

---

# Example Walkthrough

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Watch eight numbers split into singletons, then re-assemble themselves in sorted order.

</div>

Sort: $\{5, 3, 8, 1, 4, 2, 7, 6\}$


- **Split:** $\{5, 3, 8, 1\}$ and $\{4, 2, 7, 6\}$
- **Split again:** $\{5, 3\}$, $\{8, 1\}$, $\{4, 2\}$, $\{7, 6\}$
- **Split to singletons:** $\{5\}$, $\{3\}$, $\{8\}$, $\{1\}$, $\{4\}$, $\{2\}$, $\{7\}$, $\{6\}$
- **Merge pairs:** $\{3, 5\}$, $\{1, 8\}$, $\{2, 4\}$, $\{6, 7\}$
- **Merge again:** $\{1, 3, 5, 8\}$, $\{2, 4, 6, 7\}$
- **Final merge:** $\{1, 2, 3, 4, 5, 6, 7, 8\}$


---

# Complexity Analysis

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Solve $T(n) = 2T(n/2) + cn$ and you get $O(n \log n)$ — provably optimal for comparison sorts.

</div>

Let $T(n)$ be the running time on a list of length $n$.


**Recurrence:**

$$T(n) \leq T(\lceil n/2 \rceil) + T(\lfloor n/2 \rfloor) + cn$$


Ignoring floors and ceilings:

$$T(n) \leq 2T(n/2) + cn$$


**Solution:** $T(n) = O(n \log n)$

This is **optimal** for comparison-based sorting!


<!--
**Exact comparisons:** Knuth showed that mergesort using binary merge uses between n*ceil(lg n) - 2^ceil(lg n) + 1 and n*ceil(lg n) comparisons. For n = 1,000,000, that's roughly 20 million comparisons — sorting a million items in ~20 million steps.

**Information-theoretic lower bound:** There are n! possible permutations of n items. A comparison-based sort is essentially a binary decision tree, so it needs at least ceil(lg(n!)) comparisons in the worst case. By Stirling's approximation, lg(n!) ~ n lg n, which proves the Omega(n log n) lower bound. Mergesort (essentially) matches this, making it asymptotically optimal.
-->

---

# Next: Multiplying Numbers in Binary

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A teaser for Section 3.2: schoolbook multiplication is $O(n^2)$ — can we do better?

</div>

Can we multiply two $n$-bit numbers faster than $O(n^2)$?

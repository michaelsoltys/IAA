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

# Mergesort

Section 3.1 - Mergesort

---

# The Merging Problem

Suppose we have **two sorted lists**:

$$a_1 \leq a_2 \leq \cdots \leq a_n \quad \text{and} \quad b_1 \leq b_2 \leq \cdots \leq b_m$$

<v-click>

**Goal:** Combine them into one sorted list:

$$c_1 \leq c_2 \leq \cdots \leq c_{n+m}$$

</v-click>

---

# Merge Algorithm

```text
Merge Two Lists:
  Require: a₁ ≤ a₂ ≤ ··· ≤ aₙ and b₁ ≤ b₂ ≤ ··· ≤ bₘ
  p₁ ← 1; p₂ ← 1; i ← 1
  while i ≤ n + m:
    if a[p₁] ≤ b[p₂]:
      c[i] ← a[p₁]
      p₁ ← p₁ + 1
    else:
      c[i] ← b[p₂]
      p₂ ← p₂ + 1
    i ← i + 1
  Ensure: c₁ ≤ c₂ ≤ ··· ≤ c_{n+m}
```

<v-click>

**Complexity:** $O(n + m)$ — each element is compared at most once

</v-click>

---

# A Subtle Bug

The Merge algorithm as stated is **incorrect**!

<v-click>

**Problem:** If all elements of $a$ are smaller than $b_1$, then after $n$ iterations $p_1 = n + 1$, and checking $a_{p_1} \leq b_{p_2}$ causes an **out-of-bounds** error.

</v-click>

<v-click>

**Fix:** Change the while-loop condition to $p_1 \leq n \wedge p_2 \leq m$, then add a cleanup loop to copy remaining elements.

</v-click>

---

# The Mergesort Algorithm

```text
Mergesort:
  Require: A list of integers a₁, a₂, ..., aₙ
  L ← a₁, a₂, ..., aₙ
  if |L| ≤ 1:
    return L
  else:
    L₁ ← first ⌈n/2⌉ elements of L
    L₂ ← last  ⌊n/2⌋ elements of L
    return Merge(Mergesort(L₁), Mergesort(L₂))
  Ensure: a_{i₁} ≤ a_{i₂} ≤ ··· ≤ a_{iₙ}
```

<v-click>

**Divide and Conquer:**
1. **Divide** the list into two halves
2. **Conquer** each half recursively
3. **Combine** with Merge

</v-click>

---

# Example Walkthrough

Sort: $\{5, 3, 8, 1, 4, 2, 7, 6\}$

<v-clicks>

- **Split:** $\{5, 3, 8, 1\}$ and $\{4, 2, 7, 6\}$
- **Split again:** $\{5, 3\}$, $\{8, 1\}$, $\{4, 2\}$, $\{7, 6\}$
- **Split to singletons:** $\{5\}$, $\{3\}$, $\{8\}$, $\{1\}$, $\{4\}$, $\{2\}$, $\{7\}$, $\{6\}$
- **Merge pairs:** $\{3, 5\}$, $\{1, 8\}$, $\{2, 4\}$, $\{6, 7\}$
- **Merge again:** $\{1, 3, 5, 8\}$, $\{2, 4, 6, 7\}$
- **Final merge:** $\{1, 2, 3, 4, 5, 6, 7, 8\}$

</v-clicks>

---

# Complexity Analysis

Let $T(n)$ be the running time on a list of length $n$.

<v-click>

**Recurrence:**

$$T(n) \leq T(\lceil n/2 \rceil) + T(\lfloor n/2 \rfloor) + cn$$

</v-click>

<v-click>

Ignoring floors and ceilings:

$$T(n) \leq 2T(n/2) + cn$$

</v-click>

<v-click>

**Solution:** $T(n) = O(n \log n)$

This is **optimal** for comparison-based sorting!

</v-click>

---

# Key Questions

<v-clicks>

1. **Problem 3.1:** Fix the out-of-bounds bug in the Merge algorithm

2. **Problem 3.2:** Show that $L = L_1 \cup L_2$ (the split covers all elements)

3. **Problem 3.3:** Prove correctness of Mergesort using induction

4. **Problem 3.4:** Implement Mergesort for sorting words into lexicographic order

</v-clicks>

---

# Summary

<v-clicks>

- **Mergesort** is a classic divide and conquer sorting algorithm
- **Merge** combines two sorted lists in $O(n + m)$ time
- **Recurrence:** $T(n) \leq 2T(n/2) + cn$
- **Complexity:** $O(n \log n)$ — optimal for comparison-based sorting
- **Key insight:** Dividing the problem in half and combining linearly yields $O(n \log n)$

</v-clicks>

---

# Next: Multiplying Numbers in Binary

Can we multiply two $n$-bit numbers faster than $O(n^2)$?

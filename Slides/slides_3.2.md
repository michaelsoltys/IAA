---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 3.2: Multiplying Numbers in Binary
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Multiplying Numbers in Binary
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

# Multiplying Numbers in Binary

Section 3.2 - Multiplying Numbers in Binary

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# School Multiplication

Multiply $1110 \times 1101$ (i.e., $14 \times 13$):

|       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-------|---|---|---|---|---|---|---|---|
| $x$   |   |   |   |   | 1 | 1 | 1 | 0 |
| $y$   |   |   |   |   | 1 | 1 | 0 | 1 |
| $s_1$ |   |   |   |   | 1 | 1 | 1 | 0 |
| $s_2$ |   |   |   | 0 | 0 | 0 | 0 |   |
| $s_3$ |   |   | 1 | 1 | 1 | 0 |   |   |
| $s_4$ |   | 1 | 1 | 1 | 0 |   |   |   |
| $x \times y$ | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 |

<v-click>

**Complexity:** $O(n^2)$ for two $n$-bit integers

</v-click>

---

# Can We Do Better?

**Idea:** Break $n$-bit integers into $n/2$-bit halves

$$x = x_1 \cdot 2^{n/2} + x_0 \qquad y = y_1 \cdot 2^{n/2} + y_0$$

<v-click>

$x_1, y_1$ = high-order bits; $x_0, y_0$ = low-order bits

</v-click>

<v-click>

**Product expansion:**

$$xy = x_1 y_1 \cdot 2^n + (x_1 y_0 + x_0 y_1) \cdot 2^{n/2} + x_0 y_0$$

</v-click>

---

# First Attempt: 4 Recursive Multiplications

To compute $xy$ we need four products: $x_1 y_1$, $x_1 y_0$, $x_0 y_1$, $x_0 y_0$

<v-click>

**Recurrence:**

$$T(n) \leq 4T(n/2) + cn$$

</v-click>

<v-click>

**Solution:** $T(n) = O(n^{\log_2 4}) = O(n^2)$

No improvement over school multiplication!

</v-click>

---

# Karatsuba's Trick: 3 Multiplications Suffice

**Key observation:**

$$x_1 y_0 + x_0 y_1 = (x_1 + x_0)(y_1 + y_0) - (x_1 y_1 + x_0 y_0)$$

<v-click>

So we only need **three** multiplications:
1. $x_1 y_1$
2. $x_0 y_0$
3. $(x_1 + x_0)(y_1 + y_0)$

</v-click>

<v-click>

The cross term $x_1 y_0 + x_0 y_1$ is recovered by subtraction (cheap!)

</v-click>

---

# Cost Comparison

|                    | Multiplications | Additions | Shifts |
|--------------------|:-:|:-:|:-:|
| Method 1 (4 mults) | 4 | 3 | 2 |
| Method 2 (Karatsuba) | 3 | 4 | 2 |

<v-click>

Trading one multiplication for one addition is worth it — multiplications are **recursive** (expensive), while additions are $O(n)$ (cheap).

</v-click>

<v-click>

**New recurrence:**

$$T(n) \leq 3T(n/2) + dn$$

**Solution:** $T(n) = O(n^{\log_2 3}) \approx O(n^{1.59})$

</v-click>

---

# The Karatsuba Algorithm

<span style="font-size: 0.6em; color: navy;">Alg 18, Pg 66, alg:recmult</span>

```text
Karatsuba(x, y):
  Pre-condition: Two n-bit integers x and y
  if n = 1:
    if x = 1 ∧ y = 1: return 1
    else: return 0
  (x₁, x₀) ← (first ⌊n/2⌋ bits, last ⌈n/2⌉ bits) of x
  (y₁, y₀) ← (first ⌊n/2⌋ bits, last ⌈n/2⌉ bits) of y
  z₁ ← Karatsuba(x₁, y₁)
  z₂ ← Karatsuba(x₁ + x₀, y₁ + y₀)
  z₃ ← Karatsuba(x₀, y₀)
  return z₁ · 2^{2⌈n/2⌉} + (z₂ - z₁ - z₃) · 2^{⌈n/2⌉} + z₃
```

<v-click>

**Note:** Multiplying by $2^k$ is just a left-shift — $O(1)$ cost, ignored in analysis

</v-click>

---

# Why Does It Work?

Starting from $xy = x_1 y_1 \cdot 2^n + (x_1 y_0 + x_0 y_1) \cdot 2^{n/2} + x_0 y_0$:

<v-clicks>

- $z_1 = x_1 y_1$ — high-order product
- $z_3 = x_0 y_0$ — low-order product
- $z_2 = (x_1 + x_0)(y_1 + y_0) = x_1 y_1 + x_1 y_0 + x_0 y_1 + x_0 y_0$
- $z_2 - z_1 - z_3 = x_1 y_0 + x_0 y_1$ — the cross term!

</v-clicks>

---

# Key Questions

<v-clicks>

1. **Problem 3.5:** Prove the correctness of the Karatsuba algorithm <span style="font-size: 0.6em; color: navy;">Prb 3.5, Pg 65, exr:recmult-correctness</span>

2. **Problem 3.6:** Implement binary multiplication — input as two strings of 0s and 1s on the command line <span style="font-size: 0.6em; color: navy;">Prb 3.6, Pg 66, exr:recmult-program</span>

3. **Think about:** Can we do even better than $O(n^{1.59})$? (Yes — Toom-Cook, Schönhage-Strassen, and Harvey-van der Hoeven achieve near-linear time!)

</v-clicks>

---

# Summary

<v-clicks>

- **School multiplication** takes $O(n^2)$ for $n$-bit integers
- **Karatsuba's trick:** Reduce 4 recursive multiplications to 3
- **Key identity:** $(x_1 + x_0)(y_1 + y_0) - x_1 y_1 - x_0 y_0 = x_1 y_0 + x_0 y_1$
- **Recurrence:** $T(n) \leq 3T(n/2) + dn$
- **Complexity:** $O(n^{\log_2 3}) \approx O(n^{1.59})$
- **Lesson:** Reducing even one recursive call can dramatically improve asymptotics

</v-clicks>

---

# Next: Savitch's Algorithm

Divide and conquer applied to **space** optimization for graph reachability

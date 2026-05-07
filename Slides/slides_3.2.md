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

Section 3.2 — Karatsuba beats schoolbook $O(n^2)$ by trading one multiplication for some additions.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

<!--
The question "can we multiply faster than O(n^2)?" was open for centuries. Ancient methods — Egyptian multiplication (the Rhind Papyrus, c. 1650 BCE) and the doubling-and-halving method sometimes called "Russian peasant multiplication" — are all O(n^2). It wasn't until 1960 that Karatsuba, then a 23-year-old student, showed O(n^2) is not optimal — disproving a conjecture by Kolmogorov, his own advisor, who had claimed in a seminar that O(n^2) was a lower bound for multiplication.
-->

---

# School Multiplication

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The grade-school algorithm in binary — same shifts and adds, $O(n^2)$ work for $n$-bit numbers.

</div>

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


**Complexity:** $O(n^2)$ for two $n$-bit integers


---

# Can We Do Better?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Split each number into a high half and a low half — and the product expands into four pieces.

</div>

**Idea:** Break $n$-bit integers into $n/2$-bit halves

$$x = x_1 \cdot 2^{n/2} + x_0 \qquad y = y_1 \cdot 2^{n/2} + y_0$$


$x_1, y_1$ = high-order bits; $x_0, y_0$ = low-order bits


**Product expansion:**

$$xy = x_1 y_1 \cdot 2^n + (x_1 y_0 + x_0 y_1) \cdot 2^{n/2} + x_0 y_0$$


---

# First Attempt: 4 Recursive Multiplications

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Naive divide-and-conquer gives $T(n) = 4T(n/2) + cn$ — and that solves to the *same* $O(n^2)$.

</div>

To compute $xy$ we need four products: $x_1 y_1$, $x_1 y_0$, $x_0 y_1$, $x_0 y_0$


**Recurrence:**

$$T(n) \leq 4T(n/2) + cn$$


**Solution:** $T(n) = O(n^{\log_2 4}) = O(n^2)$

No improvement over school multiplication!


<!--
This is a recurring theme in algorithm design: the "obvious" divide-and-conquer doesn't always help. Splitting the problem in half but making 4 recursive calls gives $4 = 2^2$, so the exponent stays at 2. The magic happens only when you reduce the number of recursive calls below $2^2 = 4$. The same insight drives Strassen's matrix multiplication: 8 recursive multiplications give $O(n^3)$ (no gain), but Strassen's 7 give $O(n^{2.81})$.
-->

---

# Karatsuba's Trick: 3 Multiplications Suffice

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

One product computes the cross term *for free* — drop from 4 recursive calls to 3.

</div>

**Key observation:**

$$x_1 y_0 + x_0 y_1 = (x_1 + x_0)(y_1 + y_0) - (x_1 y_1 + x_0 y_0)$$


So we only need **three** multiplications:
1. $x_1 y_1$
2. $x_0 y_0$
3. $(x_1 + x_0)(y_1 + y_0)$


The cross term $x_1 y_0 + x_0 y_1$ is recovered by subtraction (cheap!)


<!--
Karatsuba discovered this trick in 1960 during a seminar by Kolmogorov at Moscow State University. Kolmogorov had conjectured that $\Omega(n^2)$ was a lower bound for multiplication. Within a week of the seminar, Karatsuba found his counterexample. Kolmogorov was so impressed that he wrote up and published the result himself in 1962, listing Karatsuba as co-author — reportedly without telling Karatsuba, who only learned of the publication later.
-->

---

# Cost Comparison

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Trading a recursive multiplication for a cheap addition is always a win — the recurrence becomes $3T(n/2)$.

</div>

|                    | Multiplications | Additions | Shifts |
|--------------------|:-:|:-:|:-:|
| Method 1 (4 mults) | 4 | 3 | 2 |
| Method 2 (Karatsuba) | 3 | 4 | 2 |


Trading one multiplication for one addition is worth it — multiplications are **recursive** (expensive), while additions are $O(n)$ (cheap).


**New recurrence:**

$$T(n) \leq 3T(n/2) + dn$$

**Solution:** $T(n) = O(n^{\log_2 3}) \approx O(n^{1.59})$


---

# The Karatsuba Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three recursive multiplications, a few shifts and adds — and you've beaten schoolbook for big enough $n$.

</div>

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


**Note:** Multiplying by $2^k$ is just a left-shift — $O(1)$ cost, ignored in analysis


<!--
In practice, Karatsuba's algorithm is faster than schoolbook multiplication for numbers longer than about 320–640 bits, depending on the platform. For smaller numbers, the overhead of recursion and extra additions makes it slower. Most big-integer libraries (GMP, Python's built-in integers, Java's BigInteger) switch from schoolbook to Karatsuba at a tuned threshold, then to Toom-Cook-3 for even larger numbers, and finally to FFT-based methods for the largest.
-->

---

# Why Does It Work?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Verify the algebra: $z_2 - z_1 - z_3$ recovers exactly the cross term we needed.

</div>

Starting from $xy = x_1 y_1 \cdot 2^n + (x_1 y_0 + x_0 y_1) \cdot 2^{n/2} + x_0 y_0$:


- $z_1 = x_1 y_1$ — high-order product
- $z_3 = x_0 y_0$ — low-order product
- $z_2 = (x_1 + x_0)(y_1 + y_0) = x_1 y_1 + x_1 y_0 + x_0 y_1 + x_0 y_0$
- $z_2 - z_1 - z_3 = x_1 y_0 + x_0 y_1$ — the cross term!


---

# The Same Trick for Matrices: Strassen's Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Block matrices, naive recursion gives $O(n^3)$ — exactly Karatsuba's "no improvement" trap.

</div>

Standard matrix multiplication of two $n \times n$ matrices: $O(n^3)$


**Block decomposition:** Split $A$ and $B$ into four $n/2 \times n/2$ submatrices:

$$A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix} \quad B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$$


**Naive block multiplication** needs **8** recursive multiplications:

$$C_{11} = A_{11}B_{11} + A_{12}B_{21}, \quad C_{12} = A_{11}B_{12} + A_{12}B_{22}, \quad \ldots$$

$$T(n) = 8T(n/2) + O(n^2) \implies O(n^{\log_2 8}) = O(n^3)$$

No improvement — same story as Karatsuba with 4 multiplications!


<!--
The parallel between Karatsuba and Strassen is exact: in both cases, the naive divide-and-conquer recovers the original complexity (n^2 for integers, n^3 for matrices). The breakthrough comes from reducing the number of recursive multiplications by one: 4→3 for Karatsuba, 8→7 for Strassen. The algebraic trick is different, but the structural insight is identical.
-->

---

# Strassen's 7 Multiplications

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Seven cleverly-chosen products in place of eight — exponent drops from $3$ to $\log_2 7 \approx 2.81$.

</div>

**Strassen (1969):** Compute 7 products instead of 8:

$$P_1 = A_{11} \cdot B_{11}, \quad P_2 = A_{12} \cdot B_{21}$$
$$P_3 = A_{21} \cdot B_{12}, \quad P_4 = A_{22} \cdot B_{22}$$
$$P_5 = (A_{11} + A_{22})(B_{11} + B_{22})$$
$$P_6 = (A_{21} + A_{22})(B_{21} - B_{22})$$
$$P_7 = (A_{11} - A_{21})(B_{11} + B_{12})$$


**Reconstruct $C$:**

$$C_{11} = P_5 + P_4 - P_2 + P_6, \quad C_{12} = P_1 + P_2$$
$$C_{21} = P_3 + P_4, \quad C_{22} = P_1 - P_3$$


$$T(n) = 7T(n/2) + O(n^2) \implies O(n^{\log_2 7}) \approx O(n^{2.81})$$


<!--
Volker Strassen published this in 1969. Like Karatsuba, it was a surprise — most people assumed O(n^3) was optimal for matrix multiplication. The result launched a decades-long search for faster algorithms. Unlike Karatsuba, Strassen's formulas are not unique — there are many ways to achieve 7 multiplications, and finding them is itself an active research area. In 2022, DeepMind's AlphaZero discovered novel matrix multiplication algorithms for specific small sizes by treating it as a tensor decomposition game, published in Nature.
-->

---

# Strassen vs Karatsuba: The Same Idea

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two famous algorithms, one structural insight — shave one recursive call, pay for it in additions.

</div>

| | Karatsuba (integers) | Strassen (matrices) |
|---|---|---|
| **Naive recursive calls** | 4 | 8 |
| **Optimized calls** | 3 | 7 |
| **Cheap operations** | $O(n)$ additions | $O(n^2)$ additions |
| **Naive complexity** | $O(n^2)$ | $O(n^3)$ |
| **Improved complexity** | $O(n^{1.59})$ | $O(n^{2.81})$ |
| **Practical crossover** | ~500 bits | ~64 rows |

**The pattern:** Trading one recursive multiplication for extra additions — because multiplications are recursive (expensive) but additions are only one level deep (cheap)

<!--
**Can we do better?** The current best for matrix multiplication is O(n^{2.371}) (Williams, Xu, Xu, Zhou, 2024). The exponent has been slowly chipped away: Strassen's 2.81 (1969), Pan's 2.796 (1978), Coppersmith-Winograd's 2.376 (1990), and most recently 2.371 (2024). Whether O(n^2) is achievable remains one of the biggest open problems in theoretical CS.

**Practical crossover:** Below the crossover (~500 bits for Karatsuba, ~64 rows for Strassen), the naive algorithm wins because the extra additions and recursion overhead dominate. Real libraries switch strategies at tuned thresholds:
- **GMP** (GNU Multiple Precision Arithmetic Library — the standard C library for big-integer arithmetic, used by Python, Mathematica, and Maple under the hood): chains schoolbook → Karatsuba → Toom-Cook → FFT as numbers get larger.
- **BLAS** (Basic Linear Algebra Subpackages — the standard interface for matrix operations, with implementations like OpenBLAS and Intel MKL): switches naive → Strassen, tuned per CPU. Most BLAS implementations don't use Strassen by default because it introduces numerical rounding errors that accumulate with recursion depth.
-->

---

# Next: Savitch's Algorithm

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Same paradigm, completely different goal — instead of saving time, we save *memory*.

</div>

Divide and conquer applied to **space** optimization for graph reachability

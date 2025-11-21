---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.5.5: Undecidability
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Undecidability
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

# Undecidability

Section 9.5.5 - Computational Foundations

---

# The Acceptance Problem

**The Language $A_{TM}$:**

$$A_{TM} = \{\langle M, w \rangle : \text{TM } M \text{ accepts } w\}$$

<v-click>

**The Question:** Is there a Turing Machine that can decide whether any arbitrary TM $M$ accepts a string $w$?

**The Answer:** No! This is **undecidable**.

</v-click>

---

# Theorem 9.6: $A_{TM}$ is Undecidable

**Theorem:** There is no Turing Machine that decides $A_{TM}$.

<v-click>

**Proof Idea:**
- Assume such a machine $H$ exists
- Construct a machine $D$ that contradicts itself
- Use diagonal argument (Cantor's technique)

</v-click>

---

# The Proof: Diagonal Argument

**Setup:** Suppose machine $H$ decides $A_{TM}$:
- Input: $\langle M, w \rangle$
- Output: **accept** if $M$ accepts $w$, **reject** if $M$ rejects or loops

<v-click>

**Define the "opposite" machine $D$:**

```text
D(⟨M⟩):
  if H(⟨M, ⟨M⟩⟩) = reject:
    return accept
  else:
    return reject
```

**Key Insight:** $D$ does the opposite of what $H$ says!

</v-click>

---

# The Contradiction

**What happens with $D(\langle D \rangle)$?**

<v-clicks>

1. We run $D$ on its own encoding $\langle D \rangle$
2. This calls $H(\langle D, \langle D \rangle \rangle)$
3. If $H$ says "reject": $D$ returns **accept**
4. If $H$ says "accept": $D$ returns **reject**

**Contradiction!** $D$ accepts iff $D$ rejects.

Since this is impossible, our assumption is wrong.
$H$ cannot exist!

</v-clicks>

---

# Practical Consequence: The Halting Problem

Imagine you're developing a debugger:

<v-clicks>

- You run a program on input $x$
- Nothing happens for a long time
- You press CTRL+C to stop it
- Question: Was I too hasty? Would it have finished given more time?

</v-clicks>

**Theorem 9.6 says:** This "halting feature" **cannot be implemented** for all programs!

<v-click>

We can build partial solutions that work on some inputs, but no algorithm works for every program and input.

</v-click>

---

# Understanding the Limitation

**Important Distinction:**

$A_{TM}$ is **undecidable** means:
- ❌ No TM halts with correct answer on ALL inputs

But:
- ✓ Some TM can halt correctly on SOME inputs
- ✓ We can build approximations (e.g., timeout after $n$ steps)
- ✓ We cannot verify correctness in general

---

# The Complement Problem

**Corollary:** $\overline{A_{TM}}$ is **not Recursively Enumerable (RE)**

<v-click>

**Proof sketch:**
- $A_{TM}$ is RE (the universal TM $U$ recognizes it)
- If both $A_{TM}$ and $\overline{A_{TM}}$ were RE, then $A_{TM}$ would be decidable
- But we know $A_{TM}$ is not decidable
- Therefore, $\overline{A_{TM}}$ is not RE

</v-click>

---

# The Busy Beaver Function

**Definition:** $\Sigma(n)$ = maximum number of 1's that a TM with $n$ states can write on a blank tape before halting.

Known values:
- $\Sigma(2) = 4$
- $\Sigma(3) = 6$
- $\Sigma(4) = 13$
- $\Sigma(5) \geq 4,098$
- $\Sigma(6) \geq 3.5 \times 10^{18267}$ ⚠️

**Key Result:** The Busy Beaver function is **undecidable**

---

# Busy Beaver Proof

**How does Busy Beaver relate to $A_{TM}$?**

If Busy Beaver were decidable, we could decide $A_{TM}$:

<v-clicks>

1. Given $\langle M, w \rangle$, construct $M'$ that:
   - Writes $w$ on empty tape
   - Simulates $M$ on $w$

2. Compute $\Sigma(|Q_{M'}|, |\Gamma_{M'}|)$ = max steps before halting

3. Simulate $M'$ for $\Sigma(|Q_{M'}|, |\Gamma_{M'}|)$ steps
   - If it halts: answer is definite ✓
   - If it doesn't: it never will ✓

This would decide $A_{TM}$ — contradiction!

</v-clicks>

---

# Reductions

**Key Technique:** Show undecidability by **reduction** from $A_{TM}$

**The Halting Problem:**
$$\text{HALT} = \{\langle M, w \rangle : M \text{ halts on } w\}$$

<v-click>

**Proof:** If $\text{HALT}$ were decidable with decider $H'$, we could decide $A_{TM}$:
- Run $H'$ on $\langle M, w \rangle$
- If $M$ halts: simulate $M$ on $w$ and answer accordingly
- Result: decider for $A_{TM}$ — contradiction!

</v-click>

---

# More Undecidable Problems

**$E_{TM}$ = "Does TM $M$ accept empty language?"**

$$E_{TM} = \{\langle M \rangle : L(M) = \emptyset\}$$

<v-click>

**$\text{REGULAR}_{TM}$ = "Is the language of TM $M$ regular?"**

$$\text{REGULAR}_{TM} = \{\langle M \rangle : L(M) \text{ is regular}\}$$

Both undecidable by reduction from $A_{TM}$!

</v-click>

---

# Rice's Theorem

**Theorem:** Every **nontrivial property** of Turing Machine languages is undecidable.

<v-clicks>

**What is a nontrivial property?**
- A property $\mathcal{P}$ is a set of TM descriptions
- Nontrivial: $\mathcal{P} \neq \emptyset$ and $\overline{\mathcal{P}} \neq \emptyset$
- Language-dependent: if $L(M_1) = L(M_2)$, then $M_1 \in \mathcal{P}$ iff $M_2 \in \mathcal{P}$

**Examples:**
- "Is $L$ non-empty?" → Undecidable
- "Does $L$ contain a specific string?" → Undecidable
- "Is $L$ infinite?" → Undecidable

</v-clicks>

---

# Enumerators and Recognizers

**Enumerator:** A TM with a write-only output tape that lists strings of a language

**Theorem:** A language is **recognizable** iff it is **enumerable**

<v-click>

**Proof sketch:**
- If $L$ is enumerable: simulate enumerator, accept when $w$ appears ✓
- If $L$ is recognizable: use "dovetailing" to enumerate:
  - Phase 1: Try string 1 for 1 step
  - Phase 2: Try strings 1-2 for 2 steps each
  - Phase 3: Try strings 1-3 for 3 steps each
  - Output strings that are accepted

This interleaving ensures no string is missed!

</v-click>

---

# Post's Correspondence Problem (PCP)

**Definition:** Given two lists of strings over alphabet $\Sigma$:
- List $A = w_1, w_2, \ldots, w_k$
- List $B = x_1, x_2, \ldots, x_k$

**Does a solution exist?** Sequence of indices $i_1, i_2, \ldots, i_m$ such that:
$$w_{i_1}w_{i_2}\cdots w_{i_m} = x_{i_1}x_{i_2}\cdots x_{i_m}$$

---

# PCP Example

**Lists:**
- $A = \{1, 10111, 10\}$
- $B = \{111, 10, 0\}$

**Solution:** Indices $2, 1, 1, 3$

$$\underbrace{10111}_{w_2}\underbrace{1}_{w_1}\underbrace{1}_{w_1}\underbrace{10}_{w_3} = \underbrace{10}_{x_2}\underbrace{111}_{x_1}\underbrace{111}_{x_1}\underbrace{0}_{x_3}$$

Both sides: $10111110$ ✓

---

# PCP is Undecidable

**Theorem:** The Post's Correspondence Problem is undecidable.

**Proof Strategy (3 steps):**

<v-clicks>

1. PCP ≥ Modified PCP (MPCP) in difficulty
2. MPCP ≥ $A_{TM}$ in difficulty
3. Since $A_{TM}$ undecidable, so is PCP

**Key Construction:** Encode TM computation as MPCP instance
- Partial solutions represent TM configurations
- Solution exists iff $M$ accepts $w$

</v-clicks>

---

# Key Takeaways

<v-clicks>

- **$A_{TM}$ is undecidable** - no algorithm can decide if any TM accepts input
- **Proof uses diagonalization** - contradiction argument (Cantor's technique)
- **Natural problems are undecidable** - halting, empty language, regularity, etc.
- **Rice's Theorem** - all nontrivial language properties undecidable
- **Reductions** - show undecidability of new problems via $A_{TM}$
- **Post's Problem** - undecidable even without explicit model of computation

</v-clicks>

---

# Implications for Computer Science

<v-clicks>

1. **Program Verification:** Cannot verify all program properties
2. **Debugging:** Cannot build universal halting detector
3. **Compiler Design:** Cannot optimize away all infinite loops
4. **Type Systems:** Cannot infer all type relationships
5. **Security:** Some security properties are undecidable

**Lesson:** Undecidability is a fundamental limit of computation, not a limitation of current technology!

</v-clicks>

---

# Summary

| Concept | Status |
|---------|--------|
| $A_{TM}$ | Undecidable |
| HALT | Undecidable (by reduction) |
| $E_{TM}$ | Undecidable (by reduction) |
| REGULAR$_{TM}$ | Undecidable (by Rice's Theorem) |
| PCP | Undecidable (by reduction from $A_{TM}$) |
| Busy Beaver | Undecidable |

---

# Key Questions and Exercises

<v-clicks>

1. **Diagonalization:** Why is the diagonal argument valid?
2. **Reductions:** Can you show HALT is undecidable?
3. **Enumerators:** Prove recognizable ⟺ enumerable
4. **PCP:** Construct an instance with no solution
5. **Rice's Theorem:** What makes a property nontrivial?

</v-clicks>

---

# Next Steps

- Study reductions in detail
- Work through PCP encoding of Turing Machines
- Prove Rice's Theorem
- Explore the Arithmetic Hierarchy
- Learn about semi-decidable problems

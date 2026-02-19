---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.3.4: Algebraic Laws for Regular Expressions
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Algebraic Laws for Regular Expressions
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

# Algebraic Laws for Regular Expressions

Section 9.3.4 - Regular Languages

---

# Overview

**Algebraic Laws** can be used to simplify REs, or to restate them in a different way

<v-clicks>

**Key concepts:**
1. **Nine fundamental laws** — commutativity, associativity, distributivity, identity, annihilator, idempotence
2. **Six Kleene star laws** — properties of $*$ and $+$
3. **Testing algebraic laws** — a surprising method using a single instance

</v-clicks>

<v-click>

Note: Unlike most of mathematics, we can verify a **universal** statement about REs with a **single** test case!

</v-click>

---
layout: section
---

# The Nine Fundamental Laws

Algebraic properties of union and concatenation

---

# Laws: Commutativity, Associativity, Identity

| Law | Description |
|-----|-------------|
| $R + P = P + R$ | commutativity of $+$ |
| $(R + P) + Q = R + (P + Q)$ | associativity of $+$ |
| $(RP)Q = R(PQ)$ | associativity of concatenation |

<v-click>

| Law | Description |
|-----|-------------|
| $\emptyset + R = R + \emptyset = R$ | $\emptyset$ identity for $+$ |
| $\varepsilon R = R\varepsilon = R$ | $\varepsilon$ identity for concatenation |
| $\emptyset R = R\emptyset = \emptyset$ | $\emptyset$ annihilator for concatenation |

</v-click>

---

# Laws: Distributivity and Idempotence

| Law | Description |
|-----|-------------|
| $R(P + Q) = RP + RQ$ | left-distributivity |
| $(P + Q)R = PR + QR$ | right-distributivity |
| $R + R = R$ | idempotent law for union |

---

# Missing Law: Commutativity of Concatenation

**Question:** Is $RP = PR$ a valid law?

<v-click>

**No!** Commutativity of concatenation is **conspicuously missing**

</v-click>

<v-click>

**Why?** Concatenation is not commutative: $ab \neq ba$ as strings

- $L(\{a\}\{b\}) = \{ab\}$
- $L(\{b\}\{a\}) = \{ba\}$

These are different languages!

</v-click>

<v-click>

**Analogy:** Matrix multiplication is also not commutative — order matters when combining structured objects

</v-click>

---
layout: section
---

# Kleene Star Laws

Properties of $*$ and $+$

---

# Six Laws of Kleene Star

<v-clicks>

| Law | Explanation |
|-----|-------------|
| $(R^*)^* = R^*$ | starring an already-starred RE changes nothing |
| $\emptyset^* = \varepsilon$ | zero or more copies of nothing is the empty string |
| $\varepsilon^* = \varepsilon$ | zero or more copies of $\varepsilon$ is $\varepsilon$ |

| Law | Explanation |
|-----|-------------|
| $R^+ = RR^* = R^*R$ | one or more copies = one copy then zero or more |
| $R^* = R^+ + \varepsilon$ | zero or more = one or more, or the empty string |
| $(R + P)^* = (R^*P^*)^*$ | interleaving lemma |

</v-clicks>

---

# A Subtle Point About $R^+$

From $R^* = R^+ + \varepsilon$ one might be tempted to conclude:

$$L(R^+) = L(R^*) - \{\varepsilon\}$$

<v-click>

**This is NOT necessarily true!**

</v-click>

<v-click>

**Counterexample:** Let $R = \varepsilon + a$

- $L(R) = \{\varepsilon, a\}$
- $L(R^+) = \{\varepsilon, a, aa, aaa, \ldots\}$ — note that $\varepsilon \in L(R^+)$ since $\varepsilon \in L(R)$
- $L(R^*) = \{\varepsilon, a, aa, aaa, \ldots\}$

So $L(R^+) = L(R^*)$ in this case — removing $\varepsilon$ would be wrong!

</v-click>

<v-click>

**The issue:** $R^+ = RR^*$, and if $\varepsilon \in L(R)$, then $\varepsilon \in L(R^+)$

</v-click>

---
layout: section
---

# Testing Algebraic Laws

A surprising verification method

---

# The Test for RE Algebraic Laws

**Problem:** How do we check if an alleged algebraic law $E = F$ is valid?

<v-click>

**Method:** Replace all variables ($R, P, Q, \ldots$) by **distinct symbols** ($a, b, c, \ldots$) to get concrete REs $C, D$. Then check if $L(C) = L(D)$.

</v-click>

<v-click>

**If $L(C) = L(D)$, then the law $E = F$ is valid!**

</v-click>

<v-click>

This is remarkable: we verify a **universal** statement (for all languages $R, P, Q, \ldots$) by testing a **single particular instance**

</v-click>

<v-click>

This contradicts typical mathematical reasoning — usually one example proves nothing about a universal claim

</v-click>

---

# Testing Example

**Claim:** $(R + P)^* = (R^*P^*)^*$

<v-clicks>

**Step 1:** Replace $R$ by $a$ and $P$ by $b$

**Step 2:** Check whether $(a + b)^* = (a^*b^*)^*$

**Step 3:** Verify:
- $L((a+b)^*) = \Sigma^*$, i.e., all strings over $\{a, b\}$
- $L((a^*b^*)^*) = \Sigma^*$, since any string is a concatenation of blocks of $a$s and $b$s

**Conclusion:** The two languages are equal, so the law holds!

</v-clicks>

---

# Why Does the Test Work?

<v-clicks>

**Intuition:** Replacing variables by distinct symbols preserves the **structural relationships** between the RE operations

If two REs produce the same language even when their components are maximally distinct (different symbols), then the equivalence depends only on the **algebraic structure**, not on the specific languages

**Formal justification:** If $L(C) \neq L(D)$ for the concrete instance, then we have a **counterexample** — the particular languages show the law fails. If $L(C) = L(D)$, then the structural equivalence guarantees $L(E) = L(F)$ for all substitutions

</v-clicks>

---

# Summary

<v-clicks>

- **Nine fundamental laws** govern union and concatenation: commutativity and associativity of $+$, associativity of concatenation, identity elements, annihilator, distributivity, idempotence

- **Commutativity of concatenation is NOT valid** — $RP \neq PR$ in general

- **Six Kleene star laws** include $(R^*)^* = R^*$, $\emptyset^* = \varepsilon$, and the interleaving law $(R+P)^* = (R^*P^*)^*$

- **Subtlety:** $L(R^+) \neq L(R^*) - \{\varepsilon\}$ in general (when $\varepsilon \in L(R)$)

- **Testing algebraic laws:** Replace variables by distinct symbols and check one instance — if it works, the law is universally valid

</v-clicks>

---

# Exercises

1. Verify each of the nine fundamental laws by converting both sides to $\varepsilon$-NFAs and checking language equality

2. Find two REs $R, P$ where $RP = PR$ happens to hold (even though it is not a general law)

3. Give an example where $L(R^+) = L(R^*) - \{\varepsilon\}$ (i.e., where the subtlety does not arise)

4. Use the test for algebraic laws to verify: $R^* = R^+ + \varepsilon$

5. Use the test to show that $R + PR^* \neq (P + R)^*$ (i.e., it is NOT a valid law)

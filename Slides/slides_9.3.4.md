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

# Algebraic Laws for Regular Expressions

Section 9.3.4 — Identities for simplifying REs, and the surprising single-test method that verifies them.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Nine fundamental laws, six star laws, and a remarkable test for verifying them with one example.

</div>

**Algebraic Laws** can be used to simplify REs, or to restate them in a different way


**Key concepts:**
1. **Nine fundamental laws** — commutativity, associativity, distributivity, identity, annihilator, idempotence
2. **Six Kleene star laws** — properties of $*$ and $+$
3. **Testing algebraic laws** — a surprising method using a single instance


Note: Unlike most of mathematics, we can verify a **universal** statement about REs with a **single** test case!


---
layout: section
---

# The Nine Fundamental Laws

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

How $+$ and concatenation behave — almost like a ring, but with one famously missing law.

</div>

Algebraic properties of union and concatenation

---

# Laws: Commutativity, Associativity, Identity

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The familiar arithmetic rules carry over — except for one important exception coming up.

</div>

| Law | Description |
|-----|-------------|
| $R + P = P + R$ | commutativity of $+$ |
| $(R + P) + Q = R + (P + Q)$ | associativity of $+$ |
| $(RP)Q = R(PQ)$ | associativity of concatenation |


| Law | Description |
|-----|-------------|
| $\emptyset + R = R + \emptyset = R$ | $\emptyset$ identity for $+$ |
| $\varepsilon R = R\varepsilon = R$ | $\varepsilon$ identity for concatenation |
| $\emptyset R = R\emptyset = \emptyset$ | $\emptyset$ annihilator for concatenation |


---

# Laws: Distributivity and Idempotence

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Concatenation distributes over $+$ on both sides — and union swallows duplicates.

</div>

| Law | Description |
|-----|-------------|
| $R(P + Q) = RP + RQ$ | left-distributivity |
| $(P + Q)R = PR + QR$ | right-distributivity |
| $R + R = R$ | idempotent law for union |

---

# Missing Law: Commutativity of Concatenation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Strings are ordered, so $ab \neq ba$ — concatenation is *not* commutative, just like matrix multiplication.

</div>

**Question:** Is $RP = PR$ a valid law?


**No!** Commutativity of concatenation is **conspicuously missing**


**Why?** Concatenation is not commutative: $ab \neq ba$ as strings

- $L(\{a\}\{b\}) = \{ab\}$
- $L(\{b\}\{a\}) = \{ba\}$

These are different languages!


**Analogy:** Matrix multiplication is also not commutative — order matters when combining structured objects


---
layout: section
---

# Kleene Star Laws

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Useful identities for $R^*$ and $R^+$ — plus a subtle gotcha when $\varepsilon \in L(R)$.

</div>

Properties of $*$ and $+$

---

# Six Laws of Kleene Star

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Including the *interleaving lemma* $(R + P)^* = (R^*P^*)^*$ — both produce all strings over the alphabet.

</div>

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


---

# A Subtle Point About $R^+$

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If $\varepsilon \in L(R)$, then $\varepsilon \in L(R^+)$ too — so $R^+$ is *not* always $R^*$ minus $\varepsilon$.

</div>

From $R^* = R^+ + \varepsilon$ one might be tempted to conclude:

$$L(R^+) = L(R^*) - \{\varepsilon\}$$


**This is NOT necessarily true!**


**Counterexample:** Let $R = \varepsilon + a$

- $L(R) = \{\varepsilon, a\}$
- $L(R^+) = \{\varepsilon, a, aa, aaa, \ldots\}$ — note that $\varepsilon \in L(R^+)$ since $\varepsilon \in L(R)$
- $L(R^*) = \{\varepsilon, a, aa, aaa, \ldots\}$

So $L(R^+) = L(R^*)$ in this case — removing $\varepsilon$ would be wrong!


**The issue:** $R^+ = RR^*$, and if $\varepsilon \in L(R)$, then $\varepsilon \in L(R^+)$


---
layout: section
---

# Testing Algebraic Laws

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A single concrete instance can verify a *universal* RE identity — and we'll see why.

</div>

A surprising verification method

---

# The Test for RE Algebraic Laws

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Substitute distinct symbols for the variables, compare the resulting languages — that's all you need.

</div>

**Problem:** How do we check if an alleged algebraic law $E = F$ is valid?


**Method:** Replace all variables ($R, P, Q, \ldots$) by **distinct symbols** ($a, b, c, \ldots$) to get concrete REs $C, D$. Then check if $L(C) = L(D)$.


**If $L(C) = L(D)$, then the law $E = F$ is valid!**


This is remarkable: we verify a **universal** statement (for all languages $R, P, Q, \ldots$) by testing a **single particular instance**


This contradicts typical mathematical reasoning — usually one example proves nothing about a universal claim


---

# Testing Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Replace $R \mapsto a$, $P \mapsto b$ — both sides describe $\{a,b\}^*$, so the law holds.

</div>

**Claim:** $(R + P)^* = (R^*P^*)^*$


**Step 1:** Replace $R$ by $a$ and $P$ by $b$

**Step 2:** Check whether $(a + b)^* = (a^*b^*)^*$

**Step 3:** Verify:
- $L((a+b)^*) = \Sigma^*$, i.e., all strings over $\{a, b\}$
- $L((a^*b^*)^*) = \Sigma^*$, since any string is a concatenation of blocks of $a$s and $b$s

**Conclusion:** The two languages are equal, so the law holds!


---

# Why Does the Test Work?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Distinct symbols expose the *structural* equivalence — no accidental coincidence between the languages.

</div>

**Intuition:** Replacing variables by distinct symbols preserves the **structural relationships** between the RE operations

If two REs produce the same language even when their components are maximally distinct (different symbols), then the equivalence depends only on the **algebraic structure**, not on the specific languages

**Formal justification:** If $L(C) \neq L(D)$ for the concrete instance, then we have a **counterexample** — the particular languages show the law fails. If $L(C) = L(D)$, then the structural equivalence guarantees $L(E) = L(F)$ for all substitutions


---

# Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Five problems on verifying laws, finding edge cases, and disproving a tempting fake-law.

</div>

1. Verify each of the nine fundamental laws by converting both sides to $\varepsilon$-NFAs and checking language equality

2. Find two REs $R, P$ where $RP = PR$ happens to hold (even though it is not a general law)

3. Give an example where $L(R^+) = L(R^*) - \{\varepsilon\}$ (i.e., where the subtlety does not arise)

4. Use the test for algebraic laws to verify: $R^* = R^+ + \varepsilon$

5. Use the test to show that $R + PR^* \neq (P + R)^*$ (i.e., it is NOT a valid law)

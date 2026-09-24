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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

$RP = PR$ is the law that is not there. Strings are ordered, so $ab \neq ba$.

</div>

<img src="./Figures/re-laws-concat.drawio.svg" class="mx-auto block" style="width: 100%; max-height: 360px;" alt="Two cards: language of a then b is {ab}, language of b then a is {ba}, not equal" />

<!--
The same reason matrix multiplication fails to commute: the objects have an order, and swapping the factors is a different object. Two-letter words are the smallest witness. RP = PR can hold for particular R and P (take R = P, or R = a* and P = a), but it is not an identity.
-->


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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

$R^* = R^+ + \varepsilon$ does not mean $L(R^+) = L(R^*) - \{\varepsilon\}$. It depends on whether $\varepsilon$ is already in $R$.

</div>

<img src="./Figures/re-laws-starplus.drawio.svg" class="mx-auto block" style="width: 100%; max-height: 400px;" alt="Left: R = a, epsilon dropped from R+. Right: R = epsilon + a, epsilon stays in R+" />

<!--
R+ is defined as RR*, one copy of R followed by a star. If that one copy can be ε, the star is free to contribute ε as well, and ε survives. The identity R* = R+ + ε is still true; union with {ε} does not force ε out of the other summand.
-->


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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

To test $E = F$, replace the variables by distinct letters and compare the two concrete languages. One free instance decides the identity.

</div>

<img src="./Figures/re-laws-test.drawio.svg" class="mx-auto block" style="width: 100%; max-height: 380px;" alt="Substitution R to a and P to b turns (R+P)* = (R*P*)* into (a+b)* = (a*b*)*, both equal to {a,b}*" />

<!--
Language operations are homomorphisms: substituting languages for letters preserves equality. Distinct letters are the free case, so equality there lifts to every substitution. A mismatch on those letters is an ordinary counterexample. Salomaa axiomatized the algebra of regular events in 1966; the classroom test is the free-case specialization of that completeness.
-->


---

# Testing Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

$(R + P)^* = (R^*P^*)^*$ becomes $(a + b)^* = (a^*b^*)^*$. Both are $\{a,b\}^*$, read two ways.

</div>

<img src="./Figures/re-laws-interleave.drawio.svg" class="mx-auto block" style="width: 100%; max-height: 380px;" alt="The string abba read letter by letter as (a+b)* and as two a*b* blocks" />

<!--
Any string over {a,b} splits uniquely into maximal runs of a's and b's. Grouping those runs as (a* b*) pairs, with a trailing empty b* if the string ends in a, shows it is in (a* b*)*. The other direction is immediate: a* b* only uses a and b. That is the interleaving lemma as a picture.
-->


---

# When the Test Fails

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

The same substitution kills a fake law. $R + PR^* \neq (P + R)^*$, because $ab$ is on one side only.

</div>

<img src="./Figures/re-laws-fake.drawio.svg" class="mx-auto block" style="width: 100%; max-height: 390px;" alt="After substituting a and b, ab is missing from a + ba* and present in (a+b)*" />

<!--
One mismatched string is enough. Distinct letters keep the two sides from accidentally agreeing: if the identity were true for all languages, it would be true of {a} and {b}. The witness ab is the shortest string that uses both letters in the order the left-hand side forbids.
-->


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

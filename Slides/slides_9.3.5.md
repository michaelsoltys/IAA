---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.3.5: Closure Properties of Regular Languages
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Closure Properties of Regular Languages
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

# Closure Properties of Regular Languages

Section 9.3.5 - Regular Languages

---

# Overview

A class of languages is **closed** under an operation if applying that operation to languages in the class always yields a language still in the class

<v-clicks>

**Regular languages are closed under:**
1. Union, Concatenation, Kleene Star
2. Complementation
3. Intersection
4. Reversal
5. Homomorphism and Inverse Homomorphism
6. NOPREFIX and NOEXTEND

</v-clicks>

<v-click>

Each closure proof uses a different technique — RE constructions, DFA modifications, or DeMorgan's law

</v-click>

---
layout: section
---

# Basic Closures

Union, Concatenation, and Kleene Star

---

# Union, Concatenation, Star

These follow directly from the equivalence of REs and FAs (Section 9.3.3):

<v-clicks>

**Union:** If $L, M$ are regular, so is $L \cup M$

*Proof:* $L = L(R)$ and $M = L(S)$, so $L \cup M = L(R + S)$

**Concatenation:** If $L, M$ are regular, so is $L \cdot M$

*Proof:* $L = L(R)$ and $M = L(S)$, so $L \cdot M = L(RS)$

**Kleene Star:** If $L$ is regular, so is $L^*$

*Proof:* $L = L(R)$, so $L^* = L(R^*)$

</v-clicks>

<v-click>

Since RE $\Leftrightarrow$ FA, and RE is closed under $+$, concatenation, and $*$ by definition, these closures are immediate

</v-click>

---
layout: section
---

# Boolean Closures

Complementation and Intersection

---

# Complementation

**Theorem:** If $L$ is regular, so is $L^c = \Sigma^* - L$

<v-clicks>

**Proof:** Let $L = L(A)$ for some DFA $A = (Q, \Sigma, \delta, q_0, F)$

Construct DFA $A'$ by swapping accepting and non-accepting states:

$$F_{A'} = Q - F_A$$

Everything else stays the same: $Q, \Sigma, \delta, q_0$

**Why it works:** A string $w$ is accepted by $A$ iff it is rejected by $A'$, and vice versa

</v-clicks>

<v-click>

**Important:** This only works for **DFAs**, not NFAs! (Why?)

</v-click>

---

# Why Not NFAs?

Swapping accept/non-accept states does **not** complement an NFA

<v-click>

**Example:** Consider an NFA that accepts $\{a, b\}^*$

If we swap states, the NFA might still accept some strings via alternative computation paths

</v-click>

<v-click>

**The issue:** An NFA accepts if **any** path leads to acceptance. Swapping states means it rejects only if **all** paths led to acceptance before — which is a different condition

</v-click>

<v-click>

**Solution:** First convert NFA to DFA (subset construction), then complement

</v-click>

---

# Intersection

**Theorem:** If $L, M$ are regular, so is $L \cap M$

<v-clicks>

**Proof:** By DeMorgan's Law:

$$L \cap M = \overline{\overline{L} \cup \overline{M}}$$

Since regular languages are closed under:
- Complementation ($\overline{L}$ and $\overline{M}$ are regular)
- Union ($\overline{L} \cup \overline{M}$ is regular)
- Complementation again ($\overline{\overline{L} \cup \overline{M}}$ is regular)

We conclude $L \cap M$ is regular

</v-clicks>

<v-click>

**Alternative:** Direct construction using the **product automaton** — run both DFAs simultaneously, accept iff both accept

</v-click>

---
layout: section
---

# Structural Closures

Reversal, Homomorphism, and Inverse Homomorphism

---

# Reversal

**Theorem:** If $L$ is regular, so is $L^R = \{w^R \mid w \in L\}$

where $(w_1 w_2 \ldots w_n)^R = w_n w_{n-1} \ldots w_1$

<v-clicks>

**Proof:** Given a RE $E$ for $L$, define $E^R$ by **structural induction**:

**Basis:**
- $a^R = a$ for $a \in \Sigma$
- $\varepsilon^R = \varepsilon$
- $\emptyset^R = \emptyset$

**Induction:**
- $(E + F)^R = E^R + F^R$
- $(EF)^R = F^R E^R$ (order reverses!)
- $(E^*)^R = (E^R)^*$

</v-clicks>

<v-click>

The key trick: $(EF)^R = F^R E^R$ — just like matrix transpose: $(AB)^T = B^T A^T$

</v-click>

---

# Homomorphism

A **homomorphism** is a function $h: \Sigma^* \to \Sigma^*$ defined symbol by symbol:

$$h(w) = h(w_1 w_2 \ldots w_n) = h(w_1) h(w_2) \ldots h(w_n)$$

<v-click>

**Example:** $h(0) = ab$, $h(1) = \varepsilon$

Then $h(0011) = ab \cdot ab \cdot \varepsilon \cdot \varepsilon = abab$

</v-click>

<v-click>

**Theorem:** If $L$ is regular, then so is $h(L) = \{h(w) \mid w \in L\}$

**Proof:** Given a RE $E$ for $L$, define $h(E)$ by replacing each symbol $a$ with $h(a)$ in the RE. The result is a valid RE for $h(L)$

</v-click>

---

# Inverse Homomorphism

**Theorem:** If $L$ is regular, then so is $h^{-1}(L) = \{w \mid h(w) \in L\}$

<v-clicks>

**Proof:** Let $A$ be the DFA for $L$. Construct a DFA for $h^{-1}(L)$:

$$\delta'(q, a) = \hat{\delta}_A(q, h(a))$$

**Idea:** On input symbol $a$, compute $h(a)$ (a string), then simulate $A$ on the entire string $h(a)$

**Example:** If $h(a) = 01$ and $A$ is in state $q$:
- Compute $\delta_A(q, 0) = p$
- Compute $\delta_A(p, 1) = r$
- So $\delta'(q, a) = r$

</v-clicks>

<v-click>

The new DFA has the **same states** as $A$ — only the transition function changes

</v-click>

---
layout: section
---

# Prefix Closures

NOPREFIX and NOEXTEND

---

# NOPREFIX and NOEXTEND

Two additional closure properties involving prefixes:

<v-clicks>

**NOPREFIX:** If $A$ is regular, so is:

$$\text{NOPREFIX}(A) = \{w \in A : \text{no proper prefix of } w \text{ is in } A\}$$

(Keep only the strings from $A$ that are "first hits" — no shorter prefix is already in $A$)

**NOEXTEND:** If $A$ is regular, so is:

$$\text{NOEXTEND}(A) = \{w \in A : w \text{ is not a proper prefix of any string in } A\}$$

(Keep only the strings from $A$ that are "dead ends" — no longer string in $A$ starts with $w$)

</v-clicks>

<v-click>

**Exercise:** Prove that both NOPREFIX and NOEXTEND preserve regularity by constructing appropriate automata

</v-click>

---

# Summary

<v-clicks>

- **Union, Concatenation, Star** — immediate from RE closure (by definition of RE)

- **Complementation** — swap accepting and non-accepting states in a **DFA** (not NFA!)

- **Intersection** — via DeMorgan: $L \cap M = \overline{\overline{L} \cup \overline{M}}$, or via product automaton

- **Reversal** — structural induction on RE, with $(EF)^R = F^R E^R$

- **Homomorphism** — apply $h$ to the RE directly

- **Inverse Homomorphism** — modify DFA transitions: $\delta'(q,a) = \hat{\delta}_A(q, h(a))$

- **NOPREFIX, NOEXTEND** — construct automata that filter by prefix conditions

</v-clicks>

---

# Exercises

1. Prove closure under complementation: given a DFA $A$ for $L$, construct $A'$ for $\overline{L}$, and prove $L(A') = \overline{L(A)}$

2. Why does complementation fail if we swap accept/reject states on an NFA? Give a concrete counterexample

3. Construct the product automaton for $L \cap M$ directly (without using DeMorgan's law)

4. Let $h(a) = 01$, $h(b) = 1$, and $L = \{w \in \{0,1\}^* \mid w \text{ ends in } 01\}$. What is $h^{-1}(L)$?

5. Give a regular language $A$ and compute $\text{NOPREFIX}(A)$ and $\text{NOEXTEND}(A)$

6. Prove that NOPREFIX preserves regularity by constructing a DFA

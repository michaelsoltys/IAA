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

# Closure Properties of Regular Languages

Section 9.3.5 — All the operations you can apply to regular languages and stay regular — with the proofs that show why.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A tour of operations that preserve regularity — each proof picks the formalism that makes it cleanest.

</div>

A class of languages is **closed** under an operation if applying that operation to languages in the class always yields a language still in the class


**Regular languages are closed under:**
1. Union, Concatenation, Kleene Star
2. Complementation
3. Intersection
4. Reversal
5. Homomorphism and Inverse Homomorphism
6. NOPREFIX and NOEXTEND


Each closure proof uses a different technique — RE constructions, DFA modifications, or DeMorgan's law


---
layout: section
---

# Basic Closures

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The three RE operations are essentially closure properties by definition — easy wins.

</div>

Union, Concatenation, and Kleene Star

---

# Union, Concatenation, Star

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If $L = L(R)$ and $M = L(S)$, then $L \cup M = L(R + S)$ — the proof writes itself.

</div>

These follow directly from the equivalence of REs and FAs (Section 9.3.3):


**Union:** If $L, M$ are regular, so is $L \cup M$

*Proof:* $L = L(R)$ and $M = L(S)$, so $L \cup M = L(R + S)$

**Concatenation:** If $L, M$ are regular, so is $L \cdot M$

*Proof:* $L = L(R)$ and $M = L(S)$, so $L \cdot M = L(RS)$

**Kleene Star:** If $L$ is regular, so is $L^*$

*Proof:* $L = L(R)$, so $L^* = L(R^*)$


Since RE $\Leftrightarrow$ FA, and RE is closed under $+$, concatenation, and $*$ by definition, these closures are immediate


---
layout: section
---

# Boolean Closures

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Flip accept states for complement, then use DeMorgan to get intersection for free.

</div>

Complementation and Intersection

---

# Complementation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Swap accepting and non-accepting states in the DFA — that's the entire construction.

</div>

**Theorem:** If $L$ is regular, so is $L^c = \Sigma^* - L$


**Proof:** Let $L = L(A)$ for some DFA $A = (Q, \Sigma, \delta, q_0, F)$

Construct DFA $A'$ by swapping accepting and non-accepting states:

$$F_{A'} = Q - F_A$$

Everything else stays the same: $Q, \Sigma, \delta, q_0$

**Why it works:** A string $w$ is accepted by $A$ iff it is rejected by $A'$, and vice versa


**Important:** This only works for **DFAs**, not NFAs! (Why?)


---

# Why Not NFAs?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

NFA acceptance is *existential* — flipping the labels asks the wrong question entirely.

</div>

Swapping accept/non-accept states does **not** complement an NFA


**Example:** Consider an NFA that accepts $\{a, b\}^*$

If we swap states, the NFA might still accept some strings via alternative computation paths


**The issue:** An NFA accepts if **any** path leads to acceptance. Swapping states means it rejects only if **all** paths led to acceptance before — which is a different condition


**Solution:** First convert NFA to DFA (subset construction), then complement


---

# Intersection

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

DeMorgan it — or build the product DFA directly. Either way, intersection stays inside the class.

</div>

**Theorem:** If $L, M$ are regular, so is $L \cap M$


**Proof:** By DeMorgan's Law:

$$L \cap M = \overline{\overline{L} \cup \overline{M}}$$

Since regular languages are closed under:
- Complementation ($\overline{L}$ and $\overline{M}$ are regular)
- Union ($\overline{L} \cup \overline{M}$ is regular)
- Complementation again ($\overline{\overline{L} \cup \overline{M}}$ is regular)

We conclude $L \cap M$ is regular


**Alternative:** Direct construction using the **product automaton** — run both DFAs simultaneously, accept iff both accept


---
layout: section
---

# Structural Closures

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Reverse strings, rename symbols, or pull strings back through a renaming — all preserve regularity.

</div>

Reversal, Homomorphism, and Inverse Homomorphism

---

# Reversal

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Reverse the RE by structural induction — concatenation flips order, just like matrix transpose.

</div>

**Theorem:** If $L$ is regular, so is $L^R = \{w^R \mid w \in L\}$

where $(w_1 w_2 \ldots w_n)^R = w_n w_{n-1} \ldots w_1$


**Proof:** Given a RE $E$ for $L$, define $E^R$ by **structural induction**:

**Basis:**
- $a^R = a$ for $a \in \Sigma$
- $\varepsilon^R = \varepsilon$
- $\emptyset^R = \emptyset$

**Induction:**
- $(E + F)^R = E^R + F^R$
- $(EF)^R = F^R E^R$ (order reverses!)
- $(E^*)^R = (E^R)^*$


The key trick: $(EF)^R = F^R E^R$ — just like matrix transpose: $(AB)^T = B^T A^T$


---

# Homomorphism

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Replace each symbol in a regular language with a string — the result is still regular.

</div>

A **homomorphism** is a function $h: \Sigma^* \to \Sigma^*$ defined symbol by symbol:

$$h(w) = h(w_1 w_2 \ldots w_n) = h(w_1) h(w_2) \ldots h(w_n)$$


**Example:** $h(0) = ab$, $h(1) = \varepsilon$

Then $h(0011) = ab \cdot ab \cdot \varepsilon \cdot \varepsilon = abab$


**Theorem:** If $L$ is regular, then so is $h(L) = \{h(w) \mid w \in L\}$

**Proof:** Given a RE $E$ for $L$, define $h(E)$ by replacing each symbol $a$ with $h(a)$ in the RE. The result is a valid RE for $h(L)$


---

# Inverse Homomorphism

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

On reading symbol $a$, simulate the original DFA on the entire string $h(a)$ — same states, new $\delta$.

</div>

**Theorem:** If $L$ is regular, then so is $h^{-1}(L) = \{w \mid h(w) \in L\}$


**Proof:** Let $A$ be the DFA for $L$. Construct a DFA for $h^{-1}(L)$:

$$\delta'(q, a) = \hat{\delta}_A(q, h(a))$$

**Idea:** On input symbol $a$, compute $h(a)$ (a string), then simulate $A$ on the entire string $h(a)$

**Example:** If $h(a) = 01$ and $A$ is in state $q$:
- Compute $\delta_A(q, 0) = p$
- Compute $\delta_A(p, 1) = r$
- So $\delta'(q, a) = r$


The new DFA has the **same states** as $A$ — only the transition function changes


---
layout: section
---

# Prefix Closures

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Two prefix-aware filters on regular languages — keep first hits, or keep dead ends.

</div>

NOPREFIX and NOEXTEND

---

# NOPREFIX and NOEXTEND

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Strip out strings whose proper prefixes (or extensions) are also in the language.

</div>

Two additional closure properties involving prefixes:


**NOPREFIX:** If $A$ is regular, so is:

$$\text{NOPREFIX}(A) = \{w \in A : \text{no proper prefix of } w \text{ is in } A\}$$

(Keep only the strings from $A$ that are "first hits" — no shorter prefix is already in $A$)

**NOEXTEND:** If $A$ is regular, so is:

$$\text{NOEXTEND}(A) = \{w \in A : w \text{ is not a proper prefix of any string in } A\}$$

(Keep only the strings from $A$ that are "dead ends" — no longer string in $A$ starts with $w$)


**Exercise:** Prove that both NOPREFIX and NOEXTEND preserve regularity by constructing appropriate automata


---

# Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Six problems to consolidate the closure proofs — including a concrete $h^{-1}$ computation.

</div>

1. Prove closure under complementation: given a DFA $A$ for $L$, construct $A'$ for $\overline{L}$, and prove $L(A') = \overline{L(A)}$

2. Why does complementation fail if we swap accept/reject states on an NFA? Give a concrete counterexample

3. Construct the product automaton for $L \cap M$ directly (without using DeMorgan's law)

4. Let $h(a) = 01$, $h(b) = 1$, and $L = \{w \in \{0,1\}^* \mid w \text{ ends in } 01\}$. What is $h^{-1}(L)$?

5. Give a regular language $A$ and compute $\text{NOPREFIX}(A)$ and $\text{NOEXTEND}(A)$

6. Prove that NOPREFIX preserves regularity by constructing a DFA

---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.5.2: Encodings
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Encodings
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

# Encodings

Section 9.5.2 - Turing Machines

---

# What is an Encoding?

<v-clicks>

- A foundational concept in computer science
- A systematic way to represent objects as strings
- **Definition:** A scheme to translate information from one format to another
- Encodings allow us to represent any object (text, machines, programs) as strings

</v-clicks>

---

# ASCII Encoding

**ASCII** = American Standard Code for Information Interchange

<v-clicks>

- Uses 7 bits per character (128 symbols total)
- First 32: non-printing legacy characters
- Remaining: standard keyboard symbols
- Example: 'A' = 65, 'Z' = 90

**Example:** Encoding "HELLO"

$$
\underbrace{01001000}_{H}
\underbrace{01000101}_{E}
\underbrace{01001100}_{L}
\underbrace{01001100}_{L}
\underbrace{01001111}_{O}
$$

</v-clicks>

---

# Extended Encodings

<v-clicks>

**Extended ASCII:**
- Uses full 8 bits (bytes) per character
- Standard ASCII has first bit = 0
- Extended symbols have first bit = 1
- Example: symbol 251 = '$\sqrt{\ }$'

**Unicode and UTF-8:**
- Unicode: standard for world's writing systems
- UTF-8: variable width (1-4 bytes per character)
- Can encode 1,112,064 valid code points
- UTF-8 extends Extended ASCII

</v-clicks>

---

# Common Encoding Formats

<v-clicks>

Much of computing is translating between encodings:

- **XML to JSON**
- **Base64:** radix-64 encoding using 64 symbols
  - Encodes chunks of 6 bits
  - Originally designed for MIME (email)
  - Common in cryptographic applications
- **Binary to text encodings**

</v-clicks>

---

# Encoding Automata

**Any object can be encoded!**

<v-click>

A DFA $B = (Q, \Sigma, \delta, q_0, F)$ where:
- $\Sigma = \{0,1\}$
- $Q = \{q_1, q_2, \ldots, q_n\}$ with $q_0 = q_1$
- $F = \{q_{i_1}, \ldots, q_{i_k}\}$

</v-click>

<v-click>

**Encoding:**

$$
\langle B\rangle := 0^{n}10^{l^0_1}10^{l^1_1}1
      0^{l^0_2}10^{l^1_2}1
      \ldots
      0^{l^0_n}10^{l^1_n}10^{i_1}10^{i_2}1\ldots 10^{i_k}
$$

</v-click>

---

# DFA Encoding Explained

$$
\langle B\rangle := 0^{n}10^{l^0_1}10^{l^1_1}1
      0^{l^0_2}10^{l^1_2}1
      \ldots
      0^{l^0_n}10^{l^1_n}10^{i_1}10^{i_2}1\ldots 10^{i_k}
$$

<v-clicks>

- $0^n$: number of states
- $0^{l^0_j}10^{l^1_j}$: from $q_j$, go to $q_{l^0_j}$ on 0 and $q_{l^1_j}$ on 1
- $0^{i_1}10^{i_2}1\ldots 10^{i_k}$: accepting states
- **Key property:** No two contiguous 1s in the encoding

</v-clicks>

---

# Encoding Pairs

<v-clicks>

Since no two 1s are contiguous in $\langle B\rangle$, we can encode pairs:

$$\langle B, w\rangle := \langle B\rangle 11w$$

- $\langle B\rangle$: encoding of the DFA
- $11$: separator (distinguishable from DFA encoding)
- $w$: the input string

This allows us to encode a DFA together with an input string!

</v-clicks>

---

# Encoding Turing Machines

**Example:** TM $M = (\{q_1, q_2\}, \{0,1\}, \delta, \ldots)$

If $\delta(q_1, 1) = (q_2, 0, \rightarrow)$:

$$
\underbrace{00}_{\text{2 states}}11
\overbrace{\underbrace{0}_{q_1}1
\underbrace{00}_11
\underbrace{00}_{q_2}1
\underbrace{0}_01
\underbrace{0}_\rightarrow}^{\delta(q_1,1)=(q_2,0,\rightarrow)}
11
\underbrace{\ldots}_{
\text{remaining transitions}}
$$

<v-click>

Every Turing machine can be encoded as a string over $\{0,1\}$!

</v-click>

---

# Well-Formed Strings (WFS)

<v-clicks>

**Problem:** Not every string encodes a valid TM

- Example: "1" does not encode anything

**Definition:** A string $x \in \{0,1\}^*$ is a **well-formed string (WFS)** if there exists a TM $M$ and string $w$ such that $x = \langle M, w\rangle$

**Key result:** The language of WFS is decidable!
- We can design a decider that checks if $x$ is a WFS

</v-clicks>

---

# Encoding vs. Encryption

<v-clicks>

**Exercise:** What is the difference?

**Encoding:**
- Systematic transformation for representation
- Publicly known scheme
- Purpose: format conversion, storage, transmission
- Example: ASCII, UTF-8, Base64

**Encryption:**
- Transformation to hide information
- Requires secret key
- Purpose: confidentiality, security
- Example: AES, RSA

</v-clicks>

---

# Summary

<v-clicks>

- **Encodings** represent objects as strings
- Common encodings: ASCII, UTF-8, Base64
- **Any object can be encoded:** text, DFAs, Turing machines
- Encoding scheme for DFAs uses unary notation and separators
- Encoding scheme for TMs encodes states and transitions
- **Well-formed strings:** strings that properly encode TM-input pairs
- The WFS language is decidable

</v-clicks>

---

# Key Takeaways

<v-clicks>

1. Encodings are fundamental to computer science
2. We can represent computational objects as strings
3. This allows us to reason about computation formally
4. Checking if a string is well-formed is decidable
5. This foundation enables the study of decidability and complexity

</v-clicks>

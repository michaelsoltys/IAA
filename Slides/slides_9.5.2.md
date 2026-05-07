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

# Encodings

Section 9.5.2 — How to write any object — DFAs, TMs, even pairs — as a string of $0$s and $1$s.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# What is an Encoding?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A *systematic*, public scheme that turns any object — text, machine, program — into a string.

</div>

- A foundational concept in computer science
- A systematic way to represent objects as strings
- **Definition:** A scheme to translate information from one format to another
- Encodings allow us to represent any object (text, machines, programs) as strings


<!--
The idea that "any object can be encoded as a string" looks innocuous but was revolutionary. Gödel used it in 1931 to encode logical formulas as natural numbers — Gödel numbering — which let him write self-referential statements about provability and prove his incompleteness theorems. Turing reused the same trick in 1936: encode TMs as strings so that TMs can take TM descriptions as input. That single move is what makes the halting problem, the universal TM, and Rice's theorem all possible. Encoding is not a clerical detail; it's the machinery that lets computation reason about itself.
-->

---

# ASCII Encoding

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The everyday encoding for English text — $7$ bits per character, $128$ symbols, one byte each.

</div>

**ASCII** = American Standard Code for Information Interchange


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


<!--
ASCII was standardized in 1963 by an ANSI committee chaired by Bob Bemer, sometimes called "the father of ASCII." The choice of 7 bits is a hardware compromise: teletype equipment of the era used 8-bit codes, and the 8th bit was reserved as a parity bit for error detection over noisy phone lines. Lowercase letters were initially omitted — uppercase only — and added later. Bemer was also the person who first publicly warned about the Y2K bug, in a 1971 paper. Nobody listened for another 28 years.
-->

---

# Extended Encodings

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Going beyond English: $8$-bit Extended ASCII, then Unicode and UTF-$8$ for *every* writing system on Earth.

</div>

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


<!--
UTF-8 has one of the best design anecdotes in computing. Ken Thompson and Rob Pike designed it in September 1992, at a diner in New Jersey, on a placemat, over dinner. They had three hours before a meeting at which a rival proposal was about to be adopted, and they needed an encoding that was self-synchronizing, backwards-compatible with ASCII, and never produced a zero byte inside a multi-byte sequence (so C strings wouldn't break). The placemat survived; Pike still has it. UTF-8 is now the encoding of more than 98% of the web.
-->

---

# Common Encoding Formats

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Real-world examples — XML, JSON, Base64 — and why so much of programming is translation.

</div>

Much of computing is translating between encodings:

- **XML to JSON**
- **Base64:** radix-64 encoding using 64 symbols
  - Encodes chunks of 6 bits
  - Originally designed for MIME (email)
  - Common in cryptographic applications
- **Binary to text encodings**


<!--
Base64 exists because early internet email was not 8-bit clean — SMTP servers in the 1980s could mangle bytes with the high bit set. MIME (1992) needed a way to send binary attachments through that fragile infrastructure, so it encoded every 3 bytes (24 bits) as 4 printable ASCII characters (6 bits each). The 33% size bloat was the cost of portability. The choice of exactly 64 symbols is the largest power of 2 that fits inside a safe printable-ASCII subset — letters, digits, plus two extra characters.
-->

---

# Encoding Automata

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A concrete recipe to write a DFA $B$ as a binary string $\langle B\rangle$ — states, transitions, accept set, all in $\{0,1\}^*$.

</div>

**Any object can be encoded!**


A DFA $B = (Q, \Sigma, \delta, q_0, F)$ where:
- $\Sigma = \{0,1\}$
- $Q = \{q_1, q_2, \ldots, q_n\}$ with $q_0 = q_1$
- $F = \{q_{i_1}, \ldots, q_{i_k}\}$


**Encoding:**

$$
\langle B\rangle := 0^{n}10^{l^0_1}10^{l^1_1}1
      0^{l^0_2}10^{l^1_2}1
      \ldots
      0^{l^0_n}10^{l^1_n}10^{i_1}10^{i_2}1\ldots 10^{i_k}
$$


---

# DFA Encoding Explained

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Reading the encoding piece by piece — and the crucial property that **no two $1$s are ever adjacent**.

</div>

$$
\langle B\rangle := 0^{n}10^{l^0_1}10^{l^1_1}1
      0^{l^0_2}10^{l^1_2}1
      \ldots
      0^{l^0_n}10^{l^1_n}10^{i_1}10^{i_2}1\ldots 10^{i_k}
$$


- $0^n$: number of states
- $0^{l^0_j}10^{l^1_j}$: from $q_j$, go to $q_{l^0_j}$ on 0 and $q_{l^1_j}$ on 1
- $0^{i_1}10^{i_2}1\ldots 10^{i_k}$: accepting states
- **Key property:** No two contiguous 1s in the encoding


---

# Encoding Pairs

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Use the double-$1$ as a separator: $\langle B,w\rangle := \langle B\rangle\,11\,w$ packs a machine and its input into one string.

</div>

Since no two 1s are contiguous in $\langle B\rangle$, we can encode pairs:

$$\langle B, w\rangle := \langle B\rangle 11w$$

- $\langle B\rangle$: encoding of the DFA
- $11$: separator (distinguishable from DFA encoding)
- $w$: the input string

This allows us to encode a DFA together with an input string!


---

# Encoding Turing Machines

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The same trick works for TMs — every transition $\delta(q,a)=(q',b,d)$ becomes a block of $0$s and $1$s.

</div>

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


Every Turing machine can be encoded as a string over $\{0,1\}$!


<!--
This is where Gödel's 1931 trick becomes Turing's 1936 trick. Once TMs are strings, a TM can take another TM's description as input — and that self-reference is the engine of every classical undecidability result. The halting problem — "does M halt on ⟨M⟩?" — only makes sense because M can read its own description. Rice's theorem (1953) goes further: every nontrivial semantic property of TMs is undecidable, proved by diagonalizing over encodings. No encoding, no diagonalization, no undecidability theorems.
-->

---

# Well-Formed Strings (WFS)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Most strings are *garbage* — but checking whether a string is a valid encoding is itself decidable.

</div>

**Problem:** Not every string encodes a valid TM

- Example: "1" does not encode anything

**Definition:** A string $x \in \{0,1\}^*$ is a **well-formed string (WFS)** if there exists a TM $M$ and string $w$ such that $x = \langle M, w\rangle$

**Key result:** The language of WFS is decidable!
- We can design a decider that checks if $x$ is a WFS


---

# Encoding vs. Encryption

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Both are public procedures — but encryption hides meaning behind a *secret key*; encoding does not.

</div>

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


<!--
The distinction was formalized by Auguste Kerckhoffs in 1883, in a principle that still governs modern cryptography: a cryptographic system should remain secure even if everything about it except the key is public. Shannon restated this in 1949 as "the enemy knows the system." So the real difference isn't "secret vs. open" — both encoding and encryption are usually public procedures. It's that encryption's output is designed to be indistinguishable from random without the key; an encoding's output is designed to be readable without any key.
-->

---

# Key Takeaways

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Once machines are strings, machines can read other machines — the door to self-reference and undecidability.

</div>

1. Encodings are fundamental to computer science
2. We can represent computational objects as strings
3. This allows us to reason about computation formally
4. Checking if a string is well-formed is decidable
5. This foundation enables the study of decidability and complexity

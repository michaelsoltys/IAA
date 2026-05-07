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

# Undecidability

Section 9.5.5 — The first natural problem we can prove no algorithm will ever solve.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# The Acceptance Problem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Can a single algorithm decide whether *any* TM accepts *any* input?

</div>

**The Language $A_{TM}$:**

$$A_{TM} = \{\langle M, w \rangle : \text{TM } M \text{ accepts } w\}$$


**The Question:** Is there a Turing Machine that can decide whether any arbitrary TM $M$ accepts a string $w$?

**The Answer:** No! This is **undecidable**.


---

# Theorem: $A_{TM}$ is Undecidable

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

No Turing machine — no algorithm at all — can answer the question for every $\langle M, w\rangle$.

</div>

**Theorem:** There is no Turing Machine that decides $A_{TM}$. <span style="font-size: 0.6em; color: navy;">Thm 9.66, Pg 253, thm:atm</span>


**Proof Idea:**
- Assume such a machine $H$ exists
- Construct a machine $D$ that contradicts itself
- Use diagonal argument (Cantor's technique)


---

# The Proof: Diagonal Argument

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Construct a machine $D$ that flips $H$'s answers — then ask $D$ about itself.

</div>

**Setup:** Suppose machine $H$ decides $A_{TM}$:
- Input: $\langle M, w \rangle$
- Output: **accept** if $M$ accepts $w$, **reject** if $M$ rejects or loops


**Define the "opposite" machine $D$:**

```text
D(⟨M⟩):
  if H(⟨M, ⟨M⟩⟩) = reject:
    return accept
  else:
    return reject
```

**Key Insight:** $D$ does the opposite of what $H$ says!


---

# The Contradiction

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$D(\langle D\rangle)$ accepts if and only if $D(\langle D\rangle)$ rejects — impossible, so $H$ can't exist.

</div>

**What happens with $D(\langle D \rangle)$?**


1. We run $D$ on its own encoding $\langle D \rangle$
2. This calls $H(\langle D, \langle D \rangle \rangle)$
3. If $H$ says "reject": $D$ returns **accept**
4. If $H$ says "accept": $D$ returns **reject**

**Contradiction!** $D$ accepts iff $D$ rejects.

Since this is impossible, our assumption is wrong.
$H$ cannot exist!


<!--
The diagonal trick is borrowed almost intact from Cantor (1891), who used it to prove that the real numbers are "more numerous" than the integers — uncountably many vs. countably many. Turing recognized in 1936 that the same trick works on Turing machines themselves: there are countably many TMs (each has a finite description string), but uncountably many languages over {0,1}, so by sheer counting most languages aren't even RE. Turing's contribution was to make this concrete: identify a *natural* language — A_TM — that diagonalizes itself out of decidability. Alonzo Church proved an equivalent result months earlier via the λ-calculus, but Turing's machine model was so visibly mechanical that his version is the one that stuck.
-->

---

# Practical Consequence: The Halting Problem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

No debugger can ever tell you whether an arbitrary program would have eventually finished.

</div>

Imagine you're developing a debugger:


- You run a program on input $x$
- Nothing happens for a long time
- You press CTRL+C to stop it
- Question: Was I too hasty? Would it have finished given more time?


**The theorem says:** This "halting feature" **cannot be implemented** for all programs!


We can build partial solutions that work on some inputs, but no algorithm works for every program and input.


<!--
Turing's 1936 paper never used the phrase "halting problem." He framed it as the "circle problem": a TM is "circle-free" if it goes on printing infinitely many symbols, "circular" otherwise. The crisper name *halting problem* was coined by Martin Davis in his 1958 textbook *Computability and Unsolvability*, and it stuck so well that today most people assume Turing called it that himself. A reminder that good naming can outlive its inventor — and that even foundational results need a marketing pass.
-->

---

# Understanding the Limitation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Undecidable means *no algorithm works for every input* — not that every individual case is hopeless.

</div>

**Important Distinction:**

$A_{TM}$ is **undecidable** means:
- ❌ No TM halts with correct answer on ALL inputs

But:
- ✓ Some TM can halt correctly on SOME inputs
- ✓ We can build approximations (e.g., timeout after $n$ steps)
- ✓ We cannot verify correctness in general

---

# The Complement Problem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$\overline{A_{TM}}$ is even worse than undecidable — it's not even *recognizable*.

</div>

**Corollary:** $\overline{A_{TM}}$ is **not Recursively Enumerable (RE)** <span style="font-size: 0.6em; color: navy;">Thm 9.68, Pg 254, thm:zero</span>


**Proof sketch:**
- $A_{TM}$ is RE (the universal TM $U$ recognizes it)
- If both $A_{TM}$ and $\overline{A_{TM}}$ were RE, then $A_{TM}$ would be decidable
- But we know $A_{TM}$ is not decidable
- Therefore, $\overline{A_{TM}}$ is not RE


---

# The Busy Beaver Function

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$\Sigma(n)$ grows so fast it outpaces *every* computable function.

</div>

**Definition:** $\Sigma(n)$ = maximum number of 1's that a TM with $n$ states can write on a blank tape before halting.

Known values:
- $\Sigma(2) = 4$
- $\Sigma(3) = 6$
- $\Sigma(4) = 13$
- $\Sigma(5) \geq 4,098$
- $\Sigma(6) \geq 3.5 \times 10^{18267}$ ⚠️

**Key Result:** The Busy Beaver function is **undecidable**

<!--
Σ(5) was famously open for over fifty years. Heiner Marxen and Jürgen Buntrock conjectured Σ(5) = 4098 in 1989 after exhaustive search couldn't beat their 5-state machine, but no one could rule out a survivor that they had missed. In **July 2024**, the Busy Beaver Challenge — an online collaboration of amateur and professional researchers — confirmed Σ(5) = 4098 *exactly*, with a Coq-verified proof. It's one of those rare results where a problem opened in the 1960s gets shut decades later by distributed Internet effort. Σ(6) is in another league: specific 6-state TMs are now known whose halting is provably independent of ZFC — meaning whether they halt is, in a precise mathematical sense, beyond what mathematics itself can decide. The Busy Beaver function isn't just uncomputable; from Σ(6) onward, it actively encodes the limits of formal mathematics.
-->

---

# Busy Beaver Proof

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If $\Sigma$ were computable, simulating $M'$ for $\Sigma(\cdot)$ steps would decide $A_{TM}$ — contradiction.

</div>

**How does Busy Beaver relate to $A_{TM}$?**

If Busy Beaver were decidable, we could decide $A_{TM}$:


1. Given $\langle M, w \rangle$, construct $M'$ that:
   - Writes $w$ on empty tape
   - Simulates $M$ on $w$

2. Compute $\Sigma(|Q_{M'}|, |\Gamma_{M'}|)$ = max steps before halting

3. Simulate $M'$ for $\Sigma(|Q_{M'}|, |\Gamma_{M'}|)$ steps
   - If it halts: answer is definite ✓
   - If it doesn't: it never will ✓

This would decide $A_{TM}$ — contradiction!


---

# Reductions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Show $X$ is undecidable by encoding $A_{TM}$ as an instance of $X$ — undecidability propagates.

</div>

**Key Technique:** Show undecidability by **reduction** from $A_{TM}$

**The Halting Problem:**
$$\text{HALT} = \{\langle M, w \rangle : M \text{ halts on } w\}$$


**Proof:** If $\text{HALT}$ were decidable with decider $H'$, we could decide $A_{TM}$:
- Run $H'$ on $\langle M, w \rangle$
- If $M$ halts: simulate $M$ on $w$ and answer accordingly
- Result: decider for $A_{TM}$ — contradiction!


---

# More Undecidable Problems

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Asking *anything* nontrivial about a TM's language tends to be undecidable.

</div>

**$E_{TM}$ = "Does TM $M$ accept empty language?"**

$$E_{TM} = \{\langle M \rangle : L(M) = \emptyset\}$$


**$\text{REGULAR}_{TM}$ = "Is the language of TM $M$ regular?"**

$$\text{REGULAR}_{TM} = \{\langle M \rangle : L(M) \text{ is regular}\}$$

Both undecidable by reduction from $A_{TM}$!


---

# Rice's Theorem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Any nontrivial property of $L(M)$ — anything depending only on the language, not on syntax — is undecidable.

</div>

**Theorem:** Every **nontrivial property** of Turing Machine languages is undecidable. <span style="font-size: 0.6em; color: navy;">Thm 9.70, Pg 256, thm:rice</span>


**What is a nontrivial property?**
- A property $\mathcal{P}$ is a set of TM descriptions
- Nontrivial: $\mathcal{P} \neq \emptyset$ and $\overline{\mathcal{P}} \neq \emptyset$
- Language-dependent: if $L(M_1) = L(M_2)$, then $M_1 \in \mathcal{P}$ iff $M_2 \in \mathcal{P}$

**Examples:**
- "Is $L$ non-empty?" → Undecidable
- "Does $L$ contain a specific string?" → Undecidable
- "Is $L$ infinite?" → Undecidable


---

# Enumerators and Recognizers

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A language is recognizable exactly when its strings can be *listed* by a TM — proven via dovetailing.

</div>

**Enumerator:** A TM with a write-only output tape that lists strings of a language

**Theorem:** A language is **recognizable** iff it is **enumerable** <span style="font-size: 0.6em; color: navy;">Thm 9.69, Pg 254, thm:enumerable</span>


**Proof sketch:**
- If $L$ is enumerable: simulate enumerator, accept when $w$ appears ✓
- If $L$ is recognizable: use "dovetailing" to enumerate:
  - Phase 1: Try string 1 for 1 step
  - Phase 2: Try strings 1-2 for 2 steps each
  - Phase 3: Try strings 1-3 for 3 steps each
  - Output strings that are accepted

This interleaving ensures no string is missed!


---

# Post's Correspondence Problem (PCP)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A pure string-matching puzzle: find indices $i_1, \ldots, i_m$ that make the two concatenations agree.

</div>

**Definition:** Given two lists of strings over alphabet $\Sigma$:
- List $A = w_1, w_2, \ldots, w_k$
- List $B = x_1, x_2, \ldots, x_k$

**Does a solution exist?** Sequence of indices $i_1, i_2, \ldots, i_m$ such that:
$$w_{i_1}w_{i_2}\cdots w_{i_m} = x_{i_1}x_{i_2}\cdots x_{i_m}$$

---

# PCP Example

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A small instance whose solution makes both sides spell out the same string $10111110$.

</div>

**Lists:**
- $A = \{1, 10111, 10\}$
- $B = \{111, 10, 0\}$

**Solution:** Indices $2, 1, 1, 3$

$$\underbrace{10111}_{w_2}\underbrace{1}_{w_1}\underbrace{1}_{w_1}\underbrace{10}_{w_3} = \underbrace{10}_{x_2}\underbrace{111}_{x_1}\underbrace{111}_{x_1}\underbrace{0}_{x_3}$$

Both sides: $10111110$ ✓

---

# PCP is Undecidable

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Reduce $A_{TM} \to$ MPCP $\to$ PCP: an accepting computation becomes a tile match.

</div>

**Theorem:** The Post's Correspondence Problem is undecidable. <span style="font-size: 0.6em; color: navy;">Lem 9.5.8, Pg 257, lem:pcp-mpcp</span>

**Proof Strategy (3 steps):**


1. PCP ≥ Modified PCP (MPCP) in difficulty
2. MPCP ≥ $A_{TM}$ in difficulty
3. Since $A_{TM}$ undecidable, so is PCP

**Key Construction:** Encode TM computation as MPCP instance
- Partial solutions represent TM configurations
- Solution exists iff $M$ accepts $w$


<!--
Emil Post invented the Correspondence Problem in 1946, but his story goes much deeper than this one paper. Post is one of the great underappreciated logicians of the 20th century: he proved a Church–Turing-thesis-equivalent result using "tag systems" as early as 1921 — over a decade before Gödel, Church, and Turing reached the same conclusions independently — but published only fragments due to lifelong struggles with bipolar disorder, and lost the historical credit. PCP itself is striking because it has *no obvious connection* to computation. It looks like a tile-matching puzzle. Yet it's exactly as undecidable as the halting problem. That's the deep lesson of reductions: undecidability is *contagious* — once you have one undecidable problem, anything that can simulate a Turing machine catches it.
-->

---

# Key Takeaways

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Undecidability is foundational, propagates by reduction, and is everywhere we look.

</div>

- **$A_{TM}$ is undecidable** - no algorithm can decide if any TM accepts input
- **Proof uses diagonalization** - contradiction argument (Cantor's technique)
- **Natural problems are undecidable** - halting, empty language, regularity, etc.
- **Rice's Theorem** - all nontrivial language properties undecidable
- **Reductions** - show undecidability of new problems via $A_{TM}$
- **Post's Problem** - undecidable even without explicit model of computation


---

# Implications for Computer Science

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Undecidability isn't a footnote — it shapes what verifiers, compilers, and type systems can ever do.

</div>

1. **Program Verification:** Cannot verify all program properties
2. **Debugging:** Cannot build universal halting detector
3. **Compiler Design:** Cannot optimize away all infinite loops
4. **Type Systems:** Cannot infer all type relationships
5. **Security:** Some security properties are undecidable

**Lesson:** Undecidability is a fundamental limit of computation, not a limitation of current technology!

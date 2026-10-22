# Chapter 1: Preliminaries

## Overview

> "It is commonly believed that more than 70% (!) of the effort and cost of developing a complex software system is devoted, in one way or another, to error correcting." — Algorithms, Harel

This chapter establishes the fundamental framework for algorithm analysis, covering correctness proofs, complexity analysis, and three classical ranking algorithms (PageRank, Stable Marriage, Pairwise Comparisons). The chapter emphasizes that proving correctness is not pedantic formalism but a real necessity given the catastrophic failures that can result from software bugs.

## Section 1.1: What is Correctness?

### Hoare's Logic Framework

**Fundamental approach:** Use pre-conditions, post-conditions, and loop invariants to prove algorithm correctness.

**Key Definitions:**
- **Pre-condition** (α_A): Assertion that holds BEFORE algorithm executes
- **Post-condition** (β_A): Assertion that holds AFTER algorithm executes
- **Partial correctness**: If pre-condition holds and algorithm terminates, post-condition holds
- **Full correctness**: Partial correctness + guaranteed termination
- **Loop invariant**: Assertion that remains true after each loop iteration

**Correctness formula (partial):**
```
(∀I∈I_A)[(α_A(I) ∧ ∃O(O=A(I))) → β_A(A(I))]
```

**Method:**
1. Choose suitable pre-condition and post-condition
2. Identify loop invariant
3. Prove invariant by induction on number of iterations
4. Use invariant to prove partial correctness
5. Show termination (typically using Least Number Principle)

### Complexity Analysis

**Random Access Machine model:** Assignments, arithmetic operations, and Boolean tests all count as single steps.

**Worst-case complexity:** T(n) = maximal running time on any input of size n

**Asymptotic Notation:**
- **Big-O** (O): Upper bound — g(n) ∈ O(f(n)) if ∃c,n₀: ∀n≥n₀, g(n) ≤ cf(n)
- **Big-Omega** (Ω): Lower bound — g(n) ∈ Ω(f(n)) if ∃c,n₀: ∀n≥n₀, g(n) ≥ cf(n)
- **Big-Theta** (Θ): Tight bound — g(n) ∈ Θ(f(n)) if g(n) ∈ O(f(n)) ∩ Ω(f(n))
- **little-o** (o): Strictly smaller — g(n) ∈ o(f(n)) if lim(n→∞) g(n)/f(n) = 0

**Example:** an² + bn + c = Θ(n²) where a > 0

### Algorithm 1: Division

**Input:** x ≥ 0, y > 0, x,y ∈ ℕ
**Output:** q, r where x = q·y + r and 0 ≤ r < y

```
q ← 0
r ← x
while (y ≤ r):
    r ← r - y
    q ← q + 1
return q, r
```

**Loop invariant:** x = q·y + r ∧ r ≥ 0

**Correctness proof:**
- Basis: Initially q=0, r=x, so x = 0·y + x ✓
- Induction: If invariant holds and we iterate once more:
  - x = q·y + r = (q+1)·y + (r-y) = q'·y + r' ✓
- Termination: Sequence r₀, r₁, r₂,... is decreasing and non-negative (LNP)

**Complexity:** O(x) steps, which is **exponential** in input size log₂(x)!
- Not practical for large x (much faster algorithms exist, e.g., Newton-Raphson)

### Algorithm 2: Euclid's Algorithm

**Input:** a > 0, b > 0, a,b ∈ ℤ
**Output:** n = gcd(a,b)

```
m ← a; n ← b; r ← rem(m,n)
while (r > 0):
    m ← n; n ← r; r ← rem(m,n)
return n
```

**Key lemma:** gcd(m,n) = gcd(n, rem(m,n))

**Loop invariant:** m > 0, n > 0, and gcd(m,n) = gcd(a,b)

**Complexity:** O(log(m·n)) = O(log m + log n) — **linear in input size**
- Much more efficient than division algorithm!
- Lamé's theorem gives tighter bound using Fibonacci numbers

**Extended Euclid's Algorithm:** Computes x,y such that mx + ny = gcd(m,n)
- Uses LNP to show such x,y exist
- Polynomial time in min{|m|ᵦ, |n|ᵦ}

### Algorithm 3: Palindromes

**Input:** Array A[0...n-1] of characters
**Output:** true iff A is a palindrome

```
i ← 0
while (i < ⌊n/2⌋):
    if (A[i] ≠ A[n-i-1]):
        return false
    i ← i + 1
return true
```

**Loop invariant:** After k-th iteration, i = k+1 and ∀j (1≤j≤k): A[j] = A[n-j+1]

**Python elegance:** `s == s[::-1]` checks palindrome in one line!

### Further Examples

**Powers of 2:** Algorithm to check if n = 2^k
**Multiplication:** Algorithm computes m·n using doubling/halving
**Ulam's Algorithm (3x+1 problem):**
- If x even: x ← x/2
- If x odd: x ← 3x+1
- **No known proof of termination!**
- Demonstrates that proving correctness is genuinely difficult

## Section 1.2: Ranking Algorithms

### PageRank

**Context:** Ranking billions of web pages by authority/quality

**Key insight:** Exploit hyperlink structure as implicit endorsements
- Important pages are linked to by other important pages
- Similar to academic citations

**The Formula:**
```
PR(X) = (1-d)/N + d · Σᵢ [PR(Tᵢ)/C(Tᵢ)]
```
Where:
- d ≈ 0.85 (damping factor) — probability of following links vs. random jump
- N = total web pages
- Tᵢ = pages pointing to X
- C(Tᵢ) = number of outlinks from Tᵢ

**Random surfer interpretation:**
- (1-d)/N: probability of randomly jumping to page X
- d·PR(Tᵢ)/C(Tᵢ): probability of reaching X by following link from Tᵢ

**Algorithm:**
1. Initialize: PR(p) = 1/N for all pages p
2. Iterate: Recompute all PR values using formula
3. Stop when convergence achieved

**Complexity:** Must handle N > 10¹² pages!

**Extensions:** Modern search considers:
- Link context (font size, emphasis tags)
- Document type (PDF, text, image, video)
- Source reputation, update frequency, popularity

**Observer effect:** Search engines shape the rankings they measure

### Stable Marriage Problem

**Input:**
- n boys B = {b₁,...,bₙ}
- n girls G = {g₁,...,gₙ}
- Each boy has preference ranking <ᵢ over girls
- Each girl has preference ranking <ʲ over boys

**Matching M:** Bijection between B and G

**Blocking pair (b,g):** b and g prefer each other to their partners in M
- b prefers g to pₘ(b)
- g prefers b to pₘ(g)

**Stable matching:** No blocking pairs exist

**Gale-Shapley Algorithm:**
- Boys propose to girls in order of preference
- Girls accept if unengaged or if new proposer is better than current partner
- Rejected boys continue proposing down their list

**Key properties:**
- Always terminates in O(n³) steps
- Always produces stable matching
- **Boy-optimal:** Each boy gets his best possible partner among all stable matchings
- **Girl-pessimal:** Each girl gets her worst possible partner among all stable matchings
- Order of boys is irrelevant (unique boy-optimal matching)

**Real-world applications:**
- College admissions
- Medical residency matching (since 1960s)
- **2012 Nobel Prize** awarded to Shapley and Roth for this work!

### Pairwise Comparisons

**History:**
- 13th century: Ramon Llull (voting systems)
- 1785: Marquis de Condorcet (voting analysis)
- 1927: Thurstone (psychological continuum)
- 1977: Saaty (AHP — Analytic Hierarchy Process)

**Pairwise Comparison Matrix:** A = [aᵢⱼ] where:
- aᵢⱼ > 0 represents "how much better" xᵢ is than xⱼ
- aᵢⱼ = 1/aⱼᵢ (reciprocal property)
- If aᵢⱼ > 1, then xᵢ preferred over xⱼ

**Consistent matrix:** aᵢⱼ · aⱼₖ = aᵢₖ for all i,j,k

**Saaty's Theorem:** Matrix A is consistent ⟺ ∃w₁,...,wₙ such that aᵢⱼ = wᵢ/wⱼ
- The weights wᵢ define a ranking

**Challenges with inconsistent matrices:**
1. How to measure inconsistency?
2. How to reduce inconsistency to acceptable level?
3. How to derive weights wᵢ from inconsistent A?
4. How to justify methods for handling inconsistency?

**Applications:** Medical decision-making, management, complex multi-criteria decisions

## Common Patterns and Techniques

### Proving Correctness

**General approach:**
1. Define pre-condition and post-condition
2. Identify loop invariant(s)
3. Prove invariant holds by induction:
   - **Base case:** Show invariant holds before first iteration
   - **Inductive step:** Assume invariant holds after k iterations, prove it holds after k+1
4. Use invariant to prove post-condition holds when algorithm terminates
5. Prove termination using LNP or other technique

### Proving Termination

**Least Number Principle (LNP):**
- Identify monotone decreasing sequence of non-negative integers
- By LNP, sequence must be finite
- Therefore algorithm terminates

**Examples:**
- Division: r₀, r₁, r₂,... where rᵢ₊₁ = rᵢ - y
- Euclid: alternating decreases in m and n
- Palindromes: ⌊n/2⌋ - i

### Program Refinement

**"Proof-driven programming":** Construct informal correctness arguments while coding
- Think about invariants
- Verify monotonicity
- Check pre/post-conditions
- Use induction for recursive algorithms

**Benefits:**
- Reduces debugging time
- Increases code reliability
- Catches errors before execution

## Important Exercises

### Correctness Proofs
- **Exercise 1.1:** Modify partial correctness formula for full correctness
- **Exercise 1.2:** Prove division algorithm terminates
- **Exercise 1.4:** Prove Euclid's algorithm terminates and analyze complexity
- **Exercise 1.5:** Design and prove Extended Euclid's algorithm

### Complexity Analysis
- **Exercise 1.3:** Show Σaᵢnⁱ = Θ(nᵏ) for polynomial of degree k
- **Exercise 1.6:** Analyze average-case complexity of Extended Euclid

### Implementation
- **Exercise 1.7:** Implement division algorithm
- **Exercise 1.8:** Implement Euclid's algorithm
- **Exercise 1.9:** Implement palindrome checker in Python
- **Exercise 1.10:** Implement PageRank
- **Exercise 1.11:** Implement Gale-Shapley algorithm

### Theoretical
- **Exercise 1.12:** Analyze Ulam's algorithm (3x+1 problem)
- **Exercise 1.13:** Prove properties of stable marriage algorithm

## Key Concepts and Takeaways

### Correctness is Critical

**Real-world failures:**
- 2003 North-East blackout: Software bug in alarm system ($500M+ damage)
- Ariane 5 flight 501: Overflow in 64→16 bit conversion ($500M loss)
- Software security vulnerabilities

**Hoare's observation:** "We still certainly do not know how to prove programs correct."

**Current challenge:** No incentive for developers to produce secure, correct software

### Levels of Confidence

1. **Algorithm correctness:** Does the algorithm solve the problem?
2. **Implementation correctness:** Does the code match the algorithm?
3. **Compiler correctness:** Does compiled code preserve semantics?
4. **Hardware correctness:** Does hardware execute correctly?
5. **Library correctness:** Are runtime dependencies bug-free?

**This book focuses on level 1:** Proving algorithms correct

### Complexity Matters

**Exponential vs. Polynomial:**
- Division algorithm: O(2ⁿ) in input size — impractical
- Euclid's algorithm: O(n) in input size — practical

**Input encoding matters:**
- Size of n is log₂(n) bits
- Algorithm in O(n) is exponential in input size!
- Algorithm in O(log n) is polynomial in input size

### Mathematical Foundations

**Essential tools:**
- **Induction:** For proving loop invariants and recursive correctness
- **LNP:** For proving termination
- **Asymptotic analysis:** For characterizing complexity
- **Logic:** For expressing pre/post-conditions

## Notes and Historical Context

### Software Correctness Crisis

**Ed Amoroso (AT&T):** "We have to write software which has many fewer errors and which is more secure."

**Fred Taylor (USAF):** "For most software developers there is no incentive to produce software that is more secure."

**Software complexity:** Often only small fraction is algorithmic content; majority is interface programming

### Practical Approaches

**Informal verification while coding:**
- Think about monotonicity
- Maintain mental invariants
- Verify pre/post-conditions
- Use induction for recursion

**Better than:** Write code, run, debug cycle

### Cultural Impact

**Palindromes:** "madamimadam" from Joyce's *Ulysses*

**Python vs. Perl:**
- Python excels at readability and data structures
- Perl excels at string manipulation (regex power)

**PageRank:** $1 trillion company (Google) founded on this algorithm

**Stable Marriage:** Applied to life-changing decisions (college, medical residency)

## Summary

Chapter 1 establishes the theoretical and practical foundations for algorithm analysis:

1. **Correctness framework:** Pre-conditions, post-conditions, loop invariants, termination
2. **Complexity analysis:** Big-O notation, worst-case analysis, input encoding
3. **Classical algorithms:** Division, Euclid, Palindromes (with full correctness proofs)
4. **Ranking algorithms:** PageRank, Stable Marriage, Pairwise Comparisons
5. **Real-world impact:** Software failures cost lives and billions of dollars

**Central message:** Proving correctness is difficult but essential. The techniques introduced (invariants, induction, asymptotic analysis) provide systematic approaches to building confidence in algorithmic solutions.

**Key skill:** Ability to construct rigorous arguments about algorithm behavior, combining:
- Mathematical proof techniques
- Inductive reasoning
- Complexity analysis
- Practical implementation awareness

The chapter balances theory (formal correctness proofs) with practice (real algorithms solving real problems), setting the stage for deeper algorithmic study in subsequent chapters.

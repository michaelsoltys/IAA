---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 9.4: Logic
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Logic - Propositional and First Order
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

# Logic

Section 9.4 - Mathematical Foundations

---

# Overview

This section presents the foundations of logic with the aim of defining **Peano Arithmetic (PA)**

<v-clicks>

**Two main topics:**
1. **Propositional Logic** - Boolean formulas and reasoning
2. **First Order Logic** - Predicate calculus with quantifiers

**Goal:** Provide logical background for formal verification of algorithms

**Scope:** Limited to foundations needed for understanding formal systems

</v-clicks>

---
layout: section
---

# Propositional Logic

Building blocks of logical reasoning

---

# Propositional Formulas

**Propositional (Boolean) formulas** are built from:

<v-clicks>

- **Propositional variables:** $p_1, p_2, p_3, \ldots$ (also called **atoms**)
  - Often use labels: $a, b, c, \ldots$ or $p, q, r, \ldots$

- **Logical connectives:**
  - $\neg$ (negation, NOT)
  - $\wedge$ (conjunction, AND)
  - $\vee$ (disjunction, OR)
  - $\rightarrow$ (implication)
  - $\leftrightarrow$ (equivalence)

</v-clicks>

---

# Definition by Structural Induction

**Base case:** Any variable $p$ is a formula

**Inductive cases:** If $\alpha, \beta$ are formulas, then:
- $\neg\alpha$ is a formula
- $(\alpha \wedge \beta)$ is a formula
- $(\alpha \vee \beta)$ is a formula

<v-click>

**Examples:**
- $p$
- $(p \vee q)$
- $(\neg(p \wedge q) \wedge (\neg p \vee \neg q))$

</v-click>

---

# Exercise: CFG for Propositional Formulas

**Exercise:** Define propositional formulas with a context-free grammar

<v-click>

**Solution sketch:**
```text
Formula → Variable
        | ¬ Formula
        | ( Formula ∧ Formula )
        | ( Formula ∨ Formula )

Variable → p | q | r | ...
```

This gives us a formal syntax for well-formed formulas!

</v-click>

---

# Unique Readability

**Key property:** No proper initial segment of a formula is a formula

<v-click>

**Weight Assignment:**
| Symbol | Weight |
|--------|--------|
| $\neg$ | 0 |
| $\wedge, \vee, ($ | 1 |
| $), p$ (any variable) | -1 |

</v-click>

<v-click>

**Lemma:** Any formula $\alpha$ has weight $-1$, but any proper initial segment has weight $\geq 0$

</v-click>

---

# Unique Readability Theorem

**Theorem:** Suppose $\alpha, \beta, \alpha', \beta'$ are formulas and $c, c'$ are binary connectives. If:
$$(\alpha \, c \, \beta) \equiv (\alpha' \, c' \, \beta')$$
(syntactically identical)

Then: $\alpha \equiv \alpha'$ and $\beta \equiv \beta'$ and $c \equiv c'$

<v-click>

**Meaning:**
- The grammar is unambiguous
- Only one candidate for the main connective
- The parse tree is unique
- Despite infix notation, parentheses make it unambiguous!

</v-click>

---

# Truth Assignments

A **truth assignment** is a map:
$$\tau: \{\text{variables}\} \longrightarrow \{T, F\}$$

<v-click>

Extend $\tau$ to all formulas:
1. $(\neg\alpha)^\tau = T$ iff $\alpha^\tau = F$
2. $(\alpha \wedge \beta)^\tau = T$ iff $\alpha^\tau = T$ **and** $\beta^\tau = T$
3. $(\alpha \vee \beta)^\tau = T$ iff $\alpha^\tau = T$ **or** $\beta^\tau = T$

</v-click>

---

# Semantic Concepts

<v-clicks>

**Satisfies:** Truth assignment $\tau$ **satisfies** formula $\alpha$ if $\alpha^\tau = T$
- $\tau$ satisfies set $\Phi$ if $\tau$ satisfies all $\alpha \in \Phi$

**Satisfiable:** Set $\Phi$ is **satisfiable** if some $\tau$ satisfies it
- Otherwise, $\Phi$ is **unsatisfiable**

**Logical Consequence:** $\Phi \vDash \alpha$ means:
- Every $\tau$ that satisfies $\Phi$ also satisfies $\alpha$

**Valid:** $\vDash \alpha$ means $\alpha^\tau = T$ for all $\tau$
- Valid formulas are called **tautologies**

**Equivalent:** $\alpha \iff \beta$ means $\alpha \vDash \beta$ and $\beta \vDash \alpha$

</v-clicks>

---

# Examples

**Tautologies:**
- $p \vee \neg p$ (Law of Excluded Middle)
- $p \rightarrow p$ (Identity)
- $\neg(p \wedge \neg p)$ (Non-contradiction)

<v-click>

**Logical Consequence:**
- $(p \wedge q) \vDash (p \vee q)$

</v-click>

<v-click>

**Equivalence (De Morgan's Law):**
- $\neg(p \vee q) \iff (\neg p \wedge \neg q)$

</v-click>

---

# Important Exercises

**Exercise:** Show that if $\Phi \vDash \alpha$ and $\Phi \cup \{\alpha\} \vDash \beta$, then $\Phi \vDash \beta$

<v-click>

**Duality Theorem:** Let $\alpha'$ be the result of:
- Interchanging $\vee$ and $\wedge$ in $\alpha$
- Replacing each $p$ by $\neg p$

Then: $\neg\alpha \iff \alpha'$

</v-click>

<v-click>

**Craig Interpolation Theorem:** If $A \rightarrow B$ is valid and variables sets overlap, there exists an "interpolant" $C$ using only common variables such that both $A \rightarrow C$ and $C \rightarrow B$ are valid

</v-click>

---
layout: section
---

# The PK Proof System

Formal proofs in propositional logic

---

# Sequent Calculus (PK)

**PK** = "Propositional Kalkül" (German logician Gentzen)

**Sequent:** A line of the form
$$\alpha_1, \ldots, \alpha_k \rightarrow \beta_1, \ldots, \beta_l$$

where:
- $\alpha_1, \ldots, \alpha_k$ is the **antecedent** (assumptions)
- $\beta_1, \ldots, \beta_l$ is the **succedent** (conclusions)
- $k, l \geq 0$ (can be empty)

<v-click>

**Meaning:** "If all $\alpha_i$ are true, then at least one $\beta_j$ is true"

Equivalent to: $(\alpha_1 \wedge \cdots \wedge \alpha_k) \rightarrow (\beta_1 \vee \cdots \vee \beta_l)$

</v-click>

---

# Special Cases of Sequents

<v-clicks>

- $\rightarrow \alpha$ means $\alpha$ (succedent only)
- $\alpha \rightarrow$ means $\neg\alpha$ (antecedent only)
- $\rightarrow$ is **false** (empty sequent is unsatisfiable)

**Valid sequents:**
- $\alpha \rightarrow \alpha$ (identity)
- $\rightarrow \alpha, \neg\alpha$ (excluded middle)
- $\alpha \wedge \neg\alpha \rightarrow$ (contradiction)

</v-clicks>

---

# PK Proof Structure

A **PK proof** is a finite rooted tree where:

<v-clicks>

- **Nodes** are labeled with sequents
- **Root** (bottom) is the **endsequent** (what we're proving)
- **Leaves** (top) are **logical axioms**: $\alpha \rightarrow \alpha$
- **Interior nodes** follow from parent(s) by **inference rules**

**Direction:** Tree grows from leaves (top/axioms) down to root (bottom/goal)

</v-clicks>

---

# Weak Structural Rules

**Exchange** (reorder formulas):
$$\frac{\Gamma_1, \alpha, \beta, \Gamma_2 \rightarrow \Delta}{\Gamma_1, \beta, \alpha, \Gamma_2 \rightarrow \Delta} \quad \frac{\Gamma \rightarrow \Delta_1, \alpha, \beta, \Delta_2}{\Gamma \rightarrow \Delta_1, \beta, \alpha, \Delta_2}$$

**Contraction** (remove duplicates):
$$\frac{\Gamma, \alpha, \alpha \rightarrow \Delta}{\Gamma, \alpha \rightarrow \Delta} \quad \frac{\Gamma \rightarrow \Delta, \alpha, \alpha}{\Gamma \rightarrow \Delta, \alpha}$$

**Weakening** (add formulas):
$$\frac{\Gamma \rightarrow \Delta}{\alpha, \Gamma \rightarrow \Delta} \quad \frac{\Gamma \rightarrow \Delta}{\Gamma \rightarrow \Delta, \alpha}$$

---

# Logical Rules - Negation

$$\frac{\Gamma \rightarrow \Delta, \alpha}{\neg\alpha, \Gamma \rightarrow \Delta} \text{(¬-left)} \quad \frac{\alpha, \Gamma \rightarrow \Delta}{\Gamma \rightarrow \Delta, \neg\alpha} \text{(¬-right)}$$

<v-click>

**Intuition:**
- To prove $\neg\alpha$ on right, prove $\alpha$ on left
- If $\neg\alpha$ is an assumption (left), then $\alpha$ must be a conclusion (right)

</v-click>

---

# Logical Rules - Conjunction

$$\frac{\alpha, \beta, \Gamma \rightarrow \Delta}{(\alpha \wedge \beta), \Gamma \rightarrow \Delta} \text{(∧-left)}$$

$$\frac{\Gamma \rightarrow \Delta, \alpha \quad \Gamma \rightarrow \Delta, \beta}{\Gamma \rightarrow \Delta, (\alpha \wedge \beta)} \text{(∧-right)}$$

<v-click>

**Intuition:**
- Left: If we assume $\alpha \wedge \beta$, we can use both $\alpha$ and $\beta$
- Right: To prove $\alpha \wedge \beta$, must prove both $\alpha$ and $\beta$ (two premises!)

</v-click>

---

# Logical Rules - Disjunction

$$\frac{\alpha, \Gamma \rightarrow \Delta \quad \beta, \Gamma \rightarrow \Delta}{(\alpha \vee \beta), \Gamma \rightarrow \Delta} \text{(∨-left)}$$

$$\frac{\Gamma \rightarrow \Delta, \alpha, \beta}{\Gamma \rightarrow \Delta, (\alpha \vee \beta)} \text{(∨-right)}$$

<v-click>

**Intuition:**
- Left: If we assume $\alpha \vee \beta$, must handle both cases (two premises!)
- Right: To prove $\alpha \vee \beta$, proving either $\alpha$ or $\beta$ suffices

</v-click>

---

# Cut Rule

The powerful (and controversial) **cut rule**:

$$\frac{\Gamma \rightarrow \Delta, \alpha \quad \alpha, \Gamma \rightarrow \Delta}{\Gamma \rightarrow \Delta}$$

<v-clicks>

**Meaning:**
- First premise: We can prove $\alpha$ (or something else in $\Delta$)
- Second premise: Assuming $\alpha$ leads to conclusion
- Conclusion: We can reach the conclusion without mentioning $\alpha$

**The Cut Formula** $\alpha$ is called the "lemma" being used

**Remarkable fact:** Cut is admissible but not necessary (Cut Elimination Theorem)

</v-clicks>

---

# Soundness and Completeness

**Rule Soundness Principle:** For each PK rule, the bottom sequent is a logical consequence of the top sequent(s)

<v-click>

**PK Soundness Theorem:** Every sequent provable in PK is valid

*Proof:* By induction on proof length
- Axioms $\alpha \rightarrow \alpha$ are valid
- Each rule preserves validity (Rule Soundness)

</v-click>

<v-click>

**PK Completeness Theorem:** Every valid propositional sequent is provable in PK (without cut or contraction!)

*Proof idea:* Induction on number of connectives, using Inversion Principle

</v-click>

---

# The Inversion Principle

**Inversion Principle:** For each PK rule (except weakening):
- If the bottom sequent is valid, then all top sequents are valid

<v-clicks>

**Example (∧-right):**
$$\frac{\Gamma \rightarrow \Delta, \alpha \quad \Gamma \rightarrow \Delta, \beta}{\Gamma \rightarrow \Delta, (\alpha \wedge \beta)}$$

If bottom is valid, both premises must be valid (otherwise $\alpha \wedge \beta$ couldn't be proven)

**Fails for weakening:** Bottom can be valid even if we just added a false formula!

</v-clicks>

---

# Extended PK (EPK)

**Abbreviations** - A practical extension:

Allow axioms of the form:
$$p \leftrightarrow \alpha$$

where:
- $p$ is a **new** variable (not used before)
- $\alpha$ is any formula

<v-click>

**Purpose:** Like "#define" in programming
- Abbreviate complex formulas
- Can nest definitions
- Makes proofs more readable

</v-click>

<v-click>

**Theorem:** Any EPK proof can be rewritten as a PK proof (but may grow exponentially!)

**Connection:** PK ↔ Boolean formulas, EPK ↔ Boolean circuits

</v-click>

---
layout: section
---

# First Order Logic

Extending to quantifiers and predicates

---

# First Order Languages

A **language** $\mathcal{L} = \{f_1, f_2, \ldots, R_1, R_2, \ldots\}$ consists of:

<v-clicks>

- **Function symbols:** $f_1, f_2, f_3, \ldots$
  - Each has an **arity** (number of arguments)
  - 0-ary function = **constant**

- **Relation symbols (predicates):** $R_1, R_2, R_3, \ldots$
  - Each has an arity

**Example:** Language of arithmetic $\mathcal{L}_A = [0, s, +, \cdot; =]$
- Constants: $0$
- Functions: $s$ (successor, arity 1), $+, \cdot$ (arity 2)
- Relation: $=$ (equality, arity 2)

</v-clicks>

---

# Terms

$\mathcal{L}$-**terms** are defined by structural induction:

<v-clicks>

**Base case:** Every variable is a term
- Variables: $x, y, z, \ldots, a, b, c, \ldots$

**Inductive case:** If $f$ is an $n$-ary function and $t_1, \ldots, t_n$ are terms:
- Then $f t_1 t_2 \cdots t_n$ is a term

**Examples** (with $f$ binary, $g$ unary, $e$ constant):
- $gex$ (apply $g$ to constant $e$ and variable $x$... wait, this doesn't parse correctly!)
- Properly: $g(e), f(g(e), x), f(x, y)$

</v-clicks>

<v-click>

**Note:** We use **infix notation** for arithmetic: $(t_1 + t_2)$ instead of $+t_1t_2$

</v-click>

---

# Arithmetic Terms

In $\mathcal{L}_A = [0, s, +, \cdot; =]$:

<v-clicks>

**Formal (prefix) notation:**
- $sss0$ means $3$ (successor of successor of successor of $0$)
- $+xy$ means $x + y$
- $\cdot(+xy)(sz)$ means $(x+y) \cdot (z+1)$

**Infix notation (what we actually use):**
- $s(s(s(0)))$ or just $sss0$ for $3$
- $(x + sy)$ instead of $+ x(sy)$
- $((x + sy) \cdot (ssz + s0))$

**Parentheses** required for infix to avoid ambiguity!

</v-clicks>

---

# First Order Formulas

$\mathcal{L}$-**formulas** are built as follows:

1. **Atomic formulas:** $R t_1 t_2 \cdots t_n$
   - $R$ is $n$-ary relation, $t_1, \ldots, t_n$ are terms
   - Example: $x = y + y$, $P(x, y)$

2. **Boolean combinations:** If $\alpha, \beta$ are formulas:
   - $\neg\alpha$, $(\alpha \vee \beta)$, $(\alpha \wedge \beta)$

3. **Quantification:** If $\alpha$ is a formula and $x$ is a variable:
   - $\forall x \alpha$ (for all $x$)
   - $\exists x \alpha$ (there exists $x$)

---

# Examples of First Order Formulas

<v-clicks>

**Simple formulas:**
- $\forall x P(x)$ - "Everything has property $P$"
- $\exists x \neg Q(x, y)$ - "There exists an $x$ such that $Q(x,y)$ is false"
- $(\neg \forall x P(x) \vee \exists x \neg P(x))$ - Tautology!

**Mixed quantifiers:**
- $\forall x \forall y \exists z (x = y + z)$ - "For all $x,y$, there exists $z$ with $x = y + z$"

**Complex formula:**
- $(\forall x \neg Q(x,y) \wedge \neg \forall z Q(f(y),z))$

</v-clicks>

---

# Bound and Free Variables

An occurrence of $x$ in $\alpha$ is:

<v-clicks>

**Bound** if it's in the **scope** of a quantifier $\forall x$ or $\exists x$

**Free** otherwise

**Examples:**
- $\exists y(x = y + y)$ - $x$ is **free**, $y$ is **bound**
- $P(x) \wedge \forall x Q(x)$ - $x$ occurs both **free** and **bound**
- $\forall x \forall y (x = y)$ - both $x$ and $y$ are **bound**

**Closed** term/formula = no free variables

**Sentence** = closed formula (no free variables)

</v-clicks>

---

# Structures and Interpretations

A **structure** $\mathcal{M}$ gives meaning to $\mathcal{L}$-formulas:

<v-clicks>

1. **Universe of discourse** $M$ - a nonempty set

2. For each $n$-ary function $f$:
   - $f^{\mathcal{M}}: M^n \rightarrow M$ (interpretation of $f$)

3. For each $n$-ary relation $P$:
   - $P^{\mathcal{M}} \subseteq M^n$ (interpretation of $P$)

**Special:** If $\mathcal{L}$ contains $=$, then $=^{\mathcal{M}}$ must be true equality

</v-clicks>

---

# Object Assignments

To evaluate formulas with free variables, we need an **object assignment**:

$$\sigma: \{\text{variables}\} \rightarrow M$$

<v-click>

**Notation:** $\sigma(m/x)$ means:
- Same as $\sigma$, except $x$ maps to $m \in M$

</v-click>

<v-click>

**Term evaluation** $t^{\mathcal{M}}[\sigma] \in M$:
1. $x^{\mathcal{M}}[\sigma] = \sigma(x)$
2. $(f t_1 \cdots t_n)^{\mathcal{M}}[\sigma] = f^{\mathcal{M}}(t_1^{\mathcal{M}}[\sigma], \ldots, t_n^{\mathcal{M}}[\sigma])$

</v-click>

---

# Tarski Semantics (BSD)

**Basic Semantic Definitions** - how formulas get truth values:

1. $\mathcal{M} \vDash (P t_1 \cdots t_n)[\sigma]$ iff $(t_1^{\mathcal{M}}[\sigma], \ldots, t_n^{\mathcal{M}}[\sigma]) \in P^{\mathcal{M}}$

2. $\mathcal{M} \vDash \neg\alpha[\sigma]$ iff $\mathcal{M} \nvDash \alpha[\sigma]$

3. $\mathcal{M} \vDash (\alpha \wedge \beta)[\sigma]$ iff $\mathcal{M} \vDash \alpha[\sigma]$ and $\mathcal{M} \vDash \beta[\sigma]$

4. $\mathcal{M} \vDash (\alpha \vee \beta)[\sigma]$ iff $\mathcal{M} \vDash \alpha[\sigma]$ or $\mathcal{M} \vDash \beta[\sigma]$

5. $\mathcal{M} \vDash \forall x \alpha[\sigma]$ iff $\mathcal{M} \vDash \alpha[\sigma(m/x)]$ for **all** $m \in M$

6. $\mathcal{M} \vDash \exists x \alpha[\sigma]$ iff $\mathcal{M} \vDash \alpha[\sigma(m/x)]$ for **some** $m \in M$

---

# Example: Order Relation

Let $\mathcal{L} = [; R, =]$ with $R$ binary

Let $\mathcal{M}$ be a structure where:
- Universe: $M = \mathbb{N}$
- $(m,n) \in R^{\mathcal{M}}$ iff $m \leq n$

<v-click>

**Evaluating formulas:**
- $\mathcal{M} \vDash \exists x \forall y R(x,y)$ - TRUE (take $x = 0$)
- $\mathcal{M} \vDash \exists y \forall x R(x,y)$ - FALSE (no maximum natural number)

</v-click>

<v-click>

**Note:** Order of quantifiers matters!
- $\exists x \forall y$ is NOT the same as $\forall y \exists x$

</v-click>

---

# Standard Structure for Arithmetic

The **standard structure** $\underline{\mathbb{N}}$ for $\mathcal{L}_A$:

<v-clicks>

- **Universe:** $M = \mathbb{N} = \{0, 1, 2, 3, \ldots\}$

- **Interpretations:**
  - $0^{\underline{\mathbb{N}}} = 0$ (the actual number zero)
  - $s^{\underline{\mathbb{N}}}(n) = n + 1$ (successor function)
  - $+^{\underline{\mathbb{N}}}, \cdot^{\underline{\mathbb{N}}}, =^{\underline{\mathbb{N}}}$ have their usual meanings

**Example:**
$$\underline{\mathbb{N}} \vDash \forall x \forall y \exists z (x = y + z \vee y = x + z)$$

"For any two numbers, one is the sum of the other plus something"

</v-clicks>

---

# Unique Readability for Terms

**Exercise:** Show the Unique Readability Theorem for terms

<v-click>

**Theorem:** Similar to propositional case
- No proper initial segment of a term is a term
- Can use weight assignments
- Parse tree is unique

</v-click>

<v-click>

**CFG for First Order Formulas:**

**Exercise:** Show that the set of $\mathcal{L}$-formulas can be given by a context-free grammar

*Hint:* Similar to propositional case, but add quantifiers as operators on formulas

</v-click>

---

# Summary: Propositional Logic

<v-clicks>

- **Formulas** built from variables and connectives $\neg, \wedge, \vee$
- **Truth assignments** give semantic meaning
- **Tautologies** are valid formulas
- **PK proof system** provides syntactic proofs
  - Sequent calculus with structural and logical rules
  - **Soundness:** Provable → Valid
  - **Completeness:** Valid → Provable (without cut!)
- **EPK** extends with abbreviations

</v-clicks>

---

# Summary: First Order Logic

<v-clicks>

- **Languages** specify function and relation symbols
- **Terms** built from variables, constants, and functions
- **Formulas** add atomic formulas and quantifiers $\forall, \exists$
- **Structures** provide interpretations (semantics)
- **Tarski semantics (BSD)** defines truth
  - Object assignments for free variables
  - Quantifiers range over universe
- **Standard model** $\underline{\mathbb{N}}$ for arithmetic

</v-clicks>

---

# Key Takeaways

<v-clicks>

1. **Syntax vs Semantics**
   - Syntax: How formulas are built (grammar, structure)
   - Semantics: What formulas mean (truth, models)

2. **Soundness and Completeness**
   - Bridge between proof (syntax) and truth (semantics)
   - "Can prove" $\iff$ "Is true"

3. **First Order Logic is Powerful**
   - Can express properties of numbers, sets, graphs, etc.
   - Foundation for mathematics and formal verification

4. **Next Steps**
   - Peano Arithmetic (PA)
   - Formal verification of algorithms
   - Gödel's incompleteness theorems

</v-clicks>

---

# Connection to Computer Science

Where does logic appear in CS?

<v-clicks>

**Formal Verification:**
- Prove program correctness
- Verify hardware designs
- Model checking

**Programming Languages:**
- Type systems are logical systems
- Curry-Howard correspondence (proofs = programs)
- Logic programming (Prolog, Datalog)

**Databases:**
- SQL queries are first-order formulas
- Relational algebra

**Artificial Intelligence:**
- Knowledge representation
- Automated theorem proving
- Planning and reasoning

</v-clicks>

---

# Next Steps

- Practice constructing PK proofs for tautologies
- Work through BSD definitions with examples
- Study Peano Arithmetic (Section 9.4.3 in the book)
- Explore formal verification applications
- Read about Gödel's incompleteness theorems

**Further Reading:** See Notes section for logic textbooks and resources

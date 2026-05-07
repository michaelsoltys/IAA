---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 10.4: Logic
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Logic - Propositional and First Order
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

# Logic

Section 10.4 — Foundations of propositional and first-order logic, building toward Peano Arithmetic.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The road map: propositional logic, then first-order logic, with $PA$ as the destination.

</div>

This section presents the foundations of logic with the aim of defining **Peano Arithmetic (PA)**


**Two main topics:**
1. **Propositional Logic** - Boolean formulas and reasoning
2. **First Order Logic** - Predicate calculus with quantifiers

**Goal:** Provide logical background for formal verification of algorithms

**Scope:** Limited to foundations needed for understanding formal systems


---
layout: section
---

# Propositional Logic

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Boolean variables and connectives — the simplest logic with non-trivial structure.

</div>

Building blocks of logical reasoning

---

# Propositional Formulas

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Variables joined by $\neg$, $\wedge$, $\vee$, $\rightarrow$, $\leftrightarrow$ — the alphabet of Boolean reasoning.

</div>

**Propositional (Boolean) formulas** are built from:


- **Propositional variables:** $p_1, p_2, p_3, \ldots$ (also called **atoms**)
  - Often use labels: $a, b, c, \ldots$ or $p, q, r, \ldots$

- **Logical connectives:**
  - $\neg$ (negation, NOT)
  - $\wedge$ (conjunction, AND)
  - $\vee$ (disjunction, OR)
  - $\rightarrow$ (implication)
  - $\leftrightarrow$ (equivalence)


---

# Definition by Structural Induction

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Build formulas inductively: start from variables, then close under the connectives.

</div>

**Base case:** Any variable $p$ is a formula

**Inductive cases:** If $\alpha, \beta$ are formulas, then:
- $\neg\alpha$ is a formula
- $(\alpha \wedge \beta)$ is a formula
- $(\alpha \vee \beta)$ is a formula


**Examples:**
- $p$
- $(p \vee q)$
- $(\neg(p \wedge q) \wedge (\neg p \vee \neg q))$


---

# Exercise: CFG for Propositional Formulas

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The same inductive definition, written as a grammar — formulas are a context-free language.

</div>

**Exercise:** Define propositional formulas with a context-free grammar <span style="font-size: 0.6em; color: navy;">Prb 10.77, Pg 305, prb:cfg</span>


**Solution sketch:**
```text
Formula → Variable
        | ¬ Formula
        | ( Formula ∧ Formula )
        | ( Formula ∨ Formula )

Variable → p | q | r | ...
```

This gives us a formal syntax for well-formed formulas!


---

# Unique Readability

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A weight-counting trick that proves every formula parses in exactly one way.

</div>

**Key property:** No proper initial segment of a formula is a formula


**Weight Assignment:**
| Symbol | Weight |
|--------|--------|
| $\neg$ | 0 |
| $\wedge, \vee, ($ | 1 |
| $), p$ (any variable) | -1 |


**Lemma:** Any formula $\alpha$ has weight $-1$, but any proper initial segment has weight $\geq 0$ <span style="font-size: 0.6em; color: navy;">Lem 10.78, Pg 305, lem:weights</span>


---

# Unique Readability Theorem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

If two formulas look the same, their main connective and subformulas must match — parse trees are unique.

</div>

**Theorem:** Suppose $\alpha, \beta, \alpha', \beta'$ are formulas and $c, c'$ are binary connectives. If:
$$(\alpha \, c \, \beta) \equiv (\alpha' \, c' \, \beta')$$
(syntactically identical)

Then: $\alpha \equiv \alpha'$ and $\beta \equiv \beta'$ and $c \equiv c'$ <span style="font-size: 0.6em; color: navy;">Thm 10.80, Pg 305, thm:urt</span>


**Meaning:**
- The grammar is unambiguous
- Only one candidate for the main connective
- The parse tree is unique
- Despite infix notation, parentheses make it unambiguous!


---

# Truth Assignments

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Pick $T$ or $F$ for each variable, and the connectives propagate truth through the whole formula.

</div>

A **truth assignment** is a map:
$$\tau: \{\text{variables}\} \longrightarrow \{T, F\}$$


Extend $\tau$ to all formulas:
1. $(\neg\alpha)^\tau = T$ iff $\alpha^\tau = F$
2. $(\alpha \wedge \beta)^\tau = T$ iff $\alpha^\tau = T$ **and** $\beta^\tau = T$
3. $(\alpha \vee \beta)^\tau = T$ iff $\alpha^\tau = T$ **or** $\beta^\tau = T$


---

# Semantic Concepts

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Satisfiable, valid, equivalent, consequence — the vocabulary for talking about meaning.

</div>


**Satisfies:** Truth assignment $\tau$ **satisfies** formula $\alpha$ if $\alpha^\tau = T$
- $\tau$ satisfies set $\Phi$ if $\tau$ satisfies all $\alpha \in \Phi$

**Satisfiable:** Set $\Phi$ is **satisfiable** if some $\tau$ satisfies it
- Otherwise, $\Phi$ is **unsatisfiable**

**Logical Consequence:** $\Phi \vDash \alpha$ means:
- Every $\tau$ that satisfies $\Phi$ also satisfies $\alpha$

**Valid:** $\vDash \alpha$ means $\alpha^\tau = T$ for all $\tau$
- Valid formulas are called **tautologies**

**Equivalent:** $\alpha \iff \beta$ means $\alpha \vDash \beta$ and $\beta \vDash \alpha$


---

# Examples

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Classical tautologies and De Morgan's law in action.

</div>

**Tautologies:**
- $p \vee \neg p$ (Law of Excluded Middle)
- $p \rightarrow p$ (Identity)
- $\neg(p \wedge \neg p)$ (Non-contradiction)


**Logical Consequence:**
- $(p \wedge q) \vDash (p \vee q)$


**Equivalence (De Morgan's Law):**
- $\neg(p \vee q) \iff (\neg p \wedge \neg q)$


---

# Important Exercises

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three classics: cut-by-consequence, Boolean duality, and Craig interpolation.

</div>

**Exercise:** Show that if $\Phi \vDash \alpha$ and $\Phi \cup \{\alpha\} \vDash \beta$, then $\Phi \vDash \beta$ <span style="font-size: 0.6em; color: navy;">Prb 10.82, Pg 306, prb:logicalconsequence</span>


**Duality Theorem:** Let $\alpha'$ be the result of:
- Interchanging $\vee$ and $\wedge$ in $\alpha$
- Replacing each $p$ by $\neg p$

Then: $\neg\alpha \iff \alpha'$ <span style="font-size: 0.6em; color: navy;">Prb 10.83, Pg 307, prb:duality</span>


**Craig Interpolation Theorem:** If $A \rightarrow B$ is valid and variables sets overlap, there exists an "interpolant" $C$ using only common variables such that both $A \rightarrow C$ and $C \rightarrow B$ are valid <span style="font-size: 0.6em; color: navy;">Prb 10.84, Pg 307, prb:craig</span>


---
layout: section
---

# The PK Proof System

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Gentzen's sequent calculus — derive valid formulas mechanically from axioms and rules.

</div>

Formal proofs in propositional logic

---

# Sequent Calculus (PK)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A sequent $\alpha_1, \ldots \rightarrow \beta_1, \ldots$ reads "if all assumptions hold, some conclusion does."

</div>

**PK** = "Propositional Kalkül" (German logician Gentzen)

**Sequent:** A line of the form
$$\alpha_1, \ldots, \alpha_k \rightarrow \beta_1, \ldots, \beta_l$$

where:
- $\alpha_1, \ldots, \alpha_k$ is the **antecedent** (assumptions)
- $\beta_1, \ldots, \beta_l$ is the **succedent** (conclusions)
- $k, l \geq 0$ (can be empty)


**Meaning:** "If all $\alpha_i$ are true, then at least one $\beta_j$ is true"

Equivalent to: $(\alpha_1 \wedge \cdots \wedge \alpha_k) \rightarrow (\beta_1 \vee \cdots \vee \beta_l)$


---

# Special Cases of Sequents

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Empty sides matter: one-sided sequents encode plain formulas, the empty sequent is contradiction.

</div>


- $\rightarrow \alpha$ means $\alpha$ (succedent only)
- $\alpha \rightarrow$ means $\neg\alpha$ (antecedent only)
- $\rightarrow$ is **false** (empty sequent is unsatisfiable)

**Valid sequents:**
- $\alpha \rightarrow \alpha$ (identity)
- $\rightarrow \alpha, \neg\alpha$ (excluded middle)
- $\alpha \wedge \neg\alpha \rightarrow$ (contradiction)


---

# PK Proof Structure

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A proof is a tree: axioms at the leaves, the goal at the root, rules in between.

</div>

A **PK proof** is a finite rooted tree where:


- **Nodes** are labeled with sequents
- **Root** (bottom) is the **endsequent** (what we're proving)
- **Leaves** (top) are **logical axioms**: $\alpha \rightarrow \alpha$
- **Interior nodes** follow from parent(s) by **inference rules**

**Direction:** Tree grows from leaves (top/axioms) down to root (bottom/goal)


---

# Weak Structural Rules

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Exchange, contraction, weakening — bookkeeping rules that don't touch logical content.

</div>

**Exchange** (reorder formulas):
$$\frac{\Gamma_1, \alpha, \beta, \Gamma_2 \rightarrow \Delta}{\Gamma_1, \beta, \alpha, \Gamma_2 \rightarrow \Delta} \quad \frac{\Gamma \rightarrow \Delta_1, \alpha, \beta, \Delta_2}{\Gamma \rightarrow \Delta_1, \beta, \alpha, \Delta_2}$$

**Contraction** (remove duplicates):
$$\frac{\Gamma, \alpha, \alpha \rightarrow \Delta}{\Gamma, \alpha \rightarrow \Delta} \quad \frac{\Gamma \rightarrow \Delta, \alpha, \alpha}{\Gamma \rightarrow \Delta, \alpha}$$

**Weakening** (add formulas):
$$\frac{\Gamma \rightarrow \Delta}{\alpha, \Gamma \rightarrow \Delta} \quad \frac{\Gamma \rightarrow \Delta}{\Gamma \rightarrow \Delta, \alpha}$$

---

# Logical Rules - Negation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

To handle $\neg\alpha$, push $\alpha$ across the arrow — negation flips sides of the sequent.

</div>

$$\frac{\Gamma \rightarrow \Delta, \alpha}{\neg\alpha, \Gamma \rightarrow \Delta} \text{(¬-left)} \quad \frac{\alpha, \Gamma \rightarrow \Delta}{\Gamma \rightarrow \Delta, \neg\alpha} \text{(¬-right)}$$


**Intuition:**
- To prove $\neg\alpha$ on right, prove $\alpha$ on left
- If $\neg\alpha$ is an assumption (left), then $\alpha$ must be a conclusion (right)


---

# Logical Rules - Conjunction

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Proving $\alpha \wedge \beta$ on the right requires *two* premises — one for each conjunct.

</div>

$$\frac{\alpha, \beta, \Gamma \rightarrow \Delta}{(\alpha \wedge \beta), \Gamma \rightarrow \Delta} \text{(∧-left)}$$

$$\frac{\Gamma \rightarrow \Delta, \alpha \quad \Gamma \rightarrow \Delta, \beta}{\Gamma \rightarrow \Delta, (\alpha \wedge \beta)} \text{(∧-right)}$$


**Intuition:**
- Left: If we assume $\alpha \wedge \beta$, we can use both $\alpha$ and $\beta$
- Right: To prove $\alpha \wedge \beta$, must prove both $\alpha$ and $\beta$ (two premises!)


---

# Logical Rules - Disjunction

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Mirror image of $\wedge$: assuming $\alpha \vee \beta$ on the left forces a case split.

</div>

$$\frac{\alpha, \Gamma \rightarrow \Delta \quad \beta, \Gamma \rightarrow \Delta}{(\alpha \vee \beta), \Gamma \rightarrow \Delta} \text{(∨-left)}$$

$$\frac{\Gamma \rightarrow \Delta, \alpha, \beta}{\Gamma \rightarrow \Delta, (\alpha \vee \beta)} \text{(∨-right)}$$


**Intuition:**
- Left: If we assume $\alpha \vee \beta$, must handle both cases (two premises!)
- Right: To prove $\alpha \vee \beta$, proving either $\alpha$ or $\beta$ suffices


---

# Cut Rule

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Use a lemma $\alpha$ then discharge it — convenient, but theoretically dispensable.

</div>

The powerful (and controversial) **cut rule**:

$$\frac{\Gamma \rightarrow \Delta, \alpha \quad \alpha, \Gamma \rightarrow \Delta}{\Gamma \rightarrow \Delta}$$


**Meaning:**
- First premise: We can prove $\alpha$ (or something else in $\Delta$)
- Second premise: Assuming $\alpha$ leads to conclusion
- Conclusion: We can reach the conclusion without mentioning $\alpha$

**The Cut Formula** $\alpha$ is called the "lemma" being used

**Remarkable fact:** Cut is admissible but not necessary (Cut Elimination Theorem)


---

# Soundness and Completeness

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

PK proves *exactly* the valid sequents — syntax and semantics agree.

</div>

**Rule Soundness Principle:** For each PK rule, the bottom sequent is a logical consequence of the top sequent(s) <span style="font-size: 0.6em; color: navy;">Prb 10.88, Pg 309, exr:rsp</span>


**PK Soundness Theorem:** Every sequent provable in PK is valid

*Proof:* By induction on proof length
- Axioms $\alpha \rightarrow \alpha$ are valid
- Each rule preserves validity (Rule Soundness)


**PK Completeness Theorem:** Every valid propositional sequent is provable in PK (without cut or contraction!) <span style="font-size: 0.6em; color: navy;">Prb 10.92, Pg 310, exr:pk-completeness1</span>

*Proof idea:* Induction on number of connectives, using Inversion Principle


---

# The Inversion Principle

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The rules can be read backward — validity below forces validity above (almost everywhere).

</div>

**Inversion Principle:** For each PK rule (except weakening):
- If the bottom sequent is valid, then all top sequents are valid


**Example (∧-right):**
$$\frac{\Gamma \rightarrow \Delta, \alpha \quad \Gamma \rightarrow \Delta, \beta}{\Gamma \rightarrow \Delta, (\alpha \wedge \beta)}$$

If bottom is valid, both premises must be valid (otherwise $\alpha \wedge \beta$ couldn't be proven)

**Fails for weakening:** Bottom can be valid even if we just added a false formula!


---

# Extended PK (EPK)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Add named abbreviations $p \leftrightarrow \alpha$ — the same expressive jump as formulas to circuits.

</div>

**Abbreviations** - A practical extension:

Allow axioms of the form:
$$p \leftrightarrow \alpha$$

where:
- $p$ is a **new** variable (not used before)
- $\alpha$ is any formula


**Purpose:** Like "#define" in programming
- Abbreviate complex formulas
- Can nest definitions
- Makes proofs more readable


**Theorem:** Any EPK proof can be rewritten as a PK proof (but may grow exponentially!)

**Connection:** PK ↔ Boolean formulas, EPK ↔ Boolean circuits


---
layout: section
---

# First Order Logic

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Add $\forall$ and $\exists$ over a domain — now we can talk about *objects*, not just truth values.

</div>

Extending to quantifiers and predicates

---

# First Order Languages

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Pick the function and relation symbols you want — e.g., $\mathcal{L}_A = [0, s, +, \cdot; =]$ for arithmetic.

</div>

A **language** $\mathcal{L} = \{f_1, f_2, \ldots, R_1, R_2, \ldots\}$ consists of:


- **Function symbols:** $f_1, f_2, f_3, \ldots$
  - Each has an **arity** (number of arguments)
  - 0-ary function = **constant**

- **Relation symbols (predicates):** $R_1, R_2, R_3, \ldots$
  - Each has an arity

**Example:** Language of arithmetic $\mathcal{L}_A = [0, s, +, \cdot; =]$
- Constants: $0$
- Functions: $s$ (successor, arity 1), $+, \cdot$ (arity 2)
- Relation: $=$ (equality, arity 2)


---

# Terms

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Variables and constants closed under function application — terms denote *objects* in the universe.

</div>

$\mathcal{L}$-**terms** are defined by structural induction:


**Base case:** Every variable is a term
- Variables: $x, y, z, \ldots, a, b, c, \ldots$

**Inductive case:** If $f$ is an $n$-ary function and $t_1, \ldots, t_n$ are terms:
- Then $f t_1 t_2 \cdots t_n$ is a term

**Examples** (with $f$ binary, $g$ unary, $e$ constant):
- $gex$ (apply $g$ to constant $e$ and variable $x$... wait, this doesn't parse correctly!)
- Properly: $g(e), f(g(e), x), f(x, y)$


**Note:** We use **infix notation** for arithmetic: $(t_1 + t_2)$ instead of $+t_1t_2$


---

# Arithmetic Terms

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Prefix vs. infix: the same term, written formally or the way humans actually read it.

</div>

In $\mathcal{L}_A = [0, s, +, \cdot; =]$:


**Formal (prefix) notation:**
- $sss0$ means $3$ (successor of successor of successor of $0$)
- $+xy$ means $x + y$
- $\cdot(+xy)(sz)$ means $(x+y) \cdot (z+1)$

**Infix notation (what we actually use):**
- $s(s(s(0)))$ or just $sss0$ for $3$
- $(x + sy)$ instead of $+ x(sy)$
- $((x + sy) \cdot (ssz + s0))$

**Parentheses** required for infix to avoid ambiguity!


---

# First Order Formulas

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Atomic formulas $R t_1 \cdots t_n$, then Boolean combinations, then quantification over variables.

</div>

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

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A few small formulas to develop a feel for what quantifiers say in plain English.

</div>


**Simple formulas:**
- $\forall x P(x)$ - "Everything has property $P$"
- $\exists x \neg Q(x, y)$ - "There exists an $x$ such that $Q(x,y)$ is false"
- $(\neg \forall x P(x) \vee \exists x \neg P(x))$ - Tautology!

**Mixed quantifiers:**
- $\forall x \forall y \exists z (x = y + z)$ - "For all $x,y$, there exists $z$ with $x = y + z$"

**Complex formula:**
- $(\forall x \neg Q(x,y) \wedge \neg \forall z Q(f(y),z))$


---

# Bound and Free Variables

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A variable bound by a quantifier is local; a free variable is a parameter from outside.

</div>

An occurrence of $x$ in $\alpha$ is:


**Bound** if it's in the **scope** of a quantifier $\forall x$ or $\exists x$

**Free** otherwise

**Examples:**
- $\exists y(x = y + y)$ - $x$ is **free**, $y$ is **bound**
- $P(x) \wedge \forall x Q(x)$ - $x$ occurs both **free** and **bound**
- $\forall x \forall y (x = y)$ - both $x$ and $y$ are **bound**

**Closed** term/formula = no free variables

**Sentence** = closed formula (no free variables)


---

# Structures and Interpretations

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Pick a universe and an interpretation for every symbol — a model is where formulas live.

</div>

A **structure** $\mathcal{M}$ gives meaning to $\mathcal{L}$-formulas:


1. **Universe of discourse** $M$ - a nonempty set

2. For each $n$-ary function $f$:
   - $f^{\mathcal{M}}: M^n \rightarrow M$ (interpretation of $f$)

3. For each $n$-ary relation $P$:
   - $P^{\mathcal{M}} \subseteq M^n$ (interpretation of $P$)

**Special:** If $\mathcal{L}$ contains $=$, then $=^{\mathcal{M}}$ must be true equality


---

# Object Assignments

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A map $\sigma$ from variables to elements of the universe — it's how free variables get values.

</div>

To evaluate formulas with free variables, we need an **object assignment**:

$$\sigma: \{\text{variables}\} \rightarrow M$$


**Notation:** $\sigma(m/x)$ means:
- Same as $\sigma$, except $x$ maps to $m \in M$


**Term evaluation** $t^{\mathcal{M}}[\sigma] \in M$:
1. $x^{\mathcal{M}}[\sigma] = \sigma(x)$
2. $(f t_1 \cdots t_n)^{\mathcal{M}}[\sigma] = f^{\mathcal{M}}(t_1^{\mathcal{M}}[\sigma], \ldots, t_n^{\mathcal{M}}[\sigma])$


---

# Tarski Semantics (BSD)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The recursive definition of $\mathcal{M} \vDash \alpha[\sigma]$ — Tarski's clean answer to "what does truth mean?"

</div>

**Basic Semantic Definitions** - how formulas get truth values:

1. $\mathcal{M} \vDash (P t_1 \cdots t_n)[\sigma]$ iff $(t_1^{\mathcal{M}}[\sigma], \ldots, t_n^{\mathcal{M}}[\sigma]) \in P^{\mathcal{M}}$

2. $\mathcal{M} \vDash \neg\alpha[\sigma]$ iff $\mathcal{M} \nvDash \alpha[\sigma]$

3. $\mathcal{M} \vDash (\alpha \wedge \beta)[\sigma]$ iff $\mathcal{M} \vDash \alpha[\sigma]$ and $\mathcal{M} \vDash \beta[\sigma]$

4. $\mathcal{M} \vDash (\alpha \vee \beta)[\sigma]$ iff $\mathcal{M} \vDash \alpha[\sigma]$ or $\mathcal{M} \vDash \beta[\sigma]$

5. $\mathcal{M} \vDash \forall x \alpha[\sigma]$ iff $\mathcal{M} \vDash \alpha[\sigma(m/x)]$ for **all** $m \in M$

6. $\mathcal{M} \vDash \exists x \alpha[\sigma]$ iff $\mathcal{M} \vDash \alpha[\sigma(m/x)]$ for **some** $m \in M$

---

# Example: Order Relation

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$\exists x \forall y$ vs. $\forall y \exists x$ — the order of quantifiers changes the meaning entirely.

</div>

Let $\mathcal{L} = [; R, =]$ with $R$ binary

Let $\mathcal{M}$ be a structure where:
- Universe: $M = \mathbb{N}$
- $(m,n) \in R^{\mathcal{M}}$ iff $m \leq n$


**Evaluating formulas:**
- $\mathcal{M} \vDash \exists x \forall y R(x,y)$ - TRUE (take $x = 0$)
- $\mathcal{M} \vDash \exists y \forall x R(x,y)$ - FALSE (no maximum natural number)


**Note:** Order of quantifiers matters!
- $\exists x \forall y$ is NOT the same as $\forall y \exists x$


---

# Standard Structure for Arithmetic

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Interpret $\mathcal{L}_A$ over $\mathbb{N}$ in the obvious way — this is the model arithmetic is *about*.

</div>

The **standard structure** $\underline{\mathbb{N}}$ for $\mathcal{L}_A$:


- **Universe:** $M = \mathbb{N} = \{0, 1, 2, 3, \ldots\}$

- **Interpretations:**
  - $0^{\underline{\mathbb{N}}} = 0$ (the actual number zero)
  - $s^{\underline{\mathbb{N}}}(n) = n + 1$ (successor function)
  - $+^{\underline{\mathbb{N}}}, \cdot^{\underline{\mathbb{N}}}, =^{\underline{\mathbb{N}}}$ have their usual meanings

**Example:**
$$\underline{\mathbb{N}} \vDash \forall x \forall y \exists z (x = y + z \vee y = x + z)$$

"For any two numbers, one is the sum of the other plus something"


---

# Unique Readability for Terms

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The same weight argument carries over to terms — and to first-order formulas.

</div>

**Exercise:** Show the Unique Readability Theorem for terms <span style="font-size: 0.6em; color: navy;">Prb 10.96, Pg 311, exr:urt-terms</span>


**Theorem:** Similar to propositional case
- No proper initial segment of a term is a term
- Can use weight assignments
- Parse tree is unique


**CFG for First Order Formulas:**

**Exercise:** Show that the set of $\mathcal{L}$-formulas can be given by a context-free grammar

*Hint:* Similar to propositional case, but add quantifiers as operators on formulas


---

# Summary: Propositional Logic

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Recap: syntax, semantics, the PK proof system, and the EPK extension.

</div>


- **Formulas** built from variables and connectives $\neg, \wedge, \vee$
- **Truth assignments** give semantic meaning
- **Tautologies** are valid formulas
- **PK proof system** provides syntactic proofs
  - Sequent calculus with structural and logical rules
  - **Soundness:** Provable → Valid
  - **Completeness:** Valid → Provable (without cut!)
- **EPK** extends with abbreviations


---

# Summary: First Order Logic

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Recap: languages, terms, formulas, structures, and Tarski semantics.

</div>


- **Languages** specify function and relation symbols
- **Terms** built from variables, constants, and functions
- **Formulas** add atomic formulas and quantifiers $\forall, \exists$
- **Structures** provide interpretations (semantics)
- **Tarski semantics (BSD)** defines truth
  - Object assignments for free variables
  - Quantifiers range over universe
- **Standard model** $\underline{\mathbb{N}}$ for arithmetic


---

# Key Takeaways

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The big themes: syntax meets semantics, and first-order logic is genuinely powerful.

</div>


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


---

# Connection to Computer Science

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Verification, type systems, databases, AI — logic is everywhere computer science hides.

</div>

Where does logic appear in CS?


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

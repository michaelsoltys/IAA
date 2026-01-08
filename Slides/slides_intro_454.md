---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## COMP 454: Automata, Languages and Computation
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: COMP 454 - Automata, Languages and Computation
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

# COMP 454

Automata, Languages and Computation

---

# Instructor

**Michael Soltys**

<v-clicks>

- Email: michael.soltys@csuci.edu
- Office: Shasta Hall 2611
- Office Hours: Thursdays 11:30–2:30 or by appointment
- Lecture: Wednesdays 7:00–8:00

</v-clicks>

---

# Prerequisites

<v-clicks>

- **MATH 300** (Discrete Math)
- **Python** programming language
- We will implement automata and parsers in Python

</v-clicks>

---

# Textbook

<div class="flex gap-8 mt-8 justify-center">
<div class="text-center">
<img src="./Figures/IAA-ed3.jpg" class="h-60" />
<p>3rd Edition</p>
</div>
<div class="text-center">
<img src="./Figures/IAA-ed4.png" class="h-60" />
<p>4th Edition</p>
</div>
</div>

<v-click>

**We use Chapter 9** (PDF provided by instructor)

**Code Repository:** https://github.com/michaelsoltys/IAA-Code

</v-click>

---

# What is This Course About?

The relation between **languages** (sets of strings) and **machines** that process them

<v-clicks>

- What can be computed?
- What are the limits of computation?
- How do we describe sets of strings formally?

</v-clicks>

---

# Course Overview

Three major topics:

<v-clicks>

1. **Regular Languages** — Finite Automata and Regular Expressions
2. **Context-Free Languages** — Grammars and Pushdown Automata
3. **Computability** — Turing Machines and the Church-Turing Thesis

</v-clicks>

---

# Course Outline

<div class="grid grid-cols-2 gap-8">
<div>

<v-clicks>

**1. Regular Languages**
- DFAs and NFAs (equivalence)
- Regular Expressions
- Pumping Lemma
- Applications to text search

**2. Context-Free Languages**
- Context-Free Grammars (CFGs)
- Pushdown Automata (PDAs)
- Pumping Lemma for CFLs

</v-clicks>

</div>
<div>

<v-clicks>

**3. Turing Machines**
- Church-Turing Thesis
- Decidability and undecidability

</v-clicks>

</div>
</div>

---

# Grading

<v-clicks>

- **Quizzes:** 8 quizzes × 5% = 40%
- **Assignments:** 4 assignments × 5% = 20%
- **Midterms:** 2 midterms × 10% = 20%
- **Final Exam:** 20% (cumulative)

</v-clicks>

---

# Student Learning Outcomes (SLOs)

Upon successful completion you will be able to:

<v-clicks>

1. **Describe** sets of strings with different computational models
2. **Understand** the computational power of different models
3. **Understand** the limits of computability

</v-clicks>

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

# COMP 454

COMP 454 — What can be computed, and what *can't* — a tour from finite automata to Turing machines.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Instructor

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Where to find me, when to find me, and how to reach me.

</div>

**Michael Soltys**


- Email: michael.soltys@csuci.edu
- Office: Shasta Hall 2611
- Office Hours: Thursdays 11:30–2:30 or by appointment
- Lecture: Wednesdays 7:00–8:00


---

# Prerequisites

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

You'll need discrete math reflexes and enough Python to implement a parser.

</div>


- **MATH 300** (Discrete Math)
- **Python** programming language
- We will implement automata and parsers in Python


---

# Textbook

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

We'll work primarily out of Chapter 9 of *An Introduction to the Analysis of Algorithms*.

</div>

<div class="flex gap-8 mt-8 justify-center">
<div class="text-center">
<img src="./Figures/IAA-ed3.jpg" class="h-60" />
<p>3rd Edition</p>
</div>
<div class="text-center">
<img src="./Figures/IAA-ed4.jpg" class="h-60" />
<p>4th Edition</p>
</div>
</div>


**We use Chapter 9** (PDF provided by instructor)

**Code Repository:** https://github.com/michaelsoltys/IAA


---

# What is This Course About?

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The deep correspondence between *what* you can describe and *how* a machine recognizes it.

</div>

The relation between **languages** (sets of strings) and **machines** that process them


- What can be computed?
- What are the limits of computation?
- How do we describe sets of strings formally?


---

# Course Overview

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

We climb the Chomsky hierarchy: regular, context-free, and finally the full Turing-computable languages.

</div>

Three major topics:


1. **Regular Languages** — Finite Automata and Regular Expressions
2. **Context-Free Languages** — Grammars and Pushdown Automata
3. **Computability** — Turing Machines and the Church-Turing Thesis


---

# Course Outline

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A topic-by-topic roadmap of the semester — the order matters; each layer subsumes the previous.

</div>

<div class="grid grid-cols-2 gap-8">
<div>


**1. Regular Languages**
- DFAs and NFAs (equivalence)
- Regular Expressions
- Pumping Lemma
- Applications to text search

**2. Context-Free Languages**
- Context-Free Grammars (CFGs)
- Pushdown Automata (PDAs)
- Pumping Lemma for CFLs


</div>
<div>


**3. Turing Machines**
- Church-Turing Thesis
- Decidability and undecidability


</div>
</div>

---

# Resources

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Where the slides, code, recordings, and assignments live — bookmark all of these.

</div>


- **Canvas:** https://cilearn.csuci.edu/courses/33936
  - Complete modules with all course material

- **GitHub:** https://github.com/michaelsoltys/IAA
  - Slides, Solutions, Summaries
  - Implementations of Algorithms

- **GitHub Classroom:** https://classroom.github.com/
  - Assignment URL provided in Canvas
  - Work directly in Codespaces

- **YouTube:** https://www.youtube.com/playlist?list=PLZV4fOisnXZ4OmDurTxZAq9WA4Vv7NIHR
  - Prerecorded lectures


---

# Grading

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

How your grade is built — frequent low-stakes work, plus two midterms and a cumulative final.

</div>


- **Quizzes:** 8 quizzes × 5% = 40%
- **Assignments:** 4 assignments × 5% = 20%
- **Midterms:** 2 midterms × 10% = 20%
- **Final Exam:** 20% (cumulative)


---

# Student Learning Outcomes (SLOs)

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

What you'll walk out of the course knowing — and being able to *do*.

</div>

Upon successful completion you will be able to:


1. **Describe** sets of strings with different computational models
2. **Understand** the computational power of different models
3. **Understand** the limits of computability

---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Sections 9.1-9.2: Alphabets, Strings and Languages
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: Alphabets, Strings and Languages
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

# Alphabets, Strings and Languages

Sections 9.1-9.2 — The vocabulary for the rest of the course: what a computation is *about* before we ask what can compute it.

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# Where This Chapter Is Going

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Programs instantiate algorithms. Hardware instantiates a *model of computation*.

</div>

The first serious attempt at a computer was Charles Babbage's **Difference Engine**, begun in the 1820s: decimal, and powered by cranking a handle. He never finished one — machining parts to the required precision was beyond the era.

**The chapter's arc:**

$$\text{finite automata} \;\longrightarrow\; \text{pushdown automata} \;\longrightarrow\; \text{Turing machines}$$

Each is a machine model, and each answers a different version of the same question: **what can be computed, and with what resources?**

Before any of that we need to say precisely what a machine is computing *about*. That is this lecture.

<!--
Babbage is worth a minute because the failure was manufacturing, not conception. The design was sound; the London toolmakers of the 1820s could not hold the tolerances. A Difference Engine No. 2 was finally built to his drawings by the Science Museum in London in 1991, using only techniques available in his lifetime, and it worked. The idea was right and the supply chain was not.

The plan for this chapter is a ladder of machines, each strictly more powerful than the last, and each characterised by the class of languages it recognises. The point of today's definitions is that "language" is the common currency in which all three models can be compared.
-->

---

# Marks Before Machines

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.6em;">

Storing information in discrete symbols is older than writing, and far older than arithmetic.

</div>

<div class="grid grid-cols-3 gap-4 items-start" style="font-size: 0.72em;">
<div class="text-center">
<div style="display: inline-block; text-align: left;">
<img src="/Figures/ocher.jpg" class="h-32 object-contain" style="display: block;" />
<div style="margin-top: 0.35em;"><strong>Engraved ocher</strong><br>Blombos Cave, South Africa<br>77,000–75,000 yrs</div>
</div>
</div>
<div class="text-center">
<div style="display: inline-block; text-align: left;">
<img src="/Figures/ishango.jpg" class="h-24 object-contain" style="display: block;" />
<div style="margin-top: 0.35em;"><strong>Ishango bone</strong><br>Congo, baboon leg, 3 rows of tallies<br>25,000–20,000 yrs</div>
</div>
</div>
<div class="text-center">
<div style="display: inline-block; text-align: left;">
<img src="/Figures/antler.jpg" class="h-24 object-contain" style="display: block;" />
<div style="margin-top: 0.35em;"><strong>Reindeer antler</strong><br>La Madeleine, France<br>17,000–11,500 yrs</div>
</div>
</div>
</div>

These are *marks*, not writing. A tally records quantity. It does not yet compose.

<!--
Photographs from the Smithsonian Museum of Natural History in Washington DC; the objects themselves are not all Smithsonian-held. The Blombos material is at Iziko Museums in Cape Town and the Ishango bone is in Brussels.

The Ishango bone is the contested one. Found in 1950 by the Belgian geologist Jean de Heinzelin near Lake Edward in what is now the DRC, it carries three columns of notches. One column reads 11, 13, 17, 19 — every prime between 10 and 20. Another shows 3 and 6, 4 and 8, 10 and 5 — doublings and halvings. Readings range from a plain tally, to a lunar calendar, to genuine arithmetic, and the argument has run for seventy years without resolution. A fragment of quartz is still set in one end, so the object may have been the handle of an engraving tool: a writing implement that also recorded numbers. Raise it precisely because it is unsettled; students assume the deep past is either "primitive" or "solved," and it is neither.

Blombos Cave has kept producing. Beyond the cross-hatched ocher plaque there are shell beads, a 100,000-year-old ochre-processing workshop, and in 2018 a stone flake bearing a deliberate cross-hatch drawn in ochre crayon about 73,000 years ago, currently the oldest known drawing. La Madeleine, the source of the reindeer antler, is the type site that gives the Magdalenian culture its name.
-->

---

# From Marks to Writing

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.6em;">

About 8,000 years ago the marks started standing for words. Then for sounds.

</div>

<div class="grid grid-cols-2 gap-6 items-start" style="font-size: 0.78em;">
<div class="text-center">
<div style="display: inline-block; text-align: left;">
<img src="/Figures/cylinder.jpg" class="h-40 object-contain" style="display: block;" />
<div style="margin-top: 0.35em;"><strong>Cylinder seal</strong> rolled across wet clay.<br>Lapis lazuli, Babylon, 4,100–3,600 yrs.<br>Hard to carve, hard to forge: a signature.</div>
</div>
</div>
<div class="text-center">
<div style="display: inline-block; text-align: left;">
<img src="/Figures/cuneiform.jpg" class="h-40 object-contain" style="display: block;" />
<div style="margin-top: 0.35em;"><strong>Cuneiform tablet</strong>, near Babylon,<br>4,000–2,600 yrs. Marks stood first for<br>concepts, later for <em>sounds and syllables</em>.</div>
</div>
</div>
</div>

**That shift is the one that matters here.** Once a mark denotes a sound rather than a thing, you have a finite alphabet that can express unboundedly many messages. Everything in this chapter rests on it.

<!--
Denise Schmandt-Besserat traced cuneiform back to small clay tokens used for accounting: tokens sealed inside clay envelopes, then impressed on the outside so the envelope could be read without breaking it, then eventually just the impressions. Writing appears to have been invented by accountants, and the earliest large corpora are receipts rather than literature. Cuneiform then ran for roughly three thousand years and was adapted to at least fifteen languages, which is a strong argument that a symbol set is a technology independent of any one language.

The cylinder seal is the detail that lands best in a computing course. Rolling a carved cylinder across wet clay produces a continuous impression that is laborious to carve and hard to forge, and it authenticates a document by a mark only the holder can make. That is a signature scheme, four thousand years early.

The move from logographic to phonetic writing is the conceptual leap this whole course depends on: a finite symbol set, composed into arbitrarily long strings, carrying meaning by convention.
-->

---

# Alphabet, String, Length

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three definitions, and everything else in the chapter is built from them.

</div>

<span style="font-size: 0.6em; color: navy;">Sec 9.2, Pg 218, sec:alphs-strings</span>

An **alphabet** $\Sigma$ is a **finite, non-empty** set of distinct symbols.

$$\Sigma = \{0,1\} \quad\text{(binary)} \qquad \Sigma = \{a,b,c,\ldots,z\}$$

We write $\Sigma_\ell$ for a generic alphabet of size $\ell$, so $\Sigma_2 = \{0,1\}$.

A **string** (or **word**) is a *finite ordered* sequence of symbols from $\Sigma$.

$$w = 010011101011 \qquad |w| = 12$$

$|w|$ denotes the **length**. The **empty string** $\varepsilon$ is the unique string with $|\varepsilon| = 0$, and it belongs to every alphabet's strings by default.

**Read the fine print:** the alphabet is *finite*, and every string is *finite*. Both restrictions are load-bearing — drop either and the machines in this chapter stop making sense.

---

# Building Sets of Strings

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

$\Sigma^k$, then $\Sigma^*$: from strings of one length to all strings at once.

</div>

<div class="grid grid-cols-2 gap-6">
<div>

$\Sigma^k$ is the set of strings of length **exactly** $k$. For $\Sigma = \{0,1\}$:

$$\Sigma^0 = \{\varepsilon\}$$
$$\Sigma^1 = \Sigma$$
$$\Sigma^2 = \{00, 01, 10, 11\}$$

**How big is $\Sigma^k$?** $\;|\Sigma|^k$.

Note $\Sigma^0 = \{\varepsilon\}$, not $\emptyset$ — there is exactly one string of length zero.

</div>
<div>

**Kleene's star** $\Sigma^*$ is the set of *all* strings over $\Sigma$:

$$\Sigma^* = \Sigma^0 \cup \underbrace{\Sigma^1 \cup \Sigma^2 \cup \Sigma^3 \cup \cdots}_{\textstyle =\;\Sigma^+}$$

$\Sigma^+$ is the same thing without $\varepsilon$.

**Concatenation** is juxtaposition. For $x = a_1\ldots a_m$ and $y = b_1\ldots b_n$:

$$x \cdot y = xy = a_1\ldots a_m b_1 \ldots b_n$$

and $w\varepsilon = \varepsilon w = w$.

</div>
</div>

**$\Sigma^*$ is infinite, but every string in it is finite.** No string has infinite length.

<!--
Stephen Cole Kleene (1909-1994), a student of Alonzo Church at Princeton, gave his name to the star, to Kleene's recursion theorem, and to the Kleene closure. He also introduced regular expressions in 1951, in a RAND report on nerve nets and finite automata — which is where §9.3 picks up.

His name is pronounced "KLAY-nee," a point he made often enough that his son reportedly said the only correct pronunciations were that one and "Kle-nay," and that "KLEEN" was simply wrong.
-->

---

# Languages

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

A language is just a set of strings. That simplicity is the point.

</div>

A **language** $L$ over $\Sigma$ is any collection of strings: $\;L \subseteq \Sigma^*$.

$$L = \{\varepsilon, 01, 0011, 000111, \ldots\} = \{0^n 1^n \mid n \ge 0\}$$

<span style="font-size: 0.6em; color: navy;">Eq 9.1, Pg 218, eq:example</span>

| | |
|---|---|
| $\{\varepsilon\}$ | the language containing exactly one string, the empty one |
| $\emptyset$ | the empty language, containing **no** strings |

$|\{\varepsilon\}| = 1$ and $|\emptyset| = 0$. They are as different as a bag holding one blank sheet and a bag holding nothing.

**Why "language"?** Because a decision problem *is* a language: the set of inputs whose answer is yes. Asking "is this number prime?" is asking "is this string in $L_{\text{prime}}$?"

---

# The Two Questions

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Everything from here to the end of the course is one of these.

</div>

**1. How do we *describe* a language?**

The set-builder notation above is informal prose. We need finite, mechanical descriptions — that is what regular expressions and grammars are for.

**2. Given $L \subseteq \Sigma^*$ and a string $x$, how do we *check* whether $x \in L$?**

$$L = \{\underbrace{10}_{2}, \underbrace{11}_{3}, \underbrace{101}_{5}, \underbrace{111}_{7}, \ldots\} \subseteq \{0,1\}^*$$

that is, $w \in L$ exactly when $w$ is the binary encoding of a prime.

A finite description of an infinite set, and a procedure to test membership. **And that raises the question the rest of the chapter exists to answer: what *is* an algorithm?**

---

# Summary

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.5em;">

Small vocabulary, large consequences.

</div>

<div class="grid grid-cols-2 gap-8" style="text-align: left; font-size: 0.88em;">
<div>

| | |
|---|---|
| **Alphabet** $\Sigma$ | finite, non-empty |
| **String** $w$ | finite sequence; $\lvert w\rvert$ its length |
| $\varepsilon$ | the unique string of length 0 |
| $\Sigma^k$ | length exactly $k$; size $\lvert\Sigma\rvert^k$ |
| $\Sigma^*,\ \Sigma^+$ | all strings; all non-empty |
| **Language** $L$ | any subset of $\Sigma^*$ |

</div>
<div>

**Carry forward**

1. A **decision problem is a language.**
2. **Finite descriptions of infinite sets** — regular expressions, grammars, machines.
3. $\{\varepsilon\} \neq \emptyset$, and $\Sigma^*$ is infinite while every member is finite.

**Problem 9.1:** $|\Sigma_2^k|$? $|\Sigma_\ell^k|$? If $L$ is the strings over $\Sigma_\ell$ with no repeated symbol, what is $|L|$?

<span style="font-size: 0.7em; color: navy;">Prb 9.1, Pg 218, exr:word-count</span>

</div>
</div>

---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Section 1.2.1: PageRank
  An Introduction to the Analysis of Algorithms (4th Edition)
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: PageRank
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

# PageRank

Section 1.2.1 — How do you rank a trillion web pages when nobody has read any of them?

<div style="position: absolute; bottom: 20px; right: 30px; font-size: 0.55em; color: navy;">All references are to the 4th edition of <em>An Introduction to the Analysis of Algorithms</em> (World Scientific, 2025)</div>

---

# The Problem

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Billions of pages match "jaguar." Which three go at the top?

</div>

Search is really two problems, and only one of them is hard:

1. **Find** the pages matching the query — a text-matching problem, largely solved
2. **Rank** them so the best is first — this is the whole game

A ranking is only useful if a human who reads the top few results stops looking. Those top pages are called **authoritative**.

**The catch:** no algorithm has read these pages. It cannot judge whether an article on jaguars is any good.

So how do you rank what you cannot understand?

<!--
This is worth dwelling on for a minute before revealing the trick, because students assume search engines somehow "understand" the pages. In 1998 nothing did. The insight that made Google is that you can rank documents without comprehending a single word of them.

Ask the class how they would do it. Common answers: count keyword occurrences (this is what AltaVista and Lycos did, and it is trivially gamed — invisible white-on-white text repeating "jaguar" a thousand times), or count visits (you have no way to measure that from outside), or hire editors (Yahoo's original directory did exactly this, and it did not scale past a few hundred thousand sites).
-->

---

# The Idea: Links Are Votes

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The web is not just pages. It is pages *plus links*, and the links are the data nobody was using.

</div>

When an author writes a hyperlink, they make an **implicit endorsement**: this page is worth reading.

The link structure is a directed graph, and it carries an enormous amount of *latent human annotation*. Millions of authors already did the judging; nobody had collected the votes.

**The analogy:** academic citations. An important paper is one cited by other important papers.

That last sentence is circular. Making it non-circular is the algorithm.

<!--
Vannevar Bush foresaw this in 1945, in an Atlantic Monthly article called "As We May Think," written while he was directing the US wartime scientific effort. He observed that every information system we build is linear (books, indexes, card catalogues) while human memory is associative: one thought reminds you of another. He proposed a machine he called the Memex that would store human knowledge connected by associative trails. That is the web, described 45 years before Tim Berners-Lee implemented it.

Brin and Page were PhD students at Stanford when they wrote the PageRank paper in 1998. The company is now worth over a trillion dollars. The algorithm on the next slide is the entire original idea.
-->

---

# The Formula

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Every page gives its rank away, split evenly among the pages it links to.

</div>

For a page $X$, let $T_1, \ldots, T_n$ be the pages linking **to** $X$, and let $C(T)$ be the number of links leaving $T$:

$$\text{PR}(X) = (1-d) + d\left[\frac{\text{PR}(T_1)}{C(T_1)} + \frac{\text{PR}(T_2)}{C(T_2)} + \cdots + \frac{\text{PR}(T_n)}{C(T_n)}\right]$$

<span style="font-size: 0.6em; color: navy;">Eq 1.4, Pg 12, eq:pagerank</span>

<div class="grid grid-cols-2 gap-4 items-center">
<div>

Two things to read off it:

- **A vote is divided.** A page linking to 100 others gives each $1/100$ of its rank. Endorsing everything endorses nothing.
- **A vote is weighted.** A link from a highly ranked page is worth more.

</div>
<div>

<img src="/Figures/pagerank.svg" class="mx-auto h-40" />

</div>
</div>

<!--
The name is a double pun: it ranks web pages, and it was written by Larry Page. The system's first name was worse. In 1996 the Stanford prototype was called BackRub, because it analysed the web's back links; it ran on borrowed hardware in a dorm room and crawled about 24 million pages. The name Google arrived in 1997, from googol, the number 10^100, and by most accounts the spelling was simply a mistake nobody bothered to fix.

The formula has a compact linear-algebra reading. Write the link structure as a matrix, add the damping term, and PageRank is the principal eigenvector of that matrix. The iteration on the next slide is the power method for finding it, which is why it converges so reliably. Brin and Page describe it this way in "The Anatomy of a Large-Scale Hypertextual Web Search Engine" (1998), still one of the most readable papers in the field.
-->

---

# The Random Surfer

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The damping factor $d$ is not a fudge. It is a person who gets bored.

</div>

Picture someone who lands on a random page and clicks links forever, never pressing Back. **PageRank of $X$ = the fraction of time this surfer spends on $X$.**

The damping factor $d$ (usually $\mathbf{0.85}$) splits their behaviour:

| With probability | They | Term |
|---|---|---|
| $d = 0.85$ | follow a link from the current page | $d\sum \text{PR}(T_i)/C(T_i)$ |
| $1 - d = 0.15$ | get bored and jump to a random page | $(1-d)$ |

Roughly: they follow about **six links** before jumping.

**Why the jump matters:** without it, a surfer entering a group of pages that only link to each other would be trapped forever, and those pages would hoard all the rank. The 15% escape hatch is what keeps the ranking honest.

<!--
Normalisation: the book divides $(1-d)$ by $N$, the size of the web, so the chance of stumbling onto any particular page scales with how big the web is.

The deeper story is that PageRank is the stationary distribution of a Markov chain on the web graph, and the damping factor is what guarantees the chain is irreducible and aperiodic, so a unique stationary distribution exists and the iteration converges to it. Students who go on to a probability course will meet this again as the Perron-Frobenius theorem. No need to say any of that here; the bored surfer is the honest intuition, and the mathematics only confirms it.
-->

---

# It Looks Circular

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

To rank $X$ you need the ranks of everything pointing at $X$. Where does the first rank come from?

</div>

**It does not matter.** Start anywhere and iterate:

```text
PageRank:
  Pre-condition: web graph of N pages, damping factor d
  for every page P:
      PR(P) ← 1/N                     # egalitarian start
  repeat:
      for every page P:
          PR'(P) ← (1-d)/N + d · Σ PR(T)/C(T)   over T linking to P
      PR ← PR'
  until the values stop changing
  Post-condition: PR is the stationary rank of every page
```

<span style="font-size: 0.6em; color: navy;">Prb 1.18, Pg 13, exr:pagerank-program</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Problems/P1.18_PageRank.py" style="font-size: 0.6em; color: teal;">[Python solution]</a>

Each pass gets closer to the true value, and in practice it **converges quickly** — a few dozen passes for the whole web.

<!--
Convergence is fast because each iteration shrinks the error by roughly the damping factor, so about 50 passes suffice even for billions of pages. The order of updates barely matters, which is what makes the computation parallelisable across thousands of machines.

Jon Kleinberg published a rival idea at almost exactly the same moment: HITS, which scores each page twice, once as a "hub" that points to good pages and once as an "authority" that good pages point to. It is arguably the more nuanced model, and it lost, partly because it must be recomputed per query while PageRank is computed once for the whole web. Kleinberg went on to win the Nevanlinna Prize. There is a lesson in there about the algorithm that is cheap to run beating the algorithm that is elegant.
-->

---

# Worked Example: Setting Up

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Six pages, $d = 1$ — no random jumps, so every bit of rank flows along a link.

</div>

<div class="grid grid-cols-2 gap-6">
<div>

<img src="/Figures/pagerank-network.svg" class="mx-auto h-48" />

<span style="font-size: 0.6em; color: navy;">Fig 1.2, Pg 14, fig:pagerank2</span>

</div>
<div>

**Read off the out-degrees** — how many ways each page splits its rank:

| page | links to | $C$ |
|---|---|---|
| A | B | 1 |
| **B** | C, D, E, F | **4** |
| C | F | 1 |
| D | E | 1 |
| E | C | 1 |
| F | A | 1 |

B is the only page that divides.

</div>
</div>

---

# Worked Example: The Equations

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Turn the picture around: for each page, who points *at* it?

</div>

With $d=1$ the formula is just $\text{PR}(X) = \sum \text{PR}(T)/C(T)$ over pages $T$ linking to $X$:

<div class="grid grid-cols-2 gap-8">
<div>

$$\text{PR}(A) = \text{PR}(F)$$
$$\text{PR}(B) = \text{PR}(A)$$
$$\text{PR}(C) = \tfrac{\text{PR}(B)}{4} + \text{PR}(E)$$

</div>
<div>

$$\text{PR}(D) = \tfrac{\text{PR}(B)}{4}$$
$$\text{PR}(E) = \tfrac{\text{PR}(B)}{4} + \text{PR}(D)$$
$$\text{PR}(F) = \tfrac{\text{PR}(B)}{4} + \text{PR}(C)$$

</div>
</div>

Six equations, six unknowns — but each is defined in terms of the others. **So iterate.** Everyone starts equal at $1/6$.

<!--
Point out that this is a linear system and could be solved directly by Gaussian elimination. For six pages that is entirely reasonable. For a trillion pages it is not: elimination is cubic in the number of pages, while one iteration costs only one pass over the links. That is the real reason PageRank iterates rather than solves.
-->

---

# Worked Example: First Three Rounds

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Apply all six equations at once, using the *previous* round's values throughout.

</div>

| $k$ | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| **0** | .1667 | .1667 | .1667 | .1667 | .1667 | .1667 |
| **1** | .1667 | .1667 | **.2083** | **.0417** | **.2083** | **.2083** |
| **2** | **.2083** | .1667 | **.2500** | .0417 | **.0833** | **.2500** |
| **3** | **.2500** | **.2083** | **.1250** | .0417 | .0833 | **.2917** |

**Round 1, page D:** $\text{PR}(D) = \text{PR}(B)/4 = (1/6)/4 = 1/24 = .0417$. D is fed only by B, and B splits four ways, so D immediately drops to a quarter of everyone else.

**Round 1, page C:** $\text{PR}(C) = \text{PR}(B)/4 + \text{PR}(E) = 1/24 + 1/6 = 5/24 = .2083$. Two inbound links, so C gains.

Notice **A and B lag**: A cannot move until F does, and B cannot move until A does. Rank has to travel.

---

# Worked Example: Converging

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Values oscillate, the swings shrink, and it settles.

</div>

| $k$ | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 3 | .2500 | .2083 | .1250 | .0417 | .0833 | .2917 |
| 4 | .2917 | .2500 | .1354 | .0521 | .0938 | .1771 |
| 6 | .1979 | .1771 | .1875 | .0729 | .1354 | .2292 |
| 8 | .2318 | .2292 | .1667 | .0495 | .0938 | .2292 |
| 10 | .2240 | .2292 | .1647 | .0579 | .1152 | .2090 |
| 12 | .2220 | .2090 | .1712 | .0560 | .1133 | .2285 |
| **$\infty$** | **.2222** | **.2222** | **.1667** | **.0556** | **.1111** | **.2222** |

**The column sums stay exactly 1 at every single round.** With $d=1$ rank is never created or destroyed, only moved. If your columns stop summing to 1, you have dropped or double-counted a link — this is the check to run first.

The wobble is real: the graph has cycles of length 4 (A→B→C→F→A) and 6, so rank sloshes around before settling.

---

# Worked Example: The Answer

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

The exact fixed point, in the fractions Problem 1.17 asks for.

</div>

<div class="grid grid-cols-2 gap-6">
<div>

| page | PR | |
|---|---|---|
| **A** | $2/9$ | .2222 |
| **B** | $2/9$ | .2222 |
| **F** | $2/9$ | .2222 |
| C | $1/6$ | .1667 |
| E | $1/9$ | .1111 |
| D | $1/18$ | .0556 |

Sum $= 1$. **A, B, F tie for first; D is last with a quarter of their rank.**

</div>
<div>

**Check it by substitution** — a fixed point must reproduce itself:

$$\text{PR}(C) = \tfrac{2/9}{4} + \tfrac{1}{9} = \tfrac{1}{18} + \tfrac{2}{18} = \tfrac{1}{6}\ \checkmark$$

$$\text{PR}(F) = \tfrac{2/9}{4} + \tfrac{1}{6} = \tfrac{1}{18} + \tfrac{3}{18} = \tfrac{2}{9}\ \checkmark$$

**Why D loses.** It has exactly one inbound link, from B, and B divides its rank four ways. One weak endorsement.

**Why A ties for first** despite one inbound link: its single voter is F, and F is itself well fed. *Whose* vote you get matters more than how many.

</div>
</div>

<span style="font-size: 0.6em; color: navy;">Prb 1.17, Pg 13, exr:pagerank</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Problems/P1.18_PageRank.py" style="font-size: 0.6em; color: teal;">[Python solution]</a>

<!--
Every number on these slides was produced by running the iteration in exact rational arithmetic, then verified by substituting the limit back into all six equations. Worth saying to the class, because the point of the fixed-point check is exactly that you never have to trust the table.

The convergence here is slower than the "a few dozen passes for the whole web" claim earlier, and the reason is instructive: d=1 was chosen to make the hand calculation clean, but it also removes the random jump that damps the oscillation. With the usual d=0.85 the wobble dies out much faster. Setting d=1 makes the arithmetic easy and the convergence hard.

Problem 1.18 asks for the same computation as a program keeping exact fractions a/b with gcd(a,b)=1, and asks whether the algorithm always terminates — a good question to leave hanging here.
-->

# Why This Was Hard to Game

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Earlier engines ranked by what a page said about itself. PageRank ranks by what *others* say about it.

</div>

| Ranking signal | Who controls it | Gameable? |
|---|---|---|
| Keyword count on the page | the page's author | trivially |
| Meta tags | the page's author | trivially |
| **Inbound links, weighted by rank** | **everyone else** | expensively |

To fake authority you now need genuinely authoritative pages to link to you. You cannot simply declare yourself important.

**This is the whole reason Google won.** Not a better index; a signal the spammers did not own.

<!--
It did not stay ungameable. Link farms, paid links, and comment spam followed within a few years, and an entire SEO industry grew up around manufacturing inbound links. Google's response was the rel="nofollow" attribute in 2005, letting a site link without passing rank, plus a long series of ranking updates.

There is a nice irony worth mentioning: search engines now shape the web they measure. Because they direct traffic, they influence which pages get linked, which changes the ranking. Physicists call this the observer effect; you cannot measure your tire pressure without letting out some air.

For about fifteen years Google published a rounded 0 to 10 PageRank score in its toolbar. The scale was logarithmic, so climbing from 6 to 7 was far harder than 5 to 6. It became a currency: sites sold links priced by their toolbar score, which is precisely the behaviour the score was meant to detect. Google stopped updating it in 2013 and removed it in 2016.
-->

---

# What PageRank Is Not

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

One number, computed once, for the whole web — and it knows nothing about your query.

</div>

- **It is query-independent.** A page's rank is the same whether you searched for "jaguar the cat" or "jaguar the car." Matching to the query is a separate step.
- **It is one signal among hundreds.** Modern search weighs freshness, location, language, document type, site reputation, and much else.
- **It does not read the page.** It cannot tell truth from falsehood, only endorsement from obscurity.

**Still:** an elegant idea, expressible in one line, that ranked the entire web using nothing but its shape.

<!--
Worth telling students who assume good ideas sell themselves: in 1999 Page and Brin tried to sell the whole thing. The asking price was around one million dollars and the buyer they approached, Excite, turned it down; other portals passed as well. The usual account is that search was seen as a commodity feature, and portals wanted visitors to stay on the site rather than leave quickly with a good answer, which is exactly what a better search engine does.

The patent belonged to Stanford, not to Google, since the work was done there. Stanford licensed it in exchange for shares, sold them in 2005, and received roughly 336 million dollars. It remains one of the most profitable pieces of university technology transfer on record.
-->

---

# Summary

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

Three ideas worth carrying out of this lecture.

</div>

1. **Structure carries information.** The link graph encoded human judgment that nobody had thought to read.

2. **Circular definitions can be computed.** When a definition refers to itself, guess, iterate, and let it converge. You will meet this again in dynamic programming and in Markov chains.

3. **The best signal is the one your adversary does not control.** A design principle far beyond search.

**Key problems**

1. **Problem 1.17:** compute PageRank by hand for the six-node network, $d=1$ <span style="font-size: 0.6em; color: navy;">Prb 1.17, Pg 13, exr:pagerank</span>

2. **Problem 1.18:** implement PageRank over a 0-1 link matrix, keeping exact fractions <span style="font-size: 0.6em; color: navy;">Prb 1.18, Pg 13, exr:pagerank-program</span> <a href="https://github.com/michaelsoltys/IAA/blob/main/Problems/P1.18_PageRank.py" style="font-size: 0.6em; color: teal;">[Python solution]</a>

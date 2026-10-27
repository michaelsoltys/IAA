---
theme: default
layout: default
highlighter: shiki
lineNumbers: true
info: |
  ## COMP 490: AWS Cloud Architecting
  Winter Session 2027 pitch for COMP 354 and COMP 454 students
  Michael Soltys
drawings:
  persist: false
transition: slide-left
title: "COMP 490: AWS Cloud Architecting"
mdc: false
---

<div style="font-size: 0.7em; letter-spacing: 0.22em; text-transform: uppercase; color: #6b7280; margin-bottom: 0.6em;">Winter Session 2027 &nbsp;·&nbsp; COMP 490 &nbsp;·&nbsp; Class #2197</div>

# AWS Cloud Architecting

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.8em;">

An advanced course on building infrastructure in the cloud, taking performance, security, scalability, and cost into account.

</div>

<div style="display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 2.2rem; align-items: center;">
<div>

<div style="font-size: 2.05em; line-height: 1.12; font-weight: 700; letter-spacing: -0.02em;">
You analyzed the algorithm.<br>
<span style="font-weight: 300;">Now architect the system it runs on.</span>
</div>

<div style="border-top: 2px solid black; margin-top: 1.4em; padding-top: 0.7em; font-size: 0.8em; line-height: 1.75;">
<b>Dec 14, 2026 to Jan 15, 2027</b><br>
Online, asynchronous &nbsp;·&nbsp; 3 units &nbsp;·&nbsp; Section E1<br>
Prerequisite: upper-division standing<br>
Instructor: Michael Soltys
</div>

</div>
<div>

<img src="./Figures/aws-pitch-diagram.png" style="max-height: 340px; width: 100%; object-fit: contain;" alt="Black-and-white sketch of a highly available architecture: users, load balancer, an Auto Scaling group across two availability zones, a primary database with a read replica, a cache, and a queue feeding workers" />

</div>
</div>

---

# What You Build

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 1.1em;">

Real infrastructure, built by hand in real AWS lab environments.

</div>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); border-top: 2px solid black; border-bottom: 1px solid #d1d5db;">
<div style="padding: 0.6em 0;"><div style="font-size: 3.8em; font-weight: 800; line-height: 1;">17</div><div style="font-size: 0.68em; letter-spacing: 0.14em; text-transform: uppercase; color: #6b7280; margin-top: 0.4em;">modules</div></div>
<div style="padding: 0.6em 0;"><div style="font-size: 3.8em; font-weight: 800; line-height: 1;">12<span style="font-weight: 300;">+1</span></div><div style="font-size: 0.68em; letter-spacing: 0.14em; text-transform: uppercase; color: #6b7280; margin-top: 0.4em;">guided, +1 optional</div></div>
<div style="padding: 0.6em 0;"><div style="font-size: 3.8em; font-weight: 800; line-height: 1;">7</div><div style="font-size: 0.68em; letter-spacing: 0.14em; text-transform: uppercase; color: #6b7280; margin-top: 0.4em;">challenge labs</div></div>
<div style="padding: 0.6em 0;"><div style="font-size: 3.8em; font-weight: 800; line-height: 1;">1</div><div style="font-size: 0.68em; letter-spacing: 0.14em; text-transform: uppercase; color: #6b7280; margin-top: 0.4em;">capstone</div></div>
</div>

<div style="margin-top: 1.2em; font-size: 0.72em; letter-spacing: 0.14em; text-transform: uppercase; color: #6b7280;">The challenge labs: one cafe, growing up</div>

<div style="display: flex; align-items: center; gap: 0.45em; margin-top: 0.5em; font-size: 0.82em; font-weight: 600; flex-wrap: nowrap;">
<span style="border: 1.5px solid black; padding: 0.3em 0.55em;">static site</span><span>→</span>
<span style="border: 1.5px solid black; padding: 0.3em 0.55em;">dynamic site</span><span>→</span>
<span style="border: 1.5px solid black; padding: 0.3em 0.55em;">managed DB</span><span>→</span>
<span style="border: 1.5px solid black; padding: 0.3em 0.55em;">private network</span><span>→</span>
<span style="border: 1.5px solid black; padding: 0.3em 0.55em;">scalable, HA</span><span>→</span>
<span style="border: 1.5px solid black; padding: 0.3em 0.55em;">automated</span><span>→</span>
<span style="background: black; color: white; padding: 0.3em 0.55em; border: 1.5px solid black;">serverless</span>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; margin-top: 1.8em; font-size: 1em; line-height: 1.5;">
<div style="border-left: 3px solid black; padding-left: 0.9em;">
<div style="font-size: 1.5em; font-weight: 800; line-height: 1.1;">Capstone</div>
Design and deploy a highly available architecture, then document it in an architecture write-up.
</div>
<div style="border-left: 3px solid black; padding-left: 0.9em;">
<div style="font-size: 1.5em; font-weight: 800; line-height: 1.1;">$0</div>
Free AWS lab environments through AWS Academy. No cost, no credit card, no surprise bill.
</div>
</div>

---

# You Already Know This

<div style="color: #9ca3af; font-style: italic; font-size: 0.9em; margin-bottom: 0.9em;">

Cloud architecture is the algorithms you know from 354 and 454, running at scale.

</div>

<div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 2.4rem; align-items: start;">
<div style="font-size: 0.86em;">

| In 354 / 454 | In the cloud |
|:--|:--|
| **Hashing** | caches, CDNs, spreading keys over servers |
| **Queues** | decoupling producers from consumers |
| **Graphs** | VPC routing, peering vs. a transit hub |
| **Complexity** | scaling out, and what it costs |
| **Finite automata** | workflows as state machines |

<div style="margin-top: 1.1em; font-size: 0.95em; line-height: 1.6;">

**Why this winter:** cloud architecture skills are in demand; the course prepares you for the AWS Certified Solutions Architect Associate exam (it does not confer it); and you finish a full 3-unit course over the break.

</div>

</div>
<div>

<div style="border: 2.5px solid black; padding: 1.1em 1.3em; text-align: left;">
<div style="font-size: 0.7em; letter-spacing: 0.2em; text-transform: uppercase; color: #6b7280;">Enroll</div>
<div style="font-size: 3.3em; font-weight: 800; line-height: 1.05; letter-spacing: -0.03em;">#2197</div>
<div style="font-size: 0.85em; margin-top: 0.4em; line-height: 1.55;">
COMP 490, Section E1<br>
Winter Session 2027<br>
Register in myCI through<br>CSUCI Extended University
</div>
<div style="border-top: 1px solid black; margin-top: 0.8em; padding-top: 0.6em; font-size: 0.62em;">
<a href="https://ext.csuci.edu/programs/winter-intersession/" style="color: black;">ext.csuci.edu/programs/winter-intersession</a>
</div>
</div>

</div>
</div>

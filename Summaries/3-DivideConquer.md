# Divide and Conquer Algorithms Summary (Chapter 3)

## Introduction

**Divide et impera** - "divide and conquer" - is a Roman military strategy that consisted of securing command by breaking a large concentration of power into portions that alone were weaker, and methodically dispatching those portions one by one. This is the fundamental idea behind divide and conquer algorithms.

**Core Strategy:**
1. **Divide**: Take a large problem and divide it into smaller parts
2. **Conquer**: Solve those parts recursively
3. **Combine**: Combine the solutions into a solution to the whole

**Key Characteristic**: Useful for problems where there already exists a tolerable exhaustive search algorithm, but the divide and conquer approach improves the running time (or space usage).

## Section 3.1: Mergesort

### The Merge Operation

**Problem**: Combine two already-sorted lists into one sorted list
- Input: Lists a₁ ≤ a₂ ≤ ... ≤ aₙ and b₁ ≤ b₂ ≤ ... ≤ bₘ
- Output: Combined list c₁ ≤ c₂ ≤ ... ≤ c_{n+m}

**Algorithm 16 - Merge two lists:**
- Maintain two pointers p₁ and p₂ for lists a and b
- Compare a_{p₁} with b_{p₂}
- Choose smaller element, add to result, advance corresponding pointer
- **Complexity**: O(n+m) - linear in total size

**Important Note**: Algorithm as stated has boundary issues when one list exhausted before the other (Exercise 3.1)

### Mergesort Algorithm

**Algorithm 17 - Mergesort:**
1. Base case: If |L| ≤ 1, return L (already sorted)
2. Divide: Split L into L₁ (first ⌈n/2⌉ elements) and L₂ (last ⌊n/2⌋ elements)
3. Conquer: Recursively sort L₁ and L₂
4. Combine: Merge the two sorted lists

**Correctness**: Proved by induction on list size

### Complexity Analysis

**Recurrence relation:**
```
T(n) ≤ T(⌈n/2⌉) + T(⌊n/2⌋) + cn
```
- Floors and ceilings don't affect asymptotic bounds
- Simplifies to: T(n) ≤ 2T(n/2) + cn

**Result**: T(n) = O(n log n)

## Section 3.2: Multiplying Numbers in Binary

### Standard Binary Multiplication

**Junior school algorithm** (Figure 3.1 example: 1110 × 1101):
- For each bit in y (right to left):
  - If 0: write row of zeros
  - If 1: copy x, shifted left
- Add all rows with carry operation
- **Complexity**: O(n²) for two n-bit integers

### Karatsuba Algorithm

**Goal**: Improve from O(n²) to O(n^{log 3}) ≈ O(n^{1.59})

**Basic Idea**: Split n-bit integers into two n/2-bit parts:
```
x = x₁·2^{n/2} + x₀
y = y₁·2^{n/2} + y₀
```

**Naive approach**:
```
xy = x₁y₁·2ⁿ + (x₁y₀ + x₀y₁)·2^{n/2} + x₀y₀
```
- Requires 4 multiplications: x₁y₁, x₁y₀, x₀y₁, x₀y₀
- Recurrence: T(n) ≤ 4T(n/2) + cn
- Result: T(n) = O(n²) - no improvement!

**Karatsuba's Insight**: Only need 3 multiplications!
```
x₁y₀ + x₀y₁ = (x₁+x₀)(y₁+y₀) - (x₁y₁ + x₀y₀)
```

**Algorithm 18 - Karatsuba:**
1. Base case: If n=1, return x·y (simple bit multiplication)
2. Split x and y into high/low parts (x₁,x₀) and (y₁,y₀)
3. Compute three products recursively:
   - z₁ = Karatsuba(x₁, y₁)
   - z₂ = Karatsuba(x₁+x₀, y₁+y₀)
   - z₃ = Karatsuba(x₀, y₀)
4. Return: z₁·2^{2⌈n/2⌉} + (z₂-(z₁+z₃))·2^{⌈n/2⌉} + z₃

**Cost Comparison** (Figure 3.2):
```
                    | Multiplications | Additions | Shifts
--------------------|-----------------|-----------|-------
Naive (4 products)  |       4         |     3     |   2
Karatsuba (3 prod)  |       3         |     4     |   2
```

**Complexity**:
- Recurrence: T(n) ≤ 3T(n/2) + dn
- **Result**: T(n) = O(n^{log 3}) ≈ O(n^{1.59})

**Key Tradeoff**: One fewer multiplication costs one additional addition, but multiplications are more expensive - the trade is worth it!

## Section 3.3: Savitch's Algorithm

### Problem: Graph Reachability

**Goal**: Determine if there's a path from node s to node t in directed graph G

**Twist**: Minimize **space** (memory) usage instead of time
- Input: n×n adjacency matrix (n² bits)
- Question: Can we use O(log² n) work memory?

### Why Care About Small Space?

**Implicit graphs**: Graph doesn't need to be stored entirely in memory
- Example: World Wide Web
  - V = all web pages
  - E = hyperlinks between pages
  - Query pages/links piecemeal without full WWW in memory

### The Algorithm

**Key Predicate**: R(G,u,v,i) = true iff there exists path from u to v of length ≤ 2^i

**Fundamental Insight**: Any path has a midpoint w!
```
R(G,u,v,i) ⟺ (∃w)[R(G,u,w,i-1) ∧ R(G,w,v,i-1)]
```

**Algorithm 19 - Savitch:**
```
Input: Graph G, nodes u,v, parameter i
Base case (i=0):
  - If u=v, return true
  - If (u,v) is an edge, return true
  - Otherwise, return false

Recursive case (i>0):
  - For every vertex w:
    - If R(G,u,w,i-1) AND R(G,w,v,i-1):
      - Return true
  - Return false
```

### Complexity Analysis

**Space**: O(log² n)
- Recursion depth: i ≤ log n
- Each recursive call uses s bits (to store node)
- Total: i·s = O(log² n) bits

**Time**: Exponential (Exercise 3.11)
- Trade extreme space savings for high time cost
- Demonstrates that divide and conquer can optimize different resources

## Section 3.4: Further Examples and Problems

### Extended Euclid's Algorithm (Recursive)

**Algorithm 20 - Extended Euclid's (recursive):**
- Revisits iterative version from Chapter 1 (Algorithm 8)
- Uses multiple return values: (d,x,y) where mx + ny = d = gcd(m,n)
- Base case: If b=0, return (a,1,0)
- Recursive case:
  - (d,x,y) ← ExtendedEuclid(b, rem(a,b))
  - Return (d, y, x - div(a,b)·y)

**Similarity**: Interesting connection to Gaussian lattice reduction (Algorithm 34)

### Quicksort

**Algorithm** (not numbered in book):
1. Pick pivot element x from list I
2. Partition into S (≤ x) and L (> x)
3. Recursively sort S and L to get S' and L'
4. Result: S', x, L'

**Haskell Implementation** (elegant functional style):
```haskell
qsort [] = []
qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
  where
    smaller = [a | a <- xs, a <= x]
    larger = [b | b <- xs, b > x]
```

**Complexity**:
- Best/Average case: O(n log n)
- Worst case: O(n²) when pivot choices are poor
- Can be mitigated with randomized pivot selection

## Master Method for Solving Recurrences

The chapter relies on the **Master Method** for analyzing divide and conquer algorithms:

### General Form
```
T(n) = aT(n/b) + f(n)
```
Where:
- a = number of recursive subproblems
- n/b = size of each subproblem
- f(n) = cost of divide and combine steps

### Three Cases

**Case 1**: If f(n) = O(n^c) where c < log_b(a)
- T(n) = Θ(n^{log_b a})

**Case 2**: If f(n) = Θ(n^c log^k n) where c = log_b(a)
- T(n) = Θ(n^c log^{k+1} n)

**Case 3**: If f(n) = Ω(n^c) where c > log_b(a)
- T(n) = Θ(f(n))

### Applications in This Chapter

**Mergesort**: T(n) = 2T(n/2) + cn
- a=2, b=2, f(n)=cn
- log₂(2) = 1, c=1 (Case 2)
- **Result**: Θ(n log n)

**Naive binary multiplication**: T(n) = 4T(n/2) + cn
- a=4, b=2, f(n)=cn
- log₂(4) = 2 > 1 (Case 1)
- **Result**: Θ(n²)

**Karatsuba**: T(n) = 3T(n/2) + dn
- a=3, b=2, f(n)=dn
- log₂(3) ≈ 1.585 > 1 (Case 1)
- **Result**: Θ(n^{log₂ 3}) ≈ Θ(n^{1.585})

## Key Concepts and Takeaways

### Algorithm Design Paradigm
1. **Identify recursive structure** in the problem
2. **Break problem into smaller instances** of same type
3. **Solve base cases** directly
4. **Combine subproblem solutions** efficiently

### Correctness Proofs
- Use **induction** on problem size
- Verify base cases work correctly
- Show recursive step preserves correctness

### Complexity Analysis
- **Set up recurrence relation** from algorithm structure
- **Solve using Master Method** (or other techniques)
- **Account for all operations**: divide, conquer, combine

### Space-Time Tradeoffs
- Most divide and conquer optimizes **time**
- Savitch shows can optimize **space** instead
- Different resources can be prioritized

## Important Exercises

### Correctness Proofs
- **Exercise 3.2**: Fix boundary condition in merge algorithm
- **Exercise 3.4**: Prove mergesort correctness
- **Exercise 3.8**: Prove Karatsuba correctness
- **Exercise 3.10**: Prove Savitch correctness and space bound
- **Exercise 3.12**: Prove recursive Extended Euclid correctness

### Complexity Analysis
- **Exercise 3.11**: Determine time complexity of Savitch's algorithm
- Master Method applications to various recurrences

### Implementation
- **Exercise 3.5**: Implement mergesort for lexicographic ordering
- **Exercise 3.9**: Implement Karatsuba multiplication
- **Exercise 3.10**: Implement Savitch with stack visualization
- **Exercise 3.13**: Implement recursive Extended Euclid

## Summary

Divide and conquer is a fundamental algorithmic paradigm that achieves efficiency through recursion. The chapter presents three main algorithms:

1. **Mergesort**: Classic example achieving O(n log n) sorting
2. **Karatsuba multiplication**: Clever reduction from 4 to 3 recursive calls, improving from O(n²) to O(n^{1.59})
3. **Savitch's algorithm**: Unconventional use of divide and conquer to minimize space rather than time

The unifying theme is **recursive problem decomposition**, with the Master Method providing a systematic approach to complexity analysis. Understanding when and how to apply divide and conquer is essential for algorithm design across all areas of computer science.

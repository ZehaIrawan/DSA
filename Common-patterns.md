
If you master these, you can solve like 70–80% of common questions.

### 1. HashMap / Frequency Counting

Two Sum, Anagrams, Duplicates, Subarray sum patterns.

**Key idea:** store counts / last seen index.

---

### 2. Two Pointers

Sorted arrays, removing duplicates, sliding window-ish problems.

**Key idea:** left/right converge or move based on condition.

---

### 3. Sliding Window

Longest substring, max sum subarray, minimum window.

**Key idea:** expand right, shrink left when invalid.

---

### 4. Stack (Monotonic Stack especially)

Next greater element, daily temperatures, histogram, valid parentheses.

**Key idea:** maintain increasing/decreasing stack.

---

### 5. Binary Search (and “binary search on answer”)

Rotated array, first/last occurrence, min in rotated, capacity problems.

**Key idea:** if function is monotonic → binary search works.

---

### 6. BFS / DFS (Graph + Tree traversal)

Tree depth, islands, shortest path in grid.

**Key idea:** DFS = explore, BFS = shortest path.

---

### 7. Dynamic Programming (basic forms)

Climbing stairs, house robber, knapsack-ish.

**Key idea:** “state + transition + base case”.

Most DP problems are just:

* 1D DP
* 2D grid DP

---

### 8. Greedy

Intervals, scheduling, jump game.

**Key idea:** make locally optimal choice that stays valid.

---

### 9. Heap / Priority Queue

Top K, merge K lists, stream median.

**Key idea:** maintain best candidates efficiently.

---

### 10. Prefix Sum

Range sum queries, subarray sums.

**Key idea:** precompute cumulative sums to answer fast.

---

## If you only memorize ONE checklist:

When you see a problem, ask:

* “Need max/min length substring?” → **sliding window**
* “Need next greater / previous smaller?” → **monotonic stack**
* “Need top K / smallest K?” → **heap**
* “Sorted array?” → **two pointers / binary search**
* “Count / frequency / duplicates?” → **hashmap**
* “Shortest path?” → **BFS**
* “All possibilities?” → **DFS/backtracking**
* “Optimal with overlap?” → **DP**
* “Intervals?” → **sort + greedy**
* “Range sums?” → **prefix sum**


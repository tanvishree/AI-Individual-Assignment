# Missionaries and Cannibals — Uninformed Search

**AI Programming Assignment 3**

## Problem Statement

Three missionaries and three cannibals need to cross a river using a boat that carries at most 2 people.
At no point can cannibals outnumber missionaries on either bank, or the missionaries will be eaten.

**Goal:** Move everyone from the left bank to the right bank.

## State Representation

Each state is a tuple: `(missionaries_left, cannibals_left, boat_side)`

| Field | Description |
|---|---|
| `missionaries_left` | Number of missionaries on the left bank (0–3) |
| `cannibals_left` | Number of cannibals on the left bank (0–3) |
| `boat_side` | `0` = boat on left bank, `1` = boat on right bank |

- **Start State:** `(3, 3, 0)` — everyone on the left
- **Goal State:** `(0, 0, 1)` — everyone on the right

## Algorithms Implemented

### 1. BFS — Breadth-First Search
Explores all states level by level using a **FIFO queue**.
Guarantees the shortest (optimal) solution.

### 2. DFS — Depth-First Search
Explores as deep as possible before backtracking using a **LIFO stack**.
Memory efficient but does not guarantee the shortest path.

### 3. IDDFS — Iterative Deepening DFS
Runs depth-limited DFS repeatedly with increasing depth limits (0, 1, 2, ...).
Combines BFS optimality with DFS memory efficiency.

---

## How to Run

```bash
python missionaries_cannibals.py
```

No external libraries required — uses only Python's built-in `collections` and `time`.

---

## Sample Output

```
==================================================
  BFS
==================================================
  Steps: 11  |  Nodes: 15  |  Time: 0.0348ms

  Step-by-step:
   0. Left[3M 3C] <boat> ~~~~        Right[0M 0C]
   1. Left[3M 1C]        ~~~~ <boat> Right[0M 2C]
  ...
  11. Left[0M 0C]        ~~~~ <boat> Right[3M 3C]

==================================================
  Algorithm    Steps   Nodes    Time(ms)
  ----------------------------------------
  BFS             11      15      0.0348
  DFS             11      12      0.0278
  IDDFS           11      66      0.2565
==================================================
```

---

## Performance Comparison

| Algorithm | Steps | Nodes Explored | Optimal? | Memory |
|---|---|---|---|---|
| BFS | 11 | 15 | ✅ Yes | Higher |
| DFS | 11 | 12 | ❌ Not guaranteed | Lower |
| IDDFS | 11 | 66 | ✅ Yes | Lower |

---

## Files

| File | Description |
|---|---|
| `missionaries_cannibals.py` | Main implementation (BFS, DFS, IDDFS) |
| `README.md` | This file |

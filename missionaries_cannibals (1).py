from collections import deque
import time

# Problem Setup
# State: (missionaries_left, cannibals_left, boat_side)
# boat_side: 0 = left bank, 1 = right bank
# Goal: move everyone from left (3,3,0) to right (0,0,1)

START = (3, 3, 0)
GOAL  = (0, 0, 1)

MOVES = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # possible boat loads

def is_valid(state):
    m, c, _ = state
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    if m > 0 and c > m:               # cannibals outnumber on left
        return False
    if (3-m) > 0 and (3-c) > (3-m):  # cannibals outnumber on right
        return False
    return True

def get_successors(state):
    m, c, boat = state
    result = []
    for dm, dc in MOVES:
        if boat == 0:
            new = (m - dm, c - dc, 1)
        else:
            new = (m + dm, c + dc, 0)
        if is_valid(new):
            result.append(new)
    return result

#BFS 

def bfs():
    queue = deque()
    queue.append((START, [START]))
    visited = {START}
    nodes = 0

    while queue:
        state, path = queue.popleft()
        nodes += 1
        if state == GOAL:
            return path, nodes
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None, nodes

# DFS
def dfs():
    stack = [(START, [START], {START})]
    nodes = 0

    while stack:
        state, path, visited = stack.pop()
        nodes += 1
        if state == GOAL:
            return path, nodes
        for next_state in get_successors(state):
            if next_state not in visited:
                stack.append((next_state, path + [next_state], visited | {next_state}))
    return None, nodes

#IDDFS 
def dls(state, path, visited, limit):
    if state == GOAL:
        return path
    if limit == 0:
        return None
    for next_state in get_successors(state):
        if next_state not in visited:
            result = dls(next_state, path + [next_state], visited | {next_state}, limit - 1)
            if result:
                return result
    return None

def iddfs():
    nodes = 0
    for depth in range(30):
        nodes += depth
        result = dls(START, [START], {START}, depth)
        if result:
            return result, nodes
    return None, nodes

#Print Solution

def print_solution(name, path, nodes, elapsed):
    print(f"\n{'='*50}")
    print(f"  {name}")
    print(f"{'='*50}")
    print(f"  Steps: {len(path)-1}  |  Nodes: {nodes}  |  Time: {elapsed:.4f}ms")
    print(f"\n  Step-by-step:")
    for i, (m, c, b) in enumerate(path):
        boat  = "<boat>" if b == 0 else "      "
        boat2 = "      " if b == 0 else "<boat>"
        print(f"  {i:2}. Left[{m}M {c}C] {boat} ~~~~ {boat2} Right[{3-m}M {3-c}C]")

# Run All 
print("Missionaries and Cannibals — Uninformed Search")

results = []
for name, func in [("BFS", bfs), ("DFS", dfs), ("IDDFS", iddfs)]:
    t = time.perf_counter()
    path, nodes = func()
    elapsed = (time.perf_counter() - t) * 1000
    results.append((name, path, nodes, elapsed))
    print_solution(name, path, nodes, elapsed)

print(f"\n{'='*50}")
print(f"  {'Algorithm':<10} {'Steps':>6} {'Nodes':>8} {'Time(ms)':>12}")
print(f"  {'-'*40}")
for name, path, nodes, elapsed in results:
    print(f"  {name:<10} {len(path)-1:>6} {nodes:>8} {elapsed:>12.4f}")
print(f"{'='*50}")

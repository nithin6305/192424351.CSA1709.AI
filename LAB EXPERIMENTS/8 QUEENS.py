from heapq import heappush, heappop

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    return sum(abs(i // 3 - (v - 1) // 3) +
               abs(i % 3 - (v - 1) % 3)
               for i, v in enumerate(state) if v != 0)

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, [start]))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue
        visited.add(state)

        zero = state.index(0)
        r, c = divmod(zero, 3)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                j = nr * 3 + nc
                new = list(state)
                new[zero], new[j] = new[j], new[zero]
                new = tuple(new)

                if new not in visited:
                    heappush(pq, (g + 1 + heuristic(new),
                                  g + 1, new, path + [new]))
    return None

path = solve(start)

if path:
    for state in path:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
    print("Steps:", len(path) - 1)
else:
    print("No solution found")

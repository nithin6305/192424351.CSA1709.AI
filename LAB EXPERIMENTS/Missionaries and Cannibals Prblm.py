from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [(1, 0), (2, 0), (0, 1),
         (0, 2), (1, 1)]

def safe(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (3 - m == 0 or 3 - m >= 3 - c))

queue = deque([(start, [start])])
visited = {start}

while queue:
    state, path = queue.popleft()
    m, c, boat = state

    if state == goal:
        for step in path:
            print(step)
        break

    for dm, dc in moves:
        if boat == 1:
            new = (m - dm, c - dc, 0)
        else:
            new = (m + dm, c + dc, 1)

        if safe(new[0], new[1]) and new not in visited:
            visited.add(new)
            queue.append((new, path + [new]))

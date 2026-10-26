import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 4, 'B': 3, 'C': 1, 'D': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            print("Start Node:", start)
            print("Goal Node:", goal)
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_cost = cost + weight
                heapq.heappush(
                    pq,
                    (new_cost + h[neighbor],
                     new_cost, neighbor, path + [neighbor])
                )

astar('A', 'D')

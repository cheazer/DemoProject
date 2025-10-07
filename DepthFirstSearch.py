def DFS(Graph, Vertex):
    visited = set()
    stack = [Vertex]
    Order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            Order.append(node)
            for neighbor in Graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return Order

raph1 = {'A': ['B','C'],
         'B': ['F'],
         'C': ['B'],
         'F': []}

print("made this change")

print(BFS(raph1, 'A'))

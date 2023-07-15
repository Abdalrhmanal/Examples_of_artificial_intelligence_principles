
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        if node not in visited:
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E','g'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['C', 'E'],
    'g':[]
}

bfs(graph, 'A')
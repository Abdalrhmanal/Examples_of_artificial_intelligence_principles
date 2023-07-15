graph = {
    '0': ['1', '2', '3'],
    '1': ['0', '2'],
    '2': ['0', '1', '4'],
    '3': [],
    '4': [],
}
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, '0')

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)],
    'G': []
}
H_table = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}
def path_f_cost(path):
    g_cost = sum(cost for _, cost in path)
    last_node = path[-1][0]
    h_cost = H_table.get(last_node, float('inf'))
    f_cost = g_cost + h_cost
    return f_cost, last_node
def a_star_search(graph, start, goal):
    visited = set()
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                if node2 not in visited:
                    new_path = path + [(node2, cost)]
                    queue.append(new_path)
    return None
solution = a_star_search(graph, 'S', 'G')
if solution:
    print('Solution is', solution)
    print('Cost of Solution is', path_f_cost(solution)[0])
else:
    print('No solution found.')

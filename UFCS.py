
#هذا الكود يقوم بتنفيذ خوارزمية البحث أولاً أفضل (UCS - Uniform Cost Search) على رسم بياني 
# (graph) للعثور على أقل تكلفة للوصول من النقطة البدء (start) إلى الهدف (goal).
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)],
    'G': []
}
def path_cost(path):
    total_cost = sum(cost for _, cost in path)
    return total_cost, path[-1][0]

def UCS(graph, start, goal):
    visited = set()
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
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
                new_path = path + [(node2, cost)]
                queue.append(new_path)
    return None
solution = UCS(graph, 'S', 'G')
if solution:
    print('Solution is', solution)
    print('Cost of Solution is', path_cost(solution)[0])
else:
    print('No solution found.')
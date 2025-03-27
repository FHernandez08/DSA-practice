sample_graph = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3, 4],
    3: [1, 0, 2],
    4: [2, 5],
    5: [4]
}

def bfs(graph, start_node):
    queue = [start_node]
    visited = set()
    
    distance = {node: float('inf') for node in graph}
    distance[start_node] = 0
    
    while queue:
        node = queue.pop()
    
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    
    return distance

# Call BFS starting from node 0
result = bfs(sample_graph, 0)
print(result)
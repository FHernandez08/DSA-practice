def bfs_traversal(graph, starting_node):
    queue = []
    visited = set()
    
    queue.append(starting_node)
    visited.add(starting_node)
    
    while queue:
        front_node = queue.pop(0)
        
        for neighbor in graph[front_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return visited
def buildGraph(connections):
    adjacent_graph = {}
    
    for a, b in connections:
        if a not in adjacent_graph:
            adjacent_graph[a] = []
        adjacent_graph[a].append(b)
        
        if b not in adjacent_graph:
            adjacent_graph[b] = []
        adjacent_graph[b].append(a)
    
    return adjacent_graph
    
    
    
connections = [["A", "B"], ["A", "C"], ["B", "D"], ["C", "E"], ["D", "E"]]
print(buildGraph(connections))
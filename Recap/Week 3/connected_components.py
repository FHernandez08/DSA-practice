def count_components(n: int, edges: list[list[int]]) -> int:
    adj_list = {}
    for i in range(n):
        adj_list[i] = []
    
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    visited = set()
    component_count = 0
    
    for node in range(n):
        if node not in visited:
            dfs(node, adj_list, visited)
            component_count += 1
            
    return component_count
        

# helper function        
def dfs(curr_node,adj_list, visited_set=set()):
    visited_set.add(curr_node)
    
    for neighbor in adj_list[curr_node]:
        if neighbor not in visited_set:
            dfs(neighbor, adj_list, visited_set)
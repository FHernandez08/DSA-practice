from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

class GraphDFS(Graph):  # Inheriting from Graph class
    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()  # Initialize the visited set

        if node not in visited:
            print(node, end=" ")  # Print the node
            visited.add(node)  # Mark the node as visited

            for neighbor in self.graph[node]:  # Recur for all connected nodes
                self.dfs(neighbor, visited)

# Example usage
g_dfs = GraphDFS()
g_dfs.add_edge(0, 1)
g_dfs.add_edge(0, 2)
g_dfs.add_edge(1, 2)
g_dfs.add_edge(2, 0)
g_dfs.add_edge(2, 3)
g_dfs.add_edge(3, 3)

print("DFS Traversal starting from node 0:")
g_dfs.dfs(0)  # Output: 0 1 2 3
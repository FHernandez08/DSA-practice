class GraphMatrix:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[0] * num_nodes for _ in range(num_nodes)]  # Initialize N x N matrix with 0s

    def add_edge(self, u, v):
        self.graph[u][v] = 1  # Add edge from u to v
        self.graph[v][u] = 1  # For undirected graphs. Remove this line for directed graphs.

    def display(self):
        for row in self.graph:
            print(row)
    
    def bfs(self, start_node):
        visited = [False] * self.num_nodes
        queue = [start_node]
        visited[start_node] = True

        print("BFS Traversal: ", end="")
        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in range(self.num_nodes):
                if self.graph[node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    def dfs(self, node, visited=None):
        if visited is None:
            visited = [False] * self.num_nodes

        visited[node] = True
        print(node, end=" ")

        for neighbor in range(self.num_nodes):
            if self.graph[node][neighbor] == 1 and not visited[neighbor]:
                self.dfs(neighbor, visited)


# Example usage
g_matrix = GraphMatrix(4)
g_matrix.add_edge(0, 1)
g_matrix.add_edge(0, 2)
g_matrix.add_edge(1, 2)
g_matrix.add_edge(2, 3)

print("Adjacency Matrix:")
g_matrix.display()

print("\nBFS starting from node 0:")
g_matrix.bfs(0)

print("\nDFS starting from node 0:")
g_matrix.dfs(0)
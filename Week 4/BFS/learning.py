from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

class GraphBFS(Graph):  # Inheriting from Graph class
    def bfs(self, start_node):
        visited = set()  # Track visited nodes
        queue = deque([start_node])  # Queue for BFS traversal

        while queue:
            node = queue.popleft()  # Dequeue a node from the front of the queue

            if node not in visited:
                print(node, end=" ")  # Print the current node
                visited.add(node)  # Mark the node as visited

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)  # Enqueue unvisited neighbors

# Example usage
g_bfs = GraphBFS()
g_bfs.add_edge(0, 1)
g_bfs.add_edge(0, 2)
g_bfs.add_edge(1, 2)
g_bfs.add_edge(2, 0)
g_bfs.add_edge(2, 3)
g_bfs.add_edge(3, 3)

print("BFS Traversal starting from node 0:")
g_bfs.bfs(0)  # Output: 0 1 2 3
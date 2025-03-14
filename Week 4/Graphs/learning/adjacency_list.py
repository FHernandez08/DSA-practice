from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Using defaultdict for automatic list creation

    def add_edge(self, u, v):
        """ Adds an edge from node u to node v (Directed Graph) """
        self.graph[u].append(v)

    def display(self):
        """ Displays the graph as an adjacency list """
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Graph representation (Adjacency List):")
g.display()
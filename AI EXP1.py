from collections import deque

class Graph:
    def __init__(self):
        # Adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Add edge u -> v
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque()

        visited.add(start)
        queue.append(start)

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def bfs_shortest_path(self, start, target):
        visited = set()
        queue = deque([(start, [start])])

        visited.add(start)

        while queue:
            node, path = queue.popleft()

            if node == target:
                return path

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None


# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    g = Graph()

    # Add edges
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')

    # Run BFS traversal
    g.bfs('A')

    # Find shortest path
    path = g.bfs_shortest_path('A', 'F')
    print("Shortest path from A to F:", path)

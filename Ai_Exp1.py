from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)
    print("\nBFS Traversal")
    while queue:
        node = queue.popleft()
        print(node, end = " ")
    
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def bfs_sp(graph, start, target):
    visited= set([start])
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path+[neighbor]))
    return None

graph = {}
n = int(input("Enter no. of vertices: "))
for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    neighbors = input(f"Enter neighbors of {vertex} (Space seperated): ").split()
    graph[vertex] = neighbors
start = input("\n Enter starting vertex of BFS: ")
target = input("Enter target vertex for shortest path: ")
bfs(graph, start)
path = bfs_sp(graph, start, target)
if path:
     print("\nShortest path: ",path)
else:
    print("\nNo path found")

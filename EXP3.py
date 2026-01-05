def dfs (graph, start, visited):
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {}
n = int(input("Enter no of vertices: "))
for i in range(n):
    vertex = input(f"Enter vertex {i + 1}: ")
    graph[vertex] = []
e = int(input("Enter no of edges: "))
for i in range(e):
    v1, v2 = input("Enter edge (v1 v2): ").split()
    graph[v1].append(v2)
    graph[v2].append(v1)
start_node = input("Enter starting node for DFS: ")
visited = set()
print("DFS Traversal : ")
dfs(graph, start_node, visited)
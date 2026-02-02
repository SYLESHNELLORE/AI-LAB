import heapq
def h_search(graph, heuristic, start, goal):
    priority_queue=[]
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()
    parent = {start : None}
    while priority_queue:
        h_value, current = heapq.heappop(priority_queue)
        if current == goal:
            break
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                if neighbor not in parent:
                    parent[neighbor] = current
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path
graph = {}
heuristic ={}
n = int(input("Enter no of nodes: "))
print("\nEnter nodes names: ")
nodes = []
for i in range(n):
    node = input()
    nodes.append(node)
    graph[node] = []
print("\nEnter edges (node neighbors). Type \"Done\" to stop.")
while True:
    edge = input()
    if edge.lower() == 'done':
        break
    u,v = edge.split()
    graph[u].append(v)
print("\nEnter heuristic value for each node:")
for node in nodes:
    heuristic[node] = int(input(f"h({node})= "))
start = input("\nEnter startingnode: ")
goal = input("Enter Goal node: ")
path = h_search(graph, heuristic, start, goal)
print("\nPath found using heuristic search: ")
print("->".join(path))
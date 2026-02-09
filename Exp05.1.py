import heapq
def a_star(start, goal, graph, heuristic):
    open_list=[]
    heapq.heappush(open_list, (0, start))
    g_cost = {start:0}
    parent = {start:None}
    while open_list:
        f, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("\nShortest path: ", path)
            print("Total cost: ", g_cost[goal])
            return
        for neighbor,cost in graph[current]:
            new_g = g_cost[current] + cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current
    print("Path not found")
graph = {}
heuristic = {}
n = int(input("Enter no of nodes: "))
nodes = []
print("Enter node names: ")
for i in range(n):
    node = input(f"Node{i+1}: ")
    nodes.append(node)
    graph[node] = []
e = int(input("Enter no of edges: "))
print("Enter edges with cost: ")
for i in range(e):
    u = input("From: ")
    v = input("To: ")
    cost = int(input("Cost: "))
    print()
    graph[u].append((v, cost))
print("Enter heuristic values: ")
for node in nodes:
    heuristic[node] = int(input(f"h({node})="))
start = input("Enter start node: ")
goal = input("Entergoalnode: ")
a_star(start, goal, graph, heuristic)
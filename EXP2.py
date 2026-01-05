import heapq

# -------- Best First Search Function --------
def best_first_search(start, goal, graph, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()

    print("\n--- Best First Search Traversal ---")

    while priority_queue:
        h_value, current = heapq.heappop(priority_queue)
        print("Visiting:", current)

        if current == goal:
            print("Goal node found!")
            return

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue,
                               (heuristic[neighbor], neighbor))

    print("Goal node not found.")


# -------- Main Program (Dynamic Input) --------
graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

nodes = []
print("\nEnter node names:")
for i in range(n):
    node = input(f"Node {i+1}: ")
    nodes.append(node)
    graph[node] = []

e = int(input("\nEnter number of edges: "))
print("Enter edges (From -> To):")
for i in range(e):
    u = input("From: ")
    v = input("To: ")
    graph[u].append(v)

print("\nEnter heuristic values:")
for node in nodes:
    heuristic[node] = int(input(f"h({node}) = "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

best_first_search(start, goal, graph, heuristic)

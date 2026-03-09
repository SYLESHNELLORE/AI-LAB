from collections import deque

def water_jug_bfs(capA, capB, goal):

    visited = set()
    queue = deque()

    queue.append((0, 0, []))

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == goal or b == goal:
            return path

        next_states = [
            (capA, b),      # Fill Jug A
            (a, capB),      # Fill Jug B
            (0, b),         # Empty Jug A
            (a, 0),         # Empty Jug B
            (a - min(a, capB - b), b + min(a, capB - b)),  # Pour A -> B
            (a + min(b, capA - a), b - min(b, capA - a))   # Pour B -> A
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None


capA = int(input("Enter capacity of Jug A: "))
capB = int(input("Enter capacity of Jug B: "))
goal = int(input("Enter the goal amount: "))

solution = water_jug_bfs(capA, capB, goal)

if solution:
    print("\nSteps to reach the goal:\n")
    for step in solution:
        print(step)
else:
    print("No solution found.")
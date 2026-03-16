import math

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    # Leaf node condition
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            False, values, alpha, beta)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Dynamic input
values = list(map(int, input("Enter 8 leaf node values: ").split()))

result = alphabeta(0, 0, True, values, -math.inf, math.inf)

print("Optimal value:", result)
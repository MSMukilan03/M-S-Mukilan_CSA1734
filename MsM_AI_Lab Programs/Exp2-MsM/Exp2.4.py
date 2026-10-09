import math
 
tree = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]
visited = 0
 
def alphabeta(node, alpha, beta, is_max):
    global visited
    if not isinstance(node, list):
        visited += 1
        return node
    if is_max:
        value = -math.inf
        for child in node:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    value = math.inf
    for child in node:
        value = min(value, alphabeta(child, alpha, beta, True))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value
 
best = alphabeta(tree, -math.inf, math.inf, True)
print("Optimal value at root (MAX):", best)
print("Leaf nodes evaluated:", visited, "(Minimax evaluates 8)")

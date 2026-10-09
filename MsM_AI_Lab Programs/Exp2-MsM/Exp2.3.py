tree = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]
visited = 0
 
def minimax(node, is_max):
    global visited
    if not isinstance(node, list):
        visited += 1
        return node
    values = [minimax(child, not is_max) for child in node]
    return max(values) if is_max else min(values)
 
best = minimax(tree, True)
print("Optimal value at root (MAX):", best)
print("Leaf nodes evaluated:", visited)

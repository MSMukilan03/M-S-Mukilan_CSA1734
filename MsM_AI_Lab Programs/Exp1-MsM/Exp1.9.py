from itertools import permutations
 
cities = ['A', 'B', 'C', 'D']
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]
 
def tour_cost(order):
    cost = 0
    for i in range(len(order)):
        cost += dist[order[i]][order[(i + 1) % len(order)]]
    return cost
 
best_cost, best_tour = float('inf'), None
for perm in permutations(range(1, len(cities))):
    tour = (0,) + perm
    c = tour_cost(tour)
    print(' -> '.join(cities[i] for i in tour + (0,)), "cost =", c)
    if c < best_cost:
        best_cost, best_tour = c, tour
 
print("\nBest tour:", ' -> '.join(cities[i] for i in best_tour + (0,)))
print("Minimum cost:", best_cost)

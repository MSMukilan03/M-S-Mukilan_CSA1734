N = 8
solutions = []
 
def safe(cols, row):
    c = len(cols)
    return all(r != row and abs(r - row) != c - i for i, r in enumerate(cols))
 
def place(cols):
    if len(cols) == N:
        solutions.append(cols[:])
        return
    for row in range(N):
        if safe(cols, row):
            cols.append(row)
            place(cols)
            cols.pop()
 
place([])
print("Total solutions:", len(solutions))
print("First solution (row index for each column):", solutions[0])
for r in range(N):
    print(' '.join('Q' if solutions[0][c] == r else '.' for c in range(N)))

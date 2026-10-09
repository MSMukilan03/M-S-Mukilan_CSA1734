import random
 
LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
 
def show(board):
    for i in range(0, 9, 3):
        print(' | '.join(board[i:i + 3]))
        if i < 6:
            print('---------')
    print()
 
def winner(board):
    for a, b, c in LINES:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    return None
 
def play():
    random.seed(7)
    board = [' '] * 9
    player = 'X'
    while True:
        move = random.choice([i for i, v in enumerate(board) if v == ' '])
        board[move] = player
        print("Player", player, "plays cell", move + 1)
        show(board)
        w = winner(board)
        if w:
            print("Winner:", w)
            return
        if ' ' not in board:
            print("Game is a draw")
            return
        player = 'O' if player == 'X' else 'X'
 
play()

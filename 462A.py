n = int(input())
board = [[0] * (n + 2)]
for i in range(n):
    board += [[0] + [0 if x == 'x' else 1 for x in input()] + [0]]
board += [[0] * (n + 2)]
yn = True
for i in range(1, n + 1):
    for j in range(1, n + 1):
        yn = yn and (board[i - 1][j] + board[i + 1][j] + board[i][j - 1] + board[i][j + 1]) % 2 == 0
print("YES" if yn else "NO")

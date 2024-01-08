board = [list(map(int, input().split())) for _ in range(9)]

max = -1
a, b = 0, 0

for i in range(9):
    for j in range(9):
        if board[i][j] > max:
            max = board[i][j]
            a = i
            b = j

print(max, a + 1, b + 1)

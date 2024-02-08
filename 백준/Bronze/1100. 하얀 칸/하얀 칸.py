board = [list(input()) for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(8):
        # 짝수 줄
        if i % 2 == 0 and j % 2 == 0:
            if board[i][j] == 'F':  # 하양, 검정 순서
                cnt += 1

        # 홀수 줄
        if i % 2 != 0 and j % 2 != 0:
            if board[i][j] == 'F':  # 하양, 검정 순서
                cnt += 1
print(cnt)

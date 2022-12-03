n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
# 잘 들어갔는지 확인
# for row in board:
#    print(row)

# dp 테이블
dp = [[0] * m for _ in range(n)]
# 0: top-down 방식에서는 0으로 하면 안됨. 절대 등장할 수 없는 값인 음수로 초깃값을 초기화 해주어야 함

for i in range(n):
    for j in range(m):
        if i:  # 0이 아닐때, dp 테이블에서 제일 윗줄이 아닐때
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if j:  # 0이 아닐때, dp 테이블에서 제일 왼쪽 줄이 아닐때
            dp[i][j] = max(dp[i][j], dp[i][j - 1])
        dp[i][j] += board[i][j]
# for row in dp:
#     print(*row)
print(dp[n - 1][m - 1]) # 우하단 값 도출

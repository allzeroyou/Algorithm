N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i:
            dp[i][j]=max(dp[i][j], dp[i-1][j])
        if j:
            dp[i][j]=max(dp[i][j], dp[i][j-1])
        dp[i][j]+=board[i][j]
# for row in dp:
#     print(*row)

print(dp[N-1][M-1])
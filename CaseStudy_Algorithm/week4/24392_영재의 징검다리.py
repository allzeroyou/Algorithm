# bottom-up
MOD= 1_000_000_007

N, M =map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M  for _ in range(N)] # 바텀업-> 초기값 0

for j in range(M):
    dp[N-1][j] = board[N-1][j] # #강화유리면 1 일반유리면 0

for i in range(N-2, -1, -1): # 큰수 부터 작은수로 역순!
    for j in range(M):
        # 일반유리면 볼것도없이 그 칸에 올 수 없음
        if board[i][j]: # 강화유리라면
            dp[i][j] = dp[i+1][j]

            if j > 0: # 왼쪽
                dp[i][j] += dp[i+1][j-1]
            if j < M-1:
                dp[i][j] += dp[i+1][j+1]
                dp[i][j] %= MOD

ans = 0

for j in range(M):
    ans += dp[0][j]
    ans %= MOD

print(ans)

# for row in dp:
#     print(*row)
'''
sep는 사이에 무슨 값을 넣을 건지 결정

print(1,2,3, sep=‘X’) 하면 1X2X3이렇게 출력됨

*은 unpacking임

*[1, 2, 3] 하면 1, 2, 3이 나옴

즉, print(*[1,2,3], sep=‘’) 하면 print(1,2,3, sep=‘’) 되고 출력은 123 이 나옴
'''
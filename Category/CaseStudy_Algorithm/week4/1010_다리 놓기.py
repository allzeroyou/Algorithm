import sys

input = sys.stdin.readline





dp = [[1] * 31 for _ in range(31)]


# 초기값 설정
for i in range(1, 31):
    dp[1][i] = i

for n in range(2, 31):
    for m in range(n + 1, 31):
        dp[n][m] = dp[n - 1][m - 1] + dp[n][m - 1]
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])

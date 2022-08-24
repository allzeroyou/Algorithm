import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


n, k = map(int, input().split())

MOD = 10_007

dp = [[0] * 1001 for _ in range(1001)]

for i in range(1001):
    dp[i][0] = dp[i][i] = 1


def bino(n, r):
    if dp[n][r] == 0:  # dp 테이블이 비었을 경우
        dp[n][r] = (bino(n - 1, r) + bino(n - 1, r - 1)) % MOD
    return dp[n][r]


print(bino(n, k))
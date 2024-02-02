n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp 테이블(보텀업)
dp = [0] * (k + 1)
# dp에서 초기값 설정은 매우 중요.
dp[0] = 1  # 동전을 사용하지 않았을 때 동전 0원 완성됨.

for coin in coins:
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]

print(dp[k])

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

# 동전 개수
ans = 0
for coin in coins:
    # k += 동전 * 개수
    ans += k//coin
    k %= coin

print(ans)

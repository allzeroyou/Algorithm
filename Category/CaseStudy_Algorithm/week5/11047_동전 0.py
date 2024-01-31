n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.reverse() # 역순으로 돌기
ans = 0

for coin in coins:  # O(N)
    ans += k//coin  # 사칙연산: O(1)
    k%=coin # 사칙연산: O(1)
    print(f'coin: {coin}, ans:{ans}, k:{k}')

print(ans)
# 총 시간복잡도: O(N)

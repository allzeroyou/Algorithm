import sys

sys.setrecursionlimit(10 ** 8)
# top-down
MOD = 10007

cache = [[0] * 1001 for _ in range(1001)]
# 초기값읕 결과값으로써 절대 등장하지 않는 값으로 해야!
# i.g) 피보나치에선, 0보다 같거나 큰 수가 나오니(0,1,1,2,3..)
# 초기값은 -1, -2 같은 수로 해야!
# 이항계수는 0이 아닌 양의 숫자가 등장하므로, 초기값은 0으로 해줘도 ok

# 1000칸으로 하면 안됨. 인덱스는 0~999까지 일것임 -> 1001로 하자
# cache[1000][1000]

for i in range(1001):
    cache[i][0] = cache[i][i] = 1  # 기저 조건을 반영해주어야!


def bino(n, r):
    if cache[n][r] == 0:
        cache[n][r] = (bino(n - 1, r) + bino(n - 1, r - 1)) % MOD

    return cache[n][r]


N, K = map(int, input().split())
print(bino(N, K))

for i in range(50):
    print(*cache[i])  # 도달안한 값은 0으로 출력

# 26 13으로 check 가능

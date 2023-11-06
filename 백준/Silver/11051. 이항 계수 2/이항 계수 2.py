import sys
sys.setrecursionlimit(10**8)
# top-down
MOD = 10007


cache =[[0]* 1001 for _ in range(1001)]


for i in range(1001):
    cache[i][0] = cache[i][i] = 1 # 기저 조건을 반영해주어야!

def bino(n,r):
    if cache[n][r] == 0:
        cache[n][r]=(bino(n-1,r)+bino(n-1,r-1))%MOD

    return cache[n][r]

N, K = map(int, input().split())
print(bino(N, K))
'''
f(n) := 길이 n 인 계단 수 개수

구하려는 답은 f(N)

초기값 f(1)=9

점화식 f(n) = f(n-1) ..

'''

MOD = 1_000_000_000

cache = [[-1]*10 for _ in range(101)]

cache[1][0] = 0

for i in range(1, 10):
    cache[1][i]=1

# 길이가 n, 마지막 숫자가 d인 계단 수 개수
def f(n, d):
    if cache[n][d] == -1:
        cache[n][d] = 0
        if d>0:
            cache[n][d] += f(n-1, d-1)
        if d<9:
            cache[n][d] += f(n-1, d+1) # 초과 가능성있음
            cache[n][d] %= MOD
    return cache[n][d]

N = int(input())
ans = 0

for d in range(10):
    ans += f(N,d)
    ans %= MOD
print(ans)

# f(N, d) for d in range(10)
# print(sum(f(N,d) for d in range(10)) % MOD)


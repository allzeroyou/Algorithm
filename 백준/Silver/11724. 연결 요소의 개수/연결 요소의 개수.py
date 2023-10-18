import sys
input = sys.stdin.readline # 빠른 입력

sys.setrecursionlimit(10**8)

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


N, M = map(int, input().split())

adj = [[0]*N for _ in range(N)] # 인접행렬

for _ in range(M):
    u, v = map(lambda x: x-1, map(int, input().split())) # to 0-based
    adj[u][v] = 1
    adj[v][u] = 1

# 인접행렬에 잘 담겼는지 확인
#for i, row in enumerate(adj):
#    print(f'{i}: {row}')
ans = 0
chk = [False] * N
for i in range(N):
    if not chk[i]:
        chk[i] = True
        ans += 1
        dfs(i)
print(ans)
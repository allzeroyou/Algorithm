# 그래프 표현
# 인접행렬  or 인접리스트
# 간선의 개수에 따라서 결정하면 됨
# 간선의 개수는 최대 N^2임
# 이때 문제에서 간선의 양 끝점이 서로 같지 않다고 명시함
# 따라서 N^2에서 대각선(간선의 양 끝점이 같은 경우)의 경우를 빼면
# NC2와 같음(N개 중에서 서로 다른 2개의 쌍을 뽑음) == N(N-1)/2 = O(N2) -> 밀집그래프
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
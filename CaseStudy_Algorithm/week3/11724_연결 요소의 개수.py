# 그래프를 코드로 표현하는 방법 2가지
# 인접행렬  or 인접리스트
# 간선의 개수에 따라서 결정하면 됨
# 간선의 개수는 최대 N^2임
# 이때 문제에서 간선의 양 끝점이 서로 같지 않다고 명시함
# 따라서 N^2에서 대각선(간선의 양 끝점이 같은 경우)의 경우를 빼면
# NC2와 같음(N개 중에서 서로 다른 2개의 쌍을 뽑음) == N(N-1)/2 = O(N^2) -> 밀집 그래프 -> 인접행렬

import sys

input = sys.stdin.readline  # 빠른 입력

sys.setrecursionlimit(10 ** 8)  # 재귀 제한 풀기


def dfs(now):
    for nxt in range(N):    # nxt: next/ 한줄을 쭉 돌면서
        if adj[now][nxt] and not chk[nxt]: # 1이 있다면 연결 되어 있고, 방문을 한 적이 없다면
            chk[nxt] = True
            dfs(nxt)


N, M = map(int, input().split())

adj = [[0] * N for _ in range(N)]  # 인접행렬(adjacent)

for _ in range(M):
    u, v = map(lambda x: x - 1, map(int, input().split()))  # 1~N(one based) -> to 0-based
    adj[u][v] = 1
    adj[v][u] = 1 # 양방향그래프(방향없는 그래프)

# 인접행렬에 잘 담겼는지 확인
# for i, row in enumerate(adj):
#    print(f'{i}: {row}')

ans = 0
chk = [False] * N # 방문 체크를 위함

for i in range(N):
    if not chk[i]: # 방문 안했으면
        chk[i] = True
        ans += 1
        dfs(i)
print(ans)


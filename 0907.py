import sys

input = sys.stdin.readline


# dfs 구현
def dfs(now):  # 현재 위치
    # 다음 연결된 노드 찾기
    # 한 줄을 쭉 보면서 열이 몇번일때의 1인 값?
    for nxt in range(n):
        if adj[now][nxt] and not visited[nxt]:  # 1이라면 연결됨(간선 존재)
            # 연결 + 방문체크(미방문시) -> 고고
            visited[nxt] = True
            dfs(nxt)


n, m = map(int, input().split())
# n^2 만큼의 2차원 배열
adj = [[0] * n for _ in range(n)]  # 인접행렬(adjacent)

# m 만큼의 u, v 쌍이 들어옴
for _ in range(m):
    u, v = map(lambda x: x - 1, map(int, input().split()))  # to 0-based
    adj[u][v] = 1
    adj[v][u] = 1  # 양방향 그래프
# 1~n => 1-based
# but 배열에서, 인덱스는 0부터 시작 & n-1에서 끝남
# 6을 담을 때 에러 발생(인덱스 5까지 존재) -> 1-based to 0-based / n+1 로 변경해주어야

# 인접행렬이 잘 담겼는지 출력
# for i, row in enumerate(adj):
#     print(f'{i}:{row}')
ans = 0  # count 변
visited = [False] * n  # 방문시 True로 변경

for i in range(n):
    if not visited[i]:  # 방문 안한 노드 발견시
        visited[i] = True  # 방문 체크
        ans += 1
        dfs(i)
print(ans)

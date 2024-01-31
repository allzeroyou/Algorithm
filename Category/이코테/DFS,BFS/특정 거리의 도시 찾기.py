# 모든 도로의 길이 = 1
# 간선의 비용 = 1
# 모든 간선의 비용이 동일할때는 bfs 사용
from collections import deque

n, m, k, x = map(int, input().split())
# 모든 도로의 길이 = 1
# 간선의 비용 = 1
# 모든 간선의 비용이 동일할때는 bfs 사용
from collections import deque

n, m, k, x = map(int, input().split())

# 2차원 맵
city = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]  # 방문하지 않은 노드

# 모든 도로의 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

visited[x] = 0  # 출발 도시까지의 거리는 0임.

# bfs 수행
q = deque([x])
while q:
    now = q.popleft()  # 현재 노드
    for next_node in city[now]:  # 현재 노드에서 이동할 수 있는 모든 도시 확인
        # 아직 방문 안했다면
        if visited[next_node] == -1:
            # 최단 거리 갱신
            visited[next_node] = visited[now] + 1
            q.append(next_node)
# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
chk = False
for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        chk = True
# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if not chk:
    print(-1)

# 2차원 맵
city = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]  # 방문하지 않은 노드

# 모든 도로의 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

visited[x] = 0  # 출발 도시까지의 거리는 0임.

# bfs 수행
q = deque([x])
while q:
    now = q.popleft()  # 현재 노드
    for next_node in city[now]:  # 현재 노드에서 이동할 수 있는 모든 도시 확인
        # 아직 방문 안했다면
        if visited[next_node] == -1:
            # 최단 거리 갱신
            visited[next_node] = visited[now] + 1
            q.append(next_node)
# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
chk = False
for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        chk = True
# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if not chk:
    print(-1)

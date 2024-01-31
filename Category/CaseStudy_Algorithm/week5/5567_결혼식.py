# 상근이의 친구-직접적인 연결
# 상근이의 친구의 친구-간접적인 연결
# 이때 상근이의 친구의 친구의 친구는 불가 -> 그래프의 깊이를 2로 제한한 탐색(bfs)

# bfs -> deque 필요
from collections import deque

n = int(input())
m = int(input())

# 그래프를 코드로 저장하는 방법 2가지: 인접행렬, 인접리스트
# 인접행렬: O(V^2) -> 밀집 그래프 이득
# 인접리스트: O(V+E) -> 희소 그래프 이득
# n^2 <= 250,000/ m <= 10,000
# 희소 그래프이므로 <인접리스트>를 사용하는게 합리적
adj = [[] for _ in range(n)]

for _ in range(m):
    # one base -> zero base
    a, b = map(lambda x: x - 1, map(int, input().split()))
    # 양방향 그래프
    adj[a].append(b)
    adj[b].append(a)


# 인접리스트 출력
# for i, row in enumerate(adj):
#     print(f'{i}, {row}')

def bfs():
    chk = [False] * n  # 방문 체크
    chk[0] = True  # 상근이 1번 -> zero base이므로 0번
    q = deque()
    q.append((0, 0))
    while q:
        now, d = q.popleft()
        if d < 2:  # depth < 2
            nd = d + 1  # 친구의 친구까지 도달 가능
            for nxt in adj[now]:
                if not chk[nxt]:
                    chk[nxt] = True
                    q.append((nxt, nd))
    return chk.count(True)


print(bfs() - 1)  # 상근이를 제외

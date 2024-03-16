# n개의 컴퓨터로 이뤄짐
# 한번의 해킹으로 여러개의 컴퓨터 해킹
# 신뢰, 비신뢰 관계로 이뤄짐.
# a->b 신뢰: b를 해킹하면 a도 해킹 가능 (순서 거꾸로 주의)--> 어떤 자료구조로?
# 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호?

from collections import deque


def bfs(node):  # 아... n이랑 n이 변수명이 겹쳐서...index error 남.
    q = deque([node])
    # 해킹한 컴퓨터 개수 세기
    cnt = 1
    # 방문 체크(중복 허용 x)
    visited = [False] * (n + 1)
    visited[node] = True  # 현재 노드를 방문(해킹)

    while q:
        cn = q.popleft()
        for nx in computer[cn]:
            if not visited[nx]:  # 방문안한 노드라면
                q.append(nx)  # 큐에 삽입
                visited[nx] = True
                cnt += 1

    return cnt


n, m = map(int, input().split())
computer = [[] for _ in range(n + 1)]  # computer 신뢰 관계 그래프

for _ in range(m):
    a, b = map(int, input().split())
    computer[b].append(a)  # b->a 순서 주의

# print(computer)
# 해킹한 컴퓨터 개수
count = [0] * (n + 1)

for i in range(1, n + 1):  # 1~n번
    count[i] = bfs(i)

# print(count)
# 해킹할 수 있는 컴퓨터 최댓값
max_com = max(count)
for i in range(len(count)):
    if count[i] == max_com:
        print(i, end=' ')

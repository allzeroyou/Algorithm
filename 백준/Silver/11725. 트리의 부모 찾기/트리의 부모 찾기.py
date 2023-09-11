from collections import deque

n = int(input())
visited = [False for _ in range(n + 1)]  # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
answer = [0 for _ in range(n + 1)]  # 정답 담을 리스트
graph = [[0] for _ in range(n + 1)]  # 트리

for _ in range(n - 1):  # 1은 제외
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 무방향은 양방향임.


def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    que = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while que:
        v = que.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                answer[i] = v
                que.append(i)
                visited[i] = True


bfs(graph, 1, visited)

for i in range(2, n + 1):  # 2번 노드부터 시행
    print(answer[i])

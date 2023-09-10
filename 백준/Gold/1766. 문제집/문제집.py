# 위상정렬+heapq 이용
import heapq

n, m = map(int, input().split())
# 문제간의 정보를 담을 그래프
graph = [[] for i in range(n + 1)]
# 진입차수 리스트(선수 문제)
indegree = [0 for i in range(n + 1)]
for i in range(m):
    first, last = map(int, input().split())
    graph[first].append(last)
    indegree[last] = indegree[last] + 1


def topology_sort():
    res = []  # 알고리즘 수행 결과 담을 리스트
    q = []  # 문제 번호가 작은 순서대로 정렬하기 위한 큐

    # 진입 차수가 0인 노드부터 큐에 삽입(문제 번호가 작은 것부터)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    while q:  # 큐가 빌때까지 반복
        # 큐에서 원소 꺼내기
        now = heapq.heappop(q)
        res.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1을 뺀다
        for j in graph[now]:
            indegree[j] = indegree[j] - 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[j] == 0:
                heapq.heappush(q, j)
    # 위상 정렬 수행한 결과 출력
    for i in res:
        print(i, end=' ')


topology_sort()

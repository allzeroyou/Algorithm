import sys

INF = int(1e9)
input=sys.stdin.readline

# 노드 개수 및 간선의 개수 입력
n = int(input())
m = int(input())

# 2차원 리스트 -> 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용->0으로 초기화
for a in range(n):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 각 간선에 대한 정보 입력 받아 그 값으로 초기화
for _ in range(m):
    a, b,c =map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
# output
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달 불가 -> 0
        if graph[a][b] == INF:
            print('0', end=' ')
        else: # 도달 가능 -> 최단거리 출력
            print(graph[a][b], end=' ')

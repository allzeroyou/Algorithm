# bfs-최단거리
from collections import deque

def solution(n, edge):
    # 양방향 그래프
    graph = [[] for _ in range(n+1)]
    
    for node in edge:
        a, b = node[0], node[1]
        graph[a].append(b)
        graph[b].append(a)
    # 최대길이
    dist = [0]*n
    visited =[0]*(n+1) # 방문체크
    
    # bfs
    q = deque([[1,0]]) #노드, 트리 깊이
    visited[1]=1
    
    while q:
        cur_node = q.popleft()
        node, dep = cur_node[0], cur_node[1]
        
        for nxt_node in graph[node]:
            if visited[nxt_node]==0: # 아직 방문안했다면
                visited[nxt_node]=1
                q.append([nxt_node, dep+1])
                dist[dep+1]+= 1
    # bfs 종료
    for i in range(n-1, -1, -1):
        if dist[i]!= 0:
            return dist[i]

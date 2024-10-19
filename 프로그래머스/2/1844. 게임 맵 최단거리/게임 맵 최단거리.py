# 최대한 빨리 도착 -> 최단거리 -> bfs
# nxm 크기 맵
# maps: 0은 벽이 있는 자리, 1은 벽이 없는 자리
from collections import deque

def solution(maps):
    answer = 0
    # 상하좌우 이동
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # bfs
    def bfs(x, y):
        # 1. 시작노드를 큐에 삽입, 방문처리
        q = deque()
        q.append((x,y))
        
        while q: # 큐가 빌때까지 반복
            x, y = q.popleft()
            # 상하좌우 칸 확인
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<= nx< len(maps) and 0<=ny< len(maps[0]) and maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y] +1 # 거리 증가
                    q.append((nx,ny)) # 큐에 삽입
                    
        return maps[len(maps)-1][len(maps[0])-1]
                    
    answer = bfs(0,0)
           
    # answer가 1 그대로 -> 도달 못함!
    if answer==1:
        return -1
    else:
        return answer

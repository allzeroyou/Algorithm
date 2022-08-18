# 최단거리 탐색
# BFS 사용
from collections import deque

dy= (0, 1, 0, -1)
dx= (1, 0, -1, 0)

N , M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y, x):
    return 0<= y < N and 0<= x < M

def bfs():
    chk = [[False]*M for _ in range(N)]
    chk[0][0] = True
    q= deque()
    q.append((0, 0, 1)) # 좌표
    while q:
        y, x,d = q.popleft()
        # print(f'({y}, {x}), d: {d}') # 시각적으로 확인
        if y==N-1 and x==M-1: # 도착
            return d
        nd = d+ 1
        for k in range(4):
            ny = y+ dy[k]
            nx = x+ dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx] and board[ny][nx]=='1': # 범위체크
            # 1만 가능, 0은 빈칸(벽이라고 생각)
                chk[ny][nx]= True
                q.append((ny, nx, nd))


print(bfs())


from collections import deque
# bfs 사용을 위한 큐 인포트

N, M = map(int, input().split())

board=[input() for _ in range(N)] # 보드판이라고 생각하겠음

# 제일 좌상단에서 시작
def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    q =deque()
    q.append((0,0,1)) # 좌표(1부터 시작)
    while q:
        y,x,d = q.popleft() # 지금까지의 누적을 d에 저장
        if y==N-1 and x==M-1: # 도착
            return
        for k in range(4):
            ny=y+dy[k]
            nx=x+dx[k]
            if is_valid_coord(ny, nx): # 범위 체크


print(bfs())




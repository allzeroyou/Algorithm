from collections import deque
import copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# 안전지대 크기
ans = 0


# 1. 벽세우기
def wall(cnt):
    if cnt == 3:
        # 2. 바이러스 퍼뜨리기
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:  # 빈칸이라면 벽세우기
                board[i][j] = 1
                wall(cnt+1) # 벽 개수 증가
                board[i][j]=0 # 벽 허물기(백트래킹용)

# 2. 바이러스 퍼뜨리기
def bfs():
    global ans
    tmp = copy.deepcopy(board) # 맵 깊은 복사

    # 1. 큐 생성
    q = deque()
    # 첫번째 노드 저장(바이러스 위치!
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                q.append((i,j))
    # queue 가 빌때까지 실행
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if  tmp[nx][ny]==0:
                    # 바이러스 퍼뜨리기
                    tmp[nx][ny]=2
                    q.append((nx,ny))
    # 벽 개수 세기
    w_cnt = 0
    for t in tmp:
        w_cnt += t.count(0)
    ans = max(w_cnt, ans)

# 함수 실행
wall(0)
print(ans)



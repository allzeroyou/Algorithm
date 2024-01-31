from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x): # 범위체크
    return 0 <= y < N and 0 <= x < N


def bfs(sy, sx):
    chk[sy][sx] = True  # 방문체크
    q = deque()
    q.append((sy, sx))
    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] > water and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx))

# 입력받기
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
lo = min(min(row) for row in board) # low
hi = max(max(row) for row in board) # high
ans = 1

for water in range(lo, hi):
    cnt = 0
    chk = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > water and not chk[i][j]:
                cnt += 1
                bfs(i, j)

    ans = max(ans, cnt)

print(ans)
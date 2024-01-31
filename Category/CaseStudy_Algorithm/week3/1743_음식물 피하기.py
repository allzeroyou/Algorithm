import sys

sys.setrecursionlimit(10 ** 8)

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
n, m, k = map(int, input().split())

board = [['.'] * (m) for _ in range(n)]

# 쓰레기 좌표 -> # 표시
for _ in range(k):
    y,x = map(int, input().split())
    board[y-1][x-1] = '#'

visited = [[False] * m for _ in range(n)]
size = 0
ans = 0


def is_valid_coord(y, x): # 범위 체크(coordinates: 좌표)
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    global ans, size
    visited[y][x] = True

    size += 1
    ans = max(ans, size)

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and not visited[ny][nx] and board[ny][nx] == '#':
            dfs(ny, nx)


for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == '#':
            size = 0
            dfs(i, j)
print(ans)

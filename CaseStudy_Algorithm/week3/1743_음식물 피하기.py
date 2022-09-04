import sys
sys.setrecursionlimit(10**8)
dy=(0, 1, 0, -1)
dx=(1,0,-1,0)
n, m, k = map(int, input().split())

board = [['.'*m for _ in range(n)]]

for _ in range(k):
    y, x =map(int, input().split())
    board[y-1][x-1]='#'

visited = [[False]*m for _ in range(n)]
sz = 0
ans = 0

def is_valid(y, x):
    return 0<=y<n and 0<=x<m
def dfs(y, x):
    global ans, sz
    visited[y][x] = True

    sz+=1
    ans=max(ans, sz)

    for k in range(4):
        ny = y+dy[k]
        nx=x+dx[k]
        if is_valid(ny, nx) and not visited[ny][nx] and board[ny][nx] =='#':
            dfs(ny, nx)
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == '#':
            sz=0
            dfs(i, j)
print(ans)
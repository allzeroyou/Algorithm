#북-동-남-서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, d): #청소시작 
    global ans #정답변수
    if a[x][y] == 0: #청소가능한 부분 
        a[x][y] = 2 #청소완료
        ans += 1 #정답 + 1
    for _ in range(4): #상하좌우탐색
        nd = (d + 3) % 4 #왼쪽으로 회전 
        nx = x + dx[nd] #새로운 x좌표
        ny = y + dy[nd] #새로운 y좌표
        if a[nx][ny] == 0: #청소가능하면 
            dfs(nx, ny, nd) #dfs탐색 
            return
        d = nd 
    nd = (d + 2) % 4 #뒤쪽 방향
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1: #바로 뒤쪽이 벽 
        return #멈추기
    dfs(nx, ny, d) #뒤로 후진에서 탐색 


n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
dfs(x, y, d)
print(ans)
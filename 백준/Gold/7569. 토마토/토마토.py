from collections import deque

# 상자 가로 m, 세로 n, 상자 수 h
m, n, h = map(int, input().split())

# 토마토 상태 -> 3차원 배열로 관리-> arr [ 높이인덱스 ] [ 세로인덱스 ] [ 가로인덱스 ] = 값 의 형태로 호출
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 하루 지나면 익은 토마토에 인접(6방향)한 익지 않은 토마토-> 익음
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]  # 앞, 뒤를 어떻게 표현하지? -> (앞:1, 뒤:-1)

# 다음 토마토 탐색할 큐
q = deque()

# 정답
ans = -1 # 최솟값으로 세팅

# bfs를 위한 큐 생성
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 익은 토마토를 큐에 저장( -> 인접한 익지 않은 토마토 탐색)
            # 높이(h), 가로(x), 세로(y) 순서
            if tomato[i][j][k] == 1:
                q.append([i, j, k])


def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if tomato[nz][nx][ny] == 0:  # 토마토가 익지 않았다면
                    # 토마토가 익는 데 걸리는 시간 = 현재까지 걸린 시간 + 1
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1
                    q.append([nz, nx, ny])


# 함수 실행
bfs()

# 모든 토마토가 익었는지 판별
flag = False

# 모든 토마토가 익는 데 걸리는 최소 일 수
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:  # bfs를 돌았음에도 익지 않은 토마토가 있을때
                flag = True
            ans = max(ans, tomato[i][j][k])  # 모든 토마토 익는 최소 일 수 구한다
if flag:
    ans = -1
elif ans == 1:  # 모든 토마토가 익은 상태였다면
    ans = 0
else:
    ans -= 1  # 오늘은 빼준다

print(ans)


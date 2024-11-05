# 토마토

# 토마토 상태: 익음, 익지않음
# 보관 후 하루가 지나면 -> 익은 토마토에 인접한 익지 않은 토마토가 익음.
# 인접: 동서남북, 앞뒤
# 최소 며칠이 지나면 모든 토마토가 익는지?

# 상자의 일부 칸에는 토마토가 없을수도

# 상자크기: 가로 m, 세로 n, 높이: h
# 가장 밑~위까지의 토마토 정보
# 각 줄: 상자 가로줄에 들어있는 토마토 상태가 m개의 정수로 주어짐
# 1: 익은 토마토, 0: 익지 x, -1: 토마토 x
# 만약 저장될때부터 모든 토마토가 익어있다면 0 출력
# 토마토가 모두 익지 못한다면 -1 출력
from collections import deque


def sol():
    m, n, h = map(int, input().split())
    # 상하좌우, 앞, 뒤
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]  # 앞: 1, 뒤: -1

    # 3차원 배열 board[h][n][m]
    board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    # 큐
    q = deque()

    # 익은토마토: 1 찾기-> 큐에 저장(bfs 실행 지점)
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 1:
                    q.append((i, j, k))

    def bfs():
        while q:
            z, y, x = q.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                    if board[nz][ny][nx] == 0:  # 익지 않았다면
                        board[nz][ny][nx] = board[z][y][x] + 1  # 지금까지 걸린시간 +1
                        q.append((nz, ny, nx))

    bfs()  # 실행

    # 모든 토마토가 익는데 걸리는 최 소 일수 구하기
    ans = 0

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0:  # 인접한 곳을 익혔는데도 익지 않은 토마토 존재시
                    print(-1)
                    return
                ans = max(ans, board[i][j][k])

    print(ans - 1)


sol()

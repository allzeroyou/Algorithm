# https://www.codetree.ai/training-field/frequent-problems/problems/codetree-mon-bread/description?page=1&pageSize=20
from collections import deque

# n: 격자크기, m: 사람 수
n, m = tuple(map(int, input().split()))

board = []  # 격자 0: 빈칸, 1: 베이스 캠프, 2: 이동 불가
for _ in range(n):
    board.append(list(map(int, input().split())))  # 0-based


def minus_one(x):
    return int(x) - 1


conv = []  # 편의점
for _ in range(m):
    conv.append(tuple(map(minus_one, input().split())))  # 1-based -> 0-based
# 현재 사람들의 위치 관리(초기: 격자 밖이므로 -1, -1)
person = [(-1, -1)] * m
# 현재 시간을 기록합니다.
curr_t = 0

# 상, 좌, 우, 하
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

# 최단거리 결과 기록
step = [[0] * n for _ in range(n)]

# 방문 여부 표시
visited = [[False] * n for _ in range(n)]


# 전부 편의점에 도착했는지 확인
def is_finish():
    for i in range(m):
        if person[i] != conv[i]:  # 도착했다면 편의점 위치와 동일해야 함.
            return False
    return True


# 격자 안에 있는 좌표인지 확인
def in_board(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


# 갈 수 있는 곳인지 체크
def can_go(x, y):
    # 범위를 벗어나지 않으면서, 방문했던 적이 없으면서, 이동이 가능한 곳이어야 함.
    return in_board(x, y) and not visited[x][y] and board[x][y] != 2


# 자신이 가고 싶은 편의점으로의 최단거리의 베이스캠프
def bfs(start_pos):
    # visited, step 값 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0
    # 초기 위치 넣어준다.
    q = deque()
    q.append(start_pos)
    sx, sy = start_pos
    visited[sx][sy] = True
    step[sx][sy] = 0

    # bfs 진행
    while q:
        x, y = q.popleft()

        # 인접한 칸을 보며 아직 방문하지 않은 칸을 큐에 넣어줌
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            # 갈 수 있는 경우만
            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))


def is_arrived(i):
    return person[i] == conv[i]


def simulate():
    # step1. 모든 사람이 한 칸 움직인다.
    for i in range(m):
        # 만약 격자 밖에 있거나 이미 편의점에 도착한 사람이라면 패스
        if person[i] == (-1, -1) or is_arrived(i):
            continue
        # 현재 위치에서 편의점까지의 최단거리를 구해야하지만, 그 다음 최단거리의 위치를 구하기 위해서-> 거꾸로 편의점에서 현재 위치까지 오는 최단거리를 구한
        # 따라서 편의점 위치를 시작으로하는 BFS 구한다.
        bfs(conv[i])

        px, py = person[i]
        # 현재 위치에서 상좌우하 중 최단거리를 고르면, 거기로 이동하는게 최단거리로 이동하는 것임.
        # 그러한 위치 중 적절한 곳을 골라줌.
        min_dist = 10000
        min_x, min_y = -1, -1
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + px, dy + py
            if in_board(nx, ny) and visited[nx][ny] and min_dist > step[nx][ny]:  # 최단거리를 찾았다면
                min_dist = step[nx][ny]
                min_x, min_y = nx, ny
        # 사람을 1칸 옮겨준다
        person[i] = (min_x, min_y)

    # step2. 편의점 도착한 사람 처리 -> 도착했다면 다른 사람들은 지날 수 없다
    for i in range(m):
        if is_arrived(i):
            px, py = person[i]
            board[px][py] = 2

    # step3. 새로 출발할 사람 처리
    # 만약 t>m라면 패스
    if curr_t > m:
        return
    # 편의점으로의 가장 가까운 베이스캠프 구하기 위해 편의점을 시작으로 하는 BFS 구한다
    bfs(conv[curr_t - 1])

    # 편의점에서 가장 가까운 베이스 캠프 선택
    # i, j 순으로 증가하기 때문에 가장 가까운 베이스 캠프가 여려개여도 알아서 (행, 열) 우선순위대로 골라짐
    min_dist = 10000
    min_x, min_y = -1, -1
    for i in range(n):
        for j in range(n):
            # 방문 가능한 베이스 캠프 중 거리가 가장 가까운 위치 찾아준다.
            if visited[i][j] and board[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_x, min_y = i, j
    # 우선순위가 가장 높은 베이스 캠프로 이동
    person[curr_t - 1] = (min_x, min_y)
    # 해당 베이스 캠프는 앞으로 이동 불가능
    board[min_x][min_y] = 2


# 1분에 한번씩 시뮬레이션 돌리기
while 1:
    curr_t += 1
    simulate()
    # 전부 이동이 끝났다면 종료하기
    if is_finish():
        break
print(curr_t)

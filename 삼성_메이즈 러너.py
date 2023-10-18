# 미로크기, 참가자수, 게임 시간
N, M, K = tuple(map(int, input().split()))
# 미로 입력
maze = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    maze[i] = [0] + list(map(int, input().split()))

# 회전의 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의
rotate_maze = [[0] * (N + 1) for _ in range(N + 1)]

# 참가자
people = [(-1, -1)]
for _ in range(M):
    people.append(tuple(map(int, input().split())))
# 출구 좌표
exit_pos = tuple(map(int, input().split()))
# 모든 참가자들의 이동 거리 합
ans = 0
# 회전해야 하는 최소 정사각형을 찾아 기록
sx, sy, square_size = 0, 0, 0


# 1. 움직이는 조건.
def move():
    global ans, exit_pos
    # M명의 모든 참가자에 대해 이동
    for i in range(1, M + 1):
        # 출구에 있다면 패스
        if people[i] == exit_pos:
            continue
        px, py = people[i]
        ex, ey = exit_pos
        # 행이 다를 경우 행 이동
        if px != ex:
            nx, ny = px, py
            if nx < ex:
                nx += 1
            else:
                nx -= 1
            # 벽이 아닐 경우 행 이동 시킴
            if not maze[nx][ny]:
                people[i] = (nx, ny)
                ans += 1
                continue
        # 열이 다른 경우 열 이동
        if py != ey:
            nx, ny = px, py
            if ny < ey:
                ny += 1
            else:
                ny -= 1
            # 벽이 아닐 경우 열 이동 시킴
            if not maze[nx][ny]:
                people[i] = (nx, ny)
                ans += 1
                continue


# 2. 미로 회전 조건.
# 2-1. 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 잡음
def find_square():
    global sx, sy, square_size, exit_pos
    ex, ey = exit_pos

    # 가장 작은 정사각형부터 모든 정사각형 만들기
    for size in range(2, N + 1):
        # 가장 좌상단 r 좌표가 작은 것이 우선됨
        for x1 in range(1, N - size + 2):
            # 가장 좌상단 c 좌표가 작은 것이 우선됨
            for y1 in range(1, N - size + 2):
                x2, y2 = x1 + size - 1, y1 + size - 1
                # 만약 출구가 해당 정사각형 안에 없다면 패스
                if not (x1 <= ex <= x2 and y1 <= ey <= y2):
                    continue
                # 한 명 이상의 참가자가 해당 정사각형 안에 있는지
                is_people_in = False
                for j in range(1, M + 1):
                    px, py = people[j]
                    if x1 <= px <= x2 and y1 <= py <= y2:
                        # 출구에 있는 참가자는 제외
                        if not (px == ex and py == ey):
                            is_people_in = True
                # 만약 한 명 이상의 참가자가 해당 정사각형 안에 있다면
                # sx, sy, square_size 정보 갱신 후 종료
                if is_people_in:
                    sx, sy = x1, y1
                    square_size = size
                    return


# 2-2. 시계방향으로 90도 회전
# 2-2-1. 선택된 정사각형 내부의 "벽"을 시계방향으로 90도 회전
def rotate_square_wall():
    # 우선 정사각형 안에 있는 벽들을 1 감소시킴
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            if maze[x][y]:
                maze[x][y] -= 1
    # 정사각형을 시계 방향으로 90도 회전
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            # step1. (sx, sy) -> (0, 0)으로 옮겨주는 변환
            ox, oy = x - sx, y - sy
            # step2. 변환된 상태에서는 회전 이후의 좌표: (x, y) -> (y, square_n - x -1)이 됨
            rx, ry = oy, square_size - ox - 1
            # step3. 다시 (sx, sy)를 더해줌
            rotate_maze[rx + sx][ry + sy] = maze[x][y]
    # rotate_maze 값을 현재 maze에 옮겨준다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            maze[x][y] = rotate_maze[x][y]


# 2-2-2. 선택된 정사각형 내부의 "참가자", "출구" 시계방향으로 90도 회전
def rotate_people_and_exit():
    global exit_pos
    # M명의 참가자들 확인
    for i in range(1, M + 1):
        px, py = people[i]
        # 해당 참가자가 정사각형 안에 있을 때만 회전
        if sx <= px < sx + square_size and sy <= py < sy + square_size:
            # step1. (sx, sy) -> (0, 0)으로 옮겨주는 변환
            ox, oy = px - sx, py - sy
            # step2. 변환된 상태에서는 회전 이후의 좌표: (x, y) -> (y, square_n - x -1)이 됨
            rx, ry = oy, square_size - ox - 1
            # step3. 다시 (sx, sy)를 더해줌
            people[i] = (rx + sx, ry + sy)
    # 출구에도 회전
    ex, ey = exit_pos
    if sx <= ex < sx + square_size and sy <= ey < sy + square_size:
        # step1. (sx, sy) -> (0, 0)으로 옮겨주는 변환
        ox, oy = ex - sx, ey - sy
        # step2. 변환된 상태에서는 회전 이후의 좌표: (x, y) -> (y, square_n - x -1)이 됨
        rx, ry = oy, square_size - ox - 1
        # step3. 다시 (sx, sy)를 더해줌
        exit_pos = (rx + sx, ry + sy)


# 게임 진행
for _ in range(K):
    # 모든 참가자들 이동
    move()
    # 모든 사람이 출구로 탈출했는지 판단
    is_all_people_exit = True
    for i in range(1, M + 1):
        if people[i] != exit_pos:
            is_all_people_exit = False
    # 만약 모든 사람이 나갔다면 종료
    if is_all_people_exit:
        break
    # 한 명 이상의 참가자와 출구룰 포함한 가장 작은 정사각형 찾기
    find_square()
    # 정사각형 내부 벽 회전
    rotate_square_wall()
    # 정사각형 내부 참가자, 출구 회전
    rotate_people_and_exit()
print(ans)
ex, ey = exit_pos
print(ex, ey)

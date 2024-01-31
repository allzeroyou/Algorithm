# 컴파일 OK
# BUT NOT PASS
# 수정 필요

# 4 x 4 격자에 m개의 몬스터, 1개의 팩맨 주어짐.
max_m = 10  # 최대 몬스터 수
max_t = 25  # 최대 게임 턴
max_n = 4  # 고정 격자 크기
dir_num = 8  # 몬스터가 움직일 수 있는 방향
pac_dic_num = 4  # 팩맨이 움직일 수 있는 방향
max_decay = 2  # 몬스터 소멸되는 턴 수

# 몬스터 m, 진행되는 턴 t
n = 4
m, t = tuple(map(int, input().split()))
# 팩맨 위치 저장
px, py = tuple(map(int, input().split()))
px -= 1
py -= 1

# map 생성
# t번째 턴에 (x,y)위치에 방향 move_dir를 바라보고 있는 몬스터 수
# board = [[[[0] * dir_num for _ in range(n)] for _ in range(n)] for _ in range(max_t + 1)]
board = [
    [
        [
            [0] * dir_num
            for _ in range(n)
        ]
        for _ in range(n)
    ]
    for _ in range(max_t + 1)
]

# 시체 저장할 격자 생성
dead_board = [[[0] * (max_decay + 1) for _ in range(n)] for _ in range(n)]

# 문제에서 주어지는 방향 순으로 dx, dy값 정의
# 몬스터 위한 방향:  ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

# 팩맨을 위한 방향: 상,좌,하,우 의 우선순위.
# dx, dy를 따로 정의
p_dxs = [-1, 0, 1, 0]
p_dys = [0, -1, 0, 1]

# 현재 몇 번째 턴인지 저장
t_num = 1

# 살아남은 총 몬스터 마리수
survive_monster = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 이때 움직이려는 칸에 시체 x and 팩맨 x and 격자를 벗어나지 않는다면
def can_go(x, y):
    return in_range(x, y) and dead_board[x][y][0] == 0 or dead_board[x][y][1] == 0 and (x, y) != (px, py)


# 반시계 방향으로 45도 회전 → 해당 방향으로 이동할 수 있는지 판단.
def get_next_pos(x, y, move_dir):
    # 현재 위치부터 반시계 방향으로 45'씩 회전-> 가능한 곳이 보이면 바로 이동
    for c_dir in range(dir_num):
        n_dir = (move_dir + c_dir + dir_num) % dir_num
        nx, ny = x + dxs[n_dir], y + dys[n_dir]
        if can_go(nx, ny):
            return (nx, ny, n_dir)
    # 이동 불가능->움직이지 않고 기존 상태로 그대로 반환
    return (x, y, move_dir)


# 몬스터 이동
def move_monster():
    # 각 (i,j)칸에 k방향을 바라보고 있는 몬스터들이
    # 그 다음으로 이동해야할 위치 및 방향을 구해
    # 전부 (칸, 방향) 단위로 이동시켜 줍니다.
    for i in range(n):
        for j in range(n):
            for k in range(dir_num):
                x, y, next_dir = get_next_pos(i, j, k)
                board[t_num][x][y][next_dir] += board[t_num - 1][i][j][k]


#  만약 가장 많이 먹을 수 있는 방향 탐색.
def get_killed_num(dir1, dir2, dir3):
    x, y = px, py
    killed_num = 0
    # 방문한 적 있는지 기록
    v_pos = []
    for move_dir in [dir1, dir2, dir3]:
        nx, ny = x + p_dxs[move_dir], y + p_dys[move_dir]
        # 움직이는 도중에 격자를 벗어난 경우라면 선택 불가
        if not in_range(nx, ny):
            return -1
        # 이미 계산한 곳에 대해선 중복 계산 x
        if (nx, ny) not in v_pos:  # 포함되지 않은 요소들에 대해서만 계산.
            killed_num += sum(board[t_num][nx][ny])
            v_pos.append((nx, ny))
    return killed_num


# 몬스터 먹는다.
def do_kill(best_route):
    global px, py
    dir1, dir2, dir3 = best_route
    # 정해진 d1, d2, d3에 맞게 이동하며 몬스터 잡음
    for move_dir in [dir1, dir2, dir3]:
        nx, ny = px + p_dxs[move_dir], py + p_dys[move_dir]
        for i in range(dir_num):
            dead_board[nx][ny][max_decay] += board[t_num][nx][ny][i]
            board[t_num][nx][ny][i] = 0
        px, py = nx, ny


# 3. 팩맨 이동
def move_pacman():
    # 팩맨 이동은 총 3칸. 각 이동마다 상하좌우의 선택지 가짐.
    max_cnt = -1
    best_route = (-1, -1, -1)

    # 만약 가장 많이 먹을 수 있는 방향이 여러개라면 → 상,좌,하,우 의 우선순위.
    for i in range(pac_dic_num):
        for j in range(pac_dic_num):
            for k in range(pac_dic_num):
                m_cnt = get_killed_num(i, j, k)
                # 가장 많은 수의 몬스터를 잡을 수 있는 경우 중 가장 우선순위가 높은 것
                if m_cnt > max_cnt:
                    max_cnt = m_cnt
                    best_route = (i, j, k)
    # 이동하는 과정에 있는 몬스터만 먹음
    do_kill(best_route)


# 몬스터 시체 소멸
def decay_monster():
    for i in range(n):
        for j in range(n):
            for k in range(max_decay):
                dead_board[i][j][k] = dead_board[i][j][k + 1]
            dead_board[i][j][max_decay] = 0


#  몬스터 복제 시도
def add_monster():
    for i in range(n):
        for j in range(n):
            for k in range(dir_num):
                board[t_num][i][j][k] += board[t_num - 1][i][j][k]


def simulate():
    # 매초마다 기록 -> 굳이 copy 안해도 ok
    # 각 칸에 있는 몬스터 이동
    move_monster()
    # 팩맨 이동
    move_pacman()
    # 시체 소멸
    decay_monster()
    # 몬스터 복제
    add_monster()


# 몬스터 개수 세기
def count_monster():
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(dir_num):
                cnt += board[t][i][j][k]
    return cnt


for _ in range(m):
    mx, my, mdir = tuple(map(int, input().split()))
    # 첫번째 턴의 상태 기록
    board[0][mx - 1][my - 1][mdir - 1] += 1
# t번 시뮬레이션 진행
while t_num <= t:
    simulate()
    t_num += 1
print(count_monster())

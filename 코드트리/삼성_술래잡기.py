# n:격자크기, m: 도망자, h: 나무 수, k: 게임 횟수
n, m, h, k = map(int, input().split())
# 각 칸에 있는 도망자 정보 관리.
# 도망자 방향만 저장하면 충분함.
hiders = [[[] for _ in range(n)] for _ in range(n)]
next_hiders = [[[] for _ in range(n)] for _ in range(n)]
# 나무 정보
tree = [[False] * n for _ in range(n)]

# 도망자 위치, 이동방법
# d:1 ->좌우로 움직임(오른쪽 보고 시작)
# d:2 -> 상하로 움직임(아래쪽 보고 시작)
for _ in range(m):
    x, y, d = tuple(map(int, input().split()))
    hiders[x - 1][y - 1].append(d)  # 0-based

# 나무 위치
for _ in range(h):
    x, y = map(int, input().split())
    tree[x - 1][y - 1] = True
# 정방향) 현재 위치에서 술래가 움직여야할 방향 관리
seeker_next_dir = [[0] * n for _ in range(n)]
# 역방향) 현재 위치에서 술래가 움직여야할 방향 관리
seeker_rev_dir = [[0] * n for _ in range(n)]
# 술래 현재 위치
seeker_pos = (n // 2, n // 2)
# 술래 움직이는 방향이 정방향: True, 아니라면 False
forward_facing = True
# 점수
total_score = 0


# 격자 내 존재하는 지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 술래가 정중앙으로부터 끝까지 움직이는 경로 계산
# 달팽이 배열(방향 배열) 채우기

def init_seeker_path():
    # 상우하좌 순으로 채워준다.
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    # 시작 위치와 방향, 해당 방향으로 이동할 횟수 설정.
    curr_x, curr_y = n // 2, n // 2  # 시작 위치(정중앙)
    move_dir, move_num = 0, 1  # 방향, 해당 방향으로 이동할 횟수

    while curr_x or curr_y:
        # move_num만큼 이동
        for _ in range(move_num):
            seeker_next_dir[curr_x][curr_y] = move_dir
            curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]
            if move_dir < 2:
                seeker_rev_dir[curr_x][curr_y] = move_dir + 2  # ? 왜 +2
            else:
                seeker_rev_dir[curr_x][curr_y] = move_dir - 2  # ? 왜
            # 이동하는 도중(0,0)로 오게되면
            # 움직이는 거 종료
            if not curr_x and not curr_y:
                break
        # 방향 바꾸기
        move_dir = (move_dir + 1) % 4
        # 만약 현재 방향이 위 or 아래 -> 특정방향으로 움직여야 할 횟수 1 증가
        if move_dir == 0 or move_dir == 2:
            move_num += 1


def move_hider(x, y, move_dir):
    # 방향: b에서 3번째요소가 1이라면->left_right/ 2이라면->up_down

    # 좌우하상 순으로 채워준다.
    dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0]

    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    # step1. 만약 격자를 벗어나면 우선 방향을 틀어준다.
    if not in_range(nx, ny):
        move_dir = 1 - move_dir if move_dir < 2 else 5 - move_dir  # 2, 1
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
    # step2. 격자 벗어나지 않을때 이동하려는 그 다음 위치에 술래가 없다면 움직임
    if (nx, ny) != seeker_pos:
        next_hiders[nx][ny].append(move_dir)
    # 술래가 있다면, 움직이지 않음
    else:
        next_hiders[x][y].append(move_dir)


def dist_from_seeker(x, y):
    # 현재 술래의 위치를 불러온다
    seeker_x, seeker_y = seeker_pos
    return abs(seeker_x - x) + abs(seeker_y - y)


def move_hider_all():
    # step1. next hider를 초기화
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []
    # step2. hider를 모두 움직여줌.
    for i in range(n):
        for j in range(n):
            # 이때 술래와의 거리가 3이하인 도망자만 움직임
            if dist_from_seeker(i, j) <= 3:
                for move_dir in hiders[i][j]:
                    move_hider(i, j, move_dir)
            # 그렇지 않다면 현재 위치 그대로 넣어준다.
            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)
    # step3. next hider 값을 옮겨줌.
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]


# 현재 술래가 바라보는 방향 구하기
def get_seeker_dir():

    # 현재 술래의 위치 불러옴
    x, y = seeker_pos
    # 어느 방향으로 움직여야 하는지에 대한 정보 가져옴
    move_dir = 0
    if forward_facing:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]
    return move_dir


def check_finsh():
    global forward_facing
    if seeker_pos == (0, 0) and forward_facing:
        forward_facing = False
    if seeker_pos == (n // 2, n // 2) and not forward_facing:
        forward_facing = True


def move_seeker():
    # 처음에는 정중앙에서 시작함
    # 달팽이처럼 움직임 -> 코드로 어떻게 구현?
    global seeker_pos
    x, y = seeker_pos
    # 상우하좌 순으로 넣어줌
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    # 방향
    move_dir = get_seeker_dir()
    # 술래를 한칸 움직인다.
    seeker_pos = (x + dxs[move_dir], y + dys[move_dir])
    # 만약 끝에 도달했다면 방향을 바꿔줘야
    check_finsh()


def get_score(t):
    # 술래의 턴에서 술래가 현재 바라보고 있는 방향을 기준으로 현재칸을 포함해 총 3칸 중
    # 도망자가 있다면 점수를 낸다.
    # 이때 나무가 있다면 해당 칸의 도망자는 패스.
    # 점수: t x 현재 턴에서 잡힌 도망자 수
    global total_score
    # 상우하좌 순으로
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    # 현재 술래의 위치, 술래의 방향 가져옴
    x, y = seeker_pos
    move_dir = get_seeker_dir()
    # 3칸을 바라본다.
    for dist in range(3):
        nx, ny = x + dist * dxs[move_dir], y + dist * dys[move_dir]
        # 격자를 벗어나지 않으며 나무가 없는 위치라면..
        if in_range(nx, ny) and not tree[nx][ny]:
            total_score += t * len(hiders[nx][ny])
            # 도망자 사라짐
            hiders[nx][ny] = []


# 게임 k번 반복
init_seeker_path()  # 편의상 술래 정보를 미리 계산

for t in range(1, k + 1):
    move_hider_all()
    move_seeker()
    get_score(t)
print(total_score)
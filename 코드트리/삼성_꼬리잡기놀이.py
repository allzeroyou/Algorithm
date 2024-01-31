# 격자 크기 n, 팀의 개수 m, 라운드 수 k
n, m, k = map(int, input().split())

# 0: 빈칸, 1: 머리사람, 2: 머리,꼬리 사람이 아닌 나머지, 3: 꼬리사람, 4: 이동선
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
# 점수의 총합
total_score = 0
# 사방탐색
dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 각 팀을 나눠줘야 함
def detect_team(hx, hy):  # (hx, hy)가 머리사람일때, 팀원들의 좌표 리스트를 돌려주는 함수
    teammates = [(hx, hy)]  # 머리 위치를 알고있음
    x, y = hx, hy  # 머리 위치부터 시작해서
    # 인접한 다른 칸으로 한칸씩 이동하며 꼬리를 찾는다.
    while a[x][y] != 3:
        for dx, dy in dirs:  # 이전에 있던 좌표로 가지 않아야 함.
            nx, ny = x + dx, y + dy
            # 격자를 벗어나지 않고
            if not in_range(nx, ny): continue
            if len(teammates) >= 2 and (nx, ny) == teammates[-2]: continue
            if a[x][y] == 1 and a[hx][hy] == 3: continue  # 머리-꼬리 이어져 있음
            if a[nx][ny] not in [2, 3]: continue
            x, y = nx, ny
            break
        teammates.append((x, y))
    return teammates


def detect_whole_teams():
    # 1. 모든 머리를 찾고
    teams = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:  # 머리사람이라면
                # 머리사람부터 이어진 팀을 찾을 수 있음.
                teams.append(detect_team(i, j))
    return teams


def move_one_team(teammates):  # teammates가 한 팀을 순서대로 쓴 경우
    # 1번을 기준으로 상,하,좌,우 탐색 -> 4번이 있는 방향으로 한 칸 이동
    x, y = teammates[0]
    for dx, dy in dirs:  # 이전에 있던 좌표로 가지 않아야 함.
        nx, ny = x + dx, y + dy
        # 격자를 벗어나지 않고
        if not in_range(nx, ny): continue
        if a[nx][ny] not in [3, 4]: continue
        break

        # 인접한 위치 중 4인 위치를 찾았다!
        # 모든 머리부터~꼬리까지 이동시킴
        ''' 꼬리사람이 아닌 나머지는 4를 한칸씩 뒤로 민다
        꼬리사람이라면 있었던 칸은 빈칸:4가 됨. 
        주의!!) 4가 없을 수도 있음. 즉 머리-꼬리가 이어진 경우가 반례임.'''
        new_coords = []

        for teammmate in teammates:
            cx, cy = teammmate  # 현재 위치
            # a[nx][ny], a[cx][cy] = a[cx][cy], a[nx][ny] # 바로 바꾸지 말고
            new_coords.append((nx, ny))
            nx, ny = cx, cy
            a[cx][cy] = 4

        for idx, (x, y) in enumerate(new_coords):
            if idx == 0:  # 머리가 새롭게 시작한 위치
                a[x][y] = 1
            elif idx == len(new_coords) - 1:  # 꼬리가 새롭게 시작한 위치
                a[x][y] = 3
            else:  # 몸이 새롭게 이동한 위치
                a[x][y] = 2


def move_whole_teams():
    # 1. 모든 팀을 찾고
    teams = detect_whole_teams()
    # 2.  한칸씩 이동시켜준다
    for teammates in teams:
        # print(teammates)
        move_one_team(teammates)


# 공을 조건에 맞게 던지고, 충돌 좌표를 return 하는 함수
def play_ball(round_num):  # 몇번째 라운드에 던져졌는지?
    # 공을 던지는 규칙성이 뭐지
    round_num %= n * 4  # 4n번째 라운드를 넘어가는 경우에는 다시 1번째 라운드의 방향으로
    if round_num < n:
        x1, y1 = round_num, 0  # 공 시작 위치(왼쪽)
        x2, y2 = round_num, n  # 공 끝나는 위치(오른쪽)
    elif round_num < n * 2:
        x1, y1 = n - 1, round_num - n  # 아래
        x2, y2 = -1, round_num - n  # 위
    elif round_num < n * 3:
        x1, y1 = (n * 3 - 1) - round_num, n - 1  # 오른쪽
        x2, y2 = (n * 3 - 1) - round_num, -1  # 왼쪽
    else:
        x1, y1 = 0, (4 * n - 1) - round_num  # 위
        x2, y2 = n - 1, (4 * n - 1) - round_num  # 아래

    # if 해당 선에 "사람"이 있고 and 최초에 만나는 사람 -> 점수 낸다.
    dx, dy = (x2 - x1) // n, (y2 - y1) // n
    x, y = x1, y1
    while (x, y) != (x2, y2):
        if a[x][y] not in [0, 4]:  # 1, 2, 3: 머리 or 몸 or 꼬리
            return (x, y)
        x, y = x + dx, y + dy

    return None


def change_head_tail(coord):
    # 머리, 꼬리 사람의 방향을 어떻게 바꾸지
    teams = detect_whole_teams()  # 모든 팀을 보면서
    for teammates in teams:  # 팀원들을 보면서
        for idx, teammate in enumerate(teammates, 1):  # 인덱스가 0이 아니라 1부터
            if teammate == coord:
                # 1. 머리와 꼬리를 반전
                x1, y1 = teammates[0]
                x2, y2 = teammates[-1]
                a[x1][y1], a[x2][y2] = a[x2][y2], a[x1][y1]
                # 2. 점수 반환
                # 점수는 머리 사람 기준으로 팀 내 k번째 사람 -> k^2 만큼 점수.
                return idx * idx


# 뼈대 구현
for round_num in range(k):
    # step1.  각 팀은 머리사람을 따라 한칸 이동
    move_whole_teams()
    coord = play_ball(round_num)  # 공 던지기
    if coord is None:
        continue

    total_score += change_head_tail(coord)

print(total_score)

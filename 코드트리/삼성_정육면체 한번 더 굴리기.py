# 컴파일 OK
# BUT NOT PASS
# 수정 필요
from collections import deque


def roll_right():
    new_arr = [0] * 6
    new_arr[0] = die[3]
    new_arr[1] = die[0]
    new_arr[2] = die[2]
    new_arr[3] = die[5]
    new_arr[4] = die[4]
    new_arr[5] = die[1]
    return new_arr


def roll_down():
    new_arr = [0] * 6
    new_arr[0] = die[2]
    new_arr[1] = die[1]
    new_arr[2] = die[5]
    new_arr[3] = die[3]
    new_arr[4] = die[0]
    new_arr[5] = die[4]
    return new_arr


def roll_left():
    new_arr = [0] * 6
    new_arr[0] = die[1]
    new_arr[1] = die[5]
    new_arr[2] = die[2]
    new_arr[3] = die[0]
    new_arr[4] = die[4]
    new_arr[5] = die[3]
    return new_arr


def roll_up():
    new_arr = [0] * 6
    new_arr[0] = die[4]
    new_arr[1] = die[1]
    new_arr[2] = die[0]
    new_arr[3] = die[3]
    new_arr[4] = die[5]
    new_arr[5] = die[2]
    return new_arr

#
# # 주사위 굴리기
# def move( dir, x, y):
#     global die
#
#
#     return dir, nx, ny, board
#
#
# # 점수 얻기
# def get_score(board, x, y):
#


# 실제 실행하는 부분
if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    die = [6, 4, 2, 3, 5, 1]

    x, y = 0, 0
    ans = 0
    dir = 0

    # row = deque([1, 3, 6, 4])  # 위-아래로 굴릴때 변하지 않는 부분
    # column = deque([1, 5, 6, 2])  # 양옆으로 굴릴때 변하지 않는 부분

    # 동남서북(시계 방향)
    dir_c = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 시뮬레이션
    for _ in range(m):

        nx, ny = x + dir_c[dir][0], y + dir_c[dir][1]
        if nx < 0 or n == nx or ny < 0 or n == ny:  # 벽에 부딪혔을때
            # 방향 전환
            dir = (dir + 2) % 4  # %4-> 3을 넘지 않음을 보장(모듈러 연산)
            # +2 : 동-서, 남-북 전환
            nx, ny = x + dir_c[dir][0], y + dir_c[dir][1]
        x,y=nx,ny
        if dir == 0:  # 동
            die = roll_right()
        elif dir == 1:  # 남
            die = roll_down()
        elif dir == 2:  # 서
            die = roll_left()
        elif dir == 3:  # 북
            die = roll_up()

        if die[0] > board[nx][ny]:  # 주사위 아랫면
            dir = (dir + 1) % 4  # 시계 90도 회전
        if die[0] < board[nx][ny]:
            dir = (dir + 3) % 4  # 반시계 90도 회전

        # 상하좌우
        # dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 방향
        start = board[nx][ny]  # 같은 숫자인지 확인용
        q = deque()  # 주사위
        # 방문처리
        visited_lst = {(nx, ny)}
        cnt = 1  # 같은 숫자 몇개인지 세기
        q.append([nx, ny])

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dir_c[i][0], y + dir_c[i][1]  # 상하좌우 탐색
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == start and (nx, ny) not in visited_lst:
                    cnt += 1
                    q.append([nx, ny])
                    visited_lst.add((nx, ny))
        ans += cnt*start

    print(ans)



# 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
# 최단거리 탐색
# BFS 사용
from collections import deque  # bfs-queue 이용

# 상대좌표 값
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [input() for _ in range(N)]  # 2차원 배열(보드판 처럼 생각) -> 문자열로 입력받음


def is_valid_coord(y, x):  # 어떤 좌표가 들어왔을때, 이 좌표가 유효범위 내에 있는가? : 범위체크 필수
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[False] * M for _ in range(N)]  # 방문 체크
    chk[0][0] = True  # zero base(0,0)
    q = deque()
    q.append((0, 0, 1))  # 좌표 + 누적 방문 횟수(처음 1부터 시작)
    while q:  # 반복문 돌기
        y, x, d = q.popleft()
        # 시각적으로 확인
        print(f'({y}, {x}), d: {d}')
        if y == N - 1 and x == M - 1:  # 도착점에 도달했다면 -> 함수 종료(몇칸 밟았는지 기록한 d 반환)
            return d

        nd = d + 1
        for k in range(4):  # 현재 위치에서 동,서,남,북 갈 수 있음
            ny = y + dy[k]  # next
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx] and board[ny][nx] == '1':  # '1'이 담긴 칸만 갈 수 있음
                # 1만 가능, 0은 빈칸(벽이라고 생각)
                chk[ny][nx] = True
                q.append((ny, nx, nd))  # 큐에 삽입(다음 좌표, 누적 방문 횟수)

    # 도달할 수 없는 경우(=다 돌았는데 도착점에 못 간 경우) -> -1을 출력하라 와 같이 문제에서 명시해줌.
    # return -1


print(bfs())

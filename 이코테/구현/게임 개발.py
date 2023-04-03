import sys

input = sys.stdin.readline

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 갈 곳 정함
# 2. 캐릭터의 바로 왼쪽 방향에 가보지 않은 칸 존재시 왼쪽 방향으로 회전 > 왼쪽으로 한칸 전진
# 왼쪽에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행. 1단계로 돌아감.
# 3. 만약 4 방향 모두 이미 가본칸, 바다 -> 바라보는 방향을 유지한채로 한칸 뒤로 가고 1단계로 돌아감.
# 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없을 때는 움직임 멈춤.

# 세로 n, 가로 m 입력받기
n, m = map(int, input().split())
# 게임 캐릭터가 있는 칸의 좌표(x,y)와 바라보는 방향 d 저장
x, y, d = map(int, input().split())
# 캐릭터가 방문한 칸의 수 cnt 생성
cnt = 0
# 2차원 배열 gameMap 생성.
gameMap = []
# 한줄씩 받아서 gameMap에 append 한다
for i in range(n):
    gameMap.append(list(map(int, input().split())))
# 북, 동, 남, 서 방향 정의
direction = [0, 1, 2, 3]

# 움직일 수 있는 방향벡터 정의
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 가본 칸은 바다로 변경. cnt 추가
gameMap[x][y] = 1
cnt += 1

# 시뮬레이션 시작
while True:
    # 4번 동안 반복
    i = 0
    while i < 4:
        nx = x + dx[d]
        ny = y + dy[d]
        # 바로 왼쪽 방향에 0이 있다면
        if gameMap[nx][ny] == 0:
            # d 왼쪽으로 회전.
            d = direction[direction.index(d) - 1]
            # 왼쪽 한칸 전진
            x, y = nx, ny
            # 가본칸이라면 바다로 변경, cnt 추가.
            gameMap[x][y] = 1
            cnt += 1
            i = 0
        # 바로 왼쪽 방향에 0이 없다면
        else:
            # d 왼쪽으로 회전.
            d = direction[direction.index(d) - 1]
            i += 1
    # 4번 반복후에도 갈 곳이 없다면 뒤로 한칸 후진.
    nx = x - dy[d]
    ny = y - dx[d]
    # 한칸 뒤로 가는게 가능하다면
    if gameMap[nx][ny] == 0:
        # 1단계로
        x, y = nx, ny
        # 가본칸은 바다로 변경, cnt 추가
        gameMap[x][y] = 1
        cnt += 1
    # 한칸 뒤로 갔더니 바다라면
    else:
        break
# 방문한 칸의 수?
print(cnt)

# 일련의 명령에 따라 개체를 차례대로 이동 -> 시뮬레이션
# 시뮬레이션 == 구현 == 완전탐색
# 코딩테스트: 1,2번 문제는 그리디, 구현임.
x, y = 1, 1
n = int(input())
plans = input().split()

# L, R, U, D에 따른 이동 방향.
dx = [0, 0, -1, 1]  # 행
dy = [-1, 1, 0, 0]  # 열
move_type = ['L', 'R', 'U', 'D']

# 이동계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동수행
    x, y = nx, ny

print(x, y)

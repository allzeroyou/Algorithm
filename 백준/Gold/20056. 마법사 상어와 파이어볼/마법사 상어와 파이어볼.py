# 삼성 구현 문제
# 조건에 맞춰 구현하면 됨
# 조건이 그림으로 안 주어져서 이해가 잘^^;;

# n: 격자, m: 파이어볼 개수, k:이동 명령 개수
n, m, k = map(int, input().split())

# r: 행,c: 열, m: 질량, s:속력, d:방향
fire_ball = []
for _ in range(m):
    r, c, w, s, d = list(map(int, input().split()))
    fire_ball.append([r - 1, c - 1, w, s, d])  # 0-based

board = [[[] for _ in range(n)] for _ in range(n)]

# 방향 벡터
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    # 파이어볼 이동
    while fire_ball:
        # 현재 파이어볼 상태
        cr, cc, cw, cs, cd = fire_ball.pop(0)
        # 다음 좌표로 이동
        nr = (cr + cs * dx[cd]) % n  # 1번-n번행 연결
        nc = (cc + cs * dy[cd]) % n  # 1번-n번행 연결
        board[nr][nc].append([cw, cs, cd])

    # 파이어볼이 2개 이상인지 체크
    for r in range(n):
        for c in range(n):
            # 2개 이상
            if len(board[r][c]) >= 2:
                # 하나로 합치고 4개로 나눈다
                sum_w, sum_s, cnt_odd, cnt_even, cnt_fireball = 0, 0, 0, 0, len(board[r][c])
                while board[r][c]:
                    w, s, d = board[r][c].pop(0)
                    sum_w += w
                    sum_s += s
                    if d % 2:  # 홀수이면
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                # 방향이 모두 홀수이거나 짝수일경우
                if cnt_odd == cnt_fireball or cnt_even == cnt_fireball:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                # 만약 질량이 0이면 소멸
                if sum_w // 5:  # 몫이 1이라면 질량은 5임.
                    for d in nd:
                        fire_ball.append([r, c, sum_w // 5, sum_s // cnt_fireball, d])
            # 1개인 경우
            if len(board[r][c]) == 1:
                fire_ball.append([r, c] + board[r][c].pop())
# print(fire_ball)
ans = 0
for fb in fire_ball:
    ans += fb[2]

print(ans)

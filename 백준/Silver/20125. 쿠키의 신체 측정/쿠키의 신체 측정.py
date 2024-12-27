# 쿠키의 신체 측정

# 한 변의 길이가 n인 정사각형
# 머리, 심장, 허리, 좌우 팔, 다리로 구성됨

# 출력
# 심장 위치
# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리 길이 반환

# sol
# 심장 위치는 머리(첫째줄) 바로 아래 칸임.
# 심장 왼쪽 칸부터~ _을 만나기 전까지 : 왼쪽 팔
# 심장 오른쪽 칸부터~ _을 만나기 전까지: 오른쪽 팔
# 심장 아래 칸부터~ _을 만나기 전까지: 허리
# 허리의 마지막 _을 만난 지점의 왼쪽 칸부터 아래 방향으로: 왼쪽 다리 # <-- '*_*'인 지점부터 ?
# 허리의 마지막 _을 만난 지점의 오른쪽 칸부터 아래 방향으로: 오른쪽 다리

n = int(input())
board = [input() for _ in range(n)]

# board 순회
flag = 0

for i in range(n):
    for j in range(n):
        # 변수 선언
        l_arm, r_arm, back, l_leg, r_leg = 0, 0, 0, 0, 0
        if board[i][j] == '*' and flag == 0:  # 머리일때
            # 해당 칸의 바로 아래칸이 심장 위치임
            print(i + 1 + 1, j + 1)  # idx to 1 based

            # 왼쪽 팔 길이 구하기
            for k in range(j):
                # print(f'k: {k}, arm: {l_arm}')
                if board[i + 1][k] == '*':  # 왼쪽 팔 길이 count
                    l_arm += 1

            # 오른쪽 팔 길이 구하기
            for h in range(j + 1, n):
                if board[i + 1][h] == '*':
                    r_arm += 1

            # 허리 구하기
            last = 0  # 허리 끝나는 지점
            for g in range(i + 2, n):
                if board[g][j] == '*':
                    back += 1
                else:
                    last = g
                    break
            # 왼쪽 다리
            for l in range(last, n):
                if board[l][j - 1] == '*':
                    l_leg += 1

            # 오른쪽 다리
            for r in range(last, n):
                if board[r][j + 1] == '*':
                    r_leg += 1

            print(l_arm, r_arm, back, l_leg, r_leg)
            flag = 1

            break

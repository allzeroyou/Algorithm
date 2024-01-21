# X가 안 들어있는 행, 열의 개수를 구하고, 둘 중 큰값이 경비원이 필요한 수

# 세로 n 가로 m
n, m = map(int, input().split())
# . 빈칸/ X 경비원
castle = [input() for x in range(n)]
# 행
rows = [0] * n
# 열
cols = [0] * m

# 맵을 좌표로 저장
for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            rows[i] += 1
            cols[j] += 1
# 행에 경비원 없는 경우
r_cnt = 0
for i in range(n):
    if rows[i] == 0:
        r_cnt += 1
# 열에 경비원 없는 경우
c_cnt = 0
for i in range(m):
    if cols[i] == 0:
        c_cnt += 1
print(max(r_cnt, c_cnt))

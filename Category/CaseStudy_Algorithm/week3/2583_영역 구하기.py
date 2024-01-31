dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# 2차원 배열을 저장하기 위해 문제의 데카르트 좌표계 -> 화면좌표계 사용
n, m, k = map(int, input().split())

board = [[True] * m for _ in range(n)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    for j in range(a, c):
        for i in range(b, d):
            board[i][j] = False  # 직사각형 부분은 False로


def is_valid_coord(y, x):  # 범위 체크
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    ret = 1  # 자기 자신 노드와 하위 서브트리의 노드 개수들 합
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and board[ny][nx]:
            board[ny][nx] = False
            ret += dfs(ny, nx)
    return ret

ans = []
for i in range(n):
    for j in range(m):
        if board[i][j]:
            board[i][j]=False
            ans.append(dfs(i, j))
print(len(ans))
print(*sorted(ans))

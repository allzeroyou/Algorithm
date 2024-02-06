# 재귀함수 실행횟수 늘리기
import sys

sys.setrecursionlimit(10 ** 8)
# 세로, 가로, 쓰레기 개수
n, m, k = map(int, input().split())
# 맵
board = [[0] * m for _ in range(n)]  # 1-based -> 0-based

# 음식물 좌표 입력받고, 맵에 표시하기
for _ in range(k):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1  # 1->0 based

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 쓰레기 크기
trash = 0
# 정답
ans = 0
# 방문체크
visited = [[0] * m for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def find_trash(x, y):
    global ans, trash
    # 1. 방문체크
    visited[x][y] = True
    # 쓰레기 사이즈 초기화
    trash = 1

    # 상하좌우 탐색하면서
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 범위 이내이고 쓰레기라면
        if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == 1:
            trash += find_trash(nx, ny)
    ans = max(ans, trash)
    return trash


for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            find_trash(i, j)

print(ans)

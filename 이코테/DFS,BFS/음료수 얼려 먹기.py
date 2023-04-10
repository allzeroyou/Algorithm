'''
최초 작성: 4/8
수정 필요.
'''

import sys
from collections import deque

#input = sys.stdin.readline

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# dy = (0, 1, 0, -1)
# dx = (1, 0, -1, 0)
#
# def bfs(x, y):
#     # 방문 배열
#     chk = [[False] * m for _ in range(n)]
#     # 방문 체크
#     chk[0][0] = True
#
#     q = deque()
#     # 시작 위치
#     q.append((0, 0))
#
#     while q:
#         # queue에서 하나 꺼내면 좌표 들어있음
#         x, y = q.popleft()
#         if y==n-1 and x==m-1: # 도착
#             return False
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 얼음 틀 안이면서 그 위치의 값이 0인 경우에만 큐에 넣음.
#             if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
#                 q.append((nx, ny))
#     return True
#
#
# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if bfs(i, j) == True:
#             cnt += 1
# print(cnt)


def ice_slush(x, y):
    # 범위를 벗어나는 경우 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 방문하지 않은 노드인 경우
    if board[x][y] == 0:
        # 방문 처리
        board[x][y] = 1

        ice_slush(x - 1, y)
        ice_slush(x + 1, y)
        ice_slush(x, y + 1)
        ice_slush(x, y - 1)
        return 1
    return 0


N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(list(map(int, input())))

cnt = 0
for i in range(N):
    for j in range(M):
        cnt += ice_slush(i, j)

print(cnt)

'''
4 5
00110
00011
11111
00000
'''

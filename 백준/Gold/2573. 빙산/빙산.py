# 덩어리 개수 세기
# 2개 이상일때까지 cnt 증가
# https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2573-%EB%B9%99%EC%82%B0-BFS


from collections import deque

# 행, 열
n, m = map(int, input().split())
# 맵
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 빙산 좌표(빙산이 있는 위치만 탐색)
ice = []

for i in range(n):
    for j in range(m):
        if board[i][j]:
            # 빙산 위치를 (i,j)형태로 저장
            ice.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 정답
ans = 0


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    # 주변 바다 개수 담는 리스트(빙산 녹이기 용)
    sea_list = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 인접한 바다 있는지 확인
                if not board[nx][ny]:  # 바다는 0
                    sea += 1
                elif board[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

        if sea > 0:
            sea_list.append((x, y, sea))
    # 빙산 녹이기
    for x, y, sea in sea_list:
        board[x][y] = max(0, board[x][y] - sea)  # 빙산은 0보다 더 줄어들지 않음

    return 1


while ice:
    # 중복 방문 안됨
    visited = [[0] * m for _ in range(n)]
    # 다 녹았다면 ice에서 제거
    del_list = []
    # 그룹 수 체크
    group = 0
    for i, j in ice:
        if board[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if board[i][j] == 0:  # 탐색 끝나면 바다가 된 빙산 체크
            del_list.append((i, j))

    if group >= 2:  # 빙산그룹이 2개 이상이면 시간 출력
        print(ans)
        break

    # 녹은 빙산은 탐색 할 필요없음 -> ice에서 제거
    ice = sorted(list(set(ice) - set(del_list)))
    ans += 1

if group < 2:
    print(0)

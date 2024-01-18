from collections import deque


def solution(maps):
    # 동서남북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 방문처리
    n = len(maps)  # row
    m = len(maps[0])  # col
    visited = [[False] * m for _ in range(n)]

    q = deque()
    q.append((0, 0))
    visited[0][0]=True

    # bfs
    # 큐가 빌때까지 반복
    while q:
        x, y = q.popleft()
        # 상하좌우 칸 확인하기
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx, ny))

                    maps[nx][ny] = maps[x][y] + 1  # 걸음 수 누적

    ans = maps[n - 1][m - 1]

    if ans == 1:  # 끝에 도달했을 경우 1이상이어야 하는데, 1인 경우는 도달 x
        ans = -1
    return ans

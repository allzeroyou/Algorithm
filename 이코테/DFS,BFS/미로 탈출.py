# (1,1)에서 출발.
# 미로의 출구는 n,m 위치에 존재
# 괴물:0, 없으면: 1
# 움직여야 하는 최소 칸의 개수?

# solution
# bfs
# bfs는 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드 탐색.
# 1,1 지점부터 bfs를 수행해 모든 노드의 값을 거리 정보로 넣으면 됨.
# 특정 노드 방문 -> 그 이전 노드의 거리에 1을 더한값을 리스트에 넣음

from collections import deque

n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
miro = []
for i in range(n):
    miro.append(list(map(int, input())))
# 이동할 4가지 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 벽인 경우 무시
            if miro[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지 최단 거리 반환
    return miro[n - 1][m - 1]


print(bfs(0, 0)) # 왜 처음 시작 위치인 1,1이 아니라 0,0이지?

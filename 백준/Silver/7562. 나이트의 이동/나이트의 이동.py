# 나이트 이동
# 나이트를 몇 번 움직이면 해당 칸으로 이동?
from collections import deque

# 문제를 보고 얻어야 하는 인사이트
# 1. 나이트가 이동할 수 있는 경로는 8가지 : [(x+-2, y+-1), (x+-1, y+-2)]
# 2. 최솟값 구하는 문제 -> 경로 탐색 -> 노드별로 최솟값 저장해야 함
# 3. 같은 좌표로 가면 안되니까 방문처리 저장(중복 x)

# 테스트 케이스 개수
tc = int(input())
# 나이트가 이동할 수 있는 경로
dx = [+1, -1, +1, -1, -2, -2, +2, +2]
dy = [+2, +2, -2, -2, +1, -1, +1, -1]


def bfs(x, y):
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()  # 가장 첫번째 요소 추출
        # 나이트 이동 경로 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안이고 처음 방문이라면
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = (visited[x][y] + 1)  # 방문 처리
                    q.append([nx, ny])
                else:  # 최솟값 업데이트
                    visited[nx][ny] = min(visited[nx][ny], (visited[x][y] + 1))  # 현재까지 오는데 걸린 횟수 + 1 vs 다음에 진행할 횟수


for t in range(tc):
    # 체스판 한 변의 길이
    n = int(input())
    # 나이트 현재 칸(start)
    sx, sy = map(int, input().split())
    # 나이트가 이동하려고 하는 칸(move)
    mx, my = map(int, input().split())

    # 중복 제거
    visited = [[0] * n for _ in range(n)]

    # 나이트가 어떻게 이동하는지(규칙 파악)
    if sx == mx and sy == my:
        print(0)
    # 최소 몇번 만에 이동?
    else:
        bfs(sx, sy)
        # 최소 칸 이동 횟수 출력
        print(visited[mx][my])

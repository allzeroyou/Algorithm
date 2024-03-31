# 25명의 학생들
# 5x5 정사각형 격자로 자리 배치
# a,b 학생 파로 나눠짐

# 칠공주 조건
# 1. 25명중 7명 선택
# 25c7=48만으로 시간 내 가능.
# 2. 7명은 가로, 세로로 인접해야 함.
# 가로, 세로 인접 --> 어떻게 표현?
# DFS
# 3. 7명중 적어도 4명 이상은 이다솜파
# 'S'의 개수 >= 4


# 뭔가 뱀 이동 같은 문제인데(길이 정해짐, 가로-세로 인접한 좌표로 이동 가능)
# 뱀 이동 어캐 풀었더라 ㅜㅜ


# 띄어쓰기 없이 붙어진 문자열을 하나씩 쪼개는법? --> 2차원 배열을 만들고, 인덱싱하여 저장하기 or input().strip()이용
import sys

input = sys.stdin.readline

board = [input().strip() for _ in range(5)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 중복 없음
visited = [[0] * 5 for _ in range(5)]

# 칠공주 조합 -> 중복 x
ans = set()


# 조건 2
# 각 칸에서 깊이 우선 탐색(dfs) 수행
# 탐색할 때 2가지 매개변수로 가짐: 지나온 노드 리스트, 지나온 노드 중 Y개수-> 3 초과시 유망하지 않으므로 더 이상 탐색 하지 않음.
def dfs(n_list, y_cnt):
    if y_cnt > 3:
        return
    if len(n_list) == 7:
        ans.add(tuple(sorted(n_list)))  # 집합: tuple 저장 가능(list 불가), 방문 순서가 달라도 구성원 7명이 같으면 하나의 경우의 수에 주의(정렬해줌)
        return

    for x, y in n_list:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = 1  # 중복 방지
                if board[nx][ny] == 'Y':
                    dfs(n_list + [(nx, ny)], y_cnt + 1)  # 지나온 노드에 현재 노드 추가, y+1
                else:
                    dfs(n_list + [(nx, ny)], y_cnt)  # 지나온 노드에 현재 노드만 추가
                visited[nx][ny] = 0  # 탐색을 위해 해지


for i in range(5):
    for j in range(5):
        visited[i][j] = 1
        if board[i][j] == 'Y':
            dfs([(i, j)], 1)
        else:
            dfs([(i, j)], 0)
print(len(ans))
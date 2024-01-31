# DFS는 그래프를 탐색하는 방법 중 하나로, 최대한 깊게 탐색하는 방법입니다.

def dfs(vertex):  # DFS 함수에서 첫 번째 인자인 vertex는 현재 위치
    for curr_v in range(1, n):  # 1번부터 정점의 개수인 n까지 포문을 돌아야 합니다.
        if graph[vertex][curr_v] and not visited[curr_v]:
            print(curr_v)
            visited[curr_v] = True
            dfs(curr_v)

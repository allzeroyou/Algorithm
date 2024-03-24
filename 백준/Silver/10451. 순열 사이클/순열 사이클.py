tc = int(input())


def dfs(v):
    visited[v] = True  # 현재 노드 방문 처리
    nv = graph[v]  # 인접 노드
    # 아직 방문하지 않은 노드라면 dfs 수향
    if not visited[nv]:
        dfs(nv)


for t in range(tc):
    n = int(input())

    # 순열
    graph = list(map(int, input().split()))
    graph.insert(0, 0)  # 1-based화
    # graph[0]=0 을 할 경우, 숫자들을 뒤로 밀지 않고, 0번째에 0 삽입
    visited = [False] * (n + 1)  # 1~n까지
    cycle = 0  # 순열 사이클 개수

    for i in range(1, n + 1):
        # 방문하지 않은 노드라면
        if not visited[i]:
            dfs(i)  # i 노드에서 dfs 호출
            cycle += 1
    print(cycle)

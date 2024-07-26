# 각 섬에서 최대 며칠씩 머무를 수 있는지를 배열에 오름차순으로 담아 return
# 지낼 수 있는 무인도가 없다면 -> -1를 배열에 담아 return

def solution(maps):
    answer = []
    
    # 무인도: 상하좌우로 연결된 땅
    dx=[0, 0, -1, 1]
    dy=[-1, 1, 0, 0]

    # 1차원 배열 -> 2차원 배열로!
    n = len(maps)
    m = len(maps[0]) # 직사각형
    
    visited = [[False]*m for _ in range(n)]
    
    # 탐색
    def dfs(x,y):
        # 1. 탐색 시작할 노드를 스택에 추가
        stack = [(x,y)]
        sum_food = 0    # 식량 합
        
        # 2. 스택이 빌 때까지 반복적으로 노드 처리
        while stack:
            # 스택에서 노드 꺼냄
            cx, cy = stack.pop()
            
            # 방문하지 않은 칸만 탐색
            if not visited[cx][cy]:
                visited[cx][cy]=True     # 방문 처리 후
                sum_food += int(maps[cx][cy]) # 식량에 더한다
                
                for i in range(4):
                    nx, ny = cx+dx[i], cy+dy[i]
                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]!='X':
                        stack.append((nx,ny))
        return sum_food
    
    # 지도 순회해서 섬 탐색
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                days = dfs(i,j)
                answer.append(days)
                
    # 예외 처리
    if not answer:
        return [-1]
    
    return sorted(answer)
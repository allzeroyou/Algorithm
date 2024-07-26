# dfs로 복습하고
# bfs로도 풀어보기

def solution(maps):
    answer = []
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 1차원 배열 -> 2차원 배열로
    n = len(maps)
    m = len(maps[0])
    # 방문처리용
    visited = [[False]*m for _ in range(n)]
    
    # 탐색 수행
    def dfs(x,y):
        # 1. 시작 노드를 스택에 추가
        stack = [(x,y)]
        # 식량 합
        sum_food = 0 
        
        while stack:
            cx, cy = stack.pop()
            
            # 2. 방문 체크
            if not visited[cx][cy]:
                visited[cx][cy] = True # 방문 체크 후
                sum_food += int(maps[cx][cy]) # 식량 합에 추가
                
                # 무인도 탐색
                for i in range(4):
                    nx, ny = cx+dx[i], cy+dy[i]
                    # 범위 내 체크
                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]!='X':
                        stack.append((nx,ny))
        return sum_food

    
    # 순회
    for i in range(n):
        for j in range(m):
            if maps[i][j]!='X' and not visited[i][j]:
                answer.append(dfs(i,j))
    # 예외 처리
    if not answer:
        return [-1]
 
    
    return sorted(answer)
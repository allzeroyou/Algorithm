# 정확성, 효율성 테스트 -> 재귀함수 주의, 시간복잡도 고려

# 알고리즘: bfs
# 2단계
# 1. 석유덩어리 크기 구하기
# 2. 어떤 컬럼에 꽂아야 최댓값?
from collections import deque 

def solution(land):
    row = len(land) # 세로(row)
    col = len(land[0]) # 가로(col)
    visited = [[False]*col for _ in range(row)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # 컬럼에 석유덩어리 크기 저장!!
    oil_size = dict()
    
    for i in range(row):
        for j in range(col):
            oil = 0
            
            if land[i][j]==1 and not visited[i][j]:
                q = deque([(i,j)]) # 큐에 삽입
                visited[i][j]=True # 방문처리
                # 석유덩어리 크기
                oil +=1
                # 현재 열 저장
                columns = set()
                
                while q:
                    x, y = q.popleft()
                    columns.add(y) # 현재 열 더하기!

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<row and 0<=ny<col and not visited[nx][ny] and land[nx][ny]==1:
                            q.append((nx,ny))
                            visited[nx][ny]=True
                            oil +=1
                            
                # 현재 석유덩어리 다 셈 -> 현재 석유덩어리가 속한 열에 크기 누적
                for column in columns:
                    if column not in oil_size:
                        oil_size[column]=oil
                    else:
                        oil_size[column]+=oil
    # {컬럼: 석유덩어리 크기}
    # 기 댓 값: { 1:8, 2:8, 3:8, 4:7, 5:7, 6:7, 7:7+2, 8:2, 9:2} )
    # 현재 출력: {0: 8, 1: 0, 2: 0, 3: 7, 4: 0, 5: 0, 6: 2, 7: 0}
    
    return max(oil_size.values())

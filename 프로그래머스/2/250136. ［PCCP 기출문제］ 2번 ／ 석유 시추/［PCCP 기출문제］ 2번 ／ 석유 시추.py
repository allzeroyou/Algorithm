# 1.석유 덩어리 크기 구하기
# 2.컬럼에 석유 덩어리 크기 저장하기(시추관 뚫기용)
from collections import deque

def solution(land):
    answer = 0
    
    n = len(land) # row
    m = len(land[0]) # col
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False]*m for _ in range(n)]

    # 컬럼에 저장용
    dic = {}
    
    # bfs
    for i in range(n):
        for j in range(m):
            # 석유덩어리 
            cnt = 0 # 초기화 반복문 안에서임 주의
            
            if land[i][j]==1 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j]=True
                cnt+=1
                # 현재 열 저장용(중복 방지)
                columns = set() 
                
                while q:
                    x,y = q.popleft()
                    columns.add(y) # 현재 열 더하기
                    
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0<=nx<n and 0<=ny<m and land[nx][ny]==1 and not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny]=True
                            cnt+=1
                # 큐가 끝났을때 석유덩어리 다 셈
                # 코드 헷갈림 주의
                for column in columns:
                    if column not in dic:
                        dic[column]=cnt
                    else:
                        dic[column]+=cnt
    
    print(dic)

    
    return max(dic.values())
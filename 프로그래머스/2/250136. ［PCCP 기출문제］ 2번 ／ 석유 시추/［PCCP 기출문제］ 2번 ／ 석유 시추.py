# 석유 시추
# 세로 n, 가로 m
# 시추관을 수직으로 "단 하나만" 뚫을 수 있음
# 가장 많은 석유를 뽑을 수 있는 시추관 위치?

# 상하좌우로 연결된 석유는 하나의 덩어리
# 석유 크기: 덩어리에 포함된 칸 수
from collections import deque

def solution(land):
    n = len(land) # 세로 col
    m = len(land[0]) # 가로 row
    
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 방문체크용    
    visited = [ [False]*m for i in range(n)]
    # 각 석유덩어리에 번호 붙이기
    num = 2 # 1은 석유가 있는 칸으로 이미 번호 붙여짐
    # key=석유덩어리번호(num): value=크기
    dic = dict()
    
    # 1. bfs로 석유덩어리 번호 붙이고, 크기 측정
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]: # 석유 땅
                # bfs 시작
                q = deque([(i,j)])
                visited[i][j]=True
                size = 0 # 현재 석유 덩어리 크기 초기화
                
                while q:
                    x,y = q.popleft()
                    land[x][y]= num # 해당 위치를 현재 석유덩어리 번호로 변경
                    size += 1 # 석유덩어리 크기 증가
                    
                    for k in range(4): # i 중복 주의 ->바깥쪽 루프에서 i사용중이므로 다른 변수명 써야함
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<m and land[nx][ny]==1 and not visited[nx][ny]:
                            visited[nx][ny]=True # 방문처리
                            q.append((nx,ny)) # 큐 삽입
                dic[num]=size # 석유 덩어리 번호에 해당하는 크기 저장
                num += 1 # 다음 석유 덩어리 탐색을 위해 번호 증가
                
    # 2. 시추관 설치해 얻을 수 있는 최대 석유량 구하기
    answer = 0 # 최대 석유량
    for i in range(m): # 모든 열에 대해 탐색
        oil_num = set() # 현재 열에서 만난 석유덩어리 번호 저장
        for j in range(n): # 현재 열에서의 모든 행 순회
            if land[j][i] > 1: # 석유 땅이라면
                oil_num.add(land[j][i]) # 해당칸의 석유 번호 저장
                
        answer = max(answer, sum([dic[x] for x in oil_num])) # 최대 석유량
            
    return answer
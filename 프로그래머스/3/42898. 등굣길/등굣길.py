# 가로 m x 세로 n 크기 맵
# 물에 잠긴 지역 좌표 2차원 배열: puddles(1 based)
# 오른쪽, 아래쪽으로만 움직여 최단거리 개수 -> 1,000,000,007으로 나눈 나머지 return
# bfs -> 모든 경로 탐색 하므로 비효율적
# 최단거리 경로의 "개수" 이므로 dp로 해결!
# 경로 개수를 dp 테이블에 저장해 점진적으로 값 계산
# 점화식
# dp[i][j] = dp[i-1][j]+dp[i][j-1] # 웅덩이 아님
# dp[i][j]= 0 # 웅덩이 

def solution(m, n, puddles):
    answer = 0
    MOD = 1_000_000_007
    
    dp = [[0]*(m+1) for _ in range(n+1)] # 1based
    # 시작점 초기화
    dp[1][1] = 1
    # 웅덩이 설정
    for x, y in puddles:
        dp[y][x] = -1 # y,x 순서 주의
        
    # dp 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j]== -1: # 웅덩이
                dp[i][j]=0
            elif i==1 and j==1:
                continue
            else:
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%MOD

    return dp[n][m]

def solution(triangle):
    answer = 0
    
    dp = triangle
    
    for i in range(1, len(dp)):
        for j in range(i+1): # 깊이 2부터 count
            if(j==0):
                dp[i][j] += dp[i-1][j]
            elif (j==i):
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
        
    
    return max(dp[len(dp)-1]) # 맨 마지막 줄에서 최댓값
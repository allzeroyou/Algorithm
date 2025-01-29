import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        
        // 삼각형 행
        int n = triangle.length;
        
        // 1. dp 테이블 정의 - 0-based
        int[][] dp = new int[n][n];
        
        // 3. 초기값 설정
        dp[0][0]=triangle[0][0];
        
        
        // 2. 점화식 도출
       for(int i=1; i<n; i++){
           for(int j=0; j<=i; j++){
               if(j==0){ // 왼쪽 끝: 바로 위의 값에서 내려와야 함
                    dp[i][j]=triangle[i][j] + dp[i-1][j];
               }
               else if(j==i){ // 오른쪽 끝: 왼쪽 위에서 내려와야 함
                    dp[i][j]=triangle[i][j] + dp[i-1][j-1];
               }
               else{
                   dp[i][j]=triangle[i][j] + Math.max(dp[i-1][j], dp[i-1][j-1]);
               }
           }
       }

        // 4. 정답 출력(최댓값 찾기)
        for(int i=0; i<n; i++){
            answer = Math.max(answer, dp[n-1][i]);
        }
        
        return answer;
    }
}
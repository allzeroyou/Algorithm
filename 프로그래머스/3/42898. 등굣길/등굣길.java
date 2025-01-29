import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        // overflow 방지
        int MOD= 1000000007;
        
        // 1. 테이블 정의: 1 based
        int[][] dp = new int[n+1][m+1];
        
        // 3. 초기값 설정
        dp[1][1]=1;

        // System.out.println(Arrays.deepToString(dp));
        
        // puddles를 조건식으로 처리하기 위해 boolean값으로 바꾼다.
        boolean[][] isPu = new boolean[n+1][m+1];
        
        for(int[] puddle: puddles){
            isPu[puddle[1]][puddle[0]]=true; // puddles는 x,y 형식이므로 순서주의
        }
            
        // 2. 점화식 도출
        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                if(isPu[i][j]){
                    dp[i][j]=0; // 물 웅덩이라면 경로 0
                }
                else{
                    // 오른쪽으로 간 경우(=왼쪽에서 온 경우)
                    dp[i][j]=(dp[i][j]+ dp[i-1][j])%MOD;
                    // 아래로 간 경우(=위쪽에서 온 경우)
                    dp[i][j]=(dp[i][j]+ dp[i][j-1])%MOD;
                        
                }
            }
        }
        
        return dp[n][m];
    }
}
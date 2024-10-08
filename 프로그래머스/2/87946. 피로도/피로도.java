import java.util.*;

class Solution {
    static int answer;
    static boolean[] visited;
    
    // 현재피로도:k, 소모 피로도: dundeons
    public int solution(int k, int[][] dungeons) {
        answer = 0;
        // 변수 세팅
        visited = new boolean[dungeons.length];
        dfs(k, dungeons, 0);
        
        
        return answer;
    }
    public void dfs(int k, int[][] dungeons, int cnt){
        for(int i=0; i<dungeons.length; i++){
            if(!visited[i] && dungeons[i][0] <= k){
                visited[i]=true;
                dfs(k- dungeons[i][1], dungeons, cnt+1);
                visited[i]=false;
            }
        }
        answer = Math.max(answer, cnt);
    }
}
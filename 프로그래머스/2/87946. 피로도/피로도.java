import java.util.*;

class Solution {
    private int maxExplored;
    
    public int solution(int k, int[][] dungeons) {
        int answer = -1;
        
        boolean[] visited = new boolean[dungeons.length]; // 방문 배열
        recur(k, dungeons, visited, 0);
        
        return maxExplored;
    }
    
    private void recur(int k, int[][] dungeons, boolean[] visited, int cnt ){
        
        // 탐험
        for(int i=0; i<dungeons.length; i++){
            // 방문 x && 현재 피로도 >= 최소 피로도
            if(!visited[i] && k>= dungeons[i][0]){
                // 방문 체크
                visited[i]=true;
                // 현재 피로도, 방문체크, 탐험횟수+1 갱신한 재귀 함수 실행
                recur(k-dungeons[i][1], dungeons, visited,cnt+1 );
                // 실행 후 방문체크 되돌려 다른 순서 탐험 가능하도록.
                visited[i]=false;
            }
            // 최댓값 구하기
            maxExplored = Math.max(cnt, maxExplored);
        }
    }
}
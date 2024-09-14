// 피로도 시스템(0 이상 정수)
// 일정 피로도 사용해 던전 탐험
// 탐험 시작에 필요: 최소 필요 피로도(조건)
// 던전 탐험을 끝낼 때 소모: 소모 피로도(감소)
// 던전을 최대한 많이 탐험할 수 있는 최대 던전 수?

class Solution {
    private int maxExplored=0;
    private boolean[] visited;
    
    public int solution(int k, int[][] dungeons) { //k: 현재 피로도, dungeons: 던전별 최소, 소모 피로도
        int answer = -1;
        visited = new boolean[dungeons.length];
        makePermu(k, dungeons, 0);
        
        return maxExplored;
    }
    
    // 던전을 탐험하는 모든 가능한 순서 고려: 순열
    public void makePermu(int fatigue, int[][] dungeons, int cnt){
        maxExplored=Math.max(maxExplored, cnt); // 최댓값 갱신
        

        for(int i =0; i<dungeons.length; i++){
            if(!visited[i] && fatigue >= dungeons[i][0]){
                visited[i]=true;
                makePermu(fatigue-dungeons[i][1], dungeons, cnt+1);
                visited[i]=false;
            }
        }
    }
}
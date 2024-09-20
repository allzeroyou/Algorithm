// 네트워크: 연결된 형태
// a-b, b-c -> a-c
// a,b,c는 모두 같은 네트워크
// 2차원 배열에 약한듯..
// computers[i][j]=1 는 연결된거

class Solution {
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        // 이미 방문한 컴퓨터는 다시 방문 x
        visited = new boolean[n];
        int answer = 0;
        
        for(int i=0; i<n; i++){
            if(!visited[i]){
                dfs(i, computers); 
                answer++; // 네트워크 개수 증가
            }
        }
        return answer;
    }
    public void dfs(int v, int[][] computers){
        // 방문체크
        visited[v]=true;
        
        for(int i=0; i<computers.length; i++){
            // 연결되어있고 방문하지 않았다면
            if(computers[v][i]==1 && !visited[i]){
                dfs(i, computers);
            }
        }
    }
}
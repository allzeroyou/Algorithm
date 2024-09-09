// 네트워크: 컴퓨터간 정보 교환할 수 있도록 연결된 형태
// 컴퓨터 A, B가 직접적 연결
// 컴퓨터 B, C가 직접적 연결 -> 컴퓨터 A,C도 간접적 연결
// 컴퓨터 A,B,C는 모두 같은 네트워크 상에 위치함

// 컴퓨터 개수: n, 정보가 담긴 2차원 배열: computers
// 네트워크 개수 return
// i번, j번 컴퓨터 연결: computers[i][j]=1
// 본인: computers[i][i]=1

// == 연결요소 개수 찾기
// 모든 컴퓨터를 돌면서 방문 안했다면 해당 컴퓨터로부터 연결된 컴퓨터 찾아서 cnt +1

class Solution {
    boolean[] visited; // 방문 배열
    public int solution(int n, int[][] computers) {
        int answer = 0; // 네트워크 수
        visited = new boolean[n];
        
        for(int i =0; i<n; i++){
                if(!visited[i]){ // 방문 체크
                    dfs(i, computers);
                    answer ++; 
                }
            }
        return answer;
    }
        
    
    void dfs(int v, int[][] computers){
        visited[v]=true;
        
        for(int i=0; i<computers.length; i++){
            if(computers[v][i]==1 && !visited[i]){ // 현재 행의 각 열 순회
                dfs(i, computers);
                
            }
        }
    }
}



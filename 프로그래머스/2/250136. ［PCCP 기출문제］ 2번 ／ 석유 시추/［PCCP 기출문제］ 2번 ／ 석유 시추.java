// 상, 하, 좌, 우로 연결된 석유 덩어리 개수를 구하기 위한 전형적인 BFS
// 다만 하나의 열 전체를 관통하는 시추관을 지나가는 석유 덩어리 집합의 개수를 시추관 위치별 저장
// -> 가장 많은 석유량을 반환하는 알고리즘 추가 요구
// BFS 알고리즘을 통해 서로 연결된 석유 덩어리들을 확인하면서 석유 덩어리의 열 위치를 저장
// 해당 석유 덩어리 집합이 추출될 수 있는 시추관의 위치와 동일하기 때문
// 주의할 점은 같은 열에 있는 석유 덩어리들은 같은 위치의 시추관에 의해 추출되기 때문에
// 중복 저장을 피하기 위해 Set 자료형에 시추관의 위치에 저장

// 마지막으로 각 석유 덩어리 집합의 석유 덩어리 개수를 확인할 때마다 시추관 위치별 석유 덩어리 집합의 개수
// 계속해서 추가해 주어 가장 많은 석유량을 구했습니다.
import java.util.*;

class Solution {
    static int n,m; // 가로, 세로 길이
    static int[] oil; // 시추관 위치별 석유량
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    
    public int solution(int[][] land) {
        int answer = 0;
        n = land.length;
        m = land[0].length;
        oil = new int[m];
        
        boolean[][] visited = new boolean[n][m];
        
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(land[i][j]==1 && visited[i][j]==false ) // 1: 석유 땅
                {
                     bfs(land, visited, i, j);
                } 
            }
        }        
        // answer
        answer = Arrays.stream(oil).max().getAsInt();        
        return answer;
    }
    
    // bfs
    public void bfs(int[][] land, boolean[][] visited, int x, int y){
        Queue<int[]>q = new LinkedList<>();
        q.add(new int[] {x,y});
        visited[x][y]=true;
        
        // 석유 덩어리 개수
        int cnt = 1;  // 처음 위치도 석유 덩어리에 포함
        // 석유 덩어리 열 위치 저장
        Set<Integer> set = new HashSet<>();
        set.add(y);

        while(!q.isEmpty()){
            int[] now = q.poll();
            int curX = now[0];
            int curY = now[1];
            
            for(int i =0; i<4; i++){
                int nx = curX+dx[i];
                int ny = curY+dy[i];
                // 범위 체크
                if(isRange(nx,ny)&&land[nx][ny]==1 && !visited[nx][ny] ) // 1: 석유 땅
                {
                    q.add(new int[] {nx,ny});
                    visited[nx][ny]=true;
                    cnt += 1; // 석유 추가
                    set.add(ny); // 열 위치 저장
                }
            }
        }
        // 해당 석유를 시추관 위치에 저장
        for(int idx: set){
            oil[idx]+=cnt;
        }
    }
    // 범위체크용 함수
    public boolean isRange(int x, int y){
        return x>=0 && x<n && y>=0 && y<m;
    }
}
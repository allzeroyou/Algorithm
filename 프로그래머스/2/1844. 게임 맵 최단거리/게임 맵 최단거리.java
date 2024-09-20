// 5x5 크기 맵, 동/서/남/북 이동, 게임 맵 벗어난 길은 불가
// 상대팀 진영에 도착할 수 없을 땐 -1 반환
// 0: 벽, 1: 벽x
// 최단거리-bfs
import java.util.*;

class Solution {
    static int[]  dx = {-1, 0, 1, 0};
    static int[]  dy = {0, 1, 0, -1};
    static boolean[][] visited;
    
    public int solution(int[][] maps) {
        int answer = 0;
        int n = maps.length; 
        int m = maps[0].length;
        
        // bfs-queue 사용
        Queue<int[]> qu = new LinkedList<>();
        visited= new boolean[n][m]; // 해당 위치 방문 체크
        
        qu.offer(new int[]{0,0,1}); // x,y,현재까지 거리
        visited[0][0] = true;
        
        while(!qu.isEmpty()){
            int[] cur = qu.poll();
            int x = cur[0];
            int y = cur[1];
            int d = cur[2];
            // 도착했다면 거리 반환
            if(x==n-1 && y==m-1){
                return d;
            }
            for(int i=0; i<4; i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                // 범위 체크, 방문 체크, 벽 x
                if(nx>=0 && nx<n && ny>=0 && ny<m && !visited[nx][ny] && maps[nx][ny]==1){
                    qu.offer(new int[]{nx, ny, d+1});
                    visited[nx][ny]=true;
                }
            }
        }
        
        return -1;
    }
}
// 게임: 두 팀으로 나눠 진행
// 상대팀 진영에 최대한 빨리 도착하는게 유리 -> 최단거리(bfs)

// 5x5 맵, 캐릭터(행:1, 열:1)에 위치
// 상대 진영: 행:n, 열:m에 위치
// 방향: 동서남북, 한칸씩 이동, 맵 벗어나면 x
// 0: 벽, 1: 벽x
// 상대 진영에 도착 x: -1 return
import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        // 방문배열
        boolean[][] visited = new boolean[n][m];
        
        // bfs; Queue
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0,0}); // 시작점 추가
        visited[0][0]=true;
        
        // 거리 배열 초기화; 각 위치까지 거리 저장
        int[][] dis = new int[n][m];
        dis[0][0] = 1;
        
        // bfs 구현
        while(!queue.isEmpty()){
            int[] cur = queue.poll(); //FIFO
            int x= cur[0];
            int y= cur[1];
            for(int i=0; i<4; i++){
                int nx=x+dx[i];
                int ny=y+dy[i];
                if(nx >= 0 && nx<n && ny >= 0 && ny<m && maps[nx][ny]==1 && !visited[nx][ny]){
                    queue.offer(new int[]{nx,ny}); // 큐에 삽입
                    visited[nx][ny]=true; // 방문 체크
                    dis[nx][ny]=dis[x][y]+1; // 지금까지 온 길 +1       
                }
            }
        }
        // 상대팀 진영에 도착못했다면(0으로 초기화):-1반환, 아니면 거리 반환
        return dis[n-1][m-1] == 0 ? -1: dis[n-1][m-1];
    }
}
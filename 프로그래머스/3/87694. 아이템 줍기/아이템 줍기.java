// 다각형 모양 지형 -> 아이템을 줍기 위해 이동
// 각 변이 x,y축과 평행한 직사각형이 겹쳐진 형태로 표현
// 캐릭터는 다각형의 둘레(굵은 선)을 따라 이동
// 직사각형을 겹친 후 중앙에 빈 공간 -> 다각형의 가장 바깥쪽 테두리가 이동경로임!

// 캐릭터가 아이템을 줍기 위해 이동하는 가장 짧은 거리?
// rectangle: 지형 나타내는 직사각형이 담긴 2차원 배열
// characterX, characterY: 초기 캐릭터 위치
// itemX, itemY: 아이템 위치
import java.util.*;

class Solution {
    // 사각형 객체
    static class Rect{
        int x1, x2, y1, y2;
        public Rect(int x1, int y1, int x2, int y2){
            this.x1 = x1;
            this.y1= y1;
            this.x2= x2;
            this.y2= y2;
        }
    }

    static int[] dx= {-1, 1,0,0};
    static int[] dy= {0,0,-1,1};
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        // 길이 2배: 좌표상 이동이므로 안으로 들어간 부분 체크용
        int[][] map = new int[101][101];
        // 사각형 리스트에 추가
        for(int[] rect: rectangle){
            // 시작점
            int sx = rect[0]*2, sy = rect[1]*2;
            // 끝점
            int fx = rect[2]*2, fy = rect[3]*2;      
            // 사각형 내부 및 경계를 -1로 채워서 사각형 그리기(x,y 좌표 순서 다름 주의)
            for(int y=sy; y<=fy; y++){
              for (int x = sx; x <= fx; x++) {
                // 현재 위치가 테두리인 경우
                if (x == sx || x == fx || y == sy || y == fy) {
                    // 이전에 내부로 표시되지 않은 경우에만 테두리로 표시
                    if (map[y][x] != 2) map[y][x] = 1;
                } else {
                    // 내부는 2로 표시
                    map[y][x] = 2;
                }
            }
        }
    }
        answer = bfs(map, characterX*2, characterY*2, itemX*2, itemY*2);
        return answer;
    }
    public int bfs(int[][] map, int cx, int cy, int ix, int iy){
        Queue<int[]> q = new LinkedList<>();
        // 시작점, 이동횟수(거리) 저장
        q.add(new int[] {cx, cy, 1});
        // 방문체크
        map[cy][cx]=3;
        
        // 순회
        while(!q.isEmpty()){
            int[] p = q.poll();
            int px=p[0], py=p[1], move=p[2];
            
            // 타겟(목표지점)도달시 종료
            if(px==ix&& py==iy){
                return (move/2); // 2배로 늘렸으니 2로 나눔
            }
            for(int i=0; i<4; i++){
                int nx = px+ dx[i];
                int ny = py+ dy[i];
                // 조건 검사
                if(nx>=0 && nx<=100 && ny>=0 && ny<=100 && map[ny][nx] ==1){ // 테두리일 경우
                    map[ny][nx] = 3; // 방문표시
                    q.add(new int[]{nx, ny, move+1});
                }
            }
        }
        // 못 가는 경우 -1 반환
        return -1;
    }
}
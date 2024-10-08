import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        List<Point>points = findIntersections(line);
        //최대,최소 좌표 찾기
        long minX = Long.MAX_VALUE, minY = Long.MAX_VALUE;
        long maxX = Long.MIN_VALUE, maxY = Long.MIN_VALUE;
        
        for(Point p:points){
            minX = Math.min(minX, p.x);
            minY = Math.min(minY, p.y);
            maxX = Math.max(maxX, p.x);
            maxY = Math.max(maxY, p.y);
        }
        // 2D 배열 생성 및 별 그리기
        int width = (int)(maxX - minX + 1);
        int height = (int)(maxY - minY + 1);
        char[][] map = new char[height][width];
        
        for (int i = 0; i < height; i++) {
            Arrays.fill(map[i], '.');
        }
        
        for (Point p : points) {
            int x = (int)(p.x - minX);
            int y = (int)(maxY - p.y);
            map[y][x] = '*';
        }
                
        // 결과 변환
        String[] result = new String[height];
        for (int i = 0; i < height; i++) {
            result[i] = new String(map[i]);
        }
        
        return result;
    }
    // 교점 표현하기 위한 Point 클래스 정의
    class Point{
        long x,y; // 좌표값
        Point(long x, long y){
            this.x=x;
            this.y=y;
        }
    }
    // 1. 직선의 교점 찾기
    List<Point> findIntersections(int[][] line){
        List<Point> points = new ArrayList<>(); // 찾은 교점 저장할 리스트
        // 모든 직선쌍 순회
        for(int i=0; i<line.length; i++){
            for(int j=i+1; j<line.length; j++){
                // 첫번째 직선의 계수 추출: Ax + By + E = 0
                long a = line[i][0], b = line[i][1], e = line[i][2];
                // 두번째 직선의 계수 추출: Cx + Dy + F = 0
                long c = line[j][0], d = line[j][1], f = line[j][2];
                
                // 두 직선의 평행 여부 확인을 위한 분모 계산
                long res = a*d - b*c;
                if(res==0) continue; // 평행 or 일치 -> 패스
                
                // 교점의 x,y 좌표 계산
                double x = (double)(b*f - e*d) / res;
                double y = (double)(e*c - a*f) / res;
                
                // 교점의 좌표가 정수인 경우에만 저장
                if(x%1 ==0 && y%1 ==0){
                    points.add(new Point((long)x, (long)y));
                }
            }
        }
        return points;
    }

        
}

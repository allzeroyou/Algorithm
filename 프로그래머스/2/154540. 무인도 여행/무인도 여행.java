// 'X': 바다, 1~9: 무인도-식량
// 상,하,좌,우로 연결된 땅은 하나의 무인도
// 각 칸 숫자 -> 식량/ 상,하,좌,우로 연결되는 칸에 적힌 숫자를 모두 합한 값=>해당 무인도에서 최대 며칠 머물 수 있는지?
// 각 섬에서 최대 며칠씩 머물 수 있는지 배열에 오름차순으로 담아 return
// 만약 지낼 수 있는 무인도 x -> -1 반환

import java.util.*;
class Solution {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static boolean[][] visited;
    static int food = 0;

    public int[] solution(String[] maps) {
        int[] answer = {};
        // 방문 체크
        visited = new boolean[maps.length][maps[0].length()]; // 2차원 배열
        // 결과 저장용 리스트
        List<Integer> res = new ArrayList<>(); 
        
        for(int i=0; i<maps.length; i++){
            for(int j=0; j<maps[0].length(); j++){
                if(!visited[i][j] && maps[i].charAt(j)!='X'){ // 방문 x
                    food=0; // 식량 초기화
                    dfs(maps, visited, i, j);
                    res.add(food);
                }
            }
        }
        if(res.isEmpty()){
            return new int[]{-1};
        }
        Collections.sort(res);
        // List -> Array로 변환
        return res.stream().mapToInt(i->i).toArray();
    }
    public void dfs(String[] maps, boolean[][] visited, int x, int y ){
        visited[x][y]=true; // 방문 처리
        // 문자 -> 숫자
        food += maps[x].charAt(y)-'0'; // 해당 좌표값의 숫자를 더하기
        for(int i=0; i<4; i++){
            int nx = x+dx[i];
            int ny = y+dy[i];
            // 범위 안, 방문 x, X가 아니라면
            if(nx>=0 && nx<maps.length && ny>=0 && ny<maps[0].length() && !visited[nx][ny] && maps[nx].charAt(ny)!='X'){
                dfs(maps, visited, nx, ny);
            }
        }
    }
}
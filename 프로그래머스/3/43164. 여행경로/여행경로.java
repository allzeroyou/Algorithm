// 완전탐색 -> 모든 가능한 경로 구하기
// 정렬(알파벳 순서가 앞서는 경로)
// 가장 첫번째 요소 리턴
import java.util.*;

class Solution {
    static boolean[] visited; // 방문 체크
    static List<String>result = new ArrayList<>();
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        // 변수세팅
        visited = new boolean[tickets.length];
        
        // 완탐 및 정렬
        dfs(tickets, "ICN", "ICN", 0);
        
        Collections.sort(result);
        
        String[] ans = result.get(0).split(" ");
        
        return ans;
    }
    public void dfs(String[][] tickets, String start, String route, int idx){
        // 종료 조건
        if(idx==tickets.length){
            result.add(route);
            return;
        }
        // 백트래킹
        for(int i=0; i<tickets.length; i++){
            if(tickets[i][0].equals(start) && !visited[i]){
                visited[i]=true;
                dfs(tickets, tickets[i][1],route+" "+tickets[i][1], idx+1 );
                visited[i]=false;
            }
        }
        return;
    }
}
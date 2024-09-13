// 주어진 항공권을 모두 이용해 여행경로 짜기
// "ICN"에서 출발
// tickets: 항공권 정보 담긴 2차원 배열
// 방문하는 공항 경로를 배열로 담아 return

// 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 return
// [a,b]->[b,a] 이렇게 이어져야 함.
import java.util.*;

class Solution {
    static Queue<String> pq = new PriorityQueue<>(); // 문자열 오름차순 정렬용
    static boolean[] visited; // 방문 배열
    
    public String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length];
        dfs(tickets, "ICN", 0, "ICN"); // 처음시작은 ICN
        // pq에 들어온 값 중 첫번째 값이 최적임
        String[] answer = pq.peek().split(",");
        
        return answer;
    }
    public void dfs(String[][] tickets, String curCity, int cnt, String path){
        // 재귀 종료 조건
        if(cnt==tickets.length){
            // pq에 전체 여행 경로 추가
            pq.add(path);
            return;
        }
        for(int i=0; i<tickets.length; i++){
            if(!visited[i] && curCity.equals(tickets[i][0])){ // 현재 도시가 다음 여행 경로의 도착지
                // 방문체크
                visited[i]=true;
                // 그다음 경로 탐색
                dfs(tickets, tickets[i][1], cnt+1, path+","+tickets[i][1]);
                // 모든 배열 순회시 방문배열 체크 초기화(백트래킹)
                visited[i]=false;
            }
        }
    }
}
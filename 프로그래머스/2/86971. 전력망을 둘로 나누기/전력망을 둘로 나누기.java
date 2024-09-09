// 전선을 하나씩 제거 -> 네트워크 두개로 나누기
// 각 부분의 송전탑 개수 계산
// 두 부분의 송전탑 개수 차이 계산, 최솟값 리턴

import java.util.*;
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n; // 최대로 가능한 차이값으로 설정

        // 인접리스트로 그래프 표현
        List<List<Integer>>graph = new ArrayList<>();
        for(int i=0; i<=n; i++){
            graph.add(new ArrayList<>());
        }
        // 그래프 구성
        for(int[] wire: wires){
            // 연결 정보 추가-양방향
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
            
        }
        // 각 전선을 끊으며 최소 차이 계산
        for(int[] wire: wires){
            graph.get(wire[0]).remove(Integer.valueOf(wire[1]));
            graph.get(wire[1]).remove(Integer.valueOf(wire[0]));
            boolean[] visited = new boolean[n+1]; // 각 DFS 호출마다 새로운 visited 배열 생성
            int cnt = dfs(1, graph, visited); // 1번에서 시작
            int diff = Math.abs(cnt - (n-cnt)); // 차이
            answer = Math.min(answer, diff);
            // 끊었던 전선 복구
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }
        return answer;
    }
    // dfs로 연결된 노드수 계산
    public int dfs(int node, List<List<Integer>> graph, boolean[] visited){
        visited[node]=true;
        int cnt = 1;
        for(int nei: graph.get(node)){
            if(!visited[nei]){
                cnt += dfs(nei, graph, visited);
            }
        }
        return cnt;
    }
}
import java.util.*;

class Solution {
    // 1. 인접리스트 생성
    HashMap<Integer, List<Integer>> map = new HashMap<>();
    
    public int solution(int n, int[][] wires) {
        int answer = -1;
        
        for(int[] wire : wires){
            map.putIfAbsent(wire[0], new ArrayList<>());
            map.putIfAbsent(wire[1], new ArrayList<>());
            map.get(wire[0]).add(wire[1]);
            map.get(wire[1]).add(wire[0]); // 양방향 그래프
        }
            
        // 2. 각 전선을 하나씩 제거해보고 두 전력망 크기 차이 계산
        int minDiff = n; // 크기 차이 최솟값        
        
        for(int[] wire: wires){
            // 전선 제거
            map.get(wire[0]).remove(Integer.valueOf(wire[1]));
            map.get(wire[1]).remove(Integer.valueOf(wire[0]));
            
            // bfs로 연결 개수 계산
            int size = bfs(wire[0], n);
            
            // 차이 계산
            int diff = Math.abs(n- 2*size); // |(n-size)-size|이므로
            minDiff = Math.min(diff, minDiff);
            
            // 전선 복구
            map.get(wire[0]).add(wire[1]);
            map.get(wire[1]).add(wire[0]);
        }
        
        return minDiff;
    }
     // 3. bfs
    private int bfs(int start, int n){
        Queue<Integer> q = new LinkedList<>(); // 큐 생성
        boolean[] visited = new boolean[n+1]; // 방문체크
        q.offer(start);
        visited[start]=true;
        
        int size = 0; // 크기
        
        while(!q.isEmpty()){
            int node = q.poll();
            size ++;
            
            // 연결 요소 구하기
            for(int nei: map.get(node)){
                if(!visited[nei]){
                    q.offer(nei);
                    visited[nei]=true;
                }
            }
        }
        return size;
    }
}
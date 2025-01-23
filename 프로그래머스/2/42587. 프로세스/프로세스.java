import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        // 우선순위 큐 생성: 우선순위 내림차순 정렬
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int pri: priorities){
            pq.add(pri); // 우선순위 큐에 추가
        }
        
        while(!pq.isEmpty()){
            for(int i=0; i<priorities.length; i++){
                if(priorities[i]==pq.peek()){
                    pq.poll();
                    answer ++; // 순서 증가
                    
                    if(i== location){ // 구하려는 위치라면
                        return answer;
                    }
                }
            }
        }
        
        return answer;
    }
}
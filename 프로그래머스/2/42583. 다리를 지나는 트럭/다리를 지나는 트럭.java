import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Queue<Integer> q = new LinkedList<>(); // 다리: 큐
        int sum = 0; // 다리에 올라온 트럭 무게 합
        
        for(int truck: truck_weights){
            while(true){
                // 큐가 비었다면
                if(q.isEmpty()){
                    q.offer(truck);
                    sum += truck;
                    answer ++; 
                    break;
                }
                // 큐가 꽉 찼다면
                else if(q.size()==bridge_length){
                    sum -= q.poll();
                }
                // 큐가 비어있지 않다면
                else{
                    if(weight < sum+truck){
                        q.offer(0);
                        answer ++; // 해당 트럭 건너는 시간 추가
                    }
                    else{
                        q.offer(truck);
                        sum+= truck;
                        answer++;
                        break;
                    }
                }
            }
        }
        
        // 걸린 시간 + 마지막 트럭까지 건너는 시간
        return answer+bridge_length;
    }
}
// n명이 입국심사 기다리는 중
// 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간 다름
// 처음에 모든 심사대 비어있음
// 한 심사대에서는 동시에 한명만 심사 가능
// 가장 앞에 서있는 사람은 비어있는 심사대로 가서 심사 받을 수 있음
// 더 빨리 끝나는 심사대가 있으면 기다렸다가 거기로 가서 심사 받을 수 있음
// 모든 사람이 심사를 받는 최소 시간?

class Solution {
    public long solution(int n, int[] times) { // n명, 심사하는데 걸리는 시간 times
        // 시간순서로 정렬되어 있음->이분탐색 가능
        // 탐색의 하한, 상한 명확함
        long left = 1L; // 최소: 1분
        long right = getMaxTime(n, times);
        long answer = right;

        
        // 이진탐색
        while(left <= right){
            long mid = left + (right-left)/2; // 오버플로우 방지용
            long count=0L; // 심사할 수 있는 사람 수

            for(int time: times){
                count += mid/time; 
            }
            if(count >= n){
                right=mid-1;
                answer = Math.min(answer, mid);
            }else{
                left=mid+1;
                }
            }
        return answer;
    }
    public long getMaxTime(int n, int[] times){
        long max = 0L;
        for(int time: times){
           max = Math.max(max, time);
        }
        return max*(long)n;
    }
}
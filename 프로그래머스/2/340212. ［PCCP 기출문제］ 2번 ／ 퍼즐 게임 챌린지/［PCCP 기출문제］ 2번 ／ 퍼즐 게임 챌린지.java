// level -> 이진탐색으로 찾기

// 현재 level 값 -> 제한 시간 내 퍼즐 해결 가능한지 판단하는 함수 작성
// diff > level: time = (diff-level)*(이전시간+현재 시간)+현재 시간
// time > limit: true(시간 초과), 아니라면 false(시간 내 가능)

// 메인에서 while문을 돌면서 이진탐색 수행
// true라면 left = mid+1
// false라면 right = mid로 변경

class Solution {
    static boolean isImpossible(int[] diffs, int[] times, long level, long limit){
        long time = (long)times[0];
        
        for(int i=1; i< times.length; i++){
            if(diffs[i] > level){
                time += ((long)diffs[i]- level)*((long)times[i-1]+(long)times[i]);
            }
            time += (long)times[i]; 
        }
        return time>limit;
    }
    
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        
        long left = 1;
        long right = limit;
        
        while(left< right){
            long mid = (left+right)/2;
            
            if(isImpossible(diffs, times, mid, limit)){
                left = mid +1;
            }else{
                right = mid;
            }
            
        }
        
        return (int)left;
    }
}
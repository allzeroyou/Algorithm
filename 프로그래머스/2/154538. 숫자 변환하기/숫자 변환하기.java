// 자연수 x -> y 변환
// 다음 연산 사용
// x + n
// x * 2
// x * 3
// 자연수 x,y,n 주어질 때, x->y로 변환하기 위해 필요한 최소 연산 횟수?
// x->y가 불가하다면: -1 return

import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        // 가능한 연산 3가지를 각각 수행하면서 최솟값=최소 연산 횟수 -> bfs 수행
        // 만약 3가지 모두 불가하다면 -1 반환
        
        // bfs-queue
        Queue<int[]> qu = new LinkedList<>(); // {값, 연산 횟수} 저장
        Set<Integer> visited = new HashSet<>();
        
        // 시작점: [현재 값, 연산횟수]
        qu.offer(new int[]{x, 0});
        visited.add(x);
        
        while(!qu.isEmpty()){
            int[] cur = qu.poll();
            int curVal = cur[0]; // 현재값
            int cnt = cur[1]; // 연산 횟수
            
            if(curVal == y){
                return cnt;
            }
            
            // 3가지 연산 수행
            int[] opers = {curVal+n, curVal*2, curVal*3};
            
            // 다음 연산
            for(int nxtVal: opers){
                if(nxtVal <= y && !visited.contains(nxtVal)){ // y보다 작고 방문 x
                    qu.offer(new int[]{nxtVal, cnt+1});
                    visited.add(nxtVal);
                }
            }
        }
        return -1;
    }
}

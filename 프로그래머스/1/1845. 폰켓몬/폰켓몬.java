import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        // 1. 중복 제거한 포켓몬 종류 set 만들기
        HashSet<Integer> set = new HashSet<>();
        
        for(int num: nums){
            set.add(num);            
        }
        System.out.println(set);
        // 2. 고르려는 마리수
        int select = nums.length/2;
    
        // 3. 최대 고르는 마릿수 return
        if(select <= set.size())
            return select;
        else
            return set.size();
    }
}
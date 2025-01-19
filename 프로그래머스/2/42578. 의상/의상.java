// 다른 옷 조합
// 서로 다른 조합 수 return
// HashMap 사용: key-의상 종류, value-의상
// 각 의상종류에 입지 않는 경우도 꼭 추가해준다
// 단, 아무것도 입지 않는 경우는 제외!

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        
        // 1. 의상 종류별로 구분하기-해시맵 사용
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String[] clothe : clothes){
            String type = clothe[1]; // 종류만 꺼내준다
            map.put(type, map.getOrDefault(type,0)+1);
        }
        // 2. 각 의상종류에 입지 않는 경우 추가해 조합 계산
        Iterator<Integer> iter = map.values().iterator();
        
        Integer answer = 1;
        while(iter.hasNext()){
            answer *= iter.next() + 1;
        }
        
        // 3. 단, 아무것도 입지않은 경우는 제외
        return answer-1;
    }
}
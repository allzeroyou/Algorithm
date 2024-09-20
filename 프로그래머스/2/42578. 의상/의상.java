// 옷 조합
import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        // 최소 1개 이상 의상 입어야 함
        // [의상이름, 의상종류]
        // map[의상종류]=의상개수
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for(int i=0; i<clothes.length; i++){
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1],0)+1);
        }
        // 해시 맵 잘 들어왔는지 체크
        // String sArr = map.toString();
        // System.out.println(sArr);
        
        // 가능한 조합 수 계산    
        int answer = 1;
        for(int cnt: map.values()){
            answer = answer*(cnt+1); // 입는 경우, 안 입는 경우
        }
        answer -= 1; // 아무것도 안 입는 경우 제외
        
        return answer;
    }
}
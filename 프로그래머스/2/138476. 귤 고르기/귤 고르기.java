// 귤 중 k개를 골라 상자 하나에 담아 판매
// 크기별로 분류시 서로 다른 종류의 수를 최소화
// 귤 개수별로 카운트 -> 상위에 포함된 귤부터 cnt를 마이너스해가면서 k가 될때 남은 귤 종류 return
// hashmap?
import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        
        int answer = 0;
        HashMap<Integer, Integer> sizeCnt = new HashMap<>();
        
        for(int size: tangerine){
            sizeCnt.put(size, sizeCnt.getOrDefault(size,0)+1);
        }
        // 개수를 기준으로 정렬-> hashmap의 values를 리스트 변환후 collections.sort 로 내림차순 정렬!
        List<Integer>counts= new ArrayList<>(sizeCnt.values());
        
        Collections.sort(counts, Collections.reverseOrder());
        
        // k개 선택
        int sum = 0;
     
        for(int count: counts){
            sum+=count;
            answer++;
            if(sum>=k){
                break;
            }
        }
        return answer;
    }
}
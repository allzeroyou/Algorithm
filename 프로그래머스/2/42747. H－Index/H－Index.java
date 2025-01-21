import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        // 1. 내림차순 정렬
        
        ArrayList<Integer> list = new ArrayList<>();
        for (int num : citations) {
            list.add(num);
        }
        Collections.sort(list, Collections.reverseOrder());

        
        //Integer[] ci = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        
        //Arrays.sort(ci, Collections.reverseOrder());
        
        // 2. 해당 논문의 인용 횟수 >= h 인지 체크
        for(int i=0; i<list.size(); i++){
            if(list.get(i) >= i+1){
                answer=i+1;
            }else{
                break;
            }
           
        }
        
        return answer;
    }
}
// 1.
// 정렬 후 comple의 참여자 수만큼 돌면서 part에만 있는 참여자 이름 출력

// 2.
// key-value로 저장
// par의 val 값과 com의 val 값이 일치하지 않는 참여자의 이름 출력

import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        // 1. 정렬
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        // 2. 두 배열이 다른 이름을 찾는다
        int i =0;
        for (; i<completion.length; i++){
            if(!participant[i].equals(completion[i]))
                break;
        }
        
        return participant[i];
    }
}
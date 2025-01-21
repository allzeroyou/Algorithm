import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        // 1. 정수를 문자열로 변환
        String[] strNum = new String[numbers.length];
        
        for(int i=0; i<numbers.length; i++){
            strNum[i]= String.valueOf(numbers[i]);
        }
        
        // 2. 문자열 배열 정렬: 내림차순
        Arrays.sort(strNum, (a,b)->(b+a).compareTo(a+b));
        
        
        // 3. 정렬된 문자열을 이어 붙이기
        answer = String.join("", strNum);
        
        // 4. 예외처리([0,0]일 경우 "00"이 아닌 0이어야 함
        if(strNum[0].equals("0")){
            return "0";
        }
        
        return answer;
    }
}
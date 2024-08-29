import java.util.Arrays;
import java.util.Comparator;


class Solution {
    public String solution(int[] numbers) { 
        // 0또는 양의 정수-> 정수를 이어 붙여 만들 수 있는 가장 큰수?
        // Java Comparator -> 커스텀 정렬 로직 구현
    
        // String 배열로 변환
        String[] strNum = new String[numbers.length];
        for(int i = 0; i<numbers.length;i++){
            strNum[i] = String.valueOf(numbers[i]);
        }
        // Comparator를 사용해 정렬
        Arrays.sort(strNum, new Comparator<String>(){
            @Override
            public int compare(String a, String b){
                return (b+a).compareTo(a+b);
            }
        });
        
        // 정렬된 숫자들을 하나의 문자열로 연결
        StringBuilder answer = new StringBuilder();
        for(String s: strNum){
            answer.append(s);
        }
        // 맨 앞이 0인 경우 (즉, 모든 숫자가 0인경우) "0"반환
        if(answer.charAt(0)=='0'){
            return "0";
        }
        return answer.toString();
        
  
    }
}
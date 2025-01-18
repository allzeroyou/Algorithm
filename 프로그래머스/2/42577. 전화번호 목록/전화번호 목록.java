import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        // HashMap 사용
        HashMap<String, Integer> map = new HashMap<>();
        
        // 1.전화번호부 만들기
        for(int i=0; i<phone_book.length; i++){
            map.put(phone_book[i], 1);
        }
        
        // 2.현재 전화번호의 접두어가 map 에 있는지 체크.
        for(int i=0; i<phone_book.length; i++){
            for(int j=1; j<phone_book[i].length(); j++){
                // 전화번호에서 접두어가 포함되는지 체크: substring
                if(map.containsKey(phone_book[i].substring(0,j))){
                    return false;
                }
            }
            
        }
         
        return answer;
    }
}
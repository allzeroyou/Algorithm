// 전화번호부
// 한 번호가 다른 번호의 접두어인 경우 확인
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        // 전화번호부 순회하면서
        // 각 전화번호가 다른 전화번호의 "접두어"라면 false
        boolean answer = true;
        
        // 전화번호부의 모든 전화번호를 해시맵에 추가
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String phone: phone_book){
            map.put(phone,1);
        }
        // 각 전화번호의 접두어가 해시맵에 존재하는지 확인
        for(String phone: phone_book){
            for(int i=0; i<phone.length(); i++){
                String prefix = phone.substring(0,i);
                if(map.containsKey(prefix)){
                    return false;
                }
            }
        }
        return answer;
    }
}
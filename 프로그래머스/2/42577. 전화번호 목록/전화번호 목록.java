// 전화번호가 다른 전화번호의 시작번호라면 -> false 반환
// 없으면 true 반환

// 1. 오름차순 정렬
// 2. 첫번째 요소 -> n-1까지 요소까지 돌면서 접두어 있는지?

import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        
        
        // 1. 정렬
        Arrays.sort(phone_book);
        // 2. for문 순회하면서 접두어 탐색
        for (int i=0; i<phone_book.length -1; i++){
            String cur = phone_book[i];
            String nxt = phone_book[i+1];
            
            // 만약 다음 문자열이 더 짧다면 접두어 불가
            if(nxt.length() < cur.length()){
                continue;
            }
            // charAt()으로 문자열 인덱스 비교
            boolean answer = true;

            for(int j=0; j<cur.length(); j++){
                if(cur.charAt(j) != nxt.charAt(j)){
                    answer = false;
                    break;
                }
            }
            if(answer){
                return false;
            }
        }
        return true; // 접두어 아니라면 true 반환
    }
}
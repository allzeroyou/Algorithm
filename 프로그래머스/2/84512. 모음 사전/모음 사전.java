import java.util.*;

class Solution {
    String[] mo = {"A", "E", "I", "O", "U"};
    List<String> dic = new ArrayList<>();
    
    public int solution(String word) {
        int answer = 0;
        
        // 1. 알파벳 조합 생성
        recur("", 5);
        
        // 2. word의 인덱스+1 반환
        return dic.indexOf(word)+1;
    }
    
    private void recur(String cur, Integer maxLeng){
        if(cur.length()>0){
            dic.add(cur);
        }
        if(cur.length() == maxLeng){
            return;
        }
        for(String m: mo){
            recur(cur+m, maxLeng);
        }
    }
}
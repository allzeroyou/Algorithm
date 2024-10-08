// 각 자리수마다 가능한 경우의 수를 계산
// 주어진 단어의 각 글자에 대해, 그 글자 이전의 모든 경우의 수를 더하기
// 마지막으로 단어의 위치를 계산
import java.util.*;

class Solution {
 // 모음 순서를 저장하는 배열
    static String[] mo = {"A", "E", "I", "O", "U"};
    // 각 자리수별 경우의 수를 저장하는 배열
    static int[] WEIGHTS = {781, 156, 31, 6, 1};
    
    public int solution(String word) {
        int answer = 0;
        
        // 단어의 각 글자에 대해 반복
        for (int i = 0; i < word.length(); i++) {
            // 현재 글자의 인덱스를 찾음
            int index = Arrays.asList(mo).indexOf(word.substring(i, i+1));
            // 해당 글자 이전의 모든 경우의 수를 더함
            answer += index * WEIGHTS[i] + 1;
        }
        
        return answer;
    }
}
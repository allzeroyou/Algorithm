import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0; i<commands.length; i++){
            int[] cur =commands[i];
            int[] subArr = Arrays.copyOfRange(array, cur[0]-1,cur[1]);
            Arrays.sort(subArr);
            
            answer[i]=subArr[cur[2]-1];
        }
        
        return answer;
    }
}
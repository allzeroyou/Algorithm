 // begin -> target으로 변환하는 가장 최단 거리? -> bfs
// 1. 한번에 한개 알파벳만 바꿀 수 있음
// 2. words에 있는 단어로만 바꿀 수 있음
import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        // 알파벳을 어떻게 바꾸지? 바꾸는게 최단 거리가 되도록 어캐하지..
        // 일단 bfs 템플릿 적어보자
        Queue<String>qu = new LinkedList<>();
        qu.offer(begin); // 시작점이 뭐지... -> 시작 단어!
        boolean[] visited = new boolean[words.length]; // 단어 중복 x
        
        while(!qu.isEmpty()){
            // 현재단계의 변환 가능한 모든 단어를 큐에 넣고, 큐에서 단어를 꺼낼때마다 answer 증가
            int size = qu.size();
            
            for(int s =0; s<size; s++){
                String cur = qu.poll();
                // bfs 종료 조건
                if(cur.equals(target)){
                    return answer;
                }
                // 변환 가능한 단어 찾기
                for(int i=0; i<words.length; i++){
                    if(!visited[i] && isDiffOneWord(cur, words[i])){
                        qu.offer(words[i]);
                        visited[i]=true;
                    }
                }
            }
            answer ++; // bfs 한 단계 수행 후 과정 증가
        }
        return 0; // 변환 불가한 경우
    }
    // 단어 바꾸기 위해 한글자만 다른 단어 찾기
    public boolean isDiffOneWord(String s1, String s2){
        int cnt = 0;
        for(int i =0; i< s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i)){
                cnt ++;
            }
        }
        return cnt == 1; // 한글자만 다른 경우 true
    }
}
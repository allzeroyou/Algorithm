// 두개의 단어 begin, target, 단어 집합: words
// 규칙을 이용해 begin -> target으로 변환하는 가장 짧은 과정?(bfs)

// 1. 한번에 한개의 알파벳만 바꿀 수 있음
// 2. words에 있는 단어로만 변환 가능

// 어떻게 words안에 있는 단어들 중 하나를 고르지? -> 두 단어가 한 글자만 다른지 하나씩 점검하는 함수로!

import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        // target이 words에 없으면 0 반환
        if(!Arrays.asList(words).contains(target)) return 0;
        
        int answer = 0;
            
        // bfs-Queue
        Queue<WordNode> q = new LinkedList<>();
         // 해당 단어를 키로 설정(중복 방지:set)
        Set<String>visited = new HashSet<>();
        
        //초기화
        q.offer(new WordNode(begin, 0));
        visited.add(begin);
        
        while(!q.isEmpty()){
            WordNode cur = q.poll();
            if(cur.word.equals(target)){
                return cur.level;
            }
            for(String word: words){
                if(!visited.contains(word)&& isConvert(cur.word, word)){
                    q.offer(new WordNode(word, cur.level+1));
                    visited.add(word);
                }
            }
        }
        
        return 0;
    }
    private boolean isConvert(String w1, String w2){
        int cnt = 0;
        for(int i =0; i<w1.length(); i++){
            if(w1.charAt(i)!=w2.charAt(i)){
                cnt++;
            }
            if(cnt>1) return false; // 1글자 이상 차이나면 false 반환
        }
        return cnt == 1; // 1글자 차이나면 당첨!
    }
    private class WordNode{
        int level; // 변환 단계
        String word;
        WordNode(String word, int level){
            this.word=word;
            this.level=level;
        }
    }
}
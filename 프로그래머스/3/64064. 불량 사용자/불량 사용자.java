// 비정상적인 방법으로 당첨 시도: 불량 사용자
// 사용자 id: 최소 하나 이상 '*'로 가림
// 불량 사용자 목록 -> 제재 id
// 1. id목록에서 가능한 불량 사용자 목록 경우의 수 구해야 함(for 순회하면서 한 문자씩 비교?)
// 2. 가능한 경우의 수 중에서 가지치기(위 가지에서 사용한 건 빼고)? dfs? 통해서 제재 아이디 목록 경우의 수 구해야함
import java.util.*;

class Solution {
    // 선택된 사용자id 저장할 집합
    static Set<Set<String>> resultSet = new HashSet<>();
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;

        // 방문 체크
        boolean[] visited = new boolean[user_id.length];
        // 현재 선택된 id 저장할 집합
        Set<String> curSet = new HashSet<>();
        
        
        dfs(user_id, banned_id, curSet, visited, 0);

        return resultSet.size(); // 경우의 수 
    }
    public void dfs(String[] user_id, String[] banned_id, Set<String> curSet, boolean[] visited, int idx){
        // 재귀 종료 조건-불량사용자 목록 다 처리했을경우
        if(idx == banned_id.length){
            resultSet.add(new HashSet<>(curSet)); // 가능한 경우의 수 추가
            return;
        }
        // 순회
        for(int i=0; i<user_id.length; i++){
            if(!visited[i] && findId(user_id[i], banned_id[idx])){ // 아직 방문하지 않고, 매칭 가능한 경우
                curSet.add(user_id[i]);
                visited[i]=true;
                dfs(user_id, banned_id, curSet, visited, idx+1 ); // 다음 불량 사용자로 이동
                // 백트래킹으로 다시 아이디 선택가능하게끔 한다.
                curSet.remove(user_id[i]);
                visited[i]=false;
            }
        }
        
    }
    
    
     // 어떻게 불량사용자 목록에서 원래 사용자 id를 찾지?
    // 1. 문자열 길이 비교(길이가 같지 않으면 불가!)
    // 2. 문자열을 돌면서 '*'가 아닌 문자가 다르면 매칭 불가(발상의 전환!-'*'는 무시하고 나머지 자리 비교해서 일치하는지 확인)
    public boolean findId(String user, String ban){
        if(user.length()!=ban.length()) return false;
        for(int i =0; i<user.length(); i++){
            if(ban.charAt(i)!= '*' && user.charAt(i)!=ban.charAt(i)) // 2. '*'가 아닌 문자열은 전부 일치해야함
            {return false;}
        }
        return true; // 모든 문자가 일치
    }
}
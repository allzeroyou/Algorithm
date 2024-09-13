// 한자리 숫자 적힌 종이조각 흩어짐
// 흩어진 종이 조각 붙여 소수 몇 개 만들 수 있는지?
// numbers: 각 종이 조각에 적힌 숫자가 적힌 문자열
// 종이로 만들 수 있는 소수 몇개 -> return
// numbers: 1<=문자열 길이<=7, 0~9 숫자로 이뤄짐

// numbers 문자열 -> 한 자릿수로 쪼개서 배열에 저장
// 배열 순회하면서 
// 숫자 조합을 통해 소수 만들어야 함
// 어떻게 숫자 조합? -> dfs 재귀!

import java.util.*;

class Solution {
    static HashSet<Integer> set = new HashSet<>(); // 중복 제거
    static char[] arr; // 종이조각
    static boolean[] visited; // 사용여부

    
    public int solution(String numbers) {
        int answer = 0;
        arr = numbers.toCharArray(); // 배열로 저장
        visited = new boolean[arr.length];
        
        // 재귀함수
        recur("", 0);
        
        answer = set.size();
        return answer;
    }
    // dfs 재귀. 가능한 숫자조합 찾고 소수면 set에 추가
    public void recur(String str, int idx){
        int num;
        if(str!=""){
            num=Integer.parseInt(str);
            if(isPrime(num)) set.add(num);
        }
        if(idx==arr.length) return; // 재귀 종료조건: 끝까지 탐색 완료 시
        
        for(int i=0; i<arr.length; i++){
            if(visited[i]) continue; // 이미 썼다면 패스
            // 그렇지 않다면
            visited[i]=true;
            recur(str+arr[i], idx+1); // 다음 재귀
            visited[i]=false; //백 트래킹
        }
    }
    
    // 소수 판별
    public boolean isPrime(int num){
        if(num<2) return false;
        for(int i=2; i<=Math.sqrt(num); i++){
            if(num%i==0) return false;
        }
        return true;
    }
}
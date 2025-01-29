import java.util.*;

class Solution {
    public int solution(int N, int number) {
        int answer = 0;
        
        // 1. 테이블 정의: 배열의 각 요소에 집합을 저장한다
        Set<Integer>[] dp = new HashSet[9];
        
        // 3. 초기값 설정
        dp[1]= new HashSet<>();
        dp[1].add(N);
        
        // tc9: number==N일때 1 반환 후 종료해야함(for문 i=2부터 시작하므로 i=1의 조건 검사를 빠뜨림)
        if(number==N){
            return 1;
        }
        
        // 2. 점화식 도출
        for(int i = 2; i < 9; i++){
            // i개의 N을 사용해 만들 수 있는 숫자 저장
            dp[i]= new HashSet<>();
            
            // 1. 반복한 숫자 추가
            String repeat = String.valueOf(N).repeat(i);
            dp[i].add(Integer.parseInt(repeat));            
            
            // 2. 이전 숫자 조합을 활용한 사칙연산
            for(int k = 1; k <i; k++){
                for(int num1: dp[k]){
                    for(int num2: dp[i-k]){
                        dp[i].add(num1+num2);
                        dp[i].add(num1-num2);
                        dp[i].add(num1*num2);
                        if (num2 !=0) dp[i].add(num1/num2);
                    }
                }
            }
            // n이 dp[i]에 있다면 최소 사용 횟수 i를 반환
            if(dp[i].contains(number)) return i;
        }
        // 최솟값이 8보다 크면 -1 return
        return -1;
    }
}
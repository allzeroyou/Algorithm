import java.util.*;

class Solution {
    HashSet<Integer> set = new HashSet<>();
    
    // 소수 체크
    public boolean isPrime(int num){
        // 1. 0과 1은 소수가 아님
        if(num == 0 || num ==1){
            return false;
        }
        // 2. 에라토스테네스의 체 limit 계산
        int limit = (int)Math.sqrt(num); // 루트 씌운 값까지 계산
        
        // 3. 에라토스 체에 따라 limit까지만 배수 여부 확인
        for(int i=2; i<limit + 1; i++){
            if(num % i == 0)
                return false;
        }
        return true;
    }
    
    public void makeNum(String comb, String others){
        // 1. 현재 조합을 set에 추가
        if(!comb.equals(""))
            set.add(Integer.valueOf(comb));
        
        for(int i=0; i<others.length(); i++){
            // 2.남은 숫자 들 중 하나를 더해 새로운 조합 만듦.
            makeNum(comb+others.charAt(i), others.substring(0,i) + others.substring(i+1));
        }
    }
    
    public int solution(String numbers) {
        int answer = 0;
        
        // 1. 숫자 조합 만들기 -> 재귀 사용
        makeNum("", numbers);
                
        // 2. 소수 개수 세기
        Iterator<Integer> iter = set.iterator();
        
        int cnt = 0;
        while(iter.hasNext()){
            int number = iter.next();
            
            if(isPrime(number))
                cnt ++;
        }
        
        // 3. 소수 개수 반환
        return cnt;
    }
}
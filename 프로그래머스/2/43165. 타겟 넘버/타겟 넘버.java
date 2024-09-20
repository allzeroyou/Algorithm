// n개의 음이 아닌 정수
// 정수들을 "순서를 바꾸지 않고", "적절히" +,- 연산자 "배치"을 통해 타겟넘버 만드려고 함.
// 타겟 만드는 경우의 수 반환
import java.util.*;

class Solution {
    
    public int solution(int[] numbers, int target) {
        int answer = 0;
        // dfs 수행: 타겟넘버가 나올때 반환
 
        
        return dfs(numbers, target, 0, 0);
    }
    // dfs 매개변수: 현재 상태를 나타내는 정보를 매개변수로 넘김!(이를 이용해 탐색 이어나감)
    public int dfs(int[] numbers, int target, int sum, int idx ){ // sum:현재까지 합, idx: 현재 탐색할 인덱스
        if(idx==numbers.length){
            return sum==target? 1: 0; // 타겟넘버가 되었을때 1, 아니면 0 반환
        }
        // +, -를 적절히 어떻게 배치하지... -> 배치하는게 아니라 그냥 재귀적으로 계속 수행
        int add = dfs(numbers, target, sum+numbers[idx], idx+1);
        int sub = dfs(numbers, target, sum-numbers[idx], idx+1);
       return add+sub; // 두 경우의 수를 합해 반환
    }
}
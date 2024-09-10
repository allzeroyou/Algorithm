// 숫자를 더하거나 빼서 타겟넘버 만듦
// 모든 경우의 수 탐색 -> dfs
class Solution {
    int answer = 0;

    public int solution(int[] numbers, int target) {
        
        dfs(numbers, target, 0,0);
        
        return answer;
    }
    private void dfs(int[] numbers, int target, int idx, int sum){
        // 종료조건: 모든 숫자 사용시
        if(idx == numbers.length){
            // 합계가 타겟넘버라면 정답 카운트
            if(sum==target){
                answer++;
            }
            return;
        }
        // 현재 숫자 더함
        dfs(numbers, target, idx+1, sum+numbers[idx]);
        
        // 현재 숫자 뺌
        dfs(numbers, target, idx+1, sum-numbers[idx]);
        
    }
}
// 비내림차순 정렬된 수열-> 다음 조건 만족하는 부분 수열
// 조건
// 1.기존 수열에서 임의의 두 인덱스의 원소, 그 사이의 원소를 모두 포함하는 부분 수열
// 2.부분 수열의 합은 k
// 3.합이 k인 부분 수열이 여러개일 경우 "길이가 짧은" 수열 찾음
// 4.길이가 짧은 수열이 여러개 인 경우 앞쪽(시작 idx가 작은) 수열 찾음

// 배열에서 2개의 포인터 -> 특정 조건을 만족하는 구간 구하기 -> "투포인터!"

class Solution {
    public int[] solution(int[] sequence, int k) { // 수열: seq, 부분 수열의 합: k
        // 부분 수열의 시작 idx, 마지막 idx를 배열에 담아 return
        int[] answer = {};
        
        int left = 0;
        int right = 0;
        int sum = 0;
        int minLength = Integer.MAX_VALUE; // 부분 수열의 최솟값
        int startIdx = -1; // 최종 시작 인덱스
        int endIdx = -1; // 최종 끝 인덱스
        
        // 투포인터로 부분 수열 찾음
        while(right < sequence.length){
            sum += sequence[right];

            // sum이 k보다 크다면.. left포인터를 오른쪽으로 이동해 합 줄임
            while(sum> k && left<=right){
                sum -= sequence[left];
                left++;    
            }
            // 부분 수열 합이 k일 경우
            if(sum == k){
                int curLength = right-left + 1;
                // 더 짧은 부분 수열 찾거나, 같은 길이라면 더 앞에 있는거 선택
                if(curLength<minLength){
                    minLength = curLength;
                    startIdx = left;
                    endIdx = right;
                }
            }
            right++;
        }
        return new int[]{startIdx, endIdx};
    }
}

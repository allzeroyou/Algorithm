// 명함 회전 가능
// 모든 명함 수납 가능한 가장 작은 크기의 지갑

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        // 각 명함의 긴 쪽을 width로, 짧은 쪽을 height로
        int maxWid = 0;
        int maxHei = 0;
        
        for(int[] card: sizes){
            int longer = Math.max(card[0], card[1]);
            int shorter = Math.min(card[0], card[1]);
            // 최댓값 갱신
            maxWid = Math.max(maxWid, longer);
            maxHei = Math.max(maxHei, shorter);
        }

        
        return maxWid*maxHei;
    }
}
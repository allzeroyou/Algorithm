// 중앙에는 노란색, 테두리 1줄은 갈색으로 칠해진 격자 모양 카펫
// 격자의 수 -> 카펫의 가로, 세로 크기?
// 카펫 구조 -> 수학식 도출(코드로 표현하기 위해)
// b: 2w+2h-4(모서리 중복 제거)
// y: (w-2)*(h-2)

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int total = brown+yellow;
        
        for(int w=3; w<=total/3; w++){ // 가로길이는 최솟값:3부터 시작
            if(total%w==0){ // 가로 길이가 전체 면적의 약수라면
                int h = total/w; // 직사각형 면적 공식
                
                // 갈색 격자 수 공식 확인
                if(2*w + 2*h -4 == brown){
                    answer[0]=h;
                    answer[1]=w; 
                    break; // 종료
                }
            }
        }
        return answer;
        
    }
}
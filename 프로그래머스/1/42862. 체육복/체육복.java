import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        // 전체 학생수: n, 체육복 도난당한 학생들 번호: lost, 여벌 체육복 학생들 번호: reserve
        // 체육수업을 들을 수 있는 학생 최댓값?
        
        int answer = 0;
        
        // 전체 학생 배열
        int[] student = new int[n];
        // 모든 학생이 체육복을 1개씩 가지고 있다고 초기화
        Arrays.fill(student,1);
        // 체육복을 도난당한 학생 처리
        for(int l:lost){
            student[l-1]--; // 인덱스화
        }
        // 여벌체육복이 있을 경우 체육복 +1
        for(int r:reserve){
            student[r-1]++;
        }
        // 체육복 빌려주기
        for(int i=0; i<n; i++){
            if(student[i]==0) {// 도난 당했을경우
                if(i>0 && student[i-1]==2) {// 내 앞 학생이 체육복 2개일 경우
                    student[i]++;
                    student[i-1]--;
                }else if(i<n-1 && student[i+1]==2){ // 마지막 인덱스 x && 내 뒤 학생이 체육복 2개일 경우
                    student[i]++;
                    student[i+1]--;
                }
            }
                
        }
        // 체육수업을 들을 수 있는 학생 count
        for(int i=0;i<n;i++){
            if(student[i]>=1){
                answer++;
            }
        }

        
        
        return answer;
    }
}
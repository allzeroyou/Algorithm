import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 값 수정이 가능하게끔 arraylist로
        List<Integer> ans = new ArrayList<>();
    
        // 배포 가능한 날짜
        List<Integer> upload = new ArrayList<>();
        
        for(int i=0; i<progresses.length; i++){
            upload.add((int)Math.ceil((100.0-progresses[i])/speeds[i]));
        }
        
        // 앞의 기능
        int pre = upload.get(0);
        int cnt = 1; // 함께 배포하는 작업 수
        
        for(int i=1; i<upload.size(); i++){
            // 앞의 배포 날짜가 더 크다면, 배포 날짜에 함께 배포한다
            if(upload.get(i) <= pre){
                cnt ++;
            }else{
                ans.add(cnt);
                cnt = 1;
                pre= upload.get(i); // 앞의 날짜 갱신
            }
        }
        ans.add(cnt); // 마지막 그룹까지 추가
        
        int[] answer = new int[ans.size()];
        
        for(int i=0; i<answer.length; i++){
            answer[i]=ans.get(i);
        }
        
        return answer;
    }
}
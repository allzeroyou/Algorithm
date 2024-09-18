// 과제 순서
// 1. 시작하기로 한 시각이 되면 시작
// 2. 새로운 과제를 시작할 시각이 되었을 때, 기존에 진행중이던 과제가 있다면 과제 "멈추고" -> 새로운 과제 시작
// 3. 진행중이던 과제를 끝냈을 때, 잠시 멈춰둔 과제가 있다면, 멈춰둔 과제를 이어서 진행
    // 3-1. 과제를 끝냈을때 "새로 시작해야 되는 과제"와 "잠시 멈춰둔 과제"가 모두 있다면 -> 새로 시작해야 하는 과제부터 진행
// 4. 멈춰둔 과제가 여러 개 일경우, 가장 최근에 멈춘 과제부터 시작

// 과제를 끝낸 순서대로 이름을 배열에 담아 return
// 선점 스케줄링 방법이랑 유사하네..
// start 기준으로 오름차순 정렬-> playtime-진행시간 -> 남은 시간:0이 될때까지 반복
// 가장 최근에 멈춘 과제부터 다시 시작 -> stack 자료구조 사용
import java.util.*;

class Solution {
    // 과제 정보 담을 클래스
    static class Assign{
        String name;
        int start;
        int play;

        Assign(String name, String start, String play){
            this.name=name;
            this.start=changeMin(start);
            this.play=Integer.parseInt(play);
        }
    }
    
    public String[] solution(String[][] plans) { // 과제 계획을 담은 2차원 문자열 배열 plans
        String[] answer = {};
        
        // plans 배열을 Assign 객체 리스트로 변환
        List<Assign> aList = new ArrayList<>();
        for(String[] plan: plans){
            aList.add(new Assign(plan[0], plan[1], plan[2]));
        }
        // 시작시간으로 정렬
        Collections.sort(aList, startTimeComp); 
        
        // 과제 처리 로직
        Stack<Assign> pausedList = new Stack<>(); // stack 자료구조
        List<String> compleList = new ArrayList<>(); // 정답 배열
        
        int curTime = aList.get(0).start;
        
        for(int i=0; i<aList.size(); i++){
            Assign curAsign = aList.get(i);
            
            // 현재시각~ 다음 과제 시작 시간 전까지 멈췄던 과제 처리
            while(!pausedList.isEmpty() && curTime < curAsign.start){
                Assign pausedAssign = pausedList.pop();
                
                // 멈춘 과제를 완전히 끝낼 수 있는 경우
                if(curTime + pausedAssign.play <= curAsign.start){
                    curTime += pausedAssign.play;
                    compleList.add(pausedAssign.name);
                }else{
                   // 멈춘 과제를 부분적으로만 진행할 수 있는 경우
                    pausedAssign.play -= (curAsign.start - curTime);
                    curTime = curAsign.start;
                    pausedList.push(pausedAssign);
                    break;
                }
            }
            curTime = Math.max(curTime, curAsign.start); // 현재 시간 업데이트
            // 다음 과제 시작 시간 또는 현재 과제 종료 시간 계산
            int nxtTime = (i<aList.size()-1) ? aList.get(i+1).start: curTime+ curAsign.play;
            if(curTime + curAsign.play<=nxtTime){
                // 현재 과제를 완전히 끝낼 수 있을 경우
                curTime += curAsign.play;
                compleList.add(curAsign.name);
            }else{
                //현재 과제를 끝ㄴ내지 못하고 멈춰야할경우
                curAsign.play -= (nxtTime - curTime);
                pausedList.push(curAsign);
                curTime = nxtTime;
            }
        }
        // 남은 멈췄던 과제 처리
        while(!pausedList.isEmpty()){
            compleList.add(pausedList.pop().name);
        }
        
        return compleList.toArray(new String[0]);
    }
    
    // 시작 시간을 분 단위로 변환
    public static int changeMin(String start){
        String[] hm = start.split(":");
        return Integer.parseInt(hm[0])*60 + Integer.parseInt(hm[1]); // 시간*60
    };
    
    // Assign 객체를 시작 시간 기준 오름차순 정렬하는 Comparator 구현
    static Comparator<Assign> startTimeComp = new Comparator<Assign>(){
        @Override
        public int compare(Assign a1, Assign a2){
            return Integer.compare(a1.start, a2.start);
        }
    };
}




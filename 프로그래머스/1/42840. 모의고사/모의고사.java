// 수포자 3명의 찍는 방법
// 1번: 1,2,3,4,5/ 1,2,3,4,5.. -> 순서대로
// 2번: 2,1, 2,3, 2,4, 2,5/ 2,1, 2,3, 2,4, 2,5, ... -> 2+(1,3,4,5)
// 3번: 3,3, 1,1, 2,2, 4,4, 5,5, 3,3, ...-> (3,1,2,4,5)*2
// 1번부터 마지막 문제까지 정답이 순서대로 들은 배열 answers

// 가장 많은 문제를 맞힌 사람?
// 가장 높은 점수를 받은 사람이 여럿일 경우-> 오름차순 정렬 후 return
import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = new int[3];
        // 각 1,2,3번의 번호 찍는 패턴을 answers만큼 반복하면서
        // 해당 요소와 일치하면 count 증가
        int[] first = {1,2,3,4,5};
        int[] second = {2,1,2,3,2,4,2,5};
        int[] third = {3,3,1,1,2,2,4,4,5,5};
            
        for(int i=0; i<answers.length; i++){
            if(answers[i]==first[i%first.length]){
                answer[0]++;
            }
            if(answers[i]==second[i%second.length]){
                answer[1]++;
            }
            if(answers[i]==third[i%third.length]){
                answer[2]++;
            }
        }
        // 정답맞힌 사람들 중 최댓값 구하기
        int maxVal = Math.max(answer[0], Math.max(answer[1], answer[2]));
        // 정답 많이 맞힌 사람의 번호를 구해야 함
        List<Integer> list = new ArrayList<>();
        for(int i=0; i<3; i++){
            if(answer[i]==maxVal){
                list.add(i+1);
            }
        }
        int[] result = new int[list.size()];
        for(int i=0; i<list.size(); i++){
            result[i] = list.get(i);
        }
        
        return result;
    }
}
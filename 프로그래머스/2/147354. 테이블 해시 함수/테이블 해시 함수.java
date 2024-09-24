import java.util.Arrays;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        //행(가로)를 col번째 컬럼 값 기준 오른차순 동일하면 기본키 첫번째 컬럼 값 기준 기준 내림차순
        //정렬이 중요하겠네요..!
        Arrays.sort(data, (o1, o2) -> {
        	return o1[col-1] != o2[col-1] ? o1[col-1] - o2[col-1] : o2[0] - o1[0];
        });
        
        int answer = 0;
        for(int i = row_begin -1; i <= row_end-1; i++) {
        	int tmp = 0;
        	for(int j = 0; j < data[i].length; j++) {
        		tmp += data[i][j] % (i+1);
        	}
        	answer = tmp ^ answer;
        }
        return answer;
    }
}

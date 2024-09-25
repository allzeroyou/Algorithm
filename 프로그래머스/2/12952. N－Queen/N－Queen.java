// 가로, 세로 길이가 n인 체스판
// 체스판 위 n개의 퀸이 서로 공격할 수 없도록 배치
// 퀸: 가로, 세로, 대각선 이동 -> 같은 행, 열, 대각선 위에 다른 퀸 위치 x
// n=12이하 자연수
// 퀸을 배치하다가 더 이상 퀸을 놓을 수 없다면 이전으로 다시 되돌아감 -> 백트래킹 이용
// 2차원 배열 상의 퀸 위치를 저장하기 위해 1차원 배열 사용(가로: row, 세로: idx)
// 이때 대각선: 직선의 기울기가 1, -1임(y 증가량/ x 증가량)
import java.util.*;

class Solution {
    static int ans = 0;
    public int solution(int n) {
        int[] map = new int[n];
        dfs(n, 0, map);
        
        return ans;
    }
    public void dfs(int n, int row, int[] map){
        if(n==row){ // 모든 행에 성공적으로 퀸 배치됨
            ans ++; // 경우의 수 증가
        }else{
            for(int i=0; i<n; i++){
                map[row] = i;
                if(check(map, row)){ // 가로, 세로, 대각선 체크
                    dfs(n, row+1, map);
                }
            }
        }
    }
    public boolean check(int[] map, int row){
        for(int i=0; i<row; i++){
            if(map[i]==map[row])return false; // 세로 같다면 false 반환
            if(Math.abs(map[i]-map[row])==Math.abs(i-row)) return false; // 대각선 같다면 false
        }
        return true;
    }
}
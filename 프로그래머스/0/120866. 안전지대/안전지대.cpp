#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board) {
    int answer = 0;
    
    int n = board.size();
    // 위험 지역 표시
    vector<vector<int>> danger(n, vector<int>(n,0));
    
    // 8방향 이동(좌,우,상,하, 대각선*4)
    int dx[] = {-1,-1,-1,0,0,1,1,1};
    int dy[] = {-1,0,1,-1,1,-1,0,1};
    
    for(int r=0; r<n; r++){
        for(int c=0; c<n; c++){
            if(board[r][c] == 1){
                danger[r][c] = 1; 
                for(int i=0;i<8;i++){
                    int nr = r+dx[i];
                    int nc = c+dy[i];
                    if(nr >= 0 && nr < n && nc >= 0 && nc < n){
                        danger[nr][nc] = 1;
                    }
                }
            }
        }
    }
    
    int safe_cnt = 0;
    for(int r=0; r<n; r++){
        for(int c=0; c<n; c++){
            if(danger[r][c] == 0) safe_cnt ++;
        }
    }
    
    return safe_cnt;
}
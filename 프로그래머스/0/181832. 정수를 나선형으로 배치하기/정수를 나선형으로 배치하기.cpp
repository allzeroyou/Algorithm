#include <vector>

using namespace std;

vector<vector<int>> solution(int n) {
    // 1. n x n 크기의 2차원 벡터를 0으로 초기화
    vector<vector<int>> answer(n, vector<int>(n, 0));
    
    // 2. 방향 벡터 (오른쪽, 아래, 왼쪽, 위)
    int dr[] = {0, 1, 0, -1};
    int dc[] = {1, 0, -1, 0};
    
    // 3.
    int r = 0;
    int c = 0;
    int dir = 0; // 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
    
    for (int num = 1; num <= n * n; ++num) {
        answer[r][c] = num;
        
        int next_r = r + dr[dir];
        int next_c = c + dc[dir];

        if (next_r < 0 || next_r >= n || next_c < 0 || next_c >= n || answer[next_r][next_c] != 0) {
            
            dir = (dir + 1) % 4; // 0->1, 1->2, 2->3, 3->0
            
            next_r = r + dr[dir];
            next_c = c + dc[dir];
        }
        
        r = next_r;
        c = next_c;
    }
    
    return answer;
}
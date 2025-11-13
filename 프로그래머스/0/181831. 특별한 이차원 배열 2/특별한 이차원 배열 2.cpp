#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> arr) {
    int answer = 0;
    // 2차원 배열
    for(int i=0; i<arr.size(); i++){
        for(int j=0; j<arr.size(); j++){
            if(arr[i][j]==arr[j][i]){
                continue;
            }else{
                return answer;
            }
        }
    }
    answer = 1;
    return answer;
}
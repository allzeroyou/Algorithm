#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    // 빈 배열 x 맨 끝에 요소 덧붙이기
    for(int i=0; i<arr.size(); i++){
        for(int j=0; j<arr[i]; j++){
            answer.push_back(arr[i]);    
        }
    }
    
    return answer;
}
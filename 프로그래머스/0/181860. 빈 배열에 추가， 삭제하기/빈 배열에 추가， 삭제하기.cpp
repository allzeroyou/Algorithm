#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<bool> flag) {
    vector<int> answer;
    // true면 arr[i]개 x 2번 추가
    // false면 마지막에서 arr[i]개 원소 제거
    for(int i=0; i<flag.size(); i++){
        
        if(flag[i]){ // true면
            for(int j=0; j<arr[i] * 2; j++){
                answer.push_back(arr[i]);                
            }
        }else{ // false면
            for(int j=0; j<arr[i]; j++){
                if(!answer.empty()){
                    answer.pop_back();
                }
            }
        }
    }
    
    return answer;
}
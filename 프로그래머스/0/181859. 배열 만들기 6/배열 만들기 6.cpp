#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    // arr -> stk 로 새로운 배열 만들기
    int i = 0;
    while(i<arr.size()){
        if(answer.empty()){
            answer.push_back(arr[i]);
            i++;
        }
        else
        {
            if(answer.back()==arr[i]){
                answer.pop_back();
                i++;
            }else{
                answer.push_back(arr[i]);
                i++;
            }
        }
    }
    if(answer.empty()){
        answer.push_back(-1);
    }
    
    return answer;
}
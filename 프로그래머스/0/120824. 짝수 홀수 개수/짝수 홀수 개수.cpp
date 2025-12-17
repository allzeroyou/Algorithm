#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    answer = {0, 0};
    
    // 짝수, 홀수 개수 담은 배열
    for(int i=0; i<num_list.size(); i++){
        if(num_list[i] % 2 == 0){
            answer[0]++;
        }else{
            answer[1]++;
        }
    }
    
    return answer;
}
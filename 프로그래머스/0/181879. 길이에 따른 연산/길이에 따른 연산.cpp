#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    // 리스트 길이 >= 11 -> 리스트 모든 원소 합
    // <= 10 -> 원소 곱
    if(num_list.size() >= 11){
        for(int i =0; i<num_list.size(); i++){
            answer += num_list[i];
        }
    }
    else if(num_list.size()<=10){
        answer = 1;
        for(int i =0; i<num_list.size(); i++){
            answer *= num_list[i];
        }
    }
    
    return answer;
}
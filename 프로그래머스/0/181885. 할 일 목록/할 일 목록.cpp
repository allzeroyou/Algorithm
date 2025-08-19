#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> todo_list, vector<bool> finished) {
    vector<string> answer;
    // finished 가 false라면 answer 에 삽입
    for(int i=0; i<todo_list.size(); i++){
        if(!finished[i]){
            answer.push_back(todo_list[i]);
        }
    }
    
    return answer;
}
#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> names) {
    vector<string> answer;
    // 5명 자른 리스트에서 1번째 원소
    for(int i=0; i<names.size(); i+=5){       
       answer.push_back(names[i]);    
    }
    return answer;
}
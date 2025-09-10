#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> solution(string my_string) {
    vector<string> answer;
    // 공백으로 자르기
    // 근데 맨 앞, 맨 뒤 공백 제거?
    istringstream iss(my_string);
    string word;
    
    while(iss>>word){
        answer.push_back(word);
    }
    
        
    
    return answer;
}
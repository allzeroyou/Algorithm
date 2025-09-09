#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> solution(string my_string) {
    vector<string> answer;
    // 문자열 공백 잘라서 배열에 넣기
    istringstream iss(my_string);
    string word;
    while(iss >> word){
        answer.push_back(word);
    }
    return answer;
}
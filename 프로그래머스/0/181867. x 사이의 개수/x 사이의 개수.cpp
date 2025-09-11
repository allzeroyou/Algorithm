#include <string>
#include <vector>

using namespace std;

vector<int> solution(string myString) {
    vector<int> answer;
    // x 기준 문자열 자르기
    char del = 'x';
    vector<string> tokens;
    size_t start = 0;
    size_t end = myString.find(del);
    
    // 배열 삽입
    while(end!=string::npos){
        tokens.push_back(myString.substr(start, end-start));
        start = end +1;
        end = myString.find(del, start);
    }
    tokens.push_back(myString.substr(start)); // 마지막 토큰
    
    // o 개수 세기 -> 배열 삽입
    for(const auto&t : tokens){
        answer.push_back(t.length());
    }
    
    return answer;
}
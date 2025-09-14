#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(string myString) {
    vector<string> answer;
    // x 기준으로 문자열 잘라 배열 만들기
    char del = 'x';
    vector<string> tokens;
    size_t start = 0;
    size_t end = myString.find(del);
    
    while(end != string::npos){
        tokens.push_back(myString.substr(start, end-start));
        start = end+1;
        end = myString.find(del, start);
    }
    tokens.push_back(myString.substr(start)); 

    // 빈 문자열 제거, 사전순 정렬
    tokens.erase(remove(tokens.begin(), tokens.end(), ""), tokens.end());
    
    std::sort(tokens.begin(), tokens.end());
    
    return tokens;
}
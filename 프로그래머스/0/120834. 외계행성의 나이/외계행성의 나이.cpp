#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string answer = "";
    // 0 -> a로, 1 -> b로 변환..
    // int형을 하나씩 자르기 위해 to_string으로 숫자->문자열로 변환
    string s = to_string(age);
    
    // 문자열 각 문자 순회
    for(int i=0; i<s.length(); i++){
        // '0'을 뻬서 정수값 얻고 'a' 더해 해당 알파벳으로 변환
        answer += (s[i] - '0' + 'a');        
    }
    
    
    return answer;
}
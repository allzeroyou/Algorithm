#include <string>
#include <vector>

using namespace std;

string solution(string myString, string pat) {
    string answer = "";
    
    // 부분 문자열 중 pat로 끝나는 가장 긴 부분 문자열?
    // pat이 마지막으로 등장하는 시작 인덱스 반환
    // 해당 인덱스에 길이를 더하면 pat이 끝나는 위치임.
    int idx = myString.rfind(pat);
    answer = myString.substr(0, idx+pat.length());
    
    return answer;
}
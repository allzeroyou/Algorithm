#include <string>
#include <vector>

using namespace std;

int solution(int num, int k) {
    int answer = 0;
    // num 를 string으로 만들어서 k가 있는지 체크
    string s = to_string(num);
    // find함수는 첫번째 문자 index 반환
    char cK = k + '0'; // 숫자 -> 문자로 변환
    size_t pos = s.find(cK);
        
    return (pos != string::npos) ? (int)pos + 1: -1 ;
}
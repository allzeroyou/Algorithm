#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    // 정수 n을 string으로 변경해서 각 자리 더하기
    string s_n = to_string(n);
    for(char c_n: s_n){
         answer += c_n - '0';
    }
    return answer;
}
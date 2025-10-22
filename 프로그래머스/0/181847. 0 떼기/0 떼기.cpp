#include <string>
#include <vector>

using namespace std;

string solution(string n_str) {
    string answer = "";
    // 문자열 맨 앞에서 0이 아닌 문자가 처음 등장하는 위치 찾기
    size_t first_non_zero = n_str.find_first_not_of('0');
    
    // 맨 앞에서 부터 0이 아닌 문자 등장하면 제거할 0 없음
    if(first_non_zero==0){
        return n_str;
    }
    
    // 맨 앞에서 부터 0이라면 -> 0 인덱스부터 first_non_zero 길이 만큼 제거
    return n_str.substr(first_non_zero);
}
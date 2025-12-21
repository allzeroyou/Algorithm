#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string letter) {
    string answer = "";
    // my_string에서 letter 제거
    int cur_idx = 0;
    int nxt_idx = 0;
    // 문자열 -> 문자로 변환
    char target = letter[0];
    
    while(my_string[cur_idx] != '\0'){
        if(my_string[cur_idx] != target){
            my_string[nxt_idx]=my_string[cur_idx];
            nxt_idx++;
        }
        cur_idx++;
    }
    // 문자열 크기 재조정
    my_string.resize(nxt_idx);
    
    return my_string;
}
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int s, int e) {
    string answer = "";
   
    for(int i=e; i>=s; i--){
        answer += my_string[i];
    }
    // 기존 문자열 + 뒤집 + 나머지 
    return my_string.substr(0, s) + answer + my_string.substr(e+1);
    
}
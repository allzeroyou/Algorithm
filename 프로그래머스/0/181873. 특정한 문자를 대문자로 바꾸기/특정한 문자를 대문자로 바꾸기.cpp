#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string alp) {
    string answer = "";
    // alp에 해당하는 글자를 대문자로
    for(int i=0; i<my_string.size(); i++){
        if(my_string[i]==alp[0]){ // char, string 타입 비교 주의
            my_string[i]=toupper(my_string[i]);
        }
    }
    return my_string;
}
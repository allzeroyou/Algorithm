#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    
    // 모음
    string aeiou = "aeiou";
    
    for(char s: my_string){
        if(aeiou.find(s) == string::npos){
            answer += s;
        }
    }
    return answer;
}
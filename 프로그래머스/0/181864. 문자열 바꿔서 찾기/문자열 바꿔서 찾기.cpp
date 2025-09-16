#include <string>
#include <vector>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    // A,B로 이뤄진 문자열 myString, pat
    // A를 B로, B를 A로 바꾼 문자열 -> chgStr
    // 연속하는 부분 문자열 중 pat이 있으면 1
    for(char &c: myString){
        if(c=='A') c='B';
        else
            c='A';
    }
    
    if (myString.find(pat) != string::npos){
        return 1;
    }
    
    return answer;
}
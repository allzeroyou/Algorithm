#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    string answer = "";
    // 알파벳 소문자로 이뤄진 문자열
    // i보다 앞서는 문자는 i로 치환
    int ascii_val = 0;
    
    for(int i=0; i<myString.size(); i++){
        ascii_val = myString[i];
        if(ascii_val < 108){  // l=108
            myString[i]='l';
        }
    }
    return myString;
}
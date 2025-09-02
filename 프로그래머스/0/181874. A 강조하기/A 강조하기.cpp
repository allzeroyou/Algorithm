#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

string solution(string myString) {
    string answer = "";
    // a -> A로 변환
    // A가 아닌 대문자 -> 소문자 변환
    
    // 1. 모두 소문자 변환
    transform(myString.begin(), myString.end(), myString.begin(), ::tolower);
    
    // 2. a라면 A로 변환
    for(int i=0; i<myString.size(); i++){
        if(myString[i]=='a'){
            myString[i] = toupper(myString[i]);
        }
    }
    
    return myString;
}
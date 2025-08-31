#include <string>
#include <vector>
#include <algorithm>
#include <cctype> // ::tolower

using namespace std;

string solution(string myString) {
    string answer = "";
    // 모든 알파벳을 소문자로 변환
    transform(myString.begin(), myString.end(), myString.begin(), ::tolower);
    
    
    return myString;
}
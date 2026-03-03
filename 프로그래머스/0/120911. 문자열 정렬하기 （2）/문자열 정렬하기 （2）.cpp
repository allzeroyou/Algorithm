#include <string>
#include <vector>
#include <algorithm> // sort, transform
#include <cctype> // tolower

using namespace std;

string solution(string my_string) {
    string answer = "";
    // 대소문자 문자열 -> 소문자로 바꾸기 & 알파벳 순서대로 정렬
    transform(my_string.begin(),my_string.end(), my_string.begin(), ::tolower);
    // 정렬
    sort(my_string.begin(), my_string.end());
    
    return my_string;
}
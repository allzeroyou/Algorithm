#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int m, int c) {
    string answer = "";
    // 1. m개씩 자르기
    int len = my_string.length();
    
    string col = "";
    
    for(int i=0; i< len; i+=m){
       string temp = my_string.substr(i, m);
        
        // c번째 문자 추출
        col += temp[c-1]; // 1-based
        
    }
    
    return col;
}
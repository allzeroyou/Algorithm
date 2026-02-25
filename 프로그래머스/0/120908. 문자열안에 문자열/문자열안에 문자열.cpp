#include <string>
#include <vector>

using namespace std;

int solution(string str1, string str2) {
    int answer = 2;
    // str1안에 str2가 있으면 1을 없으면 2 return
    if(str1.find(str2)!=string::npos){
        answer = 1;
    }
    return answer;
}
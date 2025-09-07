#include <string>
#include <vector>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    // pat이 등장하는 횟수
    for(int i=0; i<myString.size(); i++){
        int flag = 0;
        // 부분 문자열 추출
        string part = myString.substr(i, pat.size());
        if(part == pat){
            answer ++;
        }
        
    }
    return answer;
}
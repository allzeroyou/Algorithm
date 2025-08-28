#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    // 문자열 일치 여부 확인
    // 대소문자 섞여 있음
    
    // 1.길이 체크
    if(myString.size() < pat.size()){
        return answer;
    }else{ // 2.소문자 변환
        transform(myString.begin(), myString.end(), myString.begin(), ::tolower);    

        transform(pat.begin(), pat.end(), pat.begin(), ::tolower);            

        // 체크
        if(myString.find(pat)!= string::npos){ // find 함수는 찾은 위치-인덱스 반환함.
            return 1;
        }
    }

    return answer;
}
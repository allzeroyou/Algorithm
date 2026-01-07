#include <string>
#include <vector>

using namespace std;

string solution(string rsp) {
    string answer = "";
    // 가위:2, 바위:0, 보: 5
    // rsp 문자열에 저장된 가위바위보 이기는 순서대로 문자열 반환
    // 2 -> 0, 0 -> 5, 5 -> 2 return
    for(int i=0; i<rsp.length(); i++){
        if(rsp[i] == '2'){
            answer.push_back('0');
        }
        else if(rsp[i] == '0'){
            answer.push_back('5');
        }
        else if(rsp[i] == '5'){
            answer.push_back('2');
        }
    }
    
    return answer;
}
#include <string>
#include <vector>

using namespace std;

vector<string> solution(string myStr) {
    vector<string> answer;
    string tmp;
    
    // a,b,c를 구분자로 문자열 나누기
    for(char c: myStr){
        if(c=='a' || c=='b' || c=='c'){
            if(!tmp.empty()){
                answer.push_back (tmp);
                tmp = "";
            }
        }else{
            tmp += c;
        }
    }
    // 마지막 문자열도 추가해야함
    if(!tmp.empty()){
        answer.push_back(tmp);
    }
    
    // 다른 문자 없을 경우 EMPTY return
    if(answer.empty()){
        answer.push_back("EMPTY");
    }
    
    return answer;
}
#include <string>
#include <vector>

using namespace std;

int solution(vector<string> order) {
    int answer = 0;
    // order 리스트의 문자열에 cafelatte, americano가 포함된거 확인
    for(int i=0; i<order.size(); i++){
        if(order[i].find("cafelatte") != string::npos){
           answer += 5000; 
        }
        else if(order[i].find("americano") != string::npos){
           answer += 4500; 
        }else if(order[i]=="anything"){
            answer += 4500;
        }
    }
    // 금액 계산
    return answer;
}
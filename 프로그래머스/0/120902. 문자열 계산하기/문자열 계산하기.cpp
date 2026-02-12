#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string my_string) {
    // "3 + 4" -> 7
    stringstream ss(my_string);
    string token;
    
    // 1번째 숫자 삽입
    ss >> token;
    int answer = stoi(token);
    
    string num;
    string op;
    
    while(ss >> op >> num){
        if(op == "+"){
            answer += stoi(num);            
        }else if(op == "-"){
            answer -= stoi(num);
        }
    }
    return answer;
}
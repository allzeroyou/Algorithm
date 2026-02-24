#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> solution(vector<string> quiz) {
    vector<string> answer;
    // quiz: ["3 - 4 = -3", "5 + 6 = 11"]
    // result: ["X", "O"]
    
    // 공백기준으로 자르는 stringstream
    for(string s_q: quiz){
        stringstream ss(s_q);
        string X, op, Y, eq, Z;
        ss>>X>>op>>Y>>eq>>Z;
        
        int res = 0;
        int left_x = stoi(X); // 문자열 -> 정수
        int left_y = stoi(Y);
        int right_z = stoi(Z);
        
        if(op == "+"){
            res =left_x +left_y;
        }else{
            res =left_x-left_y;
        }
        if(res == right_z){
            answer.push_back("O");
        }else{
            answer.push_back("X");
        }
    }
    
    return answer;
}
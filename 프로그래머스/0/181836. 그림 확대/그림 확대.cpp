#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> picture, int k) {
    vector<string> answer;
    // 문자 * k and 문자열 * k 
    
    for(string row: picture){
        string mul_k = "";
        // 가로로 k배
        for(char c: row){
            mul_k += string(k, c); // 문자 c를 길이 k로 생성하겠음
        }
        // 세로로 k배(한줄을 k번 push)
        for(int i=0; i<k; i++){
            answer.push_back(mul_k);
        }
    }
    return answer;
}
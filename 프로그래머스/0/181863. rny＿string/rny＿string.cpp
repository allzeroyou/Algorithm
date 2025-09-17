#include <string>
#include <vector>

using namespace std;

string solution(string rny_string) {
    string answer = "";
    // m -> rn으로 변경
    // 문자열 순회하면서 m이면 rn으로 answer에 삽입
    for(char c: rny_string){
        if(c=='m'){
            answer += "rn";
        }else{
            answer += c;
        }
    }
    return answer;
}
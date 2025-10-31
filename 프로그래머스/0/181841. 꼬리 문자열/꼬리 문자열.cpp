#include <string>
#include <vector>

using namespace std;

string solution(vector<string> str_list, string ex) {
    string answer = "";
    // 모든 문자열을 순서대로 합친 문자열
    // 단 ex를 포함한 문자열은 제외
    for(int i=0; i<str_list.size(); i++){
        if(str_list[i].find(ex) != string::npos){
            continue;
        }answer += str_list[i];
    }
    
    return answer;
}
#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> str_list) {
    vector<string> answer;
    // u, d, l, r 네개의 문자열이 여러개 저장됨.
    // l, r 중 먼저 나오는 문자열이 l이라면
    // 해당 문자열 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트
    // r -> 해당 문자열 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트
    // l, r 없을 경우 빈 리스트 return
    
    for(int i=0; i<str_list.size(); i++){
        if(str_list[i]=="l"){
            // l 이전 요소들 저장
            answer.assign(str_list.begin(), str_list.begin()+i);
            break;
        }
        else if(str_list[i]=="r"){
            answer.assign(str_list.begin()+i+1, str_list.end());
            break;
        }
    }
    
    
    return answer;
}
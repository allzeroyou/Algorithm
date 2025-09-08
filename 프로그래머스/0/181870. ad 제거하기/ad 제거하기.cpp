#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    // 배열 문자열 중 ad라는 부분 문자열 포함하고 있는 모든 문자열 제거
    // 남은 문자열을 순서 유지해 배열로 return
    for(int i=0; i<strArr.size(); i++){
       if(strArr[i].find("ad")==string::npos){
           answer.push_back(strArr[i]);
       }
    }
    
    return answer;
}
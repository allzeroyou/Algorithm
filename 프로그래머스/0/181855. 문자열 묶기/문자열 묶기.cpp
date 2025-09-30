#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<string> strArr) {
    int answer = 0;
    // 문자열 배열 strArr
    // 길이가 같은 문자열끼리 그룹으로 묶었을때 가장 개수가 많은 그룹 크기?
    // key: 길이 value: 문자열 개수 -> map으로 관리
    
    map<int, int> myMap;
    for(string& s: strArr){
        myMap[s.size()]++; // 길이별 개수 증가
    }
    for(const auto&p : myMap)
    {
        if(answer < p.second) answer = p.second;
    }
    
    return answer;
}
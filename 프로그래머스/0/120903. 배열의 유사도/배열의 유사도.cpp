#include <string>
#include <vector>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    int answer = 0;
    // 같은 원소 개수 return
    // if문으로 하나씩 비교?
    for(string str1: s1){
        for(string str2: s2){
            if(str1 == str2){
                answer ++;
            }
        }
    }
    return answer;
}
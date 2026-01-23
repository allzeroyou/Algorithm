#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string my_string) {
    vector<int> answer;
    
    for(char c: my_string){
        if(c>='0'&&c<='9'){
            // '1'을 숫자 1로 바꾸기
            answer.push_back(c - '0');
        }
    }
    // 오름차순 정렬
    sort(answer.begin(), answer.end());
    
    return answer;
}
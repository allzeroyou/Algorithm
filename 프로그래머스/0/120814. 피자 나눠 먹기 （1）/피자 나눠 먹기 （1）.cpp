#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    // 몫만큼 피자수 필요함. 그리고 나머지 있으면 피자 한판 추가해줘야 함.
    answer = n/7;
    
    if(n%7 != 0){
        answer += 1;
    }

    return answer;
}
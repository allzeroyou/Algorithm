#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    // 3의 배수, 숫자 3 사용 x
    for(int i=1; i<=n; i++){
        answer ++;
        while(answer %3==0 || to_string(answer).find('3') != string::npos){
            answer ++;
        }
    }
    return answer;
}
#include <string>
#include <vector>

using namespace std;

int solution(int balls, int share) {
    long long answer = 1; // 8바이트로 늘리기
    
    // balls 중 share개 뽑기
    for(int i=1; i<=share; i++){
        answer *= (balls - i + 1);
        answer /= i;
    }
    return answer;
}
#include <string>
#include <vector>

using namespace std;

int solution(int hp) {
    int answer = 0;
    // 5, 3, 1
    // 약간 동전 나누기 같은 문제인가?
    // 먼저 5로 나눈 나머지에서 3으로 나누고, 그리고 해당 나머지를 더해주자
    answer += hp/5;
    answer += (hp%5)/3;
    answer += (hp%5)%3;

    return answer;
}
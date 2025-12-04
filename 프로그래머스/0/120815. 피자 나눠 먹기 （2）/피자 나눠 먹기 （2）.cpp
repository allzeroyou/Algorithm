#include <string>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int solution(int n) {
    int answer = 0;
    // 최소공배수 / 6
    answer = ((n / gcd(n, 6))*6) / 6;

    
    return answer;
}
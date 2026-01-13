#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int k) {
    int answer = 0;
    // numbers에서 idx+2 으로 계산
    int idx = (2*(k-1))%numbers.size();

    return numbers[idx];
}
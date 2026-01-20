#include <string>
#include <vector>
#include <algorithm> 
#include <functional>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    // 2개 곱해 최댓값 만들기
    // 내림차순 정렬 -> 1,2번째 배열 요소 곱하기
    sort(numbers.begin(), numbers.end(), greater<int>());
    answer = numbers[0] * numbers[1];
    return answer;
}
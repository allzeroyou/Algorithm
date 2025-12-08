#include <string>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    // 모든 원소 합/ 원소 길이
    for(int i=0; i<numbers.size(); i++){
        answer += numbers[i];
    }
    answer/=numbers.size();
    return answer;
}
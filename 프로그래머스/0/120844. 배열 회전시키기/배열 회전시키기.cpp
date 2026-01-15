#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers, string direction) {
    vector<int> answer;
    // right일 경우 배열 마지막 요소를 맨 앞으로
    if(direction == "right"){
        // 맨 마지막 요소
        int last = numbers.back();
        // 요소 제거
        numbers.pop_back();
        // 맨 앞에 삽입
        numbers.insert(numbers.begin(), last);
    }else{
        // 맨 앞 요소
        int first = numbers.front();
        // 요소 제거
        numbers.erase(numbers.begin());
        // 맨 뒤에 삽입
        numbers.push_back(first);
    }

    return numbers;
}
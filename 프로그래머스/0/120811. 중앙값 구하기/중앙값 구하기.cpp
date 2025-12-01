#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    // 중앙값 구하기
    // 1.오름차순 정렬
    sort(array.begin(), array.end());
    
    // 2.array 배열 길이:  /2 
    return array[array.size()/2];
}
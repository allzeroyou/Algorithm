#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    // arr 의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 0 추가
    // 2, 4, 8, 16, 32, 64, 128, 256, 512 까지 가능
    int n = 1;
    while(n < arr.size()) n *= 2;
    arr.resize(n, 0);
    
        
    return arr;
}
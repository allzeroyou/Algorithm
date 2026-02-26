#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 2;
    // 제곱근 계산한 값이 정수면 제곱수
    int root = sqrt(n);
    
    if(root*root == n){
        answer = 1;
    }
    
    return answer;
}
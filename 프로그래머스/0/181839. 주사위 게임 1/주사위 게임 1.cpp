#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    // 1. 모두 홀수
    if( (a%2 != 0) && (b%2 != 0) ){
        return a*a + b*b;
    }
    // 2. 둘 중 하나만 홀수라면
    else if((a%2 != 0) || (b%2 != 0)){
        return 2*(a+b);
    }
    // 3. 둘다 홀수 x
    else if((a%2 == 0) && (b%2 == 0)){
        return abs(a-b);
    }
    
    return answer;
}
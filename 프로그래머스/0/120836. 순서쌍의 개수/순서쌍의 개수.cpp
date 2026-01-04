#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    // 곱이 n인 순서쌍으로 표현 가능해야 함
    // n의 약수
    for(int i=1; i*i<=n; i++){ // n의 제곱근까지만 구하기
        if(n%i == 0){ // 약수 라면
            if(i*i == n){ // 제곱수일경우에는 한번만 카운트
                answer += 1;
            }else{
                // 4,5랑 5,4 -> 2개 카운트 필요함
                answer += 2;
            }
        }
    }
    
    return answer;
}
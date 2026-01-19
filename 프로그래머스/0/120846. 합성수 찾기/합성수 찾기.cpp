#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    // 합성수: 약수의 개수가 3개 이상인 수
    // 2, 3의 배수 혹은 제곱수면 무조건 합성수임
    for(int i=1; i<=n; i++){
        // 개수세기
        int cnt = 0;
        
        for(int j=1; j<=i; j++){
            if(i % j == 0)
                cnt ++;            
        }
        // 약수 개수가 3개 이상이어야 함
        if(cnt >= 3)
            answer ++;
    }
    return answer;
}
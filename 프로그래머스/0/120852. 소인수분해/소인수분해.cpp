#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    // 소인수분해
    for(int i=2; i<=n; i++){
        if(n%i == 0){
            answer.push_back(i);
            // n에서 i을 더 이상 나눌 수 없을때까지
            while(n%i == 0){
                n /= i;
            }
        }
    }
    return answer;
}
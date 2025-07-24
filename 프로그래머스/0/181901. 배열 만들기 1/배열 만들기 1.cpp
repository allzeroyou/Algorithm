#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int k) {
    vector<int> answer;
    
    // 1 <= 정수 <= n 중 k의 배수 -> 오름차순 저장
    for(int i=1; i<=n; i++){
        if(i%k==0){
            answer.push_back(i);
        }
    }
    return answer;
}
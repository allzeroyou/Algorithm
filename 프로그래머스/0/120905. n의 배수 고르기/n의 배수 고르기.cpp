#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, vector<int> numlist) {
    vector<int> answer;
    // numlist 에서 n의 배수만 남기기
    for(int num: numlist){
        if(num % n == 0){
            answer.push_back(num);
        }
    }
    
    return answer;
}
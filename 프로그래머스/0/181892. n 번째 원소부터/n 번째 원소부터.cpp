#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list, int n) {
    vector<int> answer;
    
    // 정수리스트 num_list, 정수 n
    // n번째 원소부터 마지막 원소까지 모든 원소 담은 리스트 return
    for(int i=n-1; i<=num_list.size()-1; i++){
        answer.push_back(num_list[i]);
    }
    
    return answer;
}
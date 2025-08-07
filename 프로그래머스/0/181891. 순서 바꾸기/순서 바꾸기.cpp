#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list, int n) {
    vector<int> answer;
    // n번째 이후 원소
    for(int i=n; i<num_list.size(); i++){
        answer.push_back(num_list[i]);
    }
    // ~ n번째 까지 원소
    for(int i=0; i<n; i++){
        answer.push_back(num_list[i]);
    }
    return answer;
}
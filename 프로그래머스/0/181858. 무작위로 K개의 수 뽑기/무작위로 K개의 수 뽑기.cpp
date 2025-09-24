#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer;
    // arr -> 중복 없애고 k개 길이만큼 뽑기?
    // set 에 담기 -> 중복 허용 안함 
    unordered_set<int> used;
    
    for(int a: arr){
        if(used.find(a)==used.end()){ // set 에 없다면
            answer.push_back(a);
            used.insert(a);
        }
        if(answer.size()==k) break; // k개면 종료
    }
    while(answer.size()<k) answer.push_back(-1);
    
    return answer;
}
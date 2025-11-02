#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list, int n) {
    int answer = 0;
    // 정수리스트 num_list, 찾으려는 정수 n
    // num_list에 n이 있으면 1 없음 0 return
    for(int i=0;i<num_list.size(); i++){
        if(num_list[i]==n){
            return 1;
        }
    }
    return answer;
}
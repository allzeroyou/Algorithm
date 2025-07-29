#include <string>
#include <vector>

using namespace std;

int solution(vector<int> arr, int idx) {
    int answer = -1;
    int len = arr.size();

    for(int i=0; i<len; i++){
        if( (i >= idx) && (arr[i] >= 1) ){
            answer = i;
            break; // 가장 작은 인덱스 발견시 종료
        }
    }
    
    return answer;
}
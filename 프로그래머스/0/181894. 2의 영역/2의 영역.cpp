#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    
    // arr 순회하면서 2가 있으면 cnt 증가?
    // 배열의 2가 모두 포함된 가장 작은 연속 부분 배열
    // -> 처음 2가 나온 인덱스부터 증가하면서 마지막 인덱스까지 2를 카운트?
    int flag = 0;
    int firstIdx = -1;
    int lastIdx = -1;
    
    // 첫번째 2와 마지막 2 찾기
    for(int i=0;i<arr.size(); i++){
        if(arr[i]==2){
            if(firstIdx == -1) firstIdx = i;
            lastIdx=i;
        }
    }
    // 2가 하나도 없는 경우
    if(firstIdx == -1){
        answer.push_back(-1);
        return answer;
    }
    // 부분 배열 추출
    answer.insert(answer.end(), arr.begin()+firstIdx, arr.begin()+lastIdx+1);
    return answer;
}
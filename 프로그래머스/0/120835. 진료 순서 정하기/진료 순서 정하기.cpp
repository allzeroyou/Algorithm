#include <string>
#include <vector>
#include <functional> // greater 사용
#include <algorithm> // sort 사용

using namespace std;

vector<int> solution(vector<int> emergency) {
    vector<int> answer;
    // 원본 순서와 비교해야되서 데이터 복사해야함
    vector<int> sorted_v = emergency;
    
    // 내림차순 정렬 후 인덱스+1 순서 반환
    // sort 세번째 인자에 greater<타입> () 전달 시 내림차순으로 정렬됨
    sort(sorted_v.begin(), sorted_v.end(), greater<int>());
    
    // 원본의 각 원소가 정렬된 벡터에서 몇번째 위치에 있는지 찾기
    for(int i=0; i<emergency.size(); i++){
        for(int j=0; j<sorted_v.size(); j++){
            if(emergency[i] == sorted_v[j]){
                answer.push_back(j+1);
                break;
            }
        }
    }
    
    // 출력
    return answer;
}
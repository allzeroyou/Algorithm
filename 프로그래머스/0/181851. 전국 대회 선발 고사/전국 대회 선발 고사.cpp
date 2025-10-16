#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// pair로 등수, 원래 인덱스 쌍 저장
typedef pair<int, int> rankIdxPair;

int solution(vector<int> rank, vector<bool> attendance) {
    int answer = 0;
    // 0번부터 n-1번까지, 3명 뽑음
    // attendance에서 true인 rank[i]에서 상위 3개
    // 등수, 인덱스 쌍 저장
    vector<rankIdxPair> arr;
    for(int i=0; i<attendance.size(); i++){
        if (attendance[i]){
            arr.push_back({rank[i], i});
        }
    }
    // 정렬
    sort(arr.begin(), arr.end());
    // 순서대로 정렬한 등수의 인덱스
    int a = arr[0].second;
    int b = arr[1].second;
    int c = arr[2].second;
    
    // 등수: a b c 
    // 10000*a + 100 * b + c 리턴
    answer = a*10000+ b*100 + c;
    return answer;
}
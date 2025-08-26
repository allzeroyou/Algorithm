#include <string>
#include <vector>

using namespace std;

int solution(vector<int> arr) {
    int answer = 0;
    
    // >= 50 짝수 -> 2로 나누기
    // < 50 홀수 -> *2 + 1
    while(true){
        vector<int> prev = arr;
        
        // 배열 변환
        for(int i=0; i<arr.size(); i++){
            if(arr[i]<50 && arr[i]%2 == 1){
                arr[i]=arr[i]*2+1;
            }
            else if(arr[i]>=50 && arr[i]%2 == 0){
                arr[i]= arr[i]/2;
            }
        }
        // 변화 없음 종료
        if(prev == arr) break;
        answer ++;
        
    }

    
    
    
    return answer;
}
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> arr1, vector<int> arr2) {
    int answer = 0;
    
    // 배열 길이가 다르다면 길이가 더 긴 쪽이 더 큼.
    if(arr1.size() != arr2.size()){
        if(arr1.size() > arr2.size()){
            return 1;
        }else{
            return -1;
        }
    }else{ 
        // 배열 길이가 같다면 각 배열 원소 합 비교 -> 다르다면 더 큰쪽이 크고, 같다면 같음
        int sum1 = 0;
        int sum2 = 0;
        for(int a: arr1) sum1 += a;
        for(int a2: arr2) sum2 += a2;
        
        if (sum1 > sum2){
            answer = 1;
        } else if(sum1 < sum2){
            answer = -1;
        }
    }
    // arr2가 크다면 -1
    // arr1가 크다면 1
    
    // 같으면 0 return
    return answer;
}
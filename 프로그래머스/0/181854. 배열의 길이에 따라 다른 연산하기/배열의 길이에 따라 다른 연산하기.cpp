#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int n) {
    vector<int> answer;
    // arr 길이: 홀수 -> arr 짝수 인덱스에 n 더한 배열
    if(arr.size()%2 != 0){
        for(int i=0; i<arr.size(); i+=2){
            arr[i]+=n;
        }
    }else{
    // arr 길이: 짝수 -> arr 홀수 인덱스에 n 더한 배열
        for(int i=1; i<arr.size(); i+=2)
            arr[i]+=n;
    }
    
    return arr;
}
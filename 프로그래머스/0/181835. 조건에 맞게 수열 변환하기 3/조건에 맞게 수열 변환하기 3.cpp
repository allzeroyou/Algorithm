#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer;
    // k가 홀수 -> arr 모든 원소에 k 곱하기
    // k가 짝수 -> arr 모든 원소에 k 더하기
    if(k%2 == 0)
    {
        for(int i=0; i<arr.size(); i++)
        {
            arr[i]+=k;
        }
    }else{
        for(int i=0; i<arr.size(); i++)
        {
            arr[i]*=k;
        }
    }
    return arr;
}
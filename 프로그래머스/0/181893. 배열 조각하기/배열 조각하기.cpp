#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<int> query) {
    vector<int> answer;
    
    // query 짝수인덱스 -> 해당 요소 제외, 배열의 query[i]번 인덱스 뒷부분 자름
    int idx = 0;
    
    for(int i =0; i<query.size(); i++){
        if(i % 2 == 0){
            arr = vector<int>(arr.begin(), arr.begin()+query[i]+1);
        }else{
            arr = vector<int>(arr.begin()+query[i], arr.end());        
        }
    }

    return arr;
}
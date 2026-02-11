#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array) {
    vector<int> answer;
    // 가장 큰 수, 그 수의 인덱스 담은 배열 return
    int max_num = array[0];
    int max_idx = 0;
    for(int i=0; i<array.size(); i++){
        if(array[i] > max_num){
            max_num = array[i];
            max_idx = i;
        }
    }
    answer.push_back(max_num);
    answer.push_back(max_idx);
    
    return answer;
}